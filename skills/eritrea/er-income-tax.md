---
name: er-income-tax
description: "Personal income tax for employees, landlords and sole traders under Income Tax Proclamation 62/1994 as amended, plus the 2% tax on Eritreans abroad, with the bands, exemptions, deadlines and penalties. Provides a 2026 reference using identified historical Eritrean gazettes; later current-period amendments remain unconfirmed. Use for questions such as: how much income tax on a salary in Eritrea, Eritrea rent tax, sole trader tax in Asmara, the 2% diaspora tax."
jurisdiction: ER
category: international
tax_year: 2026
last_updated: 2026-11-16
version: 0.3
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Eritrea Personal Income Tax

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

2026 reference using the available source-year gazettes read on 15 November 2026; that completed research was recovered on 16 November 2026 without redating the old law reads. The latest income-tax amendment recovered here is Legal Notice 119/2012; the Ministry of Justice’s 2023 inventory is a list, not proof that no later law exists. No 2026 consolidated income-tax text or current return was recovered. Before using these source-year rules for a current liability, establish the taxpayer’s actual period and whether a later operative instrument changes them. If current applicability cannot be established, stop the current calculation or filing; retain these historical rules as reference only. Unresolved current implementation remains under Not yet confirmed.

## Who this applies to

Any person with income that has its origin in Eritrea, wherever paid (Proc 62/1994 arts 2(8), 4). Employment, rent, business and commercial farming income are computed separately (art 5); benefits in kind are valued by the Inland Revenue Office (art 6). “Person” includes non-incorporated associations/partnerships and excludes incorporated limited-liability bodies (art 2(5)). Sales tax is in [VAT or GST](er-vat-gst.md), companies in [Corporate income tax](er-corporate-income-tax.md).

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Employment band 1 | 2% | Monthly taxable income up to 200 Nakfa | Proc 116/2001 art 2, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-116-2001/eritrean-proc-116-2001.pdf |
| Employment band 2 | 10% | 201 to 1,200 | same |
| Employment band 3 | 20% | 1,201 to 2,500 | same |
| Employment band 4 | 25% | 2,501 to 3,500 | same |
| Employment band 5 | 30% | Over 3,500 | same |
| Annual band 1 | 2% | Up to 2,400 Nakfa | Proc 116/2001 art 3 (rent), art 4 (business), https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-116-2001/eritrean-proc-116-2001.pdf |
| Annual band 2 | 10% | 2,401 to 14,400 | same |
| Annual band 3 | 20% | 14,401 to 30,000 | same |
| Annual band 4 | 25% | 30,001 to 42,000 | same |
| Annual band 5 | 30% | Over 42,000 | same |
| Commercial farming, historical statutory schedule only | 2%, 5%, 10%, 15%, 20% | Original Schedule D thresholds: up to 1,000; to 10,000; to 20,000; to 35,000; above, printed in Birr. Current currency/application and interaction with the 2016 rural-farm reform are NOT confirmed; do not calculate current farm tax from these figures. | Proc 62/1994 arts 27-30, Schedule D, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf; 2016 official reform notice, https://shabait.com/2016/12/02/legal-notice-on-farm-and-livestock-income-tax/ |
| Lottery or tombola, bingo, royalty | 10% of gross | Lottery/tombola not exceeding 500 and bingo not exceeding 400 are exempt, including the exact limits; above, 10% on gross. The 1994 source prints Birr; current currency/application remains unconfirmed. Royalty is 10% of gross independently of those chance-winning limits | Proc 62/1994 art 22(4), Schedule C-3, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf |
| Tax on Eritreans abroad | 2% of net income | Eligible Eritrean citizen living abroad with employment, rent of movable/immovable property, business, professional or other service income. The original/translated art 2 describes monthly or annual payment; do not infer a universal due day or definition of net income. Actual local consular process must be established. | Proc 67/1995 art 2 original scan, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-67-1995/eritrean-proc-67-1995.pdf; Eritrean Embassy official RRT page, https://us.embassyeritrea.org/rrt/ |

## The base

1. Classify the income and period before calculating. Employment is monthly; a payment covering more than 1 month is prorated across its covered months (Proclamation 62/1994 art 8(1)). Rent and business use separate annual schedules. Apply each band marginally, retaining the source’s whole-unit bounds; fractional-income rounding is unconfirmed. Do not combine all schedules into one total-income band.
2. Establish the taxable base and every applicable exclusion below, then calculate each slice at its linked rate. For rent, distinguish an owner’s direct lease from a sublease before claiming the allowance.
3. Apply the filing-category and withholding rules to the result. A proposed actual filing, appeal, foreign service, diaspora or farm calculation with an unresolved condition requires the operative instrument and local process first.

Employment income includes salaries, wages, allowances, pension contributions, directors’ fees and personal emoluments, cash and benefits in kind, unless lawfully excluded (arts 6-9). Regulations 20/1995 arts 4-6 provide these exclusions and adjustments:

| Item | Complete condition | Source |
|---|---|---|
| Medical and injury amounts | Under the employment contract, actual medical-treatment cost and compensation for physical injury | Reg 4(1)(a), https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-20-1995/eritrean-notice-20-1995.pdf |
| Transport allowance | In lieu of provided transport, under governmental regulations or the employment contract; Inland Revenue must deem it reasonable | Reg 4(1)(b),4(2), https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-20-1995/eritrean-notice-20-1995.pdf |
| Duty travel | Contractual on-duty travel/transport expenses; reasonable to Inland Revenue | Reg 4(1)(c),4(2), https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-20-1995/eritrean-notice-20-1995.pdf |
| Joining, completion and leave travel | Employee recruited elsewhere; specific contract provision, expense actually incurred, and reasonable to Inland Revenue | Reg 4(1)(d),4(2), https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-20-1995/eritrean-notice-20-1995.pdf |
| Cash/store allowance and entertainment | Cashier/storekeeper allowance; entertainment directly attributable to actual business; both subject to the Department’s reasonableness/reduction/rejection power | Reg 4(1)(e)-(f),4(2), https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-20-1995/eritrean-notice-20-1995.pdf |
| Refunded pension contribution | Employee retires for various reasons before pension age and receives back contributions paid while working | Reg 5, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-20-1995/eritrean-notice-20-1995.pdf |
| Employer pays employee’s tax | Employer-paid tax from its own expense is added to taxable employment income; solve the resulting gross-up, do not simply deduct the stated amount | Reg 6, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-20-1995/eritrean-notice-20-1995.pdf |

Rent: include cash, benefits in kind, furniture/equipment rent, lessee-funded improvements in addition to rent and payments made by the lessee for the lessor (Act 18; Regulations 11). For a direct owner-to-lessee lease, deduct non-income taxes on the rented house and 1/4 of gross rent of buildings/furniture/equipment for repairs, maintenance and depreciation; no other rent expenses are allowed under Regulations 12-13(1). For a sublease, deduct the rent payable by the sublessor to the head lessor under Regulations 13(2), rather than automatically applying the owner’s 1/4 allowance. Advance rent covering over 1 year is attributed to the fiscal year of payment, with that year’s tax computed by prorating taxable income across the covered years (Regulations 14); the exact final tax multiplier/rounding for that branch is held.

Business: deduct expenses wholly, necessarily and exclusively paid or incurred for the activity (Act 24), subject to Regulations 19-20 and proof. Interest is deductible only on loans from government-approved credit institutions (Act 25). The complete business-expense reconciliation, depreciation and special deductions require their own source check; do not treat any accounting cost as automatically deductible. Net business losses carry forward for 5 years, earliest first (Act 25 A inserted by Proclamation 116/2001 art 5). Legal Notice 50/2001 art 2 repeals the conflicting old Regulations 20(2). The over-25% direct/indirect share-capital or voting-right ownership-change restriction applies where the taxpayer is a company; it is not a general natural-person share-sale rule.

| Exemption | Full scope or boundary | Source |
|---|---|---|
| Rural self-employed crafts | Weavers, potters, blacksmiths, tanners and the like outside municipal/township areas who employ no other full-time workers. The text does not bar every part-time helper. | Act 31(1), https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf |
| Unskilled day workers | Not regularly employed by a single employer; working over 15 aggregate days in a month for the same employer counts as regular employment. Exactly 15 is not “over 15”. | Act 31(2), Reg 7, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-20-1995/eritrean-notice-20-1995.pdf |
| Foreign-representative pay from abroad | Represents foreign business/other persons, is not employed or retained by an employer in Eritrea, and satisfies the statutory less-than-183 aggregate days in 1 year. Reg 8 imposes whole-stay tax above 183 aggregate days in any 12 months. Exactly 183 days and the different period tests are unresolved: HOLD rather than invent an inclusive safe harbour. | Act 31(3), Reg 8, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-20-1995/eritrean-notice-20-1995.pdf |
| Bank interest and dividends | Interest received by “persons” on bank accounts; dividends received by shareholders from Eritrean incorporated/corporated bodies. Do not extend this to every kind of interest or foreign dividend. | Act 2(5),31(4)-(5), https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf |
| Diplomatic/consular pay | Reciprocity; official-duty services by diplomatic/consular representatives, or other foreign mission employees who are that state’s nationals and diplomatic-passport holders, or normally exempt by international usage/custom. | Act 31(6), https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf |
| Other statutory/treaty relief | Specific law in force, international treaty, or agreement made/approved by the Minister must actually establish the exemption. | Act 31(7), https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf |

## Deadlines and filing

Employer: declare, withhold and pay within one month from the end of the month (arts 13, 14). An employer who fails is personally liable. A person with two employers in a month, or a non-exempt embassy employee, declares and pays personally within one month of the next month (arts 11, 12).

Rent: within one month from the end of the fiscal year (art 19).

Business (art 26): 4 months after year end if balance sheet and profit and loss are required, 2 months if only a daily income and expense summary, 1 month if no books are required. Regulations category test (Legal Notice 119/2012): A is any body, or a person with gross income over 1,000,000 Nakfa. B is a person over 200,000 up to 1,000,000, a professional over 30,000, or an importer, exporter, wholesaler or distributor up to 1,000,000. C is a person up to 200,000, or a professional up to 30,000. Apply the specific professional/import/export/wholesale/distribution limb as well as the general turnover test; a conflicting or mixed category needs Department resolution. Category A keeps a daily general journal, acceptable pre-numbered sales/purchase invoices, stock cards, manufacturer production-cost report where applicable, general/administrative expense and depreciation records. B keeps a daily income/expense book and the prescribed invoices, stock, production and administrative documents; a balance sheet is also required if depreciation is claimed (Legal Notice 20/1995 art 16). Receipts must be issued without being asked (Legal Notice 81/2003).

The statutory declaration uses special forms supplied by the Inland Revenue Offices and is made at the competent office (arts 40-41). Establish the current form, submission and payment route before filing; the historical statutory office rule is not proof of a current walk-in or online workflow. An assessment can be appealed to the Tax Appeal Commission within 30 days with a cash deposit (art 55). A company or person carrying on business/professional/vocational/other trade activity deposits at least the lesser of 75% of the assessment and 75% of the last preceding finally/conclusively assessed year’s tax; a first assessment instead requires 30%; other cases require 50% (art 55). Further appeal to the High Court, once and on an error of law, is within 30 days of the Commission’s decision (arts 58-59); Commission-assessed tax remains payable pending it, with subsequent refund/balance adjustment (art 60).

## Penalties and interest

| Failure | Penalty | Source |
|---|---|---|
| Business declaration/payment failure within art 26 periods | Department may assess 20% of tax finally assessed; do not automatically apply this provision to every employment/rent failure | Proc 62/1994 art 63, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf |
| Late payment | 5% of the amount in default for every month in default, maximum 50% of amount due; partial-month convention unconfirmed | Proc 62/1994 art 64, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf |
| Required books missing or unacceptable | 20% of tax finally assessed | Proc 62/1994 art 65, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf |

The arts 63-65 penalties are added to and recovered as tax; the Department may waive them wholly or partly (art 66). The separate receipt-penalty amendment could not be opened; its historical figures are held in Sources, not applied here.

## Cross-border points

The ordinary Act taxes Eritrean-origin income wherever paid (art 2(8)); this does not remove the separate diaspora tax. Services rendered from abroad to a person/body in Eritrea fall under art 22(4) Schedule C-3’s 10% gross charge, with payer withholding, declaration and remittance within 1 month from fee payment (art 26(2)(b)); establish service/source classification and any actual treaty first. Proc 67/1995 art 3 assigns diaspora collection to Foreign Affairs through embassies/consulates/other delegates and treasury deposit. The official US Embassy page confirms eligible citizens abroad contribute 2% of net income, asks for status-specific evidence and gives a consular workflow; the full-time-student FAQ says payment may not be required without earned income but evidence and annual clearance remain. Do not turn that qualified US practice into a worldwide statutory exemption or due date.

## Two worked examples that recompute

**Case 1: salary of 5,000 Nakfa a month.** 4 + 100 + 260 + 250 + 450 = 1,064 Nakfa.

```oa-check
name: Monthly pay 5000 Nakfa
inputs:
  pay: 5000
steps:
  - band_1: min(pay, 200) * 0.02
  - band_2: (min(pay, 1200) - min(pay, 200)) * 0.10
  - band_3: (min(pay, 2500) - min(pay, 1200)) * 0.20
  - band_4: (min(pay, 3500) - min(pay, 2500)) * 0.25
  - band_5: (pay - min(pay, 3500)) * 0.30
  - tax: band_1 + band_2 + band_3 + band_4 + band_5
expected:
  tax: 1064.00
```

**Case 2: one-year furnished owner’s rent of 60,000 Nakfa.** Assume a direct owner-to-lessee lease, no additional lessee payments/improvements and no separately deductible property taxes. The 25% statutory allowance is 15,000 (derived), leaving 45,000 taxable income. The block independently derives the base and marginal tax.

```oa-check
name: Rent income 45000 after allowance
inputs:
  income: 45000
  gross_rent: 60000
steps:
  - allowance: gross_rent * 0.25
  - taxable_base: gross_rent - allowance
  - base_difference: taxable_base - income
  - band_1: min(taxable_base, 2400) * 0.02
  - band_2: (min(taxable_base, 14400) - min(taxable_base, 2400)) * 0.10
  - band_3: (min(taxable_base, 30000) - min(taxable_base, 14400)) * 0.20
  - band_4: (min(taxable_base, 42000) - min(taxable_base, 30000)) * 0.25
  - band_5: (taxable_base - min(taxable_base, 42000)) * 0.30
  - tax: band_1 + band_2 + band_3 + band_4 + band_5
expected:
  tax: 8268.00
  base_difference: 0
  taxable_base: 45000
  allowance: 15000
```

Tax is 8,268 Nakfa on the assumed one-year facts. For the advance-rent alternative: if 60,000 covers 2 years, a 45,000 base divided by 2 is 22,500 (derived). Reg 14 attributes the payment to the receipt year; it does not support telling the landlord to declare half in each year. Exact resulting payment-year tax/multiplier and approval of an alternative accounting year remain held, so no timing recommendation follows from this comparison.

## Ask the client first

- Citizen, and living in Eritrea or abroad?
- Income type: employment, rent, business, farming?
- One employer or several in the month?
- Annual gross income and occupation (sets the category)?
- Direct lease or sublease; lessee-funded improvements, lessor payments and actual covered rental years?
- Foreign representative’s local employment/retainer and aggregate dates under both statutory period tests?
- Fiscal year used, if approved as different?

## Sources

| Source and actual reading scope | Official URL | Read on |
|---|---|---|
| act: Read for English text arts 1-71, physical pages 21-42; arts 2,5-9,11-31,40-41,55-66 operative clauses and neighbors. Rate schedules superseded by Proclamation 116/2001 are not reused. Schedule C-3 and definition page visually checked. | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf | 2026-11-15 |
| rates: Read for English arts 1-7, physical 7-11; all employment/rent/business rate tables visually checked at 7-9, loss carry-forward and commencement read. | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-116-2001/eritrean-proc-116-2001.pdf | 2026-11-15 |
| reg: Read for English arts 1-27, physical 14-23; benefit exclusions/gross-up, casual/foreign workers, rent/sublease/advance payment, books and deductions/appeal rules read. Old categories and old loss 20(2) are superseded. | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-20-1995/eritrean-notice-20-1995.pdf | 2026-11-15 |
| loss: Read for Entire English instrument arts 1-3, physical 3/printed 50 visually read: repeals Regulations 20(2), effective 1 Jan 2002. | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-50-2001/eritrean-notice-50-2001.pdf | 2026-11-15 |
| receipt: Read for English Notice 81/2003 arts 1-3 and schedule, physical 8-12; receipt obligation and permitted receipt details read. Cover names Proclamation 138/2003 but this PDF does not contain its operative text. | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-81-2003/eritrean-notice-81-2003.pdf | 2026-11-15 |
| categories: Read for Entire English instrument arts 1-3, physical 3; all A/B/C category limbs and commencement read. | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-119-2012/eritrean-notice-119-2012.pdf | 2026-11-15 |
| diaspora: Read for Original Tigrinya operative page 2 visually inspected for instrument identity, embedded employment/net income/2% and arts 2-4; compared with the UK Government English Annex II, printed 11-12. No claim of an authoritative English original. | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-67-1995/eritrean-proc-67-1995.pdf | 2026-11-15 |
| embassy: Read for Whole operative General Information, status-specific evidence requirements, full-time-student FAQ and steps, web lines 59-112. US consular practice is not a universal statutory payment calendar. | https://us.embassyeritrea.org/rrt/ | 2026-11-16 |
| list: Read for Intro and entire section 16 Taxes (Except Customs), printed 10-11; Customs 112/2000 identity in section 15. Inventory is not proof that no later law exists. | https://mojeritrea.net/wp-content/uploads/2023/05/Thematic-Categorization-of-Domestic-Legislations-of-the-State-of-Eritrea.pdf | 2026-11-15 |
| farm: Read for Whole operative government notice, paragraphs 13-19; reported 1 Dec 2016 commencement and replacement, not actual statutory rate tables. | https://shabait.com/2016/12/02/legal-notice-on-farm-and-livestock-income-tax/ | 2026-11-15 |

The 15 November read dates above belong to the recovered completed writer research, not new whole-document reads on 16 November. The Embassy page alone was opened again on 16 November for the stated consular scope. Scanned English tables were checked against the visible pages. Proclamation 67/1995 was checked with the UK Government Annex II English translation as a reading aid; it is not represented as an English original or a complete current consular procedure. The older source text uses Birr and the 2001 employment/rent/business replacement uses Nakfa; no unverified conversion is assumed.

Not yet confirmed: A current 2026 consolidated text, later amendments, fiscal-year start/end, approved alternative years, current return/portal/office/payment process, fractional-income rounding, annual employment reconciliation and any day-count residence rule. Exactly 183 days and the Act’s 1 year versus Regulations 12 month exemption tests; complete actual expense/depreciation reconciliation; advance-rent final multiplier/rounding; current farm and chance-winning currency/application; actual diaspora net-income definition, current host-country collection method, relief/treaty and payment dates. Historical receipt penalty 125% of amount/minimum 500 Nakfa/licence-suspension threshold 8000 attributed to Proclamation 138/2003 art 2 could not be read: direct URL https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-138-2003/eritrean-proc-138-2003.pdf timed out, web access 403; Notice 81’s cover is insufficient, so these figures are not usable instructions. Original unsupported 800 Nakfa tax-free band, 5%/10%/15%/20% band sequence and citation “Proclamation 24/2011” remain rejected; no source found. Whether domestic 2% rehabilitation tax survives Proclamation 66/1994 partial repeal of 17/1991 was not established. The UK translation’s broad wording is not a determination of worldwide-base details.
