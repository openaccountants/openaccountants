---
name: bn-corporate-income-tax
description: "Brunei corporate income tax for year of assessment 2026 (preceding-year basis, so income of the accounting period ending in 2025). Covers the BND 1,000,000 turnover exemption, the 18.5% rate, the section 35(4) tax threshold for existing companies, the section 35(5) exemption for newly incorporated companies, allowable and disallowed deductions, capital allowances, tax credits, estimated chargeable income, the 30 June return, payment and late payment penalties, and withholding tax on payments to non-residents. Use for questions about company tax in Brunei Darussalam, Sdn Bhd tax, ECI, Revenue Division, OCP filing, Collector of Income Tax or Brunei withholding tax. Petroleum companies are out of scope."
version: 1.1
jurisdiction: BN
category: international
tax_year: 2026
tax_year_notes: "Year of assessment 2026, preceding-year basis: income of the basis period (accounting period) ending in 2025"
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Brunei Corporate Income Tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Companies incorporated or registered under the Companies Act (Chapter 39) or under any law in force elsewhere ("Sdn Bhd", "Bhd", "Pvt Ltd") on income that accrues in, is derived from or is received in Brunei Darussalam (Income Tax Act, Chapter 35, section 8(1), as described by the Revenue Division, Ministry of Finance and Economy).

Out of this skill:

- Sole proprietorships and partnerships registered as business names, and individuals: no income tax is levied on them (see [bn-income-tax](bn-income-tax.md)).
- Capital gains: not taxed.
- Companies engaged in the exploration and production of oil and gas: taxed at 55% under the Income Tax (Petroleum) Act (Chapter 119). Refer them (refusal R-BN-CIT-1 below).
- Employer retirement contributions (SPK, TAP, SCP): see [bn-payroll-social](bn-payroll-social.md).

**Tax year label.** Brunei assesses companies on a preceding-year basis. The year of assessment (YA) 2026 is charged on the income of the basis period ending in 2025 (the calendar year ending 31 December 2025 unless the company has notified a different financial year end). This skill gives the rules for YA 2026, the return due on 30 June 2026.

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Gross sales or turnover exemption, section 10(4)–(5) | Company income exempt if basis-period gross sales or turnover is no more than BND 1,000,000, including goods, services, interest, royalties and dividends. Applies from YA 2015. | YA 2026 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=30 |
| Corporate income tax rate | 18.5% of chargeable income, YA 2015 onward | YA 2026 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=69 |
| Tax threshold, existing company, first BND 100,000 of chargeable income | 25% of the applicable rate (effective 4.625%), section 35(4), YA 2011 onward | YA 2026 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=70 |
| Tax threshold, existing company, next BND 150,000 of chargeable income | 50% of the applicable rate (effective 9.25%), section 35(4) | YA 2026 | same |
| Chargeable income above BND 250,000 | Full applicable rate, 18.5% | YA 2026 | same |
| Qualifying company, first BND 100,000 of chargeable income | Exempt for the first 3 YAs, starting with the YA of the incorporation basis period. The company must be incorporated and registered in Brunei, resident there in each of those years and other than a company limited by guarantee, sections 35(5) and (7). | YA 2026 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=70 |
| Qualifying company, next BND 150,000 of chargeable income | 50% of the applicable rate (effective 9.25%) in those same 3 YAs | YA 2026 | same |
| Approved exports, section 8A | 1% final tax on gross proceeds of exports approved by the Minister. Treat all turnover as exports if local sales do not exceed 20% of total turnover. | YA 2026 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=25 |
| Motor vehicle cap, sections 11(1A) and 16(4)–(5) | Capital allowances use a BND 50,000 cost cap for cars carrying up to 7 passengers excluding the driver and weighing up to 3,000 kg unladen. For a motor car costing over BND 50,000, multiply otherwise deductible running expenses by BND 50,000 divided by cost. | YA 2026 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=49 |
| Plant and machinery, sections 16 and 16B(1) | Standard initial allowance 40% of qualifying cost and annual allowance 25% on reducing value for assets in use at the basis-period end. The Collector can allow a higher annual rate. Alternatively, claim 33⅓% of cost each year for 3 years under section 16B(1). | YA 2026 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=48 |
| Hotel buildings in operation before 1 January 2008 | Revenue Division guidance gives 4% per year for qualifying legacy expenditure. Check the unrelieved balance and the applicable acquisition and use rules. | YA 2026 | https://www.mof.gov.bn/div_revenue_typesoftaxes_incometax/ |
| Tax credit, new local employee, section 42AA | 50% of salary for up to the first 36 months of continued employment. The employee must be a citizen or permanent resident, have been unemployed for at least 1 year immediately before hiring, earn gross salary of up to BND 3,000 per month and have the required Employee Trust contributions paid. | YA 2026 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=80 |
| Tax credit, additional TAP contribution over the previous year | 10% | YA 2026 | same |
| Tax credit, training, section 42AB | 100% of gross salary paid during outside training by an approved, recognised or registered institution for a citizen or permanent resident earning up to BND 2,000 gross per month, with the required Employee Trust contributions paid. | YA 2026 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=81 |
| Tax credit, new plant and machinery, section 42B | The 15% credit applied to qualifying installations in a Brunei industrial undertaking from 1 January 2012 to 31 December 2017, with carry-forward for up to 2 YAs. The credit is unavailable for new YA 2026 expenditure. | Historical only | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=81 |
| Cap on tax credits, section 42C | 50% of tax payable in the YA. Exclude the foreign tax credit under section 42 from this cap. | YA 2026 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=82 |
| Commonwealth income tax relief, section 40 | For a Brunei resident, the lower of the Commonwealth rate and half the Brunei rate on the same income taxed in both places. Reciprocal relief must be available. Section 40(2) applies a separate calculation to non-residents. | YA 2026 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=75 |
| WHT, interest, commission, fee or other payment on a loan or indebtedness (s 9(4), 35(2)) | 2.5% (from 1 April 2017) | 2026 | https://www.mof.gov.bn/div_revenue_withholdingoftax_whtrate/ |
| WHT, royalties and lump sums for use of movable property (ss 9(5)(a) and 35(2A)(a)) | 10% | 2026 | same |
| WHT, use of or right to use scientific, technical, industrial or commercial knowledge (ss 9(5)(b) and 35(2A)(a)) | 10% | 2026 | same |
| WHT, assistance or services in applying such knowledge (ss 9(5)(ba) and 35(2A)(a)) | 10% (from 1 January 2016) | 2026 | same |
| WHT, management or assistance in management of a business (ss 9(5)(c), 35(2A)(b) and 37A) | 10% (from 1 April 2017) | 2026 | same |
| WHT, rent or other payments for use of movable property (ss 9(5)(d) and 35(2A)(a)) | 10% | 2026 | same |
| WHT, non-resident directors' remuneration (ss 35(2B) and 37B) | 10% (from 1 January 2016) | 2026 | same |
| WHT payment due | Within 14 days after the date of payment of the income (interest is deemed paid when reinvested, accumulated, capitalised or credited, s 37(7)(b)) | 2026 | https://www.mof.gov.bn/div_revenue_withholding-of-tax_wht/ |
| WHT late payment penalty, section 37(4) | 5% if unpaid within 14 days after payment to the payee. If unpaid within 30 days after payment to the payee, an additional 1% of the tax for each completed month unpaid, capped at 15% of the outstanding tax for the additional penalty. | 2026 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=73 |
| Estimated chargeable income (ECI), sections 52A and 69A | If the return has not been filed, file the estimate and pay the estimated tax within 3 months after the accounting period ends. | YA 2026 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=88 |
| Income tax return | Filed, and tax on it paid, by 30 June of the YA | YA 2026 | same |
| Additional assessment | Pay within 30 days after service of the Notice of Assessment, even if objected to (section 70) | YA 2026 | same |
| Late payment penalty, section 72(1)(a) and (ba) | 5% of unpaid tax. If the tax remains unpaid 60 days after imposition of the 5% penalty, an additional 1% of outstanding tax for each completed month of continued non-payment, capped at 12% of outstanding tax. | YA 2026 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=114 |
| Failure to file a return, section 78 | Failure without reasonable excuse is an offence. On conviction, BND 10,000 fine, with 12 months' imprisonment in default of payment. | YA 2026 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=119 |
| Record keeping (section 56A(1)(a)) | 7 years from the YA to which the income relates | YA 2026 | same |
| Objection | Written notice to the Collector within 30 days of service of the Notice of Assessment | YA 2026 | https://www.mof.gov.bn/div_revenue_typesoftaxes_incometax/ |

## The base

**Chargeable income** is the company's income for the basis period (trade or business profits, dividends, interest, discounts, rents, royalties, premiums and other profits from property, as listed in Part III of the Act) less allowable deductions and capital allowances.

1. **Dividends.** Dividends received from a corporation taxable in Brunei are excluded. Other dividends accruing in, derived from or received in Brunei are included. Dividends from the United Kingdom or Commonwealth countries are grossed up and credit claimed under the UK treaty or Commonwealth relief.
2. **Allowable deductions.** Expenses wholly and exclusively incurred in producing taxable income, including interest on borrowed money used to acquire income, rent on business premises, repairs of premises, plant and machinery, bad debts and specific doubtful debts (recoveries are income), employer contributions to approved pension or provident funds (TAP, SCP and their SPK successor), and zakat, fitrah or religious dues paid under a written law.
3. **Disallowed.** Expenses not wholly or exclusively for income, domestic or private expenses, capital withdrawn or used as capital, capital improvements (except replanting), sums recoverable under insurance or indemnity, rent or repairs not for earning income, income tax paid in Brunei or elsewhere, payments to unapproved funds. Donations are disallowed unless made to approved institutions.
4. **Depreciation** is not deductible. Capital allowances replace it. Section 16(2) sets the current standard plant and machinery annual rate. Balancing allowances or charges arise on disposal. Unabsorbed capital allowances carry forward indefinitely against income of the same trade.
5. **Losses.** Section 30(2) generally allows unused trading losses from the preceding 6 years to be deducted, using them in the earliest available year. Claim current-year losses in writing within 1 year after the YA ends. Check the remaining statutory period when a dormant company resumes business. For capital allowances, check whether the same trade continues under section 20.
6. **Tax.** Check the section 10(4) turnover exemption first. Where the ordinary rates apply, use section 35(4) or section 35(5) as appropriate, then 18.5% on the balance. Apply tax credits subject to section 42C.

### Conservative defaults

| Unknown | Default |
|---|---|
| Whether the company qualifies under section 35(7) and is in its first 3 YAs | Treat as an existing company (section 35(4)), which gives the higher tax |
| Whether a payee is resident | Treat as non-resident and withhold until a certificate of residence is produced |
| Nature of a cross-border payment | Ask; do not guess between 2.5% and 10% |
| Whether a donation recipient is approved | Disallow |

### Red flags

- Payments to foreign related parties for management, technical services or royalties with no withholding remitted.
- Interest credited to a non-resident lender's account without withholding (deemed payment rule).
- A car costing over BND 50,000 with full running costs claimed.
- A dormant company setting off brought-forward losses.

## Deadlines and filing

1. **Register.** Create an account in the One Common Portal (OCP), https://www.ocp.mofe.gov.bn, then use its income tax e-services. OCP replaced STARS for filing.
2. **ECI.** If the return has not already been filed, file the estimate and pay the estimated tax within 3 months after the end of the accounting period.
3. **Return.** By 30 June of the YA, file the Income Tax Return with the financial statements (audited unless the company qualifies for an exemption under Companies Act section 133B or 133C), the tax computation and supporting schedules (including the fixed asset breakdown for capital allowances), and pay any balance.
4. **Accounts not ready.** Write to the Collector giving the reasons, and submit draft financial accounts.
5. **Dormant company.** Still files, with the balance sheet, profit and loss account and a dormancy letter.
6. **Assessment.** Pay within 30 days after service of the Notice of Assessment even if objecting. File a written objection with precise grounds within 30 days after service, subject to an extension under section 65(2).
7. **Payment channels.** Internet banking with Baiduri, BIBD or Standard Chartered (payee "Revenue Division Tax Payment", Return ID as reference), cash or crossed cheque to "Government of Brunei Darussalam", or electronic transfer.
8. **Change of financial year end.** Email revenue@mof.gov.bn with the company circular.

## Penalties and interest

- Late payment of ECI or return tax triggers the 5% charge and, if the balance remains unpaid 60 days after the charge is imposed, the additional penalty above.
- Failure to file without reasonable excuse is an offence under section 78. The BND 10,000 fine applies on conviction, with 12 months' imprisonment in default of payment.
- Late withholding payment triggers the charges in section 37(4), with the 30-day clock measured from payment to the payee and the 15% cap applying to the additional charge.
- Under section 12(2), a deduction is disallowed if relevant documents or particulars required under section 55, 55A or 65(3) are missing after the specified or extended deadline.

## Cross-border points

- **Residence.** A company is non-resident if the control and management of its business is not exercised in Brunei Darussalam (Revenue Division withholding FAQ).
- **Withholding.** A payer withholds on covered Brunei-source payments to a person not known to be resident and on covered non-resident director remuneration. Check whether the income arises from a trade, business, profession or vocation carried on in Brunei or is effectively connected to the payee's Brunei permanent establishment before using the final gross withholding rates. Apply any treaty relief and remit through OCP within the applicable period. Refunds need a certificate of residence, the return, invoice, contract, proof of payment and an authorisation letter if a local branch claims.
- **Treaties.** Brunei has avoidance of double taxation agreements with the United Kingdom, Indonesia, China, Singapore, Vietnam, Oman, Bahrain, Japan, Pakistan, Malaysia, Laos, Hong Kong, Kuwait, the United Arab Emirates, Qatar, South Korea, Luxembourg, Cambodia and the Philippines (Revenue Division list). Treaty rates are not restated here: read the agreement. Brunei residents apply for a certificate of residence with the COR form.
- **Disputes.** Mutual agreement procedure under the relevant agreement, per the Revenue Division MAP guidelines.

## Two worked examples that recompute

**Example 1. Existing trading company, chargeable income BND 500,000, YA 2026.** Gross turnover exceeds BND 1,000,000. First BND 100,000 at 25% of 18.5% is BND 4,625. Next BND 150,000 at 50% of 18.5% is BND 13,875. The balance of BND 250,000 at 18.5% is BND 46,250. Tax is BND 64,750 (effective 12.95%). The company files on time and the full tax balance remains unpaid on 30 June. It is paid 45 days after the 5% late charge is imposed, so the penalty is BND 3,237.50.

```oa-check
name: Brunei existing company, CI BND 500,000, YA 2026, paid 45 days after the late charge
inputs:
  ci: 500000
  rate: 0.185
steps:
  - band1: min(ci, 100000) * 0.25 * rate
  - band2: clamp(ci - 100000, 0, 150000) * 0.5 * rate
  - band3: max(ci - 250000, 0) * rate
  - tax: band1 + band2 + band3
  - penalty: tax * 0.05
expected:
  tax: 64750.00
  penalty: 3237.50
```

**Example 2 (decision). Does the new-company exemption apply? Chargeable income BND 300,000.** A company with gross turnover over BND 1,000,000 incorporated and registered in Brunei in 2024, with its first basis period ending in 2024, is in its second YA. It is resident in Brunei in all 3 qualifying YAs and is not limited by guarantee: first BND 100,000 exempt, next BND 150,000 at 9.25% is BND 13,875, balance BND 50,000 at 18.5% is BND 9,250, tax BND 23,125. If it were an existing company the first band would cost BND 4,625, total BND 27,750. Check the qualifying-company conditions and whether YA 2026 falls within the first 3 YAs. In the same year it also pays a non-resident consultant BND 20,000 of Brunei-source management fees. Assume none is derived from an activity the payee carries on in Brunei or effectively connected to a Brunei permanent establishment, and no treaty reduction applies. Withholding is 10%, BND 2,000, payable within 14 days.

```oa-check
name: Brunei new company vs existing, CI BND 300,000, plus WHT on management fee
inputs:
  ci: 300000
  rate: 0.185
  mgmt_fee: 20000
steps:
  - band2: clamp(ci - 100000, 0, 150000) * 0.5 * rate
  - band3: max(ci - 250000, 0) * rate
  - tax_new: band2 + band3
  - tax_existing: min(ci, 100000) * 0.25 * rate + band2 + band3
  - saving: tax_existing - tax_new
  - wht: mgmt_fee * 0.10
expected:
  tax_new: 23125.00
  tax_existing: 27750.00
  saving: 4625.00
  wht: 2000.00
```

## Ask the client first

1. Is the client a company, or a sole proprietor or partnership outside the scope of this corporate tax guide?
2. When was the company incorporated or registered in Brunei, and what is its financial year end?
3. Is it in oil and gas exploration or production?
4. Does it pay interest, royalties, technical or management fees, rent for movable property or directors' fees to non-residents?
5. Does it export approved goods, and what share of turnover is local?
6. Does it qualify for the turnover exemption or claim a tax credit for eligible new local staff or training?

### Refusals

| Code | Trigger | Message |
|---|---|---|
| R-BN-CIT-1 | Oil and gas exploration or production | "Petroleum profits are taxed at 55% under the Income Tax (Petroleum) Act (Chapter 119). This skill does not compute them; refer to a specialist." |
| R-BN-CIT-2 | Investment Incentives Order 2001 pioneer or other incentive status | "Incentive reliefs depend on the certificate's terms. Refer to a reviewer with the certificate." |
| R-BN-CIT-3 | Treaty-reduced withholding claimed | "Read the agreement with the payee's country and get a certificate of residence before reducing withholding." |

## Sources

| Source | What was read | URL | Read on |
|---|---|---|---|
| Income Tax Act, Chapter 35, 2024 revised edition | Operative corporate rates, turnover exemption, allowances, credits, withholding and late-payment provisions | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf | 2026-11-22 |
| Income Tax Act (Amendment) Order, 2024, S 46/2024 | Amended returns and associated payment provisions | https://www.agc.gov.bn/wp-content/uploads/2026/07/S-46_2024_E-INCOME-TAX-ACT-AMENDMENT-ORDER-2024.pdf | 2026-11-22 |
| OCP Income Tax Form Guide | Filing documents and exemptions from financial-statement audit | https://ocp.mofe.gov.bn/downloads/taxFormGuides/OCP%20Income%20Tax%20Form%20Guide%20for%20YOA%202022%20onwards_v1.0.pdf | 2026-11-22 |
| Revenue Division, MOFE: Types of taxes, income tax | Read for the rate history to 18.5%, section 35(4) threshold, section 35(5) new-company exemption, export tax, ECI, return, assessment, deductions, capital allowances, motor vehicle cap, tax credits and objection | https://www.mof.gov.bn/div_revenue_typesoftaxes_incometax/ | 2026-11-14 |
| Revenue Division, rate table image on that page | Read for "Year of Assessment 2015 and Subsequent Years of Assessment 18.5%" | https://www.mof.gov.bn/wp-content/uploads/2025/10/it-rates-v1.jpg | 2026-11-14 |
| Revenue Division, FAQ corporate tax | Read for who is taxed, the 18.5% rate, 30 June return, section 78 fine, documents, dormant companies, records, payment and penalties | https://www.mof.gov.bn/div_revenue_faq_corporatetax/ | 2026-11-14 |
| Revenue Division, payment of tax | Read for ECI and return payment dates, the 5% and 1% to 12% penalties and payment channels | https://www.mof.gov.bn/div_revenue_paymentoftax/ | 2026-11-14 |
| Revenue Division, withholding tax rates (table image WHT_rates.jpg) | Read for each withholding rate and its section | https://www.mof.gov.bn/div_revenue_withholdingoftax_whtrate/ | 2026-11-14 |
| Revenue Division, withholding of tax administration | Read for the 14-day payment rule, deemed interest payment and section 37(4) penalties | https://www.mof.gov.bn/div_revenue_withholding-of-tax_wht/ | 2026-11-14 |
| Revenue Division, FAQ withholding tax | Read for the non-resident definition and refund documents | https://www.mof.gov.bn/div_revenue_faq_witholdingtax/ | 2026-11-14 |
| Revenue Division, avoidance of double taxation agreements | Read for the list of treaty partners and the certificate of residence | https://www.mof.gov.bn/div_revenue_internationaltaxation_adta/ | 2026-11-14 |
| Revenue Division, relevant Acts | Read for the list of income tax legislation | https://www.mof.gov.bn/div_revenue_taxresources_relevantacts/ | 2026-11-14 |

Not yet confirmed as at 22 November 2026: commencement and operative text of the Income Tax Act (Amendment) Order, 2026 (S 27/2026). [The Gazette index lists it as awaiting publication](https://www.agc.gov.bn/brulaw_gazette2026/). Confirm the treatment of SPK contributions before using the Employee Trust tax credits in sections 42A, 42AA and 42AB.
