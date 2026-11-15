---
name: pk-income-tax
description: Use for pakistan personal income tax and aop working paper. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return.
version: 1.1
jurisdiction: PK
tax_year: 2026
last_updated: 2026-11-14
source_checked: 2026-11-14
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Pakistan personal income tax and AOP working paper v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Resident individuals, self-employed professionals, freelancers, sole proprietors and AOPs preparing a reviewed working paper for Pakistan tax year 2026, meaning 1 July 2025 to 30 June 2026 under s.74. Use the Finance Act 2025 table applicable to this period, not a tax-year-2025 baseline or later prospective table. Companies, securities/property gains, treaties/non-residents, provincial services tax and employer monthly payroll have separate computations.

Quick answer: determine residence and the actual income category, separate final-tax receipts, then apply the salary table only if salary exceeds 75% of taxable income (in words on the page). At exactly 75%, use the other table. Keep the s.4AB surcharge, s.4C super tax and any minimum tax distinct. [ITO ss.4AB,4 C,11,74 and First Schedule Division I](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

## Rates, bands and thresholds

All amounts below are PKR, annual taxable income, for tax year 2026. Each formula gives total ordinary table tax for its band, before separate credits/charges.

| Test or income band | Amount, formula and conditions | Official source |
|---|---|---|
| Salary-table taxable income: Up to 600,000 | 0% | [First Schedule Part I Division I(2)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Salary-table taxable income: Over 600,000 to 1,200,000 | 1% of excess over 600,000 | [First Schedule Part I Division I(2)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Salary-table taxable income: Over 1,200,000 to 2,200,000 | 6,000 + 11% of excess over 1,200,000 | [First Schedule Part I Division I(2)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Salary-table taxable income: Over 2,200,000 to 3,200,000 | 116,000 + 23% of excess over 2,200,000 | [First Schedule Part I Division I(2)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Salary-table taxable income: Over 3,200,000 to 4,100,000 | 346,000 + 30% of excess over 3,200,000 | [First Schedule Part I Division I(2)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Salary-table taxable income: Over 4,100,000 | 616,000 + 35% of excess over 4,100,000 | [First Schedule Part I Division I(2)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Non-salary individual/AOP taxable income: Up to 600,000 | 0% | [Division I(1) and professional-firm proviso](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Non-salary individual/AOP taxable income: Over 600,000 to 1,200,000 | 15% of excess over 600,000 | [Division I(1) and professional-firm proviso](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Non-salary individual/AOP taxable income: Over 1,200,000 to 1,600,000 | 90,000 + 20% of excess over 1,200,000 | [Division I(1) and professional-firm proviso](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Non-salary individual/AOP taxable income: Over 1,600,000 to 3,200,000 | 170,000 + 30% of excess over 1,600,000 | [Division I(1) and professional-firm proviso](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Non-salary individual/AOP taxable income: Over 3,200,000 to 5,600,000 | 650,000 + 40% of excess over 3,200,000 | [Division I(1) and professional-firm proviso](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Non-salary individual/AOP taxable income: Over 5,600,000 | 1,610,000 + 45% of excess over 5,600,000; 40% marginal rate instead for a professional AOP legally prohibited from incorporating | [Division I(1) and professional-firm proviso](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| s.4AB surcharge: taxable income exceeds 10,000,000 | 10% of Division I income tax for individuals/AOPs; proviso gives 9% for an individual deriving income chargeable under Salary (figures in words on the page). Test the proviso separately from the salary-table percentage test | [s.4AB](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Individual residence, physical presence branch | At least 183 aggregate days in the tax year; government-posting and citizenship branches also apply (in words on the page) | [s.82(a),(c),(d)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Individual advance-tax exception | Latest assessed taxable income below 1,000,000 after the s.147(1) exclusions; exactly 1,000,000 is not below it (in words on the page) | [s.147(1)-(2)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Turnover-minimum-tax screen | Individuals/AOPs with turnover at least 100,000,000 in tax year 2017 or a later year, subject to s.113; general rate 1.25%, with specified-sector rates/exceptions (in words on the page) | [s.113; First Schedule Division IX](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Charitable-donation credit qualifying-amount cap | Individual/AOP 30% of taxable income; company 20%; if donation to associate, 15%/10% respectively; apply (A/B) x C, eligible donee and crossed-cheque cash-payment condition (percentages in words on the page) | [s.61(1)-(4)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Approved pension contribution credit | Eligible individual deriving salary/business income; qualifying contribution capped at 20% of taxable income, credit (A/B) x C (in words on the page); old age uplift expired by 30 June 2019 | [s.63(1)-(3) and dated provisos](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| AOP member-share audited-account boundary | Turnover at least 300,000,000 during the year or any preceding tax year requires financial statements audited by a firm of Chartered Accountants or Cost and Management Accountants and filed with the AOP income return for member exemption (in words on the page) | [s.92(1), second proviso](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |

## The base

### Residence and income heads

Test all s.82 branches: 183-day presence; federal/provincial official posted abroad; or citizen not present in another country for more than 182 days or not resident taxpayer of another country (figures in words on the page). An AOP is resident where control/management is wholly or partly in Pakistan at any time in the year, s.84. Do not infer non-residence solely from fewer than 183 days. Determine the whole tax-year position and refer dual residence, migration and treaties.

Section 11 has 5 heads: Salary, Property, Business, Capital Gains and Other Sources. Foreign-source income is included within the relevant head for a resident under s.11(5), not a sixth head; a non-resident includes Pakistan-source income under s.11(6). Freelance/professional business receipts are tested under s.18. Obtain gross income, actual allowable s.20 expenses, s.21 disallowances and asset/depreciation details; cash in a bank is not automatically taxable profit. [ss.11,18,20,21,82,84](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

### Computation sequence

1. Build a schedule by head and by ordinary, separate, final and minimum-tax treatment. Test s.154A exports under `pk-it-export-tax`, with PSEB/remittance and finality conditions. Exclude a genuinely final stream from ordinary bracket income; missing PSEB does not prove that all exports become ordinary income. Domestic receipts stay separate. Do not apply a historic Second Schedule clause 133 exemption or s.65 label without operative authority.
2. Compute ordinary taxable income after legally allowed deductions/losses. Section 57 ordinary business-loss carry-forward is limited to 6 succeeding tax years (in words on the page), with its separate depreciation and other loss restrictions; it is not an undocumented expense estimate or a foreign-credit carry-forward.
3. Compute the salary ratio using actual chargeable salary and taxable income. Apply the appropriate entire-income table; do not apply only a marginal band to all income or choose a higher table merely because the ratio is unknown.
4. Compute s.4AB separately using its actual taxable-income threshold and salary proviso. Do not impose 10% on every salaried case or confuse this with s.4C super tax. Refer high-income s.4C cases for the separate charge.
5. Compute eligible credits using their own formulas and conditions. Section 4(3) applies foreign tax credit first, then Part X credits, then ss.147/168 credits. Donation/pension credits use an average-rate formula; withholding is a tax credit where legally adjustable, not a reduction of gross receipts. Section 62 shares/sukuk credit is omitted; do not revive it. Historic s.65 industrial credits require their actual section and eligibility, not a generic claim.
6. Test s.113 turnover minimum tax if in scope; s.113C ACT is corporate and outside this individual/AOP computation. Under s.113(2)(c), qualifying excess minimum tax is adjusted against the specified Part I clause (1) of Division I or Division II liability for the 2 immediately succeeding tax years (in words on the page); where no tax was payable/paid, the whole minimum amount follows that conditional route. The former 3-year period was changed by Finance Act 2025. Industrial AOP WWF/WPPF needs specialist routing. Reconcile normal/minimum/separate charges, actual s.168 adjustable withholding and s.147 payments before stating balance or refund. The original invented universal ordering of minimum tax/surcharge/refund is not a substitute for each operative provision.
7. Prepare the resident individual's s.116 wealth statement and reconciliation. Under the first proviso to s.116(2), every AOP member must also furnish both statements for the year along with the AOP's income return; the former member-income threshold was omitted in 2013. This is distinct from the AOP's s.114 income return. For each required statement, reconcile opening/closing assets/liabilities, expenditure, tax, transfers and income. Never plug a gap; s.111 unexplained-income risk needs evidence. [ss.4,11,20,21,57,61-65,92,103,111,113,116,147,154 A,168](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

### AOP member treatment

An AOP is taxed separately. A member's share from taxed AOP income is exempt subject to s.92 conditions; an exempt AOP income stream has the statutory explanation. If a member is a company, exclude that corporate share from AOP computation and tax it separately at the company rate. Apply the rates-table condition: the qualifying firm must audit the accounts and the AOP must file them along with its income return, including where prior-year turnover triggers the boundary. Do not promise blanket member exemption or rely on an omitted s.92(2) for remuneration; member payments/disallowance require their operative s.21 analysis. [ss.21,92](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

## Deadlines and filing

| Obligation and conditions | Ordinary date/mechanic | Official source |
|---|---|---|
| Individual/AOP annual return | 30 September following tax-year end; ordinary tax-year-2026 date is 30 September 2026 (derived); applicable extension must be checked | [s.118(3)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Resident individual wealth/reconciliation; AOP-member first-proviso branch | Resident individual with own return; every AOP member also with the AOP's income return; notice-based statements by their notice date | [ss.116,118(4)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Return-balance tax payment | By the return due date | [s.137(1)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Individual advance-tax quarters | 15 September,15 December,15 March,15 June; s.147 exclusions/threshold/formula apply | [s.147(4 B)-(5)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| AOP advance-tax quarters | 25 September,25 December,25 March,15 June; turnover formula applies, not an individual-income threshold | [s.147(4),(5 A)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Extension application | Apply under s.119 with reasons before the applicable due date; not automatic relief | [s.119](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |

For an individual, s.147(4 B) uses latest assessed tax divided by 4 less relevant quarter credits, with its statutory exclusions; it is not simply current brackets on last year's income. For an AOP, s.147(4) uses quarter turnover x latest assessed tax / latest-year turnover less relevant quarter tax. Estimates have their own conditions. Refer changed-income, missing-turnover or estimate cases rather than invent inputs. [s.147](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

In IRIS open the actual year and individual/AOP return, complete each applicable income/separate-tax schedule, reconcile tax deductions to CPRs and complete each required individual/AOP-member wealth statement and reconciliation. Generate a PSID for any due balance, pay through the authorised channel and keep the CPR, then submit the reviewed return/statements and retain acknowledgements. Reconcile prefilled deductions to taxpayer, section, period and actual payment; do not treat prefilling as proof of credit entitlement. Exact current screens/boxes are not certified here.

## Penalties and interest

| Default and complete basic condition | Published rule | Official source |
|---|---|---|
| Late annual return | Higher of 0.1% of tax payable or 1,000 per day; minimum 10,000 for individual with at least 75% salary income,50,000 otherwise; maximum 200% tax payable; statutory reductions 75%,50%,25% for filing within 1,2,3 months of due/extended due date (in words on the page; figures shown as numerals) | [s.182 table item 1](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Unpaid ordinary tax/penalty/other covered amount | Higher of 12% per annum and KIBOR+3%; period due date to payment; s.205(1) proviso may affect an appealed-order case (in words on the page) | [s.205(1)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Unpaid advance tax | 12% yearly under s.205(1 A), due date to payment or return due date, whichever earlier; s.205(1 B) separately tests the 90% estimated-tax shortfall and its statutory accrual window (in words on the page) | [Current s.205(1 A)-(1 B)](https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf); [enacted Finance Act 2024 amendment 31](https://download1.fbr.gov.pk/Docs/2024630146346801FinanceAct-2024.pdf) |

For default after 1 July 2026, s.182 item 1 now defines tax payable as the higher of current assessed/treat-as-assessed tax and tax payable for the immediately preceding duly-filed return year. Do not reuse the older explanation for a current late-return calculation. The 2025 consolidation incorrectly spreads the Finance Act 2024 rate change into advance-tax subsections: enacted amendment 31 changes **s.205(1) only**; current s.205(1 A)/(1B) and withholding s.205(3) print 12% yearly. This is an editorial reconciliation, not a claimed prospective 2026 rate reduction. Preserve each subsection's dates and relief. [Current ss.182/205](https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf); [Finance Act 2024 amendment 31](https://download1.fbr.gov.pk/Docs/2024630146346801FinanceAct-2024.pdf), read 2026-11-14.

Wealth-statement default is a separate s.182 offence; s.182A concerns late-return consequences, not a generic wealth-statement penalty. Concealment/false statements, audits under s.177, amendments under s.122, recovery and appeals require specialist handling. No guaranteed refund processing time or audit selection is asserted.

## Cross-border points

Residents include relevant foreign-source income within each head, with actual gross receipts/foreign withholding supported. Section 103 credit is the lesser of foreign income tax paid and Pakistan tax at the average Pakistan rate on net foreign-source income, tested separately by head; speculation is separately treated. Tax must be paid within 2 years after the income year end (in words on the page). Unused credit is neither refunded nor carried back/forward. Treaty relief needs the actual s.107 treaty, residence and other conditions; it is not an automatic foreign-income exemption. Final s.154A income does not also get a foreign-tax credit. [ss.11,103,107,154 A](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

Convert currency under s.71 at the applicable SBP rate on the date the amount is taken into account under the Ordinance; the old s.72 receipt-date citation was wrong. Keep the date/rate evidence. Refer foreign-asset statements/amnesty claims, treaty positions and non-resident mixed-source cases.

ATL affects specified withholding events under the Tenth Schedule, with general uplift and express special/excluded sections; it is not a universal salary multiplier. Determine event-date status and any late-filer rule. No weekly refresh promise or blanket retrospective rate reduction is made. The 2025 text's property late-filer rule 1A was omitted by Finance Act 2026 amendment 47(a); do not carry that historical rule into later events. [Enacted amendment](https://download1.fbr.gov.pk/Docs/20266291261044366FinanceAct2026.pdf). The actual surcharge amounts, entry requirements and event rates are handled in `pk-withholding-tax`; an unverified status is an open item, not permission to invent a final rate.

## Two worked examples that recompute

### Saad's mixed export and domestic business example, corrected

Saad remains the single Karachi-resident freelance developer with no dependents in the earlier case, with total fees 5,000,000 and no other income, foreign-tax credit or zakat assumed. Assume fully qualifying PSEB export proceeds 4,000,000 with authorised-dealer proof and all s.154A finality conditions; domestic receipts 1,000,000 and allowable attributable expenses 200,000. The old assumed 3% domestic-service withholding is not a verified tax-year-2026 rate or automatically an adjustable credit. Use actual section/treatment/payment evidence before claiming it.

```oa-check
name: Saad ordinary and final streams kept separate
inputs:
  export_proceeds: 4000000
  domestic_fees: 1000000
  allowable_domestic_expenses: 200000
steps:
  - export_final_tax: export_proceeds * 0.0025
  - ordinary_income: domestic_fees - allowable_domestic_expenses
  - ordinary_table_tax: max(0, ordinary_income - 600000) * 0.15
  - tax_before_other_tests: export_final_tax + ordinary_table_tax
expected:
  export_final_tax: 10000
  ordinary_income: 800000
  ordinary_table_tax: 30000
  tax_before_other_tests: 40000
```

If actual legally adjustable domestic credit were 30,000, the ordinary balance would be 0 (derived), but the old 3%-rate assumption does not prove that credit or override minimum-tax treatment. Without PSEB but with another qualifying s.154A service case and all conditions, the export withholding is 40,000 (derived at 1%), not automatically ordinary income. Only if the 4,000,000 stream genuinely belongs in ordinary business income and 200,000 is the complete supported cost would 4,800,000 ordinary income give 1,290,000 table tax (derived). That conditional historical alternative is retained, without the false claim that missing PSEB alone costs 1,280,000.

### Salary classification boundary

Both cases below assume total taxable income 3,000,000, no other charges/credits and correctly classified components. Salary 2,400,000 is 80%, so salary-table tax is 300,000. Recompute the formula rather than reuse an old illustrative payroll table:116,000+23% x 800,000 =300,000 (derived). Salary 2,000,000 is 66.6667% (derived), so non-salary table tax 590,000 applies to the whole taxable income.

```oa-check
name: Salary table versus non-salary table on same taxable income
inputs:
  taxable_income: 3000000
  salary_case_a: 2400000
  salary_case_b: 2000000
steps:
  - salary_percent_a: salary_case_a / taxable_income * 100
  - salary_percent_b: salary_case_b / taxable_income * 100
  - salary_table_tax: 116000 + (taxable_income - 2200000) * 0.23
  - non_salary_table_tax: 170000 + (taxable_income - 1600000) * 0.30
  - difference: non_salary_table_tax - salary_table_tax
expected:
  salary_percent_a: 80
  salary_percent_b: 66.6667
  salary_table_tax: 300000
  non_salary_table_tax: 590000
  difference: 290000
```

## Ask the client first

Obtain residence days/citizenship/foreign tax residence and government posting, individual/AOP/company status, salary and all other taxable/separate/final streams, full-year bank/ledger/salary certificates, allowable expense/asset records, prior returns, actual tax certificates/CPRs, event-date ATL and late-filing history, PSEB period/e-PRCs and export conditions, foreign tax/head/net-income evidence, qualifying donation/pension evidence, AOP deed/member types and current/prior turnover/audited accounts, loss history and each required individual/AOP-member wealth reconciliation.

Refuse a final filing computation without residence, income records and legal classification. Continue supported reconstruction while evidence is obtained. Refer company returns, employer monthly payroll, NCCPL gains, property gains/236 C/236 K, provincial services tax, historic amnesties/foreign-asset statements, s.4C super tax, audit/recovery/amendment/appeal matters and industrial WWF/WPPF. Never invent credits, revive omitted relief, double-tax a qualifying member share, assume blanket exemption, or file an unreviewed working paper.


### Current late-entry ATL route, November 2026

Current s.182A surcharge amounts are company 100,000/AOP 50,000/individual 25,000; these are current-action amounts, not the historical 20,000/10,000/1,000 table. For a late individual, r 81 B(2 B)-(2D) now allows IRIS **Form ATL-U** undertaking instead of the surcharge: the 6-month period starts from successful IRIS acknowledgment, with an undertaking not to purchase, acquire or otherwise obtain ownership or a beneficial interest in any property during that period. An established breach after electronic hearing withdraws the benefit from the breach date and ordinary rules then govern. Do not promise this route to an AOP/company or describe filing alone as automatic fee-free entry. Dated event status and actual charge conditions still control withholding. [Current ITO s.182A](https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf); [signed 10 November 2026 SRO 2097](https://download1.fbr.gov.pk/SROs/202611101511326308SRO2097of2026.pdf), read 2026-11-14 for the operative rule/form.

For the actual tax-year-2026 filing cycle, FBR Circular 04 of 2026-27 dated 15 October 2026 extends the filing date to **31 October 2026** for persons originally due 30 September 2026 and previously extended to 15 October. It does not extend every company return. Apply any individual further order only on its evidence; this circular does not itself state a general payment extension. [Official circular](https://download1.fbr.gov.pk/Docs/20261015221039470Extension.pdf), read and scanned page inspected 2026-11-14.

## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for Circular 04 of 2026-27, 15 October 2026, the 31 October extension for the original 30 September cohort; scanned signed page inspected | https://download1.fbr.gov.pk/Docs/20261015221039470Extension.pdf | 2026-11-14 |
| Read for current-action s.182 item 1 explanation and s.205(1)/(1 A)/(1 B)/(3)in the 2026 consolidation, plus enacted Finance Act 2024 amendment 31, on 2026-11-14 | https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf; https://download1.fbr.gov.pk/Docs/2024630146346801FinanceAct-2024.pdf. | 2026-11-14 |
| Read for ITO ss.4/4 AB,11,18,20-21,57,61-63,71,74,82/84,92,103,113,116,118,137,147,154 A,168,174,182/205 and First Schedule Division I/IX; operative text distinguished from historic footnotes | https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf | 2026-11-14 |
| Read for June 2026 consolidation s.154A/Division IVA period amendment; this skill uses tax-year-2026 effective law rather than automatically adopting later-year amendments | https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf | 2026-11-14 |

Not yet confirmed: client-specific residence/treaty/source/classification, actual tax credits and PSEB compliance, current IRIS field identifiers, any further individual deadline orders/ATL event details, complete super-tax/sector-minimum-tax/WWF/WPPF calculations, historical residual industrial-credit/amnesty claims and full dispute procedures, NTN/CNIC format lengths, split-year/treaty treatment, prescribed foreign-tax-credit proof, historical AOP member-share rate aggregation and statutory non-filer enforcement branches. The old 6-24-month refund estimate, blanket AOP remuneration exemption, and automatic PSEB-failure/ordinary-income assumption are not usable instructions. The historic pension age uplift is expired; no current uplift is claimed.
