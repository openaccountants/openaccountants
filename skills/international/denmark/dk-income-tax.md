---
name: dk-income-tax
description: Use this skill whenever asked about Danish income tax for self-employed individuals (selvstaendig erhvervsdrivende). Trigger on phrases like "Danish tax", "AM-bidrag", "bundskat", "topskat", "kommuneskat", "virksomhedsordningen", "kapitalafkastordningen", "personfradrag", "Arsopgorelse", "Oplysningsskema", "self-employed tax Denmark", or any question about filing or computing income tax for a Danish self-employed client. Covers AM-bidrag (8%), bundskat, topskat, kommuneskat, kirkeskat, virksomhedsordningen, kapitalafkastordningen, deductible expenses, filing deadlines, and penalties. ALWAYS read this skill before touching any Danish income tax work.
version: 2.0
jurisdiction: DK
tax_year: 2026
last_updated: 2026-09-24
authored_by: OpenAccountants team
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Denmark self-employed income tax for 2026

This guide covers the ordinary income-tax workflow for a personally owned Danish business. Figures are for tax year 2026. It includes AM-bidrag, state-tax screens, municipal and church tax inputs, personal and work allowances, ordinary expenses, assets, private-car records, the two business schemes, preliminary assessment and final reporting. It does not compute a company return, VAT, payroll, share income, foreign-credit/treaty results or a taxpayer-specific final settlement.

## Required inputs before calculating or filing

Obtain and date the following. Do not substitute a generic national rate for any of them.

1. **Tax status and age:** CPR/tax year, date of birth, Danish address and municipality, Folkekirken membership, arrival/departure dates, residence elsewhere, treaty position and the source/location of each income item. Obtain state-pension-age timing and whether the taxpayer is entitled to and receives the statutory additional child allowance. Danish residence or a consecutive six-month stay is the cited starting screen for full tax liability; income without residence can instead be limited liability. [SKAT tax liability](https://skat.dk/en-us/individuals/taxation-in-denmark/tax-liability)[SKAT B-income](https://skat.dk/en-us/individuals/b-income)[SKAT 2026 work allowances](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag)
2. **Activity classification:** contracts, who controls the work, who bears risk, client count, invoices and actual working arrangements. Invoicing alone does not make an activity a business, and separate activities may have different classifications. [SKAT classification](https://skat.dk/erhverv/egen-virksomhed/afklar-virksomhedens-skatteforhold)
3. **Business records:** opening/closing position, income, invoices/credit notes, purchases, assets, debt and interest, payroll, VAT records, private withdrawals, business/private usage evidence, prior losses, and the accounting period.
4. **Other tax inputs:** wages/A-income, B-income, capital income and interest, pensions, property and share income, deductions, withholding, B-tax paid, the personal allowance shown in the current assessment and the current preliminary assessment. These alter the result even when the business accounts are correct.
5. **Scheme facts:** whether the taxpayer has used the business-tax or return-on-capital scheme, separate business finances, retained profit, withdrawals and scheme calculations. Do not elect a scheme from a rate alone.

## Ask the client first

- Is the activity actually self-employment: who controls the work, bears the costs and risk, and supplies the client-facing contract?
- Is the person fully or only limitedly liable in Denmark, and are there foreign residence, income or treaty facts?
- What municipality, Folkekirken membership, age, pension-age timing, child-allowance status and current tax-card allowance apply?
- What income belongs in personal, capital and share categories, and what AM-liable amount is supported by reconciled accounts?
- Has the taxpayer used either business-tax scheme, retained profit, withdrawals, capital-return calculation or spouse allocation?
- For each asset/car/expense, what invoice, business-use record, VAT treatment and payment evidence supports the claimed treatment?

## Rates, thresholds and deadlines

The table records published figures and the labelled inputs or outputs used in worked examples. Worked-example amounts are hypothetical arithmetic, not official taxpayer amounts; their calculation and case binding are in the packet evidence.

| Figure | Value | Source |
| --- | --- | --- |
| entertainment rate | 25% | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| private phone | DKK 3,500 | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| am rate | 8% | [official source](https://skat.dk/en-us/individuals/b-income) |
| bottom rate | 12.01% | [official source](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| middle rate | 7.5% | [official source](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| middle threshold | DKK 641,200 | [official source](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| capital threshold | DKK 55,000 | [official source](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| top threshold | DKK 777,900 | [official source](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| additional rate | 5% | [official source](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| additional threshold | DKK 2,592,700 | [official source](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| employment rate | 12.75% | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| employment cap | DKK 63,300 | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| employment full | DKK 496,471 | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| job rate | 4.5% | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| job threshold | DKK 235,200 | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| job cap | DKK 3,100 | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| job full | DKK 304,089 | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| senior rate | 1.4% | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| senior cap | DKK 6,100 | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| single rate | 11.5% | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| single cap | DKK 50,600 | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| single full | DKK 440,000 | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| vso rate | 22% | [official source](https://skat.dk/en-us/businesses/own-business/tax-on-own-business) |
| field 184 | 184 | [official source](https://skat.dk/en-us/businesses/own-business/tax-on-own-business) |
| box 147 | 147 | [official source](https://skat.dk/en-us/businesses/own-business/tax-on-own-business) |
| box 141 | 141 | [official source](https://skat.dk/en-us/businesses/own-business/tax-on-own-business) |
| field 221 | 221 | [official source](https://skat.dk/en-us/individuals/b-income) |
| field 435 | 435 | [official source](https://skat.dk/en-us/businesses/own-business/tax-on-own-business) |
| filing open | 23 | [official source](https://skat.dk/en-us/businesses/own-business/tax-on-own-business) |
| filing deadline | 1 July 2026 | [official source](https://skat.dk/en-us/businesses/own-business/tax-on-own-business) |
| late penalty | DKK 400 | [official source](https://skat.dk/en-us/businesses/own-business/tax-on-own-business) |
| personal allowance | DKK 54,100 | [official source](https://skat.dk/en-us/individuals/tax-card) |
| personal allowance 2025 | DKK 51,600 | [official source](https://skat.dk/en-us/individuals/tax-card) |
| immediate assets | DKK 36,000 | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| asset life | 3 | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| pool rate | 25% | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| green uplift | 108% | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| green window start | 1 January 2025 | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| green window end | 31 December 2026 | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| car low rate | DKK 3.94 | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| car break | 20,000 km | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| car high rate | DKK 2.28 | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| building date | 1 January 2023 | [official source](https://info.skat.dk/data.aspx?oid=2083987) |
| building new rate | 3% | [official source](https://info.skat.dk/data.aspx?oid=2083987) |
| building old rate | 4% | [official source](https://info.skat.dk/data.aspx?oid=2083987) |
| goodwill rate | one-seventh | [official source](https://info.skat.dk/data.aspx?chk=220619&oid=2083994) |
| btax months | ten | [official source](https://skat.dk/en-us/individuals/b-income) |
| btax excluded months | June and December | [official source](https://skat.dk/en-us/individuals/b-income) |
| worked example — ordinary profit | 400000 | [official source](https://skat.dk/en-us/individuals/b-income) |
| worked example — ordinary am | 32000 | [official source](https://skat.dk/en-us/individuals/b-income) |
| worked example — ordinary post am | 368000 | [official source](https://skat.dk/en-us/individuals/b-income) |
| worked example — ordinary employment | 51000 | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| worked example — ordinary job precap | 7416 | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| worked example — boundary profit | 697000 | [official source](https://skat.dk/en-us/individuals/b-income) |
| worked example — boundary am | 55760 | [official source](https://skat.dk/en-us/individuals/b-income) |
| worked example — boundary post am | 641240 | [official source](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| worked example — boundary excess | 40 | [official source](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| worked example — boundary middle component | 3 | [official source](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| worked example — under18 profit | 100000 | [official source](https://skat.dk/en-us/individuals/b-income) |
| worked example — under18 am | 0 | [official source](https://skat.dk/en-us/individuals/b-income) |
| worked example — allowance base | 440000 | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| worked example — allowance employment | 56100 | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| worked example — allowance job precap | 9216 | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| worked example — allowance senior precap | 6160 | [official source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| worked example — asset minor case | 25000 | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| worked example — asset major case | 100000 | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| worked example — asset major deduction | 25000 | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| worked example — asset major balance | 75000 | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| worked example — vehicle km | 9000 | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| worked example — vehicle deduction | 35460 | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| worked example — forecast revised | 600000 | [official source](https://skat.dk/en-us/businesses/own-business/tax-on-own-business) |
| worked example — obsolete asset amount | 15400 | [official source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |

| Worked-example amount in body | DKK 400,000 | [AM-bidrag source](https://skat.dk/en-us/individuals/b-income) |
| Worked-example amount in body | DKK 32,000 | [AM-bidrag source](https://skat.dk/en-us/individuals/b-income) |
| Worked-example amount in body | DKK 368,000 | [AM-bidrag source](https://skat.dk/en-us/individuals/b-income) |
| Worked-example amount in body | DKK 51,000 | [allowance source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| Worked-example amount in body | DKK 7,416 | [allowance source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| Worked-example amount in body | DKK 697,000 | [state-tax source](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| Worked-example amount in body | DKK 55,760 | [AM-bidrag source](https://skat.dk/en-us/individuals/b-income) |
| Worked-example amount in body | DKK 641,240 | [state-tax source](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| Worked-example amount in body | DKK 40 | [state-tax source](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| Worked-example amount in body | DKK 3 | [state-tax source](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| Worked-example amount in body | DKK 100,000 | [business-expense source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| Worked-example amount in body | 0 | [AM-bidrag source](https://skat.dk/en-us/individuals/b-income) |
| Worked-example amount in body | DKK 56,100 | [allowance source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| Worked-example amount in body | DKK 9,216 | [allowance source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| Worked-example amount in body | DKK 6,160 | [allowance source](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) |
| Worked-example amount in body | DKK 25,000 | [business-expense source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| Worked-example amount in body | DKK 75,000 | [business-expense source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| Worked-example amount in body | 9,000 km | [private-car source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| Worked-example amount in body | DKK 35,460 | [private-car source](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| Worked-example amount in body | DKK 600,000 | [own-business source](https://skat.dk/en-us/businesses/own-business/tax-on-own-business) |

## The method, step by step

1. Classify the person and each activity from the actual contracts, control and risk; screen full or limited Danish liability before calculating.
2. Reconcile accounts and identify supported business income, allowable costs, assets, private use, VAT handling and other income categories.
3. Determine the AM-bidrag base and age rule, then screen the stated state-tax layers using the required personal and capital-income inputs.
4. Calculate the personal and work-allowance inputs on their own bases, then obtain the municipality/church and tax-card facts needed for the individual calculation.
5. Decide whether business-tax or return-on-capital scheme records and elections apply; use a specialist method when they do.
6. Update the preliminary assessment during the year, reconcile B-tax/withholding, and file the completed business return with the final evidence.


### 1. Classify the taxpayer and activity

Decide whether each activity is employment, fee income, commercial self-employment or non-commercial activity from the real facts. This affects whether expenses and losses are deductible and whether AM-bidrag applies. If classification is unclear, pause the computation and obtain a SKAT clarification or Danish professional review. [SKAT classification](https://skat.dk/erhverv/egen-virksomhed/afklar-virksomhedens-skatteforhold)

For an individual, then distinguish full from limited Danish tax liability. Full liability generally covers worldwide earned and capital income; limited liability can apply to specified Danish income. A nonresident may have special personal-allowance/cross-border-worker options, so do not assume the full-liability result. [SKAT tax liability](https://skat.dk/en-us/individuals/taxation-in-denmark/tax-liability)

### 2. Prepare tax accounts and the business result

Start with reconciled income and expenditure for the completed period. VAT is not income-tax profit: keep VAT-return data and income-tax accounts separately, then reconcile them to the ledger. Only deduct expenditure incurred to secure, acquire and maintain the ongoing business. Retain invoices, payment evidence and the business reason. Private cost is not deductible; split a mixed item to the documented business share. [SKAT business-expense deductions](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses)

The following are supported examples, not an exhaustive deduction list:

| Item | Treatment in this method |
| --- | --- |
| Goods for resale, tools/equipment, professional fees, business premises, insurance and business telephone/internet | Consider only to the documented business extent in the tax accounts. [SKAT business-expense deductions](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| Advertising | The cited guidance permits full deduction in the accounts, subject to records and business purpose. [SKAT business-expense deductions](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| Entertainment of business contacts | The cited guidance permits 25%; retain recipient/purpose evidence. [SKAT business-expense deductions](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| Home office | Do not deduct room costs merely because the room is used for work. The room must not be arranged so that private use is possible; normally usable domestic offices fail this test. Furniture can be apportioned by business use. [SKAT business-expense deductions](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |
| Business phone/internet available privately | Enter the cost but assess SKAT’s private-use value rules. Its cited 2026 value is DKK 3,500; where conditions apply, add it to result and use field 462. Do not duplicate phone and internet value. [SKAT business-expense deductions](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses) |

Adjust book profit for every non-deductible/private component and every income-tax-only adjustment before using it as the taxable business result. Do not claim an employment expense again where it already reduced the business result.

### 3. Keep income streams separate

Put business/personal income, net capital income and share income into their separate statutory categories before applying rates. This draft only provides the 2026 state-tax treatment needed for the self-employed income workflow. It does not calculate a share-income result, property result, capital loss, foreign-tax credit or investment-fund classification.

### 4. Apply AM-bidrag and the 2026 state-tax layers

AM-bidrag is 8% for a person who is liable to it. From income year 2026, B-income, business profit and salary do **not** bear AM-bidrag until the calendar year in which the person turns 18. Record the birth year before calculating the contribution. SKAT says regular B-income in the preliminary assessment is included in B-tax instalments; use the actual preliminary assessment rather than inventing an instalment schedule. [SKAT B-income](https://skat.dk/en-us/individuals/b-income)

For 2026, use the following as a state-tax **screen** after validating the income basis. The middle/top/additional thresholds below are stated by SKAT as after AM-bidrag. The bottom-bracket calculation also depends on personal allowance and positive net capital income; this draft does not derive a universal taxable base.

| Layer | Published 2026 treatment |
| --- | --- |
| Bottom-bracket tax (bundskat) | 12.01% of personal income plus positive net capital income above the personal allowance. [SKAT 2026 state-tax rates](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| Middle-bracket tax | 7.5% of personal income over DKK 641,200 after AM-bidrag. The former topskat is renamed middle-bracket tax in 2026. Positive net capital income over DKK 55,000 has separate stated treatment. [SKAT 2026 state-tax rates](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| Top-bracket tax | 7.5% of personal income over DKK 777,900 after AM-bidrag. [SKAT 2026 state-tax rates](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |
| Additional top-bracket tax | 5% of personal income over DKK 2,592,700 after AM-bidrag. [SKAT 2026 state-tax rates](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) |

Add the municipality’s income-tax rate and, only where applicable, church tax for Folkekirken members. The rate is not national: obtain the taxpayer’s municipality and current rate. [SKAT 2026 state-tax rates](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat)

### 5. Calculate automatic work allowances on their own base

SKAT states that salary subject to AM-bidrag and business profit receive the ordinary employment and job allowances automatically. For 2026, calculate the ordinary employment allowance as **the lesser of 12.75% of the applicable allowance base and DKK 63,300**; the published full-allowance income is DKK 496,471. Calculate job allowance as **the lesser of 4.5% of applicable income above DKK 235,200 and DKK 3,100**; the published full-allowance income is DKK 304,089. Obtain the current assessment where age or a special income category makes the allowance base uncertain; an AM-bidrag exemption is not by itself proof that every allowance is absent. [SKAT 2026 work allowances](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag)[SKAT 2026 work allowances](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag)

For ordinary eligible cases, also test the two existing 2026 extra allowances:

| Allowance | 2026 ordinary test and calculation | Input/evidence |
| --- | --- | --- |
| Senior employment allowance | In either of the two income years before state-pension age, calculate the lesser of **1.4%** of the same allowance base and **DKK 6,100**. It ends in the income year pension age is reached. | Date of birth/state-pension-age timing and ordinary allowance eligibility. |
| Qualifying single-parent employment allowance | Where the person is entitled to **and receives** the additional child allowance under the Child Allowance Act, calculate the lesser of **11.5%** of the same allowance base and **DKK 50,600**. It is reached at DKK 440,000. | Entitlement and receipt status, not marital status or a bank narration alone. |

These allowances reduce taxable income; they are not cash payments, do not reduce the AM-bidrag calculation and do not replace the statutory personal-income threshold screens. The SKAT page separately mentions an **unpassed** proposal to expand the senior regime from two to five years and increase later rates. That proposal is not used here; the enacted two-year 2026 rule above is. [SKAT 2026 work allowances](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag)[SKAT 2026 work allowances](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag)

### 6. Choose a tax scheme only after its records are complete

Under the business-tax scheme, business and personal finances must be separate. SKAT describes two consequences: business interest may be treated as personal, rather than capital, income; and profit can be retained against provisional 22% tax, with later withdrawal taxed as personal income and the earlier tax credited. The preliminary-assessment indication is field 184, but the final choice is made on the return in box 147. [SKAT tax on own business](https://skat.dk/en-us/businesses/own-business/tax-on-own-business)

The return-on-capital scheme is presented by SKAT as a simpler alternative. Its calculated return is capital income and cannot exceed the greater of business profit or total negative capital income excluding the calculated return. The preliminary indication is field 184; the final return selection is box 141 under business information. [SKAT tax on own business](https://skat.dk/en-us/businesses/own-business/tax-on-own-business)

These are elections with record-keeping and withdrawal consequences. This draft does not calculate either scheme, recommend one, or treat the provisional 22% as a final owner tax. Refer a first election, change, large retained profit, mixed finances or interest-allocation case.

### 7. Pay during the year and file the completed period

Enter forecast business profit in preliminary-assessment field 221 or forecast loss in field 435, calculate, inspect the new tax-card page, and accept the change. Where it creates B-tax, pay the stated instalments; where no B-tax appears, SKAT says tax may be withheld from other income. Update the forecast whenever profit/loss changes. [SKAT tax on own business](https://skat.dk/en-us/businesses/own-business/tax-on-own-business)

For a personally owned business, report the completed year’s final profit/loss and required income/deduction information in E-tax for Individuals (TastSelv Borger). The current SKAT page says access starts 23 March and **1 July 2026 is the deadline for the 2025 return**. It also states DKK 400 per day for late filing and permits an application for relief in special circumstances. Do not reuse this as the 2026-return deadline; retrieve the live deadline for that later return. [SKAT tax on own business](https://skat.dk/en-us/businesses/own-business/tax-on-own-business)

## Operational working method

### Evidence first, then classify

Build one working table from the bank export, invoices, receipts and the prior-year assessment. A bank narration is a lead, not evidence of its tax treatment. For every line, record date, counterparty, amount including/excluding VAT, supporting document, business purpose, tax category, business-use proportion, VAT treatment, and whether it is a cash movement or affects taxable profit.

| Transaction type | Operational treatment |
| --- | --- |
| Client invoice/payment or platform payout | Match the payment to the invoice, contract/deliverable and VAT status. Record the income net of recoverable VAT for income-tax accounts; investigate short fees, refunds and multi-invoice payouts rather than treating the bank net as revenue automatically. |
| Transfer between taxpayer’s own accounts | Exclude from income and expense. Preserve both bank lines as reconciliation evidence. |
| Loan proceeds or loan-principal repayment | Exclude from operating profit. Identify the agreement and separately assess interest. |
| B-tax payment or tax refund | Do not treat as business expense or revenue. Reconcile the payment/refund to TastSelv and final assessment. |
| Purchase or recurring expense | Obtain receipt and business reason; apply the ordinary-expense test, then private-use, VAT and asset checks. |
| Asset, equipment, vehicle or intangible right | Do not expense from merchant text alone. Test the 2026 minor-asset threshold, useful-life, VAT status, mixed use and depreciation category. |
| Capital, rental, employment or share transaction | Keep out of the sole-trader profit calculation until it is classified under its own tax rules. |

### Personal allowance and calculation sequence

For a fully liable taxpayer, the general 2026 personal allowance is **DKK 54,100**; DKK 51,600 is the 2025 amount. Check TastSelv and liability status before using it: limited liability, a part-year situation and a cross-border-worker election can differ. The allowance reduces the bottom-bracket and local-tax computation; it is not a deduction from AM-bidrag or a licence to ignore other income. [SKAT tax liability](https://skat.dk/en-us/individuals/taxation-in-denmark/tax-liability)[SKAT 2026 state-tax rates](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat)[SKAT 2026 state-tax rates](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat)[SKAT tax card](https://skat.dk/en-us/individuals/tax-card)

Use this sequence for an ordinary no-scheme working paper:

1. Reconcile business income and allowed business costs; document every adjustment from book profit to taxable business result.
2. Identify the AM-bidrag base and birth-year gate. Calculate 8% only where the 2026 age rule makes the taxpayer liable. Keep the calculation separate from state and local income tax. [SKAT B-income](https://skat.dk/en-us/individuals/b-income)
3. Combine the taxpayer’s required personal-income and positive-net-capital-income facts before applying bottom-bracket tax and personal allowance. Do not treat share income as personal income merely because it appears in the same bank account. [SKAT 2026 state-tax rates](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat)
4. Screen personal income after AM-bidrag against the three 2026 thresholds. Apply each layer only to its stated excess. [SKAT 2026 state-tax rates](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat)[SKAT 2026 state-tax rates](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat)
5. Calculate the ordinary employment and job allowances and, where their facts are present, the senior and qualifying-single-parent allowances. Carry them to the taxable-income stage used for local/church-tax computation; do not subtract them from AM-bidrag or use them to change the personal-income threshold screen. Compare the current assessment/TastSelv result. [SKAT 2026 work allowances](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag)[SKAT 2026 work allowances](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag)
6. Apply the current municipality rate to the resulting local taxable-income base and church tax only after Folkekirken membership is confirmed. [SKAT 2026 state-tax rates](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat)
7. Credit actual withholding and B-tax paid only after matching payment evidence to the preliminary/final assessment. The difference is a provisional settlement, not proof of final tax.

### Ordinary deductions and exclusions

The business-expense test is applied item by item. It supports ordinary operating costs, not a merchant-name shortcut. Require a document, purpose and business-use basis for every line. [SKAT business-expense deductions](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses)

| Category | Handle directly when the evidence is clear | Stop and obtain more facts |
| --- | --- | --- |
| Goods for resale; rent of dedicated business premises; business insurance; accountant/lawyer fees; office supplies; software; payment-provider/bank fees | Include to the documented business extent. | Mixed personal/business use, personal benefit or unclear connection to ongoing operations. |
| Advertising | Include documented advertising/marketing cost. | Gifts, hospitality or sponsorship with a private/representation element. |
| Entertainment/representation | Include 25% of documented qualifying expenditure and add back 75%. | Personal meal, unclear guests/purpose, or gift-specific rules. |
| Telephone/internet | Record the actual cost, then apply the cited 2026 private-use value rule when its conditions apply. | Shared plans, household bundle or uncertain network/private-use facts. |
| Home workroom | Claim room cost only where it is not arranged so private use is possible; otherwise do not deduct the room cost. | Any arguable dual-use room or a claimed standard amount not supported by current guidance. |
| Private living, penalties/fines, income tax and private drawings | Exclude from business costs. | A payment that may include both a penalty and an otherwise deductible charge. |

### Assets, depreciation and private vehicles

For qualifying plant and equipment acquired in 2026, a same-year minor asset up to **DKK 36,000** may be deducted immediately. Use the price excluding VAT for a VAT-registered business and including VAT where it is not registered. Related components intended for use together are tested as one item. Qualifying assets with a maximum three-year life may also be immediately deducted. [SKAT business-expense deductions](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses)

For qualifying major plant and equipment above the threshold, maintain a depreciation schedule. SKAT’s current guidance permits up to **25%** annual diminishing-balance depreciation; it can be lower. Add qualifying assets above the threshold to the pool, calculate the year’s claimed percentage, carry the remaining balance forward, and deduct the remaining balance if it later falls below the minor-asset threshold. [SKAT business-expense deductions](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses)

Use a separate schedule for mixed plant/equipment. Record acquisition price, asset identity, total and business use, and support the split. The mixed-use asset is not pooled with wholly business assets; only business-use depreciation is deducted. Do not use the 108% green-asset uplift unless the asset is brand-new qualifying electric/battery equipment, acquired in the stated 1 January 2025–31 December 2026 window, without private use, and outside SKAT’s exclusions. [SKAT business-expense deductions](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses)

For a private car used in the business, use **one** current supported method and a mileage log: actual business share of operating cost/depreciation, or SKAT’s 2026 own-car rates of DKK 3.94/km through 20,000 km and DKK 2.28/km above it. The original Guide’s 2025 rates are obsolete. A self-employed person cannot simply pay themself tax-free mileage allowance; the result is an income-tax deduction supported by actual expense or the rate method. [SKAT business-expense deductions](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses)

Buildings/installations and purchased goodwill are not ordinary “computer purchase” cases. For qualifying buildings/installations acquired from 1 January 2023, the legal guide’s ordinary maximum is 3% annually; pre-2023 assets retain a distinct 4% rule. Qualifying purchased goodwill and listed intangible rights can be depreciated by up to 1/7 yearly, while internally generated goodwill is not assumed eligible. Use the relevant acquisition/asset evidence and separate schedules. [SKAT legal guide: building depreciation](https://info.skat.dk/data.aspx?oid=2083987) [SKAT legal guide: goodwill and intangibles](https://info.skat.dk/data.aspx?chk=220619&oid=2083994)

### B-tax and return operations

When business income is forecast, enter expected profit in field 221 or expected loss in field 435 in the preliminary income assessment. Recalculate and inspect whether TastSelv has produced B-tax. A B-tax payer normally pays ten instalments, with no ordinary instalment in June or December. Do not copy historic payment dates, interest thresholds or a bank-statement amount: use the current TastSelv decision and payment identifier. [SKAT tax on own business](https://skat.dk/en-us/businesses/own-business/tax-on-own-business) [SKAT B-income](https://skat.dk/en-us/individuals/b-income)

At year end, prepare tax accounts, reconcile them to evidence and file the final business result in TastSelv Borger. The current SKAT page gives 23 March opening and **1 July 2026** as the deadline for the **2025** self-employed return; it states DKK 400 per late day and a special-circumstances relief path. Obtain the later live deadline before using the same workflow for 2026 income. [SKAT tax on own business](https://skat.dk/en-us/businesses/own-business/tax-on-own-business)

## When to refuse or refer

- Obtain missing evidence before continuing ordinary expense, representation, asset, private-car, B-tax reconciliation or domestic classification work.
- Use a separate company method for an ApS, A/S or other company result.
- Refer dual residence, foreign income/property, treaty credit, transfer pricing, uncertain limited liability or an unresolved activity classification.
- Refer a first or changed business-tax/return-on-capital election, a VSO exit, material retained-profit withdrawal, spouse allocation or tax-ceiling computation.
- Refer a business sale, purchased-goodwill valuation, building classification or asset with uncertain ownership/private use.


## Worked cases — mechanical checks, not final tax advice

Each case states its assumptions. A calculation of a rate component is not a final assessment: municipality, church membership, other income, personal allowance and all applicable allowance facts still control the individual settlement.

### Ordinary case: DKK 400,000 profit

* AM-bidrag: DKK 400,000 × 8% = **DKK 32,000**.
* Simplified amount after AM-bidrag: DKK 400,000 − DKK 32,000 = **DKK 368,000**. It is below the DKK 641,200 middle-bracket threshold, so this simplified case has no middle/top/additional-top tax from business profit alone.
* Ordinary employment allowance: DKK 400,000 × 12.75% = **DKK 51,000**, below its DKK 63,300 cap.
* Job allowance: (DKK 400,000 − DKK 235,200) × 4.5% = DKK 7,416, so it is capped at **DKK 3,100**.
* For the local/church taxable-income stage, record the general 2026 personal allowance of **DKK 54,100** and the DKK 54,100 of ordinary work allowances above as separate deduction inputs. Do not subtract either from the AM-bidrag base or from the DKK 641,200 threshold screen.

The result is not a final tax bill: the authority's tax-card/return treatment of the personal and work-allowance inputs, positive net capital income, municipal/church rates and other deductions remains to be applied to the taxpayer's facts.

### Boundary case: middle-bracket threshold

Assume a DKK 697,000 profit where all of it is a simple AM-bidrag base.

* AM-bidrag: DKK 697,000 × 8% = **DKK 55,760**.
* Simplified post-AM amount: DKK 697,000 − DKK 55,760 = **DKK 641,240**.
* Middle-bracket excess: DKK 641,240 − DKK 641,200 = **DKK 40**; at 7.5%, the mechanical middle-bracket component is **DKK 3**.
* Ordinary employment allowance reaches its published cap of **DKK 63,300**; job allowance is likewise capped at **DKK 3,100**.

This boundary test does not establish the exact statutory basis for a real taxpayer with capital income, pension items, scheme allocations or non-AM income.

### Age-gate case: person who does not turn 18 in 2026

Assume a sole trader who turns 18 in 2027 and has DKK 100,000 of otherwise ordinary 2026 business profit.

* AM-bidrag is **0** for 2026 because the person does not turn 18 during that income year.
* Record the profit, date of birth and the current assessment. Do not infer the ordinary, senior or single-parent employment-allowance result solely from the missing AM-bidrag; test their separate eligibility/base and use the current assessment where required.
* The general 2026 personal allowance is still DKK 54,100 as a starting amount, subject to the taxpayer's liability facts. [SKAT B-income](https://skat.dk/en-us/individuals/b-income)[SKAT tax card](https://skat.dk/en-us/individuals/tax-card)

### Allowance boundary case: senior and qualifying single parent

Assume an adult sole trader has DKK 440,000 of applicable allowance-base income, is in one of the two income years before state-pension age, and is entitled to and receives the statutory additional child allowance.

* Ordinary employment allowance: DKK 440,000 × 12.75% = DKK 56,100, below the DKK 63,300 cap.
* Job allowance: (DKK 440,000 − DKK 235,200) × 4.5% = DKK 9,216, therefore **DKK 3,100** after its cap.
* Senior allowance: DKK 440,000 × 1.4% = DKK 6,160, therefore **DKK 6,100** after its cap.
* Qualifying-single-parent allowance: DKK 440,000 × 11.5% = **DKK 50,600**.

Carry the four allowance amounts to the taxable-income stage. This case does not establish the pension-age or child-benefit facts; it shows the stated calculation only. [SKAT 2026 work allowances](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag)[SKAT 2026 work allowances](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag)

### Exclusion case: invoice issued under an employment arrangement

An individual issues an invoice but works under a client’s instructions, at the client’s expense and risk, as part of that client’s contractual organisation. SKAT says actual conditions control and an employee is not self-employed simply because they issue an invoice. Stop the sole-trader method, retain the contract/work facts and assess employee or fee-earner treatment. Do not claim business deductions, losses or a business-tax scheme until classification is resolved. [SKAT classification](https://skat.dk/erhverv/egen-virksomhed/afklar-virksomhedens-skatteforhold)

### Asset case: current minor-asset threshold

A VAT-registered business buys a stand-alone laptop for DKK 25,000 excluding VAT in 2026, uses it wholly in the business, and holds evidence that it is not part of a larger combined asset.

* DKK 25,000 is below the 2026 DKK 36,000 minor-asset threshold.
* Expected income-tax treatment: **DKK 25,000 immediate deduction**, subject to the ordinary business-expense and VAT tests. It is not a 25% pool case merely because it cost more than the obsolete DKK 15,400 threshold.
* If the laptop and printer are intended to be used together, test their combined price instead. If the business is not VAT registered, test the VAT-inclusive acquisition cost. [SKAT business-expense deductions](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses)

### Major-asset case: diminishing-balance pool

A VAT-registered business buys qualifying wholly business equipment for DKK 100,000 excluding VAT in 2026, with no green-asset uplift claim.

* It exceeds DKK 36,000 and enters the qualifying asset pool.
* Maximum first-year deduction: DKK 100,000 × 25% = **DKK 25,000**.
* Remaining pool balance: DKK 100,000 − DKK 25,000 = **DKK 75,000**.

The 25% is a maximum, not a compulsory rate. A mixed-use asset uses its own business-use schedule instead of this wholly-business pool calculation. [SKAT business-expense deductions](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses)

### Vehicle case: rate method

A sole trader has a contemporaneous mileage log showing 9,000 business kilometres in their private car during 2026 and chooses the rate method.

* Expected deduction: 9,000 km × DKK 3.94 = **DKK 35,460**.
* The kilometres are below the 20,000 km rate break. Keep the log, route/purpose and annual total.
* Do not add petrol, insurance, depreciation or financing costs a second time under the rate method. [SKAT business-expense deductions](https://skat.dk/en-us/businesses/own-business/deduction-for-business-expenses)

### Filing case: forecast differs from final profit

In April 2026, a taxpayer has forecast DKK 400,000 profit in field 221, but revised accounts show expected DKK 600,000. The expected outcome is to update the preliminary assessment and use the recalculated TastSelv B-tax/withholding result. The taxpayer does not invent a new instalment amount from a generic percentage. For the completed 2025 return, final accounts and the business result must be filed by the cited 1 July 2026 deadline unless SKAT has granted applicable relief. [SKAT tax on own business](https://skat.dk/en-us/businesses/own-business/tax-on-own-business)[SKAT tax on own business](https://skat.dk/en-us/businesses/own-business/tax-on-own-business)


## Completion checklist and explicit omissions

Before filing, reconcile tax accounts to the ledger/VAT data; check every receipt and private-use adjustment; confirm municipality/church status and current preliminary assessment; classify other income; select and document any scheme; compare forecast B-tax with paid instalments; review completed TastSelv fields; save the receipt and final assessment.

This is **not complete source coverage for a final Danish tax computation**. The claim ledger provides current ordinary handling for personal allowance screening, automatic work allowances, business deductions, depreciation, private-car records, B-tax and filing. It explicitly excludes the taxpayer's local/church rates, pension and other personal deductions, property and share income, investment funds, losses, foreign credits/treaties, detailed spouse-transfer/allocation computations, detailed scheme computations, payment interest and every later filing deadline. Those require current primary sources and taxpayer facts. Refer cross-border residence, limited liability, uncertainty over classification, a first/changed business-tax or return-on-capital scheme election, or a spouse-transfer/tax-ceiling computation that cannot be resolved with the specific source and facts.

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
