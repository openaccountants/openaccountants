---
name: im-non-resident-income-tax
description: >
  Use this skill for Isle of Man income tax on individuals who are not resident
  in the Island, for the 2026/27 tax year (6 April 2026 to 5 April 2027). It covers
  the 21% non-resident rate with no personal allowance, which Manx income is
  taxable and which is excluded (Manx bank interest, Manx company dividends, the
  Manx State Pension), the section 11A limit on tax, the non-resident return due
  6 October, payer deductions under notice N15 with forms N13, N20, N35 and N37,
  the HR code for non-resident employees, pension relief on form R221, and the
  UK treaty rules on residence, employment, directors, pensions, government
  service, entitlement and mutual agreement. Trigger on: Isle of Man non-resident
  tax, Manx rent non-resident landlord, N15 notice, R221 pension relief, HR tax
  code, UK resident with Isle of Man pension. Out of scope: residents
  (im-income-tax), companies and permanent establishments (im-corporate-income-tax),
  National Insurance (im-payroll-social).
jurisdiction: IM
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-30
version: 0.4
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Isle of Man: income tax on non-resident individuals (2026/27) v0.4

This skill covers individuals who are not resident in the Isle of Man and receive Manx income, and the people who pay them. The year is **6 April 2026 to 5 April 2027**. The law is the Income Tax Act 1970 (AT 3 of 1970); the authority is the Income Tax Division of the Treasury. Residence itself is decided under [im-income-tax](im-income-tax.md) (six-month test, 90-day practice, departures); companies and permanent establishments are in [im-corporate-income-tax](im-corporate-income-tax.md); related-party treaty adjustments are in [im-related-party-uk-treaty](im-related-party-uk-treaty.md).

## Who this applies to

- **Non-resident individuals with Manx income.** A person not resident pays tax at the prescribed rate on every pound of Manx income, meaning income from a trade, profession, employment or vocation carried on in the Island and income from any other source in the Island (ITA 1970 s.1(3), (3A)).
- **Typical taxable income** after leaving: Manx rents and Manx occupational or private pensions (Leaving the Island page).
- **Income not taxable to non-residents:** Manx bank and building society interest, dividends and the Manx State Pension (Leaving the Island page). In law this works through the section 11A limit on excluded income (see The base).
- **Payers.** Anyone paying rent, interest or similar payments to a person resident outside the Island is required by the Division to deduct tax (Making payments to non-residents page). Employers of non-resident employees apply code HR (Non-resident employees page).
- **Couples.** Non-resident spouses and civil partners cannot elect joint taxation; each is taxed on their own income (Receiving Isle of Man source income page; ITA 1970 s.35C(2)).
- **Part years.** A person who becomes resident or ceases residence during the year gets both a resident and a non-resident allowance, each apportioned by date (Receiving Isle of Man source income page; s.35D). This skill works full-year non-residence; for the resident part see [im-income-tax](im-income-tax.md).

## Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Non-resident rate on all Manx taxable income | 21% | 2026/27 (also 2025/26) | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/rates-and-allowances/ ; PN 227/26; Budget 2026 page |
| Non-resident personal allowance | GBP 0 | 2026/27 | rates page; ITA 1970 s.35C(1) |
| Rate on non-corporate entities other than individuals | 21% | 2026/27 | PN 227/26; Budget 2026 page |
| Payer deduction | the prescribed higher rate (21%) | 2026/27 | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/non-residents/making-payments-to-non-residents/ ; rates page |
| Remittance of tax deducted (form N35) | within 14 days of making the payment | 2026/27 | Making payments to non-residents page |
| Non-resident return due | 6 October after the tax year (6 October 2027 for 2026/27) | 2026/27 | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/non-residents/receiving-isle-of-man-source-income/ |
| Late non-resident return penalty | GBP 100 | 2026/27 | Receiving Isle of Man source income page |
| UK treaty, employment presence limit | 183 days in any twelve-month period starting or ending in the fiscal year | from 6 April 2019 | SI 2018/1347 Article 14(2) |
| UK treaty, mutual agreement time limit | 3 years from first notification of the action | from 6 April 2019 | SI 2018/1347 Article 25(1) |

The rate was 22% for 2024/25 and 20% for 2023/24 and earlier (rates page, historic table). Practice Note PN 130/06 still shows a GBP 2,000 allowance and 18% rate from 2006; the Division warns those figures are historical (Receiving Isle of Man source income page; Leaving the Island page).

## The base

### Step 1: classify each item of Manx income

List every Manx-source receipt and sort it into taxable income, excluded income and treaty-relieved income. Do not treat every payment from a Manx account as taxable, or every payment called interest as excluded.

### Step 2: excluded income and the section 11A limit

For an individual not resident for the whole year, tax cannot exceed the sum of (a) the tax that would be due on total Manx income reduced by excluded income and (b) the tax actually deducted at source from excluded income, ignoring the personal allowance (ITA 1970 s.11A(1)). Excluded income is (s.11A(2)):

- dividends paid by a company incorporated under the Companies Acts 1931 to 2004 or registered under the Foreign Companies Act 2014;
- deposit interest paid by a holder of a deposit-taking licence under section 7 of the Financial Services Act 2008;
- interest or dividends paid by a building society authorised under the Building Societies Act 1986;
- interest or dividends on Isle of Man Government bonds (Isle of Man Loans Act 1974) and on local authority securities (Local Government Act 1985 s.50);
- social security benefits chargeable under section 48;
- national insurance retirement pensions paid by the Treasury;
- other income designated by Treasury order approved by Tynwald.

Income from a trade or profession carried on in the Island through a representative or branch is not excluded income (s.11A(2)). The limit does not apply to non-resident trustees where a beneficiary is resident in the Island (s.11A(4)).

### Step 3: tax on the remaining income

Charge 21% on the taxable Manx income with no allowance (s.1(3), s.35C; rates page). Allowable expenses and the taxable amount must be established first: tax withheld from a gross payment does not by itself fix the taxable base. Do not apply the resident 10% band or resident allowances to a full-year non-resident.

### Step 4: credits

Deduct tax withheld by payers (N13 certificates), PAYE-style deductions under code HR and any accepted treaty relief.

## Deadlines and filing

**Recipient's return.** Non-residents with Manx income such as rent or pensions receive a return issued on 6 April for the year ended the previous 5 April. Every item of income goes on it and it is due by the following 6 October (Receiving Isle of Man source income page). For 2026/27: issued 6 April 2027, due 6 October 2027. Guidance Note GN1NR is the non-resident return guide.

**Payer procedure.** When the Division learns that a person is paying a non-resident, it issues (Making payments to non-residents page):

| Form | Purpose |
|---|---|
| N15 | Notice to deduct tax from all future payments |
| N13 | Certificate of tax deducted: gross payment, tax deducted and net amount paid, sent to the recipient with the balance |
| N20 | Estate agent registration of a new property rented by a non-resident landlord, sent to the Division |
| N35 | Remittance card sent with the tax within 14 days of making the payment |
| N37 | Annual return at the tax year end listing all payments in the year |
| R221 | Application by a resident of a treaty country for a Manx pension to be paid without deduction, or for repayment of tax deducted |

A common case is a letting agent collecting rent for a non-resident owner. Reconcile N13 certificates and N35 remittances to the payer's ledger and the recipient's return.

**Employers.** A non-resident employee has no personal allowance and the employer applies code HR. If all duties are performed outside the Island, no tax need be deducted, but only after prior clearance from the Division; without clearance code HR applies. If only part of the duties are performed in the Island, tax is deducted from the whole remuneration (Non-resident employees page). Do not prorate payroll deductions on a day count without clearance; treaty relief is claimed through the Division.

**Pension relief (form R221).** By default the non-resident rate is deducted from every Manx occupational or private pension until an application is made and accepted. The R221 is sent first to the tax authority of the new country of residence to confirm residence, then to the Income Tax Division (Leaving the Island page; Non-resident pensioners page). For UK residents, a successful claim means future payments are made gross and tax deducted since 6 April 2009 is refunded (Non-resident pensioners page).

## Penalties and interest

- **Late non-resident return:** GBP 100 if not submitted by 6 October (Receiving Isle of Man source income page).
- **Payers:** tax deducted is remitted with the N35 within 14 days of payment (Making payments to non-residents page).
- Further penalties for non-residents, the payment date of a non-resident assessment, and penalties on payers who fail to deduct are on the Not yet confirmed line. Late payment interest for individuals generally is in [im-income-tax](im-income-tax.md).

## Cross-border points

### Treaty relief in general

R221 relief applies only where the relevant agreement gives relief from Manx tax on pension income arising in the Island; a foreign address alone is not enough (Making payments to non-residents page). Under the Ireland agreement, occupational pensions ("in consideration of past employment") are taxable only in Ireland, but private pensions are not covered and Isle of Man Government pensions stay taxable in the Island (Non-resident pensioners page). Other corridors: read the agreement itself.

### UK corridor (2018 agreement, SI 2018/1347)

HMRC lists the 2018 agreement as in force (it entered into force on 19 December 2018) and the 1955 arrangement, 2013 exchange of letters and 2016 protocol as terminated (HMRC treaty collection).

- **Residence (Article 4).** A resident is a person liable to tax by reason of domicile, residence, place of management, incorporation or a similar criterion; liability on source income only does not count (Art. 4(1)). For an individual resident in both: permanent home; if a home in both, centre of vital interests; if that cannot be determined or there is no home in either, habitual abode; if habitual abode in both or neither, mutual agreement (Art. 4(2)). There is no nationality step.
- **Pensions (Article 17).** Pensions and similar remuneration paid to a resident of one territory are taxable only in that territory, subject to Article 18. So a Manx occupational, personal or group personal pension paid to a UK treaty resident is taxable only in the UK once the R221 claim is accepted (Non-resident pensioners page). The UK taxable amount is a separate calculation.
- **Government service (Article 18).** Remuneration, including pensions, paid by one government for services in the discharge of governmental functions is exempt in the other territory if the individual is not ordinarily resident there, or (for remuneration other than a pension) is ordinarily resident there solely to render those services. This does not apply to services connected with a government trade or business carried on for profit. The Division applies the pension article to Isle of Man Government pensions paid to individuals resident and ordinarily resident in the UK (Non-resident pensioners page).
- **Employment (Article 14).** Employment income may be taxed where the employment is exercised (Art. 14(1)). It is taxable only in the residence territory if **all three** conditions hold: presence in the work territory not exceeding 183 days in aggregate in any twelve-month period starting or ending in the fiscal year; paid by or for an employer not resident in the work territory; not borne by the employer's permanent establishment there (Art. 14(2)). Exactly 183 days meets the presence limb. Employment aboard a ship or aircraft in international traffic (other than solely within the other territory) is taxable only in the residence territory (Art. 14(3)). The Division's own summary of Article 14 on its double taxation relief page reads the conditions as alternatives; the treaty text, which joins them with "and", governs.
- **Directors (Article 15).** Directors' fees paid by a company resident in the other territory may be taxed there.
- **Offshore activities (Article 21)** override the other articles for seabed exploration and exploitation; review them separately.
- **Entitlement (Article 23).** A benefit is denied where obtaining it was one of the principal purposes of an arrangement, unless granting it accords with the object and purpose of the provision; the competent authority may still grant it on request after considering the facts (Art. 23(1), (2)).
- **Mutual agreement (Article 25).** A person may present a case to either competent authority within three years from the first notification of the action giving rise to taxation not in accordance with the agreement, whatever the domestic remedies (Art. 25(1)). Keep domestic appeal deadlines running in parallel. The 2024 memorandum of understanding sets the arbitration process under Article 25: a written request identifying the case, with a statement from each person directly affected that no court or tribunal decision has been given on the same issues (Part 1), and minimum information covering identity, the treaty provisions at issue, facts, analysis and parallel requests (Part 2).

## Worked examples

### Example 1: non-resident landlord, deduction against final liability

A UK-resident individual owns a Douglas flat let through a Manx letting agent for 2026/27. Gross rent is GBP 24,000. Under an N15 notice the agent deducts 21% from each payment, GBP 5,040 in the year, remits it with N35 cards and issues N13 certificates. After expenses, taxable rental income is established at GBP 18,000. Tax at 21% with no allowance is GBP 3,780, so GBP 1,260 of the tax deducted is repayable on the non-resident return due 6 October 2027. (Article 6 of the UK treaty lets the Island tax the rent first.)

```oa-check
name: IM non-resident landlord, deduction vs liability (2026/27)
inputs:
  gross_rent: 24000
  taxable_rent: 18000
  rate: 21
steps:
  - deducted: pct(gross_rent, rate)
  - liability: pct(taxable_rent, rate)
  - repayable: deducted - liability
expected:
  deducted: 5040.00
  liability: 3780.00
  repayable: 1260.00
```

### Example 2: excluded income and the section 11A limit

The same landlord also receives GBP 3,000 of deposit interest from a licensed Manx bank and GBP 5,000 of dividends from a Manx company, with no tax deducted from either. Without section 11A the tax would be 21% of GBP 26,000, GBP 5,460. The limit is the tax on income reduced by excluded income (21% of GBP 18,000, GBP 3,780) plus tax deducted from excluded income (nil). Tax payable is the lower amount, GBP 3,780: the interest and dividends add no tax.

```oa-check
name: IM non-resident, s.11A limit with excluded income (2026/27)
inputs:
  taxable_rent: 18000
  bank_interest: 3000
  dividends: 5000
  tax_deducted_excluded: 0
  rate: 21
steps:
  - tax_without_limit: pct(taxable_rent + bank_interest + dividends, rate)
  - limit: pct(taxable_rent, rate) + tax_deducted_excluded
  - tax_payable: min(tax_without_limit, limit)
expected:
  tax_without_limit: 5460.00
  limit: 3780.00
  tax_payable: 3780.00
```

## Ask the client first

1. On what date did you stop being resident in the Island (or have you never been resident), and where are you resident now?
2. What Manx income do you receive (rent, pensions, employment, interest, dividends), from which payer, and what has been deducted?
3. Which N15 notices, N13 certificates, R221 applications or clearances do you or your payer hold?
4. For employment: where are the duties performed, how many days were you in the Island in each twelve-month period, and who pays and bears your salary?
5. For a pension: is it occupational, private or government, and has your new tax authority confirmed your residence on the R221?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act 1970 (AT 3 of 1970), consolidated text [62], ss.1(3), 1(3A), 11A, 35C, 35D | https://legislation.gov.im/cms/images/LEGISLATION/PRINCIPAL/1970/1970-0003/1970-0003_62.pdf | 2026-10-30 |
| Income Tax Division, Rates and allowances (current and historic) | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/rates-and-allowances/ | 2026-10-30 |
| Income Tax Division, Budget 2026 | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/budget/ | 2026-10-30 |
| Practice Note PN 227/26, Budget 2026 proposals | https://www.gov.im/media/1391759/pn-227-26-budget.pdf | 2026-10-30 |
| Income Tax Division, Receiving Isle of Man source income | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/non-residents/receiving-isle-of-man-source-income/ | 2026-10-30 |
| Income Tax Division, Making payments to non-residents | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/non-residents/making-payments-to-non-residents/ | 2026-10-30 |
| Income Tax Division, Non-resident pensioners | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/personal-tax/non-residents/non-resident-pensioners/ | 2026-10-30 |
| Income Tax Division, Leaving the Island | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/leaving-the-island/ | 2026-10-30 |
| Income Tax Division, Non-resident employees | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/employers/further-information-for-employers/non-resident-employees/ | 2026-10-30 |
| Income Tax Division, International agreements and double taxation relief | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/international-agreements-and-double-taxation-relief/ | 2026-10-30 |
| Practice Note PN 130/06, Taxation of non-resident individuals (historic rates) | https://www.gov.im/media/511796/pn13006.pdf | 2026-10-30 |
| HMRC, Isle of Man tax treaties | https://www.gov.uk/government/publications/isle-of-man-tax-treaties | 2026-10-30 |
| UK-Isle of Man Double Taxation Agreement 2018, SI 2018/1347, Articles 4, 6, 14, 15, 17, 18, 21, 23, 25 | https://www.legislation.gov.uk/uksi/2018/1347/pdfs/uksi_20181347_en.pdf | 2026-10-30 |
| HMRC, 2024 UK-Isle of Man memorandum of understanding (arbitration), Parts 1 and 2 | https://www.gov.uk/government/publications/isle-of-man-tax-treaties/2024-uk-isle-of-man-memorandum-of-understanding-in-force | 2026-10-30 |

Not yet confirmed: the payment date of a non-resident assessment; any further penalty after the GBP 100 for a non-resident return; penalties on payers who fail to deduct or remit; which expenses are allowable against non-resident rental income; electronic filing routes for N35 and N37; relief under treaties other than the UK and Ireland; foreign tax credits and permanent-establishment rules for non-resident individuals trading in the Island.

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
