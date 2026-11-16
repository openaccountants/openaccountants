---
name: ng-cgt
description: Compute Nigerian chargeable gains for 2026, including property, Nigerian shares, digital assets, gifts, connected transactions, personal exemptions and reinvestment. Route company gains into company income tax and individual gains into personal income tax. Retains and corrects the original 2025 property and share examples without treating old CGTA rules as current.
jurisdiction: NG
tax_year: 2026
last_updated: '2026-11-16'
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: '1.1'
type: computation
category: international
---

# Nigeria chargeable gains v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use for a disposal governed by the Nigeria Tax Act (NTA) from 1 January 2026. Gains are integrated into the person's income-tax computation. Use [ng-personal-income-tax](ng-personal-income-tax.md) for an individual and [ng-cit](ng-cit.md) for a company, rather than applying the former flat CGT rate. This file owns the gain and exemption tests, not those income-tax rate tables. A Nigerian resident's worldwide gains are within the charge; a non-resident requires the situs, indirect-transfer and treaty analysis. [NTA sections 6,12,26 to28,33 to55 and119 to121](https://nass.gov.ng/documents/download/11249).

The National Assembly text is the operative source used here. The conflicting older official NTA copies and transition limits are disclosed in ng-cit. Do not apply current exemptions retrospectively to a 2025 sale. Historical examples below retain their original facts and distinguish verified arithmetic from a final filing position.

| Threshold or exemption | Current rule, with boundary | Official source |
| --- | --- | --- |
| Nigerian company shares: small-disposal exemption | Aggregate proceeds must be LESS THAN NGN 150,000,000 AND gains must not exceed NGN 10,000,000 in any12 consecutive months. Exactly NGN 150,000,000 fails the proceeds limb; exactly NGN 10,000,000 passes the gain limb. | [NTA section 34(1)(a), proviso (i)](https://nass.gov.ng/documents/download/11249) |
| Nigerian shares: reinvestment | Reinvest disposal proceeds in shares of a Nigerian company in the same year of assessment. Partial reinvestment leaves the corresponding proportion of gain chargeable. This is not a deduction of the proceeds threshold from sale proceeds. Qualifying regulated securities lending is a separate exception. | [NTA section 34(1)(a), provisos (ii)/(iii)](https://nass.gov.ng/documents/download/11249) |
| Compensation | Section 50 compensation has a NGN 50,000,000 exemption, with only excess chargeable and loss-of-office deduction at payment. Separately, section 162(1)(k) exempts death gratuities or consolidated compensation for death or injuries; section 162(1)(l) subjects loss-of-office/employment compensation to Part VIII. Classify the actual award: do not cap every death/injury payment at NGN 50m. An unresolved overlap between these categories is held for legal classification before calculation. Use ng-payroll/ng-wht for withholding reconciliation. | [NTA sections 50 and 162(1)(k)/(l)](https://nass.gov.ng/documents/download/11249) |
| Private residence | Individual's sole/main residence relief, once in a lifetime; adjoining non-commercial land limited to1 acre. Apportion business or other non-qualifying use. | [NTA section 51](https://nass.gov.ng/documents/download/11249) |
| Personal chattels | Individual's tangible movable property: consideration in a period of assessment not above the HIGHER of NGN 5,000,000 and 3 times annual national minimum wage. A part-interest disposal tests the whole asset, including the retained interest's market value. Aggregate connected-person/acting-in-concert transactions as required; sets cannot be fragmented. Currency is excluded. | [NTA section 52](https://nass.gov.ng/documents/download/11249) |
| Private motor vehicles | Motor vehicles used SOLELY for private or non-profit purposes, limited to 2 per individual in a year of assessment. Mixed business/private use does not qualify automatically. | [NTA section 53](https://nass.gov.ng/documents/download/11249) |
| Lost/destroyed asset replacement | Section43's special compensation/insurance replacement relief requires its conditions and replacement within 3 years. It is not a general rollover for every voluntary business-asset sale. | [NTA section 43](https://nass.gov.ng/documents/download/11249) |

## Ask the client first

1. Taxpayer type, residence, relevant tax authority, disposal date, basis period and year of assessment; for a non-resident, actual Nigerian asset/situs and treaty facts.
2. Acquisition deed/date/cost, payment evidence, title history, inheritance or gift, connected parties, independent valuations and any earlier capital allowances.
3. Disposal contract, consideration including non-cash amounts, instalments, enforceability/conditions, costs and receipts, enhancements still reflected in the asset, compulsory acquisition or insurance replacement.
4. Every share sale in the rolling window and the same year, gains, reinvestment amounts/dates, securities-lending documents, other gains/losses and any previous exemption claims.
5. For personal exemptions, occupation/business-use history, land area, previous residence relief, vehicle count, related chattel disposals, trust/charity purpose or compensation settlement terms.

## The method, step by step

### Identify the chargeable disposal and tax period

Start with all forms of property: land/buildings, shares/options, debts, foreign currency, digital/virtual assets and incorporeal rights, including assets created by the disposer. Sale, exchange, transfer, surrender, forfeiture, compensation and certain capital sums can be disposals. A security or nominee transfer needs its specific exception; a document labelled a gift is not a commercial sale at an invented price. Use the date a right to consideration or binding duty arises, with section 38's conditional-contract/option rules. [NTA sections 33 to38](https://nass.gov.ng/documents/download/11249).

Apply sections 36/45 separately to acquisition and disposal. Section 45(3) limits acquisition cost to the actual consideration paid where that amount is below market value; a bargain purchase does not receive an automatic market-value cost step-up. Section 36(2) uses the last arm's-length consideration for a later disposal of a gifted asset, or the relevant market value if that consideration cannot be established. Section 36(1) separately addresses devolution on death; section 36(3) concerns nominees/trustees. Obtain the ownership chain and valuations. A gift is exempt under section 54 except devolution on death, whose separate rules apply. [NTA sections 36,45 and54](https://nass.gov.ng/documents/download/11249).

### Compute the gain, then the relief

For an ordinary full disposal without prior capital allowances: disposal consideration less acquisition consideration under section 39(b) and evidenced incidental disposal costs under section 40. The current text expressly adds enhancement and incidental acquisition expenditure in section 41 for a PART disposal; section 20 title costs concern business-income deductions. A broader enhancement, incidental-acquisition or title-defence deduction for an ordinary full non-business disposal is not established by these clauses and is held pending applicable authority. Do not import the old CGTA cost list, deduct an income expense twice, or deduct private consumption/unsupported estimates. For a business asset on which capital allowances were claimed, use the acquisition residue required by section 39, not full original cost a second time. No invented inflation indexation. [NTA sections 20,21,39 and40](https://nass.gov.ng/documents/download/11249).

For a part disposal allocate common cost by A/(A+B): A is disposal consideration and B is market value of the retained part. Trace asset-specific expenditure separately. Where consideration is payable by instalments extending beyond12 months, section 42 permits the corresponding instalment treatment, subject to its anti-avoidance and irrecoverability provisions. Combine transactions forming one bargain. Preserve insurance/lost-asset and compulsory-acquisition facts for sections 37 and43 instead of claiming generic rollover. [NTA sections 37,41 to45](https://nass.gov.ng/documents/download/11249).

Test the table's exemptions before transferring the taxable balance to the owning income-tax computation. Original-owner life-assurance rights, an assurance contract purchased for value, other insurance proceeds and public-character charitable/religious/educational trustees have distinct conditions. A trustee's trading gain is not automatically exempt; cessation of the qualifying trust can trigger deemed market-value disposal. Government-bond income relief is not proof that every disposal gain on every security is exempt. [NTA sections 48,49,55 and162](https://nass.gov.ng/documents/download/11249).

### Shares and losses

Compute total proceeds and actual gains across the statutory window; test both limbs, then reinvestment. If no exemption applies, the charge is on the gain, without subtracting NGN 150m from proceeds. For partial reinvestment, gain multiplied by unreinvested proceeds/total proceeds is chargeable. Do not count a purchase outside the same assessment year or shares of a non-Nigerian company as automatic qualifying reinvestment. [NTA section 34(1)(a), provisos (i) to (iii)](https://nass.gov.ng/documents/download/11249).

Carry losses through the integrated company/individual rules; digital/virtual-asset losses are confined to profits of that business. Maintain source, asset, year, amount and use. Do not carry an unverified old capital loss into 2026 as an ordinary unrestricted trading loss. For the historical CGTA regime, Finance Act 2023 section 3 permitted same-type asset losses with a maximum5-year carryforward; the old file's indefinite, general capital-loss claim is withdrawn. [NTA sections 27 and28](https://nass.gov.ng/documents/download/11249); [Finance Act 2023 section 3](https://lirs.gov.ng/assets/docs/Finance_Act_2023.pdf).

## Boundary and exception table

| Facts | Treatment or handoff |
| --- | --- |
| Mixed-use residence, acreage, more than one home or prior relief | Establish actual qualifying fraction and once-lifetime history; do not exempt the whole property by default. |
| Related person, gift, inheritance, nominee, security or debt | Obtain valuations and legal ownership chronology; apply the relevant section rather than a zero-cost default. |
| Portfolio just at either threshold | Aggregate first and apply strict proceeds/inclusive gain boundaries. A single exempt sale does not establish exemption for the whole window. |
| Mineral right, petroleum interest, treaty property company, trust, partnership or foreign indirect transfer | Refer for the specialised regime, beneficial owner, situs and treaty article; sections 46/47 can reach indirect Nigerian property interests. |
| Loss-of-job settlement | Separate salary/notice pay, pension/gratuity and compensation; no blanket exemption for a settlement described as gratuity. Reconcile withholding to actual annual liability. |
| Ordinary voluntary replacement business asset | No automatic12-month-before/after rollover instruction for 2026. The old claim and its former section 32 citation are held under Sources. |

## Worked cases

**Current boundary decision, Nigerian shares.** An individual has no other sales in the12-month window and gains NGN 10m. Proceeds NGN 149m pass both limbs; the gain is exempt. At proceeds exactly NGN 150m, the proceeds limb fails. If no reinvestment, NGN 10m goes into the individual's income-tax computation. If NGN 60m of the NGN 150m is reinvested in qualifying Nigerian shares in the same year of assessment, NGN 6m of gain remains chargeable. The personal tax payable depends on other income and deductions; this is not a flat-rate tax answer.

```oa-check
name: Nigerian share proceeds boundary and partial reinvestment
inputs:
  below_limit_proceeds: 149000000
  boundary_proceeds: 150000000
  gain: 10000000
  qualifying_reinvestment: 60000000
steps:
  - below_limit_chargeable: gain * 0
  - boundary_no_reinvestment: gain
  - boundary_partial_reinvestment: gain * (boundary_proceeds - qualifying_reinvestment) / boundary_proceeds
expected:
  below_limit_chargeable: 0
  boundary_no_reinvestment: 10000000
  boundary_partial_reinvestment: 6000000
```

**Original property case, Mr Adewale, historical15 June2025 disposal.** Lagos resident, commercial property at Ikeja bought2018 for NGN 120m, acquisition costs NGN 6m, capital enhancement in2021 NGN 25m, sale NGN 250m. Legal fee1.5% and agency5% are scenario costs, not statutory fees. Disposal costs NGN 16.25m, total allowable cost assumed NGN 167.25m, gain NGN 82.75m. At the historical assumed10% rate, arithmetic is NGN 8.275m. The original facts and arithmetic survive; source confirmation of the old property's full CGTA cost/relief provisions and any actual prior allowances is still required before treating that amount as a verified historical filing liability. It is not a 2026 tax computation.

```oa-check
name: Mr Adewale original 2025 property conditional arithmetic
inputs:
  sale: 250000000
  purchase: 120000000
  acquisition_costs: 6000000
  enhancement: 25000000
  historical_rate_assumption: 0.10
steps:
  - legal_cost: sale * 0.015
  - agency_cost: sale * 0.05
  - gain: sale - purchase - acquisition_costs - enhancement - legal_cost - agency_cost
  - conditional_historical_tax: gain * historical_rate_assumption
expected:
  legal_cost: 3750000
  agency_cost: 12500000
  gain: 82750000
  conditional_historical_tax: 8275000
```

**Original shares case, Mrs Okonkwo, historical2025.** March CompanyA proceeds NGN 60m/cost25m; August CompanyB85m/40m; November CompanyC40m/30m. Total proceeds185m, cost95m, gains90m, no reinvestment. Finance Act 2021's old threshold exempted proceeds LESS THAN NGN 100m; it was not an allowance to subtract from 185m. At the section's10% rate the charge is NGN 9m, not the old NGN 4,135,135 result. Reinvesting only NGN 85m would not exempt the full gain: chargeable gain is90m×100m/185m, with tax approximately NGN 4,864,864.86. Full qualifying proceeds reinvestment, not merely the excess over the threshold, is the relevant branch. [Finance Act 2021 section 2](https://lirs.gov.ng/assets/docs/Finance-Act-2021-Gazetted.pdf).

```oa-check
name: Mrs Okonkwo historical shares threshold is not a deduction
inputs:
  sale_a: 60000000
  sale_b: 85000000
  sale_c: 40000000
  cost_a: 25000000
  cost_b: 40000000
  cost_c: 30000000
steps:
  - proceeds: sale_a + sale_b + sale_c
  - gain: proceeds - cost_a - cost_b - cost_c
  - tax_no_reinvestment: gain * 0.10
  - tax_reinvest_85m: gain * (proceeds - 85000000) / proceeds * 0.10
expected:
  proceeds: 185000000
  gain: 90000000
  tax_no_reinvestment: 9000000
  tax_reinvest_85m: 4864864.86
```

## When to refuse or refer

Do not issue a final gain where acquisition cost, prior allowances, value, ownership, period, aggregated sales or exemption history is missing. State the missing document, not a made-up cost or exemption. Refer mining/petroleum, complex trust/partnership interests, indirect transfers, treaty conflicts and disputes. Preserve the original advice to obtain valuation evidence and to review a proposed relief before disposing of or reinvesting assets. Never submit a return from this reference.

## Filing and payment

Transfer the gain schedule to the annual individual/company return and relevant authority under [NTAA sections 3,11,13 and49](https://nass.gov.ng/documents/download/11250); use ng-return-assembly for the filing package. Withholding on a compensation payment is a separate obligation. A 2026 gain and a2026 year of assessment are not interchangeable: section 26(3) uses the preceding-year gains basis. Resolve the return's exact period using the transition evidence rather than automatically relabelling a2025 disposal as2026 income.

For the historical CGTA, Finance Act 2020 section 2 inserted self-assessment and payment by 30 June and31 December for the respective disposal periods; the former annual-only instructions missed this. Do not carry those repealed-act dates into a current integrated return without confirming a surviving requirement. [Finance Act 2020 section 2](https://www.iirs.im.gov.ng/document/docs/FINANCE_ACT_2020.pdf). Keep deeds, valuations, contracts, reinvestment evidence, receipts and calculations. [NTAA section 31](https://nass.gov.ng/documents/download/11250) requires records for6 years after the relevant assessment year; keeping an asset's acquisition/relief chain through ownership and the subsequent enquiry period is prudent record policy, not an extra statutory6-year rule here.

## Sources

| Source and actual read scope | URL | Read on |
| --- | --- | --- |
| National Assembly NTA: sections 6,12,20,21,26 to28,33 to55,119 to121 and162; share, chattel and residence exceptions read with neighbouring clauses | https://nass.gov.ng/documents/download/11249 | 2026-11-16 |
| NTAA: sections 3,11,13,31 and49 | https://nass.gov.ng/documents/download/11250 | 2026-11-16 |
| Finance Act 2021: section 2, replacement of CGTA share exemption and reinvestment; official scanned Gazette OCR | https://lirs.gov.ng/assets/docs/Finance-Act-2021-Gazetted.pdf | 2026-11-16 |
| Finance Act 2023: sections 2/3 digital assets and same-type loss carry; official Gazette OCR | https://lirs.gov.ng/assets/docs/Finance_Act_2023.pdf | 2026-11-16 |
| Finance Act 2020: section 2 half-year self-assessment/payment; official state-authority copy OCR | https://www.iirs.im.gov.ng/document/docs/FINANCE_ACT_2020.pdf | 2026-11-16 |
| Finance Act 2019: section 49 business reorganisation replacement of CGTA section 32; official state-authority copy OCR | https://www.akirs.ak.gov.ng/downloads/laws/2019-finance-bill.pdf | 2026-11-16 |

Not yet confirmed: the old connected-person capital-loss assertion (loss usable only against gains on later disposals to that same connected person); the old non-resident buyer/Nigerian payment-agent CGT withholding and TCC-before-perfecting-title assertions, pending the applicable circular/law; the full-disposal extra-cost branch identified above; a retrievable complete historical CGTA with the property's original cost/relief, foreign-remittance and indexation rules; old voluntary-business replacement relief, eligible land/building/plant/ship/aircraft/hovercraft/goodwill classes,12-month-before/after window and partial reinvestment; any surviving additional2026 disposal return beyond annual integrated filing; special diplomatic, spousal, government-security and treaty exemptions asserted by the original file; transition of historical capital losses; exact treaty outcomes or foreign situs for a live case. The old NGN 1,000 chattel threshold, unqualified private-car exemption, indefinite loss carry and blanket10% current rate are withdrawn. Old section 32 now addressed business reorganisation after Finance Act 2019; it is not authority for the original general rollover instruction.
