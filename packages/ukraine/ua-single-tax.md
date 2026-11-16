---
name: ua-single-tax
description: "Ukrainian single tax (єдиний податок) simplified regime for sole proprietors (ФОП): the three FOP groups, income limits, rates, the 1% military levy on Group 3, ЄСВ due on top, employee limits, and barred activities."
version: 1.1
jurisdiction: UA
tax_year: 2026
last_updated: 2026-11-15
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# UA Single Tax

## Who this applies to

Ukraine-resident individual entrepreneurs (ФОП / FOP) registered in ordinary single-tax Groups 1, 2 or 3 for the relevant period. Currency is UAH (₴); the tax year is the calendar year. The regime is Спрощена система оподаткування, Chapter 1 of section XIV of the Tax Code, administered by ДПС / State Tax Service. Start with ua-freelance-intake, preserve the income-tax-workflow-base dependency, and send verified results to ua-return-assembly. ЄСВ is a separate contribution: use ua-social-contributions with the corrections and referral boundaries below. Filing is through the Electronic Cabinet (cabinet.tax.gov.ua).

Contributor: Open Accountants Community. Skill version: 1.1. Companies (ТОВ), Group 4 farming and electronic residents are outside this FOP computation, even where legislation gives them separate simplified-system routes.

### Group eligibility, not a default

| Group | Eligible work and customers | Employees | Annual income cap, 2026 | Official source |
|---|---|---|---|---|
| 1 | Exclusively market-stall retail and/or the household services listed in 291.7 to the public; not unrestricted freelance services | No employees | 167 × UAH 8,647 = **UAH 1,444,049**, derived | [Tax Code 291.4(1),291.7](https://tax.gov.ua/nk/); [Budget articles 7-8](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) |
| 2 | Services, including household services, to single-tax payers/the public; production and/or sale of goods; restaurant activity. The service-customer restriction is not a blanket bar on goods sales to legal entities. Listed real-estate intermediary/valuation, internet-access and commercial jewellery activities have the separate Group 3 restriction | At most 10 counted employees simultaneously; maternity/childcare and mobilized-worker exceptions under 291.4.1 | 834 × UAH 8,647 = **UAH 7,211,598**, derived | [Tax Code 291.4(2),291.4.1](https://tax.gov.ua/nk/); [Budget 8](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) |
| 3 | Eligible FOP activities, including qualifying services to companies and foreign customers, subject to 291.5 exclusions. Freelancer/IT/consultant status alone does not establish registration or eligibility | No employee-number limit under 291.4(3) | 1,167 × UAH 8,647 = **UAH 10,091,049**, derived | [Tax Code 291.4(3),291.5](https://tax.gov.ua/nk/); [Budget 8](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) |

The approximate old caps of UAH 1.44 million, 7.21 million and 10.09 million are orientation only; use the exact derived caps for an excess calculation. Both caps and fixed single-tax wage bases use the statutory **1 January** amounts. The applicable local-council rate must still be established; a fixed January base does not mean every council's rate or every month's liability is identical.

## Rates, bands and thresholds

These ordinary rates require the correct registered period, permitted activity and verified relief position.

| Item | 2026 value and complete condition | Official source |
|---|---|---|
| Able-bodied subsistence minimum | UAH **3,328** on 1 January 2026; this is the category used for Group 1 single tax, not the overall per-person subsistence figure | [Budget 2026 article 7,PDFp 3](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) |
| Minimum wage | UAH **8,647/month**, statutory 1 January 2026 amount | [Budget 2026 article 8,PDFp 3](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf); [DPS 2026 figures](https://tax.gov.ua/media-tsentr/novini/999526.html) |
| Group 1 single tax | Local-council monthly rate, at most **10%** of January able-bodied subsistence minimum; statutory ceiling **UAH 332.80/month**, derived. Check activity/location rate and applicable relief | [Tax Code 293.1-293.2,293.6-293.7,295.5](https://tax.gov.ua/nk/); [Budget 7](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) |
| Group 2 single tax | Local-council monthly rate, at most **20%** of January minimum wage; statutory ceiling **UAH 1,729.40/month**, derived. Check activity/location rate and relief | [Tax Code 293.1-293.2,293.6-293.7,295.5](https://tax.gov.ua/nk/); [Budget 8](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) |
| Ordinary Group 3 single tax | **5%** of statutory income where VAT is included in single tax, or **3%** where separately paying VAT. The specified commercial production/supply/sale of jewellery and household precious-metal/stone articles uses 5%; distinguish household custom-making/repair below | [Tax Code 293.3](https://tax.gov.ua/nk/) |
| Groups 1/2 military levy | **10%** of January minimum wage per calendar month = **UAH 864.70/month**, derived, subject to applicable relief. Not 10% of revenue | [XXsub 10,16-1(1.1-1.3,1.12-1.13)](https://tax.gov.ua/nk/); [Budget 8](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) |
| Ordinary Group 3 military levy | **1%** of article 292 income, separately from single tax; e-residents excluded from this levy route | [XXsub 10,16-1(1.1(3),1.2(3),1.3(3))](https://tax.gov.ua/nk/) |
| FOP cap excess/specified breaches | **15%** single-tax rate on the affected income under 293.4, not an additional 15 percentage points on top of 5%, and not a substitute for checking required transition | [Tax Code 293.4,293.8](https://tax.gov.ua/nk/) |
| Ordinary own ЄСВ minimum | **22%** × monthly minimum wage = **UAH 1,902.34/month**, derived, for a liable ordinary single-tax FOP. Choose own base within statutory limits; verified exemptions can change liability. Three fully liable months at this minimum = **UAH 5,707.02**, derived | [DPS 2026 base explanation](https://sumy.tax.gov.ua/media-ark/news-ark/977379.html); [DPS national 2026 figures](https://tax.gov.ua/media-tsentr/novini/999526.html); [current employer-paid exemption](https://zir.tax.gov.ua/main/bz/view/?id=43912&src=ques) |

**Wartime distinction:** the old headline's “1% to 5%” levy increase conflated different taxpayer routes. Group 3 single-tax military levy remains the 1% statutory-income route in this skill. The levy provisions for these single-tax payers run from **1 January 2025 through 31 December of the third calendar year after the year martial law ends**, as amended in 2026; they do not simply disappear on the day martial law ends. [XXsub 10,16-1(1.1),Law 4835-IX amendment](https://tax.gov.ua/nk/).

### Fixed-payment and ЄСВ conditions

For Groups 1/2, multiple activities use the highest local rate for those activities; activity in more than one council area uses the statutory maximum for the group (293.6-293.7). Ordinary monthly fixed single tax and levy do not fall merely because receipts are low or zero. However, **do not charge every month unconditionally**:

- With **no employees**,295.5 allows Group 1/2 single-tax relief for **1 calendar month of annual leave**, and illness of **30 or more calendar days** supported by the electronic sick-leave-register extract. The corresponding military-levy relief is 16-1(1.13). For both single-tax and levy relief, submit the free-form leave/illness application under 298.3.2, including the electronic sick-leave extract for illness; 295.2 uses these applications for the single-tax accrual. Establish each tax's qualifying relief, rather than assuming an ЄСВ exemption follows.
- For qualifying Group 1/2 tax addresses in listed combat/occupied territories, XXsub 8(11) and XXsub 10,16-1(1.12) provide separate single-tax/levy nonpayment rights. Eligibility is tied to address **at the relevant territory's start date**, listed periods and statutory boundaries; a later move to another area ends the rule from the first day of the following month. The actual current territory list and individual evidence must be opened before relief is used.
- Single-tax FOPs ordinarily owe own ЄСВ despite zero revenue. Screen pension/disability, employer-paid contributions, military-service, occupied-territory and other special status before charging it. Under the current employer-paid rule, an eligible employer, including a Diia City resident, must have paid **at least the monthly minimum contribution** for that month; an “only main employment counts” restriction is obsolete. If less is paid, a single-tax FOP remains obliged to determine/pay their own base with the minimum. Other exemption conditions and documentary proof require the separate ЄСВ review; this skill gives no automatic exemption merely from a status label. [DPS 2026 explanation](https://if.tax.gov.ua/media-ark/news-ark/978737.html); [current ZIR answer](https://zir.tax.gov.ua/main/bz/view/?id=43912&src=ques).

## The base

Group 3 taxes statutory **income**, not profit. Do not deduct business expenses against the single-tax base. Cash/noncash receipts and the specifically defined material/intangible receipts are classified under 292; a bank total is not automatically the base. Groups 1/2 also need accurate income for caps and affected-income rates.

- Use the receipt-date rule in 292.6. Foreign-currency income is translated at the **official NBU rate on receipt** under 292.5. Later compulsory/voluntary currency-sale proceeds are not substituted for that base. Any actual NBU sale, repatriation or banking restriction needs its own current review; no blanket sale requirement is asserted here.
- Separate passive interest/dividends/royalties, insurance/grants and income from the individual's disposal of relevant personally owned property under 292.1; this is not an assurance those items are exempt from other personal taxes. Article 292.3 includes qualifying free goods/services and, for VAT-paying Group 3, specified expired payable debts. Agency/commission/forwarding income uses the remuneration rule in 292.4 rather than automatically including all principal money.
- For a VAT-paying 3% FOP, VAT amounts are excluded under 292.11(1). Article 292.11 also excludes qualifying credits and returnable financial assistance received and returned within **12 calendar months**; customer refunds require the documented goods-return/contract-termination/refund-letter conditions in 292.11(5). Do not net off unrelated transfers or an unsupported “loan” description. Review the other statutory exclusions and dates before finalizing the base.
- Keep income records:296.1 permits a free form with **monthly income reflection** for Groups 1/2 and non-VAT Group 3; VAT-paying Group 3 uses the prescribed income/expense form. Paper/electronic records are possible. The former income-book label does not require a nonexistent registration step, and a bank statement does not replace all underlying records.

All these base rules: [Tax Code 292.1-292.16,296.1](https://tax.gov.ua/nk/).

### Refusal catalogue and activity screen

**R-UA-1, cap breach:** apply 15% to the excess and establish the next-quarter transition. **Group 1 can elect Group 2/3 if eligible or leave; Group 2 can elect Group 3 if eligible or leave; Group 3 must leave simplified taxation.** The 293.8 application deadline is no later than 20 of the month after the quarter of excess. Do not call all three paths a forced transfer to general taxation. Preserve excess separately in the declaration under 296.5-296.6. The subsequent-year eligibility test in 292.16 also matters. [293.4,293.8,296.5-296.6](https://tax.gov.ua/nk/).

**R-UA-2, barred or mismatched activity:** check actual work and full 291.5, not the client's trade label. The old flags remain: gambling/lotteries, FX exchange, excisable goods, financial intermediation, mineral extraction/sale, arts/antiques, technical testing and enterprise management. Preserve these statutory distinctions:

- Excisable activity has the specified retail lubricants/fuel-container exception up to **20 litres** and the individual retail beer/cider/perry without added spirit/table-wine exception; it is not unrestricted alcohol/fuel permission.
- Precious-metal/stone activity has the jewellery/household-article carveout. Specified commercial production/supply/sale is Group 3/5%. **Custom jewellery-making and repair** are separately listed household services under 291.7(28)-(29); the [official 2026 Group 1 list](https://if.tax.gov.ua/media-ark/news-ark/print-967828.html) includes them. Do not force all repairs into Group 3 or treat all jewellery as barred.
- The mineral bar excludes sale of local minerals, not unrestricted extraction. Financial intermediation has specified insurance-agent/surveyor/adjuster exceptions. The actual conditions must be checked.
- Also check the remaining 291.5 exclusions: specified post/telecom services with courier exception; arts/antiques and auctions; touring events; security services; testing/audit; rental-area limits; financial institutions; disqualifying legal-entity ownership and branches; nonresident status and tax debt with its force-majeure bad-debt exception. Group 1/2 have their narrower activity/customer/employee conditions. Sanctions conditions under 291.3 also apply. If any relevant fact is unresolved, stop the affected computation and refer.

**R-UA-3, company:** refer a ТОВ, including one claiming Group 3; company computation is outside this individual skill. **R-UA-4, nonresident:** refer ordinary nonresident FOP claims; electronic residency is a distinct out-of-scope regime, not a fallback. Nonmonetary/barter settlement and unregistered/mismatched activities also need the 293.4/298 transition review. [291.3-291.8,293.4](https://tax.gov.ua/nk/).

### Replace the old unanswered-facts defaults

Unknown group or VAT status stays **unconfirmed**, not Group 3/non-VAT 5%. ЄСВ is screened as potentially due, with relief checked before finalizing. FX uses the receipt-date NBU evidence for a confirmed single-tax receipt. Unknown activity eligibility blocks final computation. A commonly used regime cannot replace actual register evidence.

## Deadlines and filing

| Obligation | Ordinary timing and conditions | Official source |
|---|---|---|
| Groups 1/2 return | Annual, within **60 calendar days** after year-end if ordinary annual conditions apply. Excess, higher-group election or leaving simplified taxation triggers the quarterly declaration conditions of 296.5.1; do not wait for annual filing | [49.18.3,294.1,296.2,296.5.1](https://tax.gov.ua/nk/) |
| Groups 1/2 single tax and levy | Advance by **20 inclusive of the current month**, not the following month; permitted advance payment is no later than the end of the current reporting year. Check relief and council-rate changes | [295.1-295.2;XXsub 10,16-1(1.11)](https://tax.gov.ua/nk/) |
| Group 3 return | Quarterly, within **40 calendar days** after quarter-end; cumulative reporting/affected income separately. Own ЄСВ information is in the **fourth-quarter** declaration for the year under 296.3 | [49.18.2,296.3,296.5-296.7](https://tax.gov.ua/nk/) |
| Group 3 single tax and levy | Within **10 calendar days after the statutory declaration deadline**, subject to applicable calendar rule. “50 days after quarter-end” is a rough shortcut, not the governing rule when filing dates move | [295.3,295.7;XXsub 10,16-1(1.11)](https://tax.gov.ua/nk/) |
| Own ЄСВ | Quarterly, **before 20** of the following month, ordinarily **19 inclusive**; if the last day is weekend/holiday/nonworking, the next working day under Instruction 449 IV.6. Verified Q3-2026 deadline: **19 October 2026** | [DPS 2026 deadline explanation](https://zak.tax.gov.ua/media-ark/news-ark/981527.html); [DPS 13 October 2026 notice](https://ck.tax.gov.ua/media-ark/news-ark/print-1058715.html) |
| FOP as employer/tax agent | The combined PIT/levy/ЄСВ calculation for income accrued to individuals is **quarterly, with monthly breakdown**, from 2026. It is required where such income was accrued during the period, including unpaid accrued wages; actual payment is not the sole trigger. It is distinct from own annual ЄСВ information in the single-tax return. A company tax agent ordinarily reports monthly | [176.2(b),296.2-296.3](https://tax.gov.ua/nk/) |

Article 49.20 moves a declaration deadline falling on a weekend/holiday to the following operational day. Payment and ЄСВ rules must be applied separately. A change, closure or relief case needs its specific declaration and payment review; these relative deadlines do not establish a final filing calendar for an unresolved case. Preserve electronic filing confirmations and reconcile actual payments before ua-return-assembly.

## Penalties and interest

The 15% affected-income rate under 293.4 is **tax**, not the whole penalty bill. Cap excess and disallowed activity can also end eligibility. Late declarations, late single tax/levy payments, ЄСВ arrears and interest require separate current compliance review. No blanket wartime waiver is assumed. The levy's specific responsibility/territorial relief provisions are in 16-1(1.11-1.13); exact additional penalty/interest amounts and individual suspension grounds are **not yet confirmed** here. Do not present the examples as a complete arrears calculation.

## Cross-border points

Eligible Group 3 FOPs can receive foreign customer income, including from companies, subject to actual residency and activity conditions. Keep original currency, receipt date and official daily NBU rate; do not replace receipt income by later bank-sale proceeds. General-system periods and personal foreign income use ua-income-tax/ua-cross-border, not this rate shortcut. VAT classification depends on registration, transaction and place of supply; the 181.1 turnover registration test expressly excludes single-tax Groups 1-3, but nonregistration does not eliminate imports or other special obligations. Refer unresolved cross-border/VAT/NBU restrictions; do not infer an exemption from the word export. [291,292.5,181.1-181.2](https://tax.gov.ua/nk/).

## Two worked examples that recompute

All original cases are retained below. These are hypothetical ordinary-liability cases with no relief, no cap/eligibility problem except the explicit cap test, verified registration, no other base adjustments and the minimum own ЄСВ chosen. Monthly ЄСВ allocations are shown for comparison; payment is quarterly. Fixed single-tax examples assume the council set the statutory maximum. Amounts are derived, not final filing advice.

### Case A: the original Group 2 monthly cost

At the maximum local rate: UAH 1,729.40 single tax + UAH 864.70 levy + UAH 1,902.34 own ЄСВ = **UAH 4,496.44/month**, derived, correcting the old roundedUAH 4,496. The same total applies to the original **UAH 5,000 low-income month** under these assumptions, not to a month with qualifying relief.

```oa-check
name: Group 2 full monthly ordinary liability and low-income case
inputs:
  january_minimum_wage: 8647
  local_rate: 0.20
  military_rate: 0.10
  esv_rate: 0.22
  monthly_receipts: 5000
steps:
  - single_tax: january_minimum_wage * local_rate
  - military_levy: january_minimum_wage * military_rate
  - own_esv: january_minimum_wage * esv_rate
  - monthly_total: single_tax + military_levy + own_esv
  - receipts_after_allocated_liability: monthly_receipts - monthly_total
expected:
  single_tax: 1729.40
  military_levy: 864.70
  own_esv: 1902.34
  monthly_total: 4496.44
  receipts_after_allocated_liability: 503.56
```

### Case B: original Group 3 non-VAT UAH 100,000 month

Single tax UAH 5,000 + levy UAH 1,000 + minimum own ЄСВUAH 1,902.34 = **UAH 7,902.34**, derived. No expense deduction against single tax.

```oa-check
name: Group 3 non-VAT 100000 income month
inputs:
  income: 100000
  single_rate: 0.05
  military_rate: 0.01
  monthly_minimum_wage: 8647
  esv_rate: 0.22
steps:
  - single_tax: income * single_rate
  - military_levy: income * military_rate
  - own_esv: monthly_minimum_wage * esv_rate
  - total_allocated_liability: single_tax + military_levy + own_esv
expected:
  single_tax: 5000
  military_levy: 1000
  own_esv: 1902.34
  total_allocated_liability: 7902.34
```

### Case C: original USD 3,000 customer receipt

Hypothetical receipt-date NBU rate 41.50 gives **UAH 124,500** statutory income;5% single tax**UAH 6,225**,1% levy**UAH 1,245**, plus minimum monthly own ЄСВ **UAH 1,902.34**. Total allocated liability **UAH 9,372.34**, derived. The actual daily NBU rate must be obtained for a real receipt. No expense deduction.

```oa-check
name: Group 3 foreign receipt at hypothetical NBU rate
inputs:
  usd_income: 3000
  receipt_nbu_rate: 41.50
  single_rate: 0.05
  military_rate: 0.01
  monthly_minimum_wage: 8647
  esv_rate: 0.22
steps:
  - income_uah: usd_income * receipt_nbu_rate
  - single_tax: income_uah * single_rate
  - military_levy: income_uah * military_rate
  - own_esv: monthly_minimum_wage * esv_rate
  - total_allocated_liability: single_tax + military_levy + own_esv
expected:
  income_uah: 124500
  single_tax: 6225
  military_levy: 1245
  own_esv: 1902.34
  total_allocated_liability: 9372.34
```

### Case D: the old November UAH 10.09 million cap warning

Exactly **UAH 10,090,000** is **UAH 1,049 below** the exact 2026 Group 3 cap UAH 10,091,049; it has **no excess** on those facts. An additional hypothetical UAH 2,000 receipt makes total UAH 10,092,000 and excess **UAH 951**. The 15% single tax on that excess is **UAH 142.65**, derived; do not add another 5% to the same excess. Separately compute ordinary-income single tax and military levy, establish the next-quarter exit/application and all other liabilities. This cap-only check is not a total tax bill.

```oa-check
name: Exact Group 3 cap corrects rounded old warning
inputs:
  cap_multiplier: 1167
  january_minimum_wage: 8647
  november_income: 10090000
  later_receipt: 2000
  excess_rate: 0.15
steps:
  - cap: cap_multiplier * january_minimum_wage
  - headroom_before: max(0, cap - november_income)
  - original_excess: max(0, november_income - cap)
  - later_total: november_income + later_receipt
  - later_excess: max(0, later_total - cap)
  - excess_single_tax: later_excess * excess_rate
expected:
  cap: 10091049
  headroom_before: 1049
  original_excess: 0
  later_total: 10092000
  later_excess: 951
  excess_single_tax: 142.65
```

## Ask the client first

Minimum: actual FOP group, VAT status/dates for Group 3, full-year bank/turnover records in UAH and all FX. Obtain the EDR extract with KVED, the **single-tax register extract** with current group/rate/effective dates, prior return and ЄСВ history. Request the income ledger (or prescribed income/expense form where relevant), all FX receipt dates/NBU evidence, customer/refund/loan support, activity/customer details, employees and counting exceptions, council rate, location/relief history and actual contributions/other employment evidence. “Recommended” documents in the old list become necessary where they establish a claimed status or exclusion; unknown facts are not defaults.

### Prohibitions preserved

1. Never deduct business expenses from the single-tax base.
2. Never omit the ЄСВ review; ordinarily due even with zero revenue, but do not charge it over a verified exemption.
3. Never omit the applicable military levy; distinguish Group 3 income 1% from Groups 1/2 fixed 10% of January minimum wage and verify relief.
4. Never apply Group 1/2 to **ineligible services** supplied to companies/foreign customers; test statutory activity/customer conditions. This does not ban every Group 2 goods sale to a company or every permitted household service.
5. Never tax a cap excess at the ordinary 5% rate; separate 15% affected income and the correct transition. Do not force Group 1/2 general taxation when an eligible higher-group route exists.
6. Never present a computed figure as definitive; obtain Ukrainian accountant/auditor review before filing.

## Sources

| Official source | Read for | Read date |
|---|---|---|
| [State Tax Service consolidated Tax Code](https://tax.gov.ua/nk/) | Read for full articles 291 and 292; 293.1-293.8; 294.1-294.7; 295.1-295.8; 296.1-296.10; 298.2.3 and 298.3.2; 176.2(b); 181.1-183.4; 49.18.2-49.20; XX subsection 8(11); XX subsection 10, 16-1(1.1-1.17). Operative paragraphs and neighboring exceptions, not the entire code. Header includes October 2026 amendments | 2026-11-15 |
| [Budget 2026 original law 4695-IX, official Odesa Finance Department](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) | Read for articles 7-8 January subsistence/minimum wage; 32 ESV cap with military exception; final provisions 3 suspension of wartime voluntary ESV 9-19. Original enacted PDF; not a claim all later budget amendments were opened | 2026-11-15 |
| [DPS national 2026 contribution figures](https://tax.gov.ua/media-tsentr/novini/999526.html) | Read for 2026 minimum wage 8,647, 22% minimum 1,902.34 and 20 minimum wage maximum base; actual 9 April 2026 statement | 2026-11-15 |
| [DPS 2026 base explanation](https://sumy.tax.gov.ua/media-ark/news-ark/977379.html) | Read for Law 2464 article 7(1)(3) self-chosen simplified base/minimum and zero-profit general-system distinction. Its maximum-base prose has a decimal typo; national figures and Budget 32 control that separate figure | 2026-11-15 |
| [Current ZIR employer-paid exemption](https://zir.tax.gov.ua/main/bz/view/?id=43912&src=ques) | Read for Law 2464 article 4(6) as amended by 4536-IX: monthly minimum actually paid and no main-employment condition; full current answer including 2026 employer list and below-minimum consequence | 2026-11-15 |
| [DPS 2026 contribution overview](https://if.tax.gov.ua/media-ark/news-ark/978737.html) | Read for pension/disability, employer-paid, military and occupied-status flags. Brief summary does not establish every exception's individual conditions; those remain review items | 2026-11-15 |
| [DPS 2026 payment deadline explanation](https://zak.tax.gov.ua/media-ark/news-ark/981527.html) | Read for Law 2464 article 9(8): before 20 means 19 inclusive, and Instruction 449 IV.6 next-working-day exception | 2026-11-15 |
| [DPS Q3-2026 notice](https://ck.tax.gov.ua/media-ark/news-ark/print-1058715.html) | Read for actual 19 October 2026 own ESV deadline, monthly liability review, account details and payment reconciliation | 2026-11-15 |
| [DPS 2026 household services list](https://if.tax.gov.ua/media-ark/news-ark/print-967828.html) | Read for full 40 listed services, especially custom jewellery-making and repair under 291.7(28)-(29), and Group 1 conditions | 2026-11-15 |

Not yet confirmed: the individual's registration, local-council rate, relief documents and territory-list dates, complete special ЄСВ exemption conditions, current NBU banking/sale/repatriation restrictions, actual receipt-date NBU rates, exact additional penalty/interest computation, and current filing-form identifiers for the individual period. Unsupported old group/VAT defaults, blanket jewellery bar, all-cap-breaches-force-general claim, blanket no-exemption ЄСВ and currency-sale-base instruction are withdrawn and corrected above. These holds block the affected final computation; they do not authorize guessing. Parliament/current ESV law endpoints could not be opened; current official tax-authority explanations are identified honestly. An archived ZIR answer ending 1 October 2025 was read as history and is not current authority.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Rates, wage-linked amounts, and martial-law measures change frequently; confirm the current minimum wage, living wage, and military-levy status with the Державна податкова служба before relying on any figure. All outputs must be reviewed and signed off by a qualified professional (a Ukrainian accountant or auditor) before filing.
