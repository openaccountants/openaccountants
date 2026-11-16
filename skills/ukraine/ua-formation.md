---
name: ua-formation
description: Use this skill whenever asked about registering or forming a business in Ukraine for a self-employed person. Trigger on phrases like "register a FOP", "how do I become a ФОП", "start a business in Ukraine", "open a sole proprietorship Ukraine", "Diia registration", "ТОВ vs ФОП", "LLC vs sole proprietor Ukraine", "choose КВЕД codes", "single tax election", "register for VAT Ukraine", "open a business bank account Ukraine", "close my ФОП", or any question about the formation, registration, tax-system choice at start-up, or deregistration of a Ukrainian sole proprietor (ФОП) or company (ТОВ). Covers registering via Diia or a state registrar/notary, documents required, choosing КВЕД activity codes, electing the single-tax group (1/2/3) vs the general system, the ₴1,000,000 VAT threshold, ЄСВ registration, opening a bank account, the ФОП-vs-ТОВ decision, and closing a ФОП. ALWAYS read this skill before any Ukrainian business-formation work.
version: 1.1
jurisdiction: UA
tax_year: 2026
last_updated: 2026-11-16
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: filing-howto
---

# Ukraine business formation: FOP and TOV, 2026

> **General reference only.** This is a source-cited formation and tax-election brief, pending review of the applicant's facts by a qualified Ukrainian accountant or lawyer. It does not authorize a registration, election, filing or payment.

## Scope

Register an ordinary Ukrainian individual entrepreneur, **ФОП / FOP**, choose actual **КВЕД** activities and an eligible tax system, establish VAT and own **ЄСВ** duties, open the appropriate account, and hand over records and reporting. Compare a **ТОВ / TOV (LLC)** where there are co-founders, investors, liability or transferability needs. Currency: UAH. Authorities: **ЄДР** state register/Ministry of Justice, **ДПС** State Tax Service, and **Дія / Diia**. Contributor remains **Open Accountants Community**.

**Key corrections:** single tax is an election, not an automatic consequence of ordinary FOP registration. New Groups 1/2 apply by registration **month-end**, starting the next month; new ordinary non-VAT Group 3 has the distinct **10-day** application rule, starting on the registration date. Groups 1-3 have a carveout from the ordinary VAT turnover-registration rule. A TOV's non-single-tax legal-person ownership must be **below 25%**, not at most 25%. [Tax Code 298.1.2,181.1,291.5.5](https://tax.gov.ua/nk/).

Read date **16 November 2026**, with precisely identified older source material below. Foreign nationals/nonresidents, disputed residence, e-residents, agricultural Group 4, reorganizations, regulated businesses, charters, beneficial-ownership declarations and liquidation documents require the qualified specialist. An ordinary FOP guide must not silently apply their exceptions. No authenticated portal submission was tested.

## Ask the client first

Reuse existing intake and register evidence before asking again. Obtain identity and **РНОКПП** tax number or the legally applicable documented exception, residence/address, citizenship/immigration status, proposed start date, existing/closed FOP history and prior-year income. **УНЗР** is a demographic-register identifier; do not substitute it for РНОКПП merely because both occur on an ID record. Confirm portal access and the actual accepted **physical-person electronic signature**, not just a login method.

Obtain the real activities and proposed primary/additional KVED codes; service versus goods/restaurant business; each customer's individual/business, tax and residence status; expected receipts, currencies, staff and other legal restrictions; current debts/sanctions and eligibility evidence. For a TOV, obtain founders, ownership percentages and legal-person owners' tax status, UBO facts, director, charter choice, capital and contribution timetable. Obtain the VAT place-of-supply forecast, taxable rolling turnover, input-VAT/pricing needs, own-ЄСВ exemption evidence by month, payment channels, account and record/reporting setup. Unknown facts block the relevant election; occupation alone does not prove eligibility.

## Rates, bands and thresholds

| Item | Ordinary 2026 rule and condition | Official source |
|---|---|---|
| January minimum wage | **8647 per month**; this is the January index, not a promise every later law or local rate is unchanged | [Budget 4695-IX art 8, original enacted text](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf); [2026 DPS corroboration](https://tax.gov.ua/media-tsentr/novini/999526.html) |
| Group 1 | No hired employees; market-stall retail and/or listed household services to the population. Annual income ceiling **1444049 = 167 × 8647**. Council-set monthly single tax at most **332.80 = 10% × 3328**, the January able-bodied subsistence amount | [291.4(1),291.7,293.1-.2](https://tax.gov.ua/nk/); [Budget art 7/8](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) |
| Group 2 | Services to single-tax payers and/or the population; goods production/sale and restaurant activity are distinct branches. At most **10 simultaneous employees**, with statutory counting exceptions; annual income ceiling **7211598 = 834 × 8647**. Council-set monthly tax at most **1729.40 = 20% × 8647** | [291.4(2),291.4.1,293.1-.2](https://tax.gov.ua/nk/); [January wage](https://tax.gov.ua/media-tsentr/novini/999526.html) |
| Group 3 | Eligible FOPs and legal entities; no ordinary FOP headcount ceiling. Annual income ceiling **10091049 = 1167 × 8647**; **5% income** with VAT included in single tax, or **3% income with separate VAT**, actual eligibility/registration required | [291.4(3),291.5,293.3](https://tax.gov.ua/nk/); [wage](https://tax.gov.ua/media-tsentr/novini/999526.html) |
| Separate military levy | Ordinary Groups 1/2 **864.70 per month = 10% January minimum wage**; ordinary Group 3 **1% article 292 income**, excluding e-residents. Individual relief must be verified separately | [XX.10.16-1(1.1-1.3),292](https://tax.gov.ua/nk/) |
| General-system FOP | Ordinary **18% PIT plus 5% levy** on the applicable net taxable business-income base; documented expenses, paid own-ЄСВ and VAT exclusions matter. No single-tax income ceiling; activity permissions still apply | [167.1,177.1-.4;XX.10.16-1](https://tax.gov.ua/nk/); [paid own-ЄСВ expense](https://cv.tax.gov.ua/media-ark/news-ark/977945.html) |
| Own ЄСВ | Ordinary **22%**. For liable simplified-system months, self-chosen base within maximum and at least the minimum: **1902.34/month**, **5707.02/three months**, **22828.08/twelve months**, derived. General-system base is the taxable activity income/profit with its own no-profit-month rule; do not apply a turnover-independent FOP minimum indiscriminately | [Law 2464 art 7 as explained by DPS](https://sumy.tax.gov.ua/media-ark/news-ark/977379.html); [current figures](https://tax.gov.ua/media-tsentr/novini/999526.html) |
| Own-ЄСВ maximum | Ordinary 2026 monthly base **172940**, monthly contribution **38046.80**, separate from the single-tax income cap. Exemptions and actual months must be established | [Budget art 32;2026 DPS figures](https://tax.gov.ua/media-tsentr/novini/999526.html) |
| Ordinary mandatory VAT registration | Taxable supplies **over 1000000**, VAT excluded, during the last **12 calendar months**; **Groups 1-3 single-tax carveout**. Imports/nonresident services and other VAT liabilities remain separate | [181.1-.2,208](https://tax.gov.ua/nk/) |
| VAT rates | Ordinary **20%**; **0%/7%/14%** require the specific statutory supply and conditions, not the customer's request or a foreign address | [193-195](https://tax.gov.ua/nk/) |
| TOV ordinary corporate tax | Generally **18%** on the corporate tax base, or eligible Group 3 election. Accounts and founder-distribution taxes are separate | [136.1,291.4-.5,293.3](https://tax.gov.ua/nk/) |

The January index is fixed by the particular single-tax/levy provision; an actual council rate or relief is not automatically fixed for every month. Current single-tax military-levy duration runs through **31 December of the third calendar year following the year martial law ends/cancels**, rather than ending immediately with martial law. Do not invent an end date. [293.1;XX.10.16-1(1.1)](https://tax.gov.ua/nk/).

## The method, step by step

### 1. Decide legal form and actual tax eligibility

A FOP is the individual carrying on business, without a separate company capital/share structure. Personal assets exposed to lawful enforcement are at risk; do not promise a protected ring-fenced FOP estate. The current DPS/NACP explanation supports that distinction but also cites the former Commercial Code, so it is not a complete current civil-liability opinion. [10 November 2026 official explanation, Civil Code 52](https://lg.tax.gov.ua/media-ark/news-ark/1066916.html).

A TOV supplies a company/participant structure for co-founders, equity investment, sale/scale and liability planning. Limited liability is **not** a promise that every participant/director is immune: unpaid contributions, guarantees and other legal grounds need counsel. Diia confirms **no statutory minimum capital**, even **one hryvnia (in words on the page)**, and offers a sole-founder decision or founders' minutes/model charter route. The old unconditional **six-month** contribution instruction is held: the opened 2024 AMCU decision quotes that default **unless the charter provides otherwise**, but the full current 2275-VIII text was inaccessible. Have counsel establish the actual charter and current contribution rule before a calendar is issued. No new charter, UBO or liquidation document is drafted here. [Diia TOV instructions/FAQ](https://diia.gov.ua/services/reyestraciya-tov-na-pidstavi-modelnogo-statutu/); [dated AMCU discussion, printed p 32](https://amcu.gov.ua/static-objects/amcu/uploads/public/675/abc/bd9/675abcbd9f2a5823893562.pdf).

Do not default every freelancer to Group 3. Compare eligible Groups 1/2, Group 3 and general system against actual customer/activity/staff/income facts. Group 2's **service** restriction is not a categorical ban on every sale of goods to a legal person, and Group 3 is not compulsory merely because a customer is foreign: the general system remains an option. Foreign-company service work ordinarily fails the Group 1/2 service routes. Full bars and exceptions, including excise, gambling, currency, minerals, jewellery and financial intermediation, stay with `ua-single-tax`; a KVED label alone is not a legal eligibility opinion. [291.4-.7](https://tax.gov.ua/nk/).

For TOV Group 3, test annual income, activities, residence, debts and all 291.5 bars. Under **291.5.5**, shares collectively owned by legal persons that are not single-tax payers **equal to or exceeding 25%** bar the route. The old “≤25% allowed” boundary was wrong. A TOV retains company accounts/financial statements under either tax regime; founder withdrawals are not the same as FOP drawings. Route corporate tax/distributions to `ua-corporate-income-tax`/`ua-income-tax` and accounts to `ua-financial-statements`. Exceeding the FOP cap does not itself force incorporation, and there is no Group 3 FOP headcount ceiling. [291.4(3),291.5.5](https://tax.gov.ua/nk/).

### 2. Select and document KVED activities

Use actual work, primary revenue activity and necessary additional activities; update the register when activities change. The old **5-7 codes** was practice commentary, not a statutory minimum/maximum or permission for unused barred activities. The current six illustrative classes are:

| KVED-2010 | Scope to check, including the classifier's exclusions | Official source |
|---|---|---|
| **62.01** | Computer programming; publishing standard software and integrated-system planning have separate classifications | [Full class](https://kved.ukrstat.gov.ua/KVED2010/62/KVED10_62_01.html) |
| **62.02** | Integrated computer-system planning/consultancy; hardware trade and specified installation activities excluded | [Full class](https://kved.ukrstat.gov.ua/KVED2010/62/KVED10_62_02.html) |
| **63.11** | Data processing/hosting and related services; computer use merely as a tool does not determine this code | [Full class](https://kved.ukrstat.gov.ua/KVED2010/63/KVED10_63_11.html) |
| **70.22** | Business/management consultancy; tax/accounting/legal advice has separate exclusions | [Full class](https://kved.ukrstat.gov.ua/KVED2010/70/KVED10_70_22.html) |
| **73.11** | Advertising agencies; publishing, film/radio production, market research and other listed exclusions require separate codes | [Full class](https://kved.ukrstat.gov.ua/KVED2010/73/KVED10_73_11.html) |
| **96.02** | Hairdressing/beauty services, including barbering; not every medical/beauty activity | [Full class](https://kved.ukrstat.gov.ua/KVED2010/96/KVED10_96_02.html) |

The official Order **191 of 28 October 2025** sets **NACE 2.1-UA effective 1 January 2027**. That is a classifier commencement, not proof of a universal client re-registration deadline or approval of every future code mapping. Use the current KVED-2010 descriptions for the 2026 examples; verify the actual transition procedure for a later application. [Official order and implementation instruction](https://stat.gov.ua/uk/page-contents/nakaz-vid-28102025-no191).

### 3. Submit the FOP registration through the actual available channel

Diia's **«Автоматична реєстрація ФОП»** service describes authorization, online form completion and the applicant's **physical-person electronic signature**, with optional tax-system markings transmitted to DPS. Confirm ID/address, РНОКПП, chosen activities and election in the real form. Login with a bank/identity service is not proof the application has been signed or accepted. The older “Diia app v2.0+”, universal BankID/Diia.Signature interchangeability and unconditional УНЗР substitution are not current document requirements here. [Official FOP service](https://diia.gov.ua/services/reyestraciya-fop).

The service is **free**, displays approximately **10 minutes** to apply and automatic registration **up to one minute**; it separately describes entry in EDR within **two working days** and an extract after tax/statistical registration within **three working days**. These are the page's different process estimates, not an unconditional statutory **24-hour** guarantee. Check application status at **Послуги → Замовлені послуги**, notification/email and the actual register record; download and preserve the legally valid **виписка**, identifiers, activities and effective date. Do not confuse every downloaded register document with a separately ordered **витяг**. [Service workflow/result/FAQ](https://diia.gov.ua/services/reyestraciya-fop).

Offline registration through **ЦНАП/state registrar** or an acting notary remains a referral route when online signature/access is unavailable. The Diia page describes an accountant/representative using a notarized power of attorney offline. Current application **Form 1**/attachments, foreign passport translation/residence rules and notary charges require the current registrar's checklist; they were not fully established here. Do not give the old universal foreign-founder document list as sufficient. Electronic-signature and bank fees/timing are provider-specific: original pointers **Privat24, Monobank, Oschadbank and Raiffeisen** are retained without a free/same-day service promise. [Official service and offline FAQ](https://diia.gov.ua/services/reyestraciya-fop).

### 4. File and verify the separate tax election

| Applicant/choice | Application and effective date | Official source |
|---|---|---|
| Newly registered ordinary FOP, Group 1/2 | Apply **by the end of the registration month**; single tax starts **first day of following month**. The intervening general-system period must be assessed | [298.1.2 first paragraph](https://tax.gov.ua/nk/) |
| Newly registered ordinary business, non-VAT Group 3 | Apply **within 10 days from state registration**; single-tax status from **registration date**. This special rule does not establish immediate **3%+VAT** status | [298.1.2 second paragraph](https://tax.gov.ua/nk/) |
| Existing general-system business switching to simplified | Apply **at least 15 calendar days before next quarter**; eligible prior-year income, attached calculation and other conditions; **once per calendar year**. Prior FOP closure/re-registration does not erase earlier-year income | [298.1.4](https://tax.gov.ua/nk/) |
| Voluntary group change | Generally **at least 15 calendar days before next quarter**, actual eligibility and VAT consequences. Excess-driven changes have different rules; no automatic retroactivity | [298.1.5,293.8](https://tax.gov.ua/nk/) |

Retain the signed application/receipt and actual single-tax register result with effective date. A portal checkbox is evidence of the request, not proof of acceptance. Without a valid ordinary election the general-system route must be evaluated; e-resident automatic status is an express separate exception, not the FOP default. Route missed elections, transitions and corrections to the qualified accountant and `ua-single-tax`/`ua-return-assembly`.

### 5. Establish VAT and own-ЄСВ status separately

Under ordinary mandatory VAT registration, apply **no later than day 10 of the following month** after the threshold event; voluntary registration normally requires application **at least 10 calendar days before the intended tax period**. A simplified-to-general transition and a change to the VAT-paying single-tax rate have their own **183.4-.5/293.8** coordination rules. Record the actual VAT entry/effective date before issuing VAT invoices. Groups 1/2 do not simply add voluntary separate VAT while keeping the same group; an eligible Group 3 **3%+VAT** route needs the coordinated election/registration. [181-183,293.3/.8](https://tax.gov.ua/nk/).

Model contract price, recoverable input VAT, client needs, electronic VAT account **СЕА ПДВ**, registration capacity and recurring reporting before choosing 3% versus 5%. No blanket “VAT is never worthwhile for a freelancer” advice. Foreign-client services require a real place-of-supply decision, not automatic zero rating. `ukraine-vat` and `ua-einvoice` own the detailed computation/document process.

Confirm DPS and own-ЄСВ payer records after EDR transmission; the old separate-application-free automatic-registration claim is **not a substitute for confirming the actual record**. Ordinary simplified-system liable months carry at least the minimum even with no receipts. Check pension/disability and actual pension/assistance requirements, employer-paid minimum **by month**, military/other relief and supporting records; do not infer an exemption from a job label. The general-system no-income-month route differs and needs its own assessment. [Current employer-paid test](https://zir.tax.gov.ua/main/bz/view/?id=43912&src=ques); [bases/no-profit branch](https://sumy.tax.gov.ua/media-ark/news-ark/977379.html).

Own contributions are ordinarily paid quarterly **before the 20th**, normally **the 19th inclusive**, with the applicable working-day adjustment. Reporting one's own ЄСВ in the relevant personal/single-tax return is distinct from the FOP **tax-agent combined report**, which is quarterly with monthly breakdown from **1 January 2026** where its trigger exists; ordinary legal-person tax agents remain monthly. Do not tell a FOP without staff/other reportable accruals that they universally owe a new quarterly employer report. [Own payment rule](https://zak.tax.gov.ua/media-ark/news-ark/981527.html); [176.2,296](https://tax.gov.ua/nk/). Route detailed calendars/returns to `ua-social-contributions`, `ua-payroll` and `ua-return-assembly`.

### 6. Open the correct account and establish records

NBU Instruction **162, paragraphs 9-13 and 24**, separates business/professional accounts from personal-use accounts and prohibits using personal-use current/payment accounts for business operations. Complete the provider's due diligence, valid ID/tax-number verification, current application and account contract. This does not prohibit every lawful cash receipt or prove all single-tax receipts must arrive by bank transfer. [Official Instruction 162](https://bank.gov.ua/admin_uploads/law/29072022_162.pdf?v=4).

Obtain the provider's actual account/tariff/FX documentation, payment credentials and evidence trail. The old claim of special monitoring lasting **roughly six months** for every new FOP is **Not yet confirmed**; ordinary due diligence is not that fixed rule. Personal drawings are not company dividends, but do not promise unrestricted withdrawals ignoring paid liabilities, banking/FX requirements or restricted funds. The opened DPS explanation supports general-system personal use **after all taxes/fees/payments are settled**; other cases require their actual conditions. [DPS account/funds explanation](https://dp.tax.gov.ua/media-ark/news-ark/945569.html).

Set up the correct income/expense records, primary-document archive and fiscalisation analysis before taking payments. The registration page's old tax-office book-registration instruction conflicts with current record rules; do not revive it. `ua-bookkeeping` owns free-form non-VAT single-tax monthly records versus the prescribed VAT/general forms and actual RRO/PRRO exceptions. Companies need their applicable accounting/financial-statement workflow.

### 7. Preserve the TOV route and its current service limit

Diia's model-charter TOV service currently displays **“послуга тимчасово недоступна”**. Do not promise completion online while it is unavailable. Its ordinary instructions describe charter choices, automatically produced application/charter/minutes or sole-founder decision/ownership structure, all founders signing, and conditional automatic processing when UBO identity data including УНЗР are verified. Otherwise it describes registrar processing. The page's **about one minute / one working day**, **free** registration and **three-working-day** extract estimates are normal service descriptions, not an availability or completion guarantee. Foreign applicants are directed to ЦНАП rather than this citizen-only online service. Refer counsel/current registrar for the actual alternative, beneficial-owner documentation and any notarized copies; no universal foreign-founder approval is given. [Full TOV service/FAQ](https://diia.gov.ua/services/reyestraciya-tov-na-pidstavi-modelnogo-statutu/).

### 8. Close a FOP without abandoning surviving obligations

The automatic **«Закриття ФОП»** service describes physical-person signature, automatic EDR/DPS transmission, status/notification and **free** processing, normally **up to one minute** after an approximately **two-minute** application. Confirm the actual entry and extracts; an estimate is not tax deregistration clearance. A representative route/foreign location/licences needs the stated conditions. [Official closure service](https://diia.gov.ua/services/avtomatichne-zakrittya-fop).

Prepare the final tax/own-ЄСВ package, settle outstanding single tax, levy, PIT and VAT, establish actual single-tax/VAT annulment and final periods, deal with employee/fiscal obligations, close the business bank account and cancel relevant licences. Closure does not erase liabilities or authorize record destruction. **Use Tax Code 177.11 for voluntary general-system closure:** the final business-only return follows the **monthly-period deadline**, with the last base period ending on the **last day of the closure month**. The Diia page's “30 days after closure” and “ten days after actual submission” shorthand is not adopted as the governing tax calendar. Own ЄСВ through the closure month depends on the actual liability/exemption and final schedule; no universal exemption-free bill is invented. [177.11,49,57](https://tax.gov.ua/nk/); `ua-return-assembly`.

Keep original records for the actual **44.3** category/start/extensions: ordinary residual category **1095 days**, specified company records **1825**, and **39/39-2/141.4** control records **2555**, plus audit/dispute/suspension holds and other legal requirements. The old “three years after closure” shortcut is not a disposal date. A closing review may occur; refer unresolved tax deregistration/debts, retention, litigation and TOV liquidation. [44.3-.4,102.3](https://tax.gov.ua/nk/); `ua-bookkeeping`.

## Worked cases

### Original A: Oksana, web developer with foreign clients

**Oksana** expects **1200000** receipts for US/EU development clients. Confirm ordinary resident FOP eligibility and actual service classification; **62.01** is a candidate only if its full description fits. She elects eligible **non-VAT Group 3 within ten days**, with the register confirming effect from registration. General system is also legally possible; “foreign means must Group 3” is withdrawn. Assuming a full year at ordinary rates, no relief and minimum own ЄСВ: single tax **60000**, levy **12000**, own ЄСВ **22828.08**, total allocation **94828.08**, derived. Although receipts exceed one million, **181.1's single-tax carveout** prevents that turnover alone forcing registration; imported services or other special VAT facts still need review. Sources: [291/293/298/181](https://tax.gov.ua/nk/), [ЄСВ figures](https://tax.gov.ua/media-tsentr/novini/999526.html).

```oa-check
name: Oksana full-year ordinary Group 3 cost allocation
inputs:
  receipts: 1200000
  single_rate: 0.05
  levy_rate: 0.01
  monthly_minimum_wage: 8647
  esv_rate: 0.22
  liable_months: 12
steps:
  single_tax: receipts * single_rate
  levy: receipts * levy_rate
  esv: monthly_minimum_wage * esv_rate * liable_months
  allocation: single_tax + levy + esv
expected:
  single_tax: 60000
  levy: 12000
  esv: 22828.08
  allocation: 94828.08
```

### Original B: Petro, local barber

**Petro** has **two employees**, serves the public and expects **900000** annual receipts. Test Group 2 and **96.02** against actual work and counting rules, not merely his job title. At the hypothetical **maximum local 20% rate**, no relief and a full liable year, monthly own allocation is **1729.40 +864.70 +1902.34 =4496.44**, annual **53957.28**, derived; staff payroll/ЄСВ are **additional**. Obtain the actual council rate. A new Group 2 application is due **registration month-end**, effect next month; the old ten-day checklist is corrected. [291.4,293,298.1.2,levy](https://tax.gov.ua/nk/); [ЄСВ](https://tax.gov.ua/media-tsentr/novini/999526.html); [96.02](https://kved.ukrstat.gov.ua/KVED2010/96/KVED10_96_02.html).

```oa-check
name: Petro illustrative maximum Group 2 own-cost budget
inputs:
  january_minimum_wage: 8647
  local_single_rate: 0.20
  fixed_levy_rate: 0.10
  esv_rate: 0.22
  liable_months: 12
steps:
  single_month: january_minimum_wage * local_single_rate
  levy_month: january_minimum_wage * fixed_levy_rate
  esv_month: january_minimum_wage * esv_rate
  monthly_total: single_month + levy_month + esv_month
  annual_total: monthly_total * liable_months
expected:
  single_month: 1729.40
  levy_month: 864.70
  esv_month: 1902.34
  monthly_total: 4496.44
  annual_total: 53957.28
```

### Original C: Maria & Andrii, SaaS co-founders

**Maria & Andrii** want shares, investment and a team; use a TOV/counsel route rather than treating one founder's FOP as jointly owned. Confirm current registration-channel availability, charter/UBO/capital decisions, actual ownership bar and income limit before electing Group 3. The old recommendation to choose **5% automatically**, or leave it solely to obtain VAT recovery, is withdrawn: an eligible **3%+VAT Group 3** branch also exists. Compare company accounts, CIT, founder distributions and any independently qualified Diia City proposal. No charter/liability or tax-election sign-off is issued here. [291.4-.5,293.3](https://tax.gov.ua/nk/); [TOV service](https://diia.gov.ua/services/reyestraciya-tov-na-pidstavi-modelnogo-statutu/).

### Original D: Ihor, a VAT-paying customer's contractor

**Ihor** receives approximately **3000000** annually from a Ukrainian VAT-paying client. Actual non-VAT Group 3 status is not lost merely for that turnover. A client's wish for credit prompts a **5% versus coordinated 3%+VAT** price/input-VAT/cash-flow comparison, not automatic registration or a promise that VAT is a flat extra cost. Confirm genuine contracting versus employment, actual place/rate, pricing, registration capacity and effective date; refer to `ukraine-vat`/`ua-einvoice`. [181-183,293.3/.8](https://tax.gov.ua/nk/).

## When to refuse or refer

Stop for foreign/nonresident or disputed-residence applicants; ambiguous/barred KVED, customer or staff tests; debt/sanctions; TOV charter/UBO/contribution/liability/distribution/liquidation work; VAT election/account/registration; missed or mid-year regime changes; own-ЄСВ relief; closure; or unresolved wartime procedures. Preserve all original prohibitions in corrected scope: no automatic ordinary election, no ineligible Group 1/2 service advice, no eligibility from memory, no turnover-only VAT mandate for Groups 1-3, no unsupported ЄСВ waiver, no extinguishment of liabilities on closure, and no unsigned final legal/tax output. No sham splitting, hidden receipts or invented documents.

Before handoff, confirm identity/tax number/address/status; actual channel/signature; primary/additional activities and all eligibility tests; election receipt/register/effective dates; general-system interim period; VAT decision and actual registration; own-ЄСВ payer/month/exemption evidence; separate business account/due diligence; downloaded EDR record; bookkeeping/fiscalisation; own versus employer calendar; and qualified review of all open items. A blank or sent application is not acceptance.

## Sources

| Official source | Read for | Read date |
|---|---|---|
| [DPS Tax Code consolidation](https://tax.gov.ua/nk/) | Read for 291.4 group conditions and 291.5.5-.8;293.1-.4;298.1.1-.5 complete election sequence;181.1-183.5 ordinary VAT registration;177.1-.4 expense/base and177.11 closure;167.1-.2;XX.10.16-1(1.1-1.7) levy. Prior same-pack 176.2/44.3/102.3 and193 reads/captures reused and explicitly bounded; not the whole Code or all special regimes | 2026-11-16; prior bounded reads 2026-11-15 |
| [Diia FOP service](https://diia.gov.ua/services/reyestraciya-fop) | Read for full operative workflow/result/FAQ, lines134-267: signature, transmission, timings, free service, extract, offline representative and bank option. Stale book instruction not adopted | 2026-11-16 |
| [Diia TOV service](https://diia.gov.ua/services/reyestraciya-tov-na-pidstavi-modelnogo-statutu/) | Read for full operative134-277: current unavailable notice, normal service estimates, charter/documents/UBO checks, all-founder signatures, foreign applicant referral and no minimum capital. Not a tested submission | 2026-11-16 |
| [Six KVED class pages,62.01 example](https://kved.ukrstat.gov.ua/KVED2010/62/KVED10_62_01.html) | Read for all six full class bodies and inclusion/exclusion lists, individually linked above;62.01,62.02,63.11,70.22,73.11,96.02. No automatic single-tax clearance | 2026-11-16 |
| [Statistics Order191](https://stat.gov.ua/uk/page-contents/nakaz-vid-28102025-no191) | Read for whole operative order: NACE2.1-UA approval/effective date and methodological implementation. Not all future transition rules or classifier mappings | 2026-11-16 |
| [Budget4695-IX official-host enacted PDF](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) | Read for preserved same-pack original33-page PDF art7/8,32 and relevant suspension provision, with independent captures/review; original read retained, not relabelled as a new read. Later amendments not all read | 2026-11-15 |
| [DPS2026 own-ЄСВ figures](https://tax.gov.ua/media-tsentr/novini/999526.html) | Read for whole operative142-165 including wage,22%,minimum,maximum and20-wage cap | 2026-11-16 |
| [DPS general/simplified bases](https://sumy.tax.gov.ua/media-ark/news-ark/977379.html) | Read for full operative65-70: separate bases and general-system no-profit branch. Its maximum-base prose typo is resolved using national DPS figures, not copied | 2026-11-16 |
| [Current employer-paid exemption](https://zir.tax.gov.ua/main/bz/view/?id=43912&src=ques) | Read for full current answer, monthly actual-paid-minimum test,2026 employer list, below-minimum/no-profit distinctions and no main-job prerequisite; prior same-pack record also retained | 2026-11-16 |
| [DPS own-ЄСВ payment](https://zak.tax.gov.ua/media-ark/news-ark/981527.html) | Read for full operative66-75:19th inclusive and next-working-day adjustment, with e-resident exclusion. No blanket20th deadline | 2026-11-16 |
| [NBU Instruction162](https://bank.gov.ua/admin_uploads/law/29072022_162.pdf?v=4) | Read for9-13 and24 with neighbors: due diligence, separate accounts, contract and prohibition on personal-use business transactions. Not whole instrument or all later FX amendments | 2026-11-16 |
| [DPS drawings/account explanation](https://dp.tax.gov.ua/media-ark/news-ark/945569.html) | Read for operative66-73: general-system personal use after taxes/fees/payments and separate-account explanation. Not universal Group3/FX withdrawal clearance | 2026-11-16 |
| [Diia closure service](https://diia.gov.ua/services/avtomatichne-zakrittya-fop) | Read for full operative134-245: registration/notification, bank/licence/representative steps and FAQ; tax-period shortcuts rejected against177.11 | 2026-11-16 |
| [DPS/NACP FOP property explanation](https://lg.tax.gov.ua/media-ark/news-ark/1066916.html) | Read for complete operative66-88. Confirms personal-property exposure, but its former Commercial Code citation is not adopted as current authority | 2026-11-16 |
| [AMCU2024 decision477-р](https://amcu.gov.ua/static-objects/amcu/uploads/public/675/abc/bd9/675abcbd9f2a5823893562.pdf) | Read for dated capital discussion printedp32,1431-1446, charter exception and distinction between initial/additional contributions. Not full current2275-VIII or current contribution-calendar clearance | 2026-11-16 |
| [DPS paid-ЄСВ expense timing](https://cv.tax.gov.ua/media-ark/news-ark/977945.html) | Read for full operative65-81:177.4.3,Order261 actual-payment record and supporting evidence; contribution accrual and expense payment are distinct | 2026-11-16 |

Not yet confirmed: full current Laws755-IV/2275-VIII/2464-VI and every foreign-founder/residence/document exception; current Form1 attachments and statutory processing guarantee; universal permitted number of KVED codes or old5-7 practice; actual future NACE transition/registration procedure; provider signature/bank/notary prices or same-day timings; universal six-month enhanced monitoring; precise company contribution timetable, liability and UBO particulars; every own-ЄСВ relief/registration/final-month condition; all current special VAT/FX/closure/retention procedures and actual portal schema. Failed Rada/ordinary-browser access and failed downloads are not read evidence. Unconfirmed items are held, not usable default instructions.

Original **PwC Worldwide Tax Summaries** pointer is retained as withdrawn secondary research provenance, not an authority or a claim of reading. Official register/source links above and domain owners replace the old blanket May2026 verification assertion.

## Disclaimer

This is bounded source-cited reference material for2026, contributed by Open Accountants Community and pending sign-off by a qualified Ukrainian accountant. It is general information, not tax, legal or accounting advice and creates no professional relationship. Every actual output requires current source/fact checks and qualified review before any taxpayer or authority relies on it. Part of the Open Accountants open-source tax-skills project; **openaccountants.com**.
