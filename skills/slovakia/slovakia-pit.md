---
name: slovakia-pit
description: "Slovak personal income tax (daň z príjmov fyzickej osoby, DPFO) for tax year 2026 under Act 595/2003 as amended by Act 261/2025. Covers residents and non-residents in outline, employment income (§5), self-employed SZČO business income (§6) with the 60% flat-rate expenses capped at EUR 20,000, the 15% rate for business revenue up to EUR 100,000, the new 19%, 25%, 30% and 35% bands set as multiples of the subsistence minimum (EUR 284.13), the 2026 personal allowance of EUR 5,966.73 and its phase-out, the spouse allowance, the child tax bonus and its taper above EUR 27,432, the EUR 17 minimum tax rule, capital income, the 31 March 2027 deadline and extensions, advances and penalties. Trigger on: daň z príjmov 2026, DPFO typ A, DPFO typ B, SZČO, živnostník, paušálne výdavky, nezdaniteľná časť, daňový bonus, Slovak income tax 2026. Out of scope: payroll withholding and contributions in sk-payroll-social, companies in sk-corporate-income-tax, non-residents and treaties in sk-cross-border."
version: 1.7
jurisdiction: SK
tax_year: 2026
last_updated: 2026-10-29
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - foundation
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovakia: personal income tax for employees and the self-employed (2026) v1.7

Source-cited draft: not reviewed by an accountant, not for filing. Built by Michael Cutajar and the OpenAccountants team.

This skill covers the annual income tax of an individual for the 2026 calendar year: employees, the self-employed (SZČO, živnostník) and people with rental, capital or other income. It links to the other Slovakia skills and does not repeat them:

- [sk-payroll-social](sk-payroll-social.md): the employer's monthly withholding and social and health contributions.
- [sk-corporate-income-tax](sk-corporate-income-tax.md): companies, including the minimum tax for legal persons.
- [sk-tax-overview](sk-tax-overview.md): the system at a glance.
- [sk-cross-border](sk-cross-border.md): residence in detail, non-residents, withholding tax and treaties.

**Which text of the law.** Act No. 595/2003 Coll. on income tax (zákon o dani z príjmov), version in force from 1 January 2026 to 30 December 2026. Act No. 261/2025 Coll. made the 2026 changes to §11 and §15; under §52zzzj(1) they apply first for the 2026 tax year. A further version in force from 31 December 2026 adds an exemption for informal carers (§9(1)(t)) and amends §11(4), but §52zzzm says those apply first for 2027. Penalties come from Act No. 563/2009 Coll., the Tax Procedure Code (daňový poriadok).

## Who this applies to

- **Residents.** A person with permanent residence (trvalý pobyt) or a home (bydlisko) in Slovakia, or who usually stays there, is taxed on worldwide income (§2(d)(1)). Staying at least 183 days in a calendar year, counting every started day, is usually staying. The tax year is the calendar year (§2(l)).
- **Non-residents.** They are taxed only on Slovak-source income (§2(e), §16). They get the spouse allowance and the child bonus only if Slovak income is at least 90% of their total income (§11(7), §33(9)). The detail is in sk-cross-border.
- **Employees** (§5). The employer withholds monthly advances. An employee with only §5 income from Slovak employers can ask an employer for the annual settlement (ročné zúčtovanie) by 15 February 2027 if they are not required to increase the tax base under §11(11) for earlier DDS deductions (§38(1)). Otherwise they file DPFO type A.
- **Self-employed** (§6(1) and (2)): trades (živnosť), liberal professions, farmers and other independent activity. They file DPFO type B.
- **Rental income** (§6(3)), **capital income** (§7) and **other income** (§8), such as sale of property, securities or crypto-assets. These go on DPFO type B.
- **Who must file.** Anyone whose taxable income in 2026 exceeds 50% of the personal allowance, so EUR 2,983.37, or who has a tax loss (§32(1)). Income taxed finally by withholding is left out of that test.
- **Out of scope.** Companies, and the special tax on top state officials (§15a).

## Rates, bands and thresholds

The bands and allowances are multiples of the subsistence minimum (životné minimum) in force on 1 January of the tax year (§11(2)(a)). For 2026 that is EUR 284.13 a month, set from 1 July 2025 by Measure No. 168/2025 Coll. Amounts below are that figure times the multiple, rounded to the cent (§47).

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Subsistence minimum, one adult, used for 2026 | EUR 284.13 a month | 2026 | https://employment.gov.sk/sk/rodina-socialna-pomoc/hmotna-nudza/zivotne-minimum/vyska-zivotneho-minima-od-1-jula-2025.html |
| Band 1: base up to 154.8 x subsistence minimum (EUR 43,983.32) | 19% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§15(a)(1a)) |
| Band 2: EUR 43,983.32 to 212.4 x (EUR 60,349.21) | 25% | 2026 | same, §15(a)(1b) |
| Band 3: EUR 60,349.21 to 264 x (EUR 75,010.32) | 30% | 2026 | same, §15(a)(1c) |
| Band 4: above EUR 75,010.32 | 35% | 2026 | same, §15(a)(1d) |
| Business base (§6(1),(2)) when that business revenue is EUR 100,000 or less | 15% | 2026 | same, §15(a)(2) |
| Business base when that business revenue exceeds EUR 100,000 | 19% / 25% / 30% / 35% bands as above | 2026 | same, §15(a)(3) |
| Ordinary capital income special base (§7), for example foreign bank interest; government-bond exception below | 19% | 2026 | same, §15(a)(4) |
| Non-exempt Slovak/EU/EEA government-bond and treasury-bill yields, gross special base (§51ea) | 13%; qualifying retail-government-bond yields and sales exempt under §9(1)(r), unless the bonds are or were business assets | 2026 | [ITA §15(a)(7), §51ea, §9(1)(r), §52zzzc](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html) |
| Foreign dividends special base (§51e) | 7% for profit periods beginning in 2017–2023 or from 1 January 2025; 10% for periods beginning in 2024; 35% non-cooperating-state rule separately applies | Paid in 2026; rate follows profit period | [ITA §15(a)(5),(6), §52zi(5), §52zzz(4), §52zzzb(5)](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html) |
| Personal allowance (21.0 x), base up to 91.8 x (EUR 26,083.13) | EUR 5,966.73 | 2026 | same, §11(2)(a) |
| Personal allowance, base above EUR 26,083.13 | EUR 14,661.11 (51.6 x) minus one third of the base; zero from a base of EUR 43,983.32 | 2026 | same, §11(2)(b) |
| Spouse allowance (19.2 x), taxpayer base up to EUR 43,983.32 | up to EUR 5,455.30, less the spouse's own income | 2026 | same, §11(3)(a) |
| Spouse allowance, taxpayer base above EUR 43,983.32 | EUR 20,116.40 (70.8 x) minus one third of the base, less the spouse's own income | 2026 | same, §11(3)(b) |
| Supplementary pension (DDS) and PEPP contributions | Own contributions actually paid, up to EUR 180 combined a year, subject to the contract and withdrawal conditions below | 2026 | same, §11(8)–(11) |
| Flat-rate expenses for a non-VAT payer (paušálne výdavky) | 60% of business revenue, cap EUR 20,000, plus compulsory contributions paid | 2026 | same, §6(10) |
| Child tax bonus, through the month of the 15th birthday | EUR 100 a month | 2026 | same, §33(1)(b) |
| Child tax bonus, after the 15th-birthday month through the 18th-birthday month | EUR 50 a month | 2026 | same, §33(1)(a) |
| Child tax bonus cap, as % of the employment or business base | 29% (1 child), 36% (2), 43% (3), 50% (4), 57% (5), 64% (6 or more) | 2026 | same, §33(6) |
| Child tax bonus taper threshold: 1.5 x 12 x average monthly wage of 2024 (EUR 1,524) | EUR 27,432; above it the bonus per child falls by 1/10 of the excess | 2026 | same, §33(11); wage: https://www.employment.gov.sk/files/slovensky/ministerstvo/analyticke-centrum/2025/sprava_sossr_2024_pub.pdf |
| Mortgage interest credit, contracts made by 31 December 2023 | 50% of eligible interest on at most EUR 50,000 of loan principal; annual cap EUR 400; reference-income multiple 1.3 | Continuing eligible five-year claims in 2026 | [Historical ITA §33a](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20230801.html), [current §52zzy(1)](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html) |
| Mortgage interest credit, contracts made after 31 December 2023 | 50% of eligible interest; annual cap EUR 1,200; reference-income multiple 1.6; first/last-year caps prorated | 2026 | [ITA §33a, §52zzy(2)](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html) |
| Minimum tax of an individual | no tax assessed if the tax is EUR 17 or less, or total income is EUR 2,983.37 or less; not where a child or mortgage bonus is claimed or tax was withheld | 2026 | same, §46a |
| Tax due in the return not paid | if EUR 5 or less | 2026 | same, §46 |
| Exempt: rental plus occasional income | first EUR 500 a year | 2026 | same, §9(1)(g) |
| Exempt regulated-market securities under §9(1)(k) | Both acquisition and regulated-market-admission clocks must exceed one year; business assets and the specified §9(1)(p)/§5(7)(q) noncash-share cases excluded, with §52zzz(3) transition | 2026 | [ITA §9(1)(k), §52zzz(3)](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html) |
| Advances: last known tax over EUR 5,000 up to EUR 16,600 / over EUR 16,600 | quarterly 1/4 / monthly 1/12 | 2026 | same, §34(1)-(3) |

**How the bands work.** The law sets two separate bases (§4(1)). Base (a) is employment income after allowances, plus rental and other income. Base (b) is business income after allowances and losses. Each base is taxed on its own scale in §15(a): base (a) always on the 19% to 35% bands, base (b) at 15% if business revenue is EUR 100,000 or less, otherwise on the same bands.

Tax on a base B above EUR 75,010.32 is 19% x 43,983.32 + 25% x 16,365.89 + 30% x 14,661.11 + 35% x (B - 75,010.32), which is EUR 16,846.64 plus 35% of the excess.

## The taxable base

**Employment (§5).** Gross pay including benefits in kind, minus the employee's compulsory social and health contributions (§5(8)). Pay for 2026 received by 31 January 2027 belongs to 2026 (§4(3)). Withholding and contributions are in [sk-payroll-social](sk-payroll-social.md).

**Self-employed (§6(1),(2)).** Revenue minus either:
- **actual expenses** (preukázateľné výdavky), with tax records or double-entry accounts (§6(11)); or
- **flat-rate expenses** of 60% of revenue, capped at EUR 20,000, if the person is not a VAT payer, or was one for only part of the year (§6(10)). The flat rate covers all expenses except the compulsory social and health contributions, which are deducted on top in the amount paid. The person still keeps a record of income and of inventory and receivables (§6(10), §6(11)(a),(d)).

The result is the business partial base. A tax loss can be carried forward for the five immediately following tax periods. Full-base loss relief requires micro-taxpayer status **in the deduction period**, not just revenue up to EUR 60,000. Under §2(w), the individual's taxable §6(1),(2) revenue must not exceed EUR 60,000; exclude a dependent person who carries out a controlled transaction in that period, a person declared bankrupt, entering liquidation or granted a payment plan, and a period shorter than twelve consecutive months except one shortened by death. Others can deduct at most 50% of the business base (§30(1)). Thus a EUR 10,000 base and EUR 8,000 unexpired loss allow EUR 8,000 relief for a qualifying micro-taxpayer, but only EUR 5,000 for the same-revenue trader with a controlled transaction; EUR 3,000 remains subject to the original expiry date. Exactly EUR 60,000 passes the revenue condition; EUR 60,000.01 does not ([ITA §§2(w),30](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html)).

**The 15% rate.** It turns on business revenue under §6(1) and (2), not on profit. Revenue of EUR 100,000 or less gives 15% on the whole business base. Above EUR 100,000 the whole business base goes on the bands (§15(a)(2),(3)).

**Allowances (nezdaniteľné časti, §11).** They reduce only the employment and business bases, never rental, capital or other income (§11(1)).
- The personal allowance and the spouse allowance are tested on the tax base from §5 and §6(1),(2) income. A taxpayer who at the start of 2026 receives an old-age, early, service or similar foreign pension gets no personal allowance if the pension for the year, including the 13th pension, exceeds the allowance; otherwise the allowance is cut to the difference (§11(6)).
- The spouse allowance needs a spouse living with the taxpayer who cared for a minor child, received a care allowance, was a registered jobseeker, or is disabled (§11(4)). The spouse's own income is net of their contributions. Months count only if the conditions held at the start of the month (§11(5)).
- **DDS/PEPP pension contributions:** deduct the taxpayer's own contributions demonstrably paid in the year, with one EUR 180 annual cap across the qualifying products, including qualifying equivalent foreign products (§11(8)/(9)). For DDS, the participant contract must have been concluded after 31 December 2013, or amended to cancel its benefit plan; a qualifying PEPP contract is the alternative. The taxpayer must also have no other DDS participant contract that fails that condition (§11(10)). Thus EUR 240 eligible DDS payments plus EUR 60 eligible PEPP payments give a combined EUR 180 deduction, rather than EUR 180 for each product; retaining another non-qualifying DDS contract prevents the claim. If a statutory early withdrawal is paid after earlier DDS deductions, add back the previously deducted DDS contributions to the tax base within the three tax periods after the withdrawal year (§11(11)). A 2026 early withdrawal with EUR 360 previously deducted therefore requires EUR 360 added back by the end of tax year 2029. Keep the payment records, every DDS contract/amendment, PEPP contract and past deduction/withdrawal history ([ITA §11(8)–(11)](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html#paragraf-11)).
- Allowances come off the employment base first, and only the rest comes off the business base (§11(12)).

**Rental (§6(3)) and other income (§8).** Start with the actual income and supported category-specific expenses. Under §9(1)(g), rental and §8(1)(a) occasional income share EUR 500 of annual income exemption. If they exceed that amount, include only the excess and reduce related expenses in the same taxable-income/total-income proportion. For a rental-only case with EUR 6,000 receipts, EUR 2,000 expenses and the whole EUR 500 available, taxable receipts are EUR 5,500; allowable expenses are `2,000 × 5,500 / 6,000`, approximately EUR 1,833.33, leaving approximately EUR 3,666.67 before the applicable filing-rounding steps. Full EUR 2,000 expenses cannot be deducted against the reduced receipts, and rental expenses cannot create a rental loss (§6(6)). Where qualifying §8(1)(d)–(f) option/security/share disposals also occur, §9(1)(i) applies to their proceeds less statutory disposal costs, with its business-asset and specified noncash-share exclusions; the exemptions under (g) and (i) together cannot exceed EUR 500. Do not give each category another EUR 500. Sales of property, movable things, options, securities, shares in an s.r.o. and crypto-assets (§8(1)(b)–(f),(t)) retain their actual gain/exemption rules; a loss on one type is ignored (§8(2)). The §9(1)(k) securities exemption requires more than one year since acquisition **and** more than one year between regulated-market admission and sale, excluding business assets and the specified §9(1)(p)/§5(7)(q) noncash-share cases, subject to §52zzz(3)'s acquisition-after-2023 transition. These taxable gains enter base (a) on the bands ([ITA §§6, 8, 9 and 52zzz](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html)).

**Capital income (§7).** Ordinary Slovak bank interest is taxed finally by withholding under §43 and stays out of the return (§7(3)); ordinary foreign bank interest enters the §7 special base at 19% (§15(a)(4)). Identify the instrument before applying that rule. Non-exempt yields on Slovak government bonds/treasury bills and bonds/bills issued by another EU/EEA state enter the **gross, no-expense-deduction §51ea special base at 13%** in 2026 (§15(a)(7)); the temporary 16% rate was for 2025 payments only (§52zzzc(3)). Section 43(3)(v)'s separate 13% withholding route concerns recipients not established or created for business; it is not a blanket withholding rule for individual bondholders. Qualifying Slovak retail government bonds (štátne dlhopisy pre občanov) and equivalent EU/EEA-state retail bonds have exempt yields **and sale income**, unless they are or were the taxpayer's business assets (§9(1)(r)). A non-exempt government-bond coupon of EUR 1,000 therefore gives EUR 130 tax before foreign-tax relief, ordinary foreign bank interest of EUR 1,000 gives EUR 190, and a qualifying non-business retail-bond coupon of EUR 1,000 gives zero. Do not extend the coupon special base to every bond sale ([ITA §§9,15,43,51ea,52zzzc](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html)). Dividends from a Slovak company are taxed by withholding. For ordinary foreign profit dividends, select the profit period before the rate: 7% for periods beginning in 2017–2023 and from 1 January 2025, but 10% for periods beginning in 2024, even when all are received in 2026. The 35% non-cooperating-state rule is separate (§51e, §15(a)(5),(6), §52zi(5), §52zzz(4), §52zzzb(5)). For EUR 10,000 gross, those ordinary domestic-law rates give EUR 700 or EUR 1,000 before applicable foreign-tax relief. Pre-2017 profit distributions need their historical regime and are not assigned either rate here.

**Child tax bonus (§33).** Start from the eligible dependent child living in the taxpayer's household and taxable §5 or §6(1),(2) income. Temporary absence from the household does not end eligibility. For each eligible month, the maximum is EUR 100 through the **month of the 15th birthday**, then EUR 50 through the **month of the 18th birthday**, and zero afterwards (§33(1),(2)). Ordinarily the conditions must hold at the month's start, but the birth, adoption, court-ordered substitute-care and commencement-of-continuous-vocational-preparation months count immediately (§33(5)). Only one eligible person claims for a month; parents can divide the year, with mother, father, then another eligible person taking priority if they do not agree (§33(4)).

Use the §5 and §6(1),(2) partial bases before allowances, or their sum B, for the 29%/36%/43%/50%/57%/64% cap for one/two/three/four/five/six-or-more children. If the eligible child count changes, split the cap by the number of months at each child count and sum those proportional entitlements (§33(6),(10)). Above B = EUR 27,432 in 2026, reduce each child's entitlement by one tenth of the excess; for part-year eligibility apply the corresponding eligible-month share, without creating a negative bonus (§33(5),(11)). The tax return can augment B by the other eligible household person's §5/§6(1),(2) base when the claimant lacks the base for the full bonus, using only the proportional months at whose start the other person qualified if they qualified for only part of the year. This is a credit calculation, not a transfer of taxable income; test **both the percentage cap and the high-base taper on augmented B** (§33(8)). The claimant must have at least 90% of all income from Slovak taxable sources, and so must the other person if their base is added (§33(9)). Claim the excess bonus over tax as a payout (§33(7)).

For a separate low-base case with one eligible under-15 child all year, claimant B = EUR 2,000 gives a EUR 580 cap. An eligible second parent's EUR 4,000 base raises B to EUR 6,000 and the cap to EUR 1,740, allowing the full EUR 1,200 nominal bonus; both parents must pass the 90% test. If that parent qualified for only six start-of-months, add EUR 2,000, not EUR 4,000: cap EUR 1,160. If B is EUR 4,000, one under-15 child qualifies all year and a second is born in July, the nominal total is EUR 1,800 but the changing-count cap is `4,000 × (29% × 6/12 + 36% × 6/12) = EUR 1,300`. For month boundaries with sufficient base below the taper threshold, a June 15th birthday gives `6 × 100 + 6 × 50 = EUR 900`; a June 18th birthday gives `6 × 50 = EUR 300`; a child born or adopted in June gives seven eligible months, or EUR 700 if under 15 ([ITA §33(1),(4)–(11)](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html)).

**Mortgage interest bonus (§33a): select the contract date first.** It concerns one housing-loan contract and one domestic flat or family house. Obtain the lender's eligible-interest certificate; a contract amendment is the same contract (§33a(2)). Section 52zzy(1),(2) preserves the following two branches.

| Contract date | Eligible interest and annual maximum | Income test at contract conclusion |
|---|---|---|
| By 31 December 2023 | 50% of interest attributable to at most EUR 50,000 of loan principal; maximum EUR 400 per full year. Use the lender-certified eligible portion, not automatically all interest on a larger loan. | Borrower's prior-calendar-year taxable income under the historical §33a(1)(b), divided by 12, at most 1.3 times that same year's official average monthly wage. |
| After 31 December 2023 | 50% of interest on the housing loan; maximum EUR 1,200 per full year, without the former EUR 50,000 principal restriction. The flat/house must serve exclusively the borrower's own permanent housing, alone or with close persons. | Borrower's prior-calendar-year taxable income under current §33a(1)(b), divided by 12, at most 1.6 times that same year's official average monthly wage. |

In both branches, the borrower and every co-borrower must be aged **18 through 35 inclusive at the loan application date**. The income test is fixed at contract conclusion, using the calendar year before that conclusion, not the current claim year. With co-borrowers, also test their combined average monthly income against `number of borrowers × 1.3 or 1.6 × reference wage`; only the claimant borrower receives the credit, not each co-borrower (§33a(4),(5)). Use the income categories specified in the applicable version: §§5,6,8 and special §§7,51e in the historical branch; the current branch also includes §51ea. The new branch's own-permanent-housing restriction must not be retrospectively added to the old branch. Do not claim as borrower while also co-borrower on another credited contract; the old/new-contract overlap exclusion in §52zzy(15) also applies. Pre-2018 state mortgage support prevents simultaneous interest-bonus claims until the month after that support last applied (§52zzy(14)).

The window is **60 consecutive months from the first month of interest charging**. In the first and last calendar years, cap the credit at `annual maximum × eligible months / 12`, and take the lower of that cap and 50% of eligible interest actually paid for the eligible period (§33a(3),(7)). For example, interest beginning in October 2023 gives the old branch a EUR 100 cap for October–December 2023, EUR 400 for full eligible years including 2026, and EUR 300 for January–September 2028. An otherwise eligible new-branch loan starting interest in October 2026 instead has caps of EUR 300 for October–December 2026, EUR 1,200 for each full eligible year and EUR 900 for January–September 2031. An eligible old-contract 2026 interest certificate of EUR 1,000 gives `min(500,400) = EUR 400`; a new-contract certificate of EUR 3,000 gives `min(1,500,1,200) = EUR 1,200` for a full eligible year. For a new loan starting interest in July with EUR 2,000 eligible interest paid, the first-year result is `min(1,000,1,200 × 6/12) = EUR 600`. These examples assume the age, income, property and other eligibility tests are met; no assumed figure is represented as an official reference wage.

Apply the mortgage bonus **after** the child bonus. Request payout of any amount exceeding the remaining tax in the return, or claim through the employer's annual settlement (§33a(8),(9)). A non-resident must satisfy the 90%-Slovak-income test (§33a(10)). On the borrower's death, §33a(11) transfers only the unexpired window to the person taking over the debt, with its stated age/income/co-borrower exceptions; the deceased claims through the death month and the successor from the following month ([current ITA §§33a,52zzy](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html); [historical §33a](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20230801.html)).

**Rounding.** Every calculation is to two decimal places, with 5 and above rounded up (§47).

## Deadlines and filing

| What | When | Rule |
|---|---|---|
| Ask the employer for the annual settlement (employment income only; no §11(11) DDS addback required) | 15 February 2027 | §38(1) |
| DPFO type A (employment only) or type B (all other cases) for 2026, and payment | 31 March 2027 | §49(2) |
| Extension by notice to the tax office before 31 March 2027 | up to 3 full months, to 30 June 2027 | §49(3)(a) |
| Extension where foreign-source income is included | up to 6 full months, to 30 September 2027 | §49(3)(b) |
| Advances in the period after the 2026 return if the last known tax was over EUR 5,000 | quarterly by the end of each quarter; monthly by month end if over EUR 16,600 | §34(1)-(3) |

The extension notice names the new deadline: the end of the month in which the return will be filed. The tax is then due by that new date (§49(3)). The notice is on the Financial Directorate's form.

A self-employed person registered for income tax, a VAT payer, and any tax adviser or lawyer acting for a client must file electronically (Tax Procedure Code §14(1)). The last known tax for advances is the tax on the business base at 19%, after losses (§34(5)).

**Verified forms for the 2026 return.** The [official Ministry forms package](https://www.mfsr.sk/files/archiv/66/prispevok_16.zip), notice MF/014310/2026-721, retains **type A MF/012185/2025-721** (DPFOAv25 v1.10, six pages). For type B it issues **MF/014308/2026-721** (DPFOBv26 v1.3, twenty pages). These apply where the filing deadline falls **after 31 December 2026**, including the ordinary 2026 return due in March 2027. The earlier type B MF/012186/2025-721 belongs to deadlines no later than 31 December 2026. The 2025 suffix on the retained type A does not make it obsolete. Use the matching [2026 instructions, notice MF/014312/2026-721](https://www.mfsr.sk/files/archiv/36/prispevok_18.zip), rather than selecting a form by its filename year alone.

**Ordinary return mapping.** “Row” below means the numbered field on those actual forms; complete the identity, year and return-type fields first.

| Calculation | Type A, employment only | Type B |
|---|---|---|
| Employment income and contributions | Gross taxable income 34; compulsory contributions 36; partial base 39 = 34 − 36 | Gross 36; contributions 37; partial base 38 |
| Business, expenses and losses | Use type B if business income is present | Table 1 by income category, totals to 39/40, adjusted positive base 45 or loss 46. Loss history in columns 47–50a, current deductions 51–54a; reduced base 55, then 57 after any separately supported deductions. Apply the statutory loss limits above; the printed fields do not create extra relief. |
| Allowances and separate taxable bases | Personal/spouse/pension allowances 40/41/42, total 43; reduced base 44, tax 45 | Allowances 73/74/75, total 77. Employment uses them first (78); unused allowance 91 reduces business base in 92/94. Non-business base 80 and business base 94 remain separate; taxable business revenue 95 chooses the rate for tax 96. |
| Foreign relief and tax total | Exemption/credit calculation 48–55; resulting tax 56 | Non-business relief 82–90; business relief 97–105; ordinary §7 relief 107–115. Tax total 116 combines 90,105,115 and the separately computed dividend/bond taxes below. Use the treaty method and supported foreign tax, not a guessed rate. |
| Child and mortgage credits | Child details 31, annual entitlement 57; mortgage details 33, entitlement 63. Other-parent augmentation, if used, is 56a. | Child details 33, entitlement 117; mortgage details 35, entitlement 123. Other-parent augmentation, if used, is 116a. |
| Already paid credits and advances | Employer-paid child/mortgage bonuses 59/65; listed advances 68–70; final amount due 71 or overpayment 72 | Employer-paid bonuses 119/125; listed advance/security categories 129–134; final amount due 135 or overpayment 136 |
| Refund or bonus payout request | Section XI; bonus payout fields 61/67 | Section XIV; bonus payout fields 121/127 |

For flat-rate business expenses, put the total expense **including contributions** in Table 1 row 10 column 2 and mark the flat-rate choice; repeat the contribution information below the table and in Annex 4 without deducting it twice. Complete Table 1b for the retained inventory/receivables records. Rental uses Table 1 row 11 and flows through 58–65; taxable §8 gains use Table 3 and 69–71. Both join base 80, without consuming the business allowance again. Ordinary §7 income uses Table 2 and 66–68, tax 106 and, after any relief,115. The §51e dividend calculation is in Annex 2 (tax total row 28); §51ea government-bond yields use Annex 3 (tax total row 14); both feed 116. Keep exempt retail-bond receipts out of these taxable-yield fields.

Follow each form's printed settlement formula. It adds back child or mortgage bonuses already paid by the employer, then subtracts the permitted advances; mortgage-bonus amounts in A65/B125 concern a return after the employer's annual settlement. Subtracting the full annual bonus again without that reconciliation would duplicate it. Apply the EUR 17 assessment rule and EUR 5 payment rule only on their stated conditions. Retain employer income/advance certificates, the lender certificate and any other-parent evidence supporting the fields. Count the actual attachments: the type B built-in annexes count only when completed (row 154), whereas type A counts all attached documents (row 86). Sources: actual forms, type A pp.2–6, type B pp.3–13,17–20; matching 2026 instructions.

## Penalties and interest

All under the Tax Procedure Code, Act 563/2009, version in force from 1 September 2026. The 1 January 2027 version has the same text for §154 to §156.

- **Late or missing return.** A fine of EUR 100 to EUR 30,000 (§154(1)(a), §155(1)(a)). For a fine within a range, the tax office does not impose one for a first breach (§155(4)). It weighs severity, duration, consequences and the taxpayer's reliability index.
- **Tax understated, found by the tax office.** 3 x the ECB base rate a year, at least 10% a year, on the extra tax, counted daily from the day after the filing deadline. It is at least 1% and at most 100% of the extra tax (§155(1)(f), (2), (5)). Paying within 15 days of the decision cuts it to two thirds (§155(17)).
- **Own correction (dodatočné daňové priznanie).** The ECB base rate a year, at least 3%, on the difference. If filed after a tax audit is announced, within the time allowed, it is 2 x the ECB base rate, at least 7% (§155(1)(g),(h), (5)).
- **Late payment interest (úrok z omeškania).** 4 x the ECB base rate on the day the arrears arose, at least 15% a year, for each day late, for at most four years (§156(2)). It is not charged if it is EUR 5 or less (§156(6)(b)).
- Fines of EUR 5 or less are not imposed (§155(11)).

## Cross-border points

- **Foreign income of a resident.** Include it. Relief follows the treaty: a credit capped at the Slovak tax on that income, or exemption (§45). Including foreign income gives the six-month extension (§49(3)(b)).
- **Non-residents.** Slovak-source income only (§16). The spouse allowance and the child bonus need at least 90% of total income from Slovak sources (§11(7), §33(9)).
- **Withholding** on payments to non-residents, the security deduction and treaty lists are in sk-cross-border.
- **Contributions abroad.** Which country insures a cross-border worker decides which contributions are deducted (§5(8)). See [sk-payroll-social](sk-payroll-social.md).

## Worked examples

### Example 1: self-employed on flat-rate expenses

Jana is a web designer with a trade licence. She is not a VAT payer. In 2026 her revenue is EUR 48,000. She uses flat-rate expenses and paid EUR 6,000 of compulsory social and health contributions. She has no other income.

Flat-rate expenses are 60% of EUR 48,000, which is EUR 28,800, capped at EUR 20,000. With the contributions on top, her business partial base is 48,000 - 20,000 - 6,000 = EUR 22,000. That is below EUR 26,083.13, so she gets the full personal allowance of EUR 5,966.73 (21 x 284.13). Her tax base is EUR 16,033.27. Revenue is under EUR 100,000, so the rate is 15%: tax EUR 2,404.99, due with DPFO type B by 31 March 2027. Her last known tax is under EUR 5,000, so she pays no advances in the next period.

**Filing Jana's figures.** On type B, Table 1 row 2 records her EUR 48,000 trade income and row 10 totals that income; row 10 column 2 has EUR 26,000 expenses, including her EUR 6,000 contributions. Rows 39/40 carry those totals; rows 41/45/55/57 are EUR 22,000 with no losses or other adjustments. The allowance is EUR 5,966.73 in 73/77 and the unused employment allocation 91; rows 92/94 are EUR 16,033.27,95 is EUR 48,000, and 96/105/116 are EUR 2,404.99. With no credits or advances,135 is EUR 2,404.99.

Independent variants in the same check preserve Jana's computation: on a EUR 10,000 pre-loss business base with EUR 8,000 unexpired losses, a qualifying micro-taxpayer uses EUR 8,000; a trader excluded by a controlled transaction uses EUR 5,000. A separate EUR 1,000 coupon gives EUR 130 for a non-exempt §51ea government bond, EUR 190 for ordinary foreign bank interest, and zero for a qualifying non-business retail government bond.

```oa-check
name: SK PIT 2026, SZCO flat-rate expenses, revenue EUR 48,000, 15% rate
inputs:
  revenue: 48000
  contributions: 6000
  subsistence_min: 284.13
  loss_variant_base: 10000
  loss_variant_available: 8000
  bond_coupon: 1000
steps:
  - flat_expenses: min(revenue * 0.60, 20000)
  - partial_base: revenue - flat_expenses - contributions
  - allowance: round(subsistence_min * 21, 2)
  - base: partial_base - allowance
  - tax: round(base * 0.15, 2)
  - micro_loss_used: min(loss_variant_available, loss_variant_base)
  - controlled_trader_loss_used: min(loss_variant_available, loss_variant_base * 0.50)
  - controlled_trader_loss_left: loss_variant_available - controlled_trader_loss_used
  - government_bond_tax: bond_coupon * 0.13
  - foreign_bank_interest_tax: bond_coupon * 0.19
  - exempt_retail_bond_tax: 0
expected:
  flat_expenses: 20000
  partial_base: 22000
  allowance: 5966.73
  base: 16033.27
  tax: 2404.99
  micro_loss_used: 8000
  controlled_trader_loss_used: 5000
  controlled_trader_loss_left: 3000
  government_bond_tax: 130
  foreign_bank_interest_tax: 190
  exempt_retail_bond_tax: 0
```

### Example 2: employee with both phase-outs

Peter is an employee. His 2026 gross pay is EUR 42,000 and his payslips show EUR 6,000 of employee contributions, so his employment partial base is EUR 36,000. He has one child aged 10 living with him all year. His wife works and does not meet the §11(4) conditions, so there is no spouse allowance. He files DPFO type A.

The base is above EUR 26,083.13, so the personal allowance phases down: 14,661.11 - 36,000 / 3 = EUR 2,661.11. His tax base is EUR 33,338.89, all in the 19% band: tax EUR 6,334.39.

The child bonus would be 12 x EUR 100 = EUR 1,200. His base of EUR 36,000 is above EUR 27,432 (1.5 x 12 x 1,524), so the bonus falls by one tenth of the EUR 8,568 excess, EUR 856.80. The bonus is EUR 343.20, well under the 29% cap. Tax after the bonus is EUR 5,991.19, before the advances his employer withheld.

**Filing Peter's figures.** On type A,34 is EUR 42,000,36 is EUR 6,000,39 is EUR 36,000; 40/43 are EUR 2,661.11,44 is EUR 33,338.89,45/56 are EUR 6,334.39, and 57 is EUR 343.20. Rows 58/64 are EUR 5,991.19 with no mortgage credit. For a separate settlement variant, if his certificates show EUR 5,500 wage-tax advances and EUR 100 child bonus already paid, enter 69 = 5,500 and 59 = 100:71 is `6,334.39 − 343.20 + 100 − 5,500 = EUR 591.19`. The EUR 100 is not an extra tax charge; it prevents paying the same part of his annual bonus twice.

The same check also recomputes the separate low-base parent-aggregation and June birthday/birth cases above, and the old/new mortgage caps. Those variants do not change Peter's stated facts or tax result; mortgage eligibility is assumed satisfied for the variant borrowers.

```oa-check
name: SK PIT 2026, employee, allowance phase-out and child bonus taper
inputs:
  gross: 42000
  contributions: 6000
  subsistence_min: 284.13
  avg_wage_2024: 1524
  months_child_under_15: 12
  low_claimant_base: 2000
  other_parent_base: 4000
  other_parent_partial_months: 6
  old_eligible_interest: 1000
  new_eligible_interest: 3000
  new_partial_interest: 2000
  partial_loan_months: 6
  employer_child_bonus_paid_variant: 100
  wage_advances_variant: 5500
steps:
  - partial_base: gross - contributions
  - allowance_cap: round(subsistence_min * 51.6, 2)
  - allowance: max(0, round(allowance_cap - partial_base / 3, 2))
  - base: partial_base - allowance
  - tax: round(base * 0.19, 2)
  - taper_threshold: 1.5 * 12 * avg_wage_2024
  - bonus_full: months_child_under_15 * 100
  - bonus_cut: round((partial_base - taper_threshold) / 10, 2)
  - bonus: min(max(0, bonus_full - bonus_cut), round(partial_base * 0.29, 2))
  - tax_after_bonus: tax - bonus
  - child_15_in_june: 6 * 100 + 6 * 50
  - child_18_in_june: 6 * 50
  - child_born_june: 7 * 100
  - changing_count_cap: 4000 * (0.29 * 6 / 12 + 0.36 * 6 / 12)
  - changing_count_bonus: min(1800, changing_count_cap)
  - low_base_bonus: min(1200, low_claimant_base * 0.29)
  - combined_base: low_claimant_base + other_parent_base
  - combined_bonus: min(1200, combined_base * 0.29)
  - partial_combined_base: low_claimant_base + other_parent_base * other_parent_partial_months / 12
  - partial_combined_bonus: min(1200, partial_combined_base * 0.29)
  - old_mortgage_bonus: min(old_eligible_interest * 0.50, 400)
  - new_mortgage_bonus: min(new_eligible_interest * 0.50, 1200)
  - new_partial_bonus: min(new_partial_interest * 0.50, 1200 * partial_loan_months / 12)
  - return_balance_variant: tax_after_bonus + employer_child_bonus_paid_variant - wage_advances_variant
expected:
  allowance_cap: 14661.11
  allowance: 2661.11
  base: 33338.89
  tax: 6334.39
  taper_threshold: 27432
  bonus: 343.20
  tax_after_bonus: 5991.19
  child_15_in_june: 900
  child_18_in_june: 300
  child_born_june: 700
  changing_count_cap: 1300
  changing_count_bonus: 1300
  low_base_bonus: 580
  combined_base: 6000
  combined_bonus: 1200
  partial_combined_base: 4000
  partial_combined_bonus: 1160
  old_mortgage_bonus: 400
  new_mortgage_bonus: 1200
  new_partial_bonus: 600
  return_balance_variant: 591.19
```

## Ask the client first

1. Where was the client's home and permanent residence in 2026, and how many days were they in Slovakia? Did they have any foreign income?
2. What kinds of income did they have: employment, business, rental, sale of property, shares or crypto, interest, dividends?
3. If self-employed: what was the business revenue (EUR 100,000 test, EUR 60,000 micro-taxpayer test), were they a VAT payer at any time in 2026, and do they want actual or flat-rate expenses? What contributions did they actually pay?
4. Children: dates of birth/adoption and dependent status, months in the household, which parent claims, and both parents' eligible bases and Slovak/total income if aggregation is needed.
5. Spouse: did they live together, which condition in §11(4) applies, and what was the spouse's own income?
6. Did they receive a pension at the start of 2026, pay into supplementary pension (DDS) or PEPP, or have a housing loan? For DDS/PEPP obtain all contracts, the post-2013 date or benefit-plan cancellation amendment, proof of own payments, and any early withdrawal and past deductions. For the housing loan obtain the contract/application and first-interest dates, co-borrowers, lender interest certificate, property use and prior-year income/reference wage.

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 595/2003 Coll. on income tax, 2026: existing provisions plus §§2(w),9(1)(r),15(a)(7),30,33,33a,43(3)(v),51ea,52zzy,52zzzc reread for this update | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html | 2026-10-27 |
| Act No. 595/2003 Coll., 31 December 2026 text: assigned provisions unchanged; §52zzzm postpones its listed changes to 2027 returns | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20261231.html | 2026-10-27 |
| Historical ITA, final 2023 version, §33a: continuing pre-2024 housing-loan credit under current §52zzy | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20230801.html | 2026-10-27 |
| Act No. 261/2025 Coll., consolidation package amending §11 and §15 | https://static.slov-lex.sk/static/SK/ZZ/2025/261/vyhlasene_znenie.html | 2026-10-23 |
| Act No. 563/2009 Coll., Tax Procedure Code, version in force from 1 September 2026 (§14, §154-§156) | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html | 2026-10-23 |
| Act No. 563/2009 Coll., version in force from 1 January 2027 (same §154-§156) | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20270101.html | 2026-10-23 |
| Ministry of Labour, subsistence minimum from 1 July 2025 (EUR 284.13) | https://employment.gov.sk/sk/rodina-socialna-pomoc/hmotna-nudza/zivotne-minimum/vyska-zivotneho-minima-od-1-jula-2025.html | 2026-10-23 |
| Ministry of Labour, Report on the social situation 2024 (average wage 2024, EUR 1,524, Statistical Office figure) | https://www.employment.gov.sk/files/slovensky/ministerstvo/analyticke-centrum/2025/sprava_sossr_2024_pub.pdf | 2026-10-23 |
| Financial Administration, income tax for citizens: allowance EUR 5,966.73, phase-out from EUR 26,083.13, EUR 14,661.11, spouse EUR 5,455.30 / EUR 20,116.40 / EUR 43,983.32, child bonus 2026 and its taper | https://www.financnasprava.sk/sk/obcania/dane/dan-z-prijmov/informovanie-dan-prijem | 2026-10-24 |
| Financial Administration, employees: filing threshold EUR 2,983.37 and the 2026 allowance figures | https://www.financnasprava.sk/sk/obcania/dane/dan-z-prijmov/zamestnanci | 2026-10-24 |
| Financial Administration, worked DPFO type A example with the child bonus (tax year 2025, same §33 text): the bonus cap is tested on the §5 partial base before allowances (row 39 / 56a, not row 44) | https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Obcania/Dan_z_prijmov/2026/2026.01.15_prilad_BONUS.pdf | 2026-10-24 |
| Ministry of Finance, notice MF/014310/2026-721 and actual type A/type B/DPPO sample forms, actual package | https://www.mfsr.sk/files/archiv/66/prispevok_16.zip | 2026-10-27 |
| Ministry of Finance, notice MF/014312/2026-721 and actual 2026 type A/type B/DPPO instructions, actual package | https://www.mfsr.sk/files/archiv/36/prispevok_18.zip | 2026-10-27 |
| ECB and NBS, actual historical main-refinancing rates | https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html; https://nbs.sk/en/statistics/financial-markets/interest-rates/ecb-key-interest-rates/ | 2026-10-27 |
| ITA §§32(2)(d),38(1): employment-only return and annual-settlement exclusion when a §11(11) DDS addback is required | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html#paragraf-38 | 2026-10-29 |

**Rate reference dates.** The [ECB history](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html), also published by [NBS](https://nbs.sk/en/statistics/financial-markets/interest-rates/ecb-key-interest-rates/), records main-refinancing rates of 2.15% from 11 June 2025, 2.40% from 17 June 2026 and 2.65% from 16 September 2026, observed through this 27 October read. At 2.65% the 10%/7%/3% penalty floors and 15% interest floor apply. Select the actual rate on delivery of the assessment or supplementary filing for §155 (§155(7)), and when arrears arise for §156(2). A future reference date needs the rate in force then; no future ECB rate is asserted. The form versions are verified by the actual Ministry packages above; the 31 December law transition remains governed by §52zzzm as explained at the start.

Historical source credit from the original Guide: [priznanie-digital/priznanie-digital](https://github.com/priznanie-digital/priznanie-digital) (MIT, 40 contributors). That contributor count is the original historical credit, not a current count or a primary-law authority.

> Contributed by Michael Cutajar.

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
