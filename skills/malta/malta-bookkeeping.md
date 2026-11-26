---
name: malta-bookkeeping
description: "Use for 2026 Malta bookkeeping, a suggested chart of accounts, expense classification, asset capitalisation, accounting depreciation versus tax wear and tear, bank reconciliation, records and size-test screening. Includes two worked examples; eligibility and specialist referrals must be resolved before using a tax result."
version: 1.6
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 1
reviewed_by: Michael Cutajar
reviewed_on: 2026-11-08
domain: bookkeeping
---

# Malta Bookkeeping v1.6

Tax year 2026. Use this Guide for day-to-day bookkeeping. The chart, posting codes and statement layouts are suggestions; they do not establish a deduction, VAT recovery or framework eligibility. Statutory accounts are covered in `malta-financial-statements`; tax computations in `malta-income-tax`, `mt-corporate-tax` and `mt-estimated-tax`; VAT in `malta-vat-return`; contributions and payroll in `malta-ssc` and `malta-payroll`.

## Section 1: Quick Reference

| Field | Value | Source |
| --- | --- | --- |
| Accounts currency | A company's annual accounts use its share-capital currency | [Cap. 386 art. 187(1)](https://legislation.mt/eli/cap/386/eng/pdf) |
| Accounting reference date | Notify the Registrar within nine months of registration; otherwise 31 December | [Cap. 386 art. 164(2)](https://legislation.mt/eli/cap/386/eng/pdf) |
| Framework | GAPSME applies within regulations 4–5 unless the board/governing body resolves to use EU-adopted IFRS for that period. Public interest entities cannot use GAPSME; see Section 9 | [S.L. 281.05](https://legislation.mt/eli/sl/281.5/eng/pdf) |
| Company records | Receipts/payments and their purpose; assets/liabilities; for goods businesses, period-end stocks and supporting stocktakings, plus identifiable purchases/sales except ordinary retail sales. Records must explain transactions, disclose the position with reasonable accuracy and enable compliant accounts | [Cap. 386 art. 163(1)–(2)](https://legislation.mt/eli/cap/386/eng/pdf) |
| Business records for income tax | Income/expenditure, receipts/payments and transactions; annual profit and loss or equivalent statement; assets/liabilities, or a company balance sheet, supported by appropriate documents. Subject to any Commissioner exemption under article 19(3) | [Cap. 372 art. 19(1)–(4)](https://legislation.mt/eli/cap/372/eng/pdf) |
| Company retention | Ten years; bound/unified records: ten years from their last entry | [Cap. 386 art. 163(5)](https://legislation.mt/eli/cap/386/eng/pdf) |
| Income-tax retention | At least nine years after completion of the transaction, act or operation, except where Commercial Code article 26 or Companies Act articles 163(5) or 324(2) have been given effect | [Cap. 372 art. 19(5)](https://legislation.mt/eli/cap/372/eng/pdf) |
| VAT retention | At least six years from the relevant year end. For a late return, start at filing; for an article 28(1) correction, start when the Commissioner receives the correction request. For capital-goods deductions subject to adjustment, start at the end of the reference period; retain the capital-goods list as part of the records | [Cap. 406 art. 48(4)](https://legislation.mt/eli/cap/406/eng/pdf); [S.L. 406.12 regs 6–7](https://legislation.mt/eli/sl/406.12/eng/pdf) |
| Ordinary VAT rate | 18% for taxable supplies outside the special-rate categories; determine the supply's actual VAT treatment first | [Cap. 406 art. 19](https://legislation.mt/eli/cap/406/eng/pdf) |

## Section 2: Recommended Chart of Accounts

Use the following suggested codes to organise the records required by article 163 and article 19. Account names and codes are internal choices; apply the recognition and tax rules separately.

### Assets (1xxx)

| Code | Account | Notes |
| --- | --- | --- |
| 1000 | Non-current assets (control) | |
| 1010 | Intangible assets: software | Assess recognition separately; see Section 5 |
| 1020 | Intangible assets: goodwill | |
| 1100 | Property, plant and equipment | |
| 1110 | Land and buildings | |
| 1120 | Motor vehicles | Keep actual book cost; see Section 4 for the tax limitation |
| 1130 | Computer hardware | |
| 1140 | Furniture and fittings | |
| 1150 | Office equipment and other machinery | |
| 1160 | Leasehold improvements | |
| 1199 | Accumulated depreciation | Contra-asset |
| 1200 | Current assets (control) | |
| 1210 | Trade receivables | |
| 1220 | Other receivables | |
| 1230 | Prepayments | |
| 1240 | VAT input (recoverable) | Post only an established recoverable amount; see Section 3 |
| 1250 | Provisional tax paid | Track payments separately for the tax computation |
| 1300 | Bank: current account | |
| 1310 | Bank: savings account | |
| 1320 | Cash in hand | |
| 1330 | Petty cash | |

### Liabilities (2xxx)

| Code | Account | Notes |
| --- | --- | --- |
| 2000 | Non-current liabilities (control) | |
| 2010 | Bank loans (long-term) | |
| 2020 | Hire purchase and lease obligations (long-term) | |
| 2100 | Current liabilities (control) | |
| 2110 | Trade payables | |
| 2120 | Other payables | |
| 2130 | Accruals | |
| 2135 | Deferred income | Track customer advances; assess recognition under Section 3 |
| 2140 | VAT output (payable) | |
| 2150 | VAT control | Net position for MTCA |
| 2160 | Income tax payable | |
| 2165 | FSS tax and Class 1 SSC withheld | Payroll |
| 2170 | SSC payable (employer share) | |
| 2180 | Bank overdraft | |
| 2190 | Bank loans (current portion) | |
| 2200 | Directors' loan account | |

### Equity (3xxx)

| Code | Account | Notes |
| --- | --- | --- |
| 3000 | Share capital or owner's capital | |
| 3010 | Share premium | |
| 3100 | Retained earnings | |
| 3200 | Current year profit or loss | Clearing account |
| 3300 | Drawings (sole trader) | |
| 3400 | Dividends paid | Track distributions separately for the company-tax computation |

### Revenue (4xxx)

| Code | Account | Notes |
| --- | --- | --- |
| 4000 | Sales: services | |
| 4010 | Sales: goods | |
| 4020 | Sales: exports and intra-EU | Determine VAT treatment separately; see `malta-vat-return` |
| 4100 | Other operating income | |
| 4200 | Government grants (revenue) | |

### Cost of sales (5xxx)

| Code | Account | Notes |
| --- | --- | --- |
| 5000 | Purchases: goods for resale | |
| 5010 | Direct materials | |
| 5020 | Subcontractors | |
| 5030 | Import duties | |
| 5100 | Opening stock | |
| 5110 | Closing stock | Stock statements are a legal record where goods are dealt in (art. 163(1)(c)) |

### Operating expenses (6xxx)

| Code | Account | Notes |
| --- | --- | --- |
| 6000 | Rent: business premises | |
| 6010 | Rates and local levies | |
| 6020 | Electricity and water | Apportion if home office |
| 6030 | Telecoms and internet | Apportion if mixed use |
| 6040 | Insurance: business | |
| 6050 | Repairs and maintenance | Separate repairs from improvements; see Section 4 |
| 6100 | Salaries and wages | See Section 4 for the deduction conditions |
| 6110 | Employer SSC (Class 1) and Maternity Leave Fund | |
| 6120 | SSC Class 2 (self-employed) | Memo for tax; see Section 4 |
| 6200 | Accountancy and audit fees | |
| 6210 | Legal and professional fees | Split capital (for example share issue, property) from revenue |
| 6220 | Bank charges | |
| 6230 | Payment processing fees | |
| 6300 | Marketing and advertising | |
| 6310 | Travel: flights and accommodation | Business purpose only |
| 6320 | Travel: local transport | |
| 6330 | Motor vehicle running costs | Business share only |
| 6340 | Motor vehicle fuel | Business share only |
| 6400 | Office supplies and stationery | |
| 6410 | Software subscriptions | |
| 6420 | Training | |
| 6430 | Professional subscriptions | |
| 6440 | Postage and courier | |
| 6500 | Depreciation | Accounting charge; added back for tax and replaced by wear and tear |
| 6600 | Bad debts written off | See Section 4 for the tax test |
| 6610 | Provision for doubtful debts (movement) | Assess the tax adjustment under Section 4 |
| 6700 | Entertainment | Flag for tax; see Section 4 |
| 6710 | Fines and penalties | Refer tax treatment under Section 4 |
| 6800 | Sundry expenses | |

### Other income and expenses (7xxx)

| Code | Account | Notes |
| --- | --- | --- |
| 7000 | Interest received | |
| 7010 | Interest paid | |
| 7100 | Profit or loss on disposal of assets | Refer the disposal tax computation under Section 4 |
| 7200 | Foreign exchange gains and losses | |

### Tax (8xxx)

| Code | Account | Notes |
| --- | --- | --- |
| 8000 | Income tax expense (current) | |
| 8010 | Deferred tax | |

## Section 3: Revenue Recognition

For a GAPSME entity, use accrual accounting: recognise transactions in the period when their effects occur, rather than simply when cash moves (Schedule paragraph 3.3). Exclude VAT collected for the authority from revenue (paragraph 6.4).

For service revenue, use the stage of completion only when revenue, stage of completion, costs incurred and costs to complete can be measured reliably and economic benefits are probable. Otherwise recognise revenue only to the extent of recognised expenses that are recoverable (paragraphs 6.7–6.8). An advance is not automatically earned revenue: progress payments and advances often do not reflect work performed (paragraph 6.13). Track unearned customer advances in 2135 and transfer to revenue as the applicable recognition conditions are met, rather than automatically spreading every contract evenly over time. [GAPSME Schedule](https://legislation.mt/eli/sl/281.5/eng/pdf).

For an ordinary taxable Article 10 sale, separate output VAT into 2140. Put only an established deductible input amount in 1240: registration alone does not establish recovery. A deduction requires the applicable qualifying use, supporting tax invoice/import document, records and other Tenth Schedule conditions; blocked inputs and mixed/exempt use can restrict recovery. Do not charge VAT on an Article 11 exempt supply only where the person is registered and entitled to that exemption. [Cap. 406 articles 22–23 and Fifth, Sixth and Tenth Schedules](https://legislation.mt/eli/cap/406/eng/pdf).

For accounting impairment/write-off of receivables (6600/6610) or IFRS recognition: Check this point with one of our partner accountants.

## Section 4: Expense Classification and Tax

For income tax, article 14(1) allows expenses incurred during the year preceding the assessment year to the extent wholly and exclusively incurred in producing income. Article 26 excludes private spending except where expressly allowed, non-income-producing spending, capital expenditure except as permitted by articles 14 and 23, improvements, amounts recoverable under insurance/indemnity, non-income-producing rent and voluntary payments. A posting code never establishes deductibility. [Cap. 123](https://legislation.mt/eli/cap/123/eng/pdf).

| Expense | Code | Treatment |
| --- | --- | --- |
| Business rent | 6000 | Apply article 14(1)(b): premises occupied for acquiring income |
| Home utilities, telecoms, travel and motor running costs | 6020, 6030, 6310, 6330, 6340 | Document the income-producing share; do not claim an unsupported private share. A log/apportionment record is a recommended evidence control |
| Repairs versus improvements | 6050 | Article 14(1)(c) covers repairs to premises/plant/machinery and renewal, repair or alteration of implements/utensils/articles employed in acquiring income; article 26 excludes capital/improvement costs, subject to its express exceptions |
| Wages | 6100 | Rule 4(1),(4): wholly/exclusively income-producing, and correctly reported in the FS3 and FS7 furnished no later than twelve months after the FSS deadline. For wages to a spouse, rule 4(5) also requires the spouse to have paid SSC on the basic wage/salary. Fringe-benefit deduction limits need separate assessment |
| Depreciation | 6500 | Reverse the accounting charge in the tax computation; calculate the statutory allowance separately under article 14(1)(f) and S.L. 123.01 |
| Bad debts / general provision | 6600, 6610 | Article 14(1)(d) requires a trade/business/profession/vocation debt proved to the Commissioner to have become bad in the relevant preceding year; a general provision alone does not meet that test. Recoveries of previously written-off/allowed bad debts are business receipts in the recovery year |
| Drawings | 3300 | Suggested posting to equity, separate from expenses |

[Income Tax Act articles 14 and 26](https://legislation.mt/eli/cap/123/eng/pdf); [Income Tax (Deductions) Rules, rule 4](https://legislation.mt/eli/sl/123.7/eng/pdf).

**Vehicle cost limitation.** Rule 3(1) caps qualifying wear-and-tear/initial allowance and balancing computations at EUR 14,000 acquisition cost. Rule 3(4) covers mechanically propelled individual-transport vehicles, excluding types not commonly used and unsuitable as private vehicles, vehicles used wholly/mainly for public hire/carriage in the ordinary business, and driving-instruction vehicles used wholly/mainly in that business. Keep actual cost in the books. [S.L. 123.07 rule 3](https://legislation.mt/eli/sl/123.7/eng/pdf).

- Leased vehicles, including the EUR 14,000 listed-price limit, occasional use, replacement vehicles and who bears wear and tear: Check this point with one of our partner accountants.
- Entertainment and fines/penalties: Check this point with one of our partner accountants.
- Personal Class 2 contributions: retain a memo pending the tax computation. Check this point with one of our partner accountants.
- Asset disposal balancing statements and fringe-benefit deductions: Check this point with one of our partner accountants.

## Section 5: Asset or Expense

For GAPSME tangible fixed assets, recognise an asset only where future economic benefits are probable and cost can be measured reliably (Schedule 7.2). Initial measurement is cost (7.3); it includes non-refundable purchase taxes and directly attributable ready-for-use costs (7.4). A written capitalisation policy must apply those requirements; it is not a tax exemption. Software and goodwill recognition: Check this point with one of our partner accountants.

For tax, apply article 26's capital-expenditure rule and any specific statutory allowance; do not invent an expense threshold.

For VAT, S.L. 406.12 covers tangible fixed assets usable long term in an economic activity. Small equipment, working tools and office furniture with price/open-market value **below** EUR 1,160, and packaging, are excluded. Repairs, maintenance, spare parts for them and rental/use charges are not input tax on capital goods under that definition. Whether VAT is included in the EUR 1,160 boundary: Check this point with one of our partner accountants.

The reference period is five years for non-property capital goods and twenty for immovable property. It starts on the first day of the first month of the deduction tax period, except that delayed first use shifts the start to the first day of the first-use tax period. Keep the list and deductions/adjustments. For an actual change of use, disposal or cessation adjustment: Check this point with one of our partner accountants. [S.L. 406.12 regulations 2–7](https://legislation.mt/eli/sl/406.12/eng/pdf).

### Tax wear and tear: minimum years (S.L. 123.01 Schedule)

These are tax minimums, not accounting lives. Accounting depreciation follows the framework and the asset's useful life.

| Category | Minimum years |
| --- | --- |
| Computers and electronic equipment; computer software; aircraft airframes, aircraft engines, aircraft engine or airframe overhaul, and aircraft interiors and other parts | 4 |
| Motor vehicles; other machinery | 5 |
| Catering equipment; air-conditioners; medical equipment; communication and broadcasting equipment; construction and excavation equipment; equipment mainly designed or used for the production of water or electricity | 6 |
| Furniture, fixtures, fittings and soft furnishings; lifts and escalators; ships; other plant | 10 |
| Electrical and plumbing installations and sanitary fittings | 15 |
| Cable and pipeline infrastructure | 20 |

Use straight-line tax allowances over no less than the scheduled years. Cost follows generally accepted accounting principles; keep cost records/documentation, and reduce the allowance to income-producing use. Rule 7(a) gives a full-year allowance for a qualifying acquisition/completion during the year when the part-year use arises only from that event. Rule 7(b) denies an allowance where sale/transfer, destruction or the specified putting-out-of-use event occurs before the final day. These are not rules for every interruption of use. Cumulative deductions cannot exceed the applicable original cost; unused allowances carry forward against the same source under article 14(1)(f). [S.L. 123.01 rules 3–7, 11](https://legislation.mt/eli/sl/123.1/eng/pdf); [Cap. 123 article 14(1)(f)](https://legislation.mt/eli/cap/123/eng/pdf).

For last-day disposals and industrial buildings (including the 2% annual and one-tenth initial allowance questions): Check this point with one of our partner accountants.

GAPSME accounting depreciation uses cost/revaluation less residual value over useful life and a method reflecting consumption; it begins when available for use. The tax table does not set accounting lives. [Schedule 7.20–7.21](https://legislation.mt/eli/sl/281.5/eng/pdf).

## Section 6: Profit and Loss Layout

Illustrative management-account grouping only. Statutory layout/disclosure compliance under the applicable framework: Check this point with one of our partner accountants.

```
INCOME STATEMENT
For the year ended [date]

Revenue                                          xxx
Cost of sales                                   (xxx)
                                                -----
GROSS PROFIT                                     xxx

Other operating income                           xxx
Administrative expenses                         (xxx)
Distribution costs                              (xxx)
Other operating expenses                        (xxx)
                                                -----
OPERATING PROFIT                                 xxx

Finance income                                   xxx
Finance costs                                   (xxx)
                                                -----
PROFIT BEFORE TAX                                xxx

Income tax expense                              (xxx)
                                                -----
PROFIT FOR THE YEAR                              xxx
```

## Section 7: Balance Sheet Layout

Illustrative management-account grouping only; apply the same statutory-layout referral as Section 6:

```
BALANCE SHEET
As at [date]

NON-CURRENT ASSETS
  Intangible assets                              xxx
  Property, plant and equipment                  xxx
                                                -----
                                                 xxx
CURRENT ASSETS
  Inventories                                    xxx
  Trade and other receivables                    xxx
  Cash and cash equivalents                      xxx
                                                -----
                                                 xxx
                                                -----
TOTAL ASSETS                                     xxx

EQUITY
  Share capital                                  xxx
  Retained earnings                              xxx
                                                -----
                                                 xxx
NON-CURRENT LIABILITIES
  Borrowings                                     xxx
CURRENT LIABILITIES
  Trade and other payables                       xxx
  Current tax liabilities                        xxx
  Borrowings (current portion)                   xxx
                                                -----
TOTAL EQUITY AND LIABILITIES                     xxx
```

## Section 8: Bank Reconciliation Patterns

Statement layouts differ by bank and change over time. Map the columns from the client's own export before importing.

| Pattern in description | Likely classification |
| --- | --- |
| Incoming transfer | Check whether it is revenue, a loan, capital or a refund |
| Direct debit or standing order | Utility, subscription, insurance, rent or loan repayment |
| Card payment | Expense; check the merchant and the receipt |
| Bank charges | 6220 |
| Utility company | 6020 |
| MTCA (tax, VAT, SSC) payment | Clear the correctly accrued liability or provisional-tax asset. This payment entry does not decide the original expense: employer SSC, nonrecoverable VAT, tax and penalties need their own charge or capitalisation analysis |
| Own-account transfer | Match both sides; do not treat as income or an expense, and keep both bank movements |

## Section 9: Size Tests (summary)

GAPSME eligibility and Companies Act exemptions are separate tests. The following GAPSME limits apply at the balance sheet date; meet at least two of three. Medium-sized means not small but within the medium limits. Public interest entities are excluded.

| GAPSME test | Balance sheet total | Revenue | Average employees |
| --- | --- | --- | --- |
| Small | EUR 4,000,000 | EUR 8,000,000 | 50 |
| Medium-sized | EUR 20,000,000 | EUR 40,000,000 | 250 |

Balance sheet total means total assets; revenue is net of rebates, VAT and directly linked taxes; where revenue is not relevant include other-source income. Compute whole-time average employees as aggregate full weeks worked divided by the period's full weeks, rounded to the nearest number; part-time as aggregate hours divided by full weeks and forty, rounded to the nearest number. Annualise revenue for a non-twelve-month period. Test the first period on its own; subsequent exceedance/cessation affects status only after two consecutive years. Small GAPSME financial statements comprise balance sheet, income statement and notes; medium entities also need changes in equity and cash flows. [S.L. 281.05 regulations 3–5](https://legislation.mt/eli/sl/281.5/eng/pdf).

For a standalone company outside the public-interest category, article 185(1)'s small-company limits are EUR 5,000,000 total assets, EUR 10,000,000 net turnover and 50 average employees (at least two not exceeded), relieving the directors' report requirement; own-share acquisition information required by the Sixth Schedule must instead be in the notes. The [MBR commencement instruction](https://www.mbr.mt/post/informative-note-entry-into-force-of-legislation-1) applies these new limits only to periods **starting on or after 20 March 2026**, with no early/retroactive adoption. They therefore cannot be applied to calendar-year 2025 or 2026 periods.

The separate article 185(2) exemption from Companies Act auditor requirements is for **private** companies not exceeding at least two of EUR 46,600 balance sheet total, EUR 93,000 net turnover and two average employees. After the first balance sheet date, changes to article 185(1)/(2) status require two consecutive periods. Total assets, net turnover and average employees follow article 185(4),(9),(10); the net-turnover and employee computations above also apply here. [Cap. 386 article 185](https://legislation.mt/eli/cap/386/eng/pdf).

For periods starting before 20 March 2026, parent/group eligibility, public-interest obligations, or whether an audit/review is nevertheless required for income tax: Check this point with one of our partner accountants. A Companies Act exemption alone does not settle the income-tax documentation requirement in article 19(4)(a). For a self-employed person's reporting obligations beyond article 19 records: Check this point with one of our partner accountants.

## Section 10: Interaction with Tax Skills

Reconcile tax-adjustment schedules to 6500, 6600/6610 and private spending; keep Class 2 (6120) in a separate memo until resolved. Reconcile provisional tax (1250), distributions (3400), VAT (1240/2140/2150) and payroll (6100/6110/2165) to their supporting records. The companion Guides named at the start identify the computation topic; do not infer a relief or eligibility from a cross-reference.

## Section 11: Worked Examples

### Example 1: laptop, accounting depreciation against tax wear and tear

A company with a 31 December year end buys a laptop for EUR 1,600 (net of recoverable VAT) on 1 October 2026. Its policy depreciates computers over 3 years from the month of purchase. Assume GAPSME applies, zero residual value, ready for use on 1 October, ordinary arm's-length purchase, full income-producing use through year end and adequate cost records. The three-year accounting life is a case input, not a prescribed life. Assume sufficient same-source taxable profits and no prior allowance on this new asset.

- Accounting depreciation for 2026: 1,600 ÷ 3 × 3 ÷ 12 = EUR 133.33.
- Tax wear and tear for 2026: 1,600 ÷ 4 = EUR 400, a full year under S.L. 123.01 rule 7(a).
- Tax adjustment: add back EUR 133.33 and deduct EUR 400, a net reduction of EUR 266.67 in chargeable income.

```oa-check
name: Laptop bought 1 October 2026, depreciation against wear and tear
inputs:
  cost: 1600
  accounting_years: 3
  months_owned: 3
  tax_years: 4
steps:
  - accounting_depreciation: round(cost / accounting_years * months_owned / 12, 2)
  - wear_and_tear: cost / tax_years
  - net_reduction: wear_and_tear - accounting_depreciation
expected:
  accounting_depreciation: 133.33
  wear_and_tear: 400
  net_reduction: 266.67
```

### Example 2: recording an Article 10 sale and a capital good purchase

An Article 10 registrant invoices EUR 2,360 including 18% VAT and buys a printer-copier for EUR 1,416 including 18% VAT. Assume both are ordinary 18% taxable supplies; the purchase has full qualifying taxable-business use, a compliant invoice and satisfied deduction conditions, with no blocked input. Assume the price is the only asset cost. For the tax allowance assume an ordinary arm's-length acquisition during 2026, put to full income-producing use through year end, documented cost, no prior allowance and sufficient same-source taxable profits.

- Sale: 2,360 ÷ 1.18 = EUR 2,000 to 4000; EUR 360 to 2140.
- Purchase: 1,416 ÷ 1.18 = EUR 1,200 to 1150; EUR 216 to 1240.
- The printer costs at least EUR 1,160 whether or not VAT is counted, so it goes on the VAT capital goods list (S.L. 406.12). For this illustration, documented preponderating use places it in "other machinery": minimum 5 years, EUR 240 wear and tear in 2026. Do not apply that classification automatically to a printer-copier: electronic equipment has a different life, and rule 4 requires classification by preponderating use.
- Net VAT for these two lines, assuming both belong in the same return and no other entries: 360 − 216 = EUR 144 payable.

```oa-check
name: Article 10 sale and capital good purchase at 18%
inputs:
  sale_gross: 2360
  purchase_gross: 1416
  rate: 0.18
steps:
  - sale_net: sale_gross / (1 + rate)
  - output_vat: sale_gross - sale_net
  - purchase_net: purchase_gross / (1 + rate)
  - input_vat: purchase_gross - purchase_net
  - net_vat_payable: output_vat - input_vat
  - wear_and_tear: purchase_net / 5
expected:
  sale_net: 2000
  output_vat: 360
  purchase_net: 1200
  input_vat: 216
  net_vat_payable: 144
  wear_and_tear: 240
```

## Section 12: Ask the Client First

1. Company or self-employed? If a company, its accounting reference date and whether the board chose IFRS.
2. VAT registration: Article 10, 11 or 12?
3. Any cars, and their cost or listed price and business use?
4. Does anyone use business assets or premises privately?
5. Payroll: obtain the FS3/FS7 records, reporting dates and any spouse or fringe-benefit details.
6. Which bank exports are available, and in what format?

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

> Contributed by Michael Cutajar.

## Sources

Read 26 November 2026: [Companies Act articles 163–164, 185, 187](https://legislation.mt/eli/cap/386/eng/pdf); [Income Tax Management Act article 19](https://legislation.mt/eli/cap/372/eng/pdf); [Income Tax Act articles 14, 26](https://legislation.mt/eli/cap/123/eng/pdf); [Wear and Tear Rules](https://legislation.mt/eli/sl/123.1/eng/pdf); [Income Tax (Deductions) Rules](https://legislation.mt/eli/sl/123.7/eng/pdf); [GAPSME regulations and Schedule](https://legislation.mt/eli/sl/281.5/eng/pdf); [VAT capital-goods regulations](https://legislation.mt/eli/sl/406.12/eng/pdf); [MBR commencement instruction](https://www.mbr.mt/post/informative-note-entry-into-force-of-legislation-1).

Applicable VAT Act proof for the ordinary rate, deduction conditions, Article 11 exemption and retention is reused from the completed 23 November 2026 source read supporting `malta-vat-return`; [Cap. 406](https://legislation.mt/eli/cap/406/eng/pdf). That original read date is preserved.

Not yet confirmed: the treatments explicitly referred to a partner accountant remain non-usable until resolved; no tax result is supplied for those points.
