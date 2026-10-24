---
name: se-social-contributions
description: "Use for Swedish social contributions of the self-employed in 2026: egenavgifter of 28.97% on active business income of a sole trader or a partner in a handelsbolag, and their components; 10.21% for those born 1938-1958 or on full pension or sickness compensation; särskild löneskatt of 24.26% on passive business; the 25% schablonavdrag and its NE or N3A reconciliation; the 7.5% special deduction and the regional deduction; waiting-period sickness rates; the 7% allmän pensionsavgift, its ceiling and tax credit; payment through F-skatt and settlement in the final tax decision; penalties and interest. Also lists the employer rates (31.42%, 10.21% from 67, youth reduction, växa refund) a sole trader with staff needs. Trigger on: egenavgifter, särskild löneskatt, schablonavdrag, allmän pensionsavgift, karensdagar, enskild firma avgifter. Out of scope: sweden-payroll, se-income-tax, se-employee-income-tax, se-cross-border."
version: 2.1
jurisdiction: SE
tax_year: 2026
last_updated: 2026-10-24
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sweden: self-employed social contributions (egenavgifter)

This skill computes the social contributions a self-employed person in Sweden pays for income year 2026: egenavgifter and allmän löneavgift on active business income, särskild löneskatt on passive business income, and the allmän pensionsavgift on earned income. It also covers the provisional deduction in the return and the next-year reconciliation. Income tax on the same profit is in [se-income-tax](se-income-tax.md). Running payroll for staff is in [sweden-payroll](sweden-payroll.md). Residence and foreign coverage are in [se-cross-border](se-cross-border.md).

## Who this applies to

- **Sole traders (enskild näringsidkare) with active business.** A natural person pays egenavgifter on the surplus of a business in which they have worked to a not insignificant extent (Socialavgiftslag (2000:980), SAL, 3 kap. 1 and 3 §§). Work-dependent activity such as consulting or a trade is active even at low hours. Holding and managing assets needs its own test of how much the person works in it.
- **Partners in a Swedish handelsbolag or kommanditbolag.** Each partner pays on their own tax-adjusted share. The provisional deduction is computed for each partner separately (Inkomstskattelag (1999:1229), IL, 16 kap. 31 §).
- **Passive business.** A person or estate with a surplus of passive business pays särskild löneskatt of 24.26% instead of egenavgifter (Lag (1990:659) om särskild löneskatt på vissa förvärvsinkomster, SLF, 2 §). Passive business is still business income, not capital income.
- **Estates.** An estate after a person who died in 2026 or earlier pays 24.26% särskild löneskatt instead of egenavgifter and allmän löneavgift on active business income (SLF 2 §; Skatteverket table for 2026). No egenavgift base is set for a person who died during the year (SAL 3 kap. 12 § third paragraph).
- **F-skatt holders paid like employees.** Pay for work from a payer who does not owe employer contributions because the worker holds F-skatt is liable to egenavgifter (SAL 3 kap. 8 §). It is reported on schedule T1, not added to business income.
- **Hobby income** is not business and takes a different return route.
- **Employer side.** If the sole trader employs staff, employer contributions on their pay are a separate payroll calculation, listed below for reference and set out in full in [sweden-payroll](sweden-payroll.md). None of the employer reliefs changes the owner's own rate.

F-skatt, FA-skatt and special A-skatt govern how tax is collected. The absence of F-skatt alone does not make business income free of contributions. With FA-skatt, keep employment withholding apart from business preliminary tax. A partner in a handelsbolag pays personal preliminary tax as special A-skatt; do not assume a sole-trader F-skatt registration.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Egenavgifter (SAL part) | 16.35% of the contribution base: sickness 3.64%, parental 2.00%, old-age pension 10.21%, survivor's pension 0.30%, labour market 0.10%, work injury 0.10% | 2026 | SAL 3 kap. 13 § (Lag 2025:1362); https://data.riksdagen.se/dokument/sfs-2000-980.text |
| Allmän löneavgift on the egenavgift base | 12.62% (a tax, not an insurance charge) | 2026 | Lag (1994:1920) om allmän löneavgift 2-3 §§ (Lag 2025:1360); https://data.riksdagen.se/dokument/sfs-1994-1920.text |
| Full egenavgifter, active business, born 1959 or later, 7 waiting days | 28.97% (16.35% + 12.62%) | 2026 | SAL 3 kap. 13 §; Lag 1994:1920 3 §; https://www.skatteverket.se/egenavgifter |
| Aged 67 at 1 January 2026 (born 1938-1958) | 10.21% old-age pension contribution only; no allmän löneavgift | 2026 | SAL 3 kap. 15 § (Lag 2022:889, in force 1 January 2026); Lag 1994:1920 2 § third paragraph |
| Born 1959 or later with full old-age pension (income and premium pension) all of 2026, or full sickness or activity compensation for any part of 2026 | 10.21% | 2026 | SAL 3 kap. 16 §; Lag 1994:1920 2 § |
| Born 1937 or earlier | 0% | 2026 | SAL transitional rules (2000:980) point 6 |
| Särskild löneskatt, passive business or estate | 24.26%, no age reduction | 2026 | SLF 2 §; https://data.riksdagen.se/dokument/sfs-1990-659.text |
| No egenavgifter or särskild löneskatt | Contribution base under SEK 1,000 | 2026 | SAL 3 kap. 14 §; SLF 2 § second paragraph |
| Sickness rate by chosen waiting period, on income up to 10 price base amounts (SEK 592,000) | 1 day 3.75%; 7 days 3.64%; 14 days 3.54%; 30 days 3.34%; 60 days 3.08%; 90 days 2.90%; 3.64% above SEK 592,000 | 2026 | SAL 3 kap. 17 §; https://www.skatteverket.se/egenavgifter |
| Schablonavdrag (provisional deduction in the return) | Law: at most 25% of the base, at most 20% for passive business and estates. Skatteverket's 2026 table: 25% born 1959 or later; 10% born 1938-1958 or on full pension or sickness compensation; 0% born 1937 or earlier | 2026 | IL 16 kap. 29-30 §§; https://www.skatteverket.se/egenavgifter |
| Special deduction (särskilt avdrag) | 7.5% of the business part of the base, at most SEK 15,000 a year; only if that part exceeds SEK 40,000; not if 67 at 1 January or paying only 10.21% under SAL 3 kap. 16 §; never below the 10.21% part | 2026 | Lag (2023:748) 3 § (Lag 2023:754, in force 1 January 2026); https://data.riksdagen.se/dokument/sfs-2023-748.text |
| Regional deduction (fixed establishment in the support area) | 10% of the base from that establishment, at most SEK 18,000 a year; first from allmän löneavgift; never below the 10.21% part; SEK 85,200 cap per handelsbolag and per person combining employer and own relief | 2026 | Lag (2001:1170) 2, 4, 6, 6 a §§ (Lag 2025:1338); https://data.riksdagen.se/dokument/sfs-2001-1170.text |
| Allmän pensionsavgift | 7% of earned income (employment and active business), each type rounded down to the nearest SEK 100 | 2026 | Lag (1994:1744) om allmän pensionsavgift 2-3 §§; https://data.riksdagen.se/dokument/sfs-1994-1744.text |
| Pension fee ceiling | Income above 8.07 income base amounts is ignored: SEK 673,038, so the fee is at most SEK 47,100; business income is cut first | 2026 | Lag 1994:1744 3 § third paragraph; https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html |
| Pension fee floor | No fee if earned income is under 42.3% of the price base amount (SEK 25,041.60) | 2026 | Lag 1994:1744 4 § |
| Tax credit for the pension fee | 100% of the fee, set against municipal and state income tax and property tax and fee; a self-employed person must have paid the fee in time | 2026 | IL 67 kap. 4 §; SFL 62 kap. 17 § |
| Income base amount (inkomstbasbelopp) | SEK 83,400 | 2026 | Socialförsäkringsbalk (2010:110) 58 kap. 26-27 §§; Skatteverket belopp och procent 2026 |
| Price base amount (prisbasbelopp) | SEK 59,200 (higher amount SEK 60,500) | 2026 | Socialförsäkringsbalk 2 kap. 6-7 §§; Skatteverket belopp och procent 2026 |
| Employer contributions (staff of a sole trader) | 31.42% = 18.80% (sickness 3.55%, parental 2.00%, old-age pension 10.21%, survivor's 0.30%, labour market 2.64%, work injury 0.10%) + 12.62% allmän löneavgift | 2026 | SAL 2 kap. 26 §; Lag 1994:1920 1 and 3 §§ |
| Employer: employee aged 67 at 1 January 2026 | 10.21%; 0% for employees born 1937 or earlier | 2026 | SAL 2 kap. 27 §; SAL transitional rules point 5 |
| Employer: youth reduction, employee aged 18-22 at 1 January 2026 (born 2003-2007), pay from 1 April 2026 to 30 September 2027 | 20.81% on pay up to SEK 25,000 a calendar month; 31.42% above | 2026 | Lag (2026:100) 2 §; https://data.riksdagen.se/dokument/sfs-2026-100.text |
| Employer: växa refund (first and second employee; sole traders qualify) | Refund of all employer contributions except the 10.21% part, on pay up to SEK 35,000 a month, for the first 24 months | 2026 | Lag (2025:1334) 3, 7-8 §§; https://data.riksdagen.se/dokument/sfs-2025-1334.text |
| Employer: no contributions on small pay | Pay to one person under SEK 1,000 in the year | 2026 | SAL 2 kap. 14 § |

The 2026 components of egenavgifter changed from 2025 (parental 2.60% to 2.00%, survivor's 0.60% to 0.30%, work injury 0.20% to 0.10%, allmän löneavgift 11.62% to 12.62%), but the total stays 28.97%. From 1 January 2026 the age for the 10.21% rate is 67 at the start of the year, not 66. Someone born 1959 turns 67 during 2026 and pays the full rate for the whole year.

## The taxable base

**Start point.** The contribution base is the sum of the person's liable net incomes in the final tax decision, plus other liable net income computed as if earned by a Swedish resident (SAL 3 kap. 12 §). For a sole trader that is the business surplus after this year's schablonavdrag (NE box R47). Start from the tax-adjusted business result, not revenue, withdrawals or the bank balance, and keep a bridge from the accounts through every tax adjustment.

**Excluded from the base.**
- Sickness and rehabilitation benefit (SAL 3 kap. 10 §). In N3A it goes in box 29.
- Business receipts on which the payer owes employer contributions (SAL 3 kap. 11 §). Deduct that income less its costs. Where costs cannot be matched, split them in proportion to the two kinds of receipts. Report the excluded income and costs at point 10.5 of Inkomstdeklaration 1.
- Pay for work under SEK 1,000 in the year from one payer, but only for income that is not business income (SAL 3 kap. 9 §).

**Losses.** A deficit in one business does not reduce a surplus in another business for contribution purposes (SAL 3 kap. 12 § second paragraph). A loss never produces negative contributions. Treat loss carry-forward in the income tax computation, not here.

**The SEK 1,000 floor.** If the final base is under SEK 1,000, no egenavgifter are due. At SEK 1,000 or more the whole base is charged (SAL 3 kap. 14 §). The same floor applies to särskild löneskatt.

**Schablonavdrag, the provisional deduction.** Egenavgifter are deductible in the business (IL 16 kap. 29 §), but the year's figure is not known until the final tax decision. So the return deducts an estimate:
1. NE box R40: add back last year's allowed schablonavdrag.
2. NE box R41: deduct the egenavgifter actually charged for last year (from last year's final tax notice).
3. NE box R42: surplus before this year's deduction.
4. NE box R43: this year's schablonavdrag. Its base is R42 less sickness benefit and less income that counts as employment income for pension purposes (IL 16 kap. 30 §). Use 25% at the full rate, 10% where only 10.21% is due, 20% for passive business.

The schablonavdrag is a return adjustment, not a bookkeeping expense. Keep the before-deduction base and the final base as two separate numbers. Do the reconciliation in the return for the year after the business stops too. If a reassessment changes a year's schablonavdrag, change its reversal in R40 of the next return. If a reassessment changes the charged egenavgifter, adjust R41 in the return for the year the decision was made.

**Partners (N3A schedule).** Use the agreed tax-adjusted share, not the partnership's whole profit. Box 25 adds back last year's deduction (box 28 last year). Box 26 deducts last year's charged egenavgifter. If the person has several businesses, split the single charged amount across them in proportion to last year's results; do not deduct it twice. Box 27 totals boxes 20 to 26; a surplus there supports this year's schablonavdrag in box 28. Box 30 goes to point 10.1 (active) or 10.3 (passive) of Inkomstdeklaration 1.

**Rate route.** For the 7-day route the gross charge is base × 28.97%. With another waiting period, split the sickness part at SEK 592,000 and add the other components (25.33% in total). Seven days applies if nothing else was chosen. The person can change the waiting period at any time in the year through Försäkringskassan but cannot choose a shorter one after turning 55. Get the dates of any change.

**Special deduction (Lag 2023:748 3 §).** Deduct 7.5% of the business part of the base, at most SEK 15,000, from egenavgifter first, then allmän löneavgift. Conditions: the business part of the base is over SEK 40,000 (exactly SEK 40,000 gives nothing); the person was under 67 at 1 January; and they are not on the 10.21%-only route under SAL 3 kap. 16 §. The total may not fall below the 10.21% old-age pension part. Never for passive income. Skatteverket applies it automatically. There is no first-years-of-business condition.

**Regional deduction (Lag 2001:1170).** Applies to income from a fixed establishment inside the support area listed in the annex to the act. A postal address in a named county is not enough. Not for anyone paying only 10.21%. From 1 January 2026 it is not available for steel, lignite and coal; transport and related infrastructure; or a business mainly in finance and insurance or intra-group activity (4 §). It is de minimis aid: obtain the history of other aid before relying on it. Claim it at point 13.1 and give the NACE code at point 13.2 of Inkomstdeklaration 1, ticking the agriculture or fisheries boxes where they apply. For a handelsbolag, the partners' combined relief is capped at SEK 85,200 and split in proportion to taxable shares; employer-side regional relief shares that cap (6-6 a §§). If eligibility evidence is missing, report the charge before regional relief and list the open claim.

**Allmän pensionsavgift base.** The fee is 7% of income from employment and of income from other gainful work, which includes active business income (Socialförsäkringsbalk 59 kap. 14 §). Passive business income is not in it. Round each income type down to the nearest SEK 100. Ignore total income above SEK 673,038, cutting business income first. Round the fee to the nearest SEK 100, with SEK 50 rounded down (Lag 1994:1744 3 §). Skatteverket sets the base in the final tax decision (5 §). The fee is not deductible; it is credited in full against income tax (IL 67 kap. 4 §). The credit cannot exceed municipal and state income tax plus property tax and fee.

## Deadlines and filing

| Step | Date for income year 2026 | Source |
|---|---|---|
| Preliminary tax decision (F-skatt or special A-skatt) for the year | By 20 January 2026; nothing is debited under SEK 2,400 | SFL 55 kap. 2 § |
| Default preliminary tax | 110% of the last final tax (105% if that final tax was below the debited preliminary tax), unless a preliminary income declaration gives another figure | SFL 55 kap. 3 § |
| Monthly F-skatt payments | Equal amounts from February 2026 to January 2027; due the 12th, but the 17th in January and August (12 August if VAT turnover is above SEK 40 million) | SFL 62 kap. 4 § |
| New business deferral | First payment pushed back three months on request; not if the decision comes after the year ends, the business was taken over, the person already runs a business, or special reasons argue against it | SFL 62 kap. 7 § |
| Seasonal business | Payments only in the months the business runs, on request | SFL 62 kap. 6 § |
| Preliminary income declaration when final tax will exceed debited tax | Mandatory when the gap is significant (Skatteverket: about 30% and at least one price base amount) or the financial year changed without permission; within 14 days; not needed in the last month of the year. Can be filed until six months after the year ends | SFL 28 kap. 4-5 §§; Skatteverket preliminärskatt page |
| Extra payment to avoid cost interest on a shortfall above SEK 30,000 | On the tax account by 12 February 2027 | SFL 65 kap. 4 and 6 §§ |
| Inkomstdeklaration 1 with NE or N3A | Due 2 May 2027, a Sunday, so a return filed on Monday 3 May 2027 is on time | SFL 32 kap. 1 §; Lag (1930:173) om beräkning av lagstadgad tid 2 § |
| Final tax decision | Fixes egenavgifter, allmän löneavgift, särskild löneskatt and the allmän pensionsavgift base | SFL 56 kap. 3 § point 5 and 6 § points 2, 4, 6 |
| Payment of tax still owed | The due date that falls next after 90 days from the final tax decision | SFL 62 kap. 8 § |
| Pension fee counted as paid | Credited in proportion to preliminary tax paid; later payments count until the end of June in the second year after the income year; fees still unpaid then are not taken out | SFL 62 kap. 17 § |

Pay what the preliminary tax decision says, not an amount derived from the estimated egenavgifter alone: the decision also covers income tax. Keep paying under the current decision until a new one arrives.

## Penalties and interest

- **Late return (förseningsavgift).** SEK 1,250 for an individual's income return. A second fee is charged if the return is still missing three months after the due date, and a third after a further two months (SFL 48 kap. 1, 6-7 §§). A person living abroad on the due date who files by 31 May pays no fee (48 kap. 3 §).
- **Incorrect information (skattetillägg).** 40% of the tax that would have been lost on income tax and the allmän pensionsavgift (SFL 49 kap. 11 § with 56 kap. 3 §). 20% on other taxes, which covers egenavgifter, allmän löneavgift and särskild löneskatt (49 kap. 11 § with 56 kap. 6 §). Lower rates apply when the error is only one of timing (49 kap. 13 §).
- **Cost interest (kostnadsränta).** Basränta 2.5% from 1 December 2024 (Skatteverket). Final tax owed carries interest at the basränta from 13 February 2027. On up to SEK 30,000 there is no interest from 13 February to 3 May 2027 (SFL 65 kap. 4 and 6 §§). Late payment after a due date carries basränta plus 15 points, now 17.5% (65 kap. 13 §). Cost interest is not deductible.
- **Unpaid pension fee.** A fee not paid in time is not taken out, but the tax credit is lost (IL 67 kap. 4 §; SFL 62 kap. 17 §).

## Cross-border points

- Egenavgifter are due on liable income from work in Sweden, and on work abroad only while the person is covered by Swedish social insurance under EU/EEA rules or a social security agreement (SAL 3 kap. 2 §). EU law and agreements override the Act (SAL 1 kap. 3 §).
- Tax residence alone does not decide coverage. Before charging Swedish rates for work outside Sweden, or before leaving income out, get the coverage certificate (A1 within the EU/EEA) with its dates and covered activities. Keep foreign-covered income separate. Do not treat an unconfirmed claim of foreign coverage as an exemption.
- Where the person is covered in Sweden, income earned abroad still enters the base, computed as if earned by a Swedish resident (SAL 3 kap. 12 § point 2).
- Residence, SINK and treaty points are in [se-cross-border](se-cross-border.md).

## Worked examples

**Example 1: ordinary sole trader.** Born 1985, active business, 7 waiting days, no other income, no regional relief. Surplus before this year's deduction (R42) SEK 400,000. Schablonavdrag 25% = SEK 100,000, so the contribution base (R47) is SEK 300,000. Gross egenavgifter 300,000 × 28.97% = SEK 86,910. The business base is above SEK 40,000, so the special deduction is the lower of 7.5% × 300,000 = SEK 22,500 and SEK 15,000: SEK 15,000. Egenavgifter are SEK 71,910, above the 10.21% floor of SEK 30,630. Allmän pensionsavgift 7% × 300,000 = SEK 21,000, credited in full against income tax. Next year R40 adds back 100,000 and R41 deducts 71,910, a net SEK 28,090 added to the 2027 result.

```oa-check
name: Sweden sole trader, R42 SEK 400,000, born 1985 (2026)
inputs:
  r42: 400000
steps:
  - schablon: r42 * 0.25
  - base: r42 - schablon
  - gross: base * 0.2897
  - relief: min(base * 0.075, 15000)
  - floor_pension: base * 0.1021
  - egenavgifter: max(gross - relief, floor_pension)
  - fee_income: min(floor(base / 100) * 100, 673038)
  - pension_fee: ceil(fee_income * 0.07 / 100 - 0.5) * 100
  - next_year_net_addback: schablon - egenavgifter
expected:
  base: 300000.00
  gross: 86910.00
  relief: 15000.00
  egenavgifter: 71910.00
  pension_fee: 21000.00
  next_year_net_addback: 28090.00
```

**Example 2: 30 waiting days and the pension fee ceiling.** Born 1980, active business, 30 waiting days chosen for the whole of 2026, no other income. R42 SEK 1,000,000. Schablonavdrag 25% = SEK 250,000; base SEK 750,000. Sickness part: 592,000 × 3.34% = SEK 19,772.80, plus (750,000 − 592,000) × 3.64% = SEK 5,751.20, total SEK 25,524. Other components 25.33% × 750,000 = SEK 189,975. Gross SEK 215,499. The special deduction is capped at SEK 15,000, giving SEK 200,499. The pension fee ignores income above 8.07 × 83,400 = SEK 673,038: 7% of that is SEK 47,112.66, rounded to SEK 47,100.

```oa-check
name: Sweden sole trader, 30 waiting days, R42 SEK 1,000,000 (2026)
inputs:
  r42: 1000000
  pbb: 59200
  ibb: 83400
steps:
  - base: r42 - r42 * 0.25
  - sick_limit: 10 * pbb
  - sickness: min(base, sick_limit) * 0.0334 + max(base - sick_limit, 0) * 0.0364
  - other: base * 0.2533
  - gross: sickness + other
  - egenavgifter: max(gross - min(base * 0.075, 15000), base * 0.1021)
  - ceiling: 8.07 * ibb
  - fee_income: min(floor(base / 100) * 100, ceiling)
  - pension_fee: ceil(fee_income * 0.07 / 100 - 0.5) * 100
expected:
  base: 750000.00
  sickness: 25524.00
  gross: 215499.00
  egenavgifter: 200499.00
  ceiling: 673038.00
  pension_fee: 47100.00
```

Boundary checks from the law: a base of SEK 999 gives no egenavgifter, and SEK 1,000 gives SEK 289.70. A base of exactly SEK 40,000 gets no special deduction (SEK 11,588 gross); at SEK 40,100 the deduction is SEK 3,007.50. A passive owner born 1956 with a base of SEK 100,000 pays SEK 24,260 särskild löneskatt, with no age rate and no special deduction. A person born 1958 with an active base of SEK 180,000 pays SEK 18,378 and gets no special deduction.

## Ask the client first

1. Year of birth, and whether they had full old-age pension all of 2026 or full sickness or activity compensation at any time in 2026 (sets 28.97% or 10.21%, and the schablonavdrag).
2. Is each business active or passive, and is any income a handelsbolag share? (Sets egenavgifter or 24.26%, and NE or N3A.)
3. The chosen waiting period and the dates of any change (changes the sickness rate up to SEK 592,000).
4. Last year's allowed schablonavdrag and the egenavgifter charged in last year's final tax notice (R40 and R41, or boxes 25 and 26).
5. Any receipts on which the payer paid employer contributions, any sickness benefit, any work abroad and its coverage certificate (all change the base).
6. A fixed establishment in the support area, its NACE code and other de minimis aid received (regional deduction).

Working paper output: income year; classification and coverage evidence; base before and after the schablonavdrag; rate route and waiting period; R40/R41 or box 25/26 reconciliation; exclusions; gross components; each deduction with its floor and cap; net egenavgifter; allmän pensionsavgift and credit; preliminary tax and due dates; return due date; open items. Do not compute a Swedish charge while foreign coverage or benefit status is unresolved. If the tax-adjusted result cannot be reconciled, settle the income tax working paper first.

## Sources

| Source | URL | Read on |
|---|---|---|
| Socialavgiftslag (2000:980), 1 kap. 3 §, 2 kap. 14, 26-27 §§, 3 kap. 1-17 §§, transitional rules points 5-6 and 2025:1362 | https://data.riksdagen.se/dokument/sfs-2000-980.text | 2026-10-24 |
| Lag (1994:1920) om allmän löneavgift, 1-3 and 6 §§ | https://data.riksdagen.se/dokument/sfs-1994-1920.text | 2026-10-24 |
| Lag (1990:659) om särskild löneskatt på vissa förvärvsinkomster, 2 § | https://data.riksdagen.se/dokument/sfs-1990-659.text | 2026-10-24 |
| Lag (2023:748) om särskilt avdrag vid beräkning av egenavgifter och allmän löneavgift, 3 § and transitional rules 2023:754 | https://data.riksdagen.se/dokument/sfs-2023-748.text | 2026-10-24 |
| Lag (2001:1170) om särskilda avdrag i vissa fall vid avgiftsberäkningen, 2, 4, 5, 6, 6 a, 6 b §§ | https://data.riksdagen.se/dokument/sfs-2001-1170.text | 2026-10-24 |
| Lag (1994:1744) om allmän pensionsavgift, 2-5 §§ | https://data.riksdagen.se/dokument/sfs-1994-1744.text | 2026-10-24 |
| Socialförsäkringsbalk (2010:110), 59 kap. 14 § | https://data.riksdagen.se/dokument/sfs-2010-110.text | 2026-10-24 |
| Inkomstskattelag (1999:1229), 16 kap. 29-31 §§, 67 kap. 4 § | https://data.riksdagen.se/dokument/sfs-1999-1229.text | 2026-10-24 |
| Skatteförfarandelag (2011:1244), 28 kap. 4-5 §§, 32 kap. 1 §, 48 kap. 1-7 §§, 49 kap. 11, 13 §§, 55 kap. 2-3 §§, 56 kap. 3, 6, 8 §§, 62 kap. 4-8, 17 §§, 65 kap. 3-6, 13 §§ | https://data.riksdagen.se/dokument/sfs-2011-1244.text | 2026-10-24 |
| Lag (2026:100) om tillfälligt sänkta arbetsgivaravgifter för unga, 2 § and transitional rules | https://data.riksdagen.se/dokument/sfs-2026-100.text | 2026-10-24 |
| Lag (2025:1334) om återbetalning av vissa avgifter till växa-företag, 3, 7-8 §§ | https://data.riksdagen.se/dokument/sfs-2025-1334.text | 2026-10-24 |
| Skatteverket, egenavgifter och särskild löneskatt (2026 table, components, waiting periods, NE reconciliation, special and regional deductions, NACE at 13.2) | https://www.skatteverket.se/egenavgifter | 2026-10-24 |
| Skatteverket, belopp och procent inkomstår 2026 (income and price base amounts, pension fee max SEK 47,100, ceiling SEK 673,038) | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html | 2026-10-24 |
| Skatteverket, fyll i N3A-bilagan (boxes 25-30) | https://www.skatteverket.se/foretag/inkomstdeklaration/deklarerasomdelagareihandelsbolag/fyllain3abilagan.4.2fb39afe18dabf1e4d251d9.html | 2026-10-24 |
| Skatteverket, preliminärskatt för företag och föreningar (significant difference, six-month limit) | https://www.skatteverket.se/foretag/skatterochavdrag/skattekontobetalaochfatillbaka/preliminarskattforforetagochforeningar.4.233f91f71260075abe8800010616.html | 2026-10-24 |
| Skatteverket, ränta på skattekontot (basränta 2.5%, high rate 17.5%) | https://www.skatteverket.se/rantapaskattekontot | 2026-10-24 |

Not yet confirmed: the support-area annex to Lag 2001:1170 was not listed here, and the de minimis conditions in its 6 c § were not worked through; the statutory basis of the sickness rates for waiting periods other than 7 days (SAL 3 kap. 17 § delegates them; the figures are Skatteverket's); the statutory basis of the 10% schablonavdrag on the 10.21% route (IL sets only the 25% and 20% maximums); the later filing date for returns filed through a tax agent; how the regional and special deductions interact when both apply to the same base; whether the youth reduction and the växa refund can apply to the same pay (see sweden-payroll); and a Skatteverket page applying the 20% skattetillägg rate to egenavgifter (the rate here is read from SFL 49 kap. 11 § with 56 kap. 3 and 6 §§).

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
