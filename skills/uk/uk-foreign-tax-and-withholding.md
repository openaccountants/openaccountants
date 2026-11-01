---
name: uk-foreign-tax-and-withholding
description: "Two cross-border methods for the UK for tax year 2026/27 and company periods in 2026. First, foreign tax credit relief for UK residents, individuals and companies: the TIOPA 2010 credit, the limit to UK tax on the same income source by source, unilateral relief, the treaty cap, deduction instead of credit and SA106 with HS263. Second, UK withholding on outbound payments: 20% on yearly interest and on royalties, no withholding on ordinary dividends, 20% on REIT property income distributions, relief at source through DT-Company, DT-Individual and the treaty passport scheme, CT61 quarterly returns, and a treaty rate table for 12 partners. Trigger phrases: foreign tax credit relief, FTCR, double tax relief, SA106, HS263, withholding tax on interest, royalty withholding UK, CT61, DTTP2, DT-Company, treaty rate. Out of scope: non-residents with UK income (uk-non-resident-sa109), FIG regime (uk-non-dom), dividend tax computation (uk-dividends), corporation tax (uk-corporation-tax)."
version: 0.3
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK foreign tax credit relief and withholding on outbound payments v0.3

Tax year 2026/27 (6 April 2026 to 5 April 2027) for individuals. Companies use their accounting period; the rates below apply to payments made in 2026. Returns being filed now (by 31 January 2027) are for 2025/26; the credit rules are the same for both years.

This skill holds two methods the UK pack did not have:

1. **Inbound:** how a UK resident gets credit for foreign tax on foreign income (individuals and companies).
2. **Outbound:** when a UK payer must deduct UK income tax from interest, royalties and other payments, how a treaty cuts the rate, and how the tax is returned on CT61.

It links out for everything else:

- Whether someone is UK resident at all: `uk-statutory-residence-test`.
- Non-residents with UK income, the s.811 limit and the NRL scheme: `uk-non-resident-sa109`.
- The 4-year FIG regime and the old remittance basis: `uk-non-dom`.
- Dividend tax rates and the dividend allowance in general: `uk-dividends`.
- The corporation tax computation, the dividend exemption and the CT600: `uk-corporation-tax`.
- Pricing of intra-group royalties and interest: `uk-transfer-pricing`.

## Who this applies to

**Foreign tax credit relief (FTCR):**

- **UK resident individuals and companies with foreign income or gains that the UK also taxes.** Credit is "not allowed unless the person ... is UK resident for that period" (TIOPA 2010 s.26(1)). HS263: "If you're not a resident of the UK, the Isle of Man or the Channel Islands, you will not be entitled to relief against UK tax." Sections 28 to 30 hold narrow exceptions for some non-residents (Isle of Man and Channel Islands tax, employment income, a UK branch of a non-resident).
- **Relief comes from a treaty or, where there is none, unilaterally.** Unilateral relief gives credit for tax "paid under the law of the territory, calculated by reference to income arising ... in the territory, and corresponding to UK tax" (TIOPA s.9(1)). Credit goes only to tax of the country where the income arises (the source rule, INTM161110).
- **Out:** a person claiming the FIG regime on a source. SA106 notes 2026: "If you're claiming relief under the FIG regime then you cannot also claim FTCR on that income." The foreign income is not taxed, so there is nothing to credit. See `uk-non-dom`.
- **Out:** dividends covered by the dividend allowance. SA106 notes 2026: "If you've not paid tax because you're within the Dividend Allowance then you cannot claim FTCR on that income."

**UK withholding on outbound payments:**

- **Yearly interest arising in the UK** paid by a company, a local authority, a partnership with a company member, or by anyone to a person whose usual place of abode is outside the UK (ITA 2007 s.874(1)).
- **Patent royalties** arising in the UK (ITA s.903) and **royalties for the use of intellectual property** where the owner's usual place of abode is outside the UK (ITA s.906).
- **REIT property income distributions** (UK-REITs deduct at the basic rate, GOV.UK "Claiming Double Taxation Relief for companies").
- **Ordinary dividends are out.** ITA 2007 s.847(2) lists every duty to deduct in Part 15: yearly interest, building society securities, public revenue dividends, annual payments and patent royalties, other IP payments, manufactured payments and non-commercial payments by companies. Company dividends are not on the list, so a UK company pays them gross.
- **Rent to non-resident landlords** is a separate regime: `uk-non-resident-sa109`.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Withholding on yearly interest (ITA s.874(2)) | 20% (the basic rate) | 2026/27 | https://www.legislation.gov.uk/ukpga/2007/3/section/874 ; https://www.legislation.gov.uk/ukpga/2026/11/section/2 |
| Withholding on yearly interest from 6 April 2027 | 22% (FA 2026 Sch 1 para 29 changes s.874(2) to "the savings basic rate" for 2027/28 onward; FA 2026 s.5 sets it at 22% for 2027/28) | 2027/28 | https://www.legislation.gov.uk/ukpga/2026/11/schedule/1/paragraph/29 ; https://www.legislation.gov.uk/ukpga/2026/11/section/5 |
| Withholding on patent royalties and IP royalties to an owner abroad (ITA ss.903, 906) | 20% (the basic rate) | 2026/27 | https://www.legislation.gov.uk/ukpga/2007/3/section/903 ; https://www.legislation.gov.uk/ukpga/2007/3/section/906 |
| Withholding on ordinary dividends | None (no duty in ITA Part 15) | Standing | https://www.legislation.gov.uk/ukpga/2007/3/section/847 |
| Withholding on UK-REIT property income dividends | Basic rate, 20% | 2026/27 | https://www.gov.uk/guidance/double-taxation-relief-for-companies |
| Rate the REIT regulations may require on PIDs from 6 April 2027 | Property basic rate, 22% (ITA s.974(1)(a) as amended by FA 2026 Sch 1 para 33; FA 2026 s.7) | 2027/28 | https://www.legislation.gov.uk/ukpga/2007/3/section/974 ; https://www.legislation.gov.uk/ukpga/2026/11/section/7 |
| CT61 return and payment | Within 14 days after each quarter ending 31 March, 30 June, 30 September, 31 December | Standing | https://www.legislation.gov.uk/ukpga/2007/3/section/949 ; https://www.legislation.gov.uk/ukpga/2007/3/section/947 |
| Dividend ordinary, upper, additional rates (for the FTCR limit) | 10.75%, 35.75%, 39.35% | 2026/27 | https://www.legislation.gov.uk/ukpga/2007/3/section/8 ; https://www.legislation.gov.uk/ukpga/2026/11/section/4 |
| Dividend allowance (dividend nil rate band) | GBP 500 | 2026/27 | https://www.legislation.gov.uk/ukpga/2007/3/section/13A |
| Personal Allowance; higher rate starts above | GBP 12,570; GBP 50,270 of income | 2026/27 | https://www.gov.uk/income-tax-rates |
| FTCR claim time limit, income tax and CGT | Later of the 4th anniversary of the end of the tax year, or 31 January after the tax year in which the foreign tax is paid | Standing | https://www.legislation.gov.uk/ukpga/2010/8/section/19 |
| FTCR claim time limit, corporation tax | Later of 4 years after the accounting period, or 1 year after the period in which the foreign tax is paid | Standing | https://www.legislation.gov.uk/ukpga/2010/8/section/19 |
| Late payment interest (applies to late CT61 tax through TMA s.87) | Bank Rate plus 4%; 7.75% from 9 January 2026 | In force on 23 October 2026 | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates |
| Treaty passport validity | 5 calendar years | Standing | https://www.gov.uk/guidance/double-taxation-treaty-passport-scheme |

### Treaty rates on interest and royalties paid from the UK

The UK deducts 20%. Where the treaty rate is lower, the treaty rate applies once relief is given (see "Relief at source" below). Every treaty below has anti-abuse limits (main purpose tests, limitation on benefits in the US treaty, beneficial ownership). Read the article before relying on the rate.

| Partner | Treaty read | Interest | Royalties | Article |
|---|---|---|---|---|
| United States | 2001 convention as amended by 2002 protocol | 0% (up to 15% on profit-linked interest, Art 11(5)) | 0% | Arts 11, 12 (Art 23 limitation on benefits) |
| Ireland | 1976 convention as amended by 1998 protocol | 0% | 0% | Arts 12, 13 |
| Germany | 2010 convention as amended by 2021 protocol | 0% | 0% | Arts 11, 12 |
| France | 2008 convention | 0% | 0% | Arts 12, 13 |
| Netherlands | 2008 convention as amended by 2013 protocol | 0% | 0% | Arts 11, 12 |
| Luxembourg | 2022 convention, in force 22 November 2023, withholding taxes from 1 January 2024 | 0% | 0% | Arts 11, 12, 29 |
| Switzerland | 1977 convention as amended by 2017 protocol | 0% | 0% | Arts 11, 12 |
| Spain | 2013 convention | 0% | 0% | Arts 11, 12 |
| Italy | 1988 convention | 10% (0% on some credit sales and government loans) | 8% | Arts 11, 12 |
| India | 1993 convention as amended in 2013 | 15% (10% to a bank) | 15%; 10% for equipment rentals and some technical fees | Arts 12, 13 |
| China | 2011 agreement as amended in 2013 | 10% | 10%; for equipment royalties 10% of 60% of the gross, so 6% | Arts 11, 12 |
| Japan | 2006 convention as amended by 2013 protocol | 0% (10% on profit-linked interest) | 0% | Arts 11, 12 |

Treaty URLs are in Sources. For Ireland, France, the Netherlands, Spain, India, China and Japan, GOV.UK also publishes a synthesised text with the Multilateral Instrument. Those texts keep the rates above and add a principal purposes test: no benefit where obtaining it was one of the principal purposes of the arrangement. The 2018 HMRC Digest of Double Taxation Treaties also tabulates rates, but it is out of date for Luxembourg and Germany, so this table is read from the treaty texts.

## The taxable base

### Foreign tax credit relief: individuals

1. **Check the treaty first.** If the treaty gives the UK sole taxing rights, there is no foreign tax to credit. If it gives the other country sole rights, there is no UK tax. If it caps the foreign tax (for example US dividends at 15%), credit is limited to the capped amount (HS263 section 1).
2. **Report the gross.** Foreign income goes into the UK computation gross. With a credit claim, "no deduction is to be made for foreign tax" (TIOPA s.31(2)(a)). On SA106 page F2, column B is the amount before tax and column C the foreign tax; on page F3, column E is marked X to claim and column F repeats column B.
3. **Credit is the lowest of three figures** (HS263 working sheet FTC6):
   - the foreign tax actually paid;
   - the foreign tax the treaty allows;
   - the UK tax on that income.
4. **UK tax on that income** is the tax on total income less the tax on total income without that item (TIOPA s.36(2); HS263 "Appendix 1"). Take each source separately. With more than one source, take them "in the order which will result in the greatest reduction" in tax (s.36(3)). Allowances can be set where they give the most relief (HS263 section 2.2).
5. **Minimisation.** Credit cannot exceed what would have been due had the taxpayer taken "all reasonable steps" under foreign law and the treaty to minimise the foreign tax (TIOPA s.33). Foreign tax over-withheld because a treaty form was not filed is reclaimed abroad, not credited in the UK.
6. **Excess foreign tax is lost.** It "cannot be repaid", cannot be deducted if any credit was claimed on that item, and cannot be carried to another year (INTM161150). Credit is never allowed against Class 4 NIC (same page).
7. **Deduction instead of credit.** A person can elect against credit (TIOPA s.27) and instead reduce the foreign income by the foreign tax (TIOPA s.112; s.113 for gains). HS263: this generally helps only where there is no UK tax in the year, for example because of losses. Credit and deduction cannot be mixed on one item (INTM161090).
8. **Credit is given at Step 6** of the ITA 2007 s.23 calculation (TIOPA s.18(6)).

### Foreign tax credit relief: companies

- The credit against corporation tax "must not exceed" R × IG: the corporation tax rate the company pays on its profits for the period, times the income or gain after the deductions allocated to it under ss.52 to 56 (TIOPA s.42).
- Allocate general deductions and loan relationship debits to the income in the way that keeps the most credit, within the rules of ss.52 to 56.
- Excess foreign tax on an overseas branch can be carried forward or back (TIOPA s.73). Otherwise the excess is lost, as for individuals (INTM161150).
- Most foreign dividends a UK company receives are exempt from corporation tax, so there is no UK tax to credit. See `uk-corporation-tax` for the dividend exemption.

### UK withholding: what is caught

- **Only yearly interest** is caught by s.874; ITA 2007 does not define it, so check whether the loan is short or long before deducting. A deed's location is ignored in deciding whether interest arises in the UK (s.874(6A)).
- **Main exemptions from s.874:** interest paid by banks in the ordinary course (s.878), interest on an advance from a bank where the person beneficially entitled is within the charge to corporation tax on it (s.879), quoted Eurobonds, meaning listed securities carrying a right to interest (s.882), qualifying private placements (s.888A), and payments a company reasonably believes are "excepted payments" (s.930), mainly because the recipient is a UK resident company (s.933) or a non-resident company trading in the UK through a permanent establishment that must bring the payment into its UK chargeable profits (s.934).
- **Royalties:** s.903 covers patent royalties arising in the UK. s.906 covers royalties and other payments for the use of intellectual property (as defined in s.907) where the owner's usual place of abode is abroad. Payments for copies of works exported for distribution abroad are outside s.906 (s.906(4)).
- **Treaty rate on royalties without HMRC clearance.** A company may deduct at the treaty rate if it "reasonably believes" at the time of payment that the payee is entitled to treaty relief (ITA s.911). If the belief turns out wrong, the full 20% is due as if s.911 had never applied (s.911(3)).
- **Interest needs HMRC clearance.** There is no reasonable-belief rule for interest. The payer deducts 20% until HMRC issues a direction, after a DT-Company or DT-Individual claim or a DTTP2 notification under the treaty passport scheme. The treaty passport page: "Until you receive a Direction letter from us, you must withhold tax from the interest payments, unless we tell you that DTTP30610 applies."
- **The EU Interest and Royalties Directive no longer applies.** ITA ss.914 to 917 were repealed by Finance Act 2021 s.34. EU payees now rely on the treaty.

## Deadlines and filing

**Individuals (FTCR):**

- Claim on SA106 (foreign pages) with the return. Box 2 holds total FTCR on income if the taxpayer works out the tax. The 2026/27 return is due 31 January 2028 online. The current SA106 published is the 2026 version, for 2025/26.
- Foreign tax on employment or self-employment income: the income goes on its own pages; the credit is claimed on SA106 pages F6 to F8 (SA106 notes 2026).
- Time limit: TIOPA s.19(2). For 2026/27, credit for tax paid by 31 January 2028 can be claimed until 5 April 2031.

**Companies (FTCR):** claimed in the CT600 for the period, within TIOPA s.19(3).

**Payers (withholding):**

- **CT61.** A UK resident company that makes a payment within ITA s.946 files a return "within 14 days after the end of the return period" (s.949(3)). Return periods are the quarters ending 31 March, 30 June, 30 September and 31 December, cut at the end of the company's accounting period (s.947). The tax is due on the same day, without assessment (s.951). The CT61 cannot be downloaded; it is requested from HMRC online. HMRC accepts aggregated figures but wants separate figures before and from 6 April "to reflect any change in the tax rate" (CTM35050). That matters for interest paid around 6 April 2027, when the rate moves to 22%.
- **Royalties paid at a treaty rate, including 0%.** A royalty paid under s.911 is still one from which the company "is required to deduct" under s.906(5) or s.903(7); s.911 only changes the rate (s.911(1)(a), (2)). It is therefore a s.946 payment, and s.949(2) and (4) require a CT61 for that quarter showing the payment and the tax, which is nil at a 0% treaty rate. The CT61 notes say the same: enter the gross royalty in box 3 and the tax deducted in box 4, tick the box below boxes 3 and 4, and also complete the CT600H supplementary pages with the CT600. "Nil returns are not required" in those notes means quarters with no entries at all. A royalty paid gross because it is an excepted payment under s.930 is different: no duty to deduct arises, so it is not a s.946 payment.
- **Other payers** (individuals, partnerships without company members) account through self assessment or under ITA Part 15 Chapter 16 (ss.903(9), 906(7)).
- **Certificates.** The payer gives the recipient a statement of tax deducted on request (ITA s.975).

**Recipients (relief at source or repayment):**

- **DT-Company / DT-Individual.** The overseas recipient applies to HMRC with a certificate of residence from its own tax authority. HMRC then authorises the payer to pay gross or at the treaty rate, or repays tax already deducted ("Claiming Double Taxation Relief for companies and other concerns"). The DT-Company form is online only.
- **Treaty passport (interest only).** An overseas corporate lender with a passport gives the borrower its reference number. The borrower notifies HMRC on form DTTP2 "as soon as possible once the loan arrangement is entered into". Passports last 5 calendar years; HMRC no longer sends renewal reminders.
- **REIT PIDs:** the overseas investor reclaims the excess over the treaty rate on form UK-REIT DT-Company (US companies use form US-Company UK-REIT).

## Penalties and interest

| Failure | Consequence | Source |
|---|---|---|
| CT61 not delivered, or a payment left off it | Up to GBP 300, then up to GBP 60 a day while it continues | https://www.legislation.gov.uk/ukpga/1970/9/section/98 |
| CT61 not delivered, or the payment not shown on it, where the payment was made gross without a reasonable belief that it was excepted, or under s.911 without a reasonable belief in treaty entitlement | Up to GBP 3,000, then up to GBP 600 a day (TMA s.98(4A), (4B), (4D)) | https://www.legislation.gov.uk/ukpga/1970/9/section/98 |
| Wrong CT61 given fraudulently or negligently | Up to GBP 3,000 (TMA s.98(2)) | https://www.legislation.gov.uk/ukpga/1970/9/section/98 |
| Tax under deducted | The payer is liable for the full sum it should have deducted (ITA s.951(2); s.938; s.911(3)) | https://www.legislation.gov.uk/ukpga/2007/3/section/951 |
| CT61 tax paid late | Interest from the due date under TMA s.87, at the late payment rate (7.75% from 9 January 2026) | https://www.legislation.gov.uk/ukpga/1970/9/section/87 |
| FTCR over-claimed on the return | Normal self assessment and CT inaccuracy rules; a later adjustment of the foreign tax that makes the credit excessive must be notified (TIOPA ss.79, 80) | https://www.legislation.gov.uk/ukpga/2010/8/contents |

Check Bank Rate on the day before quoting interest. The HMRC page names 7.75% from 9 January 2026 and was still current when read on 23 October 2026.

## Cross-border points

- **Non-residents receiving UK interest** are often not charged beyond what is deducted, because of the s.811 limit. That method is in `uk-non-resident-sa109`.
- **The FIG regime replaces credit for that source.** From 6 April 2025 a qualifying new resident can claim relief on foreign income for up to 4 years; any source claimed gets no FTCR. The remittance basis is not available for 2025/26 onward. Pre-April 2025 income remitted later, and the temporary repatriation facility, are covered in `uk-non-dom`.
- **Treaty residence matters.** A dual resident who is treaty resident elsewhere may lose UK credit claims and gain treaty relief instead. See `uk-statutory-residence-test`.
- **Transfer pricing.** Every treaty above limits the relief to an arm's length amount; the excess interest or royalty is taxed under domestic law (for example US Art 11(4), Germany Art 12(4)). UK interest limits also apply (`uk-corporation-tax` for the corporate interest restriction; `uk-transfer-pricing` for pricing).
- **Dividends from abroad.** The dividend method, W-8BEN and common foreign rates are in `uk-dividends` section 4. This skill gives the general credit limit those figures feed into.
- **US limitation on benefits.** US treaty benefits on interest and royalties need the payee to be a "qualified person" or meet another test in Art 23. A US entity that is fiscally transparent may need a different route; ask before paying gross.

## Worked examples

### Example 1: higher-rate taxpayer with GBP 10,000 of US dividends (2026/27)

Priya is UK resident and domiciled. In 2026/27 she has employment income of GBP 70,000 and US dividends of GBP 10,000 gross. Her US broker holds a W-8BEN, so US tax was withheld at 15%: GBP 1,500. The UK-US treaty caps US tax on portfolio dividends at 15% (Art 10(2)(b)), so the treaty limit is also GBP 1,500. She has no other dividends. Her adjusted net income is GBP 80,000, so she keeps the full Personal Allowance.

- **Tax on all income.** Employment income less the allowance is GBP 57,430. GBP 37,700 at 20% is GBP 7,540. GBP 19,730 at 40% is GBP 7,892. Non-dividend tax is GBP 15,432. The dividends all fall above the basic rate limit. The first GBP 500 is at the dividend nil rate. GBP 9,500 at 35.75% is GBP 3,396.25. Total GBP 18,828.25.
- **Tax without the US dividends:** GBP 15,432.
- **UK tax on the US dividends:** GBP 3,396.25.
- **Credit:** the lowest of US tax paid (GBP 1,500), the treaty limit (GBP 1,500) and the UK tax on the item (GBP 3,396.25). Credit is GBP 1,500.
- **UK tax after credit:** GBP 17,328.25. The UK tax left on the dividends is GBP 1,896.25.

**Edge case: no W-8BEN.** If the broker had withheld 30% (GBP 3,000), the credit would still be GBP 1,500, capped by the treaty (HS263 box FTC5; TIOPA s.33). She must reclaim the other GBP 1,500 from the US, not from HMRC.

On her return she enters, on SA106 under dividends from foreign companies: country USA, column B GBP 10,000 and column C GBP 1,500 (page F2), X in column E and GBP 10,000 in column F (page F3).

```oa-check
name: Higher-rate taxpayer, US dividends 10,000 with 15% US tax (2026/27)
inputs:
  employment: 70000
  us_dividend: 10000
  us_tax_paid: 1500
  us_tax_no_w8: 3000
  treaty_rate_pct: 15
  personal_allowance: 12570
  basic_band: 37700
  dividend_allowance: 500
steps:
  - taxable_non_div: employment - personal_allowance
  - non_div_tax: basic_band * 0.20 + (taxable_non_div - basic_band) * 0.40
  - div_tax: (us_dividend - dividend_allowance) * 0.3575
  - tax_with: non_div_tax + div_tax
  - tax_without: non_div_tax
  - uk_tax_on_item: tax_with - tax_without
  - treaty_limit: us_dividend * treaty_rate_pct / 100
  - credit: min(us_tax_paid, treaty_limit, uk_tax_on_item)
  - tax_after_credit: tax_with - credit
  - uk_tax_left_on_dividend: uk_tax_on_item - credit
  - credit_no_w8: min(us_tax_no_w8, treaty_limit, uk_tax_on_item)
  - reclaim_from_us: us_tax_no_w8 - credit_no_w8
expected:
  non_div_tax: 15432.00
  div_tax: 3396.25
  tax_with: 18828.25
  uk_tax_on_item: 3396.25
  credit: 1500.00
  tax_after_credit: 17328.25
  uk_tax_left_on_dividend: 1896.25
  credit_no_w8: 1500.00
  reclaim_from_us: 1500.00
```

### Example 2: UK company pays GBP 100,000 of royalties to its German parent (2026)

UK Sub Ltd has a calendar-year accounting period. It pays its German parent GBP 100,000 for the use of trade marks on 15 May 2026. The parent is resident in Germany, beneficially owns the royalty and has no UK permanent establishment.

- **Domestic rule.** The owner of the IP has its usual place of abode outside the UK, so ITA s.906 requires a 20% deduction: GBP 20,000, with GBP 80,000 paid over.
- **Treaty rule.** Under the UK-Germany convention Art 12(1) the royalties "shall be taxable only in" Germany: 0%.
- **Relief without clearance.** If UK Sub reasonably believes, at the time of payment, that the parent is entitled to treaty relief (for example it holds a German residence certificate and has checked beneficial ownership and the treaty's principal purpose test), it may deduct at 0% under s.911. It pays GBP 100,000 gross.
- **CT61 timing.** The payment falls in the quarter ending 30 June 2026. The CT61 is due by 14 July 2026, and any tax by the same date (ss.949(3), 951). Paying at 0% under s.911, UK Sub still files it, showing GBP 100,000 in box 3, nil in box 4 and the treaty box ticked, and completes CT600H with its CT600 for 2026.
- **If UK Sub cannot form that belief,** it deducts GBP 20,000, files the CT61 and pays the GBP 20,000 by 14 July 2026. The parent then reclaims it from HMRC on form DT-Company and can apply for relief at source on future payments.
- **If UK Sub pays gross on a belief it cannot defend,** HMRC can collect the GBP 20,000 from UK Sub (s.911(3)), with interest from 14 July 2026. If UK Sub also failed to deliver the CT61 or show the payment on it, the penalty is up to GBP 3,000, then up to GBP 600 a day (TMA s.98(4A), (4D)). Thirty days of interest at 7.75% on GBP 20,000 is GBP 127.40.
- **Arm's length.** If the royalty is above an arm's length amount, the treaty applies only to the arm's length part (Art 12(4)); the excess stays taxable at 20%. See `uk-transfer-pricing`.

```oa-check
name: UK company royalty 100,000 to German parent, domestic 20% against treaty 0% (2026)
inputs:
  royalty: 100000
  domestic_rate_pct: 20
  treaty_rate_pct: 0
  late_days: 30
  interest_rate_pct: 7.75
  days_in_year: 365
steps:
  - domestic_wht: royalty * domestic_rate_pct / 100
  - net_paid_domestic: royalty - domestic_wht
  - treaty_wht: royalty * treaty_rate_pct / 100
  - net_paid_treaty: royalty - treaty_wht
  - relief: domestic_wht - treaty_wht
  - interest_if_30_days_late: round(domestic_wht * interest_rate_pct / 100 * late_days / days_in_year, 2)
expected:
  domestic_wht: 20000.00
  net_paid_domestic: 80000.00
  treaty_wht: 0.00
  net_paid_treaty: 100000.00
  relief: 20000.00
  interest_if_30_days_late: 127.40
```

## Ask the client first

1. **Individuals:** Were you UK resident for the year, and are you claiming the FIG regime on any foreign source? (No credit for a non-resident, or for a source under the FIG regime.)
2. **For each foreign source:** which country, gross amount, foreign tax actually paid, and did you file the treaty form there (W-8BEN or the local equivalent)? The credit is capped at the treaty rate.
3. **Companies:** is the foreign income from a branch or a dividend? The dividend exemption and the branch carry-forward change the answer.
4. **Payers:** what is the payment (yearly interest, interest on a loan of under a year, patent royalty, other IP royalty, dividend), when is it paid, and who is the recipient: name, country, type of entity, beneficial owner?
5. **Payers:** does the recipient hold a treaty passport, an HMRC direction, or a residence certificate? Interest needs the direction before paying below 20%; royalties can rely on reasonable belief.
6. **Payers:** what is the company's accounting period end? It sets the CT61 return periods.

## Sources

| Source | URL | Read on |
|---|---|---|
| TIOPA 2010 s.9 (unilateral relief) | https://www.legislation.gov.uk/ukpga/2010/8/section/9 | 2026-10-23 |
| TIOPA 2010 s.18 (credit reduces UK tax) | https://www.legislation.gov.uk/ukpga/2010/8/section/18 | 2026-10-23 |
| TIOPA 2010 s.19 (time limits for claims) | https://www.legislation.gov.uk/ukpga/2010/8/section/19 | 2026-10-23 |
| TIOPA 2010 s.26 (credit only for UK residents) | https://www.legislation.gov.uk/ukpga/2010/8/section/26 | 2026-10-23 |
| TIOPA 2010 s.27 (election against credit) | https://www.legislation.gov.uk/ukpga/2010/8/section/27 | 2026-10-23 |
| TIOPA 2010 s.31 (no deduction where credit claimed) | https://www.legislation.gov.uk/ukpga/2010/8/section/31 | 2026-10-23 |
| TIOPA 2010 s.33 (minimisation of foreign tax) | https://www.legislation.gov.uk/ukpga/2010/8/section/33 | 2026-10-23 |
| TIOPA 2010 s.36 (income tax limit, source by source) | https://www.legislation.gov.uk/ukpga/2010/8/section/36 | 2026-10-23 |
| TIOPA 2010 s.42 (corporation tax limit) | https://www.legislation.gov.uk/ukpga/2010/8/section/42 | 2026-10-23 |
| TIOPA 2010 s.112 (deduction instead of credit) | https://www.legislation.gov.uk/ukpga/2010/8/section/112 | 2026-10-23 |
| TIOPA 2010 contents (ss.28 to 30, 73, 79, 80, 113) | https://www.legislation.gov.uk/ukpga/2010/8/contents | 2026-10-23 |
| ITA 2007 s.8 (dividend rates) | https://www.legislation.gov.uk/ukpga/2007/3/section/8 | 2026-10-23 |
| ITA 2007 s.13A (dividend nil rate, GBP 500) | https://www.legislation.gov.uk/ukpga/2007/3/section/13A | 2026-10-23 |
| ITA 2007 s.847 (duties to deduct in Part 15) | https://www.legislation.gov.uk/ukpga/2007/3/section/847 | 2026-10-23 |
| ITA 2007 s.874 (yearly interest) | https://www.legislation.gov.uk/ukpga/2007/3/section/874 | 2026-10-23 |
| ITA 2007 s.879 (interest on advances from banks) | https://www.legislation.gov.uk/ukpga/2007/3/section/879 | 2026-10-23 |
| ITA 2007 s.882 (quoted Eurobonds) | https://www.legislation.gov.uk/ukpga/2007/3/section/882 | 2026-10-23 |
| ITA 2007 s.888A (qualifying private placements) | https://www.legislation.gov.uk/ukpga/2007/3/section/888A | 2026-10-23 |
| ITA 2007 s.903 (patent royalties) | https://www.legislation.gov.uk/ukpga/2007/3/section/903 | 2026-10-23 |
| ITA 2007 s.906 (IP royalties, owner abroad) | https://www.legislation.gov.uk/ukpga/2007/3/section/906 | 2026-10-23 |
| ITA 2007 s.907 (meaning of intellectual property) | https://www.legislation.gov.uk/ukpga/2007/3/section/907 | 2026-10-23 |
| ITA 2007 s.911 (deduction at treaty rate) | https://www.legislation.gov.uk/ukpga/2007/3/section/911 | 2026-10-23 |
| ITA 2007 s.914 (repealed by FA 2021 s.34) | https://www.legislation.gov.uk/ukpga/2007/3/section/914 | 2026-10-23 |
| ITA 2007 ss.930, 933, 938 (excepted payments) | https://www.legislation.gov.uk/ukpga/2007/3/section/930 | 2026-10-23 |
| ITA 2007 s.946 (payments that go on a CT61) | https://www.legislation.gov.uk/ukpga/2007/3/section/946 | 2026-10-23 |
| ITA 2007 ss.947, 949, 951 (CT61 returns and payment) | https://www.legislation.gov.uk/ukpga/2007/3/section/949 | 2026-10-23 |
| ITA 2007 s.974 (REIT deduction rate) | https://www.legislation.gov.uk/ukpga/2007/3/section/974 | 2026-10-23 |
| ITA 2007 contents (Part 15 section list) | https://www.legislation.gov.uk/ukpga/2007/3/contents | 2026-10-23 |
| Finance Act 2026 ss.2, 4, 5, 7 (2026/27 main rates, dividend rates, 2027/28 savings and property rates) | https://www.legislation.gov.uk/ukpga/2026/11/section/5 | 2026-10-23 |
| Finance Act 2026 Sch 1 paras 29, 33 (s.874 savings basic rate, s.974 property basic rate, from 2027/28) | https://www.legislation.gov.uk/ukpga/2026/11/schedule/1/paragraph/29 | 2026-10-23 |
| TMA 1970 s.87 (interest on overdue tax deducted at source) | https://www.legislation.gov.uk/ukpga/1970/9/section/87 | 2026-10-23 |
| TMA 1970 s.98 (penalties, CT61) | https://www.legislation.gov.uk/ukpga/1970/9/section/98 | 2026-10-23 |
| HMRC HS263 Relief for foreign tax paid (2026) | https://www.gov.uk/government/publications/calculating-foreign-tax-credit-relief-on-income-hs263-self-assessment-helpsheet/relief-for-foreign-tax-paid-2026-hs263 | 2026-10-23 |
| HMRC SA106 Foreign pages and notes (2026) | https://www.gov.uk/government/publications/self-assessment-foreign-sa106 | 2026-10-23 |
| HMRC INTM161000 (DTR for UK residents) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm161000 | 2026-10-23 |
| HMRC INTM161110 (source rule) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm161110 | 2026-10-23 |
| HMRC INTM161150 (excess not repaid or carried) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm161150 | 2026-10-23 |
| HMRC INTM161090 (credit or deduction) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm161090 | 2026-10-23 |
| HMRC CTM35050 (CT61 accounting) | https://www.gov.uk/hmrc-internal-manuals/company-taxation-manual/ctm35050 | 2026-10-23 |
| HMRC CT61 Notes (2010) | https://assets.publishing.service.gov.uk/media/5a7e0a5ce5274a2e8ab4573c/ct61-notes-2010.pdf | 2026-10-23 |
| GOV.UK, Completing the CT600H page for cross-border royalties | https://www.gov.uk/guidance/supplementary-pages-ct600h-cross-border-royalties | 2026-10-23 |
| GOV.UK, Return of Income Tax on company payments (CT61) | https://www.gov.uk/government/publications/corporation-tax-return-of-income-tax-on-company-payments-ct61 | 2026-10-23 |
| GOV.UK, Claiming Double Taxation Relief for companies and other concerns | https://www.gov.uk/guidance/double-taxation-relief-for-companies | 2026-10-23 |
| GOV.UK, Double Taxation Treaty Passport Scheme | https://www.gov.uk/guidance/double-taxation-treaty-passport-scheme | 2026-10-23 |
| GOV.UK, form DT Company | https://www.gov.uk/government/publications/international-tax-double-taxation-treaty-relief-form-dt-company | 2026-10-23 |
| HMRC Digest of Double Taxation Treaties (April 2018) | https://assets.publishing.service.gov.uk/media/5b05425fed915d1317445ed2/DT_Digest_April_2018.pdf | 2026-10-23 |
| GOV.UK, Income Tax rates and Personal Allowances | https://www.gov.uk/income-tax-rates | 2026-10-23 |
| HMRC interest rates for late and early payments | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-10-23 |
| UK-USA 2001 convention as amended by 2002 protocol | https://www.gov.uk/government/publications/usa-tax-treaties/2001-uk-usa-double-taxation-convention-as-amended-by-the-2002-protocol-in-force | 2026-10-23 |
| UK-Ireland 1976 convention as amended by 1998 protocol | https://www.gov.uk/government/publications/ireland-tax-treaties/1976-uk-ireland-double-taxation-convention-as-amended-by-the-1998-protocol-in-force | 2026-10-23 |
| UK-Germany 2010 convention as amended by 2021 protocol | https://www.gov.uk/government/publications/germany-tax-treaties/2010-uk-germany-double-taxation-convention-as-amended-by-the-2021-protocol-in-force | 2026-10-23 |
| UK-France 2008 convention | https://www.gov.uk/government/publications/france-tax-treaties/2008-uk-and-france-double-taxation-convention-in-force | 2026-10-23 |
| UK-Netherlands 2008 convention as amended by 2013 protocol | https://www.gov.uk/government/publications/netherlands-tax-treaties/2008-netherlands-double-taxation-convention-as-amended-by-the-2013-protocol-in-force | 2026-10-23 |
| UK-Luxembourg 2022 convention and protocol | https://www.gov.uk/government/publications/luxembourg-tax-treaties/uk-luxembourg-double-taxation-convention-and-protocol-not-in-force | 2026-10-23 |
| UK-Luxembourg treaties page (in force 22 November 2023) | https://www.gov.uk/government/publications/luxembourg-tax-treaties | 2026-10-23 |
| UK-Switzerland 1977 convention as amended by 2017 protocol | https://www.gov.uk/government/publications/switzerland-tax-treaties/1977-uk-switzerland-double-taxation-convention-as-amended-by-the-2017-protocol-in-force | 2026-10-23 |
| UK-Spain 2013 convention | https://assets.publishing.service.gov.uk/media/5a7f1a77e5274a2e87db3d01/spain-dtc_-_in_force.pdf | 2026-10-23 |
| UK-Italy 1988 convention | https://www.gov.uk/government/publications/italy-tax-treaties/1988-uk-italy-double-taxation-convention-in-force | 2026-10-23 |
| UK-India 1993 convention as amended in 2013 | https://assets.publishing.service.gov.uk/media/5b853e67e5274a4a8fbf169d/1993_India_-_UK_Double_Taxation_Agreement__as_amended_in_2013_-_in_force.pdf | 2026-10-23 |
| UK-China 2011 agreement as amended in 2013 | https://www.gov.uk/government/publications/china-tax-treaties/2011-uk-china-double-taxation-agreement-as-amended-in-2013-in-force | 2026-10-23 |
| UK-Japan 2006 convention as amended by 2013 protocol | https://www.gov.uk/government/publications/japan-tax-treaties/2006-uk-japan-double-taxation-convention-as-amended-by-the-2013-protocol-in-force | 2026-10-23 |
| Synthesised MLI texts (Ireland, France, Netherlands, Spain, India, China, Japan), example: UK-India | https://www.gov.uk/government/publications/india-tax-treaties/2020-uk-india-synthesised-text-of-the-multilateral-instrument-and-the-1993-double-taxation-convention-in-force | 2026-10-23 |

Not yet confirmed: whether SI 2006/2867 itself has been amended so that UK-REITs deduct at 22% from 6 April 2027 (ITA s.974 now permits it; the regulations were not read); the 2026/27 (SA106 2027) form and box numbers, not yet published; whether a given loan carries "yearly" interest, which the Act does not define.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
