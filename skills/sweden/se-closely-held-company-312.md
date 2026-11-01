---
name: se-closely-held-company-312
description: "Use for the Swedish 3:12 rules for an individual who owns qualified shares (kvalificerade andelar) in a closely held company (fåmansföretag) for income year 2026, filed on form K10 with the 2027 return. Covers what a fåmansföretag and a qualified share are, the new single gränsbelopp rule from 2026 (grundbelopp of four income base amounts, SEK 322,400; wage-based amount of 50% of the payroll above eight income base amounts; interest of 11.55% on cost above SEK 100,000; saved dividend space with no uplift), dividends within the limit taxed at 20%, the excess taxed as earned income up to SEK 7,506,000, gains on qualified shares, losses, and the 3 May 2027 deadline. Trigger on: 3:12, fåmansföretag, K10, gränsbelopp, grundbelopp, lönebaserat utrymme, sparat utdelningsutrymme, utdelning aktiebolag, kvalificerade andelar. Out of scope: se-corporate-tax, se-employee-income-tax, se-capital-gains, sweden-payroll, se-cross-border."
version: 0.2
jurisdiction: SE
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sweden: the 3:12 rules for owners of closely held companies (income year 2026)

> **General reference only.** A source-cited draft, not reviewed by an accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Sweden.

This skill splits a dividend from, or a gain on, qualified shares in a closely held company between capital income and earned income. The law is chapters 56 and 57 of Inkomstskattelagen (1999:1229), "IL" below, as amended by Lag (2025:1361). That law came into force on 1 January 2026 and applies from income year 2026, so a dividend received in 2026 is reported on form K10 in the return filed in 2027 under the new rules.

Related skills in this pack. The company's own tax is in [se-corporate-tax](se-corporate-tax.md). Tax on the owner's salary, the basic deduction, municipal and state tax are in [se-employee-income-tax](se-employee-income-tax.md). Salary withholding and employer contributions are in [sweden-payroll](sweden-payroll.md). Gains on shares that are not qualified are in [se-capital-gains](se-capital-gains.md). Non-resident owners and kupongskatt are in [se-cross-border](se-cross-border.md).

## Who this applies to

**Which year's rules.** The new rules apply to tax years beginning after 31 December 2025 (Lag 2025:1361, transitional point 2). Skatteverket treats a dividend as received on the day the shareholders' meeting decides it, not on the payment date (Skatteverket, Utdelning från ditt fåmansföretag). So:

- a dividend decided in 2025 belongs to income year 2025, the 2026 return, and the old rules (the simplification rule of 2.75 income base amounts, SEK 209,550, or the main rule with its salary requirement; saved space uplifted by 104.96%);
- a dividend decided in 2026 belongs to income year 2026, the return due in May 2027, and the rules in this skill.

Three parts of the reform start later. The new wording of 57 kap. 3, 4 and 5 §§ (the extended definition, the qualification test and the outsider rule, with their periods cut from five years to four) applies only from income year 2027 (transitional point 5). For 2026 those tests still look back five years. The old 57 kap. 12 § second paragraph, 21 § second paragraph and 25-35 §§ still apply to tax years beginning before 1 January 2029 (transitional point 6); Skatteverket describes these as the index and capital-base rules for shares acquired before 1990 or 1992.

**Closely held company (fåmansföretag).** An aktiebolag or ekonomisk förening where four or fewer owners hold shares carrying more than 50% of the votes, or where the business is split into independent activities each controlled by one person (IL 56 kap. 2 §). A person and their close relatives count as one owner (56 kap. 5 §). Close relatives are parents, grandparents, spouse, children and grandchildren and their spouses, and siblings and their spouses and children (Skatteverket). For the 3:12 rules, owners who are or were active to a significant extent in the company count as one owner too (57 kap. 3 §). Listed companies and housing companies (privatbostadsföretag) are never fåmansföretag (56 kap. 3 §).

**Qualified share (kvalificerad andel).** A share in a fåmansföretag is qualified if the owner or a close relative was active to a significant extent (verksam i betydande omfattning) in the company, or in a fåmansföretag it owns or that runs the same or similar business, during the year or the five years before (57 kap. 4 § as it applies to 2026). In 2027 the look-back becomes four years.

- **Outsider rule.** If outsiders own a significant part of the company and are entitled to dividends, a share is qualified only if there are special reasons (57 kap. 5 §). Skatteverket's practice is outsiders holding at least 30%, looking at the year and the five years before.
- **Company stops being a fåmansföretag**, for example on listing. Shares that were qualified then stay qualified for at most four years after, from income year 2026 (57 kap. 6 §; five years before).
- **A dead owner's estate.** The shares stay qualified and the heirs are treated as close relatives (57 kap. 4 §).

A shareholder whose shares are not qualified reports a dividend from a fåmansföretag on form K12, not K10 (Skatteverket).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Law in force | Lag (2025:1361), in force 1 January 2026, first applied to tax years beginning after 31 December 2025 | 2026 | https://data.riksdagen.se/dokument/sfs-1999-1229.text |
| Income base amount used for the gränsbelopp (the year before the income year) | SEK 80,600 (2025) | 2026 | https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/famansforetag/andradereglerinforinkomstdeklarationen2027.4.4a54dc8b19aa6175a152359.html; IL 57 kap. 9 § |
| Grundbelopp (4 income base amounts), split equally over all shares in the company; one per owner across all companies | SEK 322,400 | 2026 | https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/famansforetag/beloppochprocentsatser.4.34f3b0b713e2cf5455b7288.html; IL 57 kap. 11 and 11 a §§ |
| Grundbelopp for income year 2027 | SEK 333,600 | 2027 | same K10 page |
| Wage-based amount (lönebaserat utrymme) | 50% of the owner's share of last year's payroll above 8 income base amounts | 2026 | IL 57 kap. 16 § |
| Deduction from the payroll (8 income base amounts) | SEK 644,800 | 2026 | Skatteverket, ändrade regler page |
| Cap on the wage-based amount | 50 times the cash pay the owner or a close relative took from the company and its subsidiaries in 2025 | 2026 | IL 57 kap. 16 § |
| Interest on cost basis | Government borrowing rate at 30 November 2025 (2.55%) plus 9 points = 11.55%, on the part of the cost above SEK 100,000 | 2026 | K10 page; IL 57 kap. 8 and 11 §§ |
| Saved dividend space (sparat utdelningsutrymme) | Carried forward at face value; no uplift from income year 2026 (2025: uplift of 104.96%) | 2026 | Skatteverket, ändrade regler and K10 pages; IL 57 kap. 13 § |
| Dividend within the gränsbelopp | Two thirds taken up as capital income at 30%: 20% of the dividend | 2026 | IL 57 kap. 20 §; https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/famansforetag/raknautskattenpadinutdelning.4.b1014b415f3321c0de27ce.html |
| Dividend above the gränsbelopp | Earned income (tjänst) at municipal and state rates | 2026 | IL 57 kap. 20 § |
| Cap on dividends taxed as earned income (90 income base amounts of the income year), per company, owner and close relatives together | SEK 7,506,000; the rest is capital income at 30% in full | 2026 | K10 page; IL 57 kap. 20 a §; 42 kap. 15 a § |
| Cap on gains taxed as earned income (100 income base amounts), year of sale and five years before, owner and close relatives together | SEK 8,340,000 | 2026 | K10 page; IL 57 kap. 22 § |
| Loss on qualified shares | Two thirds deductible against gains on shares; any rest two thirds of 70% against other capital income | 2026 | IL 48 kap. 20 and 20 a §§ |
| Late filing fee (individual) | SEK 1,250; a second after three months; a third after two more | 2026 | SFL 48 kap. 6-7 §§, https://data.riksdagen.se/dokument/sfs-2011-1244.text |

## The taxable base

**The gränsbelopp.** For each qualified share the limit is this year's amount plus saved dividend space (IL 57 kap. 10 §). From 2026 there is one rule; the old choice between the simplification rule and the main rule is gone (Skatteverket). This year's amount (57 kap. 11 §) is the sum of:

1. **Grundbelopp.** Four income base amounts of the year before (SEK 322,400 for 2026), split equally over every share in the company. An owner of 50% gets SEK 161,200. An owner with qualified shares in several companies may use only one grundbelopp in total. If the shares of the grundbelopp across companies add up to more, the grundbelopp is split in proportion to the holdings (11 a §).
2. **Wage-based amount.** The payroll (löneunderlag) is the cash pay taxed as employment income that the company and its subsidiaries paid their employees in 2025 (57 kap. 17 §). It excludes benefits in kind, expense allowances, amounts taxed under 57 kap., pay covered by state wage grants (18 §) and pay in companies owned through an alternative investment fund (17 a §). Pay to employees abroad counts if the company is in the EEA. Take the owner's share of the payroll, deduct eight income base amounts (SEK 644,800), and take 50% (16 §). The result is capped at 50 times the cash pay the owner or a close relative took from the company group in 2025. The old 4% holding requirement and the salary requirement were removed, but the cap still means someone in the family must have taken cash pay in 2025, or the amount is nil. Spouses who both own shares at 1 January compute it jointly and then split it over their shares (16 §). An owner who held the shares for part of 2025 counts only pay from that period (16 a §).
3. **Interest on cost basis.** The cost basis (omkostnadsbelopp) of the owner's shares, computed as if sold on 1 January, less contributions not meant to stay in the company (57 kap. 12 §). Interest is 11.55% of the part above SEK 100,000 (11 §). A founder with SEK 25,000 of share capital gets nothing here.

The owner must hold the shares at 1 January 2026 to get this year's amount; the year of start-up gives none, and neither do shares bought during the year (57 kap. 11 §; Skatteverket).

**Saved dividend space.** Any gränsbelopp not used is carried forward, even through years in which the shares are not qualified (57 kap. 13 §). From 2026 it is no longer uplifted by interest. If the shares pass by inheritance, gift or division of marital property, the new owner takes over the saved space and the right to this year's amount (11 and 14 §§). Skatteverket recommends filing a K10 every year, even without a dividend, to keep track of the saved space.

**Dividend.** Up to the gränsbelopp, two thirds of the dividend is capital income (57 kap. 20 §), so the tax is 20%. The excess is earned income in the inkomstslag tjänst, added to salary and taxed at the municipal rate plus 20% state tax above SEK 643,000 of taxable earned income. That computation is in [se-employee-income-tax](se-employee-income-tax.md). The earned-income part stops once the owner and close relatives have taken up SEK 7,506,000 in tjänst from the company in 2026 (20 a §). Anything above is capital income at 30% in full, because the five-sixths rule for unlisted shares does not apply to qualified shares (42 kap. 15 a §). Earned income from 57 kap. is left out when testing the cap on the basic deduction (63 kap. 5 §).

**Spouse rule.** If the owner's spouse is or was active in the company in the last five years and the owner's own taxable earned income, ignoring the 3:12 income, is lower than the spouse's, state tax on the 3:12 income is computed as if the owner had the spouse's income (57 kap. 36 §). For an owner aged 18 or under, the parents replace the spouse.

**Gain on a sale.** Compute the gain as for other shares: price less selling costs less cost basis (Skatteverket). The gain up to the gränsbelopp left after any dividend that year (this year's amount plus saved space, less the year's dividend) is taken up at two thirds in capital, 20% tax (57 kap. 13 and 21 §§). The excess is earned income, until the owner and close relatives have taken up SEK 8,340,000 in tjänst from that company over the year of sale and the five years before (22 §). The rest is capital income at 30%. A sale includes the company's bankruptcy or liquidation. A gain taxed as passive business income under 49 a kap. is outside these rules (23 §).

**Loss on a sale.** Two thirds of the loss is deducted against gains on shares in the same year; whatever is left is deducted at two thirds of 70% against other capital income (48 kap. 20 and 20 a §§).

## Deadlines and filing

- Form K10 is attached to the owner's Inkomstdeklaration 1. For income year 2026 it is due by 2 May 2027 (SFL 32 kap. 1 §), and because that is a Sunday, Monday 3 May 2027 is on time (Lag 1930:173, 2 §). Late filing, residual tax and payment dates are in [se-employee-income-tax](se-employee-income-tax.md).
- The company reports the dividend on control statement KU31 and must tick box 061 (fåmansföretag). Without the tick the dividend can be pre-filled and taxed twice (Skatteverket).
- A company can only pay a dividend after its first financial year is closed, from free equity, on a decision of the shareholders' meeting (Skatteverket). There is no dividend in the year of start-up.
- The company's own return and kupongskatt are in [se-corporate-tax](se-corporate-tax.md).

## Penalties and interest

- Late filing: SEK 1,250, a second SEK 1,250 three months after the deadline, a third two months later (SFL 48 kap. 6-7 §§).
- Tax surcharge (skattetillägg) on an incorrect statement, for example a dividend put in capital that belongs in tjänst: 40% of the tax that would have been lost (SFL 49 kap. 11 §).
- Cost interest on residual tax: see [se-employee-income-tax](se-employee-income-tax.md).

## Cross-border points

- The 3:12 split applies to owners taxed in Sweden on worldwide income. A non-resident owner's dividend from a Swedish company is taxed through kupongskatt at 30%, reduced by treaty, not under 57 kap.; see [se-cross-border](se-cross-border.md).
- An owner who leaves Sweden stays liable on gains on Swedish shares for ten years under IL 3 kap. 19 §, subject to the treaty ([se-cross-border](se-cross-border.md)).
- Pay to employees abroad counts in the payroll only if the company belongs in an EEA state (57 kap. 17 §).
- A close relative's dividend or gain taxed in another EEA state counts toward the 90 and 100 income base amount caps if it was taxed as it would have been in Sweden (57 kap. 20 a and 22 §§).

## Worked examples

### Example 1: sole owner-manager, dividend within the gränsbelopp

Lisa has owned all the shares in Lisa Konsult AB since 2019 and works in it full time, so the shares are qualified. She paid SEK 25,000 for them. In 2025 the company paid cash pay of SEK 1,200,000: SEK 720,000 to Lisa and SEK 480,000 to one employee. Her saved dividend space from her 2025 K10 is SEK 100,000. The annual meeting in May 2026 decides a dividend of SEK 500,000. Her 2026 salary is taxed as employment income ([se-employee-income-tax](se-employee-income-tax.md)) and does not change this computation.

- Grundbelopp: 4 × 80,600 = SEK 322,400, all of it because she owns every share.
- Wage-based amount: (1,200,000 − 8 × 80,600) × 50% = (1,200,000 − 644,800) × 50% = SEK 277,600. The cap, 50 × 720,000 = SEK 36,000,000, does not bite.
- Interest on cost: her cost of SEK 25,000 is below SEK 100,000, so nil.
- Gränsbelopp: 322,400 + 277,600 + 0 + 100,000 = SEK 700,000.
- The dividend of SEK 500,000 is all within the limit. Two thirds, SEK 333,333.33, is capital income taxed at 30%: SEK 100,000, which is 20% of the dividend.
- Saved dividend space to 2027: 700,000 − 500,000 = SEK 200,000, with no uplift.

```oa-check
name: Sole owner, dividend SEK 500,000 within the 2026 gränsbelopp
inputs:
  ibb_prev: 80600
  owner_share: 1
  payroll_prev: 1200000
  owner_cash_pay_prev: 720000
  cost_basis: 25000
  borrowing_rate: 0.0255
  saved_space: 100000
  dividend: 500000
steps:
  - grundbelopp: 4 * ibb_prev * owner_share
  - wage_based: min(max(payroll_prev * owner_share - 8 * ibb_prev, 0) * 0.5, 50 * owner_cash_pay_prev)
  - cost_interest: max(cost_basis - 100000, 0) * (borrowing_rate + 0.09)
  - gransbelopp: grundbelopp + wage_based + cost_interest + saved_space
  - within_limit: min(dividend, gransbelopp)
  - taxable_capital: within_limit * 2 / 3
  - tax_capital: taxable_capital * 0.30
  - saved_next_year: gransbelopp - within_limit
expected:
  grundbelopp: 322400.00
  wage_based: 277600.00
  cost_interest: 0.00
  gransbelopp: 700000.00
  taxable_capital: 333333.33
  tax_capital: 100000.00
  saved_next_year: 200000.00
```

### Example 2: dividend above the gränsbelopp, split between capital and earned income

Erik owns all the shares in Erik Bygg AB and works in it. His cost basis is SEK 300,000 (share capital plus an unconditional shareholder contribution). The company's only pay in 2025 was Erik's own salary of SEK 600,000. He has no saved dividend space. In 2026 he again takes a salary of SEK 600,000 and the meeting decides a dividend of SEK 1,000,000. He is under 66, lives in a kommun at the 2026 average rate of 32.38%, has no spouse in the company and no other income.

- Grundbelopp: SEK 322,400.
- Wage-based amount: 600,000 is below 644,800, so nil.
- Interest on cost: (300,000 − 100,000) × 11.55% = SEK 23,100.
- Gränsbelopp: 322,400 + 0 + 23,100 = SEK 345,500.
- Capital part: SEK 345,500 at two thirds = SEK 230,333.33, tax at 30% = SEK 69,100.
- Earned income part: 1,000,000 − 345,500 = SEK 654,500. It is far below the SEK 7,506,000 cap, so all of it is taxed in tjänst.
- Taxable earned income without the dividend: 600,000 − 17,400 basic deduction = SEK 582,600. With it: 582,600 + 654,500 = SEK 1,237,100. The basic deduction stays at its SEK 17,400 floor either way.
- Extra municipal tax: 654,500 × 32.38% = SEK 211,927.10.
- Extra state tax: (1,237,100 − 643,000) × 20% = SEK 118,820. Without the dividend he paid no state tax.
- His job tax credit is already at its flat top amount at SEK 600,000 of pay, so the dividend does not change it.
- Tax caused by the dividend: 69,100 + 211,927.10 + 118,820 = SEK 399,847.10, about 40% of the dividend. Burial and church fees are left out.

```oa-check
name: Dividend SEK 1,000,000 above a SEK 345,500 gränsbelopp (2026)
inputs:
  ibb_prev: 80600
  payroll_prev: 600000
  owner_cash_pay_prev: 600000
  cost_basis: 300000
  borrowing_rate: 0.0255
  saved_space: 0
  dividend: 1000000
  salary: 600000
  basic_deduction: 17400
  municipal_rate: 0.3238
  state_threshold: 643000
  cap_tjanst: 7506000
steps:
  - grundbelopp: 4 * ibb_prev
  - wage_based: min(max(payroll_prev - 8 * ibb_prev, 0) * 0.5, 50 * owner_cash_pay_prev)
  - cost_interest: max(cost_basis - 100000, 0) * (borrowing_rate + 0.09)
  - gransbelopp: grundbelopp + wage_based + cost_interest + saved_space
  - within_limit: min(dividend, gransbelopp)
  - tax_capital: within_limit * 2 / 3 * 0.30
  - excess_tjanst: min(dividend - within_limit, cap_tjanst)
  - taxable_without: salary - basic_deduction
  - taxable_with: taxable_without + excess_tjanst
  - extra_municipal: excess_tjanst * municipal_rate
  - extra_state: (max(taxable_with - state_threshold, 0) - max(taxable_without - state_threshold, 0)) * 0.20
  - total_dividend_tax: tax_capital + extra_municipal + extra_state
expected:
  cost_interest: 23100.00
  gransbelopp: 345500.00
  tax_capital: 69100.00
  excess_tjanst: 654500.00
  extra_municipal: 211927.10
  extra_state: 118820.00
  total_dividend_tax: 399847.10
```

## Ask the client first

1. When did the shareholders' meeting decide the dividend, and on what payment date? A 2025 decision falls under the old rules and the 2026 return; a 2026 decision under this skill and the 2027 return.
2. How many shares does the client hold, of how many in total, and did they own them at 1 January 2026? Do they hold qualified shares in any other company? This sets the share of the grundbelopp and whether it must be split.
3. What cash pay did the company and its subsidiaries pay in 2025, and how much of it went to the client or a close relative? This sets the wage-based amount and its cap.
4. What is the cost basis of the shares, including unconditional shareholder contributions? Only the part above SEK 100,000 earns interest.
5. What saved dividend space is on the client's last K10? Without it, the gränsbelopp may be too low.
6. Has the client or a relative worked in the company in 2021-2026, and are there outside owners? This decides whether the shares are qualified at all.

## Sources

| Source | URL | Read on |
|---|---|---|
| Inkomstskattelag (1999:1229), consolidated to SFS 2026:1393: 56 kap. 2-6 §§; 57 kap. 2-24, 36 §§; 42 kap. 15 a §; 48 kap. 20-20 a §§; 63 kap. 5 §; transitional provisions to Lag (2025:1361) | https://data.riksdagen.se/dokument/sfs-1999-1229.text | 2026-10-23 |
| Skatteförfarandelag (2011:1244): 32 kap. 1 §; 48 kap. 6-7 §§; 49 kap. 11 § | https://data.riksdagen.se/dokument/sfs-2011-1244.text | 2026-10-23 |
| Skatteverket: Ändrade regler för delägare i fåmansföretag inför inkomstdeklarationen 2027 | https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/famansforetag/andradereglerinforinkomstdeklarationen2027.4.4a54dc8b19aa6175a152359.html | 2026-10-23 |
| Skatteverket: Belopp och procentsatser (blankett K10) | https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/famansforetag/beloppochprocentsatser.4.34f3b0b713e2cf5455b7288.html | 2026-10-23 |
| Skatteverket: Räkna ut skatten på din utdelning (20% within the limit, takbelopp; describes the 2025 rules) | https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/famansforetag/raknautskattenpadinutdelning.4.b1014b415f3321c0de27ce.html | 2026-10-23 |
| Skatteverket: Fåmansföretag och kvalificerade andelar (close relatives, five-year test, outsider rule) | https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/famansforetag/famansforetagochkvalificeradeandelar.4.6efe6285127ab4f1d2580001532.html | 2026-10-23 |
| Skatteverket: Utdelning från ditt fåmansföretag (dividend date, K10 or K12, KU31 box 061) | https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/famansforetag/utdelningfrandittfamansforetag.4.b1014b415f3321c0de27b1.html | 2026-10-23 |
| Skatteverket: Försäljning av kvalificerade aktier, konkurs eller likvidation | https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/famansforetag/forsaljningavkvalificeradeaktierkonkursellerlikvidation.4.b1014b415f3321c0de2820.html | 2026-10-23 |
| Skatteverket: Belopp och procent inkomstår 2026 (statslåneränta 2.55%, income base amount 2026 SEK 83,400) | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html | 2026-10-23 |

Not yet confirmed: the wording of the repealed 57 kap. 12 § second paragraph, 21 § second paragraph and 25-35 §§ that still apply until 2028 (data.riksdagen.se shows only the current text; Skatteverket calls them the index and capital-base rules for shares bought before 1990 or 1992); the new wording of the outsider rule in 57 kap. 5 § beyond the shorter four-year period from 2027; whether the 30% outsider threshold stays Skatteverket's practice under the new wording; whether a foreign company can be a fåmansföretag for a Swedish resident owner; that the part of a dividend taxed in tjänst carries no social contributions and is not pensionable income (socialavgiftslagen and socialförsäkringsbalken not read); the K10 form version for income year 2026, not yet published on 23 October 2026.

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
