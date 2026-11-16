---
name: ua-tax-overview
description: "A one-page map of the Ukrainian tax system for tax year 2026, from the Tax Code of Ukraine as consolidated on zakon.rada.gov.ua with the martial-law amendments to October 2026. Covers the tax year, currency, the tax authority, who is resident, personal income tax at 18% (5% and 9% on dividends), the military levy (5% for individuals, 1% for single-tax group 3, 10% of the minimum wage for groups 1, 2 and 4, none on company profit), corporate income tax at 18% with 25% for financial institutions and 50% for banks in 2026, the 15% withholding on payments to non-residents, the single-tax groups, VAT at 20%, 14%, 7% and 0% with the UAH 1,000,000 registration threshold, and the main filing and payment deadlines. Use for 'how does tax work in Ukraine', 'Ukraine tax overview', 'Ukraine tax rates 2026'. It points to the pack's domain skills for the detail: ua-income-tax, ua-corporate-income-tax, ukraine-vat, ua-single-tax, ua-social-contributions, ua-payroll, ua-crypto-tax, ua-tax-optimization."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ua-tax-overview"
  jurisdiction: "UA"
  tax_year: "2026"
  last_updated: "2026-11-15"
---

# Ukraine Tax Overview v 0.4

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Start here: the map and required inputs

This is the **2026 routing map**, not a full tax computation or filing instruction. It preserves the original one-page map's subject coverage; the conditions need more space. Load the relevant domain skill below for the actual computation, forms, exceptions and review. An unchanged sibling's date, rate or passing script does not override current law: reconcile a conflict against the official provision and refer the unresolved branch before use.

All Tax Code references below mean Law 2755-VI of 2 December 2010, read in the **official Tax Service consolidated publication**, in the specific scopes in Sources. The old overview's October archive cutoff is not inherited as a current read claim. This review does not attest that every amendment or all provisions of the Code were read. The Code's transitional rules refer to martial law introduced by Decree 64/2022 of 24 February 2022; military-levy, bank-year and VAT-invoice provisions have **different** time conditions. Do not infer one blanket wartime tax waiver. [Code and transitional references](https://tax.gov.ua/nk/).

Obtain or reuse existing documented answers before choosing a route:

- Person, FOP or legal entity; Ukraine and foreign residence evidence, homes, family/economic ties and actual days. Citizenship alone does not skip earlier domestic tests or treaty analysis.
- Income type, source, payer/payee, receipt/accrual dates, gross versus statutory net base, currency and actual receipt-rate evidence. Dividends, salary, business and crypto are separate routes.
- Effective single-tax group/rate/register extract, actual activities/customer types, employees, year-to-date statutory income and any transition dates. A freelancer is not automatically an eligible Group 3 payer.
- VAT status/dates, supplies by place/type and rolling turnover, imports/nonresident services; company bank/financial/insurance/Diia City status and elections if relevant.
- Reporting period, already withheld/declared/paid amounts, required owner outputs, special relief/election evidence, and an actual official calendar for any date to be acted on.

Missing evidence is not a default, zero, exemption or filing-ready answer. The output is a routing/reconciliation brief with source, period, questions still unresolved and the qualified review needed.

## The method, step by step

### 1. Establish the tax frame and residence

| Item | Rule and boundary | Official source |
|---|---|---|
| Tax periods | Code 34.1 permits calendar year, half-year, three quarters, quarter, month or day. Ordinary personal annual reporting uses a calendar year. CIT 137.4 ordinarily uses calendar periods, but qualifying agricultural producers may choose **1 July to 30 June** only where revenue from sales of **their own-produced agricultural products in the prior tax/reporting year exceeds 50% of total revenue** under 137.4.1; newly registered and liquidated taxpayers have special first/last periods. Do not force every return onto 1 January-31 December | [34.1,49.18.4,137.4](https://tax.gov.ua/nk/) |
| Currency | UAH. Taxes paid in money in Ukraine's national currency except where the Code or customs legislation provides otherwise. This is not a rule that all income originally arrives in UAH | [35.1](https://tax.gov.ua/nk/) |
| Authority/channel | State Tax Service of Ukraine, Державна податкова служба України, [official site](https://tax.gov.ua/), implements tax policy under 41.1.1; customs has its separate 41.1.2 role. Electronic Cabinet is a filing channel.49.3 allows specified personal/post/electronic channels unless a special rule applies;49.4 makes VAT reporting electronic. Check the actual form/channel | [41.1,49.3-49.5](https://tax.gov.ua/nk/) |
| Personal domestic residence | Start with residence in Ukraine. Where also resident abroad, test permanent home, then closer personal/economic ties (centre of vital interests). If centre cannot be determined or neither state has a permanent home, the domestic rule uses presence in Ukraine **at least 183 days**, including arrival/departure days, in the tax year. Citizenship is a later fallback where preceding tests fail. Family's permanent home or business registration is **sufficient but not exclusive** centre evidence. The definition also addresses self-determination of main home/self-employed registration; e-resident status alone is insufficient. Stateless/multiple-citizenship disputes need specialist review, not a shortcut | [14.1.213](https://tax.gov.ua/nk/) |
| Company domestic residence | Legal persons and their separate units formed and operating under Ukrainian law, wherever located, fall within 14.1.213(a). Foreign formation, management, permanent establishment or dual-residence issues need the company/cross-border owner; this line does not settle them | [14.1.213(a)](https://tax.gov.ua/nk/) |
| Individual taxable scope | Residents: total taxable monthly/annual income, Ukraine-source income finally taxed on accrual/payment/provision, and foreign income. Nonresidents: relevant Ukraine-source income. Exemptions, source definitions and treaty treatment still matter. A ratified treaty's different rule prevails under 3.2; this overview supplies no treaty entitlement/rate | [163.1-163.2,3.2](https://tax.gov.ua/nk/) |

### 2. Route personal income and the separate military levy

| Item | 2026 headline with conditions | Official source |
|---|---|---|
| Ordinary PIT | **18%** of the applicable tax base, including ordinary salary/employment income; not a rate for every receipt. General FOP net-income, rental, investment, property sale, gifts/inheritance and tax discount go to `ua-income-tax`; salary to `ua-payroll` | [167.1,163-164](https://tax.gov.ua/nk/) |
| Dividends and passive income | **5%** for qualifying dividends from resident CIT-paying issuers, **except collective investment institutions**. **9%**, derived as half 18%, for dividends from nonresidents, collective investment institutions and non-CIT payers. Other passive income ordinarily **18%**, subject to the Code's specific exceptions and dividend classifications. Do not classify every distribution solely by the issuer's address | [167.5.1-167.5.4](https://tax.gov.ua/nk/) |
| Ordinary individual levy | **5%** of the relevant 163 object under XX.10.16-1, with its **own exemption rules**. “Exactly the same exempt base as PIT” is unsafe:1.7 has explicit exceptions. Certain specified service-member/security payments use **1.5%**, not a blanket service-person rate on all income. The 1.7 wartime allowance exemption requires the specified service status, payment and **direct-participation period** with the Cabinet-confirmed status; it is not all military allowance throughout martial law | [XX.10.16-1,1.1-1.3/1.7](https://tax.gov.ua/nk/) |
| Fixed entrepreneur levy | For ordinary eligible FOPs in Groups**1,2,4**, **10% of 1 January minimum wage per calendar month**, derived **UAH 864.70** for 2026 from 8647. Not 10% ofrevenue; actual statutory relief and group/time conditions must be checked by the owner | [XX.10.16-1,1.1-1.3/1.12-1.13](https://tax.gov.ua/nk/); [Budget8](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) |
| Group 3 levy | **1%** of article 292 income for Group 3 FOPs **and legal entities**, excluding e-residents. Separate from the 3%/5% single tax and from ordinary personal 5% levy | [XX.10.16-1,1.1-1.3](https://tax.gov.ua/nk/) |
| Levy duration | Overall 16-1 header refers to Parliament's decision completing Armed Forces reform. The specific entrepreneur/Group 3 levy window is **1 January 2025 through 31 December of the third calendar year after the year martial law ends/cancels**. Under the current 4835-IX amendments, the ordinary individual's 5% rate changes to **1.5% from 1 January of the next year after that third year**. Do not treat the first day after martial law as a universal end date | [XX.10.16-1,1.1/1.3,4835-IX](https://tax.gov.ua/nk/) |
| Annual individual declaration | Where required, **before 1 May** following the reporting year under 49.18.4, not “by 1 May”.179.2/.4 contain nonfiling cases: not every individual files. Ordinary self-declared individual balance is payable **before 1 August**, not “by 1 August”. A resident leaving for permanent residence abroad files **at least 60 calendar days before departure**. FOP business settlement uses the separate 57/177 route, not automatically the personalAugust rule | [49.18.4,49.20,179.2-179.7,57.1/177.5](https://tax.gov.ua/nk/) |

**Future-calendar correction:** the old 2026-income line began with 1 May 2027 Saturday and shifted it. The statute says **before 1 May**, so the ordinary last date is **30 April 2027 Friday, derived**, before checking an official 2027 calendar or individual extension. It is retained as planning arithmetic only and is **not a released filing instruction**. The old **1 March 2027** annual-CIT date is likewise a **derived 60-day calendar point**, not an opened official 2027 calendar. Confirm both with the period's actual official calendar before use.

### 3. Route registered simplified-system business

The following are ordinary headline groups, not proof of eligibility. Actual 291.3/.5 bars,291.6 settlement method, registration, activity and group restrictions must be checked. A service-customer restriction is not a blanket bar on selling goods to companies. Nonresidents and excluded activities cannot be assumed eligible.

| Group | Headline eligibility and cap | Official source |
|---|---|---|
| 1 | No employees; market-stall retail and/or 291.7 listed household services to the public. **167** January minimum wages, derived **UAH 1,444,049** in 2026. Not all freelance services | [291.4(1),291.7](https://tax.gov.ua/nk/); [Budget8](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) |
| 2 | Services to single-tax payers/public, production/sale of goods, restaurants; counted employees **at most 10 simultaneously**, with 291.4.1 maternity/childcare/mobilized counting exceptions. **834** January minimum wages, derived **UAH 7,211,598**. Specified real-estate/internet-access/commercial-jewellery restrictions require separate group review;291.7 household jewellery making/repair is a distinct branch | [291.4(2),291.4.1,291.7](https://tax.gov.ua/nk/); [Budget8](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) |
| 3 | Eligible FOPs with no employee-number restriction and eligible legal entities; **1167** January minimum wages, derived **UAH 10,091,049**. E-residents have their own conditions, not this generic FOP route | [291.4(3),291.5](https://tax.gov.ua/nk/); [Budget8](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) |
| 4 | Agricultural companies generally require **at least 75%** prior-year agricultural-production share; qualifying family-farm FOPs must meet all 291.4(4)conditions. The percentage alone is not entry approval; full farm tax computation is referred | [291.4(4),291.5-1](https://tax.gov.ua/nk/) |

| Rate/base | Ordinary headline, not full burden | Official source |
|---|---|---|
| January reference amounts | From 1 January 2026, able-bodied subsistence minimum **UAH 3328/month** and minimum wage **UAH 8647/month**. These are the categories/pinned January bases used here, not every subsistence category | [Budget7-8,original enactedPDF](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) |
| Group 1 | Local council rate at most **10%** of January able-bodied subsistence minimum monthly; derived ceiling **UAH 332.80**. Local activity/location rate and relief can differ | [293.1-293.2,293.6-293.7,295.5](https://tax.gov.ua/nk/); [Budget7](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) |
| Group 2 | Local council rate at most **20%** of January minimum wage monthly; derived ceiling **UAH 1729.40**. Do not automatically use the ceiling for every taxpayer | [293.1-293.2,293.6-293.7,295.5](https://tax.gov.ua/nk/); [Budget8](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) |
| Group 3 ordinary | **3%** of 292 income with separate registered VAT, or **5%** where VAT is included in the single tax. Applies to eligible FOP/legal-person route; rate/VAT election effective dates must agree. No expense-netting from gross statutory income | [293.3,292](https://tax.gov.ua/nk/) |
| FOP affected income | **15%** on the specified 293.4 income: cap excess, unregistered Group 1/2 activity, nonpermitted settlements, barred activity (e-resident exception as written), or activity outside the actual Group 1/2 definition. Not ordinary rate plus 15% on the same excess; group change/exit and other consequences remain separate | [293.4,293.8,298.2.3](https://tax.gov.ua/nk/) |
| Group 3 legal-person affected income | Double the 293.3 rate, derived **6% or 10%**, for the **three 293.5 categories**: excess, nonpermitted settlement, barred activity. Not an automatic copy of every FOP 293.4 category | [293.5](https://tax.gov.ua/nk/) |
| Period and own ЄСВ | Ordinary Groups**1,2,4** calendar year; Group**3** quarter, with specific 294/296 exceptions and cumulative reporting. Own ЄСВ is a **separate-law** liability, not covered by a headline single-tax percentage. Load `ua-social-contributions` and check its actual current calendar/relief evidence | [294.1-294.7,296.2-296.7](https://tax.gov.ua/nk/); separate contribution-law details not approved by this map |

### 4. Route company profit and payments abroad

| Item | Headline with conditions | Official source |
|---|---|---|
| Ordinary CIT | **18%** of the relevant taxable profit/base | [136.1](https://tax.gov.ua/nk/) |
| Financial institutions, except insurers | **25%**, including specified CFC/dividend-advance contexts in 136.1-1. The bank 2026 override below controls banks; insurer exceptions are separate | [136.1-1](https://tax.gov.ua/nk/) |
| Banks in 2026 | **50%** for 2026 reporting periods and dividend advances at 50%. XX.4.73 also disallows the 140.4.4 prior-loss reduction in 2026; unused earlier/2026 negative amount is taken into account from 1 January 2027 **under 140.4.4 conditions**. This map does not establish a 2027 bank rate or compute future loss use | [XX.4.73](https://tax.gov.ua/nk/) |
| Insurers | Income tax **3%** on relevant insurance-contract income, or **0%** on specified qualifying long-term-life, voluntary-medical and nonstate-pension contracts, **alongside ordinary 18% CIT**. Statutory contract definitions matter; not all insurance proceeds qualify for 0% | [136.2,136.5](https://tax.gov.ua/nk/) |
| Elected Diia City special regime | **9%** of the special statutory base, with 136.8 exceptions referring to 141.9-1.2.16/.17 and 141.9-1.3/.4; not 9% ofallprofits or only dividends. Load `ua-tax-optimization` and company specialist for eligibility, election and transaction classification | [136.8](https://tax.gov.ua/nk/) |
| Nonresident withholding | Ordinary **15%** on specified 141.4.1 Ukraine-source income paid by the relevant resident/PE payer, unless an applicable treaty changes treatment, with 141.4.4/.5/.11 exceptions. Ordinary goods/work/service compensation is excluded from the residual 141.4.1(k)category, but another enumerated category may apply. FOP/single-tax payer status is not blanket payor exemption. PE cases, treaty evidence, special payments, noncash/unwithheld gross-up and transactions abroad require the owner; not every foreign invoice is 15% | [141.4.1-141.4.2](https://tax.gov.ua/nk/) |
| Company and levy | CIT-paying company profit is not itself an ordinary military-levy object. Employer/personal withholding remains separate; **Group 3 legal entities do pay the 1% levy on 292 income**, so “no levy for companies” is too broad | [XX.10.16-1,1.1-1.3](https://tax.gov.ua/nk/) |
| CIT reporting and payment | Ordinary quarterly cumulative reporting: **40 calendar days** after quarter/half-year/three quarters. Calendar-year annual return, including quarterly filers' annual cumulative return: **60 calendar days**.137.5 has annual-filer classes, including new businesses, agricultural producers and specified revenue/other categories; determine the actual class first. Tax ordinarily **10 calendar days** after the statutory filing deadline under 57.1, with its payment adjustment; not 10 daysafteractualearlysubmission | [49.18.2/.3/.6,49.19-49.20,57.1,137.4-137.5](https://tax.gov.ua/nk/) |

### 5. Route VAT by transaction and status

| Item | Headline with complete routing boundary | Official source |
|---|---|---|
| Ordinary rate | **20%** standard under 193.1(a), unless a specific reduced/zero/exempt/outside-scope rule applies | [193.1,194](https://tax.gov.ua/nk/) |
| Zero rate | **0%** only for qualifying exports/listed 195 transactions; goods export needs the statutory customs confirmation. Foreign services are not automatically zero-rated goods exports. Special agricultural-export 97 rules can change initial treatment; this map does not compute them | [193.1(b),195.1.1;special97referral](https://tax.gov.ua/nk/) |
| Reduced 7% | **7%** for specifically qualifying medicines/devices/authorized clinical or expanded-access cases and listed culture/museum/accessible-film, hotel**55.10**, sporting-event ticket supplies. Classification, registration/authorization and exact statutory descriptions matter; not all medical/cultural/hotel services | [193.1(c)](https://tax.gov.ua/nk/) |
| Reduced 14% | **14%** for listed agricultural goods classified under**1001,1003,1005,1201,1205,120600**, with source/transaction and any special export conditions. Not all agricultural produce | [193.1(d)](https://tax.gov.ua/nk/) |
| Ordinary registration test | Taxable supplies **overUAH 1,000,000 excludingVAT over the last 12 calendar months**, not the calendar year.181.1 carves out Group 1-3 single-tax payers; that is not a universal VAT exemption. Voluntary registration under 182.1, importVAT under 181.2 and nonresident-service liability under 180.2/208 can still matter | [180.2,181.1-181.2,182.1](https://tax.gov.ua/nk/) |
| Ordinary VAT return/payment | Monthly, file within **20 calendar days** after the reporting month; pay within **10 calendar days** after the statutory 203.1 deadline, with applicable payment calendar. First/last periods differ under 202.1. Not invariably the 30 th or ten days after an actual early filing | [202.1,203.1-203.2,49.20,57.1](https://tax.gov.ua/nk/) |
| Tax invoices | Registered VAT sellers' tax invoices/adjustments require Unified Register registration under 201.10, including specified invoices not handed to buyers/exempt supplies. Registration/input credit, correction responsibility, martial-law deadlines and 120-1 penalties need `ukraine-vat`/`ua-einvoice`; no generic wartime relief is granted here | [201.8-201.10](https://tax.gov.ua/nk/) |

### 6. Load the original domain routes and hand off

| Question | Skill and required handoff |
|---|---|
| Individual salary, investment, rent, property sales, gifts/inheritance, general-system FOP net profit, annual declaration or tax discount | `ua-income-tax`; facts/source/classification/period, deductions/credits and residence/treaty questions |
| Company profit, bank/financial rates or withholding abroad | `ua-corporate-income-tax`; company/election/period, accounting base, payment type and treaty/PE evidence |
| VAT registration, rates, tax invoices or monthly return | `ukraine-vat`; registration/tax-point/supply/place/customs and invoice evidence |
| Single-tax groups, limits and rates | `ua-single-tax`; actual registered group/rate, eligibility,292 income, effective transitions and cap screening |
| Own entrepreneur ЄСВ | `ua-social-contributions`; separate monthly liability/exemption evidence and current payment calendar |
| Hiring/payroll PIT, levy and ЄСВ | `ua-payroll`; pay/status/months, tax-agent reporting and employer contributions separately |
| Crypto/virtual assets | `ua-crypto-tax`; transaction/cost/source/status evidence; do not treat proposed rules as enacted from this map |
| Lawful reduction and Diia City | `ua-tax-optimization`; lawful alternatives, eligibility/election facts and comparable full costs |
| Register a business | `ua-formation`; intended real activity, clients, entity/liability and registration/tax-election effective dates |

Return a concise brief naming every selected owner, its version/date, the facts supplied, assumptions expressly approved, calculation owner and unresolved branch. No domain instruction is treated as an authority that defeats a newer official provision.

## Worked cases: reconcile owner outputs, do not certify a return

**A. Ordinary taxable salary route, hypothetical.** The payroll owner has verified a 100000 UAHtaxable salary base, ordinary 18% PIT and 5% levy, no special relief/credit. PIT 18000 pluslevy 5000 is 23000; salary after those deductions 77000. Employer ЄСВ is a separate cost and is not deducted here. This is not a decision that an actual payment is salary/taxable. [167.1;XX.10.16-1](https://tax.gov.ua/nk/).

```oa-check
name: Separate PIT and levy payroll owner reconciliation
inputs:
  verified_salary_base: 100000
  imported_pit_rate: 0.18
  imported_levy_rate: 0.05
steps:
  pit: verified_salary_base * imported_pit_rate
  levy: verified_salary_base * imported_levy_rate
  total_withholding: pit + levy
  salary_after_these_deductions: verified_salary_base - total_withholding
expected:
  pit: 18000
  levy: 5000
  total_withholding: 23000
  salary_after_these_deductions: 77000
```

**B. Eligible ordinary Group 3 non-VAT route, hypothetical.** Single-tax owner confirms registered 5% status,100000 UAHarticle 292 income, no cap excess/barred income or transition; separate levy owner confirms 1%. Single tax 5000 pluslevy 1000 is 6000;94000 remains **before own ЄСВ and other expenses/liabilities**. The separate contribution input is missing, so this is **not the full tax burden or final spendable/net profit**. No invented contribution rate is plugged into the router. [293.3;XX.10.16-1](https://tax.gov.ua/nk/).

```oa-check
name: Group3 ordinary taxes exclude missing contribution output
inputs:
  verified_article292_income: 100000
  imported_single_tax_rate: 0.05
  imported_levy_rate: 0.01
steps:
  single_tax: verified_article292_income * imported_single_tax_rate
  separate_levy: verified_article292_income * imported_levy_rate
  known_tax_subtotal: single_tax + separate_levy
  balance_before_other_liabilities: verified_article292_income - known_tax_subtotal
expected:
  single_tax: 5000
  separate_levy: 1000
  known_tax_subtotal: 6000
  balance_before_other_liabilities: 94000
```

## When to refuse or refer

- Stop before filing/payment or a final answer if residence, status, actual activity, income classification, period, source document, exchange rate, owner output or amount reconciliation is missing/conflicting. A rate headline does not choose an entity or regime.
- Refer residence/treaty/nonresident withholding/PE, special dividend/passive-income treatment, service-person relief, farm/land, bank losses, insurance and Diia City election/transaction issues to the competent owner and qualified professional. This map approves none of those facts.
- Do not apply unsupported levy exemptions, presume all companies have no levy, levy 15% onallforeignpayments, use a cap from a rounded million amount, or call all foreign services zero-rated exports.
- Do not use future derived dates as released calendar advice, assume all filers use the same electronic form, confuse filing with payment, or turn wartime provisions into blanket tax/penalty/contribution relief.
- Preserve the original 9 domain routes, source/version evidence and open items. If a protected sibling differs, document and resolve against actual law, then route a separate correction; do not edit an approved/passing file as a side effect.

## Sources

| Official source | Read for | Read date |
|---|---|---|
| [Tax Code, official State Tax Service consolidated publication](https://tax.gov.ua/nk/) | Read for 3.2;14.1.213;34.1/35.1/41.1;49.3-.5/49.18-.20/57.1;136/137.4-.5;141.4.1-.2 relevant income/exclusion/payor/exception/grossup paragraphs;163.1-163.2/164.1/164.2.1/167/179.2-.9;180.2/181-183;193.1/194/195.1.1;201.8-.10 operative registration/credit/receipt paragraphs;202-203;291-296/298 ordinary simplified route;XX.4.73;XX.10.16-1 including 4835 duration/serviceexceptions;transitionalDecree 64/2022 references. Neighbor conditions read; not entireCode/full 97 agriculturalexport/specialinsurance/treaty/DiiaCitycomputation | 2026-11-15 |
| [Budget2026original enacted law4695-IX, official Odesa Finance Department PDF](https://gfu.od.gov.ua/wp-content/uploads/2025/12/pro-derzhavnyj-byudzhet-ukrayiny-na-2026-rik-zakon-%E2%84%96-4695-ix-vid-03.12.2025-d550190-20251203.pdf) | Read for 7/8 January able-bodied subsistence/minimum wage onPDFp 3, neighboring categories; original law, not all later amendments. Same-day prior single-tax review also read 32/contribution suspension but this map does not compute those liabilities | 2026-11-15 |

Not yet confirmed: all later Budget amendments' complete history and an independently opened final 2027 filing/payment calendar; released 2026 annual forms/schema/individual extensions; actual future bank rate; full current ownЄСВlaw/rates/bases/relief/calendar by this overview; specific treaties/residence/credit entitlements; complete special insurance/DiiaCity/farm/97 agricultural-export computations; individual levy exemption/service status and duration facts; any amendments beyond actually read scopes. Old 1 May 2027 shift and 1 March 2027 claims are retained only as corrected/held planning references, not filing instructions. No actual taxpayer conclusion or accountant approval.

## Disclaimer

This skill provides general routing/reference information. Every actual tax computation, election, deadline, filing or payment requires its domain evidence and review by a qualified Ukrainian professional. It is not a signed return or an attestation of an individual position.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-15. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ua-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ua-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
