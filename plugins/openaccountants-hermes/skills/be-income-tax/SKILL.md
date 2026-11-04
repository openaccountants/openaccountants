---
name: be-income-tax
description: "Belgian personal income tax (personenbelasting / impot des personnes physiques) for self-employed residents: traders and business owners (winst) and liberal professions (baten), for income 2026 (assessment year 2027). Covers the art. 130 scale (25%, 40%, 45%, 50%), the EUR 11,550 tax-free amount, actual costs versus the art. 51 lump sum (30% capped at EUR 6,070 for profits; 28.7% to 3% capped at EUR 5,340 for benefits), deduction of social contributions and VAPZ, restaurant and gift limits, car costs, the municipal surcharge, prepayments (voorafbetalingen) and the 2026 bonification rates, and the end of the prepayment increase for self-employed profits. Trigger on: personenbelasting zelfstandige, IPP indépendant, beroepskosten, forfaitaire beroepskosten, voorafbetalingen, bonificatie, Tax-on-web zelfstandige. Out of scope: be-employee-income-tax (employees and pensioners), be-social-contributions, belgium-payroll, be-corporate-tax, be-capital-gains, be-cross-border."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/be-income-tax"
  jurisdiction: "BE"
  tax_year: "2026"
  last_updated: "2026-10-23"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Belgium: income tax for the self-employed (income 2026, assessment year 2027) v2.1

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Belgium.

This skill computes the annual personal income tax of a Belgian resident who earns self-employed income. It links to the other Belgian skills instead of repeating them:

- The tax-free amount supplements for children and dependants, the marital quotient, joint assessment, federal reductions and the refund mechanics: `be-employee-income-tax`
- Quarterly self-employed social contributions and VAPZ: `be-social-contributions`
- Company directors paid by their company, and the company itself: `be-corporate-tax`
- Capital gains on financial assets: `be-capital-gains`
- Residence, non-residents and exit tax: `be-cross-border`

## Who this applies to

- **Belgian residents** taxed in the personenbelasting on worldwide income (see `be-cross-border` for the residence test).
- **Self-employed with profits (winst)**: traders, craftsmen, shopkeepers and other industrial, commercial or agricultural businesses run as a sole trader (art. 23, §1, 1° WIB 92).
- **Self-employed with benefits (baten)**: liberal professions, offices and other gainful activities not counted as profits (art. 23, §1, 2° and art. 27 WIB 92), for example consultants, doctors, lawyers, architects.
- **Assisting spouses (meewerkende echtgenoot)** for the share of income attributed to them.

Out: company directors (3% lump sum, increase for missing prepayments still applies; see "Prepayments" and `be-corporate-tax`), companies, and non-residents (`be-cross-border`). Employees and pensioners are in `be-employee-income-tax`.

Income year 2026 is assessment year 2027. All income tax figures below are the indexed amounts for income 2026 as printed in Fisconetplus. Several were changed by the law of 15 July 2026 (Belgian Official Gazette 29 July 2026), which applies from assessment year 2027.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Tax scale | 25% to EUR 16,720; 40% from EUR 16,720 to EUR 29,510; 45% from EUR 29,510 to EUR 51,070; 50% above EUR 51,070 | Income 2026 | [Art. 130 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796a4fc5-340e-4c89-a72a-88caa804ca96) |
| Tax-free amount, basic | EUR 11,550 per taxpayer (supplements for children and dependants: see `be-employee-income-tax`) | Income 2026 (law of 15 July 2026) | [Art. 131 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f3c5d665-cac4-4cbd-b714-bd287f791751) |
| Tax on the tax-free amount (deducted from the scale tax) | 25% up to EUR 11,750; 30% from EUR 11,750 to EUR 16,720; 40% to EUR 27,860; 45% to EUR 51,070; 50% above | Income 2026 | [Art. 134 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/20a503a9-4213-4e60-a91c-0ebb907e176a) |
| Lump-sum expenses, profits (winst) | 30% of gross profits after social contributions and the purchase price of goods sold; at most EUR 6,070 | Income 2026 | [Art. 51 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e2fb1778-ac33-4e91-8e57-e53c0cac384c) |
| Lump-sum expenses, benefits (baten) | 28.7% of the first EUR 7,720; 10% from EUR 7,720 to EUR 15,340; 5% from EUR 15,340 to EUR 25,530; 3% above EUR 25,530; at most EUR 5,340 | Income 2026 | [Art. 51 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e2fb1778-ac33-4e91-8e57-e53c0cac384c) |
| Lump-sum expenses, assisting spouse and company directors | Assisting spouse 5%, at most EUR 5,340; company directors 3%, at most EUR 3,200 | Income 2026 | [Art. 51 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e2fb1778-ac33-4e91-8e57-e53c0cac384c) |
| Personal social contributions | Deductible as professional expenses, including VAPZ contributions (art. 45 programme law of 24 December 2002) | Income 2026 | [Art. 52, 7° and 7°bis WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e2123748-b2c4-49ab-8b2d-5eacb94fbc34) |
| VAPZ maximum rate | Ordinary VAPZ 8.50% of the reference income (was 8.17%); social VAPZ 9.78% (was 9.40%); from contribution year 2026 | 2026 | [RSVZ, Wijzigingen VAPZ, 13 October 2026](https://www.rsvz.be/nl/nieuws/wijzigingen-vapz) |
| Restaurant costs | 69% deductible (31% disallowed) | Income 2026 | [Art. 53, 8°bis WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/69b77d81-d360-48f5-a66c-fa9eee78daca) |
| Reception costs and business gifts | 50% deductible; branded advertising items excluded from the limit | Income 2026 | [Art. 53, 8° WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/69b77d81-d360-48f5-a66c-fa9eee78daca) |
| Car costs, cars bought, leased or rented from 1 January 2026 | Not deductible unless the car emits no CO2. Plug-in hybrid: electricity at the zero-emission rate; other costs (not fuel) at 120% - 0.5% x g CO2/km, at most 75% for a car bought, leased or rented before 1 January 2028 unless it emits 50 g/km or less. Home to work by car: EUR 0.15 per km | Income 2026 | [Art. 66 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/dfec7b36-48d5-41fc-abea-04a7eaac88a3) |
| Car costs, cars bought, leased or rented before 1 January 2026 | 120% - (0.5% x coefficient x g CO2/km), coefficient 1 for diesel, 0.95 for other fuels (0.90 for natural gas under 12 fiscal hp), rounded to one decimal. Bought before 1 July 2023: at least 50% (40% at 200 g/km or more or with no CO2 data), at most 100%; bought before 1 January 2018: at least 70% for income 2026. Bought from 1 July 2023 to 31 December 2025: at most 25% unless zero-emission, 0% with no CO2 data. Plug-in hybrid bought from 1 July 2023 to 31 December 2025: electricity 100%, fuel at the 25% cap, other costs by the formula at most 75% (100% at 50 g/km or less) | Income 2026 | [Art. 550 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d51b4c37-c6d6-4fd2-ad8b-28ee18069895) |
| Prepayment increase on profits and benefits | None from assessment year 2027. The increase now applies only to company directors' pay (art. 30, 2°) | Income 2026 (law of 15 July 2026) | [Art. 157 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/333419cd-668a-47b2-b989-0e421421f5bc) |
| Base rate (basisrentevoet) | 2%: the ECB marginal lending rate on 1 January 2026 (2.40%) rounded down to the unit, never under 1% | Income 2026 | [Art. 161 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1f33c7f0-21c9-4cc3-9e45-41cb00db2b7e); [ECB key interest rates](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html) |
| Bonification on prepayments (self-employed) | 1.5, 1.25, 1 and 0.75 times the base rate: 3% (by 10 April 2026), 2.5% (by 10 July), 2% (by 10 October), 1.5% (by 20 December). Prepayments from 21 December 2026 to 20 February 2027: 0.5 times the base rate, 1% | Income 2026 | [Art. 176](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/8eff9596-837e-469e-8e90-0b1d72e582e1) and [art. 177 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d5619aa0-3a1c-4dba-8600-7e87e8c4bdfc) |
| Bonification ceiling | Only prepayments up to the total tax raised to 106%, less withholding, tax credits and any prepayments needed to avoid a director's increase. The tax on profits or benefits of a person who assists or replaces a self-employed person without an employment contract (a helper), and on indemnities under art. 27, second paragraph, 5° and 6°, is left out, so prepayments on that income earn no bonification | Income 2026 (law of 15 July 2026) | [Art. 175 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/db64628c-365f-4ee1-b0fb-122282a6c557) |
| Prepayment increase, company directors only | 2.25 times the base rate (4.5%) of the tax on directors' pay counted at 106%, less 3, 2.5, 2 and 1.5 times the base rate (6%, 5%, 4%, 3%) of prepayments by 10 April, 10 July, 10 October and 20 December; the positive difference is cut to 90%; none under 0.5% of the tax or EUR 100 | Income 2026 | [Art. 159](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/b35e0c32-dc58-4847-b389-4481bf0a969b), [160](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/fd39784e-027e-4943-bd38-458c44606ede), [163](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e97ca46f-5f52-425e-87cb-723b84f6f0ba) and [165 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/38f2eab4-a66d-494a-8a4d-d5177ad80182) |
| Municipal surcharge | Rate set by each municipality, charged on the total tax | Income 2026 | [Art. 466](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/81bf3101-a837-4d89-8b97-713e080f00ac) and [art. 468 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/4d803548-89eb-4ef5-b1a5-12f5751e1313) |
| Late payment interest | 4% a year for 2026 and 2027 | 2026, 2027 | [Art. 414 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/db296af5-75b3-49bc-95e2-a35bb742fed5); [law of 5 May 1865, art. 2, §2/1](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/da7e0caf-3428-43aa-ab80-30410a15beca) |
| Tax increase | 10% to 200% of the tax on undeclared or late income; none for a first offence in good faith, presumed | Income 2026 | [Art. 444 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5095859f-8ffb-42f9-b535-3197a7c3dbe0) |

**Coming next year, not for income 2026.** The law of 15 July 2026 adds an entrepreneur deduction (ondernemersaftrek, new art. 81 WIB 92): 10% of profits and benefits after deducting professional losses (art. 78 to 80), at most EUR 311, from assessment year 2028 (income 2027); the cap becomes EUR 415 from assessment year 2030 (income 2029). It does not apply to an assisting spouse's income, helpers' income, replacement income or attendance fees. Do not apply it to income 2026.

## The taxable base

Work through the return in this order.

1. **Gross receipts.** All profits or benefits of 2026. A VAT-registered taxpayer counts receipts net of VAT. Receipts on the bank statement are a starting point; reconcile them with the invoices issued.
2. **Less social contributions paid in 2026.** Quarterly contributions, regularisations and VAPZ paid in the year (art. 52, 7° and 7°bis). Amounts are in `be-social-contributions`.
3. **Less professional expenses: actual or lump sum.** Actual costs are deductible if made to earn the income and proven (art. 49). Without proof, the art. 51 lump sum applies instead, computed on gross receipts less social contributions and, for traders, the purchase price of goods sold. One method for all income of the same category. Taxpayers on the fixed bases of art. 342, §1 (forfaitaire grondslagen) get no lump sum.
   - Profits (winst): 30%, at most EUR 6,070. Purchases of goods sold stay deductible on top.
   - Benefits (baten): 28.7% / 10% / 5% / 3% on the bands above, at most EUR 5,340.
   Compare both before choosing. Actual costs win when real costs (rent, insurance, software, travel, depreciation) exceed the lump sum.
4. **Limits on actual costs.** Restaurant 69%, receptions and gifts 50% (art. 53). Car costs follow art. 66 (see the table). Fines, income tax and private living costs are not deductible. Mixed-use items (phone, internet, home office) count only for the business share, which the taxpayer must show.
5. **Depreciation.** Assets with a limited useful life are depreciated over that life (art. 52, 6° and art. 61 to 64), not expensed. Keep an asset register.
6. **Net professional income.** For a married couple or legal cohabitants, the assisting-spouse attribution (art. 86) and the marital quotient (art. 87 and 88) can move part of it; see `be-employee-income-tax`.
7. **Scale tax** on taxable income (art. 130), **less tax on the tax-free amount** (art. 134). With children or dependants, add the supplements first.
8. **Less reductions** (pension savings, gifts, childcare and others) as in `be-employee-income-tax`.
9. **Regional split and municipal surcharge.** The basic tax is shared between the federal state and the region, which levies its own surcharge and can grant regional reductions (see `be-employee-income-tax`). The worked examples below assume the regional surcharge exactly offsets the federal autonomy cut; that is an assumption, not a confirmed 2026 result. Then multiply the tax by the municipality's rate (art. 466). The rate must be known; if the municipality is unknown, stop and ask.
10. **Prepayments and bonification.** Deduct prepayments made for 2026 and the bonification they earned (art. 175 to 177). No increase for missing prepayments on self-employed profits or benefits from assessment year 2027.

### Classifying bank lines

Use this as a first pass on a bank statement. Anything that does not match goes to the general rules above.

| Pattern | Treatment |
|---|---|
| Transfer from a client, STRIPE / PAYPAL payout | Business receipts (net of VAT if registered) |
| LOON, WEDDE, WERKGEVER | Employment pay, not self-employed income (`be-employee-income-tax`) |
| HUUR ONTVANGEN | Rental income, not self-employed income |
| INTERESTEN, DIVIDEND | Investment income, not self-employed income |
| FOD FINANCIEN TERUGBETALING | Tax refund, not income |
| Social insurance fund (ACERTA, LIANTIS, XERIUS, GROUP S, PARTENA, UCM) | Social contributions, deductible (art. 52, 7°) |
| VAPZ / PLCI | Deductible within the VAPZ maximum (art. 52, 7°bis) |
| Office rent, professional insurance, accountant, lawyer, software, advertising, training, bank charges | Deductible if for the business |
| RESTAURANT, ZAKENLUNCH | 69% deductible if business |
| GESCHENK, RELATIEGESCHENK, reception | 50% deductible |
| BRANDSTOF, GARAGE, car lease | Art. 66 rules; ask CO2, fuel type, purchase date and business share |
| BOETE, PERSONENBELASTING, PRIVE, supermarket | Not deductible |
| Computer, furniture, vehicle purchase | Asset: depreciate, do not expense |
| Own-account transfer, loan principal, VAT payment | Exclude from profit |
| VOORAFBETALING | Prepayment: credit against the tax, record the date |

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Prepayments for income 2026 | By 10 April, 10 July, 10 October and 20 December 2026; a further window from 21 December 2026 to 20 February 2027 earns 1% | [Art. 177 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d5619aa0-3a1c-4dba-8600-7e87e8c4bdfc); [art. 176 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/8eff9596-837e-469e-8e90-0b1d72e582e1) |
| Electronic return with self-employed income | By 16 October 2027, and at least five months after the electronic return is available | [Art. 308/1 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/51c63576-3d3c-49cd-bf84-e5c6e20022ad) |
| Paper return | By 30 June 2027, and at least one month after the form is sent | [Art. 308, §1 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/182821e5-122a-4948-867e-297c16371fe1) |
| Paying a balance | Within two months of the assessment notice being sent | [Art. 413 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/09b8ca93-c681-40df-9a8f-c5a947e063ae) |
| Social contributions | Quarterly, by the last day of each quarter | `be-social-contributions` |

The exact Tax-on-web dates for income 2026 are not yet published; see "Not yet confirmed".

## Penalties and interest

- **Tax increase (art. 444 WIB 92).** Not filing, filing late, or filing a wrong return adds 10% to 200% of the tax on the undeclared or late income. No increase for a first offence in good faith, which is presumed since the programme law of 18 July 2025. It applies only if the undeclared or late income reaches EUR 2,500.
- **Administrative fine (art. 445 WIB 92).** EUR 50 to EUR 1,250 per breach.
- **Late payment interest (art. 414 WIB 92).** 4% a year for 2026 and 2027, per calendar month on the unpaid tax rounded down to EUR 10; not charged under EUR 5 a month.
- **Missing prepayments.** For self-employed profits and benefits there is no increase from assessment year 2027 (art. 157 as amended by the law of 15 July 2026). The cost of not prepaying is the lost bonification and a larger balance later. A self-employed person who is also a company director still risks the increase on the director's pay.

## Cross-border points

- **Foreign self-employed income** exempt under a treaty is exempt with progression; the municipal surcharge can still be computed as if the income were Belgian (art. 466bis). See `be-cross-border`.
- **Fixed base abroad.** Profits of a permanent establishment or fixed base in another state follow the treaty; keep separate accounts.
- **Social security** depends on where the person works under EU Regulation 883/2004; an A1 certificate decides which country's contributions are deductible. See `be-social-contributions`.
- **Non-residents** with a Belgian business file the non-resident return; see `be-cross-border`.

## Worked examples

### Example 1: consultant (benefits), lump sum beats actual costs

Facts: a single resident consultant, no children, gross benefits EUR 60,000 in 2026 (net of VAT). Social contributions paid in 2026: EUR 10,500. Provable costs: EUR 3,000. No prepayments. The municipality's rate is assumed to be 7%. The regional surcharge is assumed to offset the federal autonomy cut exactly.

1. Base for the lump sum: 60,000 - 10,500 = EUR 49,500.
2. Lump sum for benefits: 28.7% x 7,720 = 2,215.64; 10% x (15,340 - 7,720) = 762; 5% x (25,530 - 15,340) = 509.50; 3% x (49,500 - 25,530) = 719.10. Total EUR 4,206.24, under the EUR 5,340 cap. It beats the EUR 3,000 of actual costs, so the lump sum is used.
3. Net professional income: 49,500 - 4,206.24 = EUR 45,293.76.
4. Scale tax: 4,180 + 5,116 + 45% x (45,293.76 - 29,510) = EUR 16,398.69.
5. Less tax on the tax-free amount: 25% x 11,550 = 2,887.50. Tax EUR 13,511.19.
6. Municipal surcharge at 7%: EUR 945.78. Total EUR 14,456.97.
7. No prepayments, so no bonification. From income 2026 there is also no increase for missing prepayments on benefits. The full EUR 14,456.97 is due within two months of the assessment.

```oa-check
name: Consultant on benefits EUR 60,000, lump sum, income 2026
inputs:
  gross: 60000
  social_contributions: 10500
  actual_costs: 3000
  tax_free: 11550
  municipal_rate: 0.07
steps:
  - base: gross - social_contributions
  - lump_a: min(base, 7720) * 0.287
  - lump_b: (min(base, 15340) - 7720) * 0.10
  - lump_c: (min(base, 25530) - 15340) * 0.05
  - lump_d: max(base - 25530, 0) * 0.03
  - lump_sum: min(lump_a + lump_b + lump_c + lump_d, 5340)
  - costs_used: max(lump_sum, actual_costs)
  - net_income: base - costs_used
  - scale_tax: round(min(net_income, 16720) * 0.25 + (min(net_income, 29510) - 16720) * 0.40 + (min(net_income, 51070) - 29510) * 0.45 + max(net_income - 51070, 0) * 0.50, 2)
  - tax_on_tax_free: tax_free * 0.25
  - tax: scale_tax - tax_on_tax_free
  - municipal: round(tax * municipal_rate, 2)
  - total_tax: tax + municipal
expected:
  base: 49500
  lump_sum: 4206.24
  net_income: 45293.76
  scale_tax: 16398.69
  tax: 13511.19
  municipal: 945.78
  total_tax: 14456.97
```

### Example 2: trader (profits), lump sum capped, prepayments with bonification

Facts: a single resident shopkeeper, no children. Gross receipts EUR 120,000 in 2026 (net of VAT); goods bought for resale EUR 40,000; social contributions paid EUR 15,000; other provable costs EUR 9,000. Prepayments: EUR 5,000 on 2 April 2026, EUR 5,000 on 8 July 2026 and EUR 5,000 on 15 January 2027. Municipal rate assumed 7.5%. Same regional assumption as Example 1.

1. Base: 120,000 - 40,000 - 15,000 = EUR 65,000.
2. Lump sum for profits: 30% x 65,000 = 19,500, capped at EUR 6,070. Actual costs of EUR 9,000 are higher, so actual costs are used.
3. Net professional income: 65,000 - 9,000 = EUR 56,000.
4. Scale tax: 4,180 + 5,116 + 9,702 + 50% x (56,000 - 51,070) = EUR 21,463.
5. Less 2,887.50 on the tax-free amount: EUR 18,575.50.
6. Municipal surcharge at 7.5%: EUR 1,393.16. Total EUR 19,968.66.
7. Bonification ceiling (art. 175): 18,575.50 x 106% = EUR 19,690.03. All prepayments fit under it.
8. Bonification: 3% x 5,000 (by 10 April) = 150; 2.5% x 5,000 (by 10 July) = 125; the January 2027 payment falls in the new 21 December to 20 February window, 1% x 5,000 = 50. Total EUR 325.
9. Balance: 19,968.66 - 15,000 - 325 = EUR 4,643.66, due within two months of the assessment notice.

```oa-check
name: Shopkeeper, profits, actual costs, prepayments and bonification, income 2026
inputs:
  receipts: 120000
  goods_sold: 40000
  social_contributions: 15000
  actual_costs: 9000
  tax_free: 11550
  municipal_rate: 0.075
  va1: 5000
  va2: 5000
  va_late: 5000
  base_rate: 0.02
steps:
  - base: receipts - goods_sold - social_contributions
  - lump_sum: min(base * 0.30, 6070)
  - costs_used: max(lump_sum, actual_costs)
  - net_income: base - costs_used
  - scale_tax: min(net_income, 16720) * 0.25 + (min(net_income, 29510) - 16720) * 0.40 + (min(net_income, 51070) - 29510) * 0.45 + max(net_income - 51070, 0) * 0.50
  - tax: scale_tax - tax_free * 0.25
  - municipal: round(tax * municipal_rate, 2)
  - total_tax: tax + municipal
  - bonif_ceiling: round(tax * 1.06, 2)
  - bonif_regular: va1 * 1.5 * base_rate + va2 * 1.25 * base_rate
  - bonif_late: min(va_late, bonif_ceiling - va1 - va2) * 0.5 * base_rate
  - bonification: bonif_regular + bonif_late
  - balance: total_tax - va1 - va2 - va_late - bonification
expected:
  base: 65000
  lump_sum: 6070
  net_income: 56000
  scale_tax: 21463
  tax: 18575.50
  municipal: 1393.16
  total_tax: 19968.66
  bonif_ceiling: 19690.03
  bonification: 325
  balance: 4643.66
```

## Ask the client first

1. Profits (trade, shop, craft) or benefits (liberal profession)? It sets the lump-sum scale and cap.
2. Municipality of residence on 1 January 2027, for the surcharge rate.
3. Social contributions and VAPZ actually paid in 2026, with the fund's statement.
4. Actual costs with invoices, and any car: CO2, fuel type, date bought or leased, business share.
5. Prepayments made for 2026, with the payment dates.
6. Family situation and any other income (pay, rent, foreign income), whether the client is also a company director, and whether any of the income is earned as a helper who assists or replaces another self-employed person (no bonification on that part).
7. Region of residence, for the regional surcharge and regional reductions.

## Sources

| Source | URL | Read on |
|---|---|---|
| Fisconetplus, art. 51 WIB 92 (income 2026), lump-sum expenses | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e2fb1778-ac33-4e91-8e57-e53c0cac384c | 2026-10-23 |
| Fisconetplus, art. 52 WIB 92 (income 2026), social contributions | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e2123748-b2c4-49ab-8b2d-5eacb94fbc34 | 2026-10-23 |
| Fisconetplus, art. 53 WIB 92 (income 2026), restaurant and gift limits | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/69b77d81-d360-48f5-a66c-fa9eee78daca | 2026-10-23 |
| Fisconetplus, art. 66 WIB 92 (income 2026), car costs | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/dfec7b36-48d5-41fc-abea-04a7eaac88a3 | 2026-10-23 |
| Fisconetplus, art. 550 WIB 92, car costs for cars bought before 1 January 2026 (version for assessment year 2027) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d51b4c37-c6d6-4fd2-ad8b-28ee18069895 | 2026-10-23 |
| Fisconetplus, art. 130 WIB 92 (income 2026), tax scale | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796a4fc5-340e-4c89-a72a-88caa804ca96 | 2026-10-23 |
| Fisconetplus, art. 131 WIB 92 (income 2026), tax-free amount | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f3c5d665-cac4-4cbd-b714-bd287f791751 | 2026-10-23 |
| Fisconetplus, art. 134 WIB 92 (income 2026) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/20a503a9-4213-4e60-a91c-0ebb907e176a | 2026-10-23 |
| Fisconetplus, art. 157 WIB 92 (income 2026), prepayment increase | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/333419cd-668a-47b2-b989-0e421421f5bc | 2026-10-23 |
| Fisconetplus, art. 159 WIB 92 (income 2026) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/b35e0c32-dc58-4847-b389-4481bf0a969b | 2026-10-23 |
| Fisconetplus, art. 160 WIB 92 (income 2026) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/fd39784e-027e-4943-bd38-458c44606ede | 2026-10-23 |
| Fisconetplus, art. 162 WIB 92 (income 2026), royal decree power to change the increase rate | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/4519285d-7f8c-4268-94a9-32e0de756319 | 2026-10-23 |
| Fisconetplus, art. 161 WIB 92 (income 2026), base rate | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1f33c7f0-21c9-4cc3-9e45-41cb00db2b7e | 2026-10-23 |
| Fisconetplus, art. 163 WIB 92 (income 2026) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e97ca46f-5f52-425e-87cb-723b84f6f0ba | 2026-10-23 |
| Fisconetplus, art. 165 WIB 92, tax counted at 106% | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/38f2eab4-a66d-494a-8a4d-d5177ad80182 | 2026-10-23 |
| Fisconetplus, art. 175 WIB 92 (income 2026), bonification | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/db64628c-365f-4ee1-b0fb-122282a6c557 | 2026-10-23 |
| Fisconetplus, art. 176 WIB 92 (income 2026) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/8eff9596-837e-469e-8e90-0b1d72e582e1 | 2026-10-23 |
| Fisconetplus, art. 177 WIB 92 (income 2026), bonification rates | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d5619aa0-3a1c-4dba-8600-7e87e8c4bdfc | 2026-10-23 |
| Fisconetplus, art. 308 and 308/1 WIB 92, filing dates | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/182821e5-122a-4948-867e-297c16371fe1 | 2026-10-23 |
| Fisconetplus, art. 413 and 414 WIB 92, payment and interest | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/db296af5-75b3-49bc-95e2-a35bb742fed5 | 2026-10-23 |
| Fisconetplus, art. 444 and 445 WIB 92 (income 2026) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5095859f-8ffb-42f9-b535-3197a7c3dbe0 | 2026-10-23 |
| Fisconetplus, art. 465 to 470 WIB 92 (income 2026), municipal surcharge | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/81bf3101-a837-4d89-8b97-713e080f00ac | 2026-10-23 |
| Belgian Official Gazette, law of 15 July 2026 (Numac 2026005724), title 12 prepayments and the entrepreneur deduction | https://www.ejustice.just.fgov.be/eli/wet/2026/07/15/2026005724/staatsblad | 2026-10-23 |
| ECB, key interest rates (marginal lending facility 2.40% from 11 June 2025 to 16 June 2026) | https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html | 2026-10-23 |
| RSVZ, Wijzigingen VAPZ (13 October 2026) | https://www.rsvz.be/nl/nieuws/wijzigingen-vapz | 2026-10-23 |

Not yet confirmed: whether a royal decree under art. 162 set a different increase rate for assessment year 2027 (FPS Finance pages at financien.belgium.be were behind a human-verification check and could not be read; the rates above follow the law and the ECB rate); the Tax-on-web opening date and any administrative extension for income 2026; the deductible percentage for zero-emission cars (the art. 66, §1 text on Fisconetplus does not print it); the regional surcharge rates and autonomy factor for income 2026 (the examples assume they offset exactly); the VAPZ maximum in euro for 2026; whether art. 64 still allows declining-balance depreciation for a self-employed person in 2026.

> Contributed by Ryan Duguid.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `be-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/be-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
