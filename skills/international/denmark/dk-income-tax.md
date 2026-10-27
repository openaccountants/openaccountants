---
name: dk-income-tax
description: "Danish personal income tax for income year 2026, for residents who are employees or self-employed (selvstændig erhvervsdrivende). Covers AM-bidrag at 8% and the under-18 rule, bundskat 12.01%, kommuneskat and kirkeskat (2026 averages), the new 2026 bands from the personal tax reform: mellemskat 7.5% over DKK 641,200, topskat 7.5% over DKK 777,900 and toptopskat 5% over DKK 2,592,700, personfradrag DKK 54,100, beskæftigelsesfradrag, jobfradrag, senior and single-parent allowances, skatteloft 44.57% and 42%, share income at 27% and 42% over DKK 79,400, business deductions, depreciation, private car, virksomhedsordningen and kapitalafkastordningen, B-skat, årsopgørelse, the 1 July deadline, restskat and skattetillæg. Trigger on: Danish income tax, topskat 2026, mellemskat, toptopskat, AM-bidrag, personfradrag, beskæftigelsesfradrag, B-skat, årsopgørelse, restskat, self-employed tax Denmark. Out of scope: companies (dk-corporate-tax), share and property gains in depth (dk-capital-gains), non-residents and treaties (dk-cross-border), payroll withholding (dk-payroll), ATP and other contributions (dk-social-contributions), VAT (denmark-vat-return)."
version: 2.2
jurisdiction: DK
tax_year: 2026
last_updated: 2026-10-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Denmark: personal income tax, income year 2026

Tax year: the calendar year (indkomståret 2026). Currency: Danish kroner (DKK). Authority: Skattestyrelsen (skat.dk). Statutes: Personskatteloven (PSL), Ligningsloven (LL), Kildeskatteloven (KSL), Arbejdsmarkedsbidragsloven and Skattekontrolloven, on retsinformation.dk.

2026 is the first year of the personal tax reform (lov nr. 482 af 22. maj 2024, from bill L 138 of 2023-24). The consolidated Personskatteloven is still LBK nr. 1284 af 14. juni 2021, as amended; read it with lov nr. 482. The old topskat is renamed mellemskat, and two new layers start: a new topskat and a toptopskat. Read every pre-2026 source with that in mind.

## Who this applies to

- **Full tax liability.** A person who lives in Denmark, or stays in Denmark for 6 consecutive months (a short trip abroad does not break the stay), is fully liable on worldwide income. Buying a house alone does not make a person fully liable.
- **Limited liability.** A person without Danish residence who has Danish-source income is taxed on that income only. The state charges a 25% rate in place of kommuneskat (PSL § 8 c). Limited liability, cross-border workers and treaties are in dk-cross-border.
- **Employees and the self-employed.** Both pay AM-bidrag, state tax and kommuneskat. The self-employed also report business profit, may use virksomhedsordningen (VSO) or kapitalafkastordningen (KAO), and pay B-skat during the year.
- **Business or employment.** Actual conditions decide. Issuing an invoice does not make someone self-employed if they work under the client's instructions, at the client's risk and inside the client's organisation. Separate activities can be classified differently. If classification is unclear, stop and get a binding answer or a Danish adviser's view.
- **Companies are out.** An ApS or A/S is taxed under dk-corporate-tax; its owner pays tax here only on salary and on dividends as share income.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| AM-bidrag (labour market contribution) on salary, B-income and business profit | 8% | 2026 | https://skat.dk/en-us/individuals/b-income |
| AM-bidrag age rule | none until the calendar year the person turns 18 | 2026 | https://skat.dk/en-us/individuals/b-income |
| Bundskat (PSL § 6) | 12.01% | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/personskatteloven |
| Bundskat on Christiansø | 4.01% | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/personskatteloven |
| Personfradrag (PSL § 10), age 18 and over | DKK 54,100 (2025: DKK 51,600) | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/personskatteloven |
| Mellemskat (PSL § 7), rate | 7.5% | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/personskatteloven |
| Mellemskat threshold (personal income after AM-bidrag, plus capital income over the amount below) | DKK 641,200 | 2026 | https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat |
| Positive net capital income that stays outside mellemskat, single / married | DKK 55,000 / DKK 110,000 | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/personskatteloven |
| Topskat (PSL § 7 a), rate and threshold (personal income after AM-bidrag) | 7.5% over DKK 777,900 | 2026 | https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat |
| Toptopskat (PSL § 8), rate and threshold (personal income after AM-bidrag) | 5% over DKK 2,592,700 | 2026 | https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat |
| Kommuneskat, national average | 25.049% (rounded 25.0%) | 2026 | https://svmn.dk/tal-og-metode/satser/statistik-i-kommunerne/kommuneskatter-gennemsnitsprocenten-i-2026 |
| Kirkeskat, average for Folkekirken members | 0.867% | 2026 | https://svmn.dk/tal-og-metode/satser/statistik-i-kommunerne/kommuneskatter-gennemsnitsprocenten-i-2026 |
| Skatteloft I, personal income (PSL § 19, stk. 1) | 44.57% | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/personskatteloven |
| Skatteloft II, positive net capital income (PSL § 19, stk. 2) | 42.0% | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/personskatteloven |
| Municipal rate above which skatteloft I cuts mellemskat (44.57 − 12.01 − 7.5) | 25.06% | 2026 | https://info.skat.dk/data.aspx?oid=1948928 |
| Share income (aktieindkomst, PSL § 8 a) | 27% up to DKK 79,400, 42% above (2025: DKK 67,500) | 2026 | https://skat.dk/en-us/individuals/shares-and-securities/buying-and-selling-shares-and-securities |
| Share income threshold, married couple living together at year end | DKK 158,800 | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/personskatteloven |
| Compensation for reduced tax value of negative net capital income (PSL § 11) | 8% on up to DKK 50,000 | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/personskatteloven |
| Beskæftigelsesfradrag (LL § 9 J) | 12.75%, max DKK 63,300 (full at DKK 496,471) | 2026 | https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag |
| Jobfradrag | 4.5% of income over DKK 235,200, max DKK 3,100 (full at DKK 304,089) | 2026 | https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag |
| Senior beskæftigelsesfradrag (1 or 2 years before state pension age) | 1.4%, max DKK 6,100 (full at DKK 435,715) | 2026 | https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag |
| Single-parent beskæftigelsesfradrag (receives ekstra børnetilskud) | 11.5%, max DKK 50,600 (full at DKK 440,000) | 2026 | https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag |
| Virksomhedsskat on profit kept in VSO | 22% (provisional) | 2026 | https://skat.dk/en-us/businesses/own-business/tax-on-own-business |
| Working spouse allocation (KSL § 25 A, stk. 3) | up to 50% of profit, max DKK 295,900 | 2026 | https://info.skat.dk/data.aspx?oid=1976883 |
| Minor assets, immediate deduction | under DKK 36,000 (2025: DKK 34,400) | 2026 | https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses |
| Plant and equipment pool, diminishing balance | up to 25% a year | 2026 | https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses |
| Write-off of a small mixed-use asset balance | below DKK 16,900 | 2026 | https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses |
| Green asset uplift (new, no private use, bought 1 Jan 2025 to 31 Dec 2026) | 108% depreciation base | 2026 | https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses |
| Buildings bought from 1 Jan 2023 / earlier | up to 3% / up to 4% a year | 2026 | https://info.skat.dk/data.aspx?oid=2083987 |
| Purchased goodwill | up to 1/7 a year | 2026 | https://info.skat.dk/data.aspx?chk=220619&oid=2083994 |
| Private car used for business, rate method | DKK 3.94/km to 20,000 km, DKK 2.28/km above | 2026 | https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses |
| Business phone available for private use | DKK 3,500 added to profit | 2026 | https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses |
| Entertainment (repræsentation) | 25% deductible | 2026 | https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses |
| Return filing deadline, self-employed | 1 July of the following year | 2026 | https://info.skat.dk/data.aspx?oid=2284485 |
| B-skat instalments | 10, none in June and December | 2026 | https://skat.dk/en-us/individuals/b-income |
| Skattetillæg for late return (Skattekontrolloven § 73) | DKK 400 a day, max DKK 10,000; DKK 200 a day, max DKK 5,000 if taxable income is not above the mellemskat threshold | 2026 | https://info.skat.dk/data.aspx?oid=2284578 |
| Restskat surcharge (KSL § 61, stk. 2) | Opkrævningsloven § 7, stk. 2 rate plus 1.5 points; 5.7% on income year 2025 restskat; the 2026 rate is set by 15 December 2026 | 2026 | https://skat.dk/restskat |

All PSL thresholds are 2010-level base amounts indexed under PSL § 20. The 2027 figures are already published: mellemskat DKK 659,900, topskat DKK 800,500, toptopskat DKK 2,668,200, personfradrag DKK 55,700, share income DKK 89,600.

## The taxable base

Danish income tax runs on four income types. Keep them apart before any rate is applied.

1. **Personal income (personlig indkomst).** Salary, B-income and business profit, after AM-bidrag. AM-bidrag is 8% of the gross amount and is deducted before state tax.
2. **Net capital income (kapitalindkomst).** Interest received less interest paid, and some other capital items. Positive net capital income joins the bundskat base, and the part above DKK 55,000 (single) joins the mellemskat base. It never joins the topskat or toptopskat base. If spouses live together at year end, an unused part of the DKK 55,000 passes to the other spouse. The couple's positive net capital income is computed together for mellemskat only if they were married and living together for the whole year (PSL § 7, stk. 6).
3. **Share income (aktieindkomst).** Dividends and gains on shares. Taxed on its own scale, 27% then 42%. It does not count toward any band above.
4. **Taxable income (skattepligtig indkomst).** Personal income plus net capital income, less ligningsmæssige fradrag (beskæftigelsesfradrag, jobfradrag, senior and single-parent allowances, travel, union fees and others). Kommuneskat and kirkeskat are charged on this.

**The computation.**

- AM-bidrag = 8% of salary, B-income and profit (0 until the year the person turns 18).
- Bundskat = 12.01% of (personal income + positive net capital income − personfradrag).
- Mellemskat = 7.5% of (personal income + net capital income over DKK 55,000 − DKK 641,200).
- Topskat = 7.5% of (personal income − DKK 777,900).
- Toptopskat = 5% of (personal income − DKK 2,592,700).
- Kommuneskat (+ kirkeskat) = municipal rate × (taxable income − personfradrag).
- Share income tax on its own scale.
- Skatteloft: if 12.01% + 7.5% + the municipal rate is above 44.57%, the mellemskat rate on personal income is cut by the excess. With 12.01% and 7.5% this happens when the municipal rate is above 25.06%. Church tax is not counted. For positive net capital income the ceiling is 42.0%. Topskat and toptopskat are not cut. Profit kept in VSO enters the ceiling only when it is moved to personal income.

The personfradrag works as a tax credit at each rate. If its value cannot be used against bundskat, it is used against mellemskat, topskat, toptopskat and then share income tax, in that order (PSL § 9, as amended for 2026). If a married person living with their spouse at year end cannot use the full value of the personfradrag, the unused value reduces the other spouse's taxes in the same order (PSL § 10, stk. 3). Skattestyrelsen applies the transfer automatically.

**Work allowances.** Everyone with AM-bidrag-liable salary or business profit gets beskæftigelsesfradrag and jobfradrag automatically. For the self-employed the base is the AM-bidrag base of the business income; a negative result gives DKK 0. The senior allowance applies in each of the 1 or 2 years before state pension age, not in the year that age is reached. Because the allowance starts in 2026, a person who reaches state pension age in 2027 gets it for 2026 only. A proposal to widen it to 5 years and raise the rates was not enacted when the page was read. The single-parent allowance needs entitlement to and receipt of ekstra børnetilskud. These allowances reduce taxable income only. They do not reduce AM-bidrag or the personal-income band tests.

**Business profit.** Deduct costs that earn, secure and maintain the business income, to the documented business share. Points that come up most:

- Entertainment of business contacts, including restaurant meals and gifts: 25% deductible, add back 75%. Advertising is fully deductible.
- One-off costs of setting up the business are not deductible. Running costs such as rent, phone or wages paid within the 6 months before start-up can be, item by item.
- Home office: no deduction for a room unless it is arranged so that private use is not possible. Furniture can be split by business use.
- Business phone available for private use: deduct the cost and add DKK 3,500 to the business result. Internet: no value if the home connection gives near-work access to the business network; otherwise add DKK 3,500. If both phone and internet are taxable, the value is DKK 3,500 once, not twice. Enter the value in field 462 of the tax return ([skat.dk, deduction for business expenses](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses)). Spouses who both have taxable free phones are each taxed on DKK 2,625, provided the joint value is at least DKK 4,600.
- Assets: under DKK 36,000 (VAT-exclusive if VAT-registered, VAT-inclusive if not; items meant to be used together are tested together), or with a life of 3 years or less, are deducted at once. Others go into a pool at up to 25% a year. A mixed-use asset has its own schedule; its balance can be written off once under DKK 16,900, business share only. Green assets get a 108% base. Buildings: up to 3% a year (acquired from 1 January 2023) or 4% (earlier). Purchased goodwill and listed intangibles: up to 1/7 a year; self-built goodwill is not depreciated.
- Private car: either the actual business share of all costs, or DKK 3.94/km to 20,000 km and DKK 2.28/km above, with a mileage log. Do not claim fuel or insurance on top of the rate. A self-employed person cannot pay themselves tax-free mileage. A car inside VSO that is also available privately triggers company-car tax.
- Private costs, fines, income tax and drawings are never deductible. Keep VAT out of the income-tax profit.

**VSO and KAO.** Under VSO the business and private finances must be separate. Profit can be kept in the business at a provisional 22%; when it is later withdrawn it is taxed as personal income with the 22% credited. Business interest can be treated as personal income instead of capital income. Under KAO a calculated return on the business capital is capital income, capped at the higher of business profit or total negative capital income excluding that return. Indicate either scheme in field 184 of the forskudsopgørelse; the final choice is made in the return (box 147 for VSO, box 141 for KAO). A working spouse can be allocated up to 50% of the profit, max DKK 295,900. Refer a first election, a change, an exit from VSO or a large withdrawal.

**Losses.** How a business loss is carried against other income, a spouse or later years follows PSL § 13. That order was not re-read for this version: check it before using a loss.

## Deadlines and filing

- **Forskudsopgørelse (preliminary assessment).** Enter expected profit in field 221 or loss in field 435, recalculate and accept. That sets the tax card withholding rate and any B-skat. Update it whenever the forecast changes.
- **B-skat.** Paid in 10 monthly instalments, none in June and December. Fixed B-income goes in field 210. On a one-off B-income amount, pay 8% AM-bidrag and then tax at the withholding rate on the rest.
- **Årsopgørelse (tax assessment notice).** For income year 2026 it opens in TastSelv Borger in March 2027 (the 2025 one opened from 23 March 2026 for business owners). Employees with no changes need do nothing.
- **Return deadline.** The self-employed must report final profit or loss and the business information by **1 July 2027** for income year 2026. An extended deadline can be applied for from mid-March to 1 July.
- **Restskat.** Tax still owed after the year is restskat, plus a surcharge (the Opkrævningsloven § 7, stk. 2 rate plus 1.5 points, rounded to one decimal). A small restskat (base DKK 18,300 at 2010 level, indexed; DKK 25,368 for income year 2025 per skat.dk) is added to the next year's preliminary tax when the årsopgørelse is ready in time. The rest falls due in three instalments on 1 August, 1 September and 1 October of the year after the income year, with the last payment day on the 20th of each month.

## Penalties and interest

- **Late return (skattetillæg, Skattekontrolloven § 73).** DKK 400 for each day late, at most DKK 10,000. If the person's taxable income for the year is not above the mellemskat threshold (DKK 641,200 for 2026), DKK 200 a day, at most DKK 5,000. Skattestyrelsen can waive it in full or in part in special cases.
- **Late return and restskat.** If the duty to report was not met on time, interest is added to the restskat and surcharge: the Opkrævningsloven § 7, stk. 2 rate plus 0.4 percentage points for each started month from 1 September of the year after the income year until the årsopgørelse is issued.
- **Restskat surcharge.** Charged on all restskat, whether or not anything was late (see above).
- **Wrong returns.** Fines for deliberate or grossly negligent under-reporting were not re-read for this version. Refer any such case.

## Cross-border points

- A person who moves in or out mid-year is fully liable only for the part of the year with residence; personfradrag and bands then need the actual liability period. Use dk-cross-border.
- Limited liability: Danish-source salary and business income through a Danish permanent establishment are taxed here, with a 25% rate in place of kommuneskat (PSL § 8 c).
- Foreign income of a fully liable person is taxed here with relief under the treaty or the credit method. The treaty and credit computations are in dk-cross-border.
- Share income: exit tax on shares when a person leaves is in dk-capital-gains.
- Researchers and key employees under the researcher scheme (KSL § 48 E) are outside the ordinary computation; see dk-payroll and dk-cross-border.

## Worked examples

### Example 1: sole trader, average municipality

Mette runs a personally owned design business outside VSO. Her 2026 profit is DKK 500,000. She has no other income, no capital income, is not a church member and lives in a municipality at the 2026 average rate of 25.049%.

AM-bidrag is 8% of DKK 500,000, so DKK 40,000. Personal income is DKK 460,000. Beskæftigelsesfradrag is 12.75% of 500,000 = 63,750, capped at DKK 63,300. Jobfradrag is 4.5% of (500,000 − 235,200) = 11,916, capped at DKK 3,100. Taxable income is 460,000 − 63,300 − 3,100 = DKK 393,600.

Kommuneskat is 25.049% of (393,600 − 54,100), which is DKK 85,041.36. Bundskat is 12.01% of (460,000 − 54,100), which is DKK 48,748.59. Personal income is under DKK 641,200, so no mellemskat, topskat or toptopskat. Total tax including AM-bidrag is about DKK 173,789.95.

```oa-check
name: Example 1, sole trader, profit DKK 500,000, average kommuneskat (2026)
inputs:
  profit: 500000
  kommune_rate_pct: 25.049
steps:
  - am_bidrag: profit * 0.08
  - personal_income: profit - am_bidrag
  - employment_allowance: min(profit * 0.1275, 63300)
  - job_allowance: clamp((profit - 235200) * 0.045, 0, 3100)
  - taxable_income: personal_income - employment_allowance - job_allowance
  - kommuneskat: (taxable_income - 54100) * kommune_rate_pct / 100
  - bundskat: (personal_income - 54100) * 0.1201
  - mellemskat: max(personal_income - 641200, 0) * 0.075
  - total_tax: am_bidrag + kommuneskat + bundskat + mellemskat
expected:
  am_bidrag: 40000
  taxable_income: 393600
  kommuneskat: 85041.355
  bundskat: 48748.59
  total_tax: 173789.945
```

### Example 2: high earner, skatteloft and share income

Lars is self-employed outside VSO with a 2026 profit of DKK 1,000,000. He lives in a municipality at 26.30%, is not a church member, has no net capital income, and receives DKK 100,000 of dividends.

AM-bidrag is DKK 80,000, so personal income is DKK 920,000. Both allowances are at their caps (DKK 63,300 and DKK 3,100), so taxable income is DKK 853,600.

Skatteloft: 12.01 + 7.5 + 26.30 = 45.81%, which is 1.24 points above 44.57%. Mellemskat is therefore charged at 6.26% instead of 7.5%: 6.26% of (920,000 − 641,200) = DKK 17,452.88. Topskat is 7.5% of (920,000 − 777,900) = DKK 10,657.50 and is not cut. Toptopskat does not apply. Bundskat is 12.01% of (920,000 − 54,100) = DKK 103,994.59. Kommuneskat is 26.30% of (853,600 − 54,100) = DKK 210,268.50.

The dividends are share income: 27% of DKK 79,400 plus 42% of DKK 20,600 = DKK 30,090. Dividend tax already withheld by the company is credited against this in the årsopgørelse.

```oa-check
name: Example 2, profit DKK 1,000,000 at 26.30% kommuneskat with skatteloft, plus DKK 100,000 dividends (2026)
inputs:
  profit: 1000000
  kommune_rate_pct: 26.30
  dividends: 100000
steps:
  - am_bidrag: profit * 0.08
  - personal_income: profit - am_bidrag
  - employment_allowance: min(profit * 0.1275, 63300)
  - job_allowance: clamp((profit - 235200) * 0.045, 0, 3100)
  - taxable_income: personal_income - employment_allowance - job_allowance
  - ceiling_excess_pct: max(12.01 + 7.5 + kommune_rate_pct - 44.57, 0)
  - mellemskat_rate_pct: 7.5 - ceiling_excess_pct
  - mellemskat: max(personal_income - 641200, 0) * mellemskat_rate_pct / 100
  - topskat: max(personal_income - 777900, 0) * 0.075
  - toptopskat: max(personal_income - 2592700, 0) * 0.05
  - bundskat: (personal_income - 54100) * 0.1201
  - kommuneskat: (taxable_income - 54100) * kommune_rate_pct / 100
  - share_tax: min(dividends, 79400) * 0.27 + max(dividends - 79400, 0) * 0.42
  - total_tax: am_bidrag + bundskat + mellemskat + topskat + toptopskat + kommuneskat + share_tax
expected:
  taxable_income: 853600
  mellemskat_rate_pct: 6.26
  mellemskat: 17452.88
  topskat: 10657.50
  bundskat: 103994.59
  kommuneskat: 210268.50
  share_tax: 30090
  total_tax: 452463.47
```

## Ask the client first

1. Where do you live, since when, and which municipality? Are you a member of Folkekirken? (Sets liability, the municipal rate and church tax.)
2. Is the work done as an employee, as a business, or through your own company? (Decides AM-bidrag base, deductions and which skill applies.)
3. Do you use virksomhedsordningen or kapitalafkastordningen, and does a spouse work in the business? (Changes the personal and capital income split.)
4. What interest do you pay and receive, and what dividends or share gains do you have? (Capital income moves the mellemskat base; share income has its own scale.)
5. Your date of birth, and do you receive ekstra børnetilskud? (Under-18 AM-bidrag rule, senior and single-parent allowances.)
6. Your current forskudsopgørelse and B-skat paid so far. (Shows whether restskat is building up.)

## Sources

| Source | URL | Read on |
|---|---|---|
| Skatte- og Vækstministeriet, Personskatteloven rates and thresholds 2026 and 2027 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/personskatteloven | 2026-10-26 |
| Skatte- og Vækstministeriet, amounts indexed under PSL § 20, 2025-2026 | https://svmn.dk/tal-og-metode/satser/regulering-af-beloebsgraenser/beloebsgraenser-i-skattelovgivningen-der-reguleres-efter-personskattelovens-20-2025-2026 | 2026-10-26 |
| Skatte- og Vækstministeriet, average municipal and church tax 2026 | https://svmn.dk/tal-og-metode/satser/statistik-i-kommunerne/kommuneskatter-gennemsnitsprocenten-i-2026 | 2026-10-26 |
| Lov nr. 482 af 22. maj 2024 | https://www.retsinformation.dk/eli/lta/2024/482 | 2026-10-26 |
| Personskatteloven, LBK nr. 1284 af 14. juni 2021 (current consolidation) | https://www.retsinformation.dk/eli/lta/2021/1284 | 2026-10-26 |
| Skattestyrelsen, restskat for 2025 (5.7%, DKK 25,368) | https://skat.dk/restskat | 2026-10-26 |
| Folketinget, L 138 (2023-24) as adopted: reform of personal tax (PSL §§ 5, 7, 7 a, 8, 9, 19; LL § 9 J) | https://folketingstidende.dk/samling/20231/lovforslag/L138/20231_L138_som_vedtaget.pdf | 2026-10-26 |
| Skattestyrelsen, bundskat, mellemskat, topskat and toptopskat 2026 | https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat | 2026-10-26 |
| Skattestyrelsen, beskæftigelses- og jobfradrag 2026 | https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag | 2026-10-26 |
| Skattestyrelsen, tax card and personal allowance | https://skat.dk/en-us/individuals/tax-card | 2026-10-26 |
| Skattestyrelsen, B-income, AM-bidrag and B-skat instalments | https://skat.dk/en-us/individuals/b-income | 2026-10-26 |
| Skattestyrelsen, tax on own business (fields, VSO, KAO, 1 July) | https://skat.dk/en-us/businesses/own-business/tax-on-own-business | 2026-10-26 |
| Skattestyrelsen, deduction for business expenses | https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses | 2026-10-26 |
| Skattestyrelsen, share income rates 2026 | https://skat.dk/en-us/individuals/shares-and-securities/buying-and-selling-shares-and-securities | 2026-10-26 |
| Skattestyrelsen, tax liability | https://skat.dk/en-us/individuals/taxation-in-denmark/tax-liability | 2026-10-26 |
| Den juridiske vejledning, skatteloft (PSL § 19) | https://info.skat.dk/data.aspx?oid=1948928 | 2026-10-26 |
| Den juridiske vejledning, skattetillæg under Skattekontrolloven § 73 | https://info.skat.dk/data.aspx?oid=2284578 | 2026-10-26 |
| Den juridiske vejledning, 1 July deadline for individuals | https://info.skat.dk/data.aspx?oid=2284485 | 2026-10-26 |
| Den juridiske vejledning, payment of restskat (KSL § 61) | https://info.skat.dk/data.aspx?oid=2169090 | 2026-10-26 |
| Den juridiske vejledning, spouses' tax calculation (KSL § 25 A) | https://info.skat.dk/data.aspx?oid=1976883 | 2026-10-26 |
| Den juridiske vejledning, depreciation of buildings | https://info.skat.dk/data.aspx?oid=2083987 | 2026-10-26 |
| Den juridiske vejledning, depreciation of goodwill | https://info.skat.dk/data.aspx?chk=220619&oid=2083994 | 2026-10-26 |

Not yet confirmed: the restskat surcharge percent for income year 2026 (published by 15 December 2026); the indexed restskat carry-over amount for income year 2026; the date in 2027 the 2026 årsopgørelse opens; the PSL § 13 loss order; fine levels for under-reporting; AM-bidrag for limited-liability persons; the voluntary-payment (frivillig indbetaling) rules for restskat; the rule from the old version that losses from a non-commercial (hobby) activity are not deductible against other income (case law and Skattestyrelsen guidance, not read today).
