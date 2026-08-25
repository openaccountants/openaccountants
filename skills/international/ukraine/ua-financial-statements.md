---
name: ua-financial-statements
description: Use this skill whenever asked about Ukrainian financial statements and financial reporting (фінансова звітність) for legal entities, or whether a self-employed person must prepare them. Trigger on phrases like "Ukraine financial statements", "фінансова звітність", "П(С)БО", "НП(С)БО", "IFRS Ukraine", "МСФЗ", "do I file accounts as a FOP", "balance sheet Ukraine", "звіт про фінансові результати", "Форма 1-м", "Форма 1-мс", "enterprise size category Ukraine", "micro small medium large enterprise Ukraine", "statutory audit Ukraine", "Держстат financial report", "ТОВ financial statements", or any question about who must prepare and file financial statements, which accounting standards apply, the simplified report forms, deadlines, or audit obligations. This skill is about FORMAL FINANCIAL STATEMENTS for legal entities. A FOP (sole proprietor) does NOT prepare these — defer FOP records to ua-bookkeeping and FOP tax to ua-single-tax / ua-income-tax. ALWAYS read this skill before any Ukrainian financial-statement or financial-reporting work.
version: 1.0
jurisdiction: UA
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UA Financial Statements

## Ukraine Financial Statements & Financial Reporting — Self-Employed Skill v1.0

This skill explains who in Ukraine must prepare **formal financial statements** (фінансова звітність), which accounting standards apply (national П(С)БО / НП(С)БО vs international МСФЗ / IFRS), the enterprise size categories that drive the report form, where statements are filed, the deadlines, and statutory audit obligations.

**The headline for a self-employed reader:** a Ukrainian sole proprietor — **ФОП** (фізична особа-підприємець) — does **NOT** prepare formal financial statements at all. A ФОП keeps income / income-and-expense ledgers and files a single-tax or property-and-income (general-system) declaration. Formal financial statements are an obligation of **legal entities** (юридичні особи) — a **ТОВ** (товариство з обмеженою відповідальністю / limited liability company) and similar. This skill tells the self-employed reader exactly where that line sits and what changes if they incorporate a ТОВ.

For ФОП record-keeping read **ua-bookkeeping**; for single-tax groups, rates and limits read **ua-single-tax**; for general-system personal income tax read **ua-income-tax**; for VAT read **ukraine-vat**.

## Section 1 — Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Ukraine |
| Who prepares | **Legal entities** (юридичні особи — ТОВ, АТ, etc.) and representative offices of non-residents. **ФОП / sole proprietors do NOT** prepare financial statements. |
| Standards | **П(С)БО / НП(С)БО** (National Accounting Standards) for most companies; **МСФЗ / IFRS** mandatory for banks, public-interest entities (PIEs), large enterprises, securities issuers and mineral extractors — see Section 4 |
| Currency | UAH (₴) — statements are presented in thousands of hryvnia |
| Primary legislation | Law of Ukraine **№996-XIV** "On Accounting and Financial Reporting in Ukraine" (Про бухгалтерський облік та фінансову звітність в Україні); **НП(С)БО 1** (general-purpose statements); **НП(С)БО 25** (simplified statements for micro/small); Law **№2258-VIII** "On audit of financial statements and auditing activity" |
| Authorities | **ДПС** (Державна податкова служба / State Tax Service) and **Держстат** (Державна служба статистики / State Statistics Service) |
| Filing deadlines | Annual statements: file with **ДПС by 1 March** and with **Держстat by 28 February** of the year following the reporting year; PIEs/issuers/extractors **publish by 30 April**; large & medium enterprises **publish by 1 June** (see Section 3) |
| Contributor | Open Accountants Community |
| Quality tier | Research-verified — pending sign-off by a Ukrainian accountant |
| Skill version | 1.0 |

- **Reporting period** — The financial year in Ukraine is the calendar year (1 January – 31 December). Figures, forms and thresholds are stated as of May 2026 for the 2025 reporting year filed in 2026.
- **Threshold currency caveat** — The size thresholds in this skill are expressed in EUR in §996-XIV. They are applied by converting the EUR figures to UAH at the NBU rate at the balance sheet date (31 December). Always recompute with the current rate.  _(§996-XIV)_

### Conservative defaults

When inputs are ambiguous, default to the more cautious reporting posture:

1. **A ФОП files no financial statements — but confirm the legal form first.** If the client says "my company" or "ТОВ", they are a legal entity and this skill applies. If they are a ФОП, redirect to ua-bookkeeping / ua-single-tax and do not produce a balance sheet.
2. **Default a new/unknown legal entity to "small enterprise"** reporting (full НП(С)БО 1 set or simplified Форма 1-м/2-м) unless figures clearly place it in micro or in medium/large. Never default a company *down* into micro and skip required disclosures.
3. **When size sits near a threshold, classify by two-of-three over the prior year**, and treat the higher category as the safe assumption pending confirmed figures.
4. **Assume an audit may be required** for any medium or large entity, PIE or securities issuer until proven otherwise (Section 5). Do not state "no audit needed" without checking all criteria.
5. **Use only the IFRS Ukrainian translation published by the Ministry of Finance** where IFRS applies — statutory statements must rely on the official translation, not the IASB English text.
6. **Flag, don't guess.** If the legal form, prior-year size indicators, or PIE status are unknown, ask. State assumptions explicitly in any draft.

## Section 2 — FOP vs Legal Entity: What Each Files

This is the core distinction. Get it wrong and you either burden a sole proprietor with company obligations they do not have, or you let a ТОВ skip statutory statements.

### A sole proprietor (ФОП / фізична особа-підприємець)

- **ФОП does not prepare financial statements** — Does NOT prepare financial statements. There is no balance sheet, no profit-and-loss statement, no Держстат financial report for a ФОП. The Law §996-XIV applies to legal entities, not to individuals registered as entrepreneurs.  _(§996-XIV)_
- **Simplified records kept instead** — Keeps simplified records instead: an income ledger (Книга обліку доходів) or income-and-expense ledger, plus primary documents. See ua-bookkeeping.
- **Files a tax declaration, not accounts** — Single-tax groups 1–2: annual single-tax declaration (декларація платника єдиного податку). Single-tax group 3: quarterly single-tax declaration. General system: annual property-and-income declaration (податкова декларація про майновий стан і доходи). See ua-single-tax and ua-income-tax for which regime and the figures.
- **VAT and ЄСВ obligations remain tax filings, not financial statements** — A ФОП may still owe VAT returns if VAT-registered (see ukraine-vat) and ЄСВ / unified social contribution — but these are tax filings, not financial statements.

### A legal entity (юридична особа — e.g. ТОВ)

- **Legal entity must keep double-entry accounting and prepare financial statements** — MUST keep double-entry accounting and prepare financial statements under §996-XIV from the date of state registration.  _(§996-XIV)_
- **НП(С)БО 1 standard general-purpose set** — 1. Баланс (Звіт про фінансовий стан) — Balance Sheet / Statement of Financial Position (Форма №1) 2. Звіт про фінансові результати (Звіт про сукупний дохід) — Statement of Financial Results / Comprehensive Income (Форма №2) 3. Звіт про рух грошових коштів — Statement of Cash Flows (Форма №3) 4. Звіт про власний капітал — Statement of Changes in Equity (Форма №4) 5. Примітки до фінансової звітності — Notes to the financial statements (Форма №5)  _(НП(С)БО 1)_
- **Micro/small reduced set** — Micro and small enterprises file a reduced set (see Section 3).
- **Management report requirement** — Medium and large enterprises also prepare a management report (звіт про управління), and large enterprises/PIEs additional disclosures.
- **Filing authorities** — Files annually with ДПС (usually together with the corporate income tax return / податок на прибуток) and with Держстат; medium/large/PIEs also publish.

**"If I incorporate a ТОВ, what changes?"** Everything in the table above flips on. You move from a ledger + single-tax declaration to double-entry bookkeeping, a full or simplified set of financial statements under П(С)БО (or IFRS if you fall into a mandatory category), filing with both ДПС and Держстат, and — if you grow into the medium/large/PIE brackets — a statutory audit. Many small ТОВ keep simplified Форма 1-м/2-м statements and never need an audit; the burden scales with size.

## Section 3 — Enterprise Size Categories and Which Report Form

Under Article 2 of Law §996-XIV, every legal entity falls into one of four size categories. A company belongs to a category if, at the balance sheet date, it meets at least two of the three criteria for that category. Categories are re-tested each year using the prior year's indicators.

### Size criteria (§996-XIV, EUR thresholds applied at the NBU rate at 31 December)

**Size criteria table**  _(§996-XIV)_

| Category | Balance-sheet assets | Net revenue | Average headcount |
| --- | --- | --- | --- |
| **Micro** (мікропідприємство) | up to **€350,000** | up to **€700,000** | up to **10** |
| **Small** (мале) | up to **€4,000,000** | up to **€8,000,000** | up to **50** |
| **Medium** (середнє) | up to **€20,000,000** | up to **€40,000,000** | up to **250** |
| **Large** (велике) | over **€20,000,000** | over **€40,000,000** | over **250** |

- **Uncertain — two competing threshold sets** — ⚠ UNCERTAIN — two competing threshold sets. Law №4196-IX (9 January 2025) introduced EU-aligned size criteria (Commission Recommendation 2003/361/EC): broadly micro ≈ ≤9 staff and ≤€2m, small ≈ ≤49 staff and ≤€10m, medium ≈ ≤249 staff and ≤€50m revenue / ≤€43m assets. There is genuine ambiguity in mid-2026 sources about which set governs the accounting/financial-reporting form and audit versus general SME-status classification. The €350k/€700k/€4m/€8m/€20m/€40m set above is the one historically embedded in §996-XIV for financial-reporting purposes; the №4196-IX set harmonises enterprise classification with EU law. Verify the operative thresholds for the specific 2025 reporting year against the current consolidated text of §996-XIV before classifying — do not rely on these figures unchecked. Flag this to the reviewer.  _(Law №4196-IX (9 January 2025); §996-XIV; Commission Recommendation 2003/361/EC)_

### Which report form by category

**Which report form by category table**

| Category | Standard | Statement set / form |
| --- | --- | --- |
| **Micro** | НП(С)БО 25 | **Скорочена** (simplified): **Форма №1-мс** (Balance) + **Форма №2-мс** (Financial Results) — a single condensed Balance + Financial Results report. May voluntarily use Форма 1-м/2-м or the full set. |
| **Small** | НП(С)БО 25 | **Малий** simplified set: **Форма №1-м** (Balance) + **Форма №2-м** (Financial Results). |
| **Medium** | НП(С)БО 1 (or IFRS if a PIE/large) | **Full** set: Форми №1–№5 + **management report** (звіт про управління). |
| **Large** | **МСФЗ / IFRS (mandatory)** | **Full** set: Форми №1–№5 + management report + additional disclosures; PIEs add a payments-to-government / non-financial statement where applicable. |

Notes:
- **Форма 1-мс / 2-мс** (micro) and **Форма 1-м / 2-м** (small) are the simplified statements under НП(С)БО 25. Form 2-мс reports for the reporting year rather than at a date; Form 1-мс is the condensed Balance.
- Since 17 February 2023, certain single-tax group-3 legal entities on simplified accounting may choose between the 1-мс/2-мс and the 1-м/2-м forms.
- A micro or small company may always voluntarily prepare a fuller set (e.g. for lenders).
- Form selection follows the size category, not the tax regime, except where the simplified-accounting election expands the menu of permitted forms.

## Section 4 — П(С)БО / НП(С)БО vs IFRS (МСФЗ)

Ukraine runs two parallel reporting frameworks. The default is national standards; IFRS is mandatory for a defined list of higher-stakes entities.

### National Accounting Standards — П(С)БО / НП(С)БО

- **П(С)БО / НП(С)БО terminology and scope** — "П(С)БО" (Положення (стандарти) бухгалтерського обліку) is the long-standing label; newer/updated standards are issued as "НП(С)БО" (Національні положення (стандарти) бухгалтерського обліку). In practice the two terms are used interchangeably.
- **Maintained by Ministry of Finance** — Set and maintained by the Ministry of Finance of Ukraine (Мінфін).
- **НП(С)БО 1 and НП(С)БО 25 scope** — НП(С)БО 1 governs the general-purpose statements (Forms 1–5); НП(С)БО 25 governs the simplified micro/small statements (Forms 1-мс/2-мс and 1-м/2-м). This is the default framework for companies that are not in a mandatory-IFRS category.  _(НП(С)БО 1; НП(С)БО 25)_

### International Financial Reporting Standards — МСФЗ / IFRS

- **Entities for which IFRS is mandatory** — IFRS (Міжнародні стандарти фінансової звітності) is mandatory for the following entities under §996-XIV: Banks (since 2011). Public-interest entities (PIEs / підприємства, що становлять суспільний інтерес): securities issuers whose securities are admitted to trading on a stock exchange; banks; insurers; non-state pension funds; other financial institutions (except those that are micro/small); and entities that qualify as large enterprises. Public joint-stock companies (публічні акціонерні товариства). Large enterprises (per the size criteria in Section 3). Enterprises engaged in extraction of minerals of national importance. Securities issuers and parent companies of PIE groups preparing consolidated statements.  _(§996-XIV)_
- **Voluntary IFRS adoption and XBRL filing** — Other companies — including most ТОВ, micro and small entities — use П(С)БО, but any company may voluntarily adopt IFRS. Entities that fall into a mandatory-IFRS category and most others file financial statements electronically in XBRL/iXBRL taxonomy format via the single-window financial-reporting system.
- **Statutory translation rule** — Where IFRS applies, statutory statements must use the Ukrainian translation of IFRS published by the Ministry of Finance, not the IASB English original.

## Section 5 — Statutory Audit Requirements

- **Entities requiring mandatory statutory audit** — Mandatory statutory audit (обов'язковий аудит фінансової звітності) is governed by Law №2258-VIII. A statutory audit of the annual financial statements is required for: Public-interest entities (PIEs) — banks, insurers, non-state pension funds, other financial institutions (other than micro/small), exchange-traded securities issuers, and entities classified as large. Large enterprises. Medium-sized enterprises. Public joint-stock companies. Securities issuers whose securities are admitted to exchange trading or are publicly offered. Subjects of natural monopolies on the national market. Enterprises engaged in extraction of minerals of national importance.  _(Law №2258-VIII)_
- **Micro and small generally not subject to mandatory audit** — Micro and small enterprises are generally NOT subject to mandatory audit (a financial institution that is micro/small is treated as the relevant exception case — verify per entity).
- **Additional PIE audit rules** — For PIEs, the auditor must be on the relevant register and PIE audits follow a public tender with the auditor approved by the company's highest governing body; rotation rules apply. Audit must apply the International Standards on Auditing (ISA / МСА) in the Ukrainian translation published by the Ministry of Finance.
- **Verify medium-enterprise audit trigger** — ⚠ Verify the precise medium-enterprise audit trigger against the current consolidated text of §2258-VIII for the 2025 reporting year, especially given the threshold changes flagged in Section 3. The category that triggers audit (medium/large) depends on which size-threshold set is operative. Flag to the reviewer.  _(§2258-VIII)_

## Section 6 — Worked Examples

These illustrate the decision flow. They are method demonstrations, not filed returns; every output requires reviewer sign-off and confirmation of operative thresholds.

### Example 1 — A freelance developer asks "do I file accounts?"

**Facts.** Oksana is a ФОП, single-tax group 3, freelance software development, ~₴2.5m income in 2025, no employees.

**Analysis.**
- Oksana is an individual entrepreneur (ФОП), not a legal entity. §996-XIV does not apply to her.
- She prepares NO financial statements — no Balance, no Звіт про фінансові результати, no Держстат financial report.
- Her obligations: keep an income ledger (ua-bookkeeping) and file the quarterly single-tax declaration (ua-single-tax). She also pays ЄСВ and the military levy.

**Result.** No financial statements. Redirect to ua-bookkeeping and ua-single-tax. (If she had been asked whether to incorporate a ТОВ, Section 2's "what changes" note applies.)

### Example 2 — A small ТОВ's first year

**Facts.** A newly registered ТОВ, design agency, year-end 31 Dec 2025: assets ≈ €120,000, net revenue ≈ €410,000, average headcount 6.

**Analysis.**
- A legal entity → §996-XIV applies; double-entry accounting and financial statements required.
- Size test (two-of-three): assets €120k ≤ €350k ✓, revenue €410k ≤ €700k ✓, headcount 6 ≤ 10 ✓ — meets all three micro criteria → micro-enterprise (under the §996-XIV set; re-check against the №4196-IX set per Section 3).
- Standard: НП(С)БО 25 → simplified Форма №1-мс + №2-мс.
- Audit: micro → no mandatory audit.
- Standards framework: П(С)БО (not IFRS).

**Result.** Files condensed Форма 1-мс/2-мс with ДПС by 1 March 2026 and Держстат by 28 February 2026. No audit. No publication requirement. *Flag the threshold uncertainty to the reviewer.*

### Example 3 — A growing ТОВ crosses into "medium"

**Facts.** A logistics ТОВ, year-end 31 Dec 2025: assets ≈ €9m, net revenue ≈ €22m, average headcount 180. Not a financial institution, not a securities issuer.

**Analysis.**
- Legal entity → statements required.
- Size test against §996-XIV: assets €9m (≤ €20m, > €4m), revenue €22m (≤ €40m, > €8m), headcount 180 (≤ 250, > 50) — exceeds small on at least two criteria and sits within medium → medium enterprise (re-confirm under the operative threshold set — Section 3).
- Standard: НП(С)БО 1 full set (Форми №1–№5) plus a management report (звіт про управління). Not in a mandatory-IFRS category, so П(С)БО unless it elects IFRS.
- Audit: medium enterprise → mandatory statutory audit under §2258-VIII (subject to the Section 5 verification note).

**Result.** Full НП(С)БО 1 statements + management report, audited, filed with ДПС by 1 March and Держстат by 28 February, with publication by 1 June 2026. *Flag both the size-threshold and the medium-audit-trigger uncertainty to the reviewer.*

## Section 7 — Tier 2 Notes & References

**Tier 2 — practitioner notes (require care and reviewer confirmation):**

- **Threshold conflict (highest priority).** The §996-XIV financial-reporting thresholds and the №4196-IX EU-aligned SME thresholds differ. Confirm which governs the report form and the audit trigger for the 2025 reporting year before classifying. This single point drives form choice and audit obligation.
- **EUR→UAH conversion.** Apply the NBU rate at the balance sheet date (31 Dec). A company near a boundary can change category purely from FX movement — document the rate used.
- **Two-of-three, prior year.** Category is set by meeting two of three criteria, tested on the prior year's indicators; a company changes category only after the threshold is met, applied the following year.
- **Wartime / martial-law caveats.** Filing mechanics, publication, and some deadlines have been affected by martial-law measures since 2022. Verify current-year deadlines and any extensions on the ДПС and Держстат portals before relying on the dates in this skill.
- **XBRL.** PIEs and many entities file via the iXBRL single-window financial-reporting system; taxonomy versions change annually.
- **Consolidated statements** for groups and PIE-specific disclosures are out of scope here — escalate to a credentialed Ukrainian auditor.

**Primary references (web-verified, May 2026):**

- Law of Ukraine №996-XIV "On Accounting and Financial Reporting in Ukraine" (Про бухгалтерський облік та фінансову звітність в Україні).
- Law of Ukraine №2258-VIII "On audit of financial statements and auditing activity".
- Law of Ukraine №4196-IX (09.01.2025) — EU-aligned SME classification criteria.
- НП(С)БО 1 (general-purpose statements); НП(С)БО 25 (simplified micro/small statements).
- ДПС (tax.gov.ua) and Держстат (ukrstat.gov.ua) official guidance.
- Big-4 / mid-tier summaries: Forvis Mazars, Crowe, PwC, BDO, KPMG (Ukraine).
- IFRS Foundation jurisdiction profile — Ukraine; IAS Plus (Deloitte) Ukraine.

## PROHIBITIONS

- **Prohibited uses of this skill** — This skill must NOT be used to: 1. Prepare or imply that a ФОП (sole proprietor) files formal financial statements. A ФОП files tax declarations and keeps ledgers only. Never produce a Balance Sheet or Держстат financial report for an individual entrepreneur. 2. Assert a definitive size category or audit conclusion without verifying the operative thresholds for the reporting year, given the §996-XIV vs №4196-IX conflict (Sections 3 and 5). 3. State "no audit required" for a medium, large, PIE or securities-issuer entity without checking every criterion in Section 5. 4. Apply IFRS to entities not in a mandatory-IFRS category as if compulsory, or apply national П(С)БО to a bank, PIE, large enterprise or other mandatory-IFRS entity. 5. Use the IASB English IFRS text for statutory statements where the Ministry of Finance Ukrainian translation is required. 6. Quote deadlines as fixed without checking ДПС / Держстат for current-year and martial-law adjustments. 7. Sign off, file, or submit statements, or replace a credentialed Ukrainian accountant or auditor. This skill produces drafts and analysis for review only. 8. Advise on consolidated statements, group reporting, PIE-specific or sector-specific (banking, insurance) disclosures — escalate to a qualified Ukrainian auditor.

## Disclaimer

This skill is research-verified open-source content contributed by the Open Accountants Community. It was prepared from public sources (Law of Ukraine №996-XIV and №2258-VIII, НП(С)БО 1 and 25, ДПС and Держстат guidance, and Big-4 / mid-tier commentary) as of May 2026 for the 2026 filing of the 2025 reporting year. Several thresholds — in particular the enterprise size criteria and the medium-enterprise audit trigger — are in transition between the §996-XIV figures and the EU-aligned №4196-IX criteria and are explicitly flagged as uncertain.

It is not legal, accounting or tax advice and does not substitute for sign-off by a qualified Ukrainian accountant or auditor. Ukrainian financial-reporting law, standards, forms, deadlines and martial-law measures change; verify against the current consolidated legislation and the ДПС / Держstat portals before relying on any figure. Every output produced with this skill must be reviewed and signed off by a credentialed professional before filing.

Part of openaccountants.com — open-source tax skills for the self-employed.

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
