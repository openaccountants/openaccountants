---
name: sr-income-tax
description: "Suriname personal income tax (inkomstenbelasting) and wage tax (loonbelasting) for individuals, tax year 2026, under the Wet Inkomstenbelasting 1922 and the Wet Loonbelasting as amended, including Staatsbesluit S.B. 2024 no. 2. Covers residence (wonen in Suriname) and non-residents, the SRD 108,000 tax-free amount (belastingvrije som), the 8%, 18%, 28% and 38% bands, the 4% professional-expense deduction capped at SRD 4,800, the vacation allowance, bonus and child allowance exclusions, the special 5% to 35% rate for one-off payments and the overtime rate on request, deductions (mortgage interest, annuity premiums, medical costs), loss carry-forward, the provisional return by 15 April with four instalments, the definitive return within four months, the online portal, penalties and interest. Trigger on: Suriname income tax, inkomstenbelasting Suriname, loonbelasting tarief, belastingvrije som 108.000, voorlopige aangifte IB, definitieve aangifte, SRD tax, Belastingdienst Suriname. Out of"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sr-income-tax"
  jurisdiction: "SR"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Suriname personal income tax and wage tax (2026) v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill works out the income tax of an individual in Suriname for the 2026 tax year (the calendar year, 1 January to 31 December 2026, IB art. 38(1)). Employees pay wage tax (loonbelasting) withheld by the employer each month; wage tax is an advance payment on income tax (IB art. 52e). Self-employed people and others with income beyond wages file a provisional return in the year and a definitive return after it.

**Which text of the law.** The Wet Inkomstenbelasting 1922 (G.B. 1921 no. 112, text G.B. 1960 no. 84, as last amended by S.B. 2024 no. 3) and the Wet Loonbelasting (S.B. 1981 no. 181, text S.B. 1985 no. 10, as last amended by S.B. 2024 no. 2), both as published by the Suriname Tax Administration (Belastingdienst Suriname). The tax-free amount and the wage tax bands were last set by Staatsbesluit S.B. 2024 no. 2, in force from 1 January 2024. No later amendment was found on the Tax Administration law pages or among the laws passed by De Nationale Assemblée (DNA) when read on 11 November 2026, so the 2024 figures are the 2026 figures. The Minister may change these amounts by staatsbesluit (IB art. 52h, LB art. 18a): check for a new staatsbesluit before relying on them for 2026.

Linked skills: companies in [sr-corporate-income-tax](sr-corporate-income-tax.md); VAT in [sr-vat-gst](sr-vat-gst.md); the employer's monthly withholding and AOV premium in [sr-payroll-social](sr-payroll-social.md); an overview in [sr-tax-overview](sr-tax-overview.md).

## Who this applies to

- **Residents (binnenlandse belastingplichtigen).** Natural persons who live in Suriname are taxed on their zuiver inkomen from all sources (IB art. 1(2)(a), art. 4). Where someone lives is judged on the facts (IB art. 3(1)). A person who returns to live in Suriname within one year of leaving, without living elsewhere in between, is treated as having lived in Suriname throughout (IB art. 3(2)).
- **Non-residents (buitenlandse belastingplichtigen).** Natural persons who do not live in Suriname are taxed only on Surinamese-source income (binnenlands onzuiver inkomen): Surinamese real estate, mortgage debts on Surinamese property, profit shares in a business managed in Suriname (not from shareholdings), profit of a permanent establishment, director or supervisory-board fees from a Surinamese company, employment carried out in Suriname, and pay or pensions from Surinamese public bodies (IB art. 1(3)(a), arts. 26 and 27).
- **Employees.** The employer withholds wage tax on all pay from employment (LB arts. 2, 6, 19). Wage tax is credited against income tax (IB art. 52e). Where non-wage income is SRD 7,500 or less, no income tax assessment is made and wage tax is final, unless the person had pay from more than one employer at once (IB arts. 52f and 52g).
- **Self-employed and others.** Profit from a business or profession, freelance work, rent, interest and dividends, and periodic payments go into onzuiver inkomen (IB art. 4(3)). They file the provisional and definitive returns (IB arts. 42a and 43).
- **Married couples.** Each spouse is taxed separately; where both are resident taxpayers, the personal deductions of IB art. 18(1) and (2) go to the spouse with the higher onzuiver inkomen (IB art. 31(1)).
- **Out of scope:** companies and foundations that run a business (see sr-corporate-income-tax); the AOV old-age premium (see "Ask the client first" and sr-payroll-social); consular exemptions (IB art. 33); the solidarity levy, which ran from 1 February 2021 to 1 January 2022 and no longer applies (IB art. 34(1a)).

## Rates, bands and thresholds

The tax-free amount and the bands are the same in the income tax and the wage tax. Income tax applies them to zuiver inkomen: nil on the first SRD 108,000, then the bands (IB art. 34(1)). Wage tax first deducts the SRD 108,000 tax-free amount from zuiver loon, then applies the bands to the remaining belastbaar loon (LB arts. 13 and 14). The two give the same result for a full year.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Tax-free amount (belastingvrije som), resident, a full year (LB art. 13(1)(b); IB art. 34(1) nil band). Monthly wage tax uses 1/12 (LB art. 13(3)) | SRD 108,000 a year | 2026 | https://belastingdienst.sr/wp-content/uploads/2024/05/S.B.-2024-no.-2-STAATSBESLUIT-11-januari-2024-uitvoeringartikel-18a-Wet-Loonbelasting-S.B.-1981-no.-181-laatstelijk-gewijzigd-S.B.-2022-no.-149.pdf |
| Tax-free amount, non-resident employee (LB art. 13(1)(a)(2)) | None: wage tax applies from the first SRD | 2026 | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-Loonbelasting.pdf |
| Band 1: zuiver inkomen above SRD 108,000 up to SRD 150,000 (IB art. 34(1)); belastbaar loon up to SRD 42,000 (LB art. 14(1)) | 8% | 2026 | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-Inkomstenbelasting.pdf |
| Band 2: above SRD 150,000 up to SRD 192,000 (IB); belastbaar loon above SRD 42,000 up to SRD 84,000 (LB) | 18% | 2026 | same |
| Band 3: above SRD 192,000 up to SRD 234,000 (IB); belastbaar loon above SRD 84,000 up to SRD 126,000 (LB) | 28% | 2026 | same |
| Band 4: above SRD 234,000 (IB); belastbaar loon above SRD 126,000 (LB) | 38% | 2026 | same |
| Professional-expense deduction for employees (LB art. 12(2); IB art. 18(3)), only so far as no tax-free expense allowance is received | 4% of wages, at most SRD 4,800 a year | 2026 | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-Loonbelasting.pdf |
| Vacation allowance not counted as wages (LB art. 10(1)(i)) | Up to one month's wages a year, at most SRD 10,016 | 2026 | same |
| Bonus (gratificatie) for work done, with no other special rule, not counted as wages (LB art. 10(1)(j)); pro rata for a period under a year | Up to one month's wages a year, at most SRD 10,016 | 2026 | same |
| Child allowance (kinderbijslag) not counted as wages (LB art. 10(1)(h)) | SRD 125 a child a month, at most SRD 500 a month | 2026 | same |
| One-off payment (uitkering ineens) that is wages but does not relate to a period of several pay periods, taxed separately on the employee's request (LB art. 17a; IB art. 34a). No tax-free amount | 5% up to SRD 42,000; 15% to SRD 84,000; 25% to SRD 126,000; 35% above | 2026 | https://belastingdienst.sr/wp-content/uploads/2024/05/S.B.-2024-no.-2-STAATSBESLUIT-11-januari-2024-uitvoeringartikel-18a-Wet-Loonbelasting-S.B.-1981-no.-181-laatstelijk-gewijzigd-S.B.-2022-no.-149.pdf |
| Overtime pay in a monthly pay period, on the employee's request (LB art. 17c; IB art. 34c) | 5% up to SRD 500; 15% from SRD 500 to SRD 1,100; 25% above SRD 1,100, per month | 2026 | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-Loonbelasting.pdf |
| Resident artist or professional athlete on a short contract (LB art. 18(1)(b)) | 10% of the pay | 2026 | same |
| Non-resident artist or professional athlete on a short contract (LB art. 18(1)(c)) | 15% of the pay | 2026 | same |
| Domestic helpers named in art. 6 of the Staatsbesluit Loonbelasting (LB art. 18(1)(d)) | 6% of the pay | 2026 | same |
| Business cessation, transfer or liquidation profit, on request (IB art. 34(4)) | 25% flat instead of the bands | 2026 | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-Inkomstenbelasting.pdf |
| Cessation profit of a business run at least five years: exempt part (IB art. 7(6)) | First SRD 5,000 | 2026 | same |
| Car made available for work, other than a truck over 1,000 kg payload (IB art. 7a(4),(5)); not if a complete mileage log proves business-only use (art. 7a(6)) | At least 2% of the catalogue price a year added to income from work | 2026 | same |
| Free medical treatment, value counted in business profit (IB art. 7a(2)) | Actual cost, at most SRD 500 a year | 2026 | same |
| Mortgage interest on an own home used as the main residence (IB art. 18(1)(g)) | Interest on a debt of at most SRD 600,000 | 2026 | same |
| Annuity and pension premiums for the taxpayer, spouse and minor children (IB art. 18(1)(b)) | Up to 10% of onzuiver inkomen | 2026 | same |
| Medical, childbirth, accident, disability and funeral costs (art. 18(1)(f)); study costs of children (art. 18(1)(e)); support of needy relatives in the first degree (art. 18(1)(d)) | Deductible only above 10% of onzuiver inkomen | 2026 | same |
| Live-in child aged 18 or over who cannot support themselves because of a lasting disability and receives no benefit for it (IB art. 18(2)) | SRD 8,000 deduction | 2026 | same |
| Loss carry-forward (IB art. 4(4)) | Start-up losses of the first three book years: no time limit, if regular books with annual closings are kept in Suriname; other losses: the seven following years | 2026 | same |
| No income tax assessment where non-wage income is small (IB art. 52f) | Non-wage income of SRD 7,500 or less | 2026 | same |
| Bookkeeping duty for other self-employed (IB art. 42(3)(1)(c)) | Full records if profit SRD 1,200 or more or gross receipts SRD 12,000 or more | 2026 | same |
| Late payment interest (IB art. 73(1); rate set by S.B. 1995 no. 98 per the footnote in the published text) | 45% a year, simple, from the day after the due date | 2026 | same |

## The base

Work through the return in the order the portal does (the "Optelstaat inkomen" screen of the definitive return):

1. **Onzuiver inkomen** is the total of the net yield of each source (IB art. 4(3)), entered in rubrics 1 to 6 of the return:
   - Rubric 1, income from work (opbrengst van arbeid): wages less the 4% deduction (capped at SRD 4,800) for an employee (IB art. 10(4), art. 18(3)); pay excluded by LB art. 10 stays out (vacation allowance, bonus and child allowance within the caps above, employer pension rights, proven expense allowances, employer-provided commuting). "Wages" and "employment" mean what the Wet Loonbelasting says (IB art. 7(9)).
   - Rubric 2, business or professional profit (opbrengst van onderneming): profit by sound business practice, applied consistently (IB art. 7(4)). Capital spending is not a cost but is written off over its life (IB arts. 10(2), 11(1)); small items may be expensed (art. 11(2)). The private-use part of business property is not deductible (art. 7a(1)). At least 2% of a car's catalogue price a year counts as private use (art. 7a(3)). No deduction for building reserves, except the equalisation reserve of art. 11(4) and the pension reserve of art. 21, nor for interest on own capital (art. 11(3)).
   - Rubric 3, movable capital (roerend kapitaal): interest and dividends (IB art. 6). Dividend tax withheld is credited (IB art. 52e).
   - Rubric 4, real estate (onroerende goederen): rent and similar yields of property not used as one's own home, less insurance and upkeep up to the yield, ground rent, property taxes and letting costs (IB arts. 5 and 10(1)).
   - Rubric 5, periodic payments (periodieke uitkeringen): annuities and pensions. AOV benefits are not taxed, and other pensions are not taxed up to twice the AOV benefit (IB art. 8(2)).
   - Rubric 6, undivided estates (onverdeelde boedels).
   Not income: support of minors by parents, consumer co-operative refunds, insurance profit shares, and pure speculation gains outside a business (IB art. 9). Gains on buying and selling an asset without changing it are not income from work (IB art. 7(1)(c)).
2. **Less losses** (rubric 7, aftrek van vroegere verliezen): start-up losses first, then losses of the seven previous years (IB art. 4(4)).
3. **Less personal deductions** (rubric 8, aftrekposten, IB art. 18): annuity premiums up to 10% of onzuiver inkomen, with an insurer's statement each year (art. 18bis(1)); mortgage interest on the own home on up to SRD 600,000 of debt; exterior painting of the own home once every three years; medical, study and family-support costs only above 10% of onzuiver inkomen; SRD 8,000 for a disabled adult child at home. Costs count when paid (art. 18(4) with art. 13(2)).
4. **Zuiver inkomen** is the result. Tax: nil on the first SRD 108,000; then 8%, 18%, 28% and 38% (IB art. 34(1)). Where tax liability lasted only part of the year (arrival or departure), annualise: multiply zuiver inkomen by 360 and divide by the days of liability, compute the tax, then multiply by the days and divide by 360; each full month counts as 30 days (IB art. 34(3)).
5. **Credits.** Deduct wage tax and dividend tax withheld (IB art. 52e) and the provisional-return payments (IB art. 52d). The portal's "Berekening Inkomstenbelasting" screen shows: tax at the normal rate, tax at the special rate, hazard-games tax, total, less wage tax and dividend tax withheld, less provisional return or assessment, equals income tax to pay.

**Wage tax for employees (monthly).** The employer computes zuiver loon (wages less the 4% deduction, at most SRD 400 a month as 1/12 of SRD 4,800), deducts the tax-free amount for the period (SRD 9,000 a month for a resident) and applies the bands for the period (SRD 3,500 a month per band). A year is 364 days and a month 30 1/3 days when converting periods (LB art. 13(3)). A bonus that covers several pay periods is spread over them (LB art. 17). The employer's side is in [sr-payroll-social](sr-payroll-social.md).

## Deadlines and filing

All returns are filed electronically in the Tax Administration online portal (portaal.belastingdienst.sr/OPO) with an electronic signature; the inspector may allow a paper return only for someone who cannot use the portal (IB art. 42(1) and (2)). From January 2025 income tax returns are filed online; returns for 2024 and earlier stay on paper (Belastingdienst income tax page).

| Step | 2026 tax year | Law |
|---|---|---|
| Ask to file a provisional return below last year's definitive tax (written, reasoned request to the inspector, secinspectidb@belastingdienst.sr); the inspector answers in two weeks, silence counts as yes | By 15 February 2026 | IB art. 42c(2),(3); Belastingdienst notice on art. 42c |
| Provisional return (voorlopige aangifte), resident individuals; tax at least equal to the latest definitive return's tax unless the request above was granted | By 15 April 2026 | IB arts. 42a(1), 42c(1) |
| Provisional tax in four equal instalments; the first with the return | 15 April, 15 July, 15 October and 31 December 2026 | IB art. 42b(2) |
| Obligation that arises after 15 April | Return and payment by 31 December 2026 | IB art. 42b(4) |
| Definitive return (definitieve aangifte), resident individuals liable to an assessment and non-residents with Surinamese income; tax due is paid when filing | Within four months after the end of the year: by 30 April 2027 | IB arts. 43(1), 44(2) |
| A self-employed person who must keep records attaches a signed, dated balance sheet and profit and loss account (definitive) or a statement of how the income was reached (provisional) | With each return | IB arts. 42b(5), 44(5) |
| Objection against an assessment | Within 60 days of the date of the assessment notice | IB art. 54(1) |

**Portal steps (definitive return, Tax Administration manual of May 2026).** Log in at the portal; choose IB/AOV, then Aangifte IB en premie AOV, then Nieuwe aangifte IB; select Definitieve aangifte, the tax year and whether you were married all year; accept the introduction; answer the nine questions on which income you had (an individual without a sole-trader business answers No to rubrics 2 and 7); fill each rubric, entering 0 where nothing applies; check the "Optelstaat inkomen", the income tax computation and the AOV premium computation; on the payment-terms screen click Indienen and then Voltooien (the return is only filed after Voltooien). The portal then shows the amounts to pay and a separate payment reference (betaalkenmerk) for income tax and for the AOV premium. A refund is given by an assessment (IB art. 44(3)).

## Penalties and interest

- **Assessment with a 100% increase.** Where no provisional return is filed or paid (IB arts. 42a, 42b, 42c), no definitive return is filed (art. 44(1)), or tax is not paid with the definitive return (art. 44(2)), the inspector sets an assessment and, after a reminder, increases the tax in it by 100%; the increase is 10% where the failure is not due to intent or gross negligence (IB art. 51(3), (5), (6)).
- **Incorrect definitive return.** The inspector may correct it by an assessment within two years of filing (IB art. 51(2)). A provisional return with income estimated too low may be corrected within three months (art. 51(4)).
- **Interest.** Late payment carries simple interest on the tax and the increase from the day after the due date to the day of payment (IB art. 73(1)); the rate is 45% a year from 1 August 1995 under S.B. 1995 no. 98, as noted in the published text.
- **Fines.** Failing to file, including filing late, is punishable by a fine of up to SRD 500 (IB art. 88); failing to attach the required accounts likewise up to SRD 500 (art. 87). A return without the required accounts or signature counts as not filed (art. 45(2)).
- **Wage tax.** A wage tax top-up assessment can be increased by up to 100% (LB art. 25); a late payment made before an assessment can carry up to 10% (LB art. 26).

## Cross-border points

- **Non-resident employees** get no tax-free amount for wage tax (LB art. 13(1)(a)(2)). The Tax Administration income tax page says the tax-free amount is given to all natural persons except non-resident taxpayers. Non-residents may deduct only interest on mortgages on Surinamese property that is not linked to a source of income, and Surinamese-source losses (IB art. 26(2)).
- **Permanent establishment.** Construction, assembly, dredging and similar work for more than 183 days within twelve months, insurance activity, aerial surveys and resource inventories in Suriname count as a permanent establishment (IB art. 28(2)); so does exploration or exploitation on the continental shelf under a Surinamese licence (art. 28(3)).
- **International transport.** Shipping and air transport between Suriname and abroad by non-residents, and crew on those vehicles, are not business or employment in Suriname, unless the transport business is managed from Suriname (IB art. 29).
- **Double tax relief** is given only by staatsbesluit or treaty (IB art. 37); where a treaty says no wage tax is due, the employer may stop withholding only on a statement from the inspector (LB art. 19(3)). Foreign tax is not deductible from income (IB art. 26(4), art. 33(2)(3°)).
- **Dividends from Surinamese companies** carry 25% dividend tax, credited against income tax (Wet Dividendbelasting art. 5; IB art. 52e). The company side is in sr-corporate-income-tax.

## Two worked examples that recompute

**Example 1: resident employee, monthly wage SRD 20,000 for all of 2026.** Annual wages SRD 240,000, no bonus, vacation allowance or other income. The 4% deduction is SRD 9,600, capped at SRD 4,800, so zuiver loon is SRD 235,200. Less the tax-free amount of SRD 108,000, belastbaar loon is SRD 127,200. Tax: 8% of 42,000 = 3,360; 18% of 42,000 = 7,560; 28% of 42,000 = 11,760; 38% of 1,200 = 456; total SRD 23,136 a year, SRD 1,928 a month. Because non-wage income is nil (at most SRD 7,500) and there is one employer, no income tax assessment follows and the wage tax is final (IB art. 52f). The same figure comes from IB art. 34: zuiver inkomen 235,200, nil on 108,000, then the bands from 150,000, 192,000 and 234,000.

```oa-check
name: Suriname resident employee, wages SRD 240,000 (2026)
inputs:
  wages: 240000
steps:
  - expense: min(wages * 0.04, 4800)
  - zuiver: wages - expense
  - belastbaar: max(zuiver - 108000, 0)
  - b1: min(belastbaar, 42000) * 0.08
  - b2: clamp(belastbaar - 42000, 0, 42000) * 0.18
  - b3: clamp(belastbaar - 84000, 0, 42000) * 0.28
  - b4: max(belastbaar - 126000, 0) * 0.38
  - tax: b1 + b2 + b3 + b4
  - monthly: tax / 12
expected:
  zuiver: 235200
  belastbaar: 127200
  tax: 23136.00
  monthly: 1928.00
```

**Example 2 (decision): ask for the special rate on a one-off payment, or not?** A resident employee receives a one-off payment that counts as wages but does not relate to a period of several pay periods (LB art. 17a, IB art. 34a). Without a request it is added to the year's wages and taxed at the bands; with a request it is taxed alone at 5%, 15%, 25% and 35%, with no tax-free amount. The figure that decides is the employee's marginal rate against 5%, and whether part of the payment would fall inside the unused tax-free amount.

- **Case A, high earner.** Belastbaar loon without the payment is SRD 127,200 (Example 1); the payment is SRD 60,000. Normally taxed, it all falls in the 38% band: SRD 22,800 extra. At the special rate: 5% of 42,000 = 2,100 plus 15% of 18,000 = 2,700, total SRD 4,800. Request the special rate: it saves SRD 18,000.
- **Case B, low earner.** Zuiver loon without the payment is SRD 100,000, so SRD 8,000 of the tax-free amount is unused; the payment is SRD 20,000. Normally taxed, belastbaar loon becomes SRD 12,000 and the tax is 8% of 12,000 = SRD 960. At the special rate: 5% of 20,000 = SRD 1,000. Do not ask: the normal route is SRD 40 cheaper.

Before either route, check whether the payment is a vacation allowance or a bonus that LB art. 10(1)(i) or (j) keeps out of wages up to one month's pay (at most SRD 10,016).

```oa-check
name: Suriname one-off payment, special rate or normal bands (2026)
inputs:
  base_a: 127200
  pay_a: 60000
  zuiver_b: 100000
  pay_b: 20000
steps:
  - normal_a: (base_a + pay_a - 126000) * 0.38 - (base_a - 126000) * 0.38
  - special_a: min(pay_a, 42000) * 0.05 + clamp(pay_a - 42000, 0, 42000) * 0.15
  - saving_a: normal_a - special_a
  - belastbaar_b: max(zuiver_b + pay_b - 108000, 0)
  - normal_b: min(belastbaar_b, 42000) * 0.08
  - special_b: min(pay_b, 42000) * 0.05
  - saving_b: normal_b - special_b
expected:
  normal_a: 22800.00
  special_a: 4800.00
  saving_a: 18000.00
  normal_b: 960.00
  special_b: 1000.00
  saving_b: -40.00
```

## Ask the client first

1. Did you live in Suriname in 2026, all year or part of it (arrival or departure dates)? Residence decides worldwide income and the tax-free amount.
2. What income did you have besides wages: business or professional profit, rent, interest, dividends, pensions? If it was SRD 7,500 or less and you had one employer at a time, the wage tax is usually final.
3. Did you have two or more employers at the same time, or any one-off payment, bonus, vacation allowance or overtime pay? These change the wage tax and the special-rate options.
4. Are you married, and does your spouse also live in Suriname? The personal deductions go to the spouse with the higher income.
5. Do you pay mortgage interest on your own home, annuity or pension premiums, or large medical or study costs? Bring the insurer's statement and the loan statement.
6. For a business: do you keep regular books with annual closings in Suriname, and do you have losses from earlier years or from your first three book years?

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet Inkomstenbelasting 1922, text published by the Tax Administration (as last amended by S.B. 2024 no. 3): read arts. 1 to 34c (residence, sources, deductions, rates), 36 to 45 (tax year, returns), 51 to 54, 73 with its footnote, 87 and 88 | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-Inkomstenbelasting.pdf | 2026-11-11 |
| Wet Loonbelasting, text published by the Tax Administration (as last amended by S.B. 2024 no. 2): read arts. 2 to 30 (employee, wages, exclusions, deduction, tax-free amount, rates, filing, top-up assessments) | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-Loonbelasting.pdf | 2026-11-11 |
| Staatsbesluit of 11 January 2024, S.B. 2024 no. 2 (Wet Loonbelasting art. 18a): read in full (SRD 4,800 deduction, SRD 108,000 tax-free amount, bands, art. 17a rates, in force 1 January 2024, explanatory note) | https://belastingdienst.sr/wp-content/uploads/2024/05/S.B.-2024-no.-2-STAATSBESLUIT-11-januari-2024-uitvoeringartikel-18a-Wet-Loonbelasting-S.B.-1981-no.-181-laatstelijk-gewijzigd-S.B.-2022-no.-149.pdf | 2026-11-11 |
| Tax Administration, Inkomstenbelasting page: read for who is taxed, the tax-free amount not given to non-residents, and online filing from January 2025 | https://belastingdienst.sr/belastingen/inkomstenbelasting/ | 2026-11-11 |
| Tax Administration, notice "Gebruikmaking van artikel 42C" for the 2026 provisional return: read in full (request by 15 February 2026, email address) | https://belastingdienst.sr/artikel-42c-01/ | 2026-11-11 |
| Tax Administration, manual Definitieve Aangifte Inkomstenbelasting voor natuurlijke personen (May 2026): read for the portal steps, the nine questions, rubrics 1 to 8, the computation screens and payment references | https://belastingdienst.sr/wp-content/uploads/2026/05/Handleiding_1-IB-Nat.-Pers._mei-2026_compressed.pdf | 2026-11-11 |
| Wet Dividendbelasting 1973, text published by the Tax Administration: read art. 5 for the 25% rate | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-Dividendbelasting.pdf | 2026-11-11 |
| De Nationale Assemblée, amendments after 2005 and approved bills: read the lists for any 2025 or 2026 change to the income or wage tax (none found) | https://www.dna.sr/wetgeving/surinaamse-wetten/wijzigingen-na-2005/ | 2026-11-11 |

Not yet confirmed: whether a staatsbesluit for 2025 or 2026 changed the SRD 108,000 tax-free amount, the bands or the SRD 4,800 deduction (none is published on the Tax Administration law pages or listed by DNA as of 11 November 2026; the Staatsblad itself is not online); how the SRD 108,000 nil band of IB art. 34(1) applies to a non-resident's binnenlands zuiver inkomen (the Tax Administration page says non-residents get no tax-free amount; the article does not say so expressly); the AOV old-age premium rate for 2026 (the Wet AOV text the Tax Administration publishes, last amended by S.B. 2002 no. 96, says 4% of zuiver inkomen or zuiver loon, art. 20(2); whether a later change applies could not be confirmed, so it is left out of the rates table); the current late-payment interest rate beyond the 45% footnote to S.B. 1995 no. 98; the Minister's wage tax tables under LB art. 13(4).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sr-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sr-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
