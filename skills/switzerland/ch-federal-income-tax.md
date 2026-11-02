---
name: ch-federal-income-tax
description: "Swiss federal income tax for individuals (direkte Bundessteuer, impot federal direct) for tax year 2026. Covers who is liable (DBG art. 3), joint taxation of married couples, the 2026 tariffs after the cold-progression adjustment (single tariff up to 13.2% marginal and 11.5% flat from CHF 794,000; married and single-parent tariff), the CHF 263 tax reduction per child, the main deductions (commuting cap CHF 3,300, flat professional expenses, Pillar 2 and 3a, insurance premiums, private interest, childcare CHF 25,800, two-earner deduction, child and support deductions CHF 6,800), tax at source for foreign employees and the ordinary assessment from CHF 120,000, filing and payment (1 March due date, 4.00% late interest) and fines. Trigger on: Bundessteuer, DBSt, direkte Bundessteuer, Swiss federal tax, Steuertarif Bund, Kinderabzug, Zweiverdienerabzug, Säule 3a Abzug. Out of scope: ch-cantonal-tax, ch-ahv-iv, ch-payroll, ch-cross-border, ch-lump-sum."
version: 2.2
jurisdiction: CH
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Switzerland: federal income tax for individuals (direkte Bundessteuer), 2026

The Confederation levies an income tax on individuals under the Federal Act on Direct Federal Tax (DBG, SR 642.11). The cantons assess and collect it, together with their own cantonal and communal income tax, on one return. This skill covers the federal layer only. It links to the pack's other skills rather than repeating them:

- `ch-cantonal-tax`: cantonal and communal income and wealth tax, which is usually the larger part of the bill.
- `ch-ahv-iv`: AHV/IV/EO contributions of the self-employed.
- `ch-payroll`: what an employer withholds, including tax-at-source tariffs and the employer's commission.
- `ch-cross-border`: residence, arrival, departure, non-residents, the subsequent ordinary assessment (NOV) in detail, and treaties.
- `ch-lump-sum`: taxation on expenditure (Pauschalbesteuerung, DBG art. 14).

## Who this applies to

- **Residents (unlimited liability).** A person is liable on worldwide income if they have tax domicile in Switzerland (living here with the intention of staying) or tax residence: a stay of at least 30 days with work, or at least 90 days without work, ignoring short breaks (DBG art. 3). Foreign business, permanent establishments and real estate are exempt but count for the rate (DBG art. 6 and 7).
- **Non-residents (limited liability).** Taxed on Swiss sources such as a Swiss business, real estate or employment, at the rate that applies to their worldwide income (DBG art. 4, 5 and 7). See `ch-cross-border`.
- **Married couples and registered partners** living together are taxed jointly: their incomes are added up, whatever their marital property regime (DBG art. 9 para. 1 and 1bis). Children's income is added to the parent's, except their own earnings, which they are taxed on separately (DBG art. 9 para. 2).
- **Foreign employees without a settlement permit (C)** are taxed at source on employment income (DBG art. 83). This does not apply if they are married to, and living with, a Swiss citizen or C-permit holder (DBG art. 83 para. 2). See "Tax at source" below.
- **Taxation on expenditure.** Foreign nationals who do not work in Switzerland can opt for a lump-sum tax instead (DBG art. 14; minimum base CHF 435,000 in 2026). See `ch-lump-sum`.

The tax year is the calendar year (DBG art. 40). If liability starts or ends during the year, only the income of that period is taxed, but the rate on regular income is set on income converted to 12 months (DBG art. 40 para. 3).

## Rates, bands and thresholds

The tariffs and franc amounts are indexed to the consumer price index of 30 June before the tax year (DBG art. 39). For 2026 the index rose 0.06% (170.3 to 170.4 points). The Federal Department of Finance (EFD) adjusted the tariffs by ordinance of 10 September 2025 (VKP, AS 2025 579, corrected AS 2025 621); the franc deductions stayed at their 2025 amounts ([ESTV circular 2-215-D-2025](https://www.estv.admin.ch/dam/de/sd-web/vFK3ntWLQ4s4/2-215-D-2025-d.pdf)).

**Single tariff, 2026 (DBG art. 36 para. 1).** Tax at the start of each band, plus the marginal amount for each further CHF 100.

| Taxable income from (CHF) | Tax at that income (CHF) | Per further CHF 100 |
|---|---|---|
| 0 to 15,200 | 0.00 | 0.77 (above 15,200) |
| 33,200 | 138.60 | 0.88 |
| 43,500 | 229.20 | 2.64 |
| 58,000 | 612.00 | 2.97 |
| 76,200 | 1,152.50 | 5.94 |
| 82,100 | 1,502.95 | 6.60 |
| 108,900 | 3,271.75 | 8.80 |
| 141,500 | 6,140.55 | 11.00 |
| 185,100 | 10,936.55 | 13.20 |
| 793,900 | 91,298.15 | (step to the next row) |
| 794,000 | 91,310.00 | 11.50 (flat 11.5% on the whole income from here) |

**Married and single-parent tariff, 2026 (DBG art. 36 para. 2 and 2bis).**

| Taxable income from (CHF) | Tax at that income (CHF) | Per further CHF 100 |
|---|---|---|
| 0 to 29,700 | 0.00 | 1.00 (above 29,700) |
| 53,400 | 237.00 | 2.00 |
| 61,300 | 395.00 | 3.00 |
| 79,100 | 929.00 | 4.00 |
| 94,900 | 1,561.00 | 5.00 |
| 108,700 | 2,251.00 | 6.00 |
| 120,600 | 2,965.00 | 7.00 |
| 130,500 | 3,658.00 | 8.00 |
| 138,400 | 4,290.00 | 9.00 |
| 144,300 | 4,821.00 | 10.00 |
| 148,300 | 5,221.00 | 11.00 |
| 150,400 | 5,452.00 | 12.00 |
| 152,400 | 5,692.00 | 13.00 |
| 941,300 | 108,249.00 | (step to the next row) |
| 941,400 | 108,261.00 | 11.50 (flat 11.5% from here) |

Sources for both tables: [DBG art. 36](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) (version of 2 September 2026) and [ESTV Form. 58c, Tarife 2026](https://www.estv.admin.ch/dam/de/sd-web/gnde9CmEsalK/dbst-tairfe-58c-2026-dfi.pdf). The first published text had CHF 1,152.55 at CHF 76,200; the Federal Chancellery corrected it to CHF 1,152.50 on 17 October 2025 (AS 2025 621), and the ESTV table uses 1,152.50.

**Rounding.** Income below a full CHF 100 is ignored, and the annual tax is rounded down to the next 5 centimes (ESTV Form. 58c, notes 1 and 2). Tax below CHF 25 is not levied (DBG art. 36 para. 3).

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Tax reduction per child or supported person (married and single-parent tariff) | CHF 263 off the tax | 2026 | [DBG art. 36 para. 2bis](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Child deduction, per minor child or child in education | CHF 6,800 | 2026 | [DBG art. 35 para. 1 let. a](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Support deduction, per person unable to work whom the taxpayer supports | CHF 6,800 | 2026 | [DBG art. 35 para. 1 let. b](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Married couple deduction | CHF 2,800 | 2026 | [DBG art. 35 para. 1 let. c](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Two-earner deduction (married, both working) | 50% of the lower earned income, min CHF 8,600, max CHF 14,100 | 2026 | [DBG art. 33 para. 2](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Commuting costs, employees, cap | CHF 3,300 | 2026 | [DBG art. 26 para. 1 let. a](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Commuting by private car, per km | CHF 0.75 (2025: 0.70) | 2026 | [Berufskostenverordnung, annex](https://www.fedlex.admin.ch/eli/cc/1993/1363_1363_1363/de) |
| Commuting by bicycle or moped, per year | CHF 700 | 2026 | [Berufskostenverordnung, annex](https://www.fedlex.admin.ch/eli/cc/1993/1363_1363_1363/de) |
| Meals away from home, full deduction | CHF 15 a day, CHF 3,200 a year | 2026 | [Berufskostenverordnung, annex](https://www.fedlex.admin.ch/eli/cc/1993/1363_1363_1363/de) |
| Other professional expenses, flat rate | 3% of net salary, min CHF 2,000, max CHF 4,000 | 2026 | [Berufskostenverordnung, annex](https://www.fedlex.admin.ch/eli/cc/1993/1363_1363_1363/de) |
| Side job, flat rate | 20% of net income, min CHF 800, max CHF 2,400 | 2026 | [Berufskostenverordnung, annex](https://www.fedlex.admin.ch/eli/cc/1993/1363_1363_1363/de) |
| Insurance premiums and savings interest, married | CHF 3,700 (CHF 5,550 without Pillar 2 or 3a contributions) | 2026 | [DBG art. 33 para. 1 let. g and 1bis](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Insurance premiums and savings interest, others | CHF 1,800 (CHF 2,700 without Pillar 2 or 3a contributions) | 2026 | [DBG art. 33 para. 1 let. g and 1bis](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Insurance premiums, add per child or supported person | CHF 700 | 2026 | [DBG art. 33 para. 1bis let. b](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Pillar 3a, member of a pension fund | CHF 7,258 | 2026 | [BSV Masszahlen 2025/2026](https://www.bsv.admin.ch/dam/de/sd-web/GZplHByBJoFc/Internet_Masszahlenarticles_25_26_d.pdf); BVV 3 art. 7 |
| Pillar 3a, no pension fund | 20% of earned income, max CHF 36,288 | 2026 | [BSV Masszahlen 2025/2026](https://www.bsv.admin.ch/dam/de/sd-web/GZplHByBJoFc/Internet_Masszahlenarticles_25_26_d.pdf); [BVV 3 art. 7](https://www.fedlex.admin.ch/eli/cc/1985/1778_1778_1778/de) |
| Childcare by third parties, per child under 14 | Up to CHF 25,800 | 2026 | [DBG art. 33 para. 3](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Private debt interest | Up to investment income plus CHF 50,000 | 2026 | [DBG art. 33 para. 1 let. a](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Job-related training | Up to CHF 13,000 | 2026 | [DBG art. 33 para. 1 let. j](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Political party contributions | Up to CHF 10,600 | 2026 | [DBG art. 33 para. 1 let. i](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Medical costs borne by the taxpayer | Part above 5% of net income | 2026 | [DBG art. 33 para. 1 let. h](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Donations to exempt Swiss charities | From CHF 100 a year, up to 20% of net income | 2026 | [DBG art. 33a](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Tax at source: mandatory ordinary assessment (NOV) | Gross employment income of at least CHF 120,000 | 2026 | [QStV art. 9](https://www.fedlex.admin.ch/eli/cc/2018/274/de) |
| Employer's collection commission on tax at source | 1% to 2%, set by the canton | 2026 | [DBG art. 88 para. 4](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| General due date of the tax | 1 March of the following year | 2026 | [SR 642.124 art. 1](https://www.fedlex.admin.ch/eli/cc/1993/717_717_717/de) |
| Late payment and refund interest | 4.00% (2025: 4.50%) | 2026 | [ESTV circular 2-215-D-2025](https://www.estv.admin.ch/dam/de/sd-web/vFK3ntWLQ4s4/2-215-D-2025-d.pdf) |
| Interest paid on advance payments | 0.00% (2025: 0.75%) | 2026 | [ESTV circular 2-215-D-2025](https://www.estv.admin.ch/dam/de/sd-web/vFK3ntWLQ4s4/2-215-D-2025-d.pdf) |

## The taxable base

**Income.** All income is taxed unless the DBG exempts it: employment income and fringe benefits (art. 17), self-employment income (art. 18), investment income (art. 20, 20a), imputed rental value of an owner-occupied home (art. 21 para. 1 let. b), pensions and replacement income (art. 22, 23). Private capital gains on movable assets are tax-free (art. 16 para. 3). The imputed rental value is still taxed in 2026. The reform that abolishes it, accepted by voters on 28 September 2025, comes into force on 1 January 2029 (Federal Council decision of 1 April 2026), so 2026 to 2028 are taxed under the current rules, with the deductions for maintenance costs and private debt interest ([EFD press release, 1 April 2026](https://www.efd.admin.ch/de/newnsb/yGTqBPowRqyVh0zPokW-q)). Lump-sum pension payouts are taxed separately at one fifth of the tariff (art. 38); this is out of scope here.

**Employees: professional expenses (DBG art. 26).** Deductible are commuting costs up to CHF 3,300, extra costs of meals away from home and of shift work, and other necessary job costs. The EFD sets flat rates for meals and other costs (table above); the taxpayer may prove higher other costs instead of the flat 3%. Job-related training is a separate deduction under art. 33 para. 1 let. j.

**Self-employed (DBG art. 27 to 31).** Business-justified costs are deductible, including depreciation and provisions, losses on business assets, and interest on business debt. Fines and criminal-purpose payments are not. Losses carry forward for 7 years (art. 31). AHV/IV/EO contributions are deductible under art. 33 para. 1 let. d; the contribution rates are in `ch-ahv-iv`.

**General deductions (DBG art. 33 and 33a).** Private debt interest up to investment income plus CHF 50,000; maintenance payments to a separated or divorced spouse and for children in their care; AHV/IV and Pillar 2 contributions, including buy-ins; Pillar 3a within the limits above; EO, unemployment and compulsory accident premiums; other insurance premiums and savings interest within the flat caps; medical costs above 5% of net income; disability costs; party contributions; job-related training; childcare; donations.

**Two-earner deduction (DBG art. 33 para. 2).** If both spouses earn, 50% of the lower earned income is deducted, at least CHF 8,600 and at most CHF 14,100. "Earned income" is employment or self-employment income less professional or business expenses and less the art. 33 para. 1 let. d to f contributions. If one spouse works substantially in the other's business, each is allocated half of the joint earned income unless the couple proves another split.

**Social deductions (DBG art. 35).** CHF 6,800 per minor child or child in education whom the taxpayer supports (split half each between separately taxed parents with joint custody where no maintenance is deducted for the child); CHF 6,800 per supported person unable to work; CHF 2,800 for married couples. They are fixed on the facts at the end of the tax year or of liability, and given pro rata on partial liability.

**Not deductible (DBG art. 34).** Living costs of the taxpayer and family, debt repayment, purchase or improvement of assets, and income and wealth taxes.

**Tariff choice (DBG art. 36).** The single tariff applies to single, separated and divorced people without children. The married tariff applies to married couples living together and, under para. 2bis, to widowed, separated, divorced and single people who live with children or supported persons and mainly bear their maintenance. On that tariff the tax is then reduced by CHF 263 per child or supported person.

### Tax at source (Quellensteuer)

Foreign employees resident in Switzerland without a C permit pay tax at source on gross employment income, including fringe benefits and replacement income (DBG art. 83 and 84). The ESTV builds the federal share into the cantonal source-tax tariffs, which include flat amounts for professional expenses, insurance premiums and family deductions (DBG art. 85). The employer withholds, remits and is liable for the tax (DBG art. 88). Tariff codes, rates and remittance: `ch-payroll`.

- **Mandatory subsequent ordinary assessment (NOV).** If gross employment income in the year is at least CHF 120,000, or the person has income not taxed at source, they file a normal return (DBG art. 89; QStV art. 9). For a married two-earner couple, the test is met if either spouse reaches CHF 120,000 (QStV art. 9 para. 3). The spouse is assessed too. Once in the NOV, the person stays in it until source taxation ends. Tax withheld is credited without interest.
- **NOV on request.** Anyone below the triggers can ask for an ordinary assessment by 31 March of the following year, or at deregistration when leaving Switzerland (DBG art. 89a). Without it, the source tax replaces the federal income tax on employment income and no extra deductions are given later. This is how a source-taxed employee claims Pillar 3a, buy-ins or actual commuting costs.
- Part-year cases, non-residents and the quasi-resident rule: `ch-cross-border`.

## Deadlines and filing

- **Return.** One return per year covers federal, cantonal and communal income tax, filed with the cantonal tax authority. The canton sends the form or announces publicly; a taxpayer who receives nothing must still file (DBG art. 124 para. 1). The return must be complete, signed and filed on time with its attachments (art. 124 para. 2). The DBG sets no calendar date; the canton does. In Zurich the 2026 return is due **31 March 2027** ([Kantonales Steueramt Zürich, ZStB 133.1](https://www.zh.ch/de/steuern-finanzen/steuern/treuhaender/steuerbuch/steuerbuch-definition/zstb-133-1.html)). Other cantons: `ch-cantonal-tax`.
- **Source-taxed persons with other income** must request a return form by 31 March of the following year (DBG art. 89 para. 4).
- **Payment.** The 2026 tax falls due on **1 March 2027** (general due date, SR 642.124 art. 1). The canton issues a provisional bill if the assessment is not yet made, based on the return, the last assessment or the likely amount (DBG art. 162). It must be paid within 30 days of the due date (DBG art. 163). Cantons may collect in instalments in advance (DBG art. 161 para. 1; SR 642.124 art. 2). Overpayments are refunded and underpayments collected after the final assessment (art. 162 para. 3).
- **Assessment period.** The right to assess expires 5 years after the end of the tax year, and in any case after 15 years (DBG art. 120).
- **Records.** Self-employed people must attach their accounts or, with simplified bookkeeping, statements of income, expenses, assets and private drawings (DBG art. 125 para. 2).

## Penalties and interest

- **Late payment interest.** 4.00% a year for 2026, starting 30 days after the definitive or provisional bill is delivered (DBG art. 164; SR 642.124 art. 3; [ESTV circular 2-215-D-2025](https://www.estv.admin.ch/dam/de/sd-web/vFK3ntWLQ4s4/2-215-D-2025-d.pdf)). Refunds of overpaid tax carry the same 4.00%. Voluntary advance payments earn 0.00% in 2026.
- **Failure to file or other procedural breaches** after a reminder: fine up to CHF 1,000, up to CHF 10,000 in serious cases or on repeat (DBG art. 174). The authority can also assess at its discretion (DBG art. 130 para. 2).
- **Tax evasion.** The fine is normally once the evaded tax; it can be cut to one third for slight fault or raised to three times for serious fault (DBG art. 175 para. 2). Attempted evasion: two thirds of that fine (DBG art. 176). The back tax and interest are due on top (DBG art. 151).
- **Voluntary disclosure.** A first self-disclosure is fine-free if no tax authority knew of the evasion, the taxpayer cooperates fully on the back tax, and makes a serious effort to pay it. Later disclosures: fine of one fifth of the evaded tax (DBG art. 175 para. 3 and 4).
- **Employers** who fail to withhold tax at source commit evasion under DBG art. 175 para. 1; see `ch-payroll`.

## Cross-border points

- **Exemption with progression.** Foreign business income, foreign permanent establishments and foreign real estate are exempt, but worldwide income sets the rate (DBG art. 6 and 7). Ask for the foreign figures even where they are not taxed.
- **Swiss withholding tax (Verrechnungssteuer).** 35% is withheld on Swiss dividends and interest. A resident gets it back by declaring the income; it is not a final tax. See `ch-cross-border`.
- **Arrivals and departures.** Liability starts or ends with residence. Regular income is annualised for the rate (DBG art. 40 para. 3). The tax falls due when a taxpayer prepares to leave Switzerland for good (DBG art. 161 para. 4 let. a). Detail: `ch-cross-border`.
- **Non-resident employees** of Swiss employers are taxed at source, finally, unless they qualify for an NOV on request (DBG art. 91 and 99a). Frontier workers from Germany, France, Italy and Austria follow special rules: `ch-cross-border` and `germany-to-switzerland-cross-border-tax`.
- **Treaties.** Switzerland's double tax treaties override the DBG where they allocate taxing rights. Foreign tax on income Switzerland taxes is not deductible as a tax (DBG art. 34 let. e), but non-recoverable foreign withholding tax on movable private assets is deductible (DBG art. 32 para. 1).

## Worked examples

### Example 1: single person, taxable income CHF 100,000

A single person with no children has taxable income of CHF 100,000 after all deductions. The single tariff applies. The income falls in the band starting at CHF 82,100, where the tax is CHF 1,502.95, plus CHF 6.60 for each further CHF 100.

The excess is 100,000 - 82,100 = CHF 17,900, which is 179 steps of CHF 100. Tax: 1,502.95 + 179 x 6.60 = 1,502.95 + 1,181.40 = **CHF 2,684.35**. This matches the ESTV 2026 table. The effective federal rate is 2.68%; the marginal rate is 6.6%. Cantonal and communal tax come on top (`ch-cantonal-tax`).

```oa-check
name: Single, taxable income CHF 100,000, federal tax 2026
inputs:
  taxable_income: 100000
  band_start: 82100
  tax_at_band_start: 1502.95
  per_100: 6.60
steps:
  - steps_of_100: floor((taxable_income - band_start) / 100)
  - tax_raw: tax_at_band_start + steps_of_100 * per_100
  - tax: floor(tax_raw * 20) / 20
  - effective_rate_pct: round(tax / taxable_income * 100, 2)
expected:
  steps_of_100: 179
  tax: 2684.35
  effective_rate_pct: 2.68
```

### Example 2: married couple with two children, taxable income CHF 150,000

A married couple living together with two minor children has joint taxable income of CHF 150,000. That figure is already after the two child deductions (2 x CHF 6,800), the married couple deduction (CHF 2,800) and any two-earner deduction. The married tariff applies.

The income falls in the band starting at CHF 148,300, where the tax is CHF 5,221.00, plus CHF 11.00 for each further CHF 100. The excess is 150,000 - 148,300 = CHF 1,700, which is 17 steps. Tariff tax: 5,221 + 17 x 11 = CHF 5,408.00.

The edge case: children count twice, once as an income deduction and again as a reduction of the tax itself. DBG art. 36 para. 2bis cuts the tax by CHF 263 per child: 2 x 263 = CHF 526. Federal tax: 5,408 - 526 = **CHF 4,882.00**, an effective rate of 3.25%. Leaving out the CHF 263 reduction is a common error in hand computations.

```oa-check
name: Married, two children, taxable income CHF 150,000, federal tax 2026
inputs:
  taxable_income: 150000
  band_start: 148300
  tax_at_band_start: 5221
  per_100: 11
  children: 2
  reduction_per_child: 263
steps:
  - steps_of_100: floor((taxable_income - band_start) / 100)
  - tariff_tax: tax_at_band_start + steps_of_100 * per_100
  - child_reduction: children * reduction_per_child
  - tax: floor((tariff_tax - child_reduction) * 20) / 20
  - effective_rate_pct: round(tax / taxable_income * 100, 2)
expected:
  steps_of_100: 17
  tariff_tax: 5408.00
  child_reduction: 526.00
  tax: 4882.00
  effective_rate_pct: 3.25
```

## Ask the client first

1. Marital status and household on 31 December 2026: married or registered and living together, single, separated, divorced or widowed, and whether children or supported persons live with them. This picks the tariff and the CHF 263 reductions.
2. Residence permit and nationality (and the spouse's): a B or L permit means tax at source, and then whether gross employment income reaches CHF 120,000.
3. Canton and commune of residence on 31 December, which sets the filing deadline and the cantonal tax.
4. Pension fund membership, for the Pillar 3a limit (CHF 7,258 or up to CHF 36,288), and any Pillar 2 buy-ins.
5. Both spouses' earned income, for the two-earner deduction, and childcare costs for children under 14.
6. Any foreign income, business or real estate, which is exempt but sets the rate.

## Sources

| Source | URL | Read on |
|---|---|---|
| Bundesgesetz über die direkte Bundessteuer (DBG), SR 642.11, version of 2 September 2026 (and of 1 January 2026), art. 3 to 9, 14, 16 to 40, 83 to 89a, 120, 124, 130, 161 to 164, 174 to 176 | https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de | 2026-10-23 |
| Verordnung des EFD über die kalte Progression (VKP) of 10 September 2025, AS 2025 579 | https://www.fedlex.admin.ch/eli/oc/2025/579/de | 2026-10-23 |
| Berichtigung of the VKP, art. 2 para. 1, of 17 October 2025, AS 2025 621 | https://www.fedlex.admin.ch/eli/oc/2025/621/de | 2026-10-23 |
| ESTV, Form. 58c, Tarife direkte Bundessteuer 2026 | https://www.estv.admin.ch/dam/de/sd-web/gnde9CmEsalK/dbst-tairfe-58c-2026-dfi.pdf | 2026-10-23 |
| ESTV, Rundschreiben 2-215-D-2025, kalte Progression und Zinssätze für das Steuerjahr 2026, 11 September 2025 | https://www.estv.admin.ch/dam/de/sd-web/vFK3ntWLQ4s4/2-215-D-2025-d.pdf | 2026-10-23 |
| ESTV, Steuertarife zur direkten Bundessteuer | https://www.estv.admin.ch/de/steuertarife-zur-direkten-bundessteuer | 2026-10-23 |
| Verordnung des EFD über den Abzug der Berufskosten (Berufskostenverordnung), SR 642.118.1, version of 1 January 2026, annex | https://www.fedlex.admin.ch/eli/cc/1993/1363_1363_1363/de | 2026-10-23 |
| Verordnung des EFD über Fälligkeit und Verzinsung der direkten Bundessteuer, SR 642.124, art. 1 to 3 | https://www.fedlex.admin.ch/eli/cc/1993/717_717_717/de | 2026-10-23 |
| Quellensteuerverordnung (QStV), SR 642.118.2, version of 10 January 2025 (current), art. 9 | https://www.fedlex.admin.ch/eli/cc/2018/274/de | 2026-10-23 |
| Verordnung über die steuerliche Abzugsberechtigung für Beiträge an anerkannte Vorsorgeformen (BVV 3), SR 831.461.3, art. 7 | https://www.fedlex.admin.ch/eli/cc/1985/1778_1778_1778/de | 2026-10-23 |
| BSV, Wichtige Masszahlen im Bereich der beruflichen Vorsorge 2025 und 2026 | https://www.bsv.admin.ch/dam/de/sd-web/GZplHByBJoFc/Internet_Masszahlenarticles_25_26_d.pdf | 2026-10-23 |
| EFD, Bundesrat setzt Abschaffung des Eigenmietwerts auf 2029 in Kraft, press release of 1 April 2026 | https://www.efd.admin.ch/de/newnsb/yGTqBPowRqyVh0zPokW-q | 2026-10-23 |
| Kantonales Steueramt Zürich, ZStB 133.1, Fristen Steuererklärung | https://www.zh.ch/de/steuern-finanzen/steuern/treuhaender/steuerbuch/steuerbuch-definition/zstb-133-1.html | 2026-10-23 |

Not yet confirmed: how the two-earner deduction applies when the lower earned income is below the CHF 8,600 minimum (the DBG text gives only the minimum; ESTV practice was not read); filing deadlines and instalment practice in cantons other than Zurich; retroactive Pillar 3a top-up contributions (not read).

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
