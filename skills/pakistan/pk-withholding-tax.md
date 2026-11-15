---
name: pk-withholding-tax
description: Use for pakistan income-tax withholding by payment and period. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return.
jurisdiction: PK
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
version: 1.1
type: computation
---

# Pakistan income-tax withholding by payment and period v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Pakistan withholding agents and recipients preparing normal tax-year 2026 working papers (1 July 2025-30 June 2026). The rates below come from the Finance Act 2025 consolidation; a later payment requires the later law, rather than a 2026 label pasted on an old table. This covers income tax, not provincial sales-tax withholding, customs duties, federal excise or employer welfare contributions. Use `pk-payroll`, `pk-it-export-tax`, `pk-cgt` and `pk-sales-tax-services` for their owner computations.

Quick answer: identify payer obligation, recipient residence, payment limb, actual tax point, statutory base and applicable status/certificate before multiplying. Unknown classification is a pending item, not permission to apply the highest guessed rate.

## Ask the client first

Obtain payer legal form/NTN and prescribed-person evidence; recipient legal name/CNIC/NTN/residence and PE facts; actual payment dates and s.151 credit dates; contract/invoices with goods/services/sales tax separately identified; gross payment and currency evidence; dated ATL evidence; actual valid lower/exemption certificate; tax period; prior deductions/payments/CPRs. For imports obtain GD, PCT/Twelfth Schedule classification, own-use/commercial status and all customs/FED/sales-tax components. For treaty claims obtain actual treaty/protocol text, residence and beneficial-ownership/PE/anti-abuse evidence; do not invent a Pakistan requirement called Form 10 F.

## Rates, bands and thresholds

Each table entry remains subject to the payment limb's exceptions and a valid applicable certificate. Rates are on the **recipient's** company/other status, not the payer's status. [ITO First Schedule Parts II/III](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

| Tax-year 2026 payment and complete boundary | Base rate before applicable Tenth Schedule rule | Source |
|---|---|---|
| s.148 imports, Twelfth Schedule Part I | 1%; special classifications/notifications still tested | [s.148; First Schedule Part II](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.148 Part II | 2%, or 3.5% for commercial importer | [First Schedule Part II](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.148 Part III | 5.5%, or 6% for commercial importer | [First Schedule Part II](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.149 employment salary | Estimated annual salary average-rate method; load `pk-payroll`, not business slabs | [s.149](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.150 ordinary dividend outside specified special categories | 15%; special IPP/fund/REIT and other schedule branches need their actual conditions | [First Schedule Part III Div I](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.151 bank/financial-institution account/deposit profit | 20% | [First Schedule Part III Div IA(a)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.151 government-security profit to a person other than an individual | 20% | [Div IA(b)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.151 other profit within this division | 15%; do not confuse sukuk's separate division | [Div IA(c)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.152(1 A) specified non-resident contract | 7%, with PE/treaty/recipient-regime assessment | [Part III Div II(1)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.152(1 AA) non-resident insurance/reinsurance premium | 5% | [Div II(1 A)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.152(2) other chargeable non-resident payments | 20%; examine exclusions and treaty before using a default | [Div II(2)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.153(1)(a) ordinary goods to company recipient | 5%; toll manufacturing 9% | [Part III Div III(1)(b)(i)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.153(1)(a) ordinary goods to other recipient | 5.5%; toll manufacturing 11% | [Div III(1)(b)(ii)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.153 rice, cotton-seed oil or edible oils | 1.5%; not a generic food concession | [Div III(1)(a) and explanation](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.153(1)(b) specified listed services | 6%; IT/IT-enabled services as defined in s.2 have 4% proviso; explanation requires gross-receipt withholding and no court agitation of gross-receipt taxation | [Div III(2)(i)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.153(1)(b) other services | 15%; print/electronic-media advertising proviso 1.5% | [Div III(2)(ii)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.153(1)(c) contracts to company / other recipient | 7.5% /8%; sportsperson category 15%, not s.153(2) | [Div III(3)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.155 individual/AOP annual rent up to 300,000 | 0 | [Part III Div V](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Annual rent over 300,000 to 600,000 | 5% of excess over 300,000 | [Div V](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Annual rent over 600,000 to 2,000,000 | 15,000+10% of excess over 600,000 | [Div V](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Annual rent over 2,000,000 | 155,000+25% of excess over 2,000,000; no invented 4,100,000 extra band | [Div V](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.155 company recipient rent | 15% | [Div V](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |

The specified-services list includes transport, freight forwarding, air cargo, courier, manpower outsourcing, hotel, security guarding, software/IT/ITeS, tracking, non-print/electronic-media advertising, share registrar, engineering/architecture, warehousing, asset management, PTA-licensed data, telecom towers, car rental, building maintenance, PSX/PMEX, inspection/certification/testing/training, oilfield, telecom, collateral management, travel/tour, REIT management and NCCPL. Read the exact category and explanation; a low margin alone does not qualify. [Div III(2)(i)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

### ATL and statutory tax point

Tenth Schedule rule 1 generally increases applicable tax by 100%, but the Schedule has express exclusions and special branches. **Salary s.149, goods exports s.154 and services exports s.154A are excluded by rule 10(a),(c),(ca)**. Most s.152 limbs are also excluded except the specified s.152(2 A)(a)-(c) branches. Do not double every table entry. Retain dated actual ATL evidence and apply the actual section's law, including distinct property/vehicle provisions where relevant. The 2025 text's property late-filer rule 1A was omitted by Finance Act 2026 amendment 47(a); do not reuse it for events on or after 1 July 2026. [Enacted amendment](https://download1.fbr.gov.pk/Docs/20266291261044366FinanceAct2026.pdf). [Tenth Schedule rules 1/10](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

Section 158(a) uses **paid or credited, whichever earlier, for s.151**. Other cases use actual payment under s.158(b), subject to prescribed meaning and the specific charging provision. The old universal earlier-of-accrual/payment statement is an omitted historical version, not the current operative rule. Section 71 governs currency conversion evidence; a contract does not override the statutory method. [ss.71/158](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

## The method, step by step

1. Establish whether the payer is obliged. Section 153 prescribed persons include government, companies, statutory AOPs, NPOs, foreign contractors/consultants, consortium/JVs, exporters for s.153(2), builders/developers and specified intermediaries. The AOP/individual and relevant sales-tax-registered branches use turnover of **100,000,000 or more in any preceding tax year**, not the old 50,000,000 AOP test. Do not assume every small individual is prescribed. [s.153(7)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).
2. Classify the real payment. Resident goods/services/contracts, non-resident/PE payments, employment, rent, finance and distributions require their own limbs. A goods-plus-installation invoice is not automatically a contract without reading the contract and law. Separate income-tax and sales-tax withholding determinations.
3. For s.153(1), use gross amount payable **including sales tax, if any**. Do not strip the tax from the income-tax withholding base. For ordinary s.148 non-retail-price goods, the statutory value includes customs value plus customs duty, FED and sales tax; retail-price and notified-minimum-value branches differ. [ss.148(9)/153(1)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).
4. Apply actual applicable certificate, period/section/payer/recipient limits and status. Section 159 supports exempt/lower-rate/100%-credit amounts on application; low margin alone is not a general exemption. The separate s.153(4) non-minimum-tax reduced-rate branch has its own conditions, maximum reduction and company timing. Do not assume every minimum-tax service can obtain a 2% certificate. [ss.153(4)/159](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).
5. Reconcile deduction, gross payment, recipient net and actual deposit. Keep current PSID/payment instruction, CPR/GD, certificate/status evidence and quarterly statement reconciled; unknown posting delays or screen names must not be promised.

## Minimum, final and adjustable treatment

Withholding is not automatically final or refundable. Section 153(3) generally imposes minimum tax, with ordinary-goods exceptions for a manufacturer company and listed public company, and adjustable listed-public-company contract receipts. A private company service receipt is not adjustable merely because the recipient is a company. Section 148(7) generally uses minimum tax with industrial-own-use exception, while s.148(7 A) has mandatory minimum-tax categories including edible oil, packaging material, paper/board and plastics. Preserve the actual exception/notification analysis. [ss.148(7)-(7 A)/153(3)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

Salary and other supported adjustable deductions reconcile under s.168; refund entitlement/application is separately under s.170. Section 103 is foreign-tax credit, not a generic inter-company dividend exemption. Goods exports s.154 are minimum tax under the amended law; the old final-tax opt-out was omitted. Services exports s.154A have their own final-tax conditions/annual opt-out, owned by `pk-it-export-tax`; no automatic non-ATL doubling applies. Recipient-level final/minimum/normal disputes need specialist review. [ss.103/154/154 A/168/170](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

## Deadlines and filing

Section 165 is **quarterly**, not monthly: quarters ending March/June/September/December are due 20 April/20 July/20 October/20 January. Both 2025 and current 2026 texts support this cadence. Reconcile gross amounts, recipients, sections, deductions and actual CPRs. A separate annual reconciliation/certificate requirement must be supported by its current rule/form, not inferred from twelve nonexistent monthly statements. [s.165](https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf).

Deposit is separate from statement filing. Section 148 collection is at Customs under s.148(5). Use rules 43/44 below; the old other-agent fortnight table is wrong, while the government same-day branch is confirmed. Generate the correct payment instruction and retain actual bank receipt; do not promise automatic IRIS reflection within 24-48 hours or a particular upload/API capability.


### Deposit, salary statement and certificate rules now sourced

Income Tax Rules 43 requires federal/provincial government deposit on the day of collection/deduction; other persons deposit within 7 days from each week ending Sunday, with nonresident overseas remittances paid before remitting abroad. There is no separate other-agent fortnight rule. Rule 44(5) requires the s.149 deductor's **annual salary statement by 31 July** after financial-year end, Part IX Second Schedule, separately from quarterly s.165 reporting. Rule 44(4) requires reconciliation when the Commissioner requires it, not a universal annual reconciliation automatically replacing that salary statement. [Rules 43/44](https://download1.fbr.gov.pk/Docs/20269211394336470IncomeTaxRules2002.pdf).

Rule 42's non-salary collection/deduction certificate uses Part VII Second Schedule within 15 days after financial-year end or business discontinuation; an earlier in-year request is answered within 7 days. Duplicate/lost-certificate and serial-number rules apply. This non-salary rule is not an employer salary-certificate deadline. Verify actual salary certificate entitlement/form under the operative law rather than revive omitted rule 41. [r 42](https://download1.fbr.gov.pk/Docs/20269211394336470IncomeTaxRules2002.pdf).

## Penalties and interest

Failure to deduct/pay can expose the payer under s.161, with expense-disallowance questions under s.21(c), penalty/default surcharge under ss.182/205 and recipient-paid-tax relief requiring actual evidence. Do not use the old 0.1%-per-day default-surcharge claim, claim all voluntary late deposits escape penalty, or promise a refund of minimum/final tax. The default-date law, actual failure, statutory relief and calculation must be separately established; conflicting old s.165 penalty tables are not usable rates.

## Cross-border points

A royalty/FTS label needs actual s.152/s.6 and treaty analysis, including residence, beneficial owner, PE connection and anti-abuse provisions. Preserve review of UK, US, China, UAE, Saudi Arabia, Germany, Switzerland and Singapore dividend/interest/royalty/FTS articles and protocols. **The former illustrative treaty rate grid is not confirmed and must not be used.** In particular the earlier UK royalty 12.5% claim and £100,000 case cannot establish the actual treaty cap. A TRC alone does not prove every treaty condition. Refer PE attribution/elections and foreign contractor disputes.

## Worked cases

### Company A and Company B advisory cases retained and corrected

Original case: Karachi company A pays Karachi advisory firm B, an ATL private company. Assume the contract is an ordinary resident advisory service outside specified reduced categories, recipient B is an ATL private company, payer A prescribed, tax year 2026, and the **given gross invoice 1,180,000 already includes any separately assessed sales tax**. This is not an assertion that Karachi advisory services legally bear 18% sales tax.

```oa-check
name: CompanyA pays CompanyB ordinary advisory service
inputs:
  gross_including_sales_tax: 1180000
steps:
  - income_tax_withheld: gross_including_sales_tax * 0.15
  - net_to_B: gross_including_sales_tax - income_tax_withheld
expected:
  income_tax_withheld: 177000
  net_to_B: 1003000
```

```oa-check
name: Same advisory payment, recipient outside ATL and no exception
inputs:
  gross_including_sales_tax: 1180000
steps:
  - applicable_rate: 0.15 * 2
  - income_tax_withheld: gross_including_sales_tax * applicable_rate
  - net_to_B: gross_including_sales_tax - income_tax_withheld
expected:
  applicable_rate: 0.3
  income_tax_withheld: 354000
  net_to_B: 826000
```

The former 110,000/220,000 results combined an excluded-sales-tax base and superseded service rates. These are not filing instructions for a later-period payment.

### Earlier UK royalty case retained as a verification hold

The earlier Pakistan-company payment of £100,000 royalty to a UK-resident IP owner, with TRC and beneficial-ownership declaration on file, remains open. Statutory charge, treaty article/protocol, beneficial ownership, PE facts and conversion evidence must be established. The former£12,500 result relied on an unverified 12.5% treaty rate and is not a cleared computation. Do not replace it with another guessed treaty cap.

### Importer X finished-goods case retained with complete base

Assume Part III commercial classification is evidenced, ATL status supported, ordinary non-retail-price valuation applies and Customs has separately assessed the stated sales tax. The 2,160,000 sales-tax input is an assumed actual assessment, not a universal tax calculation for imports.

```oa-check
name: ImporterX PartIII commercial import
inputs:
  customs_value: 10000000
  customs_duty: 2000000
  assessed_sales_tax: 2160000
  fed: 0
steps:
  - section148_base: customs_value + customs_duty + assessed_sales_tax + fed
  - income_tax_collected: section148_base * 0.06
expected:
  section148_base: 14160000
  income_tax_collected: 849600
```

### Earlier individual-landlord rent case retained and corrected

The original company tenant pays an ATL individual landlord 2,400,000 annual rent; the example assumes twelve equal payments.

```oa-check
name: Annual rent2400000 to ATL individual landlord
inputs:
  annual_rent: 2400000
  equal_payments: 12
steps:
  - annual_withholding: 155000 + (annual_rent - 2000000) * 0.25
  - equal_payment_withholding: annual_withholding / equal_payments
expected:
  annual_withholding: 255000
  equal_payment_withholding: 21250
```

### Company X certificate case retained conditionally

Assume an actual valid 2% certificate lawfully applies during 1 July 2025-30 June 2026 to prescribed-person Company Y's 500,000 service payment to Company X in the stated period. Verify the statutory certificate route and all limits first; no general 2% entitlement is asserted.

```oa-check
name: Apply an evidenced certificate rate
inputs:
  covered_gross_payment: 500000
  actual_certificate_rate: 0.02
steps:
  - deduction: covered_gross_payment * actual_certificate_rate
  - net_payment: covered_gross_payment - deduction
expected:
  deduction: 10000
  net_payment: 490000
```

## When to refuse or refer

Retain all earlier refusal groups: provincial/ICT sales-tax withholding; WWF/WPPF; federal excise; customs/regulatory/additional duties beyond s.148; unseen or expired SROs/certificates; unsupported treaty claims; non-resident PE attribution/elections; final/minimum/normal classification disputes; petroleum, banking, insurance, power/IPP, REIT/fund specials; refunds/FTO/IRIS disputes; and combined federal/provincial determinations. Do not assume payer obligation, strip ambiguous sales tax, select a higher guessed contract rate, or apply an old-year rate as a safe default. Obtain missing facts/law and mark the calculation pending.


### Current late-entry ATL route, November 2026

Current s.182A surcharge amounts are company 100,000/AOP 50,000/individual 25,000; these are current-action amounts, not the historical 20,000/10,000/1,000 table. For a late individual, r 81 B(2 B)-(2D) now allows IRIS **Form ATL-U** undertaking instead of the surcharge: the 6-month period starts from successful IRIS acknowledgment, with an undertaking not to purchase, acquire or otherwise obtain ownership or a beneficial interest in any property during that period. An established breach after electronic hearing withdraws the benefit from the breach date and ordinary rules then govern. Do not promise this route to an AOP/company or describe filing alone as automatic fee-free entry. Dated event status and actual charge conditions still control withholding. [Current ITO s.182A](https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf); [signed 10 November 2026 SRO 2097](https://download1.fbr.gov.pk/SROs/202611101511326308SRO2097of2026.pdf), read 2026-11-14 for the operative rule/form.

## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for Finance Act 2026 amendment 47(a), Tenth Schedule rule 1A omission, distinguished from historical tax-year-2026 event rules | https://download1.fbr.gov.pk/Docs/20266291261044366FinanceAct2026.pdf | 2026-11-15 |
| Read for Income Tax Rules 42-44 operative payment, non-salary certificate, annual salary statement and requested reconciliation branches on 2026-11-14 | https://download1.fbr.gov.pk/Docs/20269211394336470IncomeTaxRules2002.pdf | 2026-11-14 |
| Read for ITO ss.71,148-149,152-155,158-159,165,168/170; First Schedule Parts II/III and Tenth Schedule rules 1/10, including adjacent exceptions and omitted historical footnotes | https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf | 2026-11-14 |
| Read for current 2026 s.165 quarterly statement schedule; use default-date law separately for penalties | https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf | 2026-11-14 |

Not yet confirmed: salary-certificate form and case-specific reconciliation notices; royalty/FTS statutory and treaty outcome for the held UK case; all former treaty-grid figures; special s.150 IPP/fund/REIT rates/recipient finality and bonus-share withholding, s.151 yield-threshold/finality and separate sukuk division, s.152PE/elections, s.156 prize/non-cash mechanics, s.156A petroleum, s.156B pension withdrawal, brokerage/commission, auctions, vehicles/token tax, electricity, telecom, distributor/retailer collection and property/late-filer rates. The old cash-withdrawal 231 A label, banking 236 P, stockbroker 233 A 0.02% and generic construction 100 D/Third Schedule references require current operative-law confirmation; they are not usable instructions. Preserve these subjects for specialist follow-up rather than transplanting old figures. No claim is made that all old individual/company treatments were correct.
