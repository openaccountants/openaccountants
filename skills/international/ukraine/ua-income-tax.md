---
name: ua-income-tax
description: "Ukrainian general-system (загальна система) personal income tax for a self-employed sole proprietor (ФОП): net business profit taxed at 18% PIT plus the 5% military levy with documented business expenses deductible under Art. 177."
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

# UA Income Tax

## Ukraine General-System Personal Income Tax (ПДФО for FOP / Загальна система) — Self-Employed Skill v1.0

This skill covers a Ukrainian sole proprietor (ФОП / фізична особа-підприємець) taxed on the general system — net business profit taxed at 18% personal income tax (ПДФО) plus a 5% military levy (військовий збір), with documented business expenses deductible. This is fundamentally different from the simplified єдиний податок (turnover-based, no expense deduction) — for that, use ua-single-tax. Unified social contribution (ЄСВ) is handled by ua-social-contributions and only referenced here.

## Section 1 — Quick Reference

**Quick Reference Table**

| Field | Value |
| --- | --- |
| Country | Ukraine |
| Regime | Загальна система оподаткування (General taxation system) for ФОП |
| Tax | ПДФО (personal income tax) + військовий збір (military levy) on net business profit |
| Taxpayer | ФОП (фізична особа-підприємець) — self-employed sole proprietor, Ukrainian resident |
| Currency | UAH (₴) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Primary legislation | Tax Code of Ukraine (Податковий кодекс України) — Art. 177 (FOP general system), Section IV (ПДФО), Art. 16¹ subsection 10 of the Transitional Provisions (military levy) |
| Tax authority | Державна податкова служба України (ДПС / State Tax Service) |
| Filing portal | Електронний кабінет платника (cabinet.tax.gov.ua) |
| Annual return | Декларація про майновий стан і доходи (property status & income declaration) |
| Filing deadline | By **1 May** of the year following the reporting year (e.g. 2026 income → by 1 May 2027) |
| Final tax payment | Within **10 calendar days** after the declaration filing deadline |
| PIT advance payments | By **20 April, 20 July, 20 October** (no Q4 advance — settled in the declaration) |
| Contributor | Open Accountants Community |
| Quality tier | Research-verified — pending sign-off by a Ukrainian accountant/auditor |
| Skill version | 1.0 |

**Wartime note:** Under martial law the military levy rose from 1.5% to **5%** effective **1 Dec 2024** and remains 5% throughout **2026**. It reverts to 1.5% in the year **after** martial law ends — verify the current status with the ДПС before relying on the rate. Figures below are as of **1 January 2026**.

### Rate table (general system, 2026)

**Rate table (general system, 2026)**  _(Art. 177; Tax Code §16¹.10 Transitional Provisions; Art. 181 ПКУ)_

| Component | Rate | Base |
| --- | --- | --- |
| ПДФО (personal income tax) | **18%** | Net taxable profit = income − documented allowable expenses |
| Військовий збір (military levy) | **5%** | Same net profit base; computed under Art. 177 rules (Tax Code §16¹.10 Transitional Provisions) |
| **Combined income-tax burden** | **23%** | of net profit |
| ЄСВ (unified social contribution) | 22% of net profit, min 22% of min. wage | See **ua-social-contributions** |
| VAT (ПДВ) | 20% standard | Mandatory registration if 12-month turnover > ₴1,000,000 — see **ukraine-vat** |

### Key 2026 amounts (as of 1 Jan 2026; verify current values)

**Key 2026 amounts**  _(Art. 177.4.6 ПКУ; Art. 181 ПКУ)_

| Item | Value | Note |
| --- | --- | --- |
| Minimum wage (мінімальна зарплата) | ₴8,647 / month | Set 1 Jan 2026 |
| Living wage, working-age (прожитковий мінімум) | ₴3,328 / month | Set 1 Jan 2026 |
| ЄСВ minimum | ₴1,902.34 / month (22% × ₴8,647) | See ua-social-contributions |
| ЄСВ maximum monthly base | 20 × min. wage = ₴172,940 | Cap on the 22% base |
| Asset threshold for "fixed asset" (ОЗ) | > ₴20,000 and useful life ≥ 1 year | Art. 177.4.6 ПКУ; below = expensed immediately |
| VAT registration threshold | ₴1,000,000 turnover / 12 months | Art. 181 ПКУ |

### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Regime not stated, but expenses are claimed / income exceeds single-tax cap | General system (this skill) |
| Regime not stated, freelancer with low costs | Likely single tax → route to ua-single-tax and confirm |
| Expense lacks a supporting document | NOT deductible — exclude and flag |
| Personal-vs-business split unclear | Treat as non-deductible (personal) unless a documented business apportionment exists |
| Fixed asset vs immediate expense unclear | If cost > ₴20,000 and life ≥ 1 yr → capitalise & depreciate (straight-line); else expense |
| Foreign-currency receipt date | NBU rate on the date funds are received (cash basis) |
| Military levy rate | 5% (martial law in force in 2026) — verify before filing |
| Whether ЄСВ applies | Assume YES; minimum ₴1,902.34/month even at a loss — confirm in ua-social-contributions |

## Section 2 — Required Inputs and Refusal Catalogue

### Required inputs

- **Required inputs** — Minimum: confirmation the FOP is on the general system; full-year bank statements for all business accounts (UAH and FX); list of business expenses with supporting documents. Recommended: Книга обліку доходів і витрат (income & expense ledger), registration extract (виписка з ЄДР) with КВЕД activity codes, prior-year declaration, ЄСВ payment history, fixed-asset register. Ideal: all primary documents (invoices/акти, видаткові накладні, bank confirmations, FX conversion records at NBU rate), depreciation schedule, evidence of advance payments made.

### Refusal catalogue

- **R-UA-1 — Company / legal entity (ТОВ, ПП)** — This skill is for an individual ФОП on the general system only. A company pays corporate income tax (податок на прибуток підприємств, 18%) under different rules. Escalate / route to a corporate skill.
- **R-UA-2 — Non-resident** — General-system ФОП taxation here assumes a Ukrainian tax resident. Non-residents have different rules and registration constraints. Escalate.
- **R-UA-3 — Employment / civil-contract income only** — Salary, gig income paid by an employer/agent under PAYE-style withholding, and ordinary citizen income (not entrepreneurial) are taxed differently (withheld at source or via the personal declaration as non-business income). Out of scope for the FOP business-profit computation. Route to a personal-income skill.
- **R-UA-4 — Independent professional (особа, яка провадить незалежну професійну діяльність)** — Notaries, lawyers, arbitration managers, etc. (Art. 178 ПКУ) are taxed similarly but under a separate article with their own nuances. Flag — do not silently apply Art. 177.  _(Art. 178 ПКУ)_
- **R-UA-5 — Single-tax (єдиний податок) payer** — Turnover-based, no expense deduction. Wrong skill → route to ua-single-tax.
- **R-UA-6 — Excisable / restricted activity questions, gambling, financial intermediation** — May require special licensing/excise treatment beyond ПДФО. Flag for a specialist.

## Section 3 — Transaction Pattern Library

Cash basis: income is recognised when funds are received; an expense is deductible only when paid AND documented AND the related income is received (matching under Art. 177.2/177.4). Ukrainian + English keywords below are indicative — confirm against the underlying document.

### Income patterns (taxable revenue)

**Income patterns (taxable revenue)**

| Bank-statement keyword (UA / EN) | Treatment |
| --- | --- |
| "оплата за послуги", "за виконані роботи", "payment for services", "invoice 123" | Business income — include in revenue |
| "аванс за товар/послуги", "advance / prepayment" | Income on receipt (cash basis) — include |
| "надходження від клієнта", "from client", PayPal/Wise/Payoneer settlement to FOP account | Business income — convert FX at NBU rate on receipt date |
| "експортна виручка", "export proceeds", USD/EUR inflow | Foreign business income — include at NBU rate on receipt |
| "повернення переплати від постачальника" (supplier refund of overpayment) | Reduces the related expense, not income — net off |

### Deductible expense patterns (documented business expenses — Art. 177.4)

**Deductible expense patterns (documented business expenses — Art. 177.4)**  _(Art. 177.4)_

| Bank-statement keyword (UA / EN) | Treatment |
| --- | --- |
| "закупівля товару/сировини", "за матеріали", "purchase of goods / raw materials" | Cost of goods/materials — deductible **only against income from their sale** (Art. 177.4.1) |
| "оренда офісу/приміщення", "rent", "оренда обладнання" | Rent of premises/equipment used in business — deductible |
| "комунальні послуги" (utilities, business premises) | Deductible to the business-use extent |
| "зарплата найманим", "ЄСВ за працівників", "wages / payroll / USC on employees" | Wages and the employer ЄСВ on employees — deductible (Art. 177.4.2) |
| "послуги зв'язку / інтернет", "telecom / internet" | Deductible if business-related |
| "банківські комісії", "РКО", "bank service fees" | Deductible bank charges |
| "транспортні / логістика / доставка", "freight / delivery" | Deductible if business-related |
| "придбання ОЗ" > ₴20,000 (fixed asset purchase) | **Capitalise & depreciate** straight-line (Art. 177.4.6–.7) — NOT a full immediate expense |
| "ремонт обладнання (поточний)", "current repair" | Current repairs deductible immediately; improvements/modernisation are capitalised |
| "обов'язкове страхування", "mandatory insurance" of business assets | Deductible (mandatory insurance only) |
| "сплата єдиного внеску ФОП за себе" (own ЄСВ) | Deductible as a business expense per Art. 177.4 sub-rules (own ЄСВ) — confirm current ДПС position |

### Non-deductible patterns (exclude from expenses)

**Non-deductible patterns (exclude from expenses)**

| Pattern | Why |
| --- | --- |
| Expense with **no supporting document** (act/invoice/receipt) | Not deductible — documentation is mandatory (Art. 177.4) |
| Personal / household spending, family, groceries, personal car for private use | Not business-related |
| Purchase of land, residential real estate (Art. 177.4.5 exclusions) | Excluded from FOP expenses |
| ПДФО, military levy, and the FOP's own income tax payments | Taxes on profit are not deductible against profit |
| Fines, penalties, late-payment interest (penya) | Not deductible |
| Cost of goods still in inventory / not yet sold | Deductible only in the period the matching income is received |
| Dividends, gifts, charitable transfers (unless within allowed limits) | Not a business expense |

### Internal transfers / exclusions (not income, not expense)

**Internal transfers / exclusions (not income, not expense)**

| Pattern | Treatment |
| --- | --- |
| Transfer between the FOP's own accounts ("переказ між власними рахунками") | Internal — exclude both legs |
| Withdrawal of own funds for personal use ("на власні потреби", "self-transfer to personal card") | Not an expense — owner drawing; exclude |
| Loan principal received / repaid ("кредит", "позика", "тіло кредиту") | Financing, not income/expense — exclude principal (interest may be deductible if business) |
| FX conversion between own accounts | Exclude; record only the UAH value of the underlying receipt |
| VAT collected/paid (if VAT-registered) | Handled in the VAT return, not in the profit computation — see ukraine-vat |

## Section 4 — Worked Examples

Receives USD 50,000 over the year (NBU rates on each receipt average ≈ ₴41.5 → ₴2,075,000 income). Documented expenses: subcontractor акти ₴400,000, software subscriptions ₴60,000, rent ₴120,000, bank fees ₴15,000, own ЄСВ ₴22,828. Net profit ≈ 2,075,000 − 617,828 = **₴1,457,172**. ПДФО 18% = ₴262,291; military levy 5% = ₴72,859. Combined income tax ≈ **₴335,150** (plus ЄСВ separately). Note: turnover ₴2.075m exceeds ₴1m → check mandatory VAT registration (ukraine-vat).

Buys goods for ₴300,000 in December 2025, sells half in 2025 and half in 2026. Only the cost of goods actually sold in 2025 (₴150,000) is deductible against 2025 income; the remaining ₴150,000 is deductible in 2026 when the matching sale revenue is received (Art. 177.4.1 matching rule).

Income ₴200,000; documented expenses ₴260,000 → negative result. No ПДФО and no military levy on business profit (there is no positive base). ЄСВ is still due at the minimum ₴1,902.34/month (₴22,828.08/year) regardless of the loss (see ua-social-contributions). A negative result does not carry forward as a deduction to the next year for FOPs.

Buys a laptop for ₴45,000 (> ₴20,000, useful life ≥ 1 yr). Not a full immediate expense. Capitalise and depreciate straight-line over its useful life (e.g. 2 years → ₴22,500/year) per Art. 177.4.6–.7. A ₴12,000 phone (< ₴20,000) is expensed immediately as a low-value item (МНМА).

A FOP self-calculates PIT advances from actual H1 results: pays by 20 April (Q1), 20 July (Q2), 20 October (Q3). The military levy and the Q4 portion are settled in the annual declaration. Final reconciliation (top-up) is paid within 10 days after the 1 May filing deadline.

Fuel and maintenance for a car used 70% business / 30% personal: only the business portion is deductible, and only with proper documentation and a defensible apportionment basis. Without documentation → exclude entirely (Tier 2 judgement — see Section 6).

## Section 5 — Tier 1 Rules (clear rules with Tax Code references)

- **Tax object = net profit** — Object of taxation is net taxable income = total income received in cash/in-kind minus documented business expenses.  _(Art. 177.2 ПКУ)_
- **ПДФО rate** — 18% percent (on net profit)  _(Art. 167.1 ПКУ)_
- **Military levy rate** — 5% percent (on the same net-profit base; raised to 5% from 1 Dec 2024; reverts to 1.5% after martial law ends)  _(Transitional Provisions §16¹.10)_
- **Cash basis** — Income is recognised when received; expenses when paid and documented.  _(Art. 177.2, 177.4)_
- **Documentation mandatory** — Only documented expenses directly related to the business are deductible; the list of allowable expenses is in Art. 177.4 ПКУ.  _(Art. 177.4 ПКУ)_
- **Cost-of-goods matching** — Cost of goods/materials is deductible in the period the income from selling them is received.  _(Art. 177.4.1)_
- **Fixed assets** — Items > ₴20,000 with life ≥ 1 year are capitalised and depreciated straight-line over their useful life. Current repairs are expensed; modernisation/improvement is capitalised. Land and residential property are excluded.  _(Art. 177.4.6–.7; Art. 177.4.5)_
- **Quarterly PIT advances** — Self-calculated from actual income/expense records; due by 20 April, 20 July, 20 October. No separate Q4 advance — Q4 is settled in the declaration.  _(Art. 177.5.1)_
- **Annual declaration** — "про майновий стан і доходи" filed by 1 May of the following year.  _(Art. 177.5, 49.18.5)_
- **Final payment** — Within 10 calendar days after the filing deadline.  _(Art. 177.5.1, 57.1)_
- **ЄСВ separate** — Unified social contribution (22% of net profit, min ₴1,902.34/month) is computed and paid separately — see ua-social-contributions.  _(Law No. 2464-VII)_
- **VAT registration threshold** — ₴1,000,000 UAH (12-month taxable turnover; mandatory registration once exceeded; voluntary registration possible)  _(Art. 181 ПКУ)_

## Section 6 — Tier 2 Catalogue (reviewer judgement)

Mixed-use assets (car, phone, home office): apportionment between business and personal use requires a defensible basis and documentation. Conservative default = exclude the personal portion; if no basis exists, exclude entirely. Own ЄСВ deductibility: the FOP's own unified social contribution treatment in expenses has shifted with legislative amendments — confirm the current-year ДПС position before deducting. Subcontractor payments to other FOPs/individuals: deductible if documented (акт виконаних робіт), but verify withholding/ЄСВ obligations if the payee is an ordinary individual rather than a registered FOP. Inventory at year-end: the matching rule means unsold-goods cost is carried, not expensed. Requires a stock count and judgement. Currency-conversion timing and rate: which NBU rate (receipt date vs sale date) and treatment of FX gains/losses on business accounts — reviewer to confirm. Depreciation useful lives: the FOP chooses useful life within reason; document and apply consistently. Transition between regimes (single tax ↔ general system mid-year): pro-rating, double-counting risks, and treatment of assets bought under the prior regime — escalate. Whether an item is a "current repair" or a capitalisable "improvement": judgement call affecting timing of the deduction.

## Section 7 — Excel Working Paper Template (ASCII)

UKRAINE FOP — GENERAL SYSTEM — PROFIT & INCOME-TAX WORKING PAPER (TY 2026)
FOP name: ____________________   ІПН/РНОКПП: ____________   КВЕД: ________
Regime: General system (Art. 177 ПКУ)   VAT-registered: Y / N

A. INCOME (cash basis)                                            UAH
  Domestic income received .....................................  __________
  Foreign income received (NBU rate on receipt) ................  __________
  Less: customer refunds / returns ............................. (__________)
  ---------------------------------------------------------------
  (1) TOTAL INCOME .............................................  __________

B. ALLOWABLE EXPENSES (documented, Art. 177.4)
  Cost of goods/materials SOLD in period ....................... (__________)
  Wages + employer ЄСВ on employees ............................ (__________)
  Rent (premises / equipment) .................................. (__________)
  Utilities / telecom / internet (business %) ................. (__________)
  Bank charges ................................................. (__________)
  Transport / logistics ....................................... (__________)
  Depreciation (straight-line, ОЗ > ₴20,000) .................. (__________)
  Low-value items (МНМА ≤ ₴20,000) ............................ (__________)
  Mandatory insurance of business assets ...................... (__________)
  Other documented business expenses .......................... (__________)
  ---------------------------------------------------------------
  (2) TOTAL ALLOWABLE EXPENSES ................................. (__________)

C. NET TAXABLE PROFIT  = (1) - (2) ............................  __________
   (if negative: PIT = 0, military levy = 0; ЄСВ still due)

D. INCOME TAX
  ПДФО         18% × C ........................................  __________
  Military levy 5% × C ........................................  __________
  ---------------------------------------------------------------
  (3) TOTAL INCOME TAX (23% × C) ..............................  __________

E. ADVANCES PAID (20 Apr / 20 Jul / 20 Oct) .................. (__________)
  (4) BALANCE DUE WITH DECLARATION = (3) - (4) ...............  __________
      Pay within 10 days after 1 May filing deadline.

F. ЄСВ (separate — see ua-social-contributions)
  22% × C, min ₴1,902.34/mo, max base ₴172,940/mo .............  __________

Reviewer (Ukrainian accountant/auditor): ____________  Date: ________

## Section 8 — Bank Statement Reading Guide (Ukrainian banks)

Most FOPs bank with PrivatStudio/Privat24 для бізнесу (PrivatBank), Monobank (sole-trader / "ФОП" account), Oschadbank, or Raiffeisen Bank. Export the business-account statement (виписка) for the full year; for FX accounts also export the conversion records.

**Bank statement terminology table**

| Ukrainian term | English | Note |
| --- | --- | --- |
| Виписка по рахунку | Account statement | The primary source document |
| Надходження / Кредит | Credit / money in | Candidate income |
| Списання / Дебет | Debit / money out | Candidate expense |
| Призначення платежу | Payment purpose / narrative | Read this to classify |
| РКО / комісія банку | Account servicing / bank fee | Deductible |
| Поточний рахунок ФОП | FOP current account | Business account |
| Валютний рахунок | FX account | Convert at NBU rate on receipt |
| Переказ на власну картку | Transfer to own card | Owner drawing — exclude |
| Еквайринг / торговий POS | Acquiring / card-terminal settlement | Sales income (gross of acquiring fee) |
| Поповнення рахунку готівкою | Cash deposit | Verify source before treating as income |

Monobank ФОП: statement downloadable as CSV/PDF in the app; "Покупки/Перекази" tags are not tax categories — reclassify by narrative. PrivatBank (Privat24 Бізнес): "виписка" with "Призначення платежу" column; acquiring settlements arrive net of fee — gross up the income and book the acquiring fee as an expense. Oschadbank / Raiffeisen: check whether VAT is shown separately on settlements if the FOP is VAT-registered. Always reconcile the bank total to the Книга обліку доходів і витрат (income & expense ledger); cash receipts not in the bank must still be declared.

## Section 9 — Onboarding Fallback (questions to ask)

1. Are you registered as a ФОП on the general system, or on the single tax (єдиний податок)? (If single tax → ua-single-tax.)
2. What are your КВЕД activity codes?
3. Are you VAT-registered (платник ПДВ)? Did 12-month turnover exceed ₴1,000,000?
4. Do you have supporting documents (акти, invoices, receipts) for the expenses you want to deduct?
5. Do you have employees? (Affects wages/ЄСВ deductions and reporting.)
6. Did you buy any fixed assets (> ₴20,000) this year? Do you keep a depreciation schedule?
7. Did you receive foreign-currency income? Do you have NBU conversion records?
8. Did you make the quarterly PIT advances (20 Apr / 20 Jul / 20 Oct)? How much?
9. Are you paying your own ЄСВ? (Confirm in ua-social-contributions.)
10. Any inventory unsold at year-end? (Affects cost-of-goods matching.)

## Section 10 — Reference Material

### Legislation

- **Legislation references** — Tax Code of Ukraine (Податковий кодекс України) — Art. 177 (taxation of FOP income on the general system: object, expenses, advances, declaration), Art. 178 (independent professional activity — out of scope), Section IV / Art. 167.1 (18% PIT rate), Art. 181 (VAT registration threshold), Art. 49.18.5 & 57.1 (filing/payment deadlines), Transitional Provisions §16¹.10 (military levy, 5% under martial law). Law No. 2464-VI "Про збір та облік єдиного внеску…" — ЄСВ (handled in ua-social-contributions). Law No. 4015-IX / No. 4113-IX (2024) — military-levy increase to 5% from 1 Dec 2024 and FOP application rules. State Tax Service: tax.gov.ua / dps.gov.ua; portal cabinet.tax.gov.ua. PwC Worldwide Tax Summaries — Ukraine (Individual).  _(Art. 177, 178, 167.1, 181, 49.18.5, 57.1, Transitional Provisions §16¹.10; Law No. 2464-VI; Law No. 4015-IX / 4113-IX)_

### Short test suite

FOP on general system, income ₴1m, documented expenses ₴300k → net profit ₴700k; ПДФО ₴126k + military levy ₴35k = ₴161k (+ ЄСВ separate). ✔
Expense with no document → not deductible; exclude. ✔
Laptop ₴45,000 → capitalise & depreciate, not full expense. ✔
Loss year → no PIT/military levy on profit; ЄСВ still ₴1,902.34/month. ✔
Single-tax payer asks to deduct expenses → wrong skill; route to ua-single-tax. ✔
Turnover ₴1.5m → flag mandatory VAT registration (> ₴1m). ✔
Transfer to own personal card → owner drawing; exclude, not an expense. ✔

## PROHIBITIONS

NEVER deduct an expense without a supporting document — documentation is mandatory under Art. 177.4.
NEVER deduct the cost of goods still unsold at year-end — apply the cost-of-goods matching rule.
NEVER expense a fixed asset (> ₴20,000, life ≥ 1 yr) in full — capitalise and depreciate straight-line.
NEVER deduct personal/household spending, land, residential property, fines, penalties, or the FOP's own income tax.
NEVER use the 1.5% military-levy rate for 2026 — it is 5% under martial law (verify current status before filing).
NEVER omit ЄСВ — it is due (min ₴1,902.34/month) even in a loss year; compute it via ua-social-contributions.
NEVER apply single-tax (turnover-based) logic here — the general system taxes net profit; route turnover cases to ua-single-tax.
NEVER treat owner drawings or transfers between the FOP's own accounts as income or expense.
NEVER present a computed figure as final — every output must be reviewed and signed off by a qualified Ukrainian accountant or auditor before filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Ukraine is under martial law and rates, wage-linked amounts (minimum/living wage, ЄСВ), the military-levy rate, and filing rules change frequently — confirm every current figure with the Державна податкова служба (tax.gov.ua / cabinet.tax.gov.ua) before relying on it. This content is research-verified but must be reviewed and signed off by a qualified Ukrainian accountant or auditor before any declaration is filed or any tax is paid.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as Ukrainian tax law changes.

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
