---
name: bs-income-tax
description: >
  Bahamas individuals, employees, self-employed persons and sole traders for
  2026. The Bahamas has no personal income tax, so this skill works out what an
  individual does pay - National Insurance (NIB) contributions at the 2024 rates
  (employee 4.65%, employer 6.65%, self-employed 10.3%, voluntary 6.5%), the
  business licence tax on turnover (none up to BSD 100,000, then 0.5%, 0.75%,
  1.25% and from July 2026 1.5% above BSD 175 million), VAT registration at BSD
  100,000, real property tax and VAT on property conveyances. Trigger on do I
  pay income tax in the Bahamas, NIB contributions, business licence Bahamas,
  self-employed Bahamas, real property tax Bahamas. Built from Bahamian
  legislation and DIR pages; not reviewed by an accountant.
version: 1.0
jurisdiction: BS
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: income-tax
type: computation
---

# Bahamas individuals: no income tax, and what is paid instead

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

| Field | Value |
|---|---|
| Country | Commonwealth of The Bahamas |
| Personal income tax | None. There is no income tax law, no return and no tax on salary, fees, rent, dividends, interest or gains |
| Tax year | Calendar 2026 |
| What individuals pay | NIB contributions; business licence tax if in business; VAT if registered; real property tax if owning property; VAT on property conveyances |
| Authorities | National Insurance Board (NIB); Department of Inland Revenue (DIR) for business licence, VAT and real property tax |
| Currency | BSD, at par with USD; treat amounts as equal, no conversion |

## Who this applies to

Employees, self-employed persons and sole traders living or working in The Bahamas, and individuals owning or buying Bahamian property. Companies go to `bs-corporate-income-tax`; employer payroll detail to `bs-payroll-social`; VAT returns to `bahamas-vat`; registering a business to `bs-company-formation`.

The basic answer to "do I pay income tax in the Bahamas" is no. No Bahamian law imposes an income tax on individuals, whether resident or not, so there is no income tax return to file. Do not invent one.

## Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
|---|---|---|---|
| Personal income tax | None | No income tax Act exists in the Bahamian statute list | Bahamas legislation, Acts by year and index: https://laws.bahamas.gov.bs/cms/legislation/acts_only/acts-by-year.html |
| NIB employee rate | 4.65% of insurable wages | Fifth Schedule 3.9% plus half of the 1.5 point increase from 1 July 2024 | National Insurance (Contributions) (Amendment) Regulations 2024, regs 4 and 9: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0037S/2024-0037S.pdf |
| NIB employer rate | 6.65% of insurable wages | Fifth Schedule 5.9% plus half of the 1.5 point increase | same |
| NIB combined, employed person | 11.30% | 9.8% plus 1.5 points | same |
| NIB self-employed rate | 10.30% of insurable income | Fifth Schedule 8.8% plus 1.5 points (reg. 30(1A)), self-employed under 65 not receiving retirement benefit | same |
| NIB voluntarily insured | 6.50% | 5.0% plus 1.5 points (reg. 35(1A)) | same |
| NIB, employed person 65 or over in receipt of retirement benefit, or earning under 50% of the ceiling while receiving it | Employer 2.0% only | Fifth Schedule rows | same |
| NIB insurable wage ceiling | BSD 810 a week | Effective July 2024 | NIB, contributions: https://www.nib-bahamas.com/contributions |
| NIB payment deadline | By the 15th of the following month | | same |
| Business licence tax, turnover not over BSD 100,000 | Exempt | s. 38(1)(i); not for a family office, financial services entity, IBC or proprietary trading business (s. 38(2)) | Business Licence (Amendment) Act 2024, s. 8: https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/08/Business-Licence-Amendment-Act-2024.pdf |
| Business licence tax, turnover over BSD 100,000 to 500,000 | 0.5% of turnover | General businesses, Second Schedule Part I para (1)(a) | same |
| Business licence tax, turnover over BSD 500,000 to 5 million | 0.75% of turnover | Para (1)(b) | same |
| Business licence tax, turnover over BSD 5 million | 1.25% of turnover | Para (1)(c) | same |
| Business licence tax, turnover over BSD 175 million | 1.5% of turnover | New para (1)(d) from 1 July 2026 | Business Licence (Amendment) Act 2026, s. 8: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0022A/2026-0022A.pdf |
| Farming, fishing, food processing | 0% to BSD 100,000; 0.5% over 100,000 to 500,000; 0.75% above | Not salt exporters | Business Licence (Amendment) Act 2024, s. 9: https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/08/Business-Licence-Amendment-Act-2024.pdf |
| Accountant's report with renewal | Turnover BSD 250K or more: independent accountant's report; BSD 250K to 4.99M: review report by a BICA member; BSD 5 million or more: audited statements | DIR renewal facts | DIR, renewing a business licence: https://inlandrevenue.finance.gov.bs/business-licence/renewing-business-licence/ |
| VAT registration | Taxable activity over BSD 100,000 | Past or next 12 months; see `bahamas-vat` | DIR VAT FAQs: https://inlandrevenue.finance.gov.bs/value-added-tax/faqs/ |
| Real property tax, owner-occupied | First BSD 300,000 exempt; next BSD 200,000 at 0.625%; balance at 1% | Owner lives there and uses it only as a dwelling | DIR, RPT FAQs: https://inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/ |
| Real property tax, owner-occupied cap | BSD 150,000 a year | s. 3(2) proviso as replaced | Real Property Tax (Amendment) Act 2026, s. 3: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0021A/2026-0021A.pdf |
| Real property tax, foreign owner-occupied | 0.625% on the part up to BSD 1 million; 1% on the part above; cap BSD 200,000 | New s. 3(2)(aa), Act in force 1 July 2026 | same |
| Real property tax, residential of 4 units or fewer, not owner-occupied | BSD 300 flat up to BSD 75,000; 0.625% above | DIR FAQ | DIR, RPT FAQs: https://inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/ |
| Real property tax, commercial or foreign-owned rental | 0.75% on the first BSD 500,000; 1% on the next BSD 1.5 million; 1.5% on the balance | DIR FAQ | same |
| Real property tax, due date and discount | Due 31 March; 10% discount if paid in full by 31 March | | same |
| Real property tax, late | 5% surcharge on 1 January if unpaid at 31 December; 5% interest on tax unpaid at the end of each tax year | | same |
| Pensioner discount | 50% of the balance after the BSD 300,000 exemption, on home value not over BSD 1 million | Bahamian, 65 or over, NIB senior citizen card | same |
| VAT on property conveyances | Third Schedule rates (2.5% to 10%) | Replaces the stamp duty bands in the previous version; see `bahamas-vat` | VAT Act reprint, Third Schedule: https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf |

## The base

### NIB

1. Find the weekly insurable wage or income: actual weekly earnings, capped at the NIB ceiling of BSD 810 a week (BSD 42,120 a year over 52 weeks).
2. Employed: employee share 4.65%, employer share 6.65%; the employer deducts the employee share and pays both.
3. Self-employed: 10.30% of insurable income, paid by the person.
4. Voluntary: 6.50%.
5. Earnings above the ceiling attract no NIB. NIB is a social insurance contribution, not income tax.

Ten NIB benefits are funded by contributions (sickness, maternity, funeral, retirement, invalidity, survivors, unemployment, industrial injury, disablement, death). A contribution paid late but within 12 months after the end of the year it was due counts as paid on time for retirement and invalidity benefit (reg. 16 as replaced in 2024).

### Business licence tax

Turnover is total revenue from business activities, in money and money's worth, without deductions (DIR renewal page). The tax is on turnover, not profit, so home office and vehicle allocations do not reduce it; they matter only for VAT input recovery. Use the band rate for the business's turnover. Each year:

- **Estimated tax** for the year = rate × prior year's turnover (s. 35(7)).
- **Unpaid tax** for the prior year = actual tax less estimated tax paid; an overpayment is a credit for the next year (s. 35(3)).

### Real property tax

Owner-occupied property: exempt to BSD 300,000, 0.625% on the next BSD 200,000, 1% on the rest, capped at BSD 150,000 a year. Partly owner-occupied: the exemption is in proportion to the space occupied, not over BSD 300,000 (DIR FAQ). RPT carries no VAT.

### Bank-statement patterns (kept from the previous version)

| Pattern | Classification | Treatment |
|---|---|---|
| NIB CONTRIBUTION, NIB PAYMENT, NATIONAL INSURANCE | NIB contribution | Self-employed: business cost; employee share: social insurance |
| NIB C10 | Employer NIB payment | Employer liability |
| NIB SURCHARGE, NIB PENALTY, NIB INTEREST | NIB penalty | Not a business expense |
| NIB BENEFIT, SICKNESS, MATERNITY, RETIREMENT PENSION | Benefit received | Exclude from business income |
| BUSINESS LICENCE, BL RENEWAL | Business licence tax | Operating cost |
| BL PENALTY, LATE BL FEE | Penalty | Not deductible |
| DIR PAYMENT, INLAND REVENUE | Tax payment | Check reference: BL, VAT or RPT |
| VAT PAYMENT, VAT REFUND | VAT settlement | Exclude from income and expense |
| [Invoice] + 10% VAT, + 5% VAT | Sale | Revenue is the net amount |
| CLIENT PAYMENT, ZELLE, PAYPAL, STRIPE, WIRE IN | Business revenue | Confirm against invoices; counts as turnover |
| SALARY, PAYROLL, WAGES | Employment income | No income tax; NIB by employer |
| RENT RECEIVED | Rental income | No income tax; RPT on the property; counts in business turnover if the renting is a business |
| BANK INTEREST | Investment income | No income tax |
| GOVERNMENT GRANT | Check nature | Revenue grants count as turnover; capital grants do not |
| OFFICE RENT, PROFESSIONAL FEES, LEGAL, SUPPLIES, MARKETING, INSURANCE, HOSTING, SOFTWARE, BANK FEES, TRAINING | Business costs | Relevant to profit and VAT input, not to BL tax |
| RESTAURANT, ENTERTAINMENT, DRAWINGS, GROCERIES, FINES | Personal or penalty | Not business costs |
| INTERNAL TRANSFER, LOAN PRINCIPAL | Exclude | Not income or expense |
| "INCOME TAX", "PROVISIONAL TAX" | No such tax | Find out what it really is (VAT, BL or RPT) |
| STAMP DUTY, VAT ON CONVEYANCE | Property transaction cost | One-off, not operating |

### Banks and terms

| Bank | Statement format |
|---|---|
| Commonwealth Bank | PDF, online export |
| Bank of The Bahamas | PDF |
| Scotiabank Bahamas | PDF, CSV |
| CIBC FirstCaribbean | PDF |
| Fidelity Bank Bahamas | PDF, CSV |
| Wise, Revolut Business | CSV, multi-currency |

| Term | Meaning |
|---|---|
| C10 | NIB monthly employer contribution form |
| R1 | NIB self-employed or voluntary registration form |
| DIR | Department of Inland Revenue |
| BL | Business licence |
| RPT | Real property tax |
| BICA | Bahamas Institute of Chartered Accountants |
| BLAE, BLAA | Business Licence Annual Estimate and Annual Actual returns |

## Deadlines and filing

| Obligation | When | Source of the rule |
|---|---|---|
| Business licence renewal application | On or before 31 January of the year after trading | Business Licence Act 2023, s. 26(3)(a) |
| Prior year turnover return and unpaid tax | On or before 31 March | s. 26(3)(b) |
| Estimated tax for the current year | By 31 March in full, or four equal instalments on 31 March, 30 June, 30 September and 31 December if notified at renewal | ss. 26(3)(c), 35(4) to (6) |
| Cessation notice | Within 14 days, no later than 31 December | DIR penalties page |
| Real property tax | 31 March | DIR RPT FAQ |
| VAT returns | 21 days after each period | `bahamas-vat` |
| NIB contributions | By the 15th of the following month | NIB contributions page |

## Penalties and interest

| Item | Penalty | Source of the rule |
|---|---|---|
| Late licence renewal or return | BSD 100 | Business Licence Act 2023, Fourth Schedule (a) |
| Late notice of cessation | BSD 100 | Fourth Schedule (b) |
| Late payment of business licence tax | 10% of the tax liability | Fourth Schedule (c) |
| Business licence interest | 5% a year on payments 30 days or more late | Fourth Schedule (d) |
| BL instalments after 31 March | 5% a year interest | s. 35(4) as amended by the 2025 No. 2 Act |
| RPT | 5% surcharge on 1 January plus 5% interest | DIR RPT FAQ |
| VAT | Greater of BSD 100 or 2% (late return); 10% (late payment) | `bahamas-vat` |

## Cross-border points

- Non-residents and expatriates pay no Bahamian income tax either. Work permits, benefits in kind and any social security agreement can still matter: refer complex expatriate cases.
- A foreign person needs Bahamas Investment Authority approval to carry on business (DIR annual licence page) and pays 10% VAT on buying real property.
- The home country may tax a Bahamian resident's income; the absence of Bahamian tax gives no foreign tax credit.

### Refusal catalogue (kept)

- R-BS-1, asked for a personal income tax computation: "The Bahamas levies no personal income tax. There is no return to file and no income tax due. NIB, business licence tax and VAT may apply."
- R-BS-2, capital gains: "There is no capital gains tax. A property sale bears VAT on the conveyance; see `bahamas-vat`."
- R-BS-3, inheritance or gifts: "There is no inheritance, estate or gift tax. Probate and estate planning go to a Bahamian attorney." A gift of property between parents, children, grandparents and spouses can be zero rated for VAT on approval (DIR First home FAQs).
- R-BS-4, company tax: use `bs-corporate-income-tax`.
- R-BS-5, complex expatriate cases: refer to a Bahamian practitioner.
- R-BS-6, NIB arrears or enforcement: do not advise; refer to a Bahamian accountant.
- R-BS-7, VAT refund claims: see `bahamas-vat`; refer if under audit.

### Prohibitions (kept)

- Never compute or imply a personal income tax, or prepare an income tax return, for a Bahamian individual.
- Never treat NIB as income tax; they are separate systems with separate authorities.
- Never skip NIB and business licence registration for a new self-employed person.
- Never allow entertainment as a business cost without a reviewer.
- Never omit the Provisional VAT Invoice step on a property transaction.
- Never present these figures as final without a reviewer; label them estimated.
- Never apply a first-home VAT relief without confirming it is a dwelling, the buyer is a Bahamian first-time buyer and the value is within the limit.

## Two worked examples that recompute

### Self-employed web developer, BSD 30,000

James earns BSD 30,000 in 2026 (BSD 576.92 a week). Income tax: none. NIB at 10.30% on BSD 30,000 = BSD 3,090 (his weekly income is under the BSD 810 ceiling). Business licence tax: turnover is not over BSD 100,000, so exempt under s. 38(1)(i); he still renews the licence by 31 January. VAT: below BSD 100,000, no registration required.

```oa-check
name: BS self-employed 2026, income 30000
inputs:
  income: 30000
  nib_rate: 0.103
  bl_rate_exempt_band: 0
steps:
  - income_tax: 0
  - nib: income * nib_rate
  - nib_monthly: round(nib / 12, 2)
  - bl_tax: income * bl_rate_exempt_band
  - total_cost: income_tax + nib + bl_tax
expected:
  nib: 3090
  nib_monthly: 257.50
  bl_tax: 0
  total_cost: 3090
```

The previous version charged him BSD 100 of business licence tax: since 1 July 2024 businesses up to BSD 100,000 are exempt.

### Decision: pay the business licence tax in full or in instalments

Sandra's consultancy had turnover of BSD 180,000 in 2025, so her 2026 estimated tax is 0.5% × 180,000 = BSD 900. Her actual 2026 turnover is BSD 240,000, an actual tax of BSD 1,200, so BSD 300 of unpaid 2026 tax is due by 31 March 2027.

- **In full:** BSD 900 by 31 March 2026.
- **Instalments:** notify DIR at renewal; BSD 225 on each of 31 March, 30 June, 30 September and 31 December 2026, with 5% a year interest on amounts paid after 31 March. The cash spreads over the year; the total tax is the same.

```oa-check
name: BS business licence estimate vs actual, 2026
inputs:
  turnover_2025: 180000
  turnover_2026: 240000
  rate: 0.005
steps:
  - estimated_2026: turnover_2025 * rate
  - instalment: estimated_2026 / 4
  - actual_2026: turnover_2026 * rate
  - unpaid_due_2027: actual_2026 - estimated_2026
expected:
  estimated_2026: 900
  instalment: 225
  actual_2026: 1200
  unpaid_due_2027: 300
```

Both turnovers sit in the BSD 100,000 to 500,000 band. Turnover is under BSD 250,000, so no accountant's report is needed with the renewal; from BSD 250,000 one is.

### Working paper (compact)

```
BAHAMAS INDIVIDUAL, TAX YEAR 2026
A. Income tax: none, no return
B. NIB: status (employed / self-employed / voluntary); weekly earnings; insurable (capped at BSD 810 a week);
   rate 4.65% (employee) + 6.65% (employer) / 10.30% / 6.50%; annual = insurable x rate x 52
C. Business licence: prior year turnover; band rate; estimated tax; actual tax; unpaid or credit;
   renewal by 31 Jan; return and payment by 31 Mar or instalments; accountant's report if turnover >= 250k
D. VAT: registered? turnover vs BSD 100,000; period; output, input, net (see bahamas-vat)
E. RPT: class; assessed value; tax per band; cap; 10% discount if paid by 31 Mar
F. Property bought or sold: VAT on conveyance per Third Schedule; Provisional VAT Invoice obtained?
Reviewer flags: NIB registered and current; licence held before trading; first-home claim checked
```

## Ask the client first

1. Employee, self-employed, or both, and weekly or annual earnings.
2. NIB number, and are contributions up to date?
3. Business licence held? Prior year and current year turnover; is the business an IBC, family office or financial services entity (no BSD 100,000 exemption)?
4. VAT registered? Taxable turnover for the last and next 12 months.
5. Property owned: class (owner-occupied, rental, commercial, vacant), assessed value, Bahamian or foreign owner, age 65 or over?
6. Any property bought or sold in 2026, and was a Provisional VAT Invoice obtained?

## Sources

| Source | URL | Read on |
|---|---|---|
| NIB, contributions page (opened with Firecrawl, built by script): read for the BSD 810 weekly ceiling and the 15th day deadline | https://www.nib-bahamas.com/contributions | 2026-11-14 |
| Bahamas legislation, Acts by year 2026: read for the 2026 amending Acts (VAT, Business Licence, Real Property Tax, Stamp, DMTT) and to confirm no income tax Act | https://laws.bahamas.gov.bs/cms/legislation/acts_only/acts-by-year.html | 2026-11-14 |
| National Insurance (Contributions) (Amendment) Regulations 2024, S.I. 37 of 2024: read for the Fifth Schedule rates and the 1.5 point increase from 1 July 2024 | https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0037S/2024-0037S.pdf | 2026-11-14 |
| Business Licence Act 2023: read for ss. 26, 35, 36 and the Fourth Schedule late fees | https://inlandrevenue.finance.gov.bs/wp-content/uploads/2023/07/Business-Licence-Act-2023.pdf | 2026-11-14 |
| Business Licence (Amendment) Act 2024: read for the BSD 100,000 exemption, its exclusions and the new Second Schedule rates | https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/08/Business-Licence-Amendment-Act-2024.pdf | 2026-11-14 |
| Business Licence (Amendment) (No. 2) Act 2025: read for 5% interest on instalments after 31 March | https://inlandrevenue.finance.gov.bs/wp-content/uploads/2025/08/BUSINESS-LICENCE-AMENDMENT-NO.-2-ACT-2025.pdf | 2026-11-14 |
| Business Licence (Amendment) Act 2026: read for the 1.5% rate above BSD 175 million from 1 July 2026 | https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0022A/2026-0022A.pdf | 2026-11-14 |
| DIR, renewing a business licence: read for the turnover definition and the accountant's report thresholds | https://inlandrevenue.finance.gov.bs/business-licence/renewing-business-licence/ | 2026-11-14 |
| DIR, annual business licence: read for eligibility and the Bahamas Investment Authority approval for non-Bahamians | https://inlandrevenue.finance.gov.bs/business-licence/business-licenceannual-business-licence/ | 2026-11-14 |
| DIR, business licence fines and penalties: read for the cessation notice deadline | https://inlandrevenue.finance.gov.bs/business-licence/fees-fines-and-penalties-bl/ | 2026-11-14 |
| DIR, RPT FAQs: read for the property classes and rates, 31 March, 10% discount, surcharge, interest and pensioner discount | https://inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/ | 2026-11-14 |
| Real Property Tax (Amendment) Act 2026: read for the BSD 150,000 cap and the foreign owner-occupied class | https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0021A/2026-0021A.pdf | 2026-11-14 |
| VAT Act reprint 1 July 2024: read for the Third Schedule conveyance rates | https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf | 2026-11-14 |
| DIR VAT FAQs: read for the BSD 100,000 registration threshold | https://inlandrevenue.finance.gov.bs/value-added-tax/faqs/ | 2026-11-14 |
| DIR First home FAQs: read for inter vivos gifts zero rated for VAT | https://inlandrevenue.finance.gov.bs/faqs-first-home/ | 2026-11-14 |

Not yet confirmed: any NIB ceiling change from July 2026 (old file: BSD 830 a week; the NIB page read shows BSD 810 effective July 2024) and the monthly ceiling (old: BSD 3,510); NIB late surcharge and interest (old: 10% plus 1.5% a month compound) and the 10 working day R1 registration rule; NIB benefit amounts (old: minimum pension BSD 364, maternity grant BSD 570, funeral BSD 2,060); whether the 2024 wording "on the proportion of turnover" makes the business licence bands marginal rather than a rate on the whole turnover (this skill applies the band rate to the whole turnover, as the 2023 Act did); which RPT class the 2026 Act's repealed s. 3(2)(e) was, and whether the DIR FAQ rates for vacant land of foreigners (BSD 100 to BSD 7,000, then 2%) still apply; the first RPT bill year for the 2026 changes; stamp duty on mortgages and leases under the Stamp Act 2024 (its schedule did not extract cleanly); the BSD 6.50 an hour minimum wage.
