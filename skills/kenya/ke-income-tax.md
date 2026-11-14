---
name: ke-income-tax
description: Use this skill whenever asked about Kenyan income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay", "KRA", "iTax", "income tax return", "personal relief", "insurance relief", "turnover tax", "presumptive tax", "self-employed tax Kenya", or any question about filing or computing income tax for a self-employed or sole proprietor client in Kenya. ALWAYS read this skill before touching any Kenyan income tax work.
jurisdiction: KE
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: 2.3
type: computation
category: international
---

# Kenya self-employed income tax (2026) v2.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Resident self-employed individuals and sole proprietors computing business income for the calendar year. [ITA ss2-4,15-16](https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf) control residence, source and taxable profit. A Kenyan bank account/PIN is an intake clue, not proof of residence. Collect bank and M-PESA records; recommended invoices, premium certificates, instalment receipts, PIN and WHT certificates; ideal full books, prior return and iTax ledger. Bank credits alone are not taxable turnover.

Refusal catalogue retained: R-KE-1 companies/LLPs and entity classification go to the relevant adviser/sibling; R-KE-2 non-resident computation is outside this resident workflow, without the old flat-rate assumption; R-KE-3 cross-border WHT/treaties need specialist review; R-KE-4 property/business-asset capital gains need a separate computation. Do not guess missing expenses, business-use share, residence or the tax regime. Hold unsupported deductions pending documents, without asserting that a conservative zero is the legal result.

## Rates, bands and thresholds

All rates below are for the 2026 year of income. The KRA consolidated Act notes outstanding Finance Act amendments on its cover; read it together with the separate Finance Act rather than relying on the cover as proof all deferred changes are applied.

| Annual taxable-income slice (KES) | Rate and condition | Official source |
|---|---|---|
| First 288,000 | 10%, Third Schedule Head B para1 | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Next 100,000 | 25%, same | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Next 5,612,000 | 30%, same | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Next 3,600,000 | 32.5%, same | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Above 9,600,000 | 35%, same | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |

| Item | Amount and complete condition | Official source |
|---|---|---|
| Resident personal relief | KES 28,800 for a full year, credit against tax; ss29-30 and Head A para1, in words on the page; prorate under s29(2)-(4) for arrival intending residence, death or permanent departure, including the paid-leave proviso | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Insurance relief | 15% of qualifying premiums, maximum KES 60,000 per year; s31 and Head A para2, in words on the page; resident claimant and qualifying policy/payer conditions below | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Turnover-tax eligibility | Resident business turnover more than KES 1,000,000 and not exceeding/expected to exceed KES 25,000,000 annually; s12C, in words on the page | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Turnover-tax rate | 1.5% of gross business receipts, final tax; no expense deduction; Head B para9, in words on the page | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Turnover-tax exclusions | Rental, management/professional/training fees and final-WHT income; non-residents outside s12C; written election out permitted | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Resident professional-fee WHT credit | 5% on aggregate qualifying fee KES 24,000 or more in a month, Head B para5(f), in words on the page; certificate supports credit, not a second final charge | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Individual instalment exemption | Current-year total tax not exceeding KES 40,000, s12(5), in words on the page; not old prior-year less-than test | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Proprietor medical costs | Own medical expenses or medical insurance cover, up to KES 1,000,000 per year, s15(3)(g), in words on the page; separate from insurance credit | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Proprietor medical costs | Own medical expenses or medical insurance cover, up to KES 1,000,000 per year, s15(3)(g), in words on the page; separate from insurance credit | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Proprietor medical costs | Own medical expenses or medical insurance cover, up to KES 1,000,000 per year, s15(3)(g), in words on the page; separate from insurance credit | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| SHIF | Contribution deductible under s15(2)(ae); not insurance relief | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |

Capital allowances replace the old reducing-balance table; use the actual asset/use category, not just its bank narration.

| Capital expenditure | Allowance and condition | Official source |
|---|---|---|
| Motor vehicles/heavy earth-moving equipment | 25% per year in equal instalments, Second Schedule para1(b)(v); non-commercial motor vehicle capital cost limited to KES 3,000,000 under para6(1), with proportionate deemed sale proceeds under para6(2), in words on the page; non-commercial motor vehicle capital cost limited to KES 3,000,000 under para6(1), with proportionate deemed sale proceeds under para6(2), in words on the page; non-commercial motor vehicle capital cost limited to KES 3,000,000 under para6(1), with proportionate deemed sale proceeds under para6(2), in words on the page | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Computers/peripheral hardware/software, calculators/copiers/duplicating | 25% per year in equal instalments, para1(b)(vi) | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Furniture and fittings | 10% per year in equal instalments, para1(b)(vii) | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Manufacture machinery | 50% first year of use; residual 25% per year in equal instalments, paras1(b)(i),(iv); special investment conditions need review | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Other machinery | 10% per year in equal instalments, para1(b)(xii) | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |

Insurance credit conditions under s31: establish paid premium and policy evidence. Life cover must insure the individual, spouse or child, secure a capital sum, be with an insurer lawfully carrying on life insurance in Kenya, and pay sums in Kenya in Kenyan currency; an employer-paid premium must be taxed on the individual. The optional pre-determination withdrawal benefit portion is excluded subject to the Commissioner’s allocation. Education maturity must be at least 10 years; life/education terms commence on or after 1 January 2003, health terms on or after 1 January 2007. A child must be under 18 when the premium is paid (including the statutory child categories). Surrender before maturity triggers recovery of relief by the insurer. These dates, periods and age are in words on the cited page. The examples assume qualifying life cover and full-year residence. Medical-expense deduction and insurance credit are distinct provisions; the treatment of an overlapping health premium requires specific authority rather than an invented blanket prohibition.

Insurance credit conditions under s31: establish paid premium and policy evidence. Life cover must insure the individual, spouse or child, secure a capital sum, be with an insurer lawfully carrying on life insurance in Kenya, and pay sums in Kenya in Kenyan currency; an employer-paid premium must be taxed on the individual. The optional pre-determination withdrawal benefit portion is excluded subject to the Commissioner’s allocation. Education maturity must be at least 10 years; life/education terms commence on or after 1 January 2003, health terms on or after 1 January 2007. A child must be under 18 when the premium is paid (including the statutory child categories). Surrender before maturity triggers recovery of relief by the insurer. These dates, periods and age are in words on the cited page. The examples assume qualifying life cover and full-year residence. Medical-expense deduction and insurance credit are distinct provisions; the treatment of an overlapping health premium requires specific authority rather than an invented blanket prohibition.

Insurance credit conditions under s31: establish paid premium and policy evidence. Life cover must insure the individual, spouse or child, secure a capital sum, be with an insurer lawfully carrying on life insurance in Kenya, and pay sums in Kenya in Kenyan currency; an employer-paid premium must be taxed on the individual. The optional pre-determination withdrawal benefit portion is excluded subject to the Commissioner’s allocation. Education maturity must be at least 10 years; life/education terms commence on or after 1 January 2003, health terms on or after 1 January 2007. A child must be under 18 when the premium is paid (including the statutory child categories). Surrender before maturity triggers recovery of relief by the insurer. These dates, periods and age are in words on the cited page. The examples assume qualifying life cover and full-year residence. Medical-expense deduction and insurance credit are distinct provisions; the treatment of an overlapping health premium requires specific authority rather than an invented blanket prohibition.

## The base

1. Reconcile income in Kenyan shillings from invoices, bank and mobile-money statements. Remove documented loans, own-account transfers and capital introduced. Gross up fees received net of creditable withholding and retain certificates.
2. Establish normal assessment or s12C turnover tax before deducting expenses. Under TOT do not deduct costs; a taxpayer can elect out by written notice. Compare only legally available routes.
3. For normal assessment, s15(1) permits expenses wholly and exclusively incurred in producing income, subject to s16 exclusions and documentation, including s16(1)(c): electronic tax invoice management system invoices unless the transaction is exempt under the TPA. Allocate mixed business/private use on evidence. Capital expenditure is not a direct revenue deduction; use capital allowances where eligible.
4. Apply allowable paid pension/SHIF deductions, the proprietor medical-cost deduction above and other established adjustments. Section22A(8) deems NSSF contributions registered defined-contribution fund contributions. For an employee, s22A(1) limits deduction to the least of actual registered-fund contributions, 30% of pensionable income and KES 360,000/year (employer-fund part-year service: KES 30,000/month of service). Section22B(1) limits individual retirement fund eligibility to an individual not a member of a registered fund/public pension scheme during the year; s22B(2) limits deduction to the least of actual contributions by 31 December, 30% of pensionable income and KES 360,000/year (employer contribution for part-year service: KES 30,000/month), with that monetary ceiling reduced by NSSF contributions. All statutory figures/dates here are in words on the page. Establish member category and pensionable income; voluntary NSSF membership alone does not establish an uncapped sole-trader deduction.
5. Apply progressive bands to normal taxable income. Personal/insurance relief are credits, not deductions from profit. Do not refund unused relief in these examples. SHIF is a deduction, without a second insurance-relief credit.
6. Offset evidenced instalment tax and creditable WHT against the final annual liability. Final-tax income is not assessed twice; identify qualifying interest/dividends separately instead of treating all bank interest as ordinary business profit.

### Transaction-pattern library (intake prompts, never proof of tax treatment)

The following retained bank/counterparty patterns help classify documents. Deductibility always depends on actual business purpose under ss15-16, not the supplier brand. They are illustrative workflow labels, not an official authority endorsement of any vendor.


#### 3.1 Kenyan banks (fees and interest)

**Kenyan banks (fees and interest)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| EQUITY BANK | Bank charges: deductible | Monthly/transaction fees |
| KCB, KENYA COMMERCIAL BANK | Bank charges: deductible | Same |
| CO-OPERATIVE BANK, CO-OP | Bank charges: deductible | Same |
| NCBA | Bank charges: deductible | Same |
| STANDARD CHARTERED KENYA | Bank charges: deductible | Same |
| ABSA KENYA (formerly Barclays) | Bank charges: deductible | Same |
| I&M BANK, DTB | Bank charges: deductible | Same |
| REVOLUT, WISE (fees) | Deductible | Fintech fees |
| INTEREST (credit) | Taxable income | Identify the interest instrument and final/credit treatment; see corporate withholding table |
| INTEREST (debit) | Deductible if business loan | Personal: NOT deductible |
| LOAN (principal) | EXCLUDE | Principal movement |

#### 3.2 M-Pesa and mobile money

**M-Pesa and mobile money**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MPESA, M-PESA, SAFARICOM | Transaction fees: deductible | Business M-Pesa charges |
| MPESA PAYBILL, TILL NO | Revenue if incoming; deductible if outgoing business payment | Verify nature |
| MPESA FLOAT, B2C, C2B | EXCLUDE if internal movement | Business float management |
| AIRTEL MONEY | Same as M-Pesa | Alternative mobile money |

#### 3.3 Kenyan government and statutory bodies

**Kenyan government and statutory bodies**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KRA, KENYA REVENUE AUTHORITY | EXCLUDE | Tax payment |
| NSSF, NATIONAL SOCIAL SECURITY | Deductible (up to statutory limit) | Provident fund contribution |
| SHIF, SOCIAL HEALTH INSURANCE | Deductible (ITA s15(2)(ae)) | Deduction from taxable income, not insurance relief |
| NHIF (legacy) | Historical-period review | Do not apply current SHIF treatment to a different historic payment |
| COUNTY GOVERNMENT, NAIROBI COUNTY | Deductible if business licence/permit | Business licence fees |

#### 3.4 Kenyan utilities and telecoms

**Kenyan utilities and telecoms**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KENYA POWER, KPLC | Deductible if business premises | Electricity; apportion if home |
| NAIROBI WATER, ELDOWAS | Deductible if business premises | Water |
| SAFARICOM, AIRTEL, TELKOM KENYA | Deductible: business phone/internet | Mixed: apportion |
| ZUKU, FAIBA | Deductible: business internet | Mixed: apportion |

#### 3.5 SaaS and software -- international

**SaaS and software -- international**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, ADOBE, META | Deductible expense | International SaaS |
| GITHUB, OPENAI, ANTHROPIC | Deductible expense | Non-EU |
| SLACK, ZOOM, ATLASSIAN | Deductible expense | Check entity |

#### 3.6 Professional services (Kenya)

**Professional services (Kenya)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ACCOUNTANT, CPA, AUDIT FIRM | Deductible | Accounting fees |
| ADVOCATE, LAW FIRM | Deductible if business | Legal fees |
| TAX AGENT | Deductible | Tax advisory |

#### 3.7 Transport and travel

**Transport and travel**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KENYA AIRWAYS, JAMBOJET | Deductible if business travel | Flights |
| UBER, BOLT, LITTLE CAB | Deductible if business | Ride services |
| TOTAL, SHELL, RUBIS, VIVO ENERGY | Deductible: business vehicle portion | Fuel |
| SGR (Madaraka Express) | Deductible if business | Train |

#### 3.8 Insurance

**Insurance**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| JUBILEE, BRITAM, CIC, UAP, APA | Deductible if business insurance | Separate business insurance from personal life relief and own medical-cover deduction under s15(3)(g); document policy and beneficiary |
| INSURANCE PREMIUM (life/health/education) | Policy-specific s31 credit conditions above; own medical-cover deduction is separate | Refer overlapping health-premium treatment pending specific authority |

#### 3.9 Food and entertainment

**Food and entertainment**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NAIVAS, CARREFOUR KE, QUICKMART | Default: NOT deductible | Personal provisioning |
| RESTAURANT | Only within s16(2)(a)(ii) exceptions and the business-income test | Business-trip/training/work-convention or conference meals/accommodation, or employee meals on employer premises; retain evidence |

#### 3.10 Internal transfers and exclusions

**Internal transfers and exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal movement |
| MPESA TO BANK, BANK TO MPESA | EXCLUDE | Own account transfer |
| DRAWINGS, PERSONAL | EXCLUDE | Owner drawings |


### Working papers, bank formats and escalation

Retain a Transactions sheet: Date, Counterparty, Description, KES amount, Revenue/Expense/Capital/Insurance/Exclude classification, deductible amount, provisional default, question and notes. Tax Computation sheet: taxable profit, bands, relief, instalments and WHT credits. These are working-paper labels, not official iTax boxes.

Read actual export headers before importing: common fields Date, Description/Narration, Debit, Credit, Balance; Equity date formats, KCB variations and Co-op separators must be confirmed in the client's file rather than hard-coded. M-PESA is separate from the bank; reconcile transaction ID, paybill/till/send-money, recipient and amount. PAYBILL/TILL indicate channels, B2C/C2B describe transfers, and FULIZA/KCB MPESA may involve loans or own movements; establish substance. Document a justified KES conversion for foreign currency; the old universal CBK transaction-date rule is not independently established here.

Ask follow-ups on business activity, turnover, elected regime, insurance, instalments and WHT certificates; do not infer residence from the bank/PIN or credits from a narration. Vehicle/home-office mixed use requires an evidenced business allocation. Industrial buildings/complex allowances go to a reviewer. A dedicated room is not treated here as a universally necessary statutory home-office condition.

### Finance Act, 2026 changes retained


Act No. 19 of 2026, assented 23 June 2026, published in Kenya Gazette Supplement No. 157 (Acts No. 19), 26 June 2026. Read in the KRA copy of the Gazette. Commencement (s.1): ss.17, 18 and 24 on 1 January 2027; s.43 on 1 September 2026; all other sections on 1 July 2026. Income Tax Act amendments that reach individuals and small businesses:

| Section | Change | In force | Official source |
|---|---|---|---|
| s.2 | "Management or professional fee" includes interchange and merchant service fees on card payments. "Royalty" is redefined to include software, proprietary or off-the-shelf, whether licence, development, training, maintenance or support fees, and proprietary digital payment card networks or platforms. New definition of "winnings": a pay-out from a lottery or prize competition by a person licensed under the Gambling Control Act, 2025 | 1 July 2026 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |
| s.3 | Contribution to a gratuity added to s.5(4) as new paragraph (ga): continuous contract of service of at least 3 years, or its renewal or extension beyond 3 years, amount paid not above 31% of emoluments earned for the contract period | 1 July 2026 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |
| s.4 | New s.6B: non-resident rental income tax, a final tax. Register through the simplified framework, then return and payment by the 20th of the month following the end of the month for which the rent is paid, unless a resident receiving the rent is subject to deduction under s.35(1)(c). The rate is in the Third Schedule, not in this section. See `non-resident-rental-income-tax-on-kenyan-property` | 1 July 2026 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |
| s.5 | Income Tax Act s.8(5A) deleted | 1 July 2026 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |
| s.7, s.16, s.21 | Scrap metal and winnings added to s.10 and s.35. Withholding: 1.5% of the gross amount on scrap metal, 20% on winnings (rates in words on the page) | 1 July 2026 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |
| s.8 | Trust income is deemed income of the trustee, executor or administrator. Qualifying dividend or interest in that income bears no further tax. Where the trustee, executor or administrator has paid tax, the beneficiary is not liable on that income | 1 July 2026 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |
| s.9 | s.12(1)(a) replaced: no instalment tax for a person who, to the best of their judgement and belief, will have no income chargeable for the year other than emoluments (read together with ITA s12(1)(b) and s12(5); do not ignore the other conditions) | 1 July 2026 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |
| s.10 | Bad debts of money lenders, banks and licensed financial institutions include principal, interest and related amounts. Deficit carry-forward proviso for a person who invested at least KES 10 billion before 1 July 2025 and has a deficit ascertained for a period before that date: deficit deemed to occur in the 2025 year and may be deducted beyond the ordinary period until extinguished | 1 July 2026 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |
| s.15, s.42 | Income Tax Act s.23 (tax avoidance adjustment) repealed. New Tax Procedures Act s.18A on tax avoidance schemes | 1 July 2026 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |
| s.17 | s.52(1): a return required by the Commissioner's notice is now due by the last day of the 4th month after the year of income, in place of a reasonable time of at least 30 days | 1 January 2027 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |
| s.18 | s.52B(1): individuals file with self-assessment by the last day of the 4th month after the year of income; others by the last day of the 6th month after the accounting period | 1 January 2027 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |
| s.19 | First Schedule: benefits arising due to death added to paragraph 53 proviso; capital gains on transfer of property to a real estate investment trust registered by the Commissioner under s.20(1) exempt (paragraph 76) | 1 July 2026 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |
| s.20 | Second Schedule: 100% in the first year of use on petroleum or gas-storage facilities item (a)(iv) where investment is over KES 10 billion; item (a)(viii) 10% is per year in equal instalments; do not apply this to machinery item (b)(iv) | 1 July 2026 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |
| s.23 | Eighth Schedule: gains of a non-resident on shares that derive value from Kenya, or where the sale changes the group membership of a Kenyan resident company or ownership of property in Kenya | 1 July 2026 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |
| s.47 | Tax Procedures Act s.75: the Commissioner may issue a pre-populated return by the end of January. The person confirms or amends it within 2 months of issue, and may rely on it to file | 1 July 2026 | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |

If a client's year of income ends on 31 December, the s.18 date is 30 April. New s.52B(1)(a) applies to "any year of income", s.1 starts it on 1 January 2027, and the Act has no transitional rule, so the 2026 return is due 30 April 2027. This is derived from the enacted provisions; the KRA notice naming the 2026 return remains a separate confirmation below.

## Deadlines and filing

| Obligation | Due and complete condition | Official source |
|---|---|---|
| Individual return before deferred change | Last day of 6th month after year under existing s52B, in words on the page; this does not preserve that deadline once the new provision commences | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Individual return after commencement | Last day of 4th month after year; FA2026 s18 effective 1 January 2027 under s1(a), in words on the page. Thus 2026 calendar-year return due 30 April 2027 is derived interpretation of commencement and wording, not a separate KRA named-year notice | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |
| Self-assessment payment | Last day of 4th month after year, s92A, in words on the page | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Ordinary instalments | 25% each by 20th of 4th,6th,9th,12th months, s12/Twelfth Schedule; agricultural exceptions need separate review | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| TOT return and payment | 20th of following calendar month, s12C(4),(8), in words on the page | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |

Calculate instalments on the lesser current-year tax basis or 110% of preceding-year assessment, reduce by specified credits under s12(2)-(3), then apply the schedule. Do not ignore the emoluments exemption conditions or current-year individual tax exemption.

For normal assessment, use iTax (https://itax.kra.go.ke), select the resident individual's income-tax return and period, enter reconciled business income/expenses, allowances, other income, reliefs and evidenced credits; validate, submit and save acknowledgement. Generate the payment registration for the correct obligation/period and reconcile the receipt and ledger. Current form/box labels are not supplied by these statutes and must be checked against the actual return.

For TOT, KRA's [official instructions](https://www.kra.go.ke/individual/filing-paying/types-of-taxes/turnover-tax-tot) direct Registration > amend PIN details, basic information/obligation details to register, and the returns menu > file return > turnover tax, download and complete the Excel return, then submit. The page directs the payment menu > payment, select the amount and generate the slip, then pay at a partner bank or through M-PESA; reconcile obligation and period against the actual screen. Save acknowledgements and payment evidence.

## Penalties and interest

[TPA ss38,83(1)(b),(d)(ii),83A](https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf): late ordinary individual return, higher of 5% of tax payable or KES 2,000, with tax reduced by prior payments/WHT credits; late TOT return KES 1,000; late tax 5% plus 1% simple interest per month or part (in words on the page). These are distinct charges. Under s38(8), aggregate accrued late interest cannot exceed the principal tax liability. Section38(6) stops accrual between notification and payment where the outstanding tax, including interest to notification, is paid in full within the notice’s specified time. Section38(2) refunds interest to the extent the underlying principal is found not payable. Under s38(8), aggregate accrued late interest cannot exceed the principal tax liability. Section38(6) stops accrual between notification and payment where the outstanding tax, including interest to notification, is paid in full within the notice’s specified time. Section38(2) refunds interest to the extent the underlying principal is found not payable. The old 20% underestimation-penalty assertion is not used without the applicable provision and facts.

## Cross-border points

Non-residents are referred outside this resident workflow; the old universal flat 30% and prohibition on progressive rates were incorrect generalisations. The Third Schedule individual table applies subject to income-type rules, and personal relief is resident-only. Foreign employment/business, treaties, non-resident consulting WHT and foreign tax relief require the relevant law and treaty. A generic professional-WHT rate must not be assumed to apply to every contract or EAC/SEZ case. Capital gains, including business assets and property, require a separate regime.

## Two worked examples that recompute


### Example 1 -- Standard self-employed, mid-range

**Input:** Resident, revenue KES 3,000,000, expenses KES 1,200,000, qualifying life-qualifying life-qualifying life-insurance premiums KES 100,000, instalment tax KES 150,000.
**Computation:** Taxable = KES 1,800,000. Tax = 28,800 + 25,000 + 423,600 = KES 477,400. Less personal relief 28,800. Less insurance relief min(15,000, 60,000) = 15,000. Net = KES 433,600. Less instalment KES 150,000. Due = KES 283,600.

```oa-check
name: Standard self-employed, profit KES 1,800,000
inputs:
  profit: 1800000
  premiums: 100000
  instalments: 150000
steps:
  - tax: 288000 * 0.10 + 100000 * 0.25 + (profit - 388000) * 0.30
  - insurance_relief: min(premiums * 0.15, 60000)
  - net: tax - 28800 - insurance_relief
  - due: net - instalments
expected:
  tax: 477400
  net: 433600
  due: 283600
```

### Example 1A -- SHIF deducted

**Input:** Resident, profit before SHIF KES 1,800,000, SHIF paid KES 49,500, no insurance premiums.
**Computation:** Taxable = KES 1,750,500. Tax = 28,800 + 25,000 + 408,750 = KES 462,550. Less personal relief 28,800. Insurance relief on SHIF is nil. Net = KES 433,750.

```oa-check
name: SHIF deducted from taxable income, no insurance relief
inputs:
  profit: 1800000
  shif: 49500
steps:
  - taxable: profit - shif
  - tax: 288000 * 0.10 + 100000 * 0.25 + (taxable - 388000) * 0.30
  - net: tax - 28800
expected:
  taxable: 1750500
  tax: 462550
  net: 433750
```

### Example 2 -- Below personal relief

**Input:** Taxable income KES 200,000.
**Computation:** Tax = 10% x 200,000 = KES 20,000. Less relief KES 28,800. Payable = KES 0.

### Example 3 -- Turnover tax

**Input:** Non-professional trader, turnover KES 8,000,000.
**Computation:** TOT = 1.5% x KES 8,000,000 = KES 120,000/year.

### Example 4 -- Trader below the turnover-tax lower boundary

**Input:** Resident small trader, turnover KES 500,000, documented deductible expenses KES 350,000.
**Computation:** Normal profit KES 150,000. Tax KES 15,000 before personal relief; payable KES 0 after the non-refundable relief. Turnover tax does not apply below its lower boundary. Do not charge the old file's invented KES 15,000 annual presumptive tax.


### Example 5 -- Legal election decision: eligible trader

Hypothetical resident trader turnover KES 8,000,000, documented allowable expenses KES 7,500,000, no other income or relief beyond personal relief. TOT would be KES 120,000. If a valid written election out makes normal assessment available, profit KES 500,000 gives tax KES 87,400 before relief, KES 58,600 after relief, difference KES 61,400. Do not silently elect or apply TOT to an excluded professional.

```oa-check
name: Eligible trader compares written election out
inputs:
  turnover: 8000000
  expenses: 7500000
steps:
  - tot: turnover * 0.015
  - profit: turnover - expenses
  - normal_gross: min(profit, 288000) * 0.10 + max(0, min(profit,388000) - 288000) * 0.25 + max(0, profit - 388000) * 0.30
  - normal_net: max(0, normal_gross - 28800)
  - difference: tot - normal_net
expected:
  tot: 120000
  profit: 500000
  normal_gross: 87400
  normal_net: 58600
  difference: 61400
```

### Retained test and edge-case register

The examples above preserve the mid-range, SHIF deduction, below-relief, turnover and below-threshold cases. Additional regression cases: KES 600,000 qualifying life-insurance premiums cap relief at KES 60,000; taxable KES 12,000,000 gives normal resident tax KES 3,718,600 after personal relief and before other credits. Recompute every case from the applicable bands, rather than trusting the old expected output.

```oa-check
name: Insurance cap and high resident income
inputs:
  profit: 12000000
  premiums: 600000
steps:
  - gross_tax: 288000 * 0.10 + 100000 * 0.25 + 5612000 * 0.30 + 3600000 * 0.325 + (profit - 9600000) * 0.35
  - net_before_insurance: gross_tax - 28800
  - insurance_cap: min(premiums * 0.15, 60000)
expected:
  net_before_insurance: 3718600
  insurance_cap: 60000
```

Preserved prohibitions/edge cases: personal relief is never an expense; insurance credit never exceeds cap; professional/management/training income is outside TOT; confirm the election before normal assessment; include evidenced WHT credits; SHIF is deductible without duplicate insurance relief; do not directly expense capital; refer capital gains and non-resident consulting; do not present a provisional working paper as definitive advice. The old presumptive-tax comparison is rejected, not an alternative liability.

## Ask the client first

- Residence and legal form, tax year, activity and any cross-border/other income.
- Reconciled bank and M-PESA statements, invoices, loans/transfers and books.
- Gross turnover, excluded activities and written election/regime evidence.
- Business/private expense split, asset categories/dates and allowance history.
- Qualifying insurance policies and paid premiums, pension and SHIF evidence.
- Instalments, WHT certificates, prior assessment and iTax ledger/filing history.

## Sources

| Source and passages actually read | Official URL | Read on |
|---|---|---|
| Read for ITA s2 residence;ss3-4,12,12C,15-16,22A-22B,29-31,35,52B,92A; Second Schedule and Third Schedule Heads A/B, Twelfth Schedule; passages on normal business income, deductions, rates, capital allowances, credits, exclusions and timing | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf | 2026-11-14 |
| Read for Finance Act 2026 ss1-23,42,47, operative amendments affecting individuals and small businesses and deferred return commencement | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf | 2026-11-14 |
| Read for TPA ss23,38,75,83,83A, records, pre-populated returns, penalties and interest | https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf | 2026-11-14 |
| Read for KRA TOT eligibility, written election, exclusions, registration, return and payment steps | https://www.kra.go.ke/individual/filing-paying/types-of-taxes/turnover-tax-tot | 2026-11-14 |
| Read for KRA PAYE deduction/relief passages for SHIF and registered pension interaction | https://www.kra.go.ke/individual/filing-paying/types-of-taxes/paye | 2026-11-14 |

Not yet confirmed: Current iTax annual-return box labels, KRA guidance naming the 2026 return explicitly under the deferred FA2026 deadline and pre-populated-return/annual-return interaction. The old KES 15,000 presumptive tax under s12D is unsupported: s12C presumptive subsections were deleted and s12D concerned minimum tax and is repealed. Old reducing-balance rates 37.5% heavy machinery,30% computers,12.5% furniture and100% farm machinery are replaced by current asset/use-based allowances. The old universal non-resident flat30%, prior-year less-than KES40000 instalment exemption,20% underestimation penalty, dedicated-room-only home office rule, specific bank CSV formats and universal CBK transaction-date conversion are not usable statutory instructions. The former farm-machinery rate is not replaced with the farmworks rate: farmworks are defined immovable works, not machinery. Confirm the machinery category before allowing a deduction. Complex industrial-building/special-investment allowances and treaty positions require separate review.

> Finance Act, 2026 extract contributed by CPA Julian Njoroge Maina, 25241.
