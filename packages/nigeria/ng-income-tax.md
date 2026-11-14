---
name: ng-income-tax
description: >
  Use this Nigeria reference for personal income tax of self-employed
  individuals (sole proprietors, freelancers), kept apart by income year.
  Transition Guidelines, whose force is held, put income earned in 2025 under
  the repealed PITA (bands of 7% to 24%, consolidated relief and the 1% minimum
  tax) and income earned from January 2026 under the Nigeria Tax Act 2025 (0%
  on the first NGN 800,000, rent relief and no consolidated relief). Match
  requests about Nigeria income tax,
  PITA, FIRS, NRS, self-assessment Nigeria, progressive tax Nigeria, minimum
  tax Nigeria, consolidated relief, CRA Nigeria, TIN Nigeria, WHT Nigeria,
  income tax Lagos, income tax Abuja and state IRS. It also keeps a Nigerian
  bank-statement narration library. ng-personal-income-tax.md states that it
  is the canonical guide and calls this file deprecated; differences are
  flagged here. This Tier 2 draft supports source checking and reviewer
  questions; it does not authorise filing, payment or a tax position.
version: 2.3
jurisdiction: NG
tax_year: 2026
tax_year_notes: "Income earned in 2026 under the Nigeria Tax Act 2025, reported for the 2027 year of assessment, and, separately, income earned in 2025 under the repealed Personal Income Tax Act, reported for the 2026 year of assessment. Paragraph 10.1.1 of the General Transition Guidelines gives 2025 income to the repealed law. The 2 regimes are shown side by side and never blended."
last_updated: 2026-11-14
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: income-tax
type: computation
---

# NG Income Tax v2.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

This reference covers Nigerian personal income tax for a self-employed individual (sole proprietor or freelancer) who is resident in Nigeria, in naira (NGN), including one with investment, rental or employment income as well. Coverage label: income earned in 2026 (2027 year of assessment) and income earned in 2025 (2026 year of assessment), each under its own law.

| Income earned in | Law applied here | Year of assessment | Basis |
| --- | --- | --- | --- |
| January to December 2025 | Personal Income Tax Act, Cap P8 LFN 2004 (PITA), as amended, although repealed | 2026 | General Transition Guidelines para 10.1.1 (Direct Assessment): income earned for 2025 and due for filing in 2026 is taxed on the repealed laws |
| From January 2026 | Nigeria Tax Act 2025 (NTA), administered under the Nigeria Tax Administration Act 2025 (NTAA) | 2027 for income of 2026 | NTA commencement 1 January 2026; s 195(g) repeals PITA; s 198 saves earlier matters; Guidelines para 10.1.1 |

Both regimes report the income of the year before the year of assessment (PITA s 41(1)(a); NTAA s 13(2)(b); NTA s 22(1)). This guide follows para 10.1.1: which law applies turns on when the income was earned, not on when the return is filed. That split rests on the Guidelines, which say they are made under NTAA s 144 and NTA s 200. They were read from an unofficial copy and their legal force is on the 'Not yet confirmed' line. That force matters, because NTA s 22(1) read alone could measure the 2026 year of assessment on 2025 profits. The test of a period ending before 1 January 2026 is the rule for companies (Guidelines para 10.1.2), not the rule written for individuals. Paragraph 10.1.2(4), which lets a taxpayer file an earlier period under the Acts with written approval, sits under the companies heading and is held for individuals. An individual whose accounting year straddles 31 December 2025 is held: no income tax text read settles how that income is split, and para 10.2.2 on contracts spanning the 2 regimes sits under transaction taxes.

The NTA was printed in at least 2 copies. The National Assembly copy (Gazette No. 117 of 26 June 2025) is the one cited here, and section numbers are from it. The Nigeria Revenue Service (NRS) copy differs in places, including some section numbers. The Fourth Schedule bands, the rent relief in s 30 and the residence definitions were compared and match. No final version was located, so each NTA citation is subject to the 'Not yet confirmed' line.

### What this file is

This is a Tier 2 draft. No accountant has approved it. `ng-personal-income-tax.md` states that it is the canonical Nigerian personal income tax guide and that this file is deprecated for tax rules, to be loaded only for its bank-narration patterns. That relationship is unchanged here, but the primary text read for this version disagrees with that guide on the consolidated relief base, the minimum tax, capital allowance rates, the FCT authority and the 1 January residence date. Check each point against the law before relying on either file. `ng-payroll.md` owns employee payroll, `ng-wht.md` owns a payer's withholding duties and `ng-cgt.md` owns capital gains.

The Federal Inland Revenue Service (FIRS) in the older texts is the NRS in the 2025 Acts. Guidelines para 4 names the NRS, a State Internal Revenue Service, the FCT Internal Revenue Service and Joint Revenue Committees of Local Government Councils, and para 20 defines 'relevant tax authority' as the NRS, a State IRS, the FCT IRS or an LG Revenue Committee. The NRS (Establishment) Act 2025, the Joint Revenue Board (Establishment) Act 2025 and the older FIRS Establishment Act were not read.

### Stop and refer

| Code | Trigger | Action |
| --- | --- | --- |
| R-NG-1 | Non-resident earning Nigeria-source income | Stop. Different rules apply; see 'Cross-border points' |
| R-NG-2 | Residence unknown | Stop until resolved. Treatment differs |
| R-NG-3 | State of residence unknown | Stop until resolved. It decides the filing authority |
| R-NG-4 | Capital expenditure claimed as an expense | Reject. Use the capital allowance schedule (PITA s 21(b); NTA s 21(b)) |
| R-NG-5 | Old personal allowance, children's allowance or dependent relative allowance claimed | Stop. Replaced by the consolidated relief allowance through the PITA (Amendment) Act 2011, and neither applies to income earned from January 2026 |
| R-NG-6 | Petroleum profits tax | Escalate. Separate regime, not covered |

## Rates, bands and thresholds

On the Guidelines split this guide follows, the NTA bands apply only to income earned from January 2026, and the PITA bands only to income earned in 2025. Applying the PITA table to 2026 income taxes from the first naira instead of from NGN 800,000 and stops at 24% instead of 25%.

### Income earned from January 2026: NTA s 58 and Fourth Schedule

| Chargeable income (NGN) | Rate | Tax at top of band | Source |
| --- | --- | --- | --- |
| First 800,000 | 0% | 0 | NTA Fourth Schedule, Gazette No. 117 of 26 June 2025: https://nass.gov.ng/documents/download/11249 |
| Next 2,200,000 (to 3,000,000) | 15% | 330,000 | same |
| Next 9,000,000 (to 12,000,000) | 18% | 1,950,000 | same |
| Next 13,000,000 (to 25,000,000) | 21% | 4,680,000 | same |
| Next 25,000,000 (to 50,000,000) | 23% | 10,430,000 | same |
| Above 50,000,000 | 25% | | same |

Section 58 applies the Fourth Schedule to an individual 'other than an individual earning the Minimum Wage in line with the Minimum Wage Act'. NTA s 162(1)(t) separately exempts income from an employment where the person earns gross income of national minimum wage or less from that employment.

### Income earned in 2025: PITA s 37 and Sixth Schedule

| Chargeable income (NGN) | Rate | Tax at top of band | Source |
| --- | --- | --- | --- |
| First 300,000 | 7% | 21,000 | PITA Sixth Schedule para (3), read in the FIRS-hosted text (archived copy, annotated to the Finance Act 2020): https://web.archive.org/web/20250514045957/https://old.firs.gov.ng/wp-content/uploads/2021/07/Personal-Income-Tax-Act.pdf |
| Next 300,000 (to 600,000) | 11% | 54,000 | same |
| Next 500,000 (to 1,100,000) | 15% | 129,000 | same |
| Next 500,000 (to 1,600,000) | 19% | 224,000 | same |
| Next 1,600,000 (to 3,200,000) | 21% | 560,000 | same |
| Above 3,200,000 | 24% | | same |

### Reliefs and floors, income earned in 2025

| Item | Amount and condition | Source |
| --- | --- | --- |
| Consolidated relief allowance (CRA) | The higher of NGN 200,000 and 1% of gross income, plus 20% of gross income (s 33(1)). The Sixth Schedule para (1) states it as NGN 200,000 plus 20% and omits the 1% limb. 'Gross income' for s 33 is income from all sources less non-taxable income, income on which no further tax is payable, the Sixth Schedule para (2) items and all allowable business expenses and capital allowance (s 33(2)). It is not receipts before expenses | PITA ss 33(1), 33(2), Sixth Schedule paras (1), (2): https://web.archive.org/web/20250514045957/https://old.firs.gov.ng/wp-content/uploads/2021/07/Personal-Income-Tax-Act.pdf; Finance Act 2020 s 29: https://archive.gazettes.africa/archive/ng/2021/ng-government-gazette-dated-2021-01-04-no-4.pdf |
| Sixth Schedule para (2) items | National Housing Fund contribution, National Health Insurance Scheme, life assurance premium, National Pension Scheme, gratuities | same |
| Life premium | Annual premium paid in the preceding year to an insurance company on the individual's life or the spouse's life. Finance Act 2021 s 23 restated s 33(3) 'subject to section 17' and dropped the deferred annuity words | Finance Act 2021 s 23: https://budgetoffice.gov.ng/index.php/resources/internal-resources/budget-documents/finance-act-2021/download |
| Minimum tax | Where there is no chargeable income, or tax on chargeable income is less than 1% of total income, tax is charged at 1% of total income (s 37). The Sixth Schedule para (3) says 1% of 'Gross Income', and the s 33(2) definition is limited to s 33. The 2 wordings differ; see 'The base' | PITA s 37, Sixth Schedule para (3): https://web.archive.org/web/20250514045957/https://old.firs.gov.ng/wp-content/uploads/2021/07/Personal-Income-Tax-Act.pdf |
| Minimum wage carve-out | Minimum tax does not apply to a person earning the National Minimum Wage or less from an employment (s 37 proviso). Third Schedule para 33 exempts that employment income. Neither text extends to self-employment income | same |
| Early filing bonus | 1% of the tax payable, for a return filed in time with no default in the payment arrangement (s 45) | same |
| No-return limit | No return is filed by a person whose only income is employment of NGN 30,000 or less (s 43) | same |
| Rent paid on a home | No relief in the PITA text read. Rent is deductible only where occupied to acquire the income (s 20(1)(c), s 21(d)) | same |

### Reliefs, income earned from January 2026

| Item | Amount and condition | Source |
| --- | --- | --- |
| Consolidated relief allowance | None. NTA s 30 has no equivalent, although the Fourth Schedule preamble still speaks of 'the relief allowance and exemptions' granted under s 30(1) | NTA ss 28, 30: https://nass.gov.ng/documents/download/11249 |
| Rent relief | 20% of annual rent paid, capped at NGN 500,000, whichever is lower, provided the individual accurately declares the actual rent paid and other information the authority prescribes (s 30(2)(a)(vi)). The text says 'annual rent paid' and does not say the rent must be on a home; whether rent already deducted as a business expense also counts is held | same |
| Eligible deductions | Payments made by the individual in a year of assessment for the individual's National Housing Fund contributions, National Health Insurance Scheme contributions and Pension Reform Act contributions, interest on loans for developing an owner-occupied residential house, and any annuity or premium paid in the preceding year on the individual's or spouse's life or a deferred annuity on either's life (s 30(2)(a)(i) to (v)). Which year's payments count against income of 2026 is held; only limb (v) says the preceding year | same |
| Claim and proof | A deduction must be claimed in writing in the prescribed form (s 31). The authority may refuse it without adequate evidence (s 32) | same |
| Minimum tax for individuals | None found. A text search of the National Assembly copy finds no individual minimum tax in s 58, the Fourth Schedule or elsewhere. The NRS copy has a poor text layer, so the search does not cover it | same |

### Capital allowances

Rates for income earned in 2025 are 2 steps: an initial allowance on cost, then an annual allowance on what remains. Rates for income earned from January 2026 are one straight rate.

| Qualifying expenditure, income earned in 2025 | Initial (Table I) | Annual (Table II) | Source |
| --- | --- | --- | --- |
| Building | 5% | 10% | PITA Fifth Schedule paras 7, 8, Tables I, II: https://web.archive.org/web/20250514045957/https://old.firs.gov.ng/wp-content/uploads/2021/07/Personal-Income-Tax-Act.pdf |
| Industrial building | 15% | 10% | same |
| Mining | 20% | 10% | same |
| Plant, excluding furniture and fittings | 20% | 10% | same |
| Plant for manufacturing, construction and agricultural production | 25% | 10% (Table II has one plant row) | same |
| Furniture and fittings | 15% | 10% | same |
| Motor vehicle | 25% | 20% | same |
| Motor vehicle for public transportation with at least 3 buses | 30% | 20% (Table II has one motor vehicle row) | same |
| Plantation equipment | 20% | 33 1/3% | same |
| Housing estate | 20% | 10% | same |
| Ranching and plantation | 30% | 15% | same |
| Research and development | 25% | 12 1/2% | same |

The annual allowance is charged on expenditure after the initial allowance, and NGN 10 stays in the accounts until disposal (para 8(1)). Capital allowance deducted in a year cannot exceed 66 2/3% of assessable profits, except for an individual in the agro-allied industry or in manufacturing (para 27(7), (8)). The tables have no computer equipment row; whether a computer is plant is held.

| Class, income earned from January 2026 | Rate | Source |
| --- | --- | --- |
| Building, agricultural, mast, intangible assets and heavy transportation expenditure | 10% | NTA First Schedule Part I, para 6, Table I, applied to individuals by s 28(2)(b)(ii): https://nass.gov.ng/documents/download/11249 |
| Plant, agricultural equipment, furniture and fittings, mining and other equipment expenditure | 20% | same |
| Motor vehicle, software and other capital expenditure | 25% | same |

Table I sits in a Part headed for companies; s 28(2)(b)(ii) brings it to individuals and para 18 reaches professions. The 1% of cost in para 6(a) is a notional record that neither raises nor lowers the allowance. Para 23 carries assets already under allowance: the remaining years are the years under the Act less years already taken (para 23(1)), a single allowance clears the residue where the older years equal or exceed those years (para 23(2)), and where allowance was fully granted before commencement, the amount retained in the books under the repealed law gets no allowance (para 23(3)).

### Withholding on payments to a non-corporate recipient

Regulation 11 makes these rates effective from 1 January 2025, and regulation 12 revokes all earlier withholding regulations. Only rows this guide uses are shown; the rest of the First Schedule (corporate columns, and page B764 on directors' fees and other items) is left to `ng-wht.md`.

| Payment | Resident | Non-resident | Source |
| --- | --- | --- | --- |
| Commission, consultancy, technical, management and professional fees | 5% | 10% | Deduction of Tax at Source (Withholding) Regulations 2024, S.I. No. 34 of 2024, First Schedule (page image checked): https://archive.gazettes.africa/archive/ng/2024/ng-government-gazette-dated-2024-10-02-no-168.pdf |
| Supply or rendering of services not specifically listed | 2% | 5% | same |
| Supply of goods or materials other than by the manufacturer or producer | 2% | N/A | same |
| Construction of road, bridges, building and power plants | 2% | 5% | same |
| Any other form of construction and related activities | 5% | 10% | same |
| Dividend, interest | 10% | 10% | same |
| Royalty | 5% | 5% | same |
| Rent, hire or lease | 10% | 10% | same |

The deduction is twice the rate for non-passive income where the recipient has no Tax Identification Number (reg 3(c)). A body within the small company test need not deduct where the supplier has a valid TIN and the transaction is NGN 2,000,000 or less in the month (reg 4(2)). Regulation 10 lists exempt transactions, including telephone charges, internet data, airline tickets, insurance premiums, listed fuels and across-the-counter transactions; `ng-wht.md` owns the full list. These Regulations were made under the repealed Acts. Guidelines para 10.2.1 keeps goods delivered or services rendered up to 31 December 2025 under the repealed laws, whenever paid, and puts transactions from 1 January 2026 under the new Acts, except where payment was made in advance before commencement; para 10.2.2 splits a contract executed across that date. Whether these rates continue from January 2026 rests on NTA s 198(b) (subsidiary legislation continues unless inconsistent) and NTAA s 51 (regulation rates). No notice confirming this was read, so the rates are held for 2026.

The National Minimum Wage figure is held. NGN 70,000 a month was read only in the National Minimum Wage (Amendment) Bill 2024, not the Act, so no calculation here relies on it.

## The base

### Order of calculation, income earned in 2025

```
income_by_source   = receipts less s 20 expenses, source by source (s 23)
total_income       = total assessable income less losses (s 36(2)) less capital allowances (Fifth Schedule)
cra_base           = total_income less non-taxable income, income on which no further tax is payable and Sixth Schedule para (2) items not already deducted (s 33(2))
cra                = max(200,000, 1% x cra_base) + 20% x cra_base
chargeable_income  = max(cra_base - cra, 0)
tax                = Sixth Schedule bands on chargeable_income
floor              = 1% x total_income (s 37), unless the proviso applies
tax_payable        = max(tax, floor)
balance            = tax_payable - receipted tax deducted at source (s 73(4))
```

Pension is allowed as a s 20(1)(g) deduction, so the examples take it before total income. It is deducted once.

**Minimum tax base, held.** Section 37 says 1% of total income, which is after expenses, losses and capital allowances (s 36). The Sixth Schedule says 1% of 'Gross Income' without defining it there. If that were read as receipts, the floor would be far higher for a high-expense trader, so show both figures and leave the choice to a reviewer. This guide does not repeat the older claim that minimum tax cannot be reduced by expenses: s 37 does not say that. Example 3 shows the difference.

### Order of calculation, income earned from January 2026

```
assessable_profits = profits of the accounting period before the year of assessment (s 22(1))
taxable_income     = assessable_profits + employment income + investment income + other income + chargeable gains (s 28(2)(a))
total_income       = taxable_income - losses - capital allowance - exempt income - income taxed finally at source (s 28(2)(b))
chargeable_income  = max(total_income - eligible_deductions (s 30), 0)
tax                = Fourth Schedule bands on chargeable_income
balance            = tax - credits for tax deducted at source
```

The `max(..., 0)` is a display floor: a nil result gives no tax. No text read carries unused s 30 deductions forward.

### What is deductible

Income earned in 2025: s 20(1) allows outgoings wholly, exclusively, necessarily and reasonably incurred and ultimately borne by the individual in producing the income, and for a trade s 20(1)(h) allows expenses, or part of them, wholly and exclusively for it. Listed: interest on capital borrowed, interest on loans for developing an owner-occupied residential house, rent and premiums on land or buildings occupied to acquire the income, repairs (less any domestic part), bad and estimated doubtful debts on the conditions set, public-officer and social insurance contributions, contributions to a fund recognised under the Pension Reform Act, and research expenses. Section 21 refuses domestic or private expense, capital withdrawn and capital expenditure, loss or expense recoverable under insurance or indemnity, rent or repairs of premises not incurred to produce the income, taxes on income or profits (except as s 13 provides), pension payments outside s 20(1)(f) and (g), depreciation, reserves (except as s 21(h) allows), and expenses of earning management fees or management fees paid, except as the Minister approves or allows. A waived or refunded deduction becomes income (s 22). Where income is chargeable solely because it was brought into or received in Nigeria, s 20 gives no right to a deduction from the amount brought in or received (s 20(2)).

Income earned from January 2026: NTA s 20 allows expenses wholly and exclusively incurred, with no 'or part' words, so a business share of a mixed expense for 2026 is a working treatment and is held; its listed items (a) to (m) were read and are not repeated here. Section 21 refuses capital repaid or withdrawn, capital expenditure, domestic or private expense, recoverable sums, taxes on profit or income, unapproved retirement payments, depreciation and impairment, unrealised exchange differences, reserves, connected payments outside the Transfer Pricing Regulations, expenses of exempt income, expenses allowable against chargeable gains, penalties or fines, tax borne for another person, regulated securities lending compensating payments, and any expense on which VAT was due but not charged, or on imported items where the import duty or levy was not paid. Under s 20(4), an expense in another currency is deductible only to the extent of its naira equivalent at the official Central Bank of Nigeria rate for the date or period.

The s 21(p) limb matters for bookkeeping: an expense can fail because the supplier charged no VAT that was due.

### Basis periods, new trades, cessation and losses

| Point | Income earned in 2025 | Income earned from January 2026 |
| --- | --- | --- |
| Normal basis | Income of the year before the year of assessment (s 23(1)); accounts to another date on direction (s 23(2)) | Accounting period immediately before the year of assessment (s 22(1)) |
| New trade | First year: start to end of first accounting period. Second year: next day to end of second period. Third and later years: from the day after the period just ended (s 24, Finance Act 2020 s 27) | First year of assessment: start to end of first accounting period (s 22(2)). A change of accounting date is notified at least 30 days before the usual filing date (s 23) |
| Cessation | Beginning of the accounting period to cessation; tax payable within 3 months (s 25) | Same income measure; tax payable within 6 months (s 24(1)) |
| Losses | Trade loss of the year of assessment, if claimed in writing within 12 months after its end (s 36(2)(a)). An earlier trade loss is set against later income of the same trade, lapsing after 4 years. Agricultural trade: no time limit. Rental excess is treated as a trade loss (s 36(2), (3)) | Loss of the year or preceding year of assessment in a trade, and loss on disposing of a chargeable asset (s 28(3)(a), (b)). A loss is set as far as possible against assessable profit of a trade of the next year of assessment and later years until recouped; digital or virtual asset losses only against profit or gain from those assets (s 28(3)) |
| No reliable records | Turnover assessment (s 7); presumptive regime (s 36(6)) | Presumptive regime by regulation (s 29) |

### Credit for tax deducted at source

Tax deducted is an advance or final tax of the supplier, not a further tax (reg 5). It does not reduce income: include the gross fee. Tax so recovered is set off against the assessment (PITA s 73(4)). The law names the document: on remittance the payer issues a receipt and a statement in the Third Schedule format or as the authority prescribes, showing the name, address and TIN of the person deducted from (or, with no TIN, the National Identification Number of an individual or RC number of a company), nature of transaction, gross amount, amount deducted and month (reg 8(1)). The recipient may submit that receipt as evidence for the credit (reg 8(2)). If a receipt was issued and the money was not remitted, the recipient is still credited (reg 8(3)). A bank narration is not that evidence. Without a receipt, do not credit the amount; ask for it. For 2026, these documents carry over only if the Regulations do.

### Working rules

- **T1-NG-1.** For income earned in 2025, compute CRA on the s 33(2) gross income, which is after allowable business expenses and capital allowance. CRA on receipts overstates relief. CRA does not exist for income earned from January 2026.
- **T1-NG-2.** For income earned in 2025, compare computed tax with the s 37 floor and show the Sixth Schedule reading beside it. For income earned from January 2026, no individual minimum tax was found.
- **T1-NG-3.** Capital expenditure is never a direct expense. Use the Fifth Schedule (2025 income) or First Schedule Part I (2026 income).
- **T1-NG-4.** Tax deducted is a credit, not a reduction of income, and needs the receipt above.
- **T1-NG-5.** The filing authority depends on residence; see 'Deadlines and filing'. This is not optional.
- **T1-NG-6.** The personal, children's and dependent relative allowances are gone. The FIRS-hosted text annotates s 33(1) as substituted by the PITA (Amendment) Act 2011 s 5(a), so the change dates from then, not 2020. The Finance Act 2020 s 29 substituted s 33(2) and (3), and its s 30 added the s 37 proviso.

### Reviewer judgement items

| Code | Situation | Why | Treatment |
| --- | --- | --- | --- |
| T2-NG-1 | Mixed-use vehicle | Business proportion must be documented | Flag. Reviewer sets a reasonable business share. Private use fails s 21 in either regime |
| T2-NG-2 | Home office | Only premises used to produce income qualify | Flag. Document proportion and exclusivity. For 2026, whether the same rent can support both rent relief and a business deduction is held |
| T2-NG-3 | Capital allowance on complex assets | 2025: initial and annual allowance and residue. 2026: para 23 carry-over | Flag. Verify the asset register and schedule |
| T2-NG-4 | Operations in more than one State | First Schedule para 6 uses the place or principal place of residence on 1 January. Para 6(b) deems residence in any territory the earned income comes from: under PITA 'in any other case', under the NTAA where there was no place or principal place of residence. Para 8 orders the paragraphs | Flag. Verify the authority for each income source |
| T2-NG-5 | Foreign income of a resident | See 'Cross-border points' | Escalate. Treaty analysis required |
| T2-NG-6 | Voluntary NHF or NHIS contributions | The amount depends on actual payment and the statutory basis | Verify receipts and limits |

### Pension, housing fund and health contributions

Pension Reform Act 2014 (Act No. 4, gazetted 2 July 2014) s 4(1) sets minimums for employees: 10% by the employer and 8% by the employee of monthly emoluments, which s 120 defines as total emoluments under the contract of employment, not less than basic salary, housing allowance and transport allowance. Self-employed persons are entitled to participate under Commission guidelines (s 2(3)) and to make voluntary contributions (s 4(7)), so no 8% minimum was read for them. Later amendment of that Act was not checked. National Housing Fund Act s 4(1) sets 2.5% of basic monthly salary for a worker earning NGN 3,000 or more a year, and s 10 says all self-employed persons 'shall deduct' that amount from monthly income and remit within one month. So the LFN 2004 text does not call it voluntary for the self-employed; whether later law changed this was not checked. The National Health Insurance Authority Act was not read; the tax texts still say National Health Insurance Scheme.

### Bank narration library

These patterns are bookkeeping aids, not law. Each line is a first classification, subject to the deduction tests above and the document behind it. 'Receipt' means gross business income; where a platform deducts fees, gross up to the amount before fees.

| Code | Narration pattern | First classification | Note |
| --- | --- | --- | --- |
| I-01 | `TRANSFER FROM [client]` / `NIP CR [client]` | Receipt | Standard NIP (NIBSS Instant Payment) transfer from client |
| I-02 | `USSD CREDIT` / `*737 CREDIT` | Receipt | USSD banking credit from client |
| I-03 | `POS SETTLEMENT` / `CARD COLLECTION` | Receipt, gross up | POS terminal settlement |
| I-04 | `PAYSTACK PAYOUT` / `PAYSTACK SETTLEMENT` | Receipt, gross up | Paystack (Nigerian payment processor) payout |
| I-05 | `FLUTTERWAVE PAYOUT` / `FLUTTERWAVE SETTLEMENT` | Receipt, gross up | Flutterwave settlement |
| I-06 | `STRIPE PAYOUT NGN` | Receipt, gross up, or foreign | Stripe payout; classify by payer country |
| I-07 | `PAYPAL TRANSFER` / `PAYPAL WITHDRAWAL` | Receipt, foreign source likely | PayPal; flag for FX conversion |
| I-08 | `PAYONEER DEPOSIT` | Receipt, foreign source | Payoneer settlement |
| I-09 | `OPAY RECEIVED` / `PALMPAY RECEIVED` | Receipt | Mobile money or fintech receipt |
| I-10 | `TAX REFUND FIRS` / `REFUND SIRS` | Not income | Refund from a tax authority |
| I-11 | `INTEREST EARNED` / `SAVINGS INTEREST` | Investment income | Add to income; check whether deducted tax is final |
| I-12 | `RENTAL INCOME` / `RENT RECEIVED` | Rental income | Add to income |
| I-13 | `WHT DEDUCTED` (annotation on payment) | Credit, not a reduction of income | Credit against tax; require the receipt |
| E-01 | `OFFICE RENT` / `RENT PAYMENT [landlord]` | Rent, business premises | Require receipt or invoice. Rent not paid for the business is not this line: see rent relief for 2026, and nothing for 2025 |
| E-02 | `EKEDC` / `IKEDC` / `AEDC` / `BEDC` / `PHED` / `KAEDCO` | Electricity, business share | Distribution company payment |
| E-03 | `MTN` / `AIRTEL` / `GLO` / `9MOBILE` | Phone and internet, business share | Telecom provider |
| E-04 | `SPECTRANET` / `SMILE` / `IPNX` / `SWIFT NETWORK` | Internet, business share | ISP provider |
| E-05 | `ADOBE` / `MICROSOFT 365` / `GOOGLE WORKSPACE` | Software | Professional tools; a capital purchase goes to the schedule |
| E-06 | `ACCOUNTANT` / `AUDIT FEE` / `TAX CONSULTANT` | Professional fees | Check the business purpose |
| E-07 | `ARIK AIR` / `AIR PEACE` / `DANA AIR` / `IBOM AIR` | Air travel, business purpose | Document purpose |
| E-08 | `HOTEL` / `BOOKING.COM` / `AIRBNB` | Accommodation, business travel | Business purpose |
| E-09 | `PENSION CONTRIBUTION` / `RSA [fund name]` | Pension | Approved scheme contribution, not an ordinary expense |
| E-10 | `NHF` / `NATIONAL HOUSING FUND` | National Housing Fund | If applicable |
| E-11 | `LIFE INSURANCE` / `PREMIUM PAYMENT` | Life premium | Own or spouse's life; paid in the year before the year of assessment |
| E-12 | `NHIS` / `HEALTH INSURANCE` | Health insurance | The Scheme is named in the tax texts; private cover is not confirmed as qualifying |
| E-13 | `TAX PAYMENT FIRS` / `SIRS PAYMENT` | Tax payment, not deductible | PITA s 21(e), NTA s 21(e) |
| E-14 | `FUEL` / `PETROL` / `DIESEL` / `TOTAL` / `OANDO` / `CONOIL` | Fuel, business share | Document business use |
| E-15 | `OFFICE SUPPLIES` / `STATIONERY` | Supplies | Check the business purpose |
| E-16 | `MARKETING` / `GOOGLE ADS` / `META ADS` / `ADVERTISING` | Marketing | For 2026, check s 21(p) on VAT due and not charged |
| E-17 | `STAFF SALARY` / `PAYROLL` | Staff costs | PAYE obligations follow; see `ng-payroll.md` |
| E-18 | `TRAINING` / `COURSE` / `CERTIFICATION` | Training | Must meet the deduction test for the trade |
| E-19 | `GENERATOR FUEL` / `DIESEL GEN` | Generator fuel, business share | Common in Nigeria due to power supply |

Bank and channel fees: treat a fee as a business expense where it was incurred for the business and that use is documented, whatever label the bank gives the account (PITA s 20(1)(h); NTA s 20(1)). On an account used for both, deduct the business part for income of 2025 and refuse the private part (PITA ss 20(1), 21(a)); for income of 2026 the same split is held (NTA ss 20(1), 21(c)). Without evidence of business use, ask. Names to match: GTBANK, GUARANTY TRUST (now GTCo); ACCESS BANK (merged with Diamond Bank); ZENITH BANK; UBA, UNITED BANK FOR AFRICA; FIRST BANK, FBN; STANBIC IBTC; FCMB, FIRST CITY MONUMENT; FIDELITY BANK; STERLING BANK; WEMA BANK / ALAT; KUDA BANK, OPAY, PALMPAY, MONIEPOINT (fintech and digital banks). Fee lines to match: ACCOUNT MAINTENANCE FEE, COT (commission on turnover or maintenance); SMS ALERT FEE, NOTIFICATION FEE; TRANSFER FEE, NIP FEE.

| Pattern | Treatment | Note |
| --- | --- | --- |
| STAMP DUTY, STAMP DUTY CHARGE | Exclude for now; held | The NGN 50 charge on electronic receipts or transfers of NGN 10,000 or more is the Stamp Duties Act s 89A levy (Finance Act 2020 s 48) for 2025 and NTA Ninth Schedule item 48 for 2026, with exemptions in s 184 for sums below NGN 10,000, salary payments and intra-bank self-transfers. No text read says it is non-deductible: the refusals cover taxes on income or profits. Reviewer decides |
| FIRS, FEDERAL INLAND REVENUE; NRS | Exclude | Federal tax authority payment |
| LIRS, LAGOS STATE IRS | Exclude | State tax authority |
| CAC, CORPORATE AFFAIRS COMMISSION | Business expense, unless capital | Registration fee; a formation cost is held under s 21(b) |
| OWN ACCOUNT TRANSFER, SELF TRANSFER | Exclude | Internal movement |
| ATM WITHDRAWAL | Tier 2, ask | Default exclude; determine purpose |
| LOAN DISBURSEMENT | Exclude | Loan proceeds, not income |
| LOAN REPAYMENT | Exclude | Principal; interest may be a s 20 item |

### Reading bank statements

Formats below were carried from the earlier version and were not tested against live exports. Amounts are NGN with comma thousands and a period decimal (for example `2,500,000.00`). Consolidate every account: multiple accounts across banks is common.

| Bank | Export | Columns and narrations |
| --- | --- | --- |
| GTBank (Guaranty Trust / GTCo) | CSV or PDF from GTBank Internet Banking or GTWorld app | `Date;Description;Debit;Credit;Balance`. Date DD/MM/YYYY or DD-MMM-YYYY. Credits `NIP CR FROM [sender]`, `MOBILE TRANSFER FROM [sender]` |
| Access Bank | CSV or Excel from Access More app or Internet Banking | `Date;Narration;Debit;Credit;Balance`. Credits `NIP CREDIT FROM [sender]`, `TRANSFER FROM [sender]` |
| Zenith Bank | CSV from Zenith Internet Banking or ZMobile | `Trans Date;Value Date;Description;Debit;Credit;Balance`. Credits `NIP CR [sender]`, `INWARD TRF FROM [sender]` |
| UBA (United Bank for Africa) | CSV or PDF from UBA Internet Banking or UBA Mobile | Standard Nigerian bank format |
| First Bank of Nigeria (FBN) | CSV from FirstBank Online or FirstMobile | `Date;Description;Debit;Credit;Balance` |
| Stanbic IBTC | CSV from Stanbic IBTC Internet Banking | Standard format |
| Kuda Bank, OPay, PalmPay, Moniepoint | CSV or PDF from app | Simple format; credit and debit columns or a single column. `Transfer from [name]`, `Received from [name]`, `OPay Transfer from [name]`, `PalmPay Transfer from [name]`, `Moniepoint Transfer from [name]` |
| Paystack, Flutterwave | Appear in the main bank statement as `PAYSTACK SETTLEMENT` or `FLUTTERWAVE PAYOUT` | Gross up, because the platform deducts fees before settlement. Cross-check the merchant dashboard |

NIP (NIBSS Instant Payment) is the standard inter-bank transfer system. USSD banking (*737 for GTBank, *901 for Access, *966 for Zenith, and others) is common for mobile transfers. POS settlements may be delayed 1 to 3 days.

## Deadlines and filing

The dates below are kept apart by income year. Every date for 2025 income has already passed at 5 November 2026, so check what the relevant authority did before advising a late filer.

| Item | Income earned in 2025 (2026 year of assessment) | Income earned from January 2026 |
| --- | --- | --- |
| Return date | Within 90 days from the start of the year of assessment (PITA s 41(3)), which is 31 March 2026. The FCT Internal Revenue Service (FCT-IRS) extended individual returns from 31 March to 30 April 2026 by public notice dated 1 April 2026. For a State, check the authority's notices; no Lagos Internal Revenue Service (LIRS) notice was read | Held. NTAA s 13 requires a return each year of assessment without notice but states no date in the text read, and Guidelines para 19 leaves detailed deadlines to notices from the relevant tax authority. The FCT-IRS notice says the statutory deadline remains 31 March every year, and its home page says on or before 31 March; that is the authority's statement, not enacted text found in the NTAA. For income of 2026, confirm the date for the 2027 year of assessment with the authority |
| Who must file | Each taxable person, without notice or demand (s 41(1)); s 43 limits this for a person whose only income is employment of NGN 30,000 or less | Every taxable person, whether or not liable to tax (NTAA s 13(1)(a)), and non-residents liable under Chapter Two (s 13(1)(b)). A person with nil tax still files. Section 15 lets the authority issue simplified return guidelines for low-income and informal taxpayers |
| Payment | Self-assessment under s 44, then within 2 months of service of a notice of assessment (s 68(1)). Where 2 months ends before 14 December and at least half has been paid, the balance may be paid not later than that day (s 68(1)(a)). The authority may extend time (s 68(1)(b)). No text read requires payment with the return on 31 March, so the older claim of a 31 March payment date is held | On or before the due date of filing, in a lump sum or instalments (NTAA s 49(1)); within 30 days for an assessment (s 49(2)). The return carries evidence of payment (s 13(2)(e)) |
| Authority | The State where the individual is resident (PITA s 2(1)(a), s 41(1)). Text and practice differ for the FCT: PITA s 2(1)(b)(iii) names the Federal Inland Revenue Service for every resident of the FCT, yet the FCT-IRS collected and extended 2026 returns on its own site. Held; confirm with the FCT-IRS | The relevant tax authority in a State or the FCT for resident individuals (NTAA s 3(2)). The NRS exclusively for armed forces and police other than civilians, Foreign Service officers and non-residents with Nigerian income (s 3(1)(a)) |
| Residence date | 1 January of the year of assessment: 1 January 2026 for income of 2025 (PITA First Schedule para 6). If the source is first acquired in the year and there was no place of residence on that day, the territory where a place of residence is first established (para 6(a)) | 1 January of the year of assessment: 1 January 2027 for income of 2026 (NTAA First Schedule para 6). If the source is first acquired in the year and there was no place or principal place of residence on that day, the territory where a place of residence is first established (para 6(a)) |
| Form | 'Prescribed' form, not named in the text read. `ng-return-assembly.md` calls it PIT Form A; that name is unconfirmed. The return was due after commencement, so Guidelines para 6(2) points to forms under the Acts, and para 6(3) keeps existing forms valid pending new ones | Self-assessment form (NTAA s 13(2)(a)); existing forms stay valid pending new ones (Guidelines para 6(3)) |
| Return content | Income from every source for the preceding year and the particulars the return requires on income, allowance, relief or deduction (s 41(1)), with a declaration (s 41(2)) | (a) self-assessment form, (b) income of every source for the preceding year, (c) personal relief and tax computation, (d) for a trade, an audited statement or a statement of accounts attested by the taxpayer, (e) evidence of payment (s 13(2)) |
| Tax number | TIN needed for a business bank account (s 49(1), Finance Act 2019) | Tax ID (NTAA ss 4, 7) |
| Records | Books adequate for tax (s 52). Guidelines para 9(1) keeps records under the old laws for their statutory periods, but no period was found in the sections read, so the older 6 years is held for this period | 6 years after the year of assessment, in English (NTAA s 31). The older claim that WHT certificates are kept permanently has no basis in the text read |
| Records to keep | Business records, invoices, receipts, bank statements and contracts, as a working list; the sections read state a general duty, not this list | The same working list. Books must hold sufficient information on all relevant transactions (NTAA s 31(2)) |

### Portals

| Who | Portal | Status |
| --- | --- | --- |
| Lagos residents | LIRS eTax: https://etax.lirs.net/login | Linked from https://lirs.gov.ng/ |
| FCT residents | FCT-IRS TaxPorta: https://taxporta.fctirs.gov.ng/login | Linked from https://fctirs.gov.ng/. The FCT-IRS notice calls electronic filing through its portal the approved method |
| Other States | Each State Internal Revenue Service (for example Rivers and Kano in the examples) | Check the State's site. Not read |
| Persons under NTAA s 3(1)(a) | NRS Rev360, https://selfservice.nrs.gov.ng; older TaxPro Max, taxpromax.firs.gov.ng | Not confirmed from the NRS, whose home page could not be read: see 'Not yet confirmed'. Checked that the self-service address answers, nothing more |

The portal fields, box labels and upload rules were not read for any portal, because they sit behind a login, so this guide names no box numbers.

### What happens after filing

Income earned in 2025: the authority may accept the return, refuse it and assess to best judgement (s 54) or raise an additional assessment within 6 years, or at any time for fraud, wilful default or neglect (s 55). Income earned from January 2026: a self-assessment is treated as the assessment (NTAA s 34(2)), and the authority may accept it, accept it and raise an additional assessment, or reject it and assess to best judgement (s 34(4)). An objection is due within 30 days of service (PITA s 58, NTAA s 41(2)(a)); Guidelines para 7(2) applies the procedure under the Acts to any objection raised after 1 January 2026, whatever the year in dispute. An overpayment is refunded or set off: under PITA s 73(4), an excess from compliance with ss 69 to 72 is refunded within 90 days, unless it is a final tax, with an option to set off against future tax; under NTAA s 55, after audit, within 90 days of the decision, with a set-off option and a 6-year claim period.

Remitting WHT is the payer's duty: to the NRS by the 21st, and to a State by the 10th for capital gains tax and PAYE or the 30th for others (reg 7(1)). NTAA s 107 uses the 21st. Reg 4(1)(a) excludes an individual; whether a sole proprietor's business falls under reg 4(1)(e) as an 'enterprise' is held. See `ng-wht.md`.

The Guidelines (para 17(3)) give the Joint Revenue Board a role in harmonised administration; the Joint Tax Board of the older texts (www.jtb.gov.ng) and www.firs.gov.ng were not read for this version.

### Working paper

Working paper only. Every worked result goes to a reviewer. Complete one sheet per income year; never carry a line from one regime into the other.

```
NIGERIAN PERSONAL INCOME TAX WORKING PAPER (SELF-EMPLOYED / SOLE PROPRIETOR)
Taxpayer: _______________  TIN or Tax ID: _______________
Income year: [ ] 2025 (PITA, 2026 year of assessment)  [ ] 2026 (NTA, 2027 year of assessment)
State or FCT on 1 January of the year of assessment: _______________
Relevant tax authority: _______________  Portal: _______________

SECTION A: BUSINESS RECEIPTS
Business receipts:                          ___________
Platform payouts (grossed up):              ___________
Other business income:                      ___________
TOTAL BUSINESS RECEIPTS                     ___________

SECTION B: ALLOWABLE BUSINESS DEDUCTIONS
Office rent:                                ___________
Utilities (business share):                 ___________
Telecom (business share):                   ___________
Software:                                   ___________
Professional fees:                          ___________
Travel (business purpose):                  ___________
Marketing:                                  ___________
Staff salaries:                             ___________
Office supplies:                            ___________
Generator fuel (business share):            ___________
Other deductible:                           ___________
Pension (2025 income only: s 20(1)(g)):     ___________
TOTAL DEDUCTIONS                            ___________

SECTION C: BUSINESS PROFIT
Receipts less deductions:                   ___________

SECTION D: OTHER INCOME
Investment income:                          ___________
Rental income:                              ___________
Employment income:                          ___________
Capital allowances:                         (__________)
Losses:                                     (__________)
TOTAL INCOME                                ___________

SECTION E: RELIEFS, 2025 INCOME ONLY
Other Sixth Schedule para (2) items:        ___________
Gross income under s 33(2):                 ___________
CRA: max(200,000, 1% x s 33(2) gross income) + 20% x s 33(2) gross income  ___________

SECTION F: ELIGIBLE DEDUCTIONS, 2026 INCOME ONLY
NHF:                                        ___________
NHIS:                                       ___________
Pension:                                    ___________
Interest on owner-occupied house loan:      ___________
Life premium or deferred annuity:           ___________
Rent relief: min(20% x annual rent paid, 500,000)  ___________

SECTION G: TAX COMPUTATION
Chargeable income (not below zero):         ___________
Tax at the bands for the regime:            ___________
2025 only, s 37 floor (1% x total income):  ___________
2025 only, Sixth Schedule reading shown for the reviewer: ___________
TAX PAYABLE                                 ___________

SECTION H: CREDITS
Tax deducted, with receipts and statements: (__________)
TAX DUE / (REFUND)                          ___________

SECTION I: REVIEWER FLAGS
[ ] Residence confirmed (resident)?
[ ] Relevant tax authority confirmed?
[ ] Income year matched to its law?
[ ] 2025 only: CRA computed on s 33(2) gross income, after expenses?
[ ] 2025 only: minimum tax compared with computed tax, both readings shown?
[ ] Capital expenditure on the capital allowance schedule, not deducted directly?
[ ] WHT receipts and statements held for all credits?
[ ] Old personal allowance system NOT applied?
[ ] Generator and fuel expenses documented for the business share?
[ ] Multiple income sources properly aggregated?
```

## Penalties and interest

Which column governs a late return for 2025 income is held. Guidelines para 2 applies the Guidelines to returns due from 1 January 2026, but paras 5(2), 5(3) and 10(2) keep penalties under the Acts away from periods before commencement. The return is for a pre-commencement income year, was due after commencement, and the earlier version of this guide applied the NTAA to any failure from 1 January 2026. Show both and let a reviewer decide.

| Failure | Under PITA, for income earned in 2025 | Under NTAA, for income earned from January 2026 |
| --- | --- | --- |
| Failing to register | No separate provision found in the sections read | NGN 50,000 in the first month and NGN 25,000 each month the failure continues (s 100(1)) |
| Failing to file | On conviction, fine of NGN 20,000 plus NGN 2,000 for each day the failure continues, with 6 months' imprisonment in default, the daily sum starting from the day after conviction or a later day the court orders (s 94(1), Finance Act 2021 s 26). For a failure to meet a s 41 notice on non-employment income, the authority may instead impose a penalty equal to the income tax for the preceding year of assessment, by written notice, recoverable 30 days after service and open to remission (s 94(4)) | NGN 100,000 in the first month and NGN 50,000 each month the failure continues (s 101) |
| Late payment | 10% per annum of the tax added (s 76(1)); demand note, then enforcement after one month (s 76(2)); failure without lawful excuse is an offence (s 76(4)); the authority may remit the penalty for good cause (s 79). Interest at bank base lending rate from when the tax was payable (s 77) | 10% of the tax plus interest at the Monetary Policy Rate plus a spread for naira, or the Secured Overnight Financing Rate plus a spread for foreign currency (s 65(1)); demand with 30 days to pay (s 65(2)); remission (s 66) |
| Books and records | On conviction, NGN 50,000 for an individual outside salary employment and NGN 500,000 for a corporate entity, and the authority may direct what to keep (s 52) | NGN 10,000 for a person other than a company and NGN 50,000 for a company (s 102) |
| Incorrect return, no reasonable excuse | On conviction, a fine of 'N20,000 of the correct tax and double the amount of tax which has been undercharged' (s 95(1), read as printed); complaint within the year of assessment or 6 years after it (s 95(2)); may be compounded (s 95(3)) | Knowingly filing an incomplete or inaccurate return: the s 101 amounts |
| False statement or return | On conviction, NGN 50,000 for an individual and NGN 500,000 for a corporate body or up to 6 months' imprisonment; where the offence concerns the person's own tax for the year, NGN 10,000 or treble the tax chargeable, whichever is greater, is substituted for the fine (s 96(1)) | Administrative penalty of NGN 1,000,000 plus the tax undercharged, or on conviction a fine of NGN 1,000,000 or up to 3 years' imprisonment or both, plus the tax (s 124) |
| Other contravention | The s 94(1) fine | Administrative penalty of NGN 1,000,000, or on conviction up to 3 years' imprisonment or a fine or both (s 127) |
| Payer failing to deduct or remit | Failing to deduct, or to remit within 30 days: a penalty of 10% of the tax, plus the tax, plus interest at the Monetary Policy Rate (s 74(1)) | Failing to deduct: 40% (s 105). Failing to remit by the 21st: an administrative penalty of 10% per annum, among the consequences in s 107, which `ng-wht.md` owns |

The NGN 50,000 and NGN 25,000 monthly figures carried in the earlier version as the 'before 2026' filing penalty are in the NTAA for failing to register. They were not found in PITA.

## Cross-border points

**Residence, income earned from January 2026.** NTA s 201 makes an individual resident if any one limb is met: (a) domiciled in Nigeria, (b) a permanent place available for domestic use in Nigeria, (c) place of habitual abode in Nigeria, (d) substantial economic and immediate family ties in Nigeria, (e) sojourns in Nigeria aggregating not less than 183 days in a 12-month period, including annual leave or temporary absence, or (f) serving as a diplomat or diplomatic agent of Nigeria in another country. A 'non-resident individual' is one who meets none of those limbs, read cumulatively. Do not reduce this to a 183-day test: a person abroad for most of the year can still be resident under limbs (a) to (d).

**Residence, income earned in 2025.** A text search of the FIRS-hosted PITA found no 183-day individual residence test. PITA uses 'place of residence' and 'principal place of residence' to place an individual in a territory (First Schedule paras 6, 7, 8) and s 2(1)(b)(iv) for a person resident outside Nigeria. Whether a person is non-resident under PITA is held where the facts are not plain.

**Foreign income of a resident, income earned in 2025.** Income from a source inside or outside Nigeria is in scope (s 3(1)), and foreign income is the amount brought into or received in Nigeria (s 13). If the income arose in a country to which s 39 applies, that is where a s 38 arrangement allows the foreign tax as a credit (s 39(1)), s 13 takes the amount computed under s 39(5): no deduction for foreign tax, and an amount received is increased by the appropriate amount of the foreign tax. Section 39(6) allows a deduction for foreign tax above the credit. Income chargeable solely because it was brought in or received gets no s 20 deduction (s 20(2)); which foreign income that covers is held. Third Schedule para 30 exempts dividend, interest, rent, royalties, fee or commission earned from abroad and brought into Nigeria by a Nigerian resident in convertible currency paid into a domiciliary account in a bank approved by the Government. Para 28 covers domiciliary interest, para 29 temporary guests and professionals, and para 31 certain receipts of an author, sportsman, playwright, musician or artist. Whether services performed from Nigeria for a foreign client are 'earned from abroad' is held. Double taxation relief: ss 11, 38, 39.

**Foreign income of a resident, income earned from January 2026.** NTA s 12 charges a resident individual on income, gains or profits wherever they arise, whether or not brought into or received in Nigeria, so the PITA s 13 amount-brought-in rule of 2025 does not continue. NTA s 162(1)(s) exempts dividend, interest, rent or royalty from outside Nigeria brought through approved channels. Fees and commission are not in that paragraph, so do not assume the 2025 exemption for them continues. Unilateral relief is the lower of the Nigerian tax on that income (foreign income over total income, times tax) and the foreign tax paid (s 119). Treaties: ss 120, 121.

**Non-resident, income earned in 2025.** The NRS's predecessor collected (s 2(1)(b)(iv)). Tax deducted is final for a non-resident without a taxable presence (reg 6(3)), at the non-resident column above. Services under a significant economic presence are in s 6A. Rent, interest and royalty: ss 69, 70.

**Non-resident, income earned from January 2026.** NRS (NTAA s 3(1)(a)), return duty s 13(1)(b), final deduction on the items in s 51(2): dividend, interest, rent, royalty, directors' fee, entertainers and sportspersons. NTA s 17(4) makes the amount deducted final unless the person has a permanent establishment or significant economic presence; s 17(8) sets a floor of the tax withheld at source and, where the income is not liable to a deduction, 4% of the total income from Nigeria; s 17(9) deals with the taxable presence.

**PayPal and Payoneer.** Record the receipt in naira. NTA s 20(4) fixes the rate only for expenses, so the rate for foreign receipts is held for both years.

**Several States.** Itinerant workers: PITA s 2(3), s 108. See T2-NG-4.

## Two worked examples that recompute

Coverage label: Examples 2 and 6B are income earned in 2026 under the NTA. The rest are income earned in 2025 under PITA. All figures are illustrations. Tax bands are in the `tax` step of each block.

Example 1 and Example 2 are the decision pair: the same client, one with each law. Examples 3 to 7 test the other points the earlier version raised.

### Example 1: GTBank, Lagos IT consultant, income earned in 2025

Chidi Okafor, IT consultant, Lagos. Sample lines from his GTBank statement:

```
Date;Description;Debit;Credit;Balance
05/01/2025;NIP CR FROM TECH CORP LTD;;2,500,000;
15/01/2025;ACCOUNT MAINTENANCE FEE;1,500;;
10/02/2025;NIP CR FROM STARTUP DIGITAL;;1,800,000;
28/02/2025;PENSION RSA CONTRIBUTION;120,000;;
15/03/2025;PAYSTACK SETTLEMENT;;980,000;
01/04/2025;MTN AIRTIME/DATA;25,000;;
20/04/2025;NIP CR FROM GAMMA SOLUTIONS;;3,200,000;
10/07/2025;ACCOUNTANT FEES;150,000;;
10/10/2025;AIR PEACE LAGOS-ABUJA;85,000;;
15/11/2025;WHT DEDUCTED BY TECH CORP;250,000;;
```

These lines are a sample and do not add up to the annual totals. The `WHT DEDUCTED` line is an annotation: a bank narration is not a receipt. Annual assumptions: gross fees NGN 8,000,000 (the sample credits add to NGN 8,480,000, so the figure needs a reconciliation in practice); expenses NGN 3,000,000 (accounting 150,000, travel 85,000, telecom 300,000, software 240,000, marketing 180,000, office rent 1,200,000, generator fuel 360,000, other 485,000); pension NGN 120,000; receipted WHT NGN 400,000, being 5% under the 2024 Regulations (the earlier version used 500,000).

```oa-check
name: NG income earned in 2025, PITA, Lagos consultant
inputs:
  receipts: 8000000
  expenses: 3000000
  pension: 120000
  wht_receipted: 400000
steps:
  - cra_base: receipts - expenses - pension
  - cra: max(200000, pct(cra_base, 1)) + pct(cra_base, 20)
  - ci: max(cra_base - cra, 0)
  - tax: pct(min(ci, 300000), 7) + pct(clamp(ci - 300000, 0, 300000), 11) + pct(clamp(ci - 600000, 0, 500000), 15) + pct(clamp(ci - 1100000, 0, 500000), 19) + pct(clamp(ci - 1600000, 0, 1600000), 21) + pct(max(ci - 3200000, 0), 24)
  - floor_s37: pct(cra_base, 1)
  - tax_payable: max(tax, floor_s37)
  - due: tax_payable - wht_receipted
  - bonus_if_filed_on_time: pct(tax_payable, 1)
expected:
  cra_base: 4880000
  cra: 1176000
  ci: 3704000
  tax: 680960
  floor_s37: 48800
  tax_payable: 680960
  due: 280960
  bonus_if_filed_on_time: 6809.60
```

The tax is above both the s 37 floor and the 1% of receipts reading (NGN 80,000), so the minimum tax decision does not change the result. CRA on receipts, as in the earlier version, gave NGN 534,800, which understates tax by NGN 146,160. Filing authority: LIRS. Bonus is shown as a possible item only; s 45 needs filing in time and no default in the payment arrangement.

### Example 2: the same client, income earned in 2026, and the rent decision

Same figures, but the income is earned in 2026 and he pays NGN 1,800,000 rent on his home. The office rent stays in expenses under s 20. Pension moves from expenses to an eligible deduction under s 30. No CRA and no s 37 floor.

```oa-check
name: NG income earned in 2026, NTA, home rent below the cap
inputs:
  receipts: 8000000
  expenses: 3000000
  pension: 120000
  rent_paid: 1800000
  wht_receipted: 400000
steps:
  - total_income: receipts - expenses
  - rent_relief: min(pct(rent_paid, 20), 500000)
  - ci: max(total_income - pension - rent_relief, 0)
  - tax: pct(clamp(ci - 800000, 0, 2200000), 15) + pct(clamp(ci - 3000000, 0, 9000000), 18) + pct(clamp(ci - 12000000, 0, 13000000), 21) + pct(clamp(ci - 25000000, 0, 25000000), 23) + pct(max(ci - 50000000, 0), 25)
  - due: tax - wht_receipted
expected:
  total_income: 5000000
  rent_relief: 360000
  ci: 4520000
  tax: 603600
  due: 203600
```

```oa-check
name: NG income earned in 2026, NTA, home rent above the cap
inputs:
  receipts: 8000000
  expenses: 3000000
  pension: 120000
  rent_paid: 3000000
steps:
  - total_income: receipts - expenses
  - rent_relief: min(pct(rent_paid, 20), 500000)
  - ci: max(total_income - pension - rent_relief, 0)
  - tax: pct(clamp(ci - 800000, 0, 2200000), 15) + pct(clamp(ci - 3000000, 0, 9000000), 18) + pct(clamp(ci - 12000000, 0, 13000000), 21) + pct(clamp(ci - 25000000, 0, 25000000), 23) + pct(max(ci - 50000000, 0), 25)
expected:
  rent_relief: 500000
  ci: 4380000
  tax: 578400
```

The decision: which law, and which rent. For the same income, the 2025 law gives NGN 680,960 and the 2026 law NGN 603,600 at NGN 1,800,000 of home rent. At NGN 3,000,000 of rent, 20% would be NGN 600,000, so the NGN 500,000 cap sets the relief. The relief needs an accurate declaration of the rent actually paid. The example assumes rent and pension paid in 2026 count against income of 2026, which is held. Whether rent already deducted as a business expense can also count towards s 30 is held, so this example keeps the 2 rents separate. For 2025 the home rent gives nothing. WHT in 2026 assumes the 2024 Regulations continue, which is held.

### Example 3: UBA, Lagos consultant, minimum tax decision, income earned in 2025

Tunde Adeyemi, consultant, Lagos. Gross NGN 10,000,000, expenses NGN 9,000,000, pension NGN 500,000.

```oa-check
name: NG income earned in 2025, PITA, high expenses with pension
inputs:
  receipts: 10000000
  expenses: 9000000
  pension: 500000
steps:
  - cra_base: receipts - expenses - pension
  - cra: max(200000, pct(cra_base, 1)) + pct(cra_base, 20)
  - ci: max(cra_base - cra, 0)
  - tax: pct(min(ci, 300000), 7) + pct(clamp(ci - 300000, 0, 300000), 11) + pct(clamp(ci - 600000, 0, 500000), 15) + pct(clamp(ci - 1100000, 0, 500000), 19) + pct(clamp(ci - 1600000, 0, 1600000), 21) + pct(max(ci - 3200000, 0), 24)
  - floor_s37: pct(cra_base, 1)
  - tax_payable_s37: max(tax, floor_s37)
  - tax_on_receipts_reading: max(tax, pct(receipts, 1))
expected:
  cra_base: 500000
  cra: 300000
  ci: 200000
  tax: 14000
  floor_s37: 5000
  tax_payable_s37: 14000
  tax_on_receipts_reading: 100000
```

Variant: expenses NGN 9,800,000 and no pension.

```oa-check
name: NG income earned in 2025, PITA, nil chargeable income
inputs:
  receipts: 10000000
  expenses: 9800000
steps:
  - cra_base: receipts - expenses
  - cra: max(200000, pct(cra_base, 1)) + pct(cra_base, 20)
  - ci: max(cra_base - cra, 0)
  - tax: pct(min(ci, 300000), 7)
  - floor_s37: pct(cra_base, 1)
  - tax_payable_s37: max(tax, floor_s37)
  - tax_on_receipts_reading: max(tax, pct(receipts, 1))
expected:
  cra_base: 200000
  cra: 240000
  ci: 0
  tax: 0
  floor_s37: 2000
  tax_payable_s37: 2000
  tax_on_receipts_reading: 100000
```

Under s 37, the first case is NGN 14,000, and tax on chargeable income is above the floor. If the Sixth Schedule 'Gross Income' meant receipts, both cases would be NGN 100,000. That is the held point, so give the reviewer both figures. If pension were not taken in total income the first floor would be NGN 10,000, still below tax. The same facts for 2026 income have no minimum tax to test.

### Example 4: Access Bank, Abuja management consultant, income earned in 2025

Amina Bello, management consultant, Abuja. Gross NGN 12,000,000, all from corporate clients. Expenses are assumed at NGN 9,000,000, as the earlier version gave none. At 5% WHT is NGN 600,000.

```oa-check
name: NG income earned in 2025, PITA, WHT above tax
inputs:
  receipts: 12000000
  expenses: 9000000
  wht_receipted: 600000
steps:
  - cra_base: receipts - expenses
  - cra: max(200000, pct(cra_base, 1)) + pct(cra_base, 20)
  - ci: max(cra_base - cra, 0)
  - tax: pct(min(ci, 300000), 7) + pct(clamp(ci - 300000, 0, 300000), 11) + pct(clamp(ci - 600000, 0, 500000), 15) + pct(clamp(ci - 1100000, 0, 500000), 19) + pct(clamp(ci - 1600000, 0, 1600000), 21) + pct(max(ci - 3200000, 0), 24)
  - floor_s37: pct(cra_base, 1)
  - excess_credit: wht_receipted - max(tax, floor_s37)
expected:
  cra_base: 3000000
  cra: 800000
  ci: 2200000
  tax: 350000
  floor_s37: 30000
  excess_credit: 250000
```

WHT of NGN 600,000 is set against tax of NGN 350,000, and the excess of NGN 250,000 is claimed as a refund or set-off; whether s 73(4) reaches this excess depends on which section the deduction fell under. If a client actually deducted 10%, that is over-deduction against the 2024 Regulations unless she had no TIN (reg 3(c)): credit only what the receipts show. Filing authority for an FCT resident is the held FCT point; start with the FCT-IRS.

### Example 5: Zenith Bank, Port Harcourt physician, income earned in 2025

Dr Emeka Nwosu, physician, Port Harcourt, Rivers State. Gross NGN 20,000,000 (hospital fees and private patients), expenses NGN 5,000,000, pension NGN 800,000. If any part is employment income from a hospital, split it out: PAYE and `ng-payroll.md` apply.

```oa-check
name: NG income earned in 2025, PITA, top band
inputs:
  receipts: 20000000
  expenses: 5000000
  pension: 800000
steps:
  - cra_base: receipts - expenses - pension
  - cra: max(200000, pct(cra_base, 1)) + pct(cra_base, 20)
  - ci: max(cra_base - cra, 0)
  - tax: pct(min(ci, 300000), 7) + pct(clamp(ci - 300000, 0, 300000), 11) + pct(clamp(ci - 600000, 0, 500000), 15) + pct(clamp(ci - 1100000, 0, 500000), 19) + pct(clamp(ci - 1600000, 0, 1600000), 21) + pct(max(ci - 3200000, 0), 24)
expected:
  cra_base: 14200000
  cra: 3040000
  ci: 11160000
  tax: 2470400
```

The earlier version's CRA on receipts gave NGN 2,192,000. File with the Rivers State Internal Revenue Service, not the NRS.

### Example 6: Kuda Bank, Lagos freelance designer, low income

Ngozi Eze, freelance designer, Lagos. Gross NGN 600,000, expenses NGN 100,000.

```oa-check
name: NG Example 6A income earned in 2025, PITA, low income
inputs:
  receipts: 600000
  expenses: 100000
steps:
  - cra_base: receipts - expenses
  - cra: max(200000, pct(cra_base, 1)) + pct(cra_base, 20)
  - ci: max(cra_base - cra, 0)
  - tax: pct(min(ci, 300000), 7)
  - floor_s37: pct(cra_base, 1)
  - tax_payable_s37: max(tax, floor_s37)
expected:
  cra_base: 500000
  cra: 300000
  ci: 200000
  tax: 14000
  floor_s37: 5000
  tax_payable_s37: 14000
```

```oa-check
name: NG Example 6B income earned in 2026, NTA, under the 0% band
inputs:
  receipts: 600000
  expenses: 100000
steps:
  - ci: max(receipts - expenses, 0)
  - tax: pct(clamp(ci - 800000, 0, 2200000), 15)
expected:
  ci: 500000
  tax: 0
```

The same income is NGN 14,000 under 2025 law (the earlier version's NGN 12,600 used CRA on receipts) and nil under 2026 law, but she still files for 2026 income (NTAA s 13(1)(a)).

### Example 7: First Bank, Kano accountant with rental income, income earned in 2025

Ibrahim Musa, accountant, Kano. Self-employment NGN 6,000,000 and rental income NGN 2,400,000, each after its own expenses (none were given).

```oa-check
name: NG income earned in 2025, PITA, 2 sources
inputs:
  business: 6000000
  rental: 2400000
steps:
  - cra_base: business + rental
  - cra: max(200000, pct(cra_base, 1)) + pct(cra_base, 20)
  - ci: max(cra_base - cra, 0)
  - tax: pct(min(ci, 300000), 7) + pct(clamp(ci - 300000, 0, 300000), 11) + pct(clamp(ci - 600000, 0, 500000), 15) + pct(clamp(ci - 1100000, 0, 500000), 19) + pct(clamp(ci - 1600000, 0, 1600000), 21) + pct(max(ci - 3200000, 0), 24)
expected:
  cra_base: 8400000
  cra: 1880000
  ci: 6520000
  tax: 1356800
```

All income aggregates after expenses source by source, and one set of bands applies to the total. File with the Kano State Internal Revenue Service. A loss on the rental stays with s 36(2)(b)(iii).

## Ask the client first

1. **Year and accounts.** Which income year is in question, the accounting date, when the business began or stopped, and whether an accounting year crosses 31 December 2025.
2. **Residence and location.** Whether the client is resident in Nigeria, the State or FCT of the place or principal place of residence on the relevant 1 January, days in Nigeria, whether the client is a diplomat or Foreign Service officer, and in which States income is earned. This decides the authority and portal.
3. **Income.** Gross business receipts (from all bank, fintech and platform accounts, 12 months of statements), employment, investment and rental income, foreign income, whether it reached Nigeria or stayed offshore, how it came in, and whether any is in a domiciliary account.
4. **Expenses and assets.** Business expenses with documents, business share of mixed costs, capital assets bought or carried forward, and past losses.
5. **Reliefs.** Pension, National Housing Fund, health insurance and life premium payments, any owner-occupied house loan interest, and for 2026 income the actual rent paid with evidence and the property it relates to.
6. **Credits and identity.** TIN or Tax ID, receipts and statements for all tax deducted, tax already paid, and last year's assessment.

### Defaults and red flags

| Situation | Default |
| --- | --- |
| Residence or State unknown | Stop until resolved (R-NG-2, R-NG-3) |
| CRA computed on receipts | Wrong for 2025 income; use s 33(2). No CRA for 2026 income |
| Capital expenditure deducted directly | Wrong; use capital allowances |
| WHT receipt and statement missing | Do not credit; ask for them. Regulation 8(3) still gives a credit where a receipt was issued but the money was not remitted |
| Minimum tax not checked for 2025 income | Compare computed tax with the s 37 floor and show the Sixth Schedule reading |
| Filing authority unclear | The State of residence; for the FCT, start with the FCT-IRS and record the held point |
| Income year unknown | Stop. The law cannot be chosen |

| Flag | Meaning |
| --- | --- |
| Computed tax is 0 for 2025 income and the floor is above 0 | The s 37 floor applies. For 2026 income, nil tax is nil |
| No WHT receipts from clients | No credit until received |
| Expenses close to income | The Sixth Schedule reading matters for 2025 income; flag to the reviewer |
| Operations in more than one State | Verify the authority |
| Capital expenditure directly expensed | Move to the capital allowance schedule |

### Questions to put to the client

**Filing authority.** 'Personal income tax is paid to the tax authority where you lived on 1 January of the assessment year: your State's Internal Revenue Service or, for Abuja, start with the FCT Internal Revenue Service, which we confirm for your income year. Armed forces and police members who are not civilians, Foreign Service officers and non-residents go to the federal service. Where was your home on that date?'

**WHT receipts.** 'If clients deducted withholding tax from your fees, you need each client's receipt and statement for the amount. Please ask each client for them. Without them the credit is not claimed. From January 2025 the rates for resident non-corporate recipients are 5% on professional fees and 2% on many other services; the rates for 2026 payments are held.'

**CRA.** 'For income earned in 2025 you get a consolidated relief allowance, worked out automatically after your business expenses: the higher of NGN 200,000 or 1% of that figure, plus 20% of that figure. It replaced the personal, children's and dependent relative allowances. Claim it in writing on the return (s 34). It does not exist for income earned from January 2026, when rent relief and other listed deductions apply instead, on evidence.'

**Minimum tax.** 'For income earned in 2025, tax cannot fall below 1% of your total income. How that 1% is measured for someone with high expenses is an open question, so a reviewer will look at it. No individual minimum tax was found for income earned from January 2026.'

### Completion checks

Working paper only. Every worked result goes to a reviewer.

- Income year matched to its law, with no figure from the other regime.
- Authority and portal named, and the residence date stated.
- Every credit backed by a receipt and statement.
- Each held point in 'Not yet confirmed' that touches the client is shown to the reviewer.
- The output says it is not advice and not approved by an accountant.

## Sources

Read on means the date read for this conversion. Limits follow each source. The FIRS-hosted PITA text was read through a dated archived copy; it carries annotations to the Finance Act 2020, and Finance Act 2021 changes were read in that Act. The Finance Act 2020 and Withholding Regulations gazettes were read from the gazettes.africa archive, a third-party host. No State law was read, and no State notice beyond the FCT-IRS notice below. The NRS home page could not be read: a bot check blocked it.

| Source | URL | Read on |
| --- | --- | --- |
| Personal Income Tax Act Cap P8 LFN 2004, FIRS-hosted consolidated text, archived copy of 14 May 2025, annotated to the Finance Act 2020, read in part: ss 2, 3, 6, 6A, 7, 11, 13, 20 to 25, 33 to 39, 41, 43 to 45, 49, 52, 54, 55, 58, 68 to 70, 73, 74, 76, 77, 79, 94 to 96, 108, First Schedule paras 6 to 8, Third Schedule paras 28 to 33, Fifth Schedule paras 7, 8, 27 and Tables I, II, Sixth Schedule | https://web.archive.org/web/20250514045957/https://old.firs.gov.ng/wp-content/uploads/2021/07/Personal-Income-Tax-Act.pdf | 2026-11-05 |
| Finance Act 2020, Gazette No. 4 of 4 January 2021, read in part: ss 25, 27 to 30, 48 | https://archive.gazettes.africa/archive/ng/2021/ng-government-gazette-dated-2021-01-04-no-4.pdf | 2026-11-05 |
| Finance Act 2021, read in part: ss 23, 26, 27 | https://budgetoffice.gov.ng/index.php/resources/internal-resources/budget-documents/finance-act-2021/download | 2026-11-05 |
| Nigeria Tax Act 2025, Act No. 7, Gazette No. 117 of 26 June 2025, National Assembly copy, read in part: ss 12, 13, 15, 17, 20 to 24, 28 to 32, 58, 119 to 121, 162(1), 184, 195, 198, 200, 201, First Schedule Part I, Fourth Schedule, Ninth Schedule items 47, 48 | https://nass.gov.ng/documents/download/11249 | 2026-11-05 |
| Nigeria Tax Act 2025, NRS copy, read for comparison only: Fourth Schedule, s 30 (page image of A417) and residence definitions; its text layer is poor | https://www.nrs.gov.ng/uploads/NIGERIA_TAX_ACT_2025_ef6bb812a5.pdf | 2026-11-05 |
| Nigeria Tax Administration Act 2025, Act No. 5, read in part: ss 3, 4, 7, 13 to 15, 31, 33, 34, 41, 49, 51, 55, 65, 66, 100 to 102, 105, 107, 124, 127, 144, First Schedule | https://tat.gov.ng/Nigeria-Tax-Act-2025.pdf | 2026-11-05 |
| Nigeria Tax Administration Act 2025, press-hosted approved copy, read for comparison only, compared with the copy above by script | https://media.premiumtimesng.com/wp-content/files/2026/01/Approved-Copy-to-Print-NIGERIA-TAX-ADMINISTRATION-ACT-2025.pdf.pdf | 2026-11-05 |
| General Transition Guidelines for the Nigeria Tax Act 2025 and related Acts, read in full; a consultancy-hosted copy, because no official URL was found, so its text and date are not confirmed from the issuer | https://www.bomesresourcesconsulting.com/wp-content/uploads/2026/06/Transition-Guidelines-Nigeria-Tax-Act-2025.pdf | 2026-11-05 |
| Deduction of Tax at Source (Withholding) Regulations 2024, S.I. No. 34 of 2024, Gazette No. 168 of 2 October 2024, read in part: regs 1 to 13 and First Schedule page B763 (page image checked), page B764 not checked | https://archive.gazettes.africa/archive/ng/2024/ng-government-gazette-dated-2024-10-02-no-168.pdf | 2026-11-05 |
| Pension Reform Act 2014, Act No. 4, Official Gazette No. 64 of 2 July 2014, NGF Digital Repository scan, read in part by page image: ss 2 to 4, 120; later amendments not checked | https://ngfrepository.org.ng:8443/bitstream/123456789/968/1/PENSION%20REFORM%20ACT%202014%20-%20GAZETTED%20COPY.pdf | 2026-11-05 |
| Pension Reform Act 2014, PenCom copy, read for comparison only: ss 2 to 4 (page images; the text layer is garbled, and the title page says 'A Bill' with commencement blank) | https://www.pencom.gov.ng/wp-content/uploads/2018/01/PRA_2014.pdf | 2026-11-05 |
| National Housing Fund Act Cap N45 LFN 2004, read in part: ss 4, 10; an unofficial host, and later amendments not checked | https://placng.org/lawsofnigeria/laws/N45.pdf | 2026-11-05 |
| National Minimum Wage (Amendment) Bill 2024, read in full; a Bill, not the Act | https://placng.org/i/wp-content/uploads/2024/07/National-Minimum-Wage-Amendment-Bill-2024.pdf | 2026-11-05 |
| FCT Internal Revenue Service home page, read for its filing line and portal links | https://fctirs.gov.ng/ | 2026-11-05 |
| FCT Internal Revenue Service public notice extending individual returns, read in full | https://fctirs.gov.ng/fct-irs-extends-deadline-for-filing-of-individual-tax-returns-by-one-month/ | 2026-11-05 |
| Lagos Internal Revenue Service home page, read for its portal link; no filing notice shown | https://lirs.gov.ng/ | 2026-11-05 |

Not yet confirmed: the final gazetted text of the Nigeria Tax Act 2025 (2 printed copies differ and press reports a December 2025 direction to gazette again); the official source, date and legal force of the General Transition Guidelines, on which the split between the 2 regimes rests; the printed NTAA commencement entry against the 1 January 2026 date in the Guidelines; how an individual's accounting year crossing 31 December 2025 is split; the minimum tax base under s 37 against the Sixth Schedule; the due date for returns on income of 2026; whether 2025 tax was payable with the return; the Lagos extension of the 2026 return date (press gives 14 and then 21 April 2026; no LIRS notice read); a minimum NGN 500,000 FCT-IRS late-filing penalty reported in the press and found in no text read; which authority collects from FCT residents for 2025 income (PITA text against FCT-IRS practice); which penalties apply to a late 2025 income return; whether the 2024 Withholding Regulations continue for 2026 payments; the enacted National Minimum Wage amount and Act; how the minimum wage carve-outs reach a self-employed person; any PITA change in the Finance Act 2023, which was not obtained; later amendment of the National Housing Fund Act; the National Health Insurance Authority Act; later amendment of the Pension Reform Act; whether a computer is plant for the Fifth Schedule; deductibility of stamp duty and the electronic transfer levy; capital or revenue treatment of CAC fees; a record retention period for 2025; whether rent relief reaches rent that is also a business expense or is not on a home; the Rev360 rollout (law-firm notes say it replaced TaxPro Max from 30 April 2026, with non-residents staying on TaxPro Max); whether Nigerian-performed services are 'earned from abroad'; which foreign income is chargeable solely by being brought in for PITA s 20(2); the business share of a mixed expense under NTA s 20(1); the exchange rate rule for foreign receipts; non-resident status under PITA; form names and portal fields; whether a sole proprietor's business is an 'enterprise' under reg 4(1)(e) of the Withholding Regulations; which year's payments count as eligible deductions against income of 2026; the words 'relief allowance' in the Fourth Schedule preamble; and the bank export formats.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.2 | 2026-11-05 | Converted to the upstream template. Split income earned in 2025 (PITA) from income earned from January 2026 (Nigeria Tax Act 2025), and corrected the CRA base, minimum tax, capital allowances, order of calculation, withholding rates, filing authority, penalties and residence date. Examples recomputed. |
| 2.1 | Legacy | Legacy version, computing CRA on receipts and blending the 2 regimes. |

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
