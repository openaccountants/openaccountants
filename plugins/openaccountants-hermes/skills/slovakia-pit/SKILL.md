---
name: slovakia-pit
description: "Slovak personal income tax (daň z príjmov fyzickej osoby, DPFO) for tax year 2026 under Act 595/2003 as amended by Act 261/2025. Covers residents and non-residents in outline, employment income (§5), self-employed SZČO business income (§6) with the 60% flat-rate expenses capped at EUR 20,000, the 15% rate for business revenue up to EUR 100,000, the new 19%, 25%, 30% and 35% bands set as multiples of the subsistence minimum (EUR 284.13), the 2026 personal allowance of EUR 5,966.73 and its phase-out, the spouse allowance, the child tax bonus and its taper above EUR 27,432, the EUR 17 minimum tax rule, capital income, the 31 March 2027 deadline and extensions, advances and penalties. Trigger on: daň z príjmov 2026, DPFO typ A, DPFO typ B, SZČO, živnostník, paušálne výdavky, nezdaniteľná časť, daňový bonus, Slovak income tax 2026. Out of scope: payroll withholding and contributions in sk-payroll-social, companies in sk-corporate-income-tax, non-residents and treaties in sk-cross-border."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/slovakia-pit"
  jurisdiction: "SK"
  tax_year: "2026"
  last_updated: "2026-10-24"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Slovakia: personal income tax for employees and the self-employed (2026) v1.1

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
- **Employees** (§5). The employer withholds monthly advances. An employee with only §5 income from Slovak employers can ask an employer for the annual settlement (ročné zúčtovanie) by 15 February 2027 instead of filing (§38(1)). Otherwise they file DPFO type A.
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
| Capital income special base (§7), for example foreign interest | 19% | 2026 | same, §15(a)(4) |
| Foreign dividends special base (§51e(3)(a)) | 7% (35% from a non-cooperating state) | 2026 | same, §15(a)(5),(6) |
| Personal allowance (21.0 x), base up to 91.8 x (EUR 26,083.13) | EUR 5,966.73 | 2026 | same, §11(2)(a) |
| Personal allowance, base above EUR 26,083.13 | EUR 14,661.11 (51.6 x) minus one third of the base; zero from a base of EUR 43,983.32 | 2026 | same, §11(2)(b) |
| Spouse allowance (19.2 x), taxpayer base up to EUR 43,983.32 | up to EUR 5,455.30, less the spouse's own income | 2026 | same, §11(3)(a) |
| Spouse allowance, taxpayer base above EUR 43,983.32 | EUR 20,116.40 (70.8 x) minus one third of the base, less the spouse's own income | 2026 | same, §11(3)(b) |
| Supplementary pension (DDS) and PEPP contributions | up to EUR 180 a year | 2026 | same, §11(9) |
| Flat-rate expenses for a non-VAT payer (paušálne výdavky) | 60% of business revenue, cap EUR 20,000, plus compulsory contributions paid | 2026 | same, §6(10) |
| Child tax bonus, child under 15 | EUR 100 a month | 2026 | same, §33(1)(b) |
| Child tax bonus, child aged 15 to 18 | EUR 50 a month | 2026 | same, §33(1)(a) |
| Child tax bonus cap, as % of the employment or business base | 29% (1 child), 36% (2), 43% (3), 50% (4), 57% (5), 64% (6 or more) | 2026 | same, §33(6) |
| Child tax bonus taper threshold: 1.5 x 12 x average monthly wage of 2024 (EUR 1,524) | EUR 27,432; above it the bonus per child falls by 1/10 of the excess | 2026 | same, §33(11); wage: https://www.employment.gov.sk/files/slovensky/ministerstvo/analyticke-centrum/2025/sprava_sossr_2024_pub.pdf |
| Minimum tax of an individual | no tax assessed if the tax is EUR 17 or less, or total income is EUR 2,983.37 or less; not where a child or mortgage bonus is claimed or tax was withheld | 2026 | same, §46a |
| Tax due in the return not paid | if EUR 5 or less | 2026 | same, §46 |
| Exempt: rental plus occasional income | first EUR 500 a year | 2026 | same, §9(1)(g) |
| Exempt: listed securities held over one year (not business assets) | fully exempt | 2026 | same, §9(1)(k) |
| Advances: last known tax over EUR 5,000 up to EUR 16,600 / over EUR 16,600 | quarterly 1/4 / monthly 1/12 | 2026 | same, §34(1)-(3) |

**How the bands work.** The law sets two separate bases (§4(1)). Base (a) is employment income after allowances, plus rental and other income. Base (b) is business income after allowances and losses. Each base is taxed on its own scale in §15(a): base (a) always on the 19% to 35% bands, base (b) at 15% if business revenue is EUR 100,000 or less, otherwise on the same bands.

Tax on a base B above EUR 75,010.32 is 19% x 43,983.32 + 25% x 16,365.89 + 30% x 14,661.11 + 35% x (B - 75,010.32), which is EUR 16,846.64 plus 35% of the excess.

## The taxable base

**Employment (§5).** Gross pay including benefits in kind, minus the employee's compulsory social and health contributions (§5(8)). Pay for 2026 received by 31 January 2027 belongs to 2026 (§4(3)). Withholding and contributions are in [sk-payroll-social](sk-payroll-social.md).

**Self-employed (§6(1),(2)).** Revenue minus either:
- **actual expenses** (preukázateľné výdavky), with tax records or double-entry accounts (§6(11)); or
- **flat-rate expenses** of 60% of revenue, capped at EUR 20,000, if the person is not a VAT payer, or was one for only part of the year (§6(10)). The flat rate covers all expenses except the compulsory social and health contributions, which are deducted on top in the amount paid. The person still keeps a record of income and of inventory and receivables (§6(10), §6(11)(a),(d)).

The result is the business partial base. A tax loss can be carried forward five years. A micro-taxpayer (business revenue up to EUR 60,000, §2(w)) can use it in full; others only up to 50% of the business base (§30(1)).

**The 15% rate.** It turns on business revenue under §6(1) and (2), not on profit. Revenue of EUR 100,000 or less gives 15% on the whole business base. Above EUR 100,000 the whole business base goes on the bands (§15(a)(2),(3)).

**Allowances (nezdaniteľné časti, §11).** They reduce only the employment and business bases, never rental, capital or other income (§11(1)).
- The personal allowance and the spouse allowance are tested on the tax base from §5 and §6(1),(2) income. A taxpayer who at the start of 2026 receives an old-age, early, service or similar foreign pension gets no personal allowance if the pension for the year, including the 13th pension, exceeds the allowance; otherwise the allowance is cut to the difference (§11(6)).
- The spouse allowance needs a spouse living with the taxpayer who cared for a minor child, received a care allowance, was a registered jobseeker, or is disabled (§11(4)). The spouse's own income is net of their contributions. Months count only if the conditions held at the start of the month (§11(5)).
- Allowances come off the employment base first, and only the rest comes off the business base (§11(12)).

**Rental (§6(3)) and other income (§8).** Income minus proven expenses. Rental income and occasional income are exempt up to EUR 500 in total (§9(1)(g)). Sales of property, movable things, options, securities, shares in an s.r.o. and crypto-assets (§8(1)(b)-(f),(t)) are taxed on the gain. A loss on one type is ignored (§8(2)). Several sales are exempt if held long enough, for example listed securities held over a year (§9(1)(k)). These gains are taxed in base (a) on the bands.

**Capital income (§7).** Slovak interest is taxed by withholding under §43 and stays out of the return (§7(3)). Foreign interest and similar income go in a special base taxed at 19% (§15(a)(4)). Dividends from a Slovak company are taxed by withholding. Foreign dividends go in a special base at 7%, or 35% from a non-cooperating state (§51e, §15(a)(5),(6)).

**Credits.** From the tax computed:
- **Child tax bonus (§33).** EUR 100 a month for each child under 15 and EUR 50 a month for each child aged 15 to 18, for each month at whose start the conditions were met (§33(1),(5)). The child lives in the taxpayer's household, and the taxpayer needs employment or business income. The total is capped at a percentage of the employment or business partial base, or their sum, taken before allowances (§33(6)); the Financial Administration's worked return uses that base. If that base exceeds EUR 27,432, the bonus for each child falls by one tenth of the excess (§33(11)). Only one parent claims (§33(4)). If the bonus exceeds the tax, the difference is paid out (§33(7)). The taxpayer must have at least 90% of income from Slovak sources (§33(9)).
- **Mortgage interest bonus** for borrowers aged 18 to 35 at application (§33a). The conditions differ for loan contracts made up to 31 December 2023 and after; check them in the law before claiming it.

**Rounding.** Every calculation is to two decimal places, with 5 and above rounded up (§47).

## Deadlines and filing

| What | When | Rule |
|---|---|---|
| Ask the employer for the annual settlement (employment income only) | 15 February 2027 | §38(1) |
| DPFO type A (employment only) or type B (all other cases) for 2026, and payment | 31 March 2027 | §49(2) |
| Extension by notice to the tax office before 31 March 2027 | up to 3 full months, to 30 June 2027 | §49(3)(a) |
| Extension where foreign-source income is included | up to 6 full months, to 30 September 2027 | §49(3)(b) |
| Advances in the period after the 2026 return if the last known tax was over EUR 5,000 | quarterly by the end of each quarter; monthly by month end if over EUR 16,600 | §34(1)-(3) |

The extension notice names the new deadline: the end of the month in which the return will be filed. The tax is then due by that new date (§49(3)). The notice is on the Financial Directorate's form.

A self-employed person registered for income tax, a VAT payer, and any tax adviser or lawyer acting for a client must file electronically (Tax Procedure Code §14(1)). The last known tax for advances is the tax on the business base at 19%, after losses (§34(5)).

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

```oa-check
name: SK PIT 2026, SZCO flat-rate expenses, revenue EUR 48,000, 15% rate
inputs:
  revenue: 48000
  contributions: 6000
  subsistence_min: 284.13
steps:
  - flat_expenses: min(revenue * 0.60, 20000)
  - partial_base: revenue - flat_expenses - contributions
  - allowance: round(subsistence_min * 21, 2)
  - base: partial_base - allowance
  - tax: round(base * 0.15, 2)
expected:
  flat_expenses: 20000
  partial_base: 22000
  allowance: 5966.73
  base: 16033.27
  tax: 2404.99
```

### Example 2: employee with both phase-outs

Peter is an employee. His 2026 gross pay is EUR 42,000 and his payslips show EUR 6,000 of employee contributions, so his employment partial base is EUR 36,000. He has one child aged 10 living with him all year. His wife works and does not meet the §11(4) conditions, so there is no spouse allowance. He files DPFO type A.

The base is above EUR 26,083.13, so the personal allowance phases down: 14,661.11 - 36,000 / 3 = EUR 2,661.11. His tax base is EUR 33,338.89, all in the 19% band: tax EUR 6,334.39.

The child bonus would be 12 x EUR 100 = EUR 1,200. His base of EUR 36,000 is above EUR 27,432 (1.5 x 12 x 1,524), so the bonus falls by one tenth of the EUR 8,568 excess, EUR 856.80. The bonus is EUR 343.20, well under the 29% cap. Tax after the bonus is EUR 5,991.19, before the advances his employer withheld.

```oa-check
name: SK PIT 2026, employee, allowance phase-out and child bonus taper
inputs:
  gross: 42000
  contributions: 6000
  subsistence_min: 284.13
  avg_wage_2024: 1524
  months_child_under_15: 12
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
expected:
  allowance_cap: 14661.11
  allowance: 2661.11
  base: 33338.89
  tax: 6334.39
  taper_threshold: 27432
  bonus: 343.20
  tax_after_bonus: 5991.19
```

## Ask the client first

1. Where was the client's home and permanent residence in 2026, and how many days were they in Slovakia? Did they have any foreign income?
2. What kinds of income did they have: employment, business, rental, sale of property, shares or crypto, interest, dividends?
3. If self-employed: what was the business revenue (EUR 100,000 test, EUR 60,000 micro-taxpayer test), were they a VAT payer at any time in 2026, and do they want actual or flat-rate expenses? What contributions did they actually pay?
4. Children: dates of birth, months living in the household, and which parent claims the bonus.
5. Spouse: did they live together, which condition in §11(4) applies, and what was the spouse's own income?
6. Did they receive a pension at the start of 2026, pay into supplementary pension (DDS) or PEPP, or have a young person's mortgage?

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 595/2003 Coll. on income tax, version in force 1 January 2026 to 30 December 2026 (§2, §4-§9, §11, §15, §30, §32-§34, §38, §45, §46, §46a, §47, §49, §51e, §52zzzj) | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html | 2026-10-23 |
| Act No. 595/2003 Coll., version in force from 31 December 2026 (§52zzzm) | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20261231.html | 2026-10-23 |
| Act No. 261/2025 Coll., consolidation package amending §11 and §15 | https://static.slov-lex.sk/static/SK/ZZ/2025/261/vyhlasene_znenie.html | 2026-10-23 |
| Act No. 563/2009 Coll., Tax Procedure Code, version in force from 1 September 2026 (§14, §154-§156) | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html | 2026-10-23 |
| Act No. 563/2009 Coll., version in force from 1 January 2027 (same §154-§156) | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20270101.html | 2026-10-23 |
| Ministry of Labour, subsistence minimum from 1 July 2025 (EUR 284.13) | https://employment.gov.sk/sk/rodina-socialna-pomoc/hmotna-nudza/zivotne-minimum/vyska-zivotneho-minima-od-1-jula-2025.html | 2026-10-23 |
| Ministry of Labour, Report on the social situation 2024 (average wage 2024, EUR 1,524, Statistical Office figure) | https://www.employment.gov.sk/files/slovensky/ministerstvo/analyticke-centrum/2025/sprava_sossr_2024_pub.pdf | 2026-10-23 |
| Financial Administration, income tax for citizens: allowance EUR 5,966.73, phase-out from EUR 26,083.13, EUR 14,661.11, spouse EUR 5,455.30 / EUR 20,116.40 / EUR 43,983.32, child bonus 2026 and its taper | https://www.financnasprava.sk/sk/obcania/dane/dan-z-prijmov/informovanie-dan-prijem | 2026-10-24 |
| Financial Administration, employees: filing threshold EUR 2,983.37 and the 2026 allowance figures | https://www.financnasprava.sk/sk/obcania/dane/dan-z-prijmov/zamestnanci | 2026-10-24 |
| Financial Administration, worked DPFO type A example with the child bonus (tax year 2025, same §33 text): the bonus cap is tested on the §5 partial base before allowances (row 39 / 56a, not row 44) | https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Obcania/Dan_z_prijmov/2026/2026.01.15_prilad_BONUS.pdf | 2026-10-24 |

Not yet confirmed: the current ECB base rate behind the penalty and interest floors; the 2026 DPFO form versions; the young person's mortgage bonus conditions in §33a.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `slovakia-pit` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/slovakia-pit. If neither is available, confirm every figure against the official source pages cited above before relying on it.
