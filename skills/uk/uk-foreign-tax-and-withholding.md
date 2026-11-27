---
name: uk-foreign-tax-and-withholding
description: "UK foreign tax credit relief for individuals and companies; UK withholding on outbound interest, royalties, ordinary dividends and REIT PIDs; SA106/HS263, CT61, treaty relief and a 12-partner treaty matrix. Individuals: 2026/27, with separately labelled 2025/26 forms; companies: periods/payments in 2026. Links to residence, FIG, dividends, corporation tax and transfer pricing Guides."
version: 0.5
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: computation
---

# UK foreign tax credit relief and withholding on outbound payments v0.5

Individuals: tax year 2026/27 (6 April 2026 to 5 April 2027). Companies use the accounting period for credit and payment date for withholding. The published SA106 2026 is for 2025/26, whose ordinary online deadline is 31 January 2027; its box numbers are not confirmed 2026/27 instructions.

## Who this applies to

This Guide computes credit for foreign tax on income or gains also taxed in the UK, and determines UK withholding. Credit normally requires UK residence for the period (TIOPA 2010 s.26). Sections 28–30 contain limited unilateral-relief exceptions for Isle of Man/Channel Islands residence, specified overseas employment and UK branches/permanent establishments. Non-resident exception computations: **Check this point with one of our partner accountants.**

Relief may arise under a treaty or unilaterally. Under s.9 the foreign tax must correspond to UK tax and be calculated on income/gains arising in that territory, subject to statutory exceptions and restrictions. Check the treaty first: s.11 prevents unilateral relief duplicating treaty credit or bypassing an express treaty denial. For ordinary dividend withholding, s.13 requires tax charged directly on the dividend that neither payer nor recipient would otherwise have borne; specialist underlying-tax cases remain held below. Absence of a treaty does not itself prevent credit. Income relieved under a FIG claim, and dividends with no UK tax because of the dividend allowance, give no credit. For a partial FIG claim, only the appropriate unrelieved proportion remains eligible (SA106 Notes 2026, FN7).

Use uk-statutory-residence-test for residence/treaty residence; uk-non-resident-sa109 for non-resident UK income, s.811 and landlord withholding; uk-non-dom for FIG eligibility, pre-6 April 2025 income, the former remittance basis and TRF; uk-dividends for dividend taxation; uk-corporation-tax for corporate exemptions/CT600/interest restrictions; uk-transfer-pricing for connected-party pricing.

## Rates, bands and thresholds

These are domestic rates before an applicable exemption or authorised treaty reduction.

| Item | Rate or amount | Period and official source |
|---|---|---|
| UK-source yearly interest within ITA 2007 s.874 | 20% | 2026/27; https://www.legislation.gov.uk/ukpga/2007/3/section/874 ; https://www.legislation.gov.uk/ukpga/2026/11/section/2 |
| Yearly interest: enacted change | 22% savings basic rate | From 6 April 2027, 2027/28; FA 2026 s.6(8), Sch 1 para 29; https://www.legislation.gov.uk/ukpga/2026/11/section/5 ; https://www.legislation.gov.uk/ukpga/2026/11/section/6 |
| Royalties within ss.903/906 | 20% basic rate | 2026/27; https://www.legislation.gov.uk/ukpga/2007/3/section/903 ; https://www.legislation.gov.uk/ukpga/2007/3/section/906 ; https://www.legislation.gov.uk/ukpga/2026/11/section/2 |
| Ordinary UK company dividends | No withholding | Excludes REIT PIDs and other special payments; ITA Part 15; https://www.legislation.gov.uk/ukpga/2007/3/section/847 |
| REIT property income distributions (PIDs) | 20% basic rate, subject to gross-payment exceptions | 2026/27; SI 2006/2867 regs 3 and 7; https://www.legislation.gov.uk/uksi/2006/2867/regulation/3 ; https://www.legislation.gov.uk/uksi/2006/2867/regulation/7 ; https://www.legislation.gov.uk/ukpga/2026/11/section/2 |
| CT61 return and tax | Within 14 days after return period ends | Accounting-period boundaries can shorten ordinary quarters; https://www.legislation.gov.uk/ukpga/2007/3/section/947 ; https://www.legislation.gov.uk/ukpga/2007/3/section/949 ; https://www.legislation.gov.uk/ukpga/2007/3/section/951 |
| Dividend ordinary / upper / additional rates; nil-rate allowance | 10.75% / 35.75% / 39.35%; GBP 500 | 2026/27; https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past ; https://www.legislation.gov.uk/ukpga/2026/11/section/4 |
| Example 1 allowance and taxable basic band | GBP 12,570; GBP 37,700 | Full allowance stipulated, no band extensions; higher-rate entry at GBP 50,270 gross is derived for this case only; https://www.gov.uk/income-tax-rates ; https://www.legislation.gov.uk/ukpga/2007/3/section/10 |
| HMRC late-payment interest | 8.00% from 24 November 2026; previously 7.75% from 9 January 2026 | Variable: use the rate for each overdue day. The original July/August illustration below uses 7.75%; https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates |

### Treaty rates on interest and royalties paid from the UK

The table gives UK source-state ceilings for ordinary payments, not automatic withholding instructions or a new domestic charge on equipment rentals/technical fees. Confirm treaty residence, beneficial ownership, payment definition, source, absence of an effectively connected UK permanent establishment/fixed base, arm’s length amount and entitlement/anti-abuse conditions. Interest needs the HMRC direction below unless a domestic exemption applies; royalties need the s.911 conditions. A treaty ceiling never raises a lower domestic liability.

| Partner | Treaty text | Interest | Royalties | Article |
|---|---|---|---|---|
| United States | 2001 convention as amended by 2002 protocol | 0% ordinary; up to 15% for Art 11(5) contingent interest; securitisation exception Art 11(6) | 0% | Arts 11, 12 (Art 23 limitation on benefits); https://www.gov.uk/government/publications/usa-tax-treaties/2001-uk-usa-double-taxation-convention-as-amended-by-the-2002-protocol-in-force |
| Ireland | 1976 convention as amended by 1998 protocol | 0% | 0% | Arts 12, 13; https://www.gov.uk/government/publications/ireland-tax-treaties/1976-uk-ireland-double-taxation-convention-as-amended-by-the-1998-protocol-in-force |
| Germany | 2010 convention as amended by 2021 protocol | 0% | 0% | Arts 11, 12; https://www.gov.uk/government/publications/germany-tax-treaties/2010-uk-germany-double-taxation-convention-as-amended-by-the-2021-protocol-in-force |
| France | 2008 convention | 0% | 0% | Arts 12, 13; https://www.gov.uk/government/publications/france-tax-treaties/2008-uk-and-france-double-taxation-convention-in-force |
| Netherlands | 2008 convention as amended by 2013 protocol | 0% | 0% | Arts 11, 12; https://www.gov.uk/government/publications/netherlands-tax-treaties/2008-netherlands-double-taxation-convention-as-amended-by-the-2013-protocol-in-force |
| Luxembourg | 2022 convention, in force 22 November 2023, withholding taxes from 1 January 2024 | 0% | 0% | Arts 11, 12, 29; https://www.gov.uk/government/publications/luxembourg-tax-treaties/uk-luxembourg-double-taxation-convention-and-protocol-not-in-force |
| Switzerland | 1977 convention as amended by 2017 protocol | 0% | 0% | Arts 11, 12; https://www.gov.uk/government/publications/switzerland-tax-treaties/1977-uk-switzerland-double-taxation-convention-as-amended-by-the-2017-protocol-in-force |
| Spain | 2013 convention | 0% | 0% | Arts 11, 12; https://www.gov.uk/government/publications/spain-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2013-uk-spain-double-taxation-convention-in-force |
| Italy | 1988 convention | 10%; 0% for qualifying equipment/goods credit sales and public/government-backed loans, Art 11(3)–(4) | 8% | Arts 11, 12; https://www.gov.uk/government/publications/italy-tax-treaties/1988-uk-italy-double-taxation-convention-in-force |
| India | 1993 convention as amended in 2013 | 15%; 10% for a beneficial-owner resident bank carrying on bona fide banking business; qualifying public/export-credit interest exempt | 15% Art 13(3)(a) IP and (4)(a)/(c) technical fees; 10% Art 13(3)(b) equipment and (4)(b) ancillary fees, subject to (5) | Arts 12, 13; https://www.gov.uk/government/publications/india-tax-treaties/2020-uk-india-synthesised-text-of-the-multilateral-instrument-and-the-1993-double-taxation-convention-in-force |
| China | 2011 agreement as amended in 2013 | 10%; qualifying government/guaranteed interest exempt under Art 11(3) | 10%; for equipment royalties 10% of 60% of the gross, so 6% | Arts 11, 12; https://www.gov.uk/government/publications/china-tax-treaties/2011-uk-china-double-taxation-agreement-as-amended-in-2013-in-force |
| Japan | 2006 convention as amended by 2013 protocol | 0% ordinary; 10% for Art 11(2) contingent/similar interest; Art 22 entitlement required | 0% | Arts 11, 12; https://www.gov.uk/government/publications/japan-tax-treaties/2006-uk-japan-double-taxation-convention-as-amended-by-the-2013-protocol-in-force |


The US treaty also has Article 23 limitation on benefits and conduit exclusions. Japan Article 22 limits entitlement to its interest exemption and royalty relief; its back-to-back rules can deny beneficial ownership. Apply current treaty/MLI anti-abuse provisions, including the object-and-purpose exception to the principal purposes test where relevant. This table is not clearance for treaty shopping. For transparent entities, conduit/back-to-back arrangements, unusual securitisations, disputed entitlement or a connected UK establishment, stop before applying a table outcome: **Check this point with one of our partner accountants.** Italy Article 11(10) and India Article 12(10) also restrict relief for specified exempt recipients who sell/contract to sell the holding within three months; refer those cases on the same basis. Luxembourg’s 2022 treaty applies to source withholding from 1 January 2024; the old digest is not the rate authority.

## The base

### Foreign tax credit relief

1. Check the treaty’s taxing rights first. Exclusive UK rights leave no permissible foreign tax to credit; exclusive foreign rights leave no UK tax on that item. Otherwise report income gross when claiming credit (TIOPA ss.18, 31).
2. For each source, credit is the lowest of foreign tax paid, foreign tax permitted by the treaty, and UK tax attributable to that source. For income tax, compare UK tax with and without that item, successively removing sources in the order giving the greatest total relief (s.36; HS263). Allocate allowances/reliefs lawfully; do not treat each source as if all could independently occupy the highest band.
3. Take all reasonable steps under foreign law and the treaty to minimise foreign tax, including available claims/elections (s.33). Over-withheld treaty tax is a foreign repayment issue, not extra UK credit.
4. Ordinary excess credit cannot be refunded, deducted after any part has been credited on that income, or moved to another year. No credit against Class 4 NIC (INTM161150). Corporate exceptions are considered separately below.
5. Compare deduction relief instead of credit where relevant. Elect against credit under s.27; s.112 reduces foreign income by qualifying foreign tax paid, subject to its restrictions, and s.113 deals with tax borne on disposal of an asset. Do not combine credit and deduction on the same income. Loss years may favour deduction (HS263). Credit against income tax is applied at Step 6 (s.18(6)).
6. **Companies:** first determine whether the income/dividend/branch profits are exempt, using uk-corporation-tax; no credit against UK tax that is not charged. Section 42 caps credit at R × IG, with IG reduced by allocations under ss.52–56 and subject to its trade/loan/intangible/CFC modifications. R is the applicable pre-credit corporation tax rate, not a universal rate for every company. Do not apply an arbitrary gross-income percentage.
7. **Overseas branches:** ss.72–74 provide carry-forward and carry-back of excess on qualifying overseas PE trading income of a UK-resident company, subject to statutory ordering and credit limits. Recent periods must begin no more than three years before the excess period; ceasing to have the PE cuts off unused forward amounts. This is not a general carryover for all foreign income. For underlying dividend tax, specialist allocations or a branch exemption/carryover computation: **Check this point with one of our partner accountants.**

### UK withholding

- **Interest:** s.874 catches UK-source yearly interest paid by a company, local authority, partnership with a company member, or anyone to someone whose usual abode is abroad. The loan’s duration/intention and circumstances matter, not just payment frequency; do not automatically exempt a loan labelled short-term. Ignore the deed’s location when deciding UK source (s.874(6A)). Uncertain classification/source: **Check this point with one of our partner accountants.**
- **Bank exemptions:** s.878 covers a bank’s ordinary-course payment, subject to its compensation-interest exception. Section 879 covers an advance from a bank where the beneficial owner is within the corporation tax charge on the interest, including its specified s.18A bank case. A foreign bank is not automatically exempt merely because it is a bank.
- **Securities:** quoted Eurobonds are exempt under s.882 only if the s.987 definition is met, including company issue, qualifying listing/trading and right to interest. Qualifying private placements have further regulatory conditions under s.888A. Do not infer eligibility from the instrument’s name. Instrument/regulatory eligibility: **Check this point with one of our partner accountants.**
- **Excepted company payments:** s.930 disapplies specified duties where a company/local authority/qualifying partnership reasonably believes the payment is excepted, subject to HMRC directions and trustee/agent restrictions. Section 933 covers a beneficial-owner UK-resident company; s.934 a beneficial-owner non-resident company trading through a UK PE required to bring the payment into UK chargeable profits. Confirm entitlement before paying gross.
- **Royalties:** s.903 requires the UK-arising patent payment to be charged to income/corporation tax and excludes specified annual payments. Section 906 requires the relevant UK tax charge and covers both IP use/right-to-use where the owner’s abode is abroad, and periodic consideration for IP assigned by an assignor whose abode is abroad. Use the s.907 IP definition, including its copyright exclusions; copies/articles exported for foreign distribution are excluded by s.906(4). Not every cross-border service or equipment payment is an IP royalty.
- **Royalties at a treaty rate:** s.911 applies to a company’s royalty subject to Chapter 6/7 deduction, with tax collectible under Chapter 15/16, if at payment it reasonably believes the payee entitled to treaty relief. The company can use that rate without advance clearance. If the payee was actually not entitled, s.911(3) withdraws the reduction even if the belief was reasonable. Keep evidence of residence, beneficial ownership and treaty entitlement.
- **Interest relief at source:** if no domestic exemption applies, withhold until HMRC gives a direction. A passport alone is not a direction; HMRC’s limited DTTP30610 exception needs HMRC confirmation. Do not extend the royalty reasonable-belief rule to interest.
- **EU directive:** FA 2021 s.34 repealed the former interest/royalty exemptions for payments from 1 June 2021 (and specified earlier avoidance cases). An EU recipient needs an available domestic or treaty route now.

## Deadlines and filing

**Credit claims:** TIOPA s.19 gives individuals the later of four years from tax-year end and 31 January following the year foreign tax is paid; companies the later of four years from period end and one year from the end of the period foreign tax is paid. Thus the ordinary 2026/27 individual deadline is 5 April 2031 where foreign tax is paid by 31 January 2028. A later payment can extend it. Adjustments under ss.79–80 have separate rules.

Claim income FTCR through SA106/HS263; employment or self-employment income belongs on its own pages, with credit details on the applicable foreign pages. On **SA106 2026 for 2025/26**, box 2 is the total income credit if calculating your tax; ordinary dividends use B gross, C the lower of actual foreign tax and treaty-allowed tax, E an X and F the taxable amount following the notes. Do not automatically report over-withheld tax as allowable C. The 2026/27 ordinary online return deadline is 31 January 2028, subject to late-notice exceptions. SA106 2027 box numbers are not yet confirmed: **Check this point with one of our partner accountants.** Companies claim credit in their CT600 for the period.

**CT61:** a UK-resident company making s.946 payments files within 14 days of period end, with tax due the same day without assessment (ss.949, 951). Ordinary quarters end 31 March, 30 June, 30 September and 31 December, split at accounting-period boundaries; building societies have different quarter dates (s.947). Request CT61 from HMRC; it cannot be downloaded. Show separate pre/from 6 April figures where rates differ and reconcile to the accounts (CTM35050).

**Treaty royalties, including nil tax:** a s.911 rate reduction leaves the underlying s.903(7)/906(5) duty within s.946. Report gross payment and tax even at a nil treaty rate. CT61 notes direct gross royalties to box 3, tax to box 4, treaty-procedure tick, and CT600H with the CT600. The 2010 notes’ EU-directive section is superseded by FA 2021 s.34. A payment actually excepted under s.930 has no such deduction duty. No s.946 payments in a period means no return under s.949(2).

**Other payers:** use the applicable self-assessment or Chapter 16 route rather than assume every payer uses CT61 (ss.874(7), 903, 906). Under s.975, provide gross amount, tax and net payment in writing when the recipient requests it in writing, unless the separate s.975A duty applies.

**Relief/repayment:** the overseas recipient claims under DT-Company or DT-Individual with the required tax-residence certification. Use HMRC’s current form route. A passported lender supplies its reference; the borrower files DTTP2 as soon as possible after the loan arrangement. Passports normally last five calendar years; no expiry reminder is issued. UK-REIT treaty repayment claims use UK-REIT DT-Company or, for US companies, US-Company UK-REIT, subject to eligibility.

## Penalties and interest

| Failure | Consequence and conditions | Official source |
|---|---|---|
| CT61 failure within TMA s.98 | Up to GBP 300; if continuing after the initial penalty is imposed, up to GBP 60 for each subsequent continuing day; statutory remedy restrictions apply | https://www.legislation.gov.uk/ukpga/1970/9/section/98 |
| Specified unjustified gross/reduced payment and failure to deliver/show it, s.98(4A)–(4D) | Substituted maxima GBP 3,000 and GBP 600 per subsequent continuing day; requires statutory non-entitlement and lack of reasonable belief, not merely a late return | https://www.legislation.gov.uk/ukpga/1970/9/section/98 |
| CT61 incorrect information furnished fraudulently or negligently | Up to GBP 3,000 under s.98(2); apply its conditions, not automatically to an innocent error | https://www.legislation.gov.uk/ukpga/1970/9/section/98 |
| Unpaid CT61 tax | Payer owes the required deduction; interest from statutory due date at the rate for the overdue period | https://www.legislation.gov.uk/ukpga/2007/3/section/951 ; https://www.legislation.gov.uk/ukpga/1970/9/section/87 |

If a later foreign-tax adjustment makes credit excessive, s.80 generally requires notice to HMRC within one year; its Lloyd’s exception and penalty conditions matter. Section 79 provides a special six-year adjustment claim/assessment window after all material determinations. For return-inaccuracy penalties, a disputed s.98 case or special adjustment: **Check this point with one of our partner accountants.**

## Cross-border points

REIT PIDs differ from ordinary dividends. The 2026/27 basic-rate rule has statutory gross-payment exceptions (SI 2006/2867 reg 7). FA 2026 changes ITA s.974’s enabling limit to the property basic rate from 2027/28; this alone does not prove the rate actually required by the REIT regulations then. **Non-usable hold: do not apply the old proposed 22% REIT deduction for 6 April 2027 onward from this Guide. Check this point with one of our partner accountants.**

Treaty relief on connected-party payments is limited to the arm’s length amount. Do not automatically tax all excess at 20%: treaties preserve domestic taxation with due regard to their other provisions, including possible distribution classification. For excess/classification disputes, transparent entities or dual-resident treaty entitlement: **Check this point with one of our partner accountants.** Residence, non-resident s.811, FIG/TRF, corporate exemption/interest limits and transfer pricing remain with the linked UK Guides above.

## Two worked examples that recompute

### Example 1: higher-rate taxpayer with GBP 10,000 of US dividends (2026/27)

Priya is UK resident and domiciled. Preserve the original inputs: employment GBP 70,000, US dividends GBP 10,000 gross, actual US tax GBP 1,500 with W-8BEN, alternative withholding GBP 3,000 without it. Assume England main employment rates, no other income, deductions, band extensions or FIG claim, full allowance entitlement, UK treaty residence, beneficial ownership and ordinary US portfolio shares. US Article 10(2)(b) caps this dividend at 15%; Article 23 treats an individual resident as a qualified person. For US citizenship/saving-clause or special investment-vehicle facts: Check this point with one of our partner accountants.

Taxable employment is GBP 57,430: GBP 37,700 × 20% + GBP 19,730 × 40% = GBP 15,432. The GBP 500 dividend allowance leaves GBP 9,500 × 35.75% = GBP 3,396.25. UK tax before credit is GBP 18,828.25 and without the dividend GBP 15,432. Credit = min(GBP 1,500 paid, GBP 1,500 treaty cap, GBP 3,396.25 UK tax) = GBP 1,500. UK tax after credit is GBP 17,328.25; UK dividend tax remaining GBP 1,896.25. If GBP 3,000 was withheld, ordinary credit is still GBP 1,500; seek the GBP 1,500 excess abroad. These are 2026/27 computations, not confirmation of unpublished return boxes. The SA106 2026 B/C/E/F illustration above applies only to its stated 2025/26 form.

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

UK Sub Ltd has a calendar-year accounting period and pays GBP 100,000 for trade marks on 15 May 2026. Preserve the parent’s German residence, beneficial ownership and absence of a UK PE. Assume a UK-arising taxable, arm’s length royalty, no treaty abuse and no other exemption.

Domestic s.906 withholding is GBP 20,000; net GBP 80,000. UK-Germany Article 12(1) gives a nil source-state rate on these facts. If the company reasonably believes at payment that the parent is entitled and s.911’s collection conditions hold, it can pay GBP 100,000 gross. CT61 for the quarter ending 30 June is due 14 July 2026 even with nil treaty tax: box 3 GBP 100,000, box 4 nil and treaty tick, plus CT600H with the period’s CT600. If it cannot reasonably establish entitlement, deduct/pay GBP 20,000 by that date and the eligible parent claims repayment.

If the parent was actually not entitled, s.911(3) restores the domestic liability; deficient belief alone is not that statutory trigger. An additional failure to report with no reasonable belief and no entitlement can engage the enhanced s.98 maxima. For a separate illustration of **30 overdue days after 14 July 2026** entirely within the then 7.75% rate, interest on GBP 20,000 is GBP 127.40. The current 8% rate from 24 November is not substituted into that historical interval. An above-arm’s-length royalty needs the excess classified under domestic law and the treaty; do not extend the nil rate to it or assume every excess has the same tax outcome.

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

1. Residence/treaty residence and tax year; any FIG claim and the exact relieved amount, plus US citizenship or other special treaty facts.
2. Each source: country, gross income/gain, UK taxable amount, foreign tax paid/payable/refunded, treaty cap and steps already taken for relief abroad.
3. For companies: period end, exemptions, PE/trading source, deductions allocated, rate and unused foreign tax history.
4. For outbound payments: date, UK source, legal payment type, loan terms, IP/assignment terms, arm’s length amount, and beneficial owner’s residence/entity/UK PE facts.
5. Exemption evidence, treaty residence certificate, entitlement/anti-abuse checks, HMRC direction or passport reference/DTTP2; identify what supports any s.911 reasonable belief.
6. Return periods, payment records, deduction statements, CT61/CT600H filings and any later tax adjustment.

## Sources

Case amounts are hypothetical original inputs. Dates below distinguish fresh reads from applicable unchanged UK proof reused from the completed UK dividends/SA100 ledgers.

| Source | URL | Read on |
|---|---|---|
| TIOPA 2010 s.9 (unilateral relief) | https://www.legislation.gov.uk/ukpga/2010/8/section/9 | 2026-11-27 |
| TIOPA 2010 s.18 (credit reduces UK tax) | https://www.legislation.gov.uk/ukpga/2010/8/section/18 | 2026-11-27 |
| TIOPA 2010 s.19 (time limits for claims) | https://www.legislation.gov.uk/ukpga/2010/8/section/19 | 2026-11-27 |
| TIOPA 2010 s.26 (credit only for UK residents) | https://www.legislation.gov.uk/ukpga/2010/8/section/26 | 2026-11-27 |
| TIOPA 2010 s.27 (election against credit) | https://www.legislation.gov.uk/ukpga/2010/8/section/27 | 2026-11-27 |
| TIOPA 2010 s.31 (no deduction where credit claimed) | https://www.legislation.gov.uk/ukpga/2010/8/section/31 | 2026-11-27 |
| TIOPA 2010 s.33 (minimisation of foreign tax) | https://www.legislation.gov.uk/ukpga/2010/8/section/33 | 2026-11-27 |
| TIOPA 2010 s.36 (income tax limit, source by source) | https://www.legislation.gov.uk/ukpga/2010/8/section/36 | 2026-11-27 |
| TIOPA 2010 s.42 (corporation tax limit) | https://www.legislation.gov.uk/ukpga/2010/8/section/42 | 2026-11-27 |
| TIOPA 2010 ss.112–113 (read for income/disposal-tax deduction conditions) | https://www.legislation.gov.uk/ukpga/2010/8/section/112 ; https://www.legislation.gov.uk/ukpga/2010/8/section/113 | 2026-11-27 |
| ITA 2007 s.847 (duties to deduct in Part 15) | https://www.legislation.gov.uk/ukpga/2007/3/section/847 | 2026-11-27 |
| ITA 2007 s.874 (yearly interest) | https://www.legislation.gov.uk/ukpga/2007/3/section/874 | 2026-11-27 |
| ITA 2007 s.879 (interest on advances from banks) | https://www.legislation.gov.uk/ukpga/2007/3/section/879 | 2026-11-27 |
| ITA 2007 s.882 (quoted Eurobonds) | https://www.legislation.gov.uk/ukpga/2007/3/section/882 | 2026-11-27 |
| ITA 2007 s.888A (qualifying private placements) | https://www.legislation.gov.uk/ukpga/2007/3/section/888A | 2026-11-27 |
| ITA 2007 s.903 (patent royalties) | https://www.legislation.gov.uk/ukpga/2007/3/section/903 | 2026-11-27 |
| ITA 2007 s.906 (IP royalties, owner abroad) | https://www.legislation.gov.uk/ukpga/2007/3/section/906 | 2026-11-27 |
| ITA 2007 s.907 (meaning of intellectual property) | https://www.legislation.gov.uk/ukpga/2007/3/section/907 | 2026-11-27 |
| ITA 2007 s.911 (deduction at treaty rate) | https://www.legislation.gov.uk/ukpga/2007/3/section/911 | 2026-11-27 |
| ITA 2007 s.946 (payments that go on a CT61) | https://www.legislation.gov.uk/ukpga/2007/3/section/946 | 2026-11-27 |
| ITA 2007 ss.947, 949, 951 (CT61 returns and payment) | https://www.legislation.gov.uk/ukpga/2007/3/section/949 | 2026-11-27 |
| TMA 1970 s.87 (interest on overdue tax deducted at source) | https://www.legislation.gov.uk/ukpga/1970/9/section/87 | 2026-11-27 |
| TMA 1970 s.98 (penalties, CT61) | https://www.legislation.gov.uk/ukpga/1970/9/section/98 | 2026-11-27 |
| HMRC HS263 Relief for foreign tax paid (2026) | https://www.gov.uk/government/publications/calculating-foreign-tax-credit-relief-on-income-hs263-self-assessment-helpsheet/relief-for-foreign-tax-paid-2026-hs263 | 2026-11-27 |
| HMRC SA106 Foreign pages and notes (2026) | https://www.gov.uk/government/publications/self-assessment-foreign-sa106 | 2026-11-27 |
| HMRC INTM161150 (excess not repaid or carried) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm161150 | 2026-11-27 |
| HMRC CTM35050 (CT61 accounting) | https://www.gov.uk/hmrc-internal-manuals/company-taxation-manual/ctm35050 | 2026-11-27 |
| HMRC CT61 Notes (2010) | https://assets.publishing.service.gov.uk/media/5a7e0a5ce5274a2e8ab4573c/ct61-notes-2010.pdf | 2026-11-27 |
| GOV.UK, Completing the CT600H page for cross-border royalties | https://www.gov.uk/guidance/supplementary-pages-ct600h-cross-border-royalties | 2026-11-27 |
| GOV.UK, Return of Income Tax on company payments (CT61) | https://www.gov.uk/government/publications/corporation-tax-return-of-income-tax-on-company-payments-ct61 | 2026-11-27 |
| GOV.UK, Claiming Double Taxation Relief for companies and other concerns | https://www.gov.uk/guidance/double-taxation-relief-for-companies | 2026-11-27 |
| GOV.UK, Double Taxation Treaty Passport Scheme | https://www.gov.uk/guidance/double-taxation-treaty-passport-scheme | 2026-11-27 |
| GOV.UK, form DT Company | https://www.gov.uk/government/publications/international-tax-double-taxation-treaty-relief-form-dt-company | 2026-11-27 |
| HMRC interest rates for late and early payments | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-11-27 |
|UK-USA 2001 convention as amended by 2002 protocol (read for Arts 10–12 and 23) | https://www.gov.uk/government/publications/usa-tax-treaties/2001-uk-usa-double-taxation-convention-as-amended-by-the-2002-protocol-in-force | 2026-11-27 |
|UK-Ireland 1976 convention as amended by 1998 protocol (read for Arts 12–13) | https://www.gov.uk/government/publications/ireland-tax-treaties/1976-uk-ireland-double-taxation-convention-as-amended-by-the-1998-protocol-in-force | 2026-11-27 |
|UK-Germany 2010 convention as amended by 2021 protocol (read for Arts 11–12 and treaty benefit test) | https://www.gov.uk/government/publications/germany-tax-treaties/2010-uk-germany-double-taxation-convention-as-amended-by-the-2021-protocol-in-force | 2026-11-27 |
|UK-France 2008 convention (read for Arts 12–13) | https://www.gov.uk/government/publications/france-tax-treaties/2008-uk-and-france-double-taxation-convention-in-force | 2026-11-27 |
|UK-Netherlands 2008 convention as amended by 2013 protocol (read for Arts 11–12) | https://www.gov.uk/government/publications/netherlands-tax-treaties/2008-netherlands-double-taxation-convention-as-amended-by-the-2013-protocol-in-force | 2026-11-27 |
|UK-Luxembourg 2022 convention and protocol (read for Arts 11–12 and 29) | https://www.gov.uk/government/publications/luxembourg-tax-treaties/uk-luxembourg-double-taxation-convention-and-protocol-not-in-force | 2026-11-27 |
|UK-Luxembourg treaties page (in force 22 November 2023) (read for Arts 11–12 and 29) | https://www.gov.uk/government/publications/luxembourg-tax-treaties | 2026-11-27 |
|UK-Switzerland 1977 convention as amended by 2017 protocol (read for Arts 11–12) | https://www.gov.uk/government/publications/switzerland-tax-treaties/1977-uk-switzerland-double-taxation-convention-as-amended-by-the-2017-protocol-in-force | 2026-11-27 |
|UK-Spain 2013 convention (read for Arts 11–12 and MLI benefit test) | https://www.gov.uk/government/publications/spain-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2013-uk-spain-double-taxation-convention-in-force | 2026-11-27 |
|UK-Italy 1988 convention (read for Arts 11–12) | https://www.gov.uk/government/publications/italy-tax-treaties/1988-uk-italy-double-taxation-convention-in-force | 2026-11-27 |
|UK-India 1993 convention as amended in 2013 (read for Arts 12–13 and MLI benefit test) | https://www.gov.uk/government/publications/india-tax-treaties/2020-uk-india-synthesised-text-of-the-multilateral-instrument-and-the-1993-double-taxation-convention-in-force | 2026-11-27 |
|UK-China 2011 agreement as amended in 2013 (read for Arts 11–12) | https://www.gov.uk/government/publications/china-tax-treaties/2011-uk-china-double-taxation-agreement-as-amended-in-2013-in-force | 2026-11-27 |
|UK-Japan 2006 convention as amended by 2013 protocol (read for Arts 11–12 and 22) | https://www.gov.uk/government/publications/japan-tax-treaties/2006-uk-japan-double-taxation-convention-as-amended-by-the-2013-protocol-in-force | 2026-11-27 |
| Synthesised MLI texts (Ireland, France, Netherlands, Spain, India, China, Japan), example: UK-India | https://www.gov.uk/government/publications/india-tax-treaties/2020-uk-india-synthesised-text-of-the-multilateral-instrument-and-the-1993-double-taxation-convention-in-force | 2026-11-27 |
| FA 2026 ss.2, 4, 5, 6 and Sch 1 paras 29, 33: rates and commencement | https://www.legislation.gov.uk/ukpga/2026/11/section/6 | 2026-11-27 |
| REIT deduction and exceptions, SI 2006/2867 regs 3, 7 | https://www.legislation.gov.uk/uksi/2006/2867/regulation/3 ; https://www.legislation.gov.uk/uksi/2006/2867/regulation/7 | 2026-11-27 |
| TIOPA ss.28–30, 72–74, 79–80: exceptions, branch carryover and adjustment | https://www.legislation.gov.uk/ukpga/2010/8/section/72 ; https://www.legislation.gov.uk/ukpga/2010/8/section/80 | 2026-11-27 |
| ITA ss.878, 930, 933, 934, 975, 987: exceptions, statements and securities | https://www.legislation.gov.uk/ukpga/2007/3/section/930 ; https://www.legislation.gov.uk/ukpga/2007/3/section/987 | 2026-11-27 |
| FA 2021 s.34: EU exemption repeal | https://www.legislation.gov.uk/ukpga/2021/26/section/34 | 2026-11-27 |
| SA106 2026 and notes, for 2025/26 only | https://assets.publishing.service.gov.uk/media/69bbd5d34b1db2e4ba9b645f/SA106_2026.pdf ; https://assets.publishing.service.gov.uk/media/69bbd6144c478213a823ce14/SA106_Notes_2026.pdf | 2026-11-27 |
| HMRC yearly interest | https://www.gov.uk/hmrc-internal-manuals/savings-and-investment-manual/saim9070 ; https://www.gov.uk/hmrc-internal-manuals/savings-and-investment-manual/saim9075 | 2026-11-27 |
| UK rates/allowances and ordinary deadlines: completed UK dividends/SA100 proof reused | https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past ; https://www.gov.uk/income-tax-rates ; https://www.legislation.gov.uk/ukpga/1970/9/section/8 | 2026-11-26/27; applicability 2026-11-27 |
| Current UK treaty/MLI eligibility texts (rates also checked against base treaties above) | https://www.gov.uk/government/publications/ireland-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-1976-ireland-uk-double-taxation-convention-in-force ; https://www.gov.uk/government/publications/france-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2008-uk-france-double-taxation-convention-in-force ; https://www.gov.uk/government/publications/netherlands-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2008-uk-netherlands-double-taxation-convention-in-force ; https://www.gov.uk/government/publications/china-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2013-uk-china-double-taxation-agreement-and-protocol-in-force ; https://www.gov.uk/government/publications/japan-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2006-uk-japan-double-taxation-convention-in-force | 2026-11-27 |

Not yet confirmed: 2027/28 REIT regulatory deduction rate; SA106 2027 form boxes; transaction-specific specialist outcomes explicitly held above. These holds are not usable filing conclusions.
