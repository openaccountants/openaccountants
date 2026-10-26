---
name: uk-non-dom
description: "How the UK taxes the foreign income and gains of people who used to be non-doms, and of new arrivals, for tax year 2026/27 (6 April 2026 to 5 April 2027), after Finance Act 2025 ended the remittance basis. Covers the 4-year foreign income and gains (FIG) regime for people who were non-resident for 10 years, how to claim it and what the claim costs (personal allowance, CGT annual exempt amount, foreign losses), Overseas Workday Relief, the Temporary Repatriation Facility (12% for 2025/26 and 2026/27, 15% for 2027/28), rebasing to 5 April 2017, and the inheritance tax long-term UK resident test (10 of 20 years) with its tail. Trigger on: UK non-dom, remittance basis abolished, FIG regime, 4-year exemption, TRF, temporary repatriation facility, 2017 rebasing, long-term UK resident, IHT tail, overseas workday relief. Out of scope: deciding residence (uk-statutory-residence-test), non-resident returns (uk-non-resident-sa109), foreign tax credit relief (uk-foreign-tax-and-withholding), non-UK trusts."
version: 1.1
jurisdiction: GB
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - uk-income-tax-sa100
  - uk-statutory-residence-test
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK non-doms after April 2025: the 4-year FIG regime, the TRF, rebasing and IHT (2026/27)

## Who this applies to

- **What ended.** Finance Act 2025 Schedule 9 ended the remittance basis. HMRC: "On 6 April 2025 the 4-year foreign income and gains regime replaced the remittance basis" and "the 2024 to 2025 tax year was the last year for which the remittance basis could be claimed, or could apply automatically" (HS264). Domicile no longer matters for income tax or CGT. Every UK resident is taxed on worldwide income and gains as they arise, unless a FIG claim is made.
- **Residence comes first.** Every rule here turns on UK residence under the statutory residence test (Finance Act 2013 Schedule 45). Use `uk-statutory-residence-test` for each year in the look-back. For the FIG test, a split year and a year in which a treaty makes the person resident elsewhere still count as UK resident years (RFIG44000). A look-back reaching 2012/13 or earlier uses the pre-SRT rules: refer it.
- **The 4-year FIG regime (ITTOIA 2005 s845B).** A person is a qualifying new resident for a tax year if they are UK resident, not disqualified (a member of the House of Commons or Lords for any part of the year), were not UK resident in each of the 10 tax years before it, and are at least 10 years old at its start (the age test was added by Finance Act 2026). They also qualify in each of the next three tax years in which they are UK resident and not disqualified. The 10 years count back from the first qualifying year, not from the year of claim.
- **Arrivals before the reform.** 2022/23, 2023/24 or 2024/25 count as a first qualifying year if the test would have been met then (s845B(3)(c)), but no claim can be made for those years. For 2026/27: a 2024/25 arrival is in year 3, a 2023/24 arrival is in year 4, a 2022/23 arrival has no year left.
- **Edges.** Exactly 10 non-resident years is enough; nine is not, for any year of that stay. A non-resident year inside the window is lost and not replaced: a person cannot "roll that year over to a later year of UK residence" (RFIG44000). Nationality and domicile do not matter: a returning Briton with 10 years away qualifies. A year as a member of Parliament counts as UK resident and breaks the run.
- **The TRF** is for anyone UK resident in the year of designation who used the remittance basis for at least one year before 2025/26 (FA 2025 Sch 10 para 1(5) and (7)).
- **Rebasing** is for former remittance basis claimants who meet five conditions (FA 2025 Sch 11 para 1; see the taxable base).
- **Inheritance tax.** From 6 April 2025 the long-term UK resident test in IHTA 1984 s6A replaced domicile and deemed domicile. A long-term UK resident is within IHT on worldwide assets. Transfers and deaths before 6 April 2025 follow the old domicile rules.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| FIG regime: non-resident years needed before the first qualifying year | 10 consecutive tax years | 2025/26 on | https://www.legislation.gov.uk/ukpga/2005/5/section/845B |
| FIG regime: length | First qualifying year plus the next 3 tax years | 2025/26 on | https://www.legislation.gov.uk/ukpga/2005/5/section/845B |
| FIG regime: minimum age at 6 April | 10 | 2025/26 on | https://www.legislation.gov.uk/ukpga/2005/5/section/845B |
| FIG claim deadline | 12 months from 31 January after the tax year (31 January 2029 for 2026/27) | 2026/27 | https://www.legislation.gov.uk/ukpga/2005/5/section/845A |
| Overseas Workday Relief limit per qualifying year | Lower of 30% of qualifying employment income or £300,000 | 2025/26 on | https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43600 |
| TRF charge, designated in 2025/26 or 2026/27 return | 12% | 2025/26, 2026/27 | https://www.legislation.gov.uk/ukpga/2025/8/schedule/10 |
| TRF charge, designated in 2027/28 return | 15% | 2027/28 | https://www.legislation.gov.uk/ukpga/2025/8/schedule/10 |
| TRF designation election deadline | 12 months from 31 January after the tax year (31 January 2029 for 2026/27) | 2026/27 | https://www.legislation.gov.uk/ukpga/2025/8/schedule/10 |
| Rebasing date | Market value on 5 April 2017 | disposals from 6 April 2025 | https://www.legislation.gov.uk/ukpga/2025/8/schedule/11 |
| IHT long-term UK resident | UK resident in at least 10 of the previous 20 tax years | 2025/26 on | https://www.legislation.gov.uk/ukpga/1984/51/section/6A |
| IHT tail: consecutive non-resident years to fall out | 3 (13 or fewer resident years), then one more per resident year: 14 needs 4, up to 20 needs 10 | 2025/26 on | https://www.legislation.gov.uk/ukpga/1984/51/section/6A |
| Personal allowance (lost on a FIG claim or OWR election) | £12,570 | 2026/27 | https://www.legislation.gov.uk/ukpga/2007/3/section/35 |
| Basic rate limit | £37,700 at 20%; higher rate 40%; additional rate 45% over £125,140 | 2026/27 | https://www.legislation.gov.uk/ukpga/2007/3/section/10 |
| Remittance basis charge (£30,000 / £60,000 up to 2024/25) | Abolished; no charge | 2025/26 on | https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm32210 |

The TRF rates are set by FA 2025 Sch 10 para 1(8): "12% of the amount of that capital" for 2025/26 or 2026/27, and "15%" for 2027/28. There is no TRF after 2027/28.

## The taxable base

**What a FIG claim relieves.** Qualifying foreign income (ITTOIA 2005 s845H) that arises on or after 6 April 2025: profits of a trade carried on wholly outside the UK, overseas property profits, foreign interest, dividends from non-UK companies, most foreign pensions, royalties and offshore income gains. Foreign gains are relieved by a separate foreign gain claim (TCGA 1992 Schedule D1). Not covered: UK income and gains, foreign employment income (use OWR), and any FIG that arose before 6 April 2025, "whether or not he remits them" in the window (RFIG44000).

**How the claim works (s845A).** It must be made in a return, source by source, and quantified. The relief is deducted at Step 2 of ITA 2007 s23, and only from qualifying foreign income (s845A(3A), added by Finance Act 2026). A smaller claim relieves only the amount claimed. A wrongly quantified claim is still valid; an unquantified one is not (RFIG42100). There is no cap and no automatic relief. Relieved amounts can be brought to the UK at any time without further UK tax. Each year needs its own claim.

**What a claim costs.** A foreign income claim, a foreign gain claim or an OWR election for a year removes, for that year (ITTOIA ss845C to 845G, s845E for the allowances; TCGA s1K; RFIG43000; GOV.UK "Allowances you'll lose"):
- the personal allowance, blind person's allowance, married couple's allowance, marriage allowance and life insurance relief;
- the CGT annual exempt amount;
- foreign losses of that year, which stop being allowable;
- relief for losses of a trade or property business carried on wholly outside the UK, in that year or any other (s845C);
- the overseas property finance cost reduction under s274A, and its carry forward becomes nil (s845D).

The cost applies even when the claim covers one small source. Brought-forward overseas losses are used against that business before the relief. Adjusted net income for the child benefit charge and tax-free childcare still counts all foreign income. A foreign income claim also cuts the maximum pension contribution relief by the relieved foreign income that counts as relevant UK earnings, but never below the £3,600 basic amount (s845F(2); FA 2004 s190(4)). UK losses are unaffected.

**Overseas Workday Relief (ITEPA 2003 Part 2 Chapter 5C).** A qualifying new resident employee can elect and claim relief on the part of employment income for duties performed outside the UK. No FIG claim is needed and the money no longer has to stay offshore. The limit for each qualifying year is the lower of 30% of the qualifying employment income or £300,000, counted across all years in which that year's earnings are taxed, such as a later bonus (EIM43600). Earnings taxed before the employment year cannot use it. Transitional rules (EIM43605): an arrival in 2023/24 or 2024/25 who used OWR on the remittance basis gets OWR without the limit for years ending before 6 April 2028; a 2022/23 arrival who used OWR gets none for 2025/26. Earnings for remittance basis years keep the old OWR rules.

**Old money: pre-6 April 2025 FIG.** FIG that arose to a remittance basis user before 6 April 2025 "will continue to be taxed at the usual tax rates if they are remitted to the UK on or after 6 April 2025, unless these amounts are designated under the temporary repatriation facility" (HS264). The old remittance rules still decide what a remittance is (money or assets brought in, used for UK services or debts, benefits to relevant persons such as a spouse, minor children and close companies), and mixed fund ordering still applies. Remitted foreign dividends are taxed at the normal rates, not the dividend rates, with no dividend allowance. Business investment relief claims end after 5 April 2028.

**The TRF (FA 2025 Sch 10).** "Qualifying overseas capital" can be designated in the 2025/26, 2026/27 or 2027/28 return: pre-6 April 2025 FIG, amounts of uncertain origin in a mixed fund, capital payments and benefits from non-UK trusts matched to pre-2025 FIG, and assets derived from such FIG. Partial designation is allowed and nothing has to be brought in. Once the charge is paid the capital can be remitted later without further tax, and designated capital comes out of a mixed fund first. The charge is "charged as if they were amounts of income tax" (para 9), but HMRC treats it as a charge on capital: no foreign tax credit, no effect on adjusted net income, bands or payments on account, and earlier remittance basis charges cannot be set against it (RDRM73400). Foreign income is converted at the rate on 6 April of the designation year (6 April 2026 for 2026/27); foreign gains at the rate on disposal (HS264). Money taken from offshore to pay the charge is itself a remittance unless designated.

**Rebasing to 5 April 2017 (FA 2025 Sch 11 para 1).** On a disposal on or after 6 April 2025 the gain is computed from market value on 5 April 2017 if all of these hold: the asset was held on 5 April 2017; it "was not situated in the United Kingdom at any time in the period beginning with 6 March 2024 and ending with 5 April 2025"; the person was never UK domiciled (including deemed domicile under ITA 2007 s835BA) before 2025/26; and they made a remittance basis claim under ITA s809B for at least one year from 2017/18 to 2024/25 in which the remittance basis did not apply automatically. It applies despite the spouse no-gain/no-loss rule and follows share reorganisations. Para 2 carves out assets in the UK only for public access, repairs or sale, personal clothing, footwear, jewellery or watches, the under-£1,000 notional remittance rule, or temporary importation. Para 3: the person can elect out for a disposal, and the election "is irrevocable". Elect out when original cost beats the 2017 value. Para 4 amends the separate 2017 rebasing for deemed domiciliaries (refer). Rebasing changes only the base cost; the gain is taxed as it arises.

**Inheritance tax (IHTA 1984 s6A).** Long-term UK resident "at all times in a tax year if they were UK resident for at least 10 of the previous 20 tax years". Not long-term resident after 10 consecutive non-resident years in the previous 19, or after the "required number" of consecutive non-resident years ending last year. Count the resident years in the 20 tax years ending with the last resident year: 13 or fewer needs 3, 14 needs 4, and so on to 20, which needs 10. After 10 years away the count resets. HMRC transitional rules: someone without UK domicile or deemed domicile on 30 October 2024, non-resident for 2025/26 and not returning, is not long-term resident; someone deemed domiciled on 30 October 2024 who leaves the same way drops out after 3 years. Section 6B modifies the test for young persons; ss267ZC to 267ZE allow an election in. Any IHT computation is a refer case.

**Trusts (pointer only).** Overseas assets in a trust the person set up or added to are within IHT "even when you were not a long-term UK resident", except trust assets placed in trust while non-UK domiciled that were overseas on 30 October 2024 and at death (GOV.UK). Settlor and beneficiary charges, capital payment matching, transfer of assets abroad and TRF designation of trust amounts are refer cases. Tell trustees when long-term residence status changes.

## Deadlines and filing

- **Return.** SA100 with the SA109 "Residence and foreign income and gains (FIG) regime etc" pages for the FIG claim, the OWR election and claim, and the TRF election; SA106 for foreign income; SA108 for gains. MTD for Income Tax users claim through their software (HS264).
- **2026/27 dates.** Register for Self Assessment by 5 October 2027. Paper return by 31 October 2027, online return and balancing payment by 31 January 2028, second payment on account 31 July 2028 (GOV.UK deadlines pattern; that page currently shows the 2025/26 dates).
- **FIG claim and TRF designation for 2026/27:** in the return or an amendment, by 31 January 2029 (s845A(5); Sch 10 para 8(1)). Each can be amended in the same window. Outside it a designation cannot be withdrawn and there is no repayment if the money is later spent abroad. Late claims only under HMRC's general late claims policy. No consequential claim after careless or deliberate loss of tax (s845A(6)).
- **TRF boxes.** HS264 lists SA109 box 50 (election), 51 (total designated, excluding trust amounts), 52 (trust capital payments and benefits) and 54 (other information) on the 2025/26 return. Entries in sterling.
- **Rebasing election out:** TMA 1970 ss42 and 43 claim procedure (Sch 11 para 3(2)).
- **2025/26 returns being filed now:** online return and payment by 31 January 2027; FIG claim and TRF designation (12%) until 31 January 2028.
- **Records.** Keep records of designated capital, the charge paid and workday evidence. TRF records count as records needed for a correct return (Sch 10 para 9(7)).

## Penalties and interest

- The TRF charge is collected and penalised like income tax (Sch 10 para 9(4)). FIG and OWR errors are income tax errors.
- **Late filing:** £100; after 3 months £10 a day up to £900; after 6 months 5% of the tax due or £300, whichever is greater; after 12 months another 5% or £300 (GOV.UK, Self Assessment penalties).
- **Late payment:** 5% of the tax unpaid at 30 days, 6 months and 12 months (GOV.UK).
- **Interest:** late payment interest is base rate plus 4% from 6 April 2025; 7.75% from 9 January 2026 (HMRC interest rates page).
- **Inaccuracy:** a wrong FIG claim or TRF designation in a return is an inaccuracy under FA 2007 Schedule 24.

## Cross-border points

- **Treaties.** A FIG claim does not change treaty residence (RFIG43000). A treaty-resident-elsewhere year still breaks the 10-year run. HMRC treats the TRF charge as outside treaties covering income and gains, so no foreign tax credit against it (RDRM73400). Use `uk-foreign-tax-and-withholding` for credit relief.
- **Claim or credit.** If foreign tax already matches the UK rate, a FIG claim may only cost the allowances. Compare the claim with the arising basis plus foreign tax credit, year by year.
- **Leaving.** Temporary non-residence does not bite on a leaver inside the first 4 years, because they are not resident for 4 of the 7 years before departure (RFIG44000). IHT follows the person for the tail years after leaving.
- **Arriving in a split year.** The split year counts as a full UK resident year for the FIG test and starts the window (RFIG44000). This matches `uk-statutory-residence-test`.

## Worked examples

### Example 1: a new arrival, FIG claim or not

Leila was not UK resident in any of the 10 tax years to 2025/26 and is UK resident from 6 April 2026, outside Scotland. In 2026/27 she has a UK salary of £60,000 and overseas rental profit of £40,000, with no foreign tax. She is a qualifying new resident for 2026/27.

- **No claim.** Total income £100,000; her personal allowance is not tapered (income is not above £100,000). Taxable £87,430. Tax: £37,700 at 20% = £7,540; £49,730 at 40% = £19,892. Total £27,432.
- **FIG claim on the £40,000.** The rental profit is deducted. She loses the personal allowance. Taxable £60,000: £7,540 + £22,300 at 40% = £8,920. Total £16,460.
- **Saving £10,972.** She also loses the CGT annual exempt amount for the year; if she has UK gains, add that cost. Claim by 31 January 2029.

```oa-check
name: Qualifying new resident, salary 60,000 and foreign rent 40,000, claim vs no claim (2026/27)
inputs:
  uk_salary: 60000
  foreign_rent: 40000
  personal_allowance: 12570
  basic_band: 37700
steps:
  - taxable_no_claim: uk_salary + foreign_rent - personal_allowance
  - tax_no_claim: min(taxable_no_claim, basic_band) * 0.20 + max(taxable_no_claim - basic_band, 0) * 0.40
  - taxable_claim: uk_salary
  - tax_claim: min(taxable_claim, basic_band) * 0.20 + max(taxable_claim - basic_band, 0) * 0.40
  - saving: tax_no_claim - tax_claim
expected:
  taxable_no_claim: 87430
  tax_no_claim: 27432
  tax_claim: 16460
  saving: 10972
```

### Example 2: TRF timing, 2026/27 against 2027/28 against no designation

Nida used the remittance basis up to 2024/25. She holds £30,000 of 2022/23 foreign income offshore and is UK resident in 2026/27. She is an additional rate taxpayer.

- **Designate in the 2026/27 return:** 12% of £30,000 = £3,600 (HMRC's own figure in RDRM73400). Election by 31 January 2029.
- **Wait for 2027/28:** 15% = £4,500. The delay costs £900.
- **Bring it in with no designation:** taxed at her usual rate, 45% = £13,500.
- **Edge.** If she pays the charge from the same offshore account, that payment is a remittance. Designating the full £30,000 covers it; paying from undesignated old FIG would be taxed at 45%.

```oa-check
name: TRF on 30,000 of pre-2025 foreign income, 12% vs 15% vs remitted at 45%
inputs:
  old_fig: 30000
steps:
  - trf_2026_27: old_fig * 0.12
  - trf_2027_28: old_fig * 0.15
  - cost_of_waiting: trf_2027_28 - trf_2026_27
  - undesignated_tax: old_fig * 0.45
  - saving_vs_undesignated: undesignated_tax - trf_2026_27
expected:
  trf_2026_27: 3600
  trf_2027_28: 4500
  cost_of_waiting: 900
  undesignated_tax: 13500
  saving_vs_undesignated: 9900
```

## Ask the client first

1. Were you UK resident (under the SRT, counting split and treaty years) in any of the 10 tax years before you arrived? In which year did your current UK residence start? Were you ever a member of Parliament?
2. Did you ever claim the remittance basis, or have it apply automatically, up to 2024/25? Which years, and was it a s809B claim? Were you ever UK domiciled or deemed domiciled?
3. How much pre-6 April 2025 foreign income and gains is still offshore, where, and can you show which year and type each amount came from? Do you plan to bring any to the UK?
4. What foreign income and gains, foreign losses and UK gains do you expect in 2026/27? Do you work both in and outside the UK, and what share of workdays is overseas?
5. Do you still hold foreign assets you owned on 5 April 2017? Was any in the UK between 6 March 2024 and 5 April 2025?
6. How many of the last 20 tax years were you UK resident? Are you a settlor or beneficiary of a non-UK trust? Are you planning to leave?

## Sources

| Source | URL | Read on |
|---|---|---|
| ITTOIA 2005 s845A (foreign income claim) | https://www.legislation.gov.uk/ukpga/2005/5/section/845A | 2026-10-26 |
| ITTOIA 2005 s845B (qualifying new resident) | https://www.legislation.gov.uk/ukpga/2005/5/section/845B | 2026-10-26 |
| ITTOIA 2005 s845C (losses) | https://www.legislation.gov.uk/ukpga/2005/5/section/845C | 2026-10-26 |
| ITTOIA 2005 s845E (allowances lost) | https://www.legislation.gov.uk/ukpga/2005/5/section/845E | 2026-10-26 |
| ITTOIA 2005 s845F (pension relief) | https://www.legislation.gov.uk/ukpga/2005/5/section/845F | 2026-10-26 |
| Finance Act 2004 s190 (basic amount £3,600) | https://www.legislation.gov.uk/ukpga/2004/12/section/190 | 2026-10-26 |
| Finance Act 2025, contents (s37 and Sch 9 end of remittance basis) | https://www.legislation.gov.uk/ukpga/2025/8/contents | 2026-10-26 |
| Finance Act 2025 Sch 10 (temporary repatriation facility) | https://www.legislation.gov.uk/ukpga/2025/8/schedule/10 | 2026-10-26 |
| Finance Act 2025 Sch 11 (rebasing) | https://www.legislation.gov.uk/ukpga/2025/8/schedule/11 | 2026-10-26 |
| IHTA 1984 s6A (long-term UK resident) | https://www.legislation.gov.uk/ukpga/1984/51/section/6A | 2026-10-26 |
| ITA 2007 s10 (basic rate limit) | https://www.legislation.gov.uk/ukpga/2007/3/section/10 | 2026-10-24 |
| ITA 2007 s35 (personal allowance) | https://www.legislation.gov.uk/ukpga/2007/3/section/35 | 2026-10-24 |
| GOV.UK, Income Tax rates and allowances | https://www.gov.uk/income-tax-rates | 2026-10-24 |
| GOV.UK, Check if you can claim the 4-year FIG regime | https://www.gov.uk/guidance/check-if-you-can-claim-the-4-year-foreign-income-and-gains-regime | 2026-10-24 |
| GOV.UK, IHT if you're a long-term UK resident | https://www.gov.uk/guidance/inheritance-tax-if-youre-a-long-term-uk-resident | 2026-10-26 |
| HMRC HS264, remittance of pre-2025 FIG and the TRF | https://www.gov.uk/government/publications/remittance-basis-hs264-self-assessment-helpsheet/hs264-remittance-of-pre-6-april-2025-foreign-income-and-gains-and-the-temporary-repatriation-facility-trf | 2026-10-26 |
| HMRC RDRM73400 (TRF charge) | https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73400 | 2026-10-26 |
| HMRC RFIG44000 (qualifying new residents) | https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000 | 2026-10-26 |
| HMRC RFIG43000 (effect of a claim) | https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig43000 | 2026-10-26 |
| HMRC EIM43600 (OWR financial limit) | https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43600 | 2026-10-26 |
| GOV.UK, Self Assessment deadlines | https://www.gov.uk/self-assessment-tax-returns/deadlines | 2026-10-24 |
| GOV.UK, Self Assessment penalties | https://www.gov.uk/self-assessment-tax-returns/penalties | 2026-10-24 |
| HMRC interest rates for late and early payments | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-10-24 |

Not yet confirmed: the 2026/27 SA109 box numbers for the TRF and FIG claims; the 2026/27 Self Assessment dates as printed by GOV.UK (pattern applied); the OWR transitional table (EIM43605), the RFIG42100 quantification rule and the business investment relief end date, carried from version 1.0 but not re-read today; the remittance basis charge figures (RDRM32210) and deemed domicile Conditions A and B (ITA s835BA), kept as history only; the OWR claim time limit; the commencement of the age-10 test for 2025/26.

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
