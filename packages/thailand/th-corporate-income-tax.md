---
name: th-corporate-income-tax
description: "Thailand ordinary corporate income tax for 2026: accrual net-profit adjustments, continuously qualifying SME bands, PND.50 and PND.51 preparation, payment credits and foreign-company withholding boundaries."
jurisdiction: TH
tax_year: 2026
last_updated: 2026-11-16
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
category: international
version: 1.0
---

# Thailand corporate income tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

**2026 answer layer:** compute ordinary net-profit CIT for a Thai-incorporated company or juristic partnership and the Thai business of a foreign company. Establish paid-up capital, sales/service revenue and the qualifying history before applying the SME bands. Separate non-resident gross-income withholding, branch profit disposal, special industries, incentives and [top-up tax](th-top-up-tax.md).

Thai incorporation brings worldwide business profit into the ordinary tax computation; a foreign company carrying on business in Thailand is taxed on profit from or connected with that Thai business. A foreign company receiving specified Thai-paid income without carrying on business here follows §70 rather than an automatic net-profit assessment. See [Revenue Code §§65-66 and 70](https://www.rd.go.th/english/37764.html).

## Rates, bands and thresholds

| Item | Amount and conditions | Period | Official source |
|---|---|---|---|
| Ordinary net-profit rate | 20% of taxable net profit; special regimes require their own legal basis | 2026 | [Income Tax Schedule (2)(a)](https://www.rd.go.th/5938.html) |
| SME eligibility | Paid-up capital at period end at most THB 5,000,000 AND sales/service revenue at most THB 30,000,000; check the continuous qualification rule from periods starting on/after 1 January 2012 | 2026 | [Royal Decree 530 §§6-8, amended by 583 and 603 (amounts in words on the page)](https://www.rd.go.th/28271.html) |
| Qualifying SME first slice | Exempt up to THB 300,000 of net profit | 2026 | [Royal Decree 530 §7 (in words on the page)](https://www.rd.go.th/28271.html) |
| Qualifying SME middle slice | 15% only on profit over THB 300,000 and up to THB 3,000,000 | Periods beginning on/after 1 January 2017 | [Royal Decree 530 §6(3)(b), as amended by 603 (in words on the page)](https://www.rd.go.th/28271.html) |
| Qualifying SME top slice | 20% only on profit over THB 3,000,000 | Periods beginning on/after 1 January 2017 | [Royal Decree 530 §6(3)(b), as amended by 603 (in words on the page)](https://www.rd.go.th/28271.html) |
| Annual PND.50 | File and pay within 150 days after the accounting-period end | 2026 periods | [Revenue Code §§68-69](https://www.rd.go.th/english/37764.html) |
| Half-year PND.51 | File and pay within 2 months after the first 6 months; first/final period shorter than 12 months excepted | 2026 periods | [Revenue Code §67 bis](https://www.rd.go.th/english/37764.html) |
| PND.51 estimated-profit base | Compute tax on one half of the estimated annual taxable net profit, then apply the applicable rate/bands; do not halve annual SME tax | Ordinary estimate method, §67 bis(1) | [PND.51 instructions for periods beginning on/after 1 January 2025, pages 3-4](https://www.rd.go.th/fileadmin/tax_pdf/cit/2568/Ins51_290468.pdf) |
| Half-year underestimation | More than 25% underestimation without reasonable cause can trigger 20% surcharge on the applicable tax shortfall; actual-profit filers have a separate shortfall rule | 2026 periods | [Revenue Code §67 ter](https://www.rd.go.th/english/37764.html) |

## The base

1. Reconcile the accounts to all income from the business, including non-cash benefits and foreign business income where applicable. Use the accrual basis: recognise income arising in the period even if not received, with related expenses under §§65 bis and 65 ter. Record first-period and approved year-end changes; the usual period is 12 months ([§65](https://www.rd.go.th/english/37764.html)).
2. Build a tax-adjustment schedule rather than taxing accounting profit unchanged. Test capital expenditure and depreciation, reserves, personal or non-business expenses, unsupported payees, excessive shareholder remuneration, fines, surcharges and corporate income tax. Entertainment expense has separate deductibility conditions; VAT treatment is a different test. Do not invent deduction percentages from an old summary ([§§65 bis and 65 ter](https://www.rd.go.th/english/37764.html)).
3. Track eligible losses by originating period. The ordinary carry-forward is the previous 5 accounting periods; losses already used or reimbursed cannot be reused ([§65 ter(12)](https://www.rd.go.th/english/37764.html)).
4. For Thai-company dividends received, test the partial exclusion and the full-exclusion conditions in §65 bis(10), including qualifying listed-company or qualifying shareholding status, no cross-holding where required, and the holding periods before and after receipt. Do not label every domestic dividend exempt ([§65 bis(10)](https://www.rd.go.th/english/37764.html)).
5. Apply the ordinary rate or prove SME eligibility and apply the marginal slices. A period that exceeds the qualifying capital or sales/service-revenue ceiling can break the continuous condition; do not regain the concession automatically just by falling below the ceiling later ([Royal Decree 530 §8](https://www.rd.go.th/28271.html)).
6. Deduct only supported withholding and half-year payments creditable to this taxpayer and period. Reconcile certificates and tax receipts to the resulting payable or overpayment ([§§67 bis and 69 bis](https://www.rd.go.th/english/37764.html)).

## Deadlines and filing

Prepare PND.51 under §67 bis(1) by estimating annual tax-adjusted net profit, deducting eligible brought-forward losses and exempt profit as instructed, taking one half of the resulting estimated taxable profit, and applying the applicable rate/bands to that half-profit base. Do not compute annual SME tax and divide it by two: the marginal exemption/bands make those different calculations. The [current PND.51 instructions, pages 3-4, method 1 and items 1(1)(7)/2](https://www.rd.go.th/fileadmin/tax_pdf/cit/2568/Ins51_290468.pdf) set out that sequence. Listed companies, banks, finance, securities and credit foncier companies and prescribed entities instead use the statutory actual first-half net-profit method. Document a large estimate/actual variance and reasonable cause; an exemption for a short first/final period must be checked, not assumed for every loss-maker.

For PND.50, gather the signed accounts, tax reconciliation, losses, income-tax certificates, PND.51 proof and incentive documents. Use the Revenue Department's [official filing-service route](https://www.rd.go.th/rdeservice/63813.html) to e-Filing, choose PND.50 or PND.51 and the correct taxpayer, period and original/amended status; enter the relevant net-profit and tax computation, attach the required statements, review the calculated liability, submit, pay using the generated reference, and retain the return, acknowledgement and payment receipt separately. This is a preparation sequence, not a claim to have tested a signed-in portal. The statutory annual deadline is independent of the AGM date. No general electronic extension is assumed without the period's published calendar.

## Penalties and interest

The half-year surcharge is stated above with its reasonable-cause condition. Late annual filing/payment, audit adjustments and criminal offences require the applicable assessment and penalty provisions; do not substitute the half-year surcharge for every default. Current remission instructions and a complete annual penalty computation have not been read for this skill and remain under Not yet confirmed.

## Cross-border points

For a foreign company not carrying on business in Thailand, identify the income category and payer, beneficial ownership, treaty residence and the applicable treaty article before withholding. The domestic [Income Tax Schedule (2)(b)-(d)](https://www.rd.go.th/5938.html) sets 15% for §70 income other than the specified dividend/profit-share category, 10% for §40(4)(b) dividends/profit shares within §70, and 10% for §70 bis profit disposal. Apply these only after establishing the charging provision: interest and royalties are not automatically taxable merely because money was sent abroad. Do not apply a corporate-recipient provision indiscriminately to a resident individual. [Section 70](https://www.rd.go.th/english/37764.html) also contains an exception for specified interest from the government or a qualifying Thai-law financial institution. Treaty reductions require evidence. Domestic-company dividend withholding has its own exclusions and must not be decided solely by the old blanket rate.

Branch-profit disposal is a separate §70 bis event, not the ordinary corporate-income-tax return. Foreign international transport has the §67 gross-receipts method. Special industries, BOI privileges, transfer pricing and treaty permanent-establishment questions require their own full analysis. Preserve those boundaries rather than treating every foreign-company receipt as ordinary Thai net profit.

## Two worked examples that recompute

**SME or ordinary rate, same profit.** Assume a qualifying ordinary Thai SME, taxable profit THB 1,200,000, period-end paid-up capital THB 2,000,000 and sales/service revenue THB 10,000,000, with no historical qualification breach and no special incentive. SME tax is THB 135,000; the ordinary-rate counterfactual is THB 240,000. The THB 105,000 difference is derived, not an election available to an ineligible entity.

```oa-check
name: Thailand SME eligibility comparison
inputs:
  profit: 1200000
steps:
  - sme_tax: max(min(profit, 3000000) - 300000, 0) * 0.15 + max(profit - 3000000, 0) * 0.20
  - ordinary_tax: profit * 0.20
  - difference: ordinary_tax - sme_tax
expected:
  sme_tax: 135000
  ordinary_tax: 240000
  difference: 105000
```

**Crossing the SME top slice and crediting payments.** Qualifying profit THB 4,000,000 gives THB 605,000 tax. With a documented PND.51 payment of THB 250,000 and eligible withholding certificates of THB 30,000, the annual balance is THB 325,000. The same profit under the ordinary rate would give THB 800,000 before credits. These are hypothetical inputs, not statutory thresholds.

```oa-check
name: Thailand SME top band and annual credits
inputs:
  profit: 4000000
  half_year_paid: 250000
  withholding: 30000
steps:
  - sme_tax: max(min(profit, 3000000) - 300000, 0) * 0.15 + max(profit - 3000000, 0) * 0.20
  - ordinary_tax: profit * 0.20
  - balance: sme_tax - half_year_paid - withholding
expected:
  sme_tax: 605000
  ordinary_tax: 800000
  balance: 325000
```

**Half-year SME estimate: halve profit before applying bands.** Assume a continuously qualifying ordinary SME and estimated annual taxable profit THB 1,200,000 after the relevant adjustments, losses and exemptions. The PND.51 estimate-method base is THB 600,000. Applying the SME bands to that base gives THB 45,000 before credits. Half the annual SME tax would be THB 67,500, which overstates this half-year computation by THB 22,500. This example does not apply to the statutory actual-first-half-profit method.

```oa-check
name: Thailand PND51 half estimated profit before SME bands
inputs:
  annual_estimated_taxable_profit: 1200000
steps:
  - half_profit: annual_estimated_taxable_profit * 0.5
  - half_year_tax: max(min(half_profit, 3000000) - 300000, 0) * 0.15 + max(half_profit - 3000000, 0) * 0.20
  - annual_sme_tax: max(min(annual_estimated_taxable_profit, 3000000) - 300000, 0) * 0.15 + max(annual_estimated_taxable_profit - 3000000, 0) * 0.20
  - incorrect_half_annual_tax: annual_sme_tax * 0.5
  - overstatement: incorrect_half_annual_tax - half_year_tax
expected:
  half_profit: 600000
  half_year_tax: 45000
  annual_sme_tax: 135000
  incorrect_half_annual_tax: 67500
  overstatement: 22500
```

## Ask the client first

- Thai-incorporated entity, Thai branch or non-resident payee, and accounting-period dates?
- Period-end paid-up capital, sales/service revenue and the complete SME qualification history?
- Reconciled profit, foreign income, related parties, tax losses and incentives?
- Dividends received, shareholdings and holding dates?
- PND.51 estimates/payments and withholding certificates for this period?
- Treaty residence, income category, beneficial ownership and any profit remittance abroad?

## Sources

| Source and actual reading scope | URL | Read on |
|---|---|---|
| Revenue Code, corporate income tax (Read for §§65-70 bis, including accruals, expenses, dividend exclusions, losses, estimates, deadlines, certifications, withholding and interest exception) | https://www.rd.go.th/english/37764.html | 2026-11-16 |
| Revenue Code income-tax schedule (Read for company net-profit and non-resident gross-income categories) | https://www.rd.go.th/5938.html | 2026-11-16 |
| RD PND.51 instructions for accounting periods beginning on/after 1 January 2025 (Read for page 1 period scope, pages 3-4 method 1 versus method 2, tax-base item 1(1)(1)-(7), and item 2 tax calculation including current ordinary/SME bands; not the full 11-page special-regime instructions) | https://www.rd.go.th/fileadmin/tax_pdf/cit/2568/Ins51_290468.pdf | 2026-11-16 |
| Consolidated Royal Decree 530 (Read for §§6-8 and the displayed amendments by Decrees 583 and 603, including continuing capital/revenue conditions) | https://www.rd.go.th/28271.html | 2026-11-16 |
| Revenue Department filing-service index (Read for PND.50, PND.51, PND.54 and withholding portal routes; no authenticated submission) | https://www.rd.go.th/rdeservice/63813.html | 2026-11-16 |

Not yet confirmed: complete annual late-filing/payment and remission rules; current domestic-company dividend-withholding exemptions; treaty-specific rates and permanent-establishment relief. Legacy headline dividend 10%, non-resident interest/royalty 15% and domestic dividend 10% entries are not blanket instructions: classification, exemptions and treaty conditions must first be established. No bank or treaty special regime is computed here.
