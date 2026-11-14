---
name: wealth-estate-tax-workflow-base
description: "Shared 2026 method for wealth, estate, inheritance, gift and property-transfer tax working papers. Preserves event, personal scope, asset/situs valuation, liabilities, beneficiary, relief, rate, integration, foreign-relief and filing steps, with bounded France IFI and UK inheritance-tax applications. Load actual current country rules for other regimes, complete tax computation and filing."
version: 0.2
jurisdiction: GLOBAL
tax_year: 2026
type: cross-country-method
last_updated: 2026-11-14
category: foundation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# Wealth Estate Tax Workflow Base

## Wealth / Estate / Gift / Property Transfer Tax Workflow Base v0.2

## Scope

Shared 2026 preparation method for transfer-on-death, gift, annual wealth and property-transfer tax work. It preserves the full inventory, relationship, relief, computation and filing handoff; it is not a worldwide rate/valuation table. The UK and France examples below are bounded applications. Internal [T1]/[T2]/[T3] tags are workpaper flags, not professional approval.

## Ask the client first

Obtain the exact tax/event and date; donor/deceased/recipient and residence/citizenship/domicile history; asset legal/beneficial ownership and situs; valuation and debt documents; beneficiaries/relationships and representative; prior gifts, relief/credit use and relevant jurisdictions. Unknown ownership, date, representative or valuation remains unresolved.

## Section 1 , Audience and assumptions

This base covers a family of related taxes triggered by:
- **Holding** , annual wealth tax
- **Transfer at death** , inheritance / estate tax
- **Inter-vivos transfer** , gift tax
- **Real estate purchase / transfer** , property transfer tax / stamp duty

This base assumes:
- The taxpayer (or their representative) is preparing an accurate inventory
- Cross-border situs rules require multi-jurisdictional analysis
- A credentialed practitioner signs off before filing or transfer

## The method, step by step

### Step 1 , Identify the chargeable event

**Event / Tax(es) potentially triggered table**  _([T1])_

| Event | Tax(es) potentially triggered |
| --- | --- |
| Country-specific annual reference date, never default 31 December | Investigate the actual annual wealth/real-estate/income regime in Spain, Norway, Switzerland, Argentina, Colombia, Uruguay, France or the Netherlands; these are not all the same legal tax |
| Death of holder | Inheritance / estate tax (DE, FR, ES, IT, NL, BE, UK, US, JP, KR) |
| Gift / lifetime transfer | Gift tax (DE, FR, ES, IT, NL, BE, UK, US, JP, KR) |
| Real estate purchase | Property transfer tax (UK SDLT, DE GrESt, FR DMTO, IT registro, ES ITP/AJD, NL OB, SG BSD+ABSD, HK AVD) |

### Step 2 , Determine personal scope

- **Personal scope:** establish the actual taxpayer, donor/deceased/recipient, residence, domicile, citizenship and long-term-residence history under each tax and treaty. Ordinary income-tax residence alone does not establish worldwide estate/gift/wealth scope, nor does non-residence universally exclude overseas assets. The UK section below explains the change and continuing scope after leaving.
- **Property-transfer scope:** identify the actual property situs and local/state tax, purchaser's residence/citizenship/entity and other-property ownership, transaction and effective date, exemptions and any surcharge/refund. Preserve separate UK, Singapore, Canadian provincial and Australian state investigations; a single country-level percentage cannot stand in for them.

### Step 3 , Inventory all assets

- **For each asset, document** , Class (real estate, listed shares, unlisted shares, bank deposit, debt instrument, private equity, art / collectibles, crypto-asset, pension rights, life insurance, business interest); Location (situs per jurisdiction's rules); Valuation date; Valuation method (cadastral value, FMV, latest transaction, IFRS book value, professional appraisal); Ownership share  _([T1])_

### Step 4 , Apply valuation rules

- **Spanish succession/gift and wealth:** obtain the actual tax, asset, effective date, autonomous-community rules and statutory valuation base/reference-value rules. Do not substitute a universal cadastral value or the same base for inheritance tax and wealth tax.
- **French IFI:** use the actual annual reference date and market value, then the qualifying principal-residence reduction and ownership exceptions in the sourced France section below.
- **German inheritance/gift:** obtain the current Bewertungsgesetz valuation route for the actual asset, especially business property; an unverified accounting or cadastral amount is not a tax valuation
- **UK IHT:** obtain death-date asset values, beneficial ownership, gift/trust history and current liability/relief rules. [HMRC estate valuation](https://www.gov.uk/valuing-estate-of-someone-who-died/estimate-estate-value).
- **US estate:** route death-date/alternate valuation, election eligibility, consistency and beneficiary basis to the current federal estate method. The old unconditional alternative-date description does not establish an available election
- **Italian succession/property:** obtain the actual asset, rendita, statutory revaluation/multiplier, first-home eligibility and transfer tax before computation. Do not apply the old example multipliers as a complete current valuation formula

### Step 5 , Deduct liabilities

- **Liabilities:** inventory mortgages, funeral/administration costs, outstanding taxes and loans with their payer, asset link, date, recourse and evidence. Deduct only where the actual regime allows, after related-party, purpose, timing, valuation and cap tests. Keep Spain/Uruguay foreign-debt questions and US/UK estate-expense categories for the country method, not as universal deductions. France below illustrates why the debt does not simply follow the gross asset value.

### Step 6 , Identify beneficiaries and apply relationship rules

- **Beneficiary relationship categories** , Spouse / civil partner / cohabitant; Direct descendants (children, grandchildren); Direct ascendants (parents, grandparents); Siblings; Other relatives within a defined degree; Unrelated. Each relationship has distinct exemptions and rates (Germany Class I-III; Spain Group I-IV; France direct line vs collateral).  _([T1])_

### Step 7 , Apply exemptions and reliefs

- **Reliefs to test separately:** marital/civil-partner, principal-home, family-business, agricultural, charitable and disabled-beneficiary provisions. Preserve the US/UK/German marital, Spanish habitual-home, French Pacte Dutreil and German business-relief questions, but obtain their actual conditions and limits from current country law. UK Business/Agricultural Relief is not universally unlimited at the full percentage in 2026; the sourced UK section below records the changed boundary.

### Step 8 , Apply rate schedule

- **Rates:** obtain the actual tax, year, relationship class, taxable slice and national/regional schedule. Preserve the US estate, French succession, German inheritance, Italian relationship-class, Spanish autonomous-community and Swiss cantonal branches; do not compute from a generic minimum/maximum range or a relationship label alone.

### Step 9 , Apply caps and integration

- **Caps and integration:** obtain the actual Spanish income/wealth/solidarity interaction and floor, French IFI cap and relevant income/tax definitions, US estate/gift/GST credit/exemption allocation and UK gift cumulation. These are distinct computations, not automatic percentage caps or one interchangeable US credit. The UK gift lookback does not make every gift taxable or exempt without the applicable exception and retained-benefit analysis. [HMRC gifts](https://www.gov.uk/inheritance-tax/gifts).

### Step 10 , Compute and apply foreign tax credits

- **Foreign-tax relief:** identify the actual treaty, covered taxes, persons/assets and operative relief article; article numbering is not universal. Separately test domestic unilateral credit/deduction and its same-income/asset, payer, timing and cap conditions. Double taxation by itself does not create a refundable credit or prove that both countries must grant relief.

### Step 11 , Filing and payment

- **Filing and payment:** identify the actual tax authority, form/schedules, taxpayer/representative, due dates, payment reference, conditional instalment/security, conversion and attachments from the current country method. A worldwide months-from-event range is not a filing deadline. Retain acceptance/submission and actual payment evidence separately.

## Country applications

### France, IFI

The ordinary IFI valuation date is **1 January**, not a default year end. Directly held qualifying principal residence may receive the reduction below; holdings through a management SCI and usufruct/beneficial interests need their actual exceptions. Determine the household and which residence qualifies. [DGFiP valuation](https://www.impots.gouv.fr/particulier/questions/comment-determiner-la-valeur-des-biens-que-je-declare-pour-le-calcul-de-limpot).

Debt must exist and be borne at the relevant date and relate to taxable assets. Bullet/perpetual loans and related-party debts have special rules. The law permits specified family/controlled-company loans when normal conditions and effective repayments are proved; the FAQ's blanket family-loan exclusion is too broad. Follow **CGI art. 974 III**, not that shorthand. Its high-debt restriction also has a non-mainly-tax-purpose exception in IV. [Law, complete art. 974](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037988599), [FAQ, qualified principal-home debt treatment](https://www.impots.gouv.fr/particulier/questions/que-puis-je-deduire-au-niveau-du-passif-de-limpot-sur-la-fortune-immobiliere).

### United Kingdom, inheritance tax

For the relevant post-change events, ordinary residence alone does not settle overseas-asset scope: test long-term UK residence, actual history and departure/transitional provisions. An overseas move does not automatically end IHT exposure. Value estate assets at death, identify joint beneficial interests, gifts and trust rights, and test each debt/relief separately. Gifts with retained benefits can remain relevant despite the normal lookback. [HMRC long-term residence](https://www.gov.uk/guidance/inheritance-tax-if-youre-a-long-term-uk-resident), [valuation](https://www.gov.uk/valuing-estate-of-someone-who-died/estimate-estate-value), [gifts](https://www.gov.uk/inheritance-tax/gifts).

The old unqualified full Business Relief statement is not current. For deaths on or after **6 April 2026**, the official guidance caps the full-relief allowance for qualifying business/agricultural property and gives partial relief for qualifying excess; asset/ownership/exclusion and spouse-transfer conditions matter. It is not a general exemption for every business or every investment share. Use the current UK estate method for the full allocation, claim and tax computation. [HMRC qualifying property](https://www.gov.uk/business-relief-inheritance-tax/what-qualifies-for-business-relief).

### Other countries and taxes

Retain each named Spain, Germany, Italy, US, Switzerland, Singapore, Canada/province, Australia/state, Norway, Argentina, Colombia, Uruguay, Netherlands, Belgium, Japan and Korea investigation in the relevant country workpaper. The method does not certify their old rates, multipliers, exemptions, situs or deadlines without reading the current law. This is a scoped limit, not permission to discard their assets or taxpayer groups.

### Rates, bands and thresholds

These are limited method switches, not a worldwide tax-rate card.

| Item and conditions | Current method value | Official source |
|---|---|---|
| France IFI valuation date | 1 January of the actual tax year | [DGFiP valuation](https://www.impots.gouv.fr/particulier/questions/comment-determiner-la-valeur-des-biens-que-je-declare-pour-le-calcul-de-limpot) |
| France IFI qualifying principal residence, directly held; actual ownership/household exceptions apply | 30% reduction in market value | same |
| UK qualifying business/agricultural property, deaths on or after 6 April 2026; actual eligibility/allowance allocation and transfers apply | 100% relief capped by the GBP 2.5 million allowance; qualifying excess generally 50% | [HMRC Business Relief](https://www.gov.uk/business-relief-inheritance-tax/what-qualifies-for-business-relief) |

## Worked cases

**French principal residence, qualifying bank debt.** Assume a directly held qualifying principal residence has 1 January market value EUR 1,000,000. The actual legally deductible bank mortgage is EUR 400,000. There are no SCI/usufruct, related-party, bullet-loan or high-debt adjustments, and the household meets the principal-residence conditions. Residence value after the reduction is EUR 700,000; the qualifying debt is not simply reduced by the same percentage, leaving EUR 300,000 of net real-estate value in this limited workpaper. This does not compute IFI liability or establish filing status, which requires the whole household's relevant assets and current thresholds. [Valuation](https://www.impots.gouv.fr/particulier/questions/comment-determiner-la-valeur-des-biens-que-je-declare-pour-le-calcul-de-limpot), [principal-home debt](https://www.impots.gouv.fr/particulier/questions/que-puis-je-deduire-au-niveau-du-passif-de-limpot-sur-la-fortune-immobiliere).

```oa-check
name: French IFI principal residence and proved bank debt
inputs:
  market_value: 1000000
  principal_residence_reduction: 0.30
  deductible_bank_debt: 400000
steps:
  - residence_value: market_value * (1 - principal_residence_reduction)
  - allowed_debt_in_this_case: min(deductible_bank_debt, residence_value)
  - net_value: residence_value - allowed_debt_in_this_case
expected:
  residence_value: 700000
  allowed_debt_in_this_case: 400000
  net_value: 300000
```

**UK Business Relief boundary, simplified confirmed facts.** Assume a death after the 2026 change, qualifying property GBP 3 million, full GBP 2.5 million allowance available, and no transferable addition, competing agricultural allocation, special asset, exclusion or trust adjustment. Full relief covers GBP 2.5 million; partial relief on the GBP 0.5 million excess is GBP 0.25 million. Remaining property value before other estate allowances/tax is GBP 0.25 million, not zero. Eligibility and allowance availability must be established before using the example; it is not the final IHT bill. [HMRC full and partial relief](https://www.gov.uk/business-relief-inheritance-tax/what-qualifies-for-business-relief).

```oa-check
name: UK business relief does not automatically exempt all property
inputs:
  qualifying_property: 3000000
  available_full_relief_allowance: 2500000
  excess_relief_rate: 0.50
steps:
  - full_relief: min(qualifying_property, available_full_relief_allowance)
  - excess: max(qualifying_property - full_relief, 0)
  - partial_relief: excess * excess_relief_rate
  - remaining_value: qualifying_property - full_relief - partial_relief
expected:
  full_relief: 2500000
  excess: 500000
  partial_relief: 250000
  remaining_value: 250000
```

## Section 3 , Cross-border specifics

### 3.1 Situs determination

**Asset class / Situs evidence to investigate, never a worldwide conclusion**

| Asset class | Typical situs |
| --- | --- |
| Real estate | Identify land location and the actual tax's situs rule, ownership and treaty scope |
| Tangible movable | Establish physical location and relevant event date, then any actual situs exception |
| Shares in companies | Establish issuer incorporation/residence, register and the applicable look-through/anti-avoidance rule |
| Bank deposits | Identify debtor, branch, account and the applicable tax's actual debt/situs rule |
| Government bonds | Obtain issuer, legal instrument and applicable situs/exemption rule |
| Private equity / unlisted | Obtain issuer/entity/property details and the actual share/partnership/look-through rule |
| Crypto | Establish custody, beneficial rights, owner history and applicable country rule; no worldwide residence-based situs default |

### 3.2 Treaties

Wealth / estate / inheritance tax treaties exist sparsely. Most relief is unilateral.

## Section 4 , Reviewer brief

```
1. Personal scope
   - Tax residence / domicile / LTR confirmation
   - Worldwide vs local-situs basis

2. Asset inventory
   - Class, situs, value, ownership

3. Liabilities and deductions

4. Beneficiary / heir register
   - Relationship classification per jurisdiction

5. Exemptions and reliefs schedule

6. Computation per jurisdiction

7. Separate country cap/integration workpapers (Spain, France, US estate/gift/GST allocation)

8. Cross-border credit

9. Filing schedule and payment plan

10. Reviewer questions , [T2]/[T3] items
```

## Section 5 , Self-checks (14)

1. [ ] Tax residence / domicile / LTR tested per each jurisdiction's specific definition
2. [ ] Actual regime/event reference date established; annual wealth does not default to 31 December
3. [ ] All assets inventoried with situs determination
4. [ ] Valuation methodology per jurisdiction (cadastral, FMV, multiplier, professional appraisal)
5. [ ] Deductible liabilities only included where regime permits
6. [ ] Beneficiary relationships classified per jurisdiction taxonomy
7. [ ] Exemptions applied (marital, habitual residence, business, agricultural)
8. [ ] Rate schedule applied to net not gross
9. [ ] Actual Spanish/French cap definitions, limits/floors and exceptions applied only from the relevant country method
10. [ ] UK gift history, exemptions, applicable lookback, retained benefits and any trust/chargeable-transfer route checked rather than a universal gift rule
11. [ ] Actual treaty/unilateral relief eligibility and limit established; double taxation alone does not establish a credit
12. [ ] Filing form, deadline, payment plan per jurisdiction
13. [ ] Step-up basis impact recorded (US beneficiaries' income tax)
14. [ ] Output flags every [T2]/[T3] item for reviewer judgement

## When to refuse or refer

**Refusal catalogue table**

| Refusal | Trigger |
| --- | --- |
| R-WET-1 | Beneficiary / heir under disability and lacking representative |
| R-WET-2 | Trust / nominee / hidden beneficial ownership without disclosure |
| R-WET-3 | Asset class not clearly classified (NFT, crypto, complex derivative) |
| R-WET-4 | Family business with relief eligibility uncertain (continuation, payroll, holding period) |
| R-WET-5 | Cross-border situs in dispute |
| R-WET-6 | DAC6 / MDR reportable arrangement |
| R-WET-7 | Pre-existing tax authority audit or controversy |

- **R-WET-1** , Beneficiary / heir under disability and lacking representative
- **R-WET-2** , Trust / nominee / hidden beneficial ownership without disclosure
- **R-WET-3** , Asset class not clearly classified (NFT, crypto, complex derivative)
- **R-WET-4** , Family business with relief eligibility uncertain (continuation, payroll, holding period)
- **R-WET-5** , Cross-border situs in dispute
- **R-WET-6** , DAC6 / MDR reportable arrangement
- **R-WET-7** , Pre-existing tax authority audit or controversy

## Section 7 , Disclaimer

This workflow base produces working papers for review by credentialed estate planning practitioners. Estate, gift, wealth, and property transfer taxes have material magnitude and are jurisdiction-specific. Every output must be reviewed and signed off by a credentialed practitioner before filing or executing a transfer.

The most up-to-date, verified version of this workflow base is maintained at [openaccountants.com](https://openaccountants.com).

## Lifecycle recap

0. **Step 1 workflow orchestration** , Identify the chargeable event
0. **Step 2 workflow orchestration** , Determine personal scope
0. **Step 3 workflow orchestration** , Inventory all assets
0. **Step 4 workflow orchestration** , Apply valuation rules
0. **Step 5 workflow orchestration** , Deduct liabilities
0. **Step 6 workflow orchestration** , Identify beneficiaries and apply relationship rules
0. **Step 7 workflow orchestration** , Apply exemptions and reliefs
0. **Step 8 workflow orchestration** , Apply rate schedule
0. **Step 9 workflow orchestration** , Apply caps and integration
0. **Step 10 workflow orchestration** , Compute and apply foreign tax credits
0. **Step 11 workflow orchestration** , Filing and payment


## Sources

| Source and what was actually read | Official URL | Read on |
|---|---|---|
| DGFiP IFI valuation FAQ, updated April 2026. Read for complete operative valuation/ownership sections for January valuation, principal residence, SCI and usufruct limitations | https://www.impots.gouv.fr/particulier/questions/comment-determiner-la-valeur-des-biens-que-je-declare-pour-le-calcul-de-limpot | 2026-11-14 |
| DGFiP IFI debt FAQ, updated April 2026. Read for debt conditions and principal-home debt treatment; its blanket family-loan sentence is qualified by the law below | https://www.impots.gouv.fr/particulier/questions/que-puis-je-deduire-au-niveau-du-passif-de-limpot-sur-la-fortune-immobiliere | 2026-11-14 |
| CGI art. 974, complete I to IV. Read for actual debt categories, bullet/perpetual-loan adjustments, family/controlled-company normal-conditions exceptions and high-debt purpose exception. Page displayed in force since December 2018 in the code current to 12 November 2026; not a read of the whole code | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037988599 | 2026-11-14 |
| HMRC long-term UK residence guidance. Read for scope, history, departure and transitional sections; no ordinary-residence shortcut adopted | https://www.gov.uk/guidance/inheritance-tax-if-youre-a-long-term-uk-resident | 2026-11-14 |
| HMRC estate value. Read for opening estate estimate/assets and joint-ownership sections; not all specialist valuations in linked pages | https://www.gov.uk/valuing-estate-of-someone-who-died/estimate-estate-value | 2026-11-14 |
| HMRC gifts. Read for normal lookback, taper and retained-benefit sections; the method does not declare every lifetime gift automatically taxable or exempt | https://www.gov.uk/inheritance-tax/gifts | 2026-11-14 |
| HMRC Business Relief qualifying property. Read for full/partial relief, April 2026 allowance, spouse transfer, ownership and exclusions | https://www.gov.uk/business-relief-inheritance-tax/what-qualifies-for-business-relief | 2026-11-14 |

Not yet confirmed: current local/state property surcharges (old UK 2%, Singapore 60%, generic Canada 25%, Australian 7 to 8% are not adopted); Spanish succession/wealth valuation and its old 300,000 home/60% integration shorthand; German marital 500,000/business 85 to 100% and inheritance 7 to 50% figures; French succession 5 to 45%, Pacte Dutreil 75% and full IFI cap computation; Italian 110/120 multipliers and 4/6/8% relationship figures; US 18 to 40% estate range, alternate-valuation eligibility and separate estate/gift/GST integration. Also obtain each other country's actual annual date, situs, treaty/unilateral relief, liabilities, current forms, payment and deadlines instead of the old generic 6 to 12 months or assumed treaty article/count. The topics and asset/beneficiary groups remain in the method; their unverified numeric shortcuts do not remain usable tax guidance.
