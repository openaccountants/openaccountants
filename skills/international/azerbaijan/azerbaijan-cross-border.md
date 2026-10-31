---
name: azerbaijan-cross-border
description: 'Use this skill for 2026 Azerbaijan cross-border income and corporate tax working papers. It covers residence, domestic source and permanent-establishment tests, ordinary non-resident withholding, PE profit remittances, net-fee gross-up, foreign-tax credit, treaty administration, departure reporting and CFC screening. Trigger on Azerbaijan non-resident tax, withholding, treaty, tax residence, PE, foreign income, remittance tax, DTA forms, CFC and leaving Azerbaijan. The complete CFC inclusion, preferential-jurisdiction payment interactions and migration asset computations remain incomplete. VAT and contributions require their dedicated skills. Checked against the law (tier 2); no accountant has signed it off.'
jurisdiction: AZ
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-31
version: 0.1
trust_label: Built by Michael Cutajar and the OpenAccountants team
---

# Azerbaijan Cross-border Tax, Treaties and Non-residents v0.1

> **Checked against the law.** Tax year 2026. Figures independently re-checked against the official sources on 31 October 2026. General reference for working papers; a qualified professional must review the facts and filing position. No accountant has signed this skill off.

## Who this applies to

Individuals moving into/out of Azerbaijan, resident enterprises with foreign income or subsidiaries, non-residents earning Azerbaijan-source income, permanent establishments (PEs) and payers withholding tax on cross-border payments. This skill implements domestic residence/source/PE screening, ordinary non-resident withholding, foreign-tax credit and treaty-administration steps for 2026. It identifies CFC and departure obligations; the full CFC inclusion and departure-asset computation remains incomplete.

Under [Tax Code art. 13.2.5](https://e-qanun.az/frameworks/46/f_46948.html), an individual is resident if physically present more than 182 days in the calendar year, or in specified Azerbaijan state service abroad. If presence in neither state exceeds 182 days, apply permanent home, centre of vital interests, habitual abode and citizenship in that order. An entity is resident if established under Azerbaijan law or its place of practical management/commercial decision-making is in Azerbaijan. The actual treaty supplies any relevant dual-residence rule.

## Rates, bands and thresholds

| Item | Domestic rule | Tax year | Official source |
|---|---|---|---|
| Individual presence residence limb | More than 182 calendar-year days | 2026 | [Tax Code art. 13.2.5.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Ordinary PE duration test | At least 90 days in any 12 months | 2026 | [Tax Code art. 19.1, 19.4](https://e-qanun.az/frameworks/46/f_46948.html) |
| Corporate/PE profit tax | 20% of taxable profit | 2026 | [Tax Code art. 105.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Dividends to non-residents | 5%, subject to exemptions/treaties | 2026 | [Tax Code art. 122.1, 125.1.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Non-resident interest | 10%, subject to specific exemptions/treaties | 2026 | [Tax Code art. 123.1, 125.1.2](https://e-qanun.az/frameworks/46/f_46948.html) |
| Non-resident rent/royalties | 14% under ordinary rent/royalty rule | 2026 | [Tax Code art. 124.1, 125.1.7](https://e-qanun.az/frameworks/46/f_46948.html) |
| Specified insurance/reinsurance payments | 4% | 2026 | [Tax Code art. 125.1.3](https://e-qanun.az/frameworks/46/f_46948.html) |
| Specified international transport/communications payments | 6%; foreign-to-foreign/transit exceptions | 2026 | [Tax Code art. 125.1.4](https://e-qanun.az/frameworks/46/f_46948.html) |
| Other Azerbaijan-source non-PE work/services/income | 10%, excluding specific categories | 2026 | [Tax Code art. 125.1.5](https://e-qanun.az/frameworks/46/f_46948.html) |
| PE net profit paid/remitted to non-resident | 5% in addition to profit tax | 2026 | [Tax Code art. 126](https://e-qanun.az/frameworks/46/f_46948.html) |
| Preferential-jurisdiction payment rule | 10% on art. 13.2.16.14-1 payments, independently of other Code provisions | 2026 | [Tax Code art. 125-1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Foreign-tax credit ceiling | Azerbaijan tax on the same foreign-source income/profit | 2026 | [Tax Code art. 127.1–127.2](https://e-qanun.az/frameworks/46/f_46948.html) |
| CFC screening | More than 50% control/profit rights; foreign effective tax at most 75% of corresponding Azerbaijan profit tax; more than 30% listed passive-type revenue | 2026 | [Tax Code art. 14-2.1](https://e-qanun.az/frameworks/46/f_46948.html) |

## The base

First establish the recipient, beneficial owner, residence, income category and domestic source. Residents report worldwide income under arts. 97 and 104. Non-residents are taxed on Azerbaijan-source income under art. 13.2.16; the payment's bank destination alone is not the source test. Domestic employment, Azerbaijan property, specified business/service and investment income have distinct source limbs. Foreign management and financial-service payments have their own rule in art. 13.2.16.15. Review the actual contract, place and nature of performance, payer/PE connection and any statutory exception before calling all foreign services taxable or exempt.

Then test PE. Art. 19.1 covers direct or authorised-person business activity for at least 90 days in any 12 months. The listed sites include management, offices/branches/agencies, construction/installation and supervision, natural-resource sites, consultancy and other business locations. Art. 19.2.10 also identifies representatives preparing/concluding contracts and organising customers for the non-resident. Art. 19.2-1 aggregates related/controlled subcontractor construction periods where the subcontractor activity exceeds 30 days. Preparatory/auxiliary exceptions in art. 19.3 are subject to anti-fragmentation in art. 19.3-1. A treaty can alter domestic PE treatment under art. 2.5; do not apply a generic treaty construction period without reading the actual treaty.

For a PE, calculate attributable revenue less allowed expenses under arts. 104.2 and 108–121, using TP attribution under art. 14-1.10. Apply 20% corporate profit tax, then 5% on the amount of net profit transferred to the non-resident under art. 126. A retained profit and an actual remittance are distinct facts. See az-corporate-income-tax for depreciation, losses and instalments.

For non-PE income, art. 125.1 applies gross withholding without expense deductions at the applicable rate. Remove VAT/excise from the statutory gross base where required by art. 105.2 and classify the payment. Dividends, interest, royalties, insurance, transport and salary have specific rates. Salary follows art. 101 rather than the general service rate. Art. 124's residential rent to an individual has the specific 10% rule; ordinary commercial rent/royalty remains 14%. For a contract promising the non-resident a net amount N with payer-borne tax at rate r, gross taxable consideration is N/(1−r); tax is gross × r. A net-fee promise must be evidenced, not assumed.

From 25 December 2026, Law 413-VIIQD (arts. 2.5, 2.6 and 26) amends two withholding rules. Art. 123.1 drops its carve-out for PEs of individuals carrying on financial leasing, and its 10% rate expressly names loan interest under a financial lease paid to a non-resident without an Azerbaijan PE. Art. 125.5, which relieves payments by civil-aviation companies for aircraft and engines taken from non-residents without a PE, drops the words "or leasing (except financial leasing)" and then covers rent only. Payments up to 24 December 2026 use the current wording.

For art. 125.1.4 transport, distinguish an Azerbaijan/foreign international route from foreign-to-foreign or transit carriage expressly excluded in that paragraph. For art. 125-1, screen the actual official preferential-jurisdiction list under art. 128.3, recipient and payment account, including indirect payments. Do not substitute a commercial tax-haven list or assume treaty relief settles this separate payment charge. The complete payment-list exclusions and interactions remain outside the implemented calculation here.

For foreign-tax credit, compute Azerbaijan tax on the same foreign-source income under its domestic category, identify income/profit tax actually paid abroad, and credit the lower of those amounts under art. 127. Do not credit foreign VAT, social payments or a tax on unrelated income. DTA Rules section 4 governs the DTA-02 application and supporting foreign tax/income evidence. Under paragraph 4.2-2, attach the foreign-credit consent letter to the resident's income/profit-tax return. An excess foreign tax is not a negative Azerbaijan tax.

CFC screening under art. 14-2 requires all the stated limbs: direct/indirect voting, capital or profit rights above 50%, alone or with related persons; the foreign effective-tax comparison; and the listed revenue mix. The passive list includes interest, royalties, share/participation disposals, financial leasing, insurance/banking/financial transactions and specified no-economic-value supplies. Arts. 14-2.3–14-2.4 address double taxation and excluded income. The financial-leasing limb changes on 25 December 2026 under Law 413-VIIQD. Do not calculate the inclusion solely from accounting dividend receipts; the implementing inclusion and reporting rules must also be applied.

For treaties, retrieve the relevant agreement and any effective protocol/MLI modification from the [official treaty register](https://taxes.gov.az/az/page/ikiqat-vergitutmanin-aradan-qaldirilmasina-dair-beynelxalq-sazisler), which identifies effective/application dates and modified texts. The authority states MLI application for Azerbaijan began on 1 January 2025, but that is not proof every treaty provision changed on that date. Verify recipient residence, beneficial ownership and the specific income/PE article before applying any reduced rate. This pack supplies no generic treaty-rate table.

## Deadlines and filing

For art. 150.1.3–150.1.7 non-wage withholding, remit by the 20th of the month following the quarter in which income was paid; file the required withholding return by that date under art. 150.3.2–150.3.3. Salary and the other specified monthly-pay categories instead follow art. 150.3.1. Preferential-jurisdiction payment tax under art. 125-1 is reported/paid by the following quarter's 20th under art. 150.3-6. Do not use one universal monthly deadline for all non-resident payments.

PEs and persons with taxable unwithheld source income file annual profit/income returns by 31 March following the year under arts. 149.1–149.2 and pay under art. 152.1. Art. 149.6 permits the specified non-PE recipients taxed under arts. 125.1.3–.5 or .7 to file a net-basis recalculation/refund claim by the annual deadline, using allowed PE-style expenses and the art. 105.1 rate, capped at the original gross withholding. Do not assume gross withholding is always the only possible final computation.

Use DTA-01 for residence certification, DTA-02 for foreign-tax credit, DTA-03 for prior treaty relief and DTA-05 for refund under the [DTA administration Rules](https://www.taxes.gov.az/az/page/ikiqat-vergitutmanin-aradan-qaldirilmasi-haqqinda-beynelxalq-muqavilelerin-inzibatciligi-qaydalari). Under paragraphs 5.5–5.7, the payer must obtain the authority's consent letter before applying a reduced treaty rate; without timely consent, withhold domestically and use the refund procedure. DTA-05 must be filed no later than five years after the tax reporting period under paragraph 7.1. Attach residence, contract, payment/withholding and beneficial-owner evidence as required by sections 5, 7 and 7-1, with the document authentication/translation requirements in section 8. Under paragraph 5.3, submit DTA-03 by the end of the current quarter in which the income is paid. That filing limit does not replace the separate requirement to obtain consent before payment to use relief at source. Residence certification alone does not replace consent for relief at source.

For departure, art. 13.2.5.2 treats an individual as non-resident from the last day of presence through the year-end only if also non-resident in the immediately following tax year. Collect the next-year evidence. Changes to registered address/details are reportable within 15 days under art. 34.3; financial-institution residence changes require information within 30 days under art. 76-1.2. Suspension/individual business cessation needs a return within 30 days under art. 149.3; entity/PE liquidation uses art. 149.4's liquidation-balance event. VAT deregistration can tax retained inventory under arts. 159.6 and 166.3, subject to art. 159.7's full/partial input-credit entitlement condition. None of these establishes a general zero exit-tax result for unrealised assets.

## Penalties and interest

Under [Tax Code art. 57.1](https://e-qanun.az/frameworks/46/f_46948.html), failure without grounds to submit a required return for a period with taxable or exempt operations or tax objects attracts AZN 40. Under [Tax Code art. 58.1](https://e-qanun.az/frameworks/46/f_46948.html), an understated or evaded tax amount attracts a 50% financial sanction, excluding additional tax assessed by a desk audit; the horizontal-monitoring case in art. 58.1-1 uses 25%. Under [Tax Code art. 59.1–59.2](https://e-qanun.az/frameworks/46/f_46948.html), late tax or advance payments bear 0.1% per overdue day, for at most one year. For additional tax identified by field audit or horizontal monitoring, interest starts on the assessment date under art. 59.2. Apply the facts and procedural exceptions before assessing a sanction.

The payer remains liable for unwithheld/unremitted tax, interest and sanctions under art. 150.2. Failure/incorrect filing of the CFC statement is within the 6,000 sanction in art. 57.4; identify the actual statement required by art. 16.1.4-3. Obtain source-country treaty/refund deadlines separately.

## Cross-border points

Run VAT place-of-supply and reverse charge separately under arts. 168–169, and contribution eligibility separately under the insurance laws. Income-tax treaty relief does not settle either charge. A business move can change management residence, PE, payroll, CFC control and VAT registration at different times. Retain an event-by-event timeline with asset transfers, distributions, staff, premises and management decisions. This skill cannot substantiate a universal absence of migration/exit tax or implement the full CFC attribution for an arbitrary ownership chain.

## Two worked examples that recompute

### PE profit and actual remittance

Assume ordinary PE taxable profit of 100,000, no losses/credits or treaty relief, and all after-tax profit remitted. Profit tax is 20,000. The 80,000 remittance bears 4,000 additional tax, for 24,000 combined. Cash received by the head office after these taxes is 76,000 (arts. 105.1, 126).

```oa-check
name: AZ PE profit and full remittance 2026
inputs:
  profit: 100000
steps:
  - profit_tax: profit*0.20
  - remittance: profit-profit_tax
  - remittance_tax: remittance*0.05
  - combined_tax: profit_tax+remittance_tax
  - head_office_net: remittance-remittance_tax
expected:
  profit_tax: 20000
  remittance_tax: 4000
  combined_tax: 24000
  head_office_net: 76000
```

### Net-fee gross-up for a taxable non-PE service

Assume a service falls within art. 125.1.5, no treaty relief applies, and the contract guarantees the non-resident 90,000 net of Azerbaijan income withholding. Gross consideration is 90,000/(1−10%) = 100,000 and withholding is 10,000. This example excludes VAT from the promise and calculation; any art. 169 reverse charge is assessed separately.

```oa-check
name: AZ non-resident service net-fee gross-up 2026
inputs:
  net_fee: 90000
  rate: 0.1
steps:
  - gross_fee: net_fee/(1-rate)
  - withholding: gross_fee*rate
  - recipient_net: gross_fee-withholding
expected:
  gross_fee: 100000
  withholding: 10000
  recipient_net: 90000
```

## Ask the client first

- What are residence days, home/management facts and departure/next-year plans and evidence?
- Where are the work, property, customers and PE facilities/agents, and what are the activity dates?
- What is each payment category, gross/net promise, recipient/beneficial owner and payment route?
- Which treaty/protocol/MLI text applies and is a relief-at-source consent letter already held?
- What foreign income/tax, control rights, CFC accounts and preferential-jurisdiction links exist?
- What assets, profits, remittances, suspensions and liquidation events accompany the move?

## Sources

| Source and provisions read | Official URL | Read on |
|---|---|---|
| Tax Code, arts. 2, 13–19, 34, 57–59, 76-1, 95–105, 122–128, 149–152, 159, 166 | https://e-qanun.az/frameworks/46/f_46948.html | 2026-10-31 |
| Law 413-VIIQD of 26 May 2026, arts. 2.5, 2.6 and 26 | https://frameworks.e-qanun.az/62/f_62107.html | 2026-10-31 |
| DTA administration Rules, sections 3–8 | https://www.taxes.gov.az/az/page/ikiqat-vergitutmanin-aradan-qaldirilmasi-haqqinda-beynelxalq-muqavilelerin-inzibatciligi-qaydalari | 2026-10-31 |
| STS official treaty register, effective/application dates and MLI text links | https://taxes.gov.az/az/page/ikiqat-vergitutmanin-aradan-qaldirilmasina-dair-beynelxalq-sazisler | 2026-10-31 |

Not yet confirmed: Full CFC inclusion/ownership-chain calculation and implementing statement; preferential-jurisdiction payment exclusions/interactions and current official list; migration/exit asset valuation; which contracts the Law on Financial Lease (412-VIIQ) treats as a financial lease from 25 December 2026. No zero-tax result is inferred.
