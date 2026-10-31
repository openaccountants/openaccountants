---
name: kenya-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Kenya VAT return (VAT-3), classify transactions for Kenyan VAT purposes, or advise on VAT registration and filing in Kenya. Trigger on phrases like "Kenya VAT", "KRA VAT", "VAT-3 Kenya", "input tax Kenya", "output tax Kenya", "Kenya Revenue Authority VAT", or any Kenya VAT request. Also covers the former ke-vat-return slug. ALWAYS read this skill before touching any Kenya VAT work.
version: 3.0
jurisdiction: KE
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - vat-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---


# Kenya VAT v3.0

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

This skill also replaces the former `ke-vat-return` slug. The law is the VAT Act (Cap. 476, formerly No. 35 of 2013) as at 1 July 2025, amended by the Finance Act 2026 (No. 19 of 2026), most of which took effect on 1 July 2026. A 2026 period straddles that date: use the old rule before it and the new rule after it.

## Who this applies to

- A person who made, or expects to make, taxable supplies of KES 5,000,000 or more in any 12 months must apply to register within 30 days of becoming liable (s. 34(1)). Capital asset sales and sales made solely because the business is ending stay out of the test (s. 34(2)). Below the limit, registration is voluntary, on conditions (KRA).
- A person supplying imported digital services over the internet, an electronic network or a digital marketplace registers whatever its turnover (s. 34(1) proviso; s. 5(7)).
- Skill use: month-by-month preparation of the return from a bank statement, ETR receipts and invoices, with a KRA PIN. Minimum input: the month's bank statement and PIN. Recommended: purchase invoices, sales invoices, prior excess credit. Ideal: iTax registers, import entries, asset register. No bank statement is a hard stop. All credits stay provisional until the documents are seen.
- Refuse and refer: R-KE-1 non-registered vendor (only a registered person charges VAT, confirm registration); R-KE-2 partial exemption without full-year data; R-KE-3 large withholding VAT reconciliations; R-KE-4 non-resident digital suppliers; property and land transactions.

## Rates, bands and thresholds

| Item | Amount | Conditions | Tax year | Official URL |
| --- | --- | --- | --- | --- |
| Standard rate | 16% | Every taxable supply, import and imported taxable service not zero-rated (s. 5(2)(b)) | 2026 | https://new.kenyalaw.org/akn/ke/act/2013/35/eng@2025-07-01 |
| Zero rate | 0% | Second Schedule Part A, in the course of a registered person's business, not hotel, restaurant or entertainment services | 2026 | https://new.kenyalaw.org/akn/ke/act/2013/35/eng@2025-07-01 |
| Registration threshold | KES 5,000,000 | Any 12 months, s. 34(1) | 2026 | https://new.kenyalaw.org/akn/ke/act/2013/35/eng@2025-07-01 |
| Withholding VAT | 2% of taxable value | Appointed agents, TPA s. 42A(1). Not on zero-rated supplies, on registered manufacturers with investment of at least KES 2 billion at 31 December 2024, or on official aid-funded projects (s. 42A(1) proviso, (3)). Replaces the 6% in the earlier skill | 2026 | https://new.kenyalaw.org/akn/ke/act/2015/29/eng@2025-07-01 |
| Refund claim, excess from zero-rating or withholding | 12 months | From the date the tax is due and payable, s. 17(5) | 2026 | https://new.kenyalaw.org/akn/ke/act/2013/35/eng@2025-07-01 |
| Input tax claim window | 6 months | After the end of the period of the supply or import, s. 17(2) | 2026 | https://new.kenyalaw.org/akn/ke/act/2013/35/eng@2025-07-01 |
| Bad debt relief wait | 3 years | Was 2 years, s. 31(1), Finance Act 2026 s. 29 | 2026 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |

Zero-rated (Second Schedule Part A, paragraph): exported goods (1), exported taxable services (23), supplies to EPZ businesses (2) and SEZ enterprises (12), ship stores (3), international air passengers (5), services to international carriers (6), goods in transit services (10), ordinary bread (13A), listed milk and cream (15), Kenyan-origin goods carried abroad (20), LPG (27). Finance Act 2026 s. 33 deleted paragraphs 11 and 35 and narrowed paragraphs 31 and 32 by tariff heading.

Exempt (First Schedule): financial services, insurance (excluding consultancy, actuaries, assessors), education, medical, veterinary, dental, ambulance and nursing services, agricultural services, burial, passenger transport except international air and hired or chartered conveyances, land and residential letting, postal stamps (Part II paras 1 to 8, 29). Goods include listed medicaments and fertilizers of Chapter 31 (Part I para 151). The earlier skill called medicines, fertilizers and ambulances zero-rated: the Act makes them exempt, so no refund of input tax. Added from 1 July 2026: dialyzers, scrap metal, pharmaceutical inputs on recommendation, BEV stoves, credit and sale of repossessed collateral (Part I paras 158 to 161, 166). Electricity and water do not appear in the schedules, so they stand at 16%.

## The base

- Output tax: 16% of taxable value; on a VAT-inclusive receipt, tax is gross x 16/116.
- Labour and outsourcing: from 1 July 2026 salaries, wages and statutory deductions are disbursements for the client, outside the value (s. 13(5A), (5B)).
- Hire purchase: finance charges leave the value only if the supplier is licensed and the agreement is registered under the Hire Purchase Act (s. 13(6)(a)).
- Payment services: money transfer stays exempt, but processing, settlement, merchant acquiring, gateway and aggregation fees by a payment service provider are not (First Schedule Part II para 1(b), Finance Act 2026 s. 32(b)).
- Input tax: deductible only to the extent the purchase makes taxable supplies (s. 17(1)), with an original invoice or certified copy, or customs entry and receipt (s. 17(3)), unless the supplier has declared the invoice.
- Blocked: passenger cars and minibuses with their repairs, unless dealt in or hired as the business; entertainment, restaurant and accommodation, unless that is the business or the recipient is away from home on business (s. 17(4)).
- Excess input tax carries forward (s. 17(5)). From 1 July 2026 input tax on supplies to the KDF, its welfare services, NIS and Police is deductible with documents and not apportioned (s. 17(5)(e), (7), (8)).
- Newly exempt supplies: on the date supplies become exempt, pay back input tax on unsold stock in that period's return (s. 17A).
- Invoices: one showing tax only for a taxable supply (s. 42(2)).
- Withholding VAT: a client appointed as agent pays over 2% of taxable value. Record full output tax, take the 2% as a credit on its certificate. Excess from withholding is refundable or set off (s. 17(5)).
- Imported services: tax falls on the recipient (s. 5(6)), but "supply of imported services" covers a registered recipient only where it would not have full input tax (s. 2). A fully taxable registered business has no entry. An exempt or partly exempt one, or a non-registered recipient, is liable on the disallowed position; refer R-KE-2.

### Supplier pattern library (bank statement classification)

#### 3.1 Kenyan banks: fees (exempt / exclude)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KENYA COMMERCIAL BANK, KCB | EXCLUDE (fees) | Bank charges for lending and money dealing are exempt (First Schedule Part II para 1); check any fee invoice showing VAT |
| EQUITY BANK, EQUITY GROUP | EXCLUDE (fees) | Same |
| COOPERATIVE BANK, CO-OP BANK | EXCLUDE (fees) | Same |
| ABSA BANK KENYA | EXCLUDE (fees) | Same |
| STANDARD CHARTERED KENYA | EXCLUDE (fees) | Same |
| NCBA BANK, NCBA GROUP | EXCLUDE (fees) | Same |
| I&M BANK | EXCLUDE (fees) | Same |
| DIAMOND TRUST BANK, DTB | EXCLUDE (fees) | Same |
| MPESA, M-PESA (SAFARICOM) | EXCLUDE (person-to-person transfer fees); Input 16% (Lipa na M-Pesa or other merchant, gateway, processing fees from 1 July 2026) | Finance Act 2026 s. 32(b) |
| AIRTEL MONEY | Same as M-Pesa | Same |
| BANK CHARGES, INTEREST | EXCLUDE | Bank fee or interest, exempt |

#### 3.2 Kenyan government and statutory (exclude)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KENYA REVENUE AUTHORITY, KRA | EXCLUDE | Tax payment |
| NATIONAL SOCIAL SECURITY FUND, NSSF | EXCLUDE | Social insurance |
| NATIONAL HOSPITAL INSURANCE FUND, NHIF | EXCLUDE | Health insurance contribution |
| NITA, NATIONAL INDUSTRIAL TRAINING | EXCLUDE | Statutory levy |
| NTSA, NATIONAL TRANSPORT AND SAFETY | EXCLUDE | Regulatory fee |

#### 3.3 Kenyan utilities (taxable at 16%)

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| KENYA POWER, KPLC | Input 16% | 16% | Electricity: taxable |
| NAIROBI CITY WATER, NCWSC | Input 16% | 16% | Water: taxable |
| SAFARICOM (data/voice) | Input 16% | 16% | Telecom: taxable |
| AIRTEL KENYA | Input 16% | 16% | Mobile: taxable |
| TELKOM KENYA, TELKOM | Input 16% | 16% | Telecom: taxable |
| ZUKU FIBER, WANANCHI GROUP | Input 16% | 16% | Internet: taxable |
| LIQUID TELECOM KENYA | Input 16% | 16% | Internet: taxable |

#### 3.4 Transport and logistics

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| KENYA AIRWAYS, KQ | Check route | 0%/exempt | International 0% (Second Schedule para 5); domestic exempt (First Schedule Part II para 7), no input tax |
| JAMBOJET | Exempt | None | Domestic passenger carriage, First Schedule Part II para 7 |
| AFRICAAIRWAYS | Check route | 0%/exempt | Same as Kenya Airways |
| UBER KENYA | Check invoice | Exempt/16% | Passenger carriage exempt unless the conveyance is hired or chartered (para 7); the platform commission is a separate supply |
| BOLT KENYA | Check invoice | Exempt/16% | Same |
| LITTLE CAB | Check invoice | Exempt/16% | Same |
| DHL KENYA | Input 16% | 16% | Courier: taxable |
| FEDEX KENYA | Input 16% | 16% | Courier: taxable |
| G4S KENYA, WELLS FARGO (courier) | Input 16% | 16% | Security/courier: taxable |
| POSTA KENYA (parcel) | Input 16% | 16% | Parcel: taxable |
| POSTA KENYA (stamps) | EXEMPT | None | First Schedule Part II para 29 |

#### 3.5 Food and retail

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| NAKUMATT, NAIVAS SUPERMARKET | Input 16%/0% | Mixed | Non-food 16%; ordinary bread and listed milk are zero-rated (Second Schedule paras 13A, 15). Read the itemised receipt |
| QUICKMART SUPERMARKET | Input 16%/0% | Mixed | Same |
| CARREFOUR KENYA | Input 16%/0% | Mixed | Same |
| CHANDARANA FOODPLUS | Input 16%/0% | Mixed | Supermarket: split |
| TUSKYS SUPERMARKET | Input 16%/0% | Mixed | Same |
| KWAL, DEL MONTE KENYA (packaged food) | Input 16% | 16% | Processed food: 16% |
| UNGA LIMITED (maize flour) | Check invoice | Per invoice | Rate not confirmed, see Sources |

#### 3.6 SaaS: international suppliers

A non-resident supplying imported digital services must register whatever its turnover (VAT Act s. 34(1) proviso). If the invoice shows a KRA PIN and VAT, treat it as a Kenyan taxable purchase. If not, see "Imported services" under The base.

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE (Workspace, Ads) | Imported services rule | Registered and fully taxable recipient: no entry |
| MICROSOFT (365, Azure) | Imported services rule | Same |
| META, FACEBOOK ADS | Imported services rule | Same |
| ZOOM, SLACK, NOTION | Imported services rule | Same |
| AWS | Imported services rule | Same |

#### 3.7 Payment processors (16% from 1 July 2026)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MPESA TRANSACTION FEE | EXCLUDE | Bank charges for lending and money dealing are exempt (First Schedule Part II para 1); check any fee invoice showing VAT |
| PESAPAL (fees) | Input 16% | Finance Act 2026 s. 32(b): gateway and aggregation fees are outside the exemption |
| STRIPE (fees) | Input 16% or imported services rule | Non-resident supplier: see 3.6 |
| PAYPAL (fees) | Input 16% or imported services rule | Same |

#### 3.8 Internal transfers and exclusions

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Internal movement |
| LOAN, REPAYMENT | EXCLUDE | Loan principal |
| SALARY, PAYROLL | EXCLUDE | Outside VAT scope |
| DIVIDEND | EXCLUDE | Out of scope |
| ATM, CASH WITHDRAWAL | Tier 2: ask | Default exclude |


### Bank statement reading guide

#### Common Kenyan bank formats

| Bank | Key columns | Date format | Amount |
| --- | --- | --- | --- |
| KCB | Date, Description, Debit, Credit, Balance | DD/MM/YYYY | KES |
| Equity Bank | Date, Narrative, Withdrawal, Deposit, Balance | DD/MM/YYYY | KES |
| Co-op Bank | Date, Description, Debit, Credit, Balance | DD/MM/YYYY | KES |
| ABSA Kenya | Date, Description, Amount, Balance | DD/MM/YYYY | KES |

#### Key Kenyan banking terms

| Term | Meaning | Hint |
| --- | --- | --- |
| Credit / Deposit | Incoming | Potential revenue |
| Debit / Withdrawal | Outgoing | Potential expense |
| M-PESA | Mobile money | Check if fee or transfer |
| Bank Charges | Fee | Exempt |
| Interest | Interest | Exempt |
| Balance | Balance | Ignore |


## Deadlines and filing

Monthly. Log in to iTax (https://itax.kra.go.ke) with the PIN, complete the VAT return for the period, submit, generate the payment slip and pay.

| Obligation | Due | Source |
| --- | --- | --- |
| Return | 20th day after the end of the period, s. 44 | https://new.kenyalaw.org/akn/ke/act/2013/35/eng@2025-07-01 |
| Payment | 20th of the following month | https://www.kra.go.ke/individual/filing-paying/types-of-taxes/value-added-tax |
| Registration | 30 days after liability, s. 34(1) | https://new.kenyalaw.org/akn/ke/act/2013/35/eng@2025-07-01 |

Working paper (our labels, not iTax box numbers):

```
KENYA VAT-3 WORKING PAPER
Period: ____________  PIN: ____________

A. OUTPUT TAX
  A1. Standard-rated sales 16% (net)           ___________
  A2. Output tax (A1 × 16%)                    ___________
  A3. Zero-rated exports                       ___________
  A4. Exempt sales                             ___________
  A5. Imported services tax, recipient liable    ___________

B. INPUT TAX
  B1. Standard-rated purchases 16% (net)       ___________
  B2. Input tax (B1 × 16%)                     ___________
  B3. Import input tax                         ___________
  B4. Imported services input, if deductible   ___________
  B5. Total input (B2+B3+B4)                  ___________
  B6. WHT-VAT credits                          ___________

C. NET VAT
  C1. Net (A2 − B5)                            ___________
  C2. WHT-VAT credits (B6)                     ___________
  C3. Prior credit                             ___________
  C4. Net payable (C1−C2−C3)                   ___________

REVIEWER FLAGS:
  [ ] ETR/e-invoices confirmed?
  [ ] Export evidence held?
  [ ] WHT-VAT certificates collected?
  [ ] Imported services reviewed?
```

## Penalties and interest

| Item | Amount | Official URL |
| --- | --- | --- |
| Late or missing VAT return | Higher of 5% of tax payable or KES 10,000, TPA s. 83(1)(c) | https://new.kenyalaw.org/akn/ke/act/2015/29/eng@2025-07-01 |
| Late payment penalty | 5% of tax due, TPA s. 83A | https://new.kenyalaw.org/akn/ke/act/2015/29/eng@2025-07-01 |
| Late payment interest | 1% a month or part, TPA s. 38 | https://new.kenyalaw.org/akn/ke/act/2015/29/eng@2025-07-01 |
| Deliberate tax shortfall | 75% of the shortfall, TPA s. 84(2)(a) | https://new.kenyalaw.org/akn/ke/act/2015/29/eng@2025-07-01 |
| Non-filing from the VAT Special Table | No penalty, per KRA | https://www.kra.go.ke/individual/filing-paying/types-of-taxes/value-added-tax |

## Cross-border points

- Exported services are zero-rated (para 23). Hold the contract and payment evidence; without it use 16%. Exported goods need customs documents.
- Imports: VAT applies on taxable goods (s. 5(1)(b)); deduct with the customs entry and receipt.
- Non-resident digital suppliers: see Who this applies to.
- Returning residents: the para 99 limit rose to USD 2,000 from USD 300 (Finance Act 2026 s. 32(a)(vi)).

## Two worked examples that recompute

Example 1, ordinary month. IT consultant in Nairobi. Safaricom pays KES 1,160,000 gross for consulting; a foreign client pays KES 645,000 for an exported service (0%). Kenya Power KES 11,600 and DHL KES 5,800 gross, both 16%. Google Workspace without VAT on the invoice: fully taxable, so no entry. M-Pesa person-to-person fee KES 232: exempt. If Safaricom were a withholding agent, it would withhold 2% of KES 1,000,000.

```oa-check
name: Kenya monthly VAT with withholding credit
inputs:
  sales_gross: 1160000
  power_gross: 11600
  courier_gross: 5800
steps:
  - output: sales_gross * 16 / 116
  - input: (power_gross + courier_gross) * 16 / 116
  - withheld: (sales_gross - output) * 0.02
  - payable: output - input - withheld
expected:
  output: 160000
  input: 2400
  withheld: 20000
  payable: 137600
```

Example 2, decision: file now unpaid, or file and pay late? March VAT of KES 150,000 is three months late. Not filing and not paying costs the filing penalty (higher of 5% and KES 10,000), the payment penalty and 3% interest. Filing on time and paying late saves KES 10,000.

```oa-check
name: Late VAT return and payment, three months
inputs:
  tax: 150000
  months: 3
steps:
  - filing: max(tax * 0.05, 10000)
  - payment: tax * 0.05
  - interest: tax * 0.01 * months
  - total_late_both: filing + payment + interest
  - total_filed_on_time: payment + interest
  - saving: total_late_both - total_filed_on_time
expected:
  filing: 10000
  total_late_both: 22000
  total_filed_on_time: 12000
  saving: 10000
```

## Ask the client first

1. KRA PIN and VAT registration?
2. Month covered by the statement?
3. Exports: contract and payment evidence?
4. Government or other clients who withhold VAT? Certificates?
5. Foreign subscriptions: does the invoice show a KRA PIN? Any exempt sales?
6. Prior excess credit?
7. Itemised receipts for mixed groceries? ATM withdrawals: what for?

Defaults when unanswered: unknown sale rate 16%; unknown counterparty domestic; unproven export 16%; unknown business use 0% input; no invoice no input; exempt or taxable unclear, 16%. Review flags: single item above KES 500,000; tax effect above KES 80,000; counterparty above 40%; more than 4 defaults in a return; net position above KES 200,000.

Never claim input tax without the document, never zero-rate without evidence, never ignore withholding certificates, and never present the result as final: a CPA(K) or tax practitioner reviews it.

## Sources

| Source | URL | Read |
| --- | --- | --- |
| VAT Act, Cap. 476, legislation as at 1 July 2026 (Legal Notice 128 of 2026), KRA copy | https://www.kra.go.ke/images/publications/Value-Added-Tax-Act-2026.pdf | 2026-10-31 (ss. 2, 10, 17, 31, 34, 44 and the Schedule paragraphs cited, by passage in extracted text, not cover to cover) |
| VAT Act, Cap. 476, version of 1 July 2025 (cited in the tables above) | https://new.kenyalaw.org/akn/ke/act/2013/35/eng@2025-07-01 | 2026-10-31 by keyword passages; on review the page would not render, so check against the KRA copy |
| Finance Act 2026, No. 19 of 2026, ss. 25 to 33, 48 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf | 2026-10-31 |
| Tax Procedures Act, Cap. 469B, legislation as at 1 September 2026, KRA copy | https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf | 2026-10-31 (ss. 38, 42A, 83, 83A, 84, by passage in extracted text, not cover to cover) |
| Tax Procedures Act, Cap. 469B, version of 1 July 2025 (cited in the tables above) | https://new.kenyalaw.org/akn/ke/act/2015/29/eng@2025-07-01 | 2026-10-31 by keyword passages; check against the KRA copy |
| KRA VAT page | https://www.kra.go.ke/individual/filing-paying/types-of-taxes/value-added-tax | 2026-10-31 |
| KRA, Finance Act 2026 summary | https://www.kra.go.ke/popular-links/finance-act-2026-what-it-means-for-you | 2026-10-31 |

Not yet confirmed: the earlier skill's 100% withholding on foreign entities; s. 17(6) apportionment wording; iTax return box numbers (the earlier skill's Sections A to I are dropped from the body until read); ETR and eTIMS rules (earlier skill cited s. 27, not read), and whether a non-eTIMS invoice bars input tax; the rate on maize flour and textbooks (earlier skill: 0%, not found in the Second Schedule passages read); ride-hailing treatment under para 7; any 2026 petroleum rate change; effective dates that differ from 1 July 2026 for individual VAT items; supplier statuses in the pattern tables, which are unaudited; the Finance Act 2026 s. 86 TPA replacement on electronic tax systems.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network: accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
