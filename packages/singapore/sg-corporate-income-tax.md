---
name: sg-corporate-income-tax
description: "Corporate income tax in Singapore for a company, for Year of Assessment 2027 (financial year ending in 2026), with Year of Assessment 2026 figures alongside where a relief is set year by year. Covers the 17% rate, the preceding-year basis, what income is taxed, the foreign-sourced income exemption, the partial tax exemption, the start-up exemption, the YA 2026 corporate income tax rebate and cash grant, deductions, capital allowances, losses, group relief, one-tier dividends, ECI, Form C-S, Form C-S (Lite), Form C, instalments and penalties. Use for: how is my Singapore Pte Ltd taxed, Singapore company tax rate, corporate tax Singapore, start-up tax exemption, partial tax exemption, CIT rebate, ECI filing, Form C-S deadline, tax on company profit Singapore. Out of scope: sole proprietors and partners (sg-income-tax), GST (singapore-gst, sg-gst-return), CPF (sg-cpf-medisave), forming the company (singapore-formation), individual residency (sg-tax-residency), capital gains detail (sg-zero-cgt), transfer pricing (singapore-transfer-pricing)."
jurisdiction: SG
tax_year: 2026
tax_year_notes: "YA 2027 baseline for financial years ending in 2026, with YA 2026 figures and relief identified separately. Law checked as at 22 November 2026."
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
category: international
type: computation
version: 1.1
---

# Singapore Corporate Income Tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Work out the Singapore income tax of a company for Year of Assessment (YA) 2027, which taxes the financial year ending in 2026. YA 2026 figures (financial year ending in 2025) are shown next to it where a relief is set year by year, because the YA 2026 return is due on 30 November 2026. The law is the Income Tax Act 1947 (ITA), current version on Singapore Statutes Online, and the Inland Revenue Authority of Singapore (IRAS) guidance.

A company here means a body incorporated under the Companies Act 1967 (a "Pte Ltd" or "Ltd"), a Singapore branch of a foreign company, or a foreign company. A sole proprietorship or partnership is not a company. Source: [IRAS basic guide](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/basic-guide-to-corporate-income-tax-for-companies).

Out of scope, use the sibling skill:

| Topic | Skill |
|---|---|
| Sole proprietors and partners | [sg-income-tax](sg-income-tax.md) |
| GST | [singapore-gst](singapore-gst.md) and [sg-gst-return](sg-gst-return.md) |
| CPF and MediSave | [sg-cpf-medisave](sg-cpf-medisave.md) |
| Forming the company | [singapore-formation](singapore-formation.md) |
| Tax residency of individuals | [sg-tax-residency](sg-tax-residency.md) |
| Capital gains in detail | [sg-zero-cgt](sg-zero-cgt.md) |
| Transfer pricing | [singapore-transfer-pricing](singapore-transfer-pricing.md) |

Tax incentives with a concessionary rate, insurers, shipping, property developers, investment holding companies and real estate investment trusts have their own rules and are not computed here.

## Ask the client first

1. Financial year end, and the date of incorporation. These fix the YA and whether the company is in its first 3 YAs.
2. Where it is incorporated, and where the board makes strategic decisions (tax residency).
3. Shareholders throughout the financial year: how many, are they individuals, does at least one individual hold 10% or more of the ordinary shares. Principal activity: is it investment holding or property development.
4. Revenue, accounting profit, and the tax adjustments: private car costs, depreciation, capital items, donations, fixed assets bought.
5. Unutilised losses, capital allowances or donations brought forward, and any change in shareholders since they arose.
6. Any foreign income, any of it brought into Singapore, foreign tax paid on it, and any payment to a non-resident (interest, royalties, service or management fees, director's fees).
7. For the YA 2026 cash grant, check the 2025 CPF records, the employee's citizenship or permanent residence and shareholder-director status, any centralised hiring or secondment and whether the company remained active at disbursement.
8. For a multinational group, obtain consolidated revenue for the 4 preceding financial years and the periods they cover. Apply the EUR 750 million test in section 8 of the Multinational Enterprise (Minimum Tax) Act 2024.

## The method, step by step

### 1. Rate, year of assessment and basis period [ITA section 43(1)(a)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr43-)

Tax is charged for each YA on the chargeable income of a company at 17%. Section 43(1)(a): "every company or body of persons, tax at the rate of 17% on every dollar of the chargeable income". The same rate applies to local and foreign companies.

Singapore taxes on a preceding-year basis. The company's financial year is the basis period, and it is generally the 12 months before the YA. The company picks its own year end.

| Financial year ends | Year of Assessment | Form C-S or Form C due |
|---|---|---|
| Any date in 2025 | YA 2026 | 30 November 2026 |
| Any date in 2026 | YA 2027 | 30 November 2027 |

A basis period cannot be longer than 12 months. If the first accounts cover more than 12 months, split the profit over two YAs, by actual dates or by time apportionment. The first YA is the YA for the basis period in which the company was incorporated. Source: [IRAS basic guide](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/basic-guide-to-corporate-income-tax-for-companies).

### 2. Which income is taxed [ITA section 10(1) and 10(25)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr10-)

Section 10(1) taxes income "accruing in or derived from Singapore or received in Singapore from outside Singapore". That covers trade or business profits, dividends, interest, rents, royalties and other profits from property.

Foreign income is "received in Singapore" under section 10(25) when it is:

- remitted to, transmitted or brought into Singapore;
- applied to pay a debt incurred in a trade or business carried on in Singapore; or
- applied to buy movable property that is brought into Singapore.

Foreign income that arises from a trade or business carried on in Singapore is taxed when it accrues, whether or not it is received in Singapore. Source: [IRAS, companies receiving foreign income](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/companies-receiving-foreign-income).

**Tax residency.** A company is resident for a YA if the control and management of its business was exercised in Singapore in the preceding calendar year. This usually follows where the board meets to make strategic decisions. The place of incorporation does not decide it. Source: [IRAS, tax residency of a company](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/tax-residency-of-a-company-certificate-of-residence).

**Foreign-sourced income exemption** [ITA section 13(8) and 13(9)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr13-). A resident company is exempt on three kinds of foreign income received in Singapore: foreign-sourced dividends, foreign branch profits, and foreign-sourced service income. All three conditions must be met:

| Condition | Rule | Source |
|---|---|---|
| Subject to tax | Test the territory's comparable income tax or qualified domestic minimum top-up tax, disregarding excluded top-up tax. For dividends the underlying tax paid by the paying company can count. IRAS can accept incentives for substantive business activities where the company documents the exemption | [ITA section 13(9)(a)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr13-) and [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/companies-receiving-foreign-income) |
| Headline rate | The highest corporate tax rate of that territory is at least 15% on receipt in Singapore. Disregard excluded and qualified domestic minimum top-up taxes for this test | [ITA section 13(9)(b)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr13-) |
| Benefit | The Comptroller is satisfied the exemption is beneficial to the company | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/companies-receiving-foreign-income) |

For other foreign income (such as interest, royalties or rent), check for a specific exemption, including under [ITA section 13(12)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr13-). If the income is taxable on receipt, test foreign tax credit eligibility under step 8.

### 3. Compute chargeable income [ITA sections 14 and 15](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr14-)

Start from accounting profit and adjust.

**Deductible.** Section 14(1) allows "all outgoings and expenses wholly and exclusively incurred during that period by that person in the production of the income". IRAS reads this as four tests: incurred solely to produce income, actually incurred (the legal liability has arisen), revenue and not capital in nature, and not prohibited by the Act. Source: [IRAS, business expenses](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses).

**Not deductible** [ITA section 15(1)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr15-):

| Item | Rule | Source |
|---|---|---|
| Private or domestic expenses | Section 15(1)(a) | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses) |
| Capital expenditure, including the cost of incorporating the company and buying fixed assets | Section 15(1)(c). Claim capital allowances instead where they exist | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses) |
| Depreciation and amortisation | Add back. Claim capital allowances instead | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses) |
| Private cars (S-plated) and business cars (Q-plated or RU-plated, registered on or after 1 April 1998) | Disallow ordinary running costs and reimbursements under section 15(1)(k), subject to the statutory exceptions for qualifying vehicles and businesses. Apply ordinary deduction tests to vans, lorries and buses | [ITA section 15(1)(k) and (3)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr15-) and [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses/tax-treatment-of-business-expenses-(m-r)) |
| Donations | Not a business expense. Approved donations are relieved separately | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses) |

Under section 14R, for an eligible business the deemed commencement date is the first day of the accounting year in which it earns its first business receipt. Test qualifying revenue expenditure in that year and in the 12 months before the deemed date. Check separate rules for specified pre-commencement costs such as qualifying research or renovation. [IRAS e-Tax Guide, paragraphs 2.1 and 2.2](https://www.iras.gov.sg/media/docs/default-source/e-tax/etaxguide_income-tax_treatment-of-certain-expenses-incurred-prior-to-the-commencement-of-a-business-activity.pdf).

**Capital allowances** [ITA sections 19 and 19A](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr19A-). Claimed on plant and machinery used in the trade. The company chooses the method per asset:

| Method | What is allowed | Source |
|---|---|---|
| 1 year, computers and prescribed automation equipment (section 19A(2)) | 100% of cost | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances) |
| 1 year, low-value assets (section 19A(10A)) | 100% of cost for an asset costing not more than $5,000. Total claim for all low-value assets capped at $30,000 per YA | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances) |
| 3 years (section 19A(1)) | One third of cost each year, for any qualifying asset | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances) |
| Working life (section 19) | Initial allowance of 20% and annual allowance on the remaining 80%. If the initial allowance is not claimed in the year the expenditure is incurred, calculate annual allowance on 100%. For qualifying YA 2023 onward acquisitions, elect 6 or 12 years if the prescribed life is 12 years or less. The 16-year option is available if the prescribed life is 16 years | [ITA section 19](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr19-) and [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances) |

The 2-year write-off applied to assets acquired in the basis periods for YA 2021, YA 2022 and YA 2024. Apply the available 1-year, 3-year or working-life methods to qualifying YA 2026 and YA 2027 purchases. Qualifying private hire or driving instruction cars and foreign-registered cars used exclusively outside Singapore for business can qualify for capital allowances. Vans, lorries and motorcycles used for business can also qualify. The 1-year and 3-year write-offs and working-life annual allowance can be deferred. The historical 2-year write-off and working-life initial allowance have fixed claim timing. Check for a balancing allowance or charge on disposal. [IRAS capital allowances](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances).

**Unutilised losses, capital allowances and donations** [ITA sections 23 and 37](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr37-). Brought-forward losses must be set off first; the company cannot hold them back to make more use of an exemption. A capital allowance claim can be deferred.

| Item | Carry forward | Conditions | Source |
|---|---|---|---|
| Trade losses | Indefinitely | Shareholding test | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/unutilised-items-(capital-allowances-trade-losses-donations)) |
| Capital allowances | Indefinitely | Shareholding test, and the company carries on the same trade or business | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/unutilised-items-(capital-allowances-trade-losses-donations)) |
| Approved donations | Up to 5 YAs | Shareholding test | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/unutilised-items-(capital-allowances-trade-losses-donations)) |

Shareholding test: the same persons must hold 50% or more of issued shares on both relevant dates. The first date is the last day of the calendar year in which the loss was incurred or the donation made, or the last day of the YA in which the capital allowances arose. The second is the first day of the YA of deduction. Apply the statutory look-through rules. For unutilised losses or capital allowances, apply to IRAS for a waiver if the shareholder change was for bona fide commercial reasons without a tax benefit or advantage. The Minister or an appointed person can grant a waiver under sections 23(5) and 37(16). [IRAS unutilised items](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/unutilised-items-(capital-allowances-trade-losses-donations)).

**Carry-back** [ITA section 37D](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr37D-). Current-year unutilised capital allowances and trade losses can be carried back 1 YA, to the immediately preceding YA. The maximum is $100,000. Capital allowances go first, then losses. The shareholding and same-business tests apply, and the company must claim it. Source: [IRAS, loss carry-back relief](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-reliefs/loss-carry-back-relief).

**Group relief** [ITA section 37B](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr37B-). Current-year unutilised capital allowances, trade losses and donations can be transferred to another group company if both companies:

- are incorporated in Singapore;
- are in the same group under the 75% ordinary-share test, directly or through qualifying Singapore-incorporated companies. Apply the corresponding 75% residual profit and asset entitlement tests and apportion qualifying deductions if the companies met the group test for only part of the basis period;
- have accounting periods ending on the same day; and
- elect when they file their returns. The election is irrevocable.

Source: [IRAS, group relief](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-reliefs/group-relief).

### 4. Apply the exemption: partial, or start-up [ITA section 43(6B) to (6D)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr43-)

The exemption applies to normal chargeable income, meaning income taxed at 17%. A company gets one of the two, never both. The bands are the same for YA 2026 and YA 2027; the statute sets them for "the year of assessment 2020 and subsequent years of assessment".

| Scheme | Band of chargeable income | Exempt | Maximum exempt amount per YA | Source |
|---|---|---|---|---|
| Partial tax exemption | First $10,000 | 75% ($7,500) | | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes) |
| Partial tax exemption | Next $190,000 | 50% ($95,000) | $102,500 | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes) |
| Start-up exemption | First $100,000 | 75% ($75,000) | | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes) |
| Start-up exemption | Next $100,000 | 50% ($50,000) | $125,000 | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes) |

**Partial tax exemption.** Every company gets it, including a foreign company and a Singapore branch, unless it claims the start-up exemption.

**Tax exemption scheme for new start-up companies.** Only for the first 3 consecutive YAs, counted from the YA of the basis period in which the company was incorporated. A YA with a loss or no income still counts as one of the 3. An unused exempt amount cannot be carried to another YA. For each YA claimed, the company must:

- be incorporated in Singapore;
- be tax resident in Singapore for that YA; and
- where limited by shares, have its total share capital beneficially held directly by no more than 20 shareholders throughout the basis period, where either all are individuals, or at least one is an individual holding at least 10% of issued ordinary shares throughout the period. For a company limited by guarantee, test whether all members are individuals throughout the period or at least one individual member represents at least 10% of total winding-up contributions throughout the period.

For a company incorporated on or after 26 February 2013, [ITA section 43(11)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr43-) excludes a company undertaking property development directly or as a partner, and a company whose sole activity is holding investments. Where a partner's partnership solely holds investments, the partnership limb excludes the company if the company itself has no activity or solely holds investments. The partial exemption is available to these companies on qualifying income. A sole proprietorship or partnership converted into a Singapore company can claim the start-up exemption if the conditions are met. IRAS audits companies set up to split an existing business's income across shell companies. [IRAS exemption schemes](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes).

Tax payable before rebate = (chargeable income less the exempt amount) at 17%, less foreign tax credit and other set-offs.

### 5. Corporate income tax rebate and cash grant [ITA section 92M](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr92M-)

A rebate is set one year at a time: announced in the Budget, then written into the Act as its own section (section 92L for YA 2025, section 92M for YA 2026). Never carry one year's rebate into another year.

| YA | CIT Rebate | Cash grant | Cap on rebate plus grant | Source |
|---|---|---|---|---|
| 2026 | 50% of tax payable | $2,000 | $40,000 | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes); ITA section 92M(1) and (3) |
| 2027 | Use the enacted baseline as at 22 November 2026 | Pending any YA 2027 announcement | Pending any YA 2027 announcement | [IRAS rebate table](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes) |

How YA 2026 got to these figures: the Budget 2026 statement (paragraph 18(b)) gave a 40% rebate, a minimum benefit of $1,500 and a cap of $30,000. Budget 2026 Annex H-1, item 1, records the update announced in the 7 April 2026 Ministerial Statement: a 50% rebate, a minimum benefit of $2,000 and a total maximum of $40,000 per company. Both sets are for the same YA 2026; the second replaced the first. The enhanced figures are the law: section 92M, inserted by the Finance (Income Taxes) Act 2026 (Act 23 of 2026, in force 4 November 2026), remits "50% of the tax payable for that year of assessment" less "the cash grant of $2,000", up to "$40,000, less the cash grant of $2,000". IRAS applies the same figures.

Rules for YA 2026:

- The rebate is available to resident and non-resident taxpaying companies where the Comptroller is satisfied it is beneficial. Compute it after set-offs such as foreign tax credit and before tax deducted at source. Exclude tax levied under section 43(3), (3A), (3B) and (3C).
- The tax-exempt cash grant generally requires an active company to have made a compulsory CPF contribution in calendar year 2025 for at least one qualifying Singapore citizen or permanent resident employee, excluding shareholder-directors. Holding investments counts as active. There are separate conditions for a centralised hire or a related-party secondee, including who bore the remuneration and CPF cost. Apply the disbursement exclusions for inactive companies, liquidation, receivership over all property or cessation, subject to Comptroller permission. The Comptroller may also waive the contribution timing requirement where just and equitable. [ITA section 92M(3) to (8)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr92M-).
- A company that gets the cash grant: if 50% of tax is $2,000 or less, no rebate is given. If it is more, the rebate is the 50% amount (capped at $40,000) less $2,000 (section 92M(1) and (2)).
- A company that does not get the cash grant: the rebate is the 50% amount, capped at $40,000.
- IRAS computes the rebate automatically. Do not deduct it in the ECI or the return.
- A company that met the condition but did not receive the grant (for example staff hired through a group company) can appeal by myTax Mail by 30 November 2026.

For YA 2027, give the tax under the law at the audit cutoff and check the availability of any YA 2027 relief at the time of filing.

### 6. Dividends and capital gains [ITA section 13(1)(za)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr13-)

**One-tier system.** The company's tax is final. Section 13(1)(za) exempts "any dividends paid on or after 1 January 2008 by any company resident in Singapore". Ordinary one-tier dividends are exempt for shareholders. Check separate rules for co-operative distributions. [IRAS dividend treatment](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/dividends).

**Capital gains.** There is no general capital gains tax. IRAS: "Capital gains are not taxable", for example gains on the sale of fixed assets. Whether a gain is capital or trading income is a question of fact (the badges of trade). Use [sg-zero-cgt](sg-zero-cgt.md) for that test and for the section 13W equity disposal rule. Source: [IRAS, taxable and non-taxable income](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/taxable-non-taxable-income).

**Gains on foreign assets** [ITA section 10L](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr10L-). For sales or disposals on or after 1 January 2024, section 10L can charge gains received in Singapore that would otherwise be non-taxable or exempt. It applies to a seller in a relevant group whose entities are established in multiple jurisdictions or have a place of business in more than one jurisdiction. Test the applicable financial institution, incentive and economic substance exclusions. Intellectual property gains have a separate rule, including the qualifying intellectual property nexus test. Refer if the client is in a cross-border group and disposed of a foreign asset.

### 7. File and pay

**Estimated Chargeable Income (ECI)** [ITA section 63](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr63-). File within 3 months from the end of the financial year. State ECI before the partial or start-up exemption; IRAS applies it.

| ECI rule | Figure | Source |
|---|---|---|
| Deadline | 3 months from the financial year end | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/estimated-chargeable-income-(eci)-filing) |
| Waiver, both needed | Annual revenue of $5 million or below, and ECI is nil | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/estimated-chargeable-income-(eci)-filing) |

Use revenue from the company's main activity. Exclude separate-source income outside that activity. For an investment holding company use its investment income. The company self-assesses the ECI waiver and checks its return obligation separately.

**The return.** File the applicable corporate return by 30 November, including for a nil or loss year. A qualifying dormant company can apply for an IRAS filing waiver. File electronically at mytax.iras.gov.sg. [IRAS 2026 filing season](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-filing-season-2026) and [dormant company waiver](https://www.iras.gov.sg/taxes/corporate-income-tax/dormant-companies-or-companies-closing-down/dormant-companies).

| Form | Who can use it | Documents | Source |
|---|---|---|---|
| Form C-S | Incorporated in Singapore; annual revenue of $5 million or below; only income taxable at 17%; not claiming carry-back relief, group relief, investment allowance, foreign tax credit or tax deducted at source | Keep accounts and tax computation; send only if asked | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-(lite)-form-c-filing/overview-of-form-c-s-form-c-s-(lite)-form-c) |
| Form C-S (Lite) | Meets the Form C-S conditions and has annual revenue of $200,000 or below | Same as Form C-S | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-(lite)-form-c-filing/overview-of-form-c-s-form-c-s-(lite)-form-c) |
| Form C | Every other company | File financial statements and tax computation with the form | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-(lite)-form-c-filing/overview-of-form-c-s-form-c-s-(lite)-form-c) |

One-tier exempt Singapore dividends and foreign income exempt under section 13(8) do not stop a company using Form C-S. A foreign tax credit claim does: it needs Form C.

**Payment.** Tax is payable within one month after service of the notice of assessment, even if the company objects, subject to any extension allowed by the Comptroller. For a company the objection period is 2 months from service. [ITA section 85](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr85-) and [section 76](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr76-).

**Instalments.** A Singapore-registered company that pays by GIRO can pay its ECI tax by instalments. The earlier it files, the more instalments:

| ECI filed within | Instalments | Source |
|---|---|---|
| 1 month from financial year end | 10 | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/estimated-chargeable-income-(eci)-filing) |
| 2 months | 8 | same |
| 3 months | 6 | same |
| After 3 months | None | same |

File by the 26th for the earlier start to GIRO deductions. IRAS may combine the first 2 deductions for a later filing within the same qualifying month. The minimum monthly GIRO deduction is $50. [IRAS ECI filing](https://www.iras.gov.sg/taxes/corporate-income-tax/estimated-chargeable-income-(eci)-filing).

**Penalties.**

| Failure | Consequence | Source |
|---|---|---|
| Tax not paid by the due date (section 87) | 5% penalty on the unpaid tax | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/corporate-income-tax-payment/late-payment-or-non-payment-of-corporate-income-tax) |
| Still unpaid 60 days after the 5% penalty | A further 1% for each completed month, up to 12% of the unpaid tax | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/corporate-income-tax-payment/late-payment-or-non-payment-of-corporate-income-tax) |
| Return not filed by the due date | IRAS may assess estimated tax payable within 1 month of service, offer composition of up to $5,000 per offence, or summon the company. A statutory filing failure without reasonable excuse carries a fine of up to $5,000 on conviction, with up to 6 months' imprisonment in default of payment | [ITA sections 85 and 94A](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr85-,pr94A-) and [IRAS late filing](https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-(lite)-form-c-filing/late-filing-or-non-filing-of-Corporate-Income-Tax-Returns-form-c-s-form-c-s-(Lite)-form-c) |
| Filing failure without reasonable excuse for 2 years or more | On conviction, penalty of twice the tax assessed and a fine up to $5,000, with up to 6 months' imprisonment in default of payment | [ITA section 94A(3)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr94A-) |
| Director fails without reasonable excuse to comply with a section 65B(3) notice | On conviction, fine up to $10,000, imprisonment up to 12 months or both. A continuing offence can carry a further fine of up to $100 for each day or part of a day after conviction | [ITA section 65C](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr65C-) |
| Incorrect return or information without reasonable excuse or through negligence, section 95(2) | On conviction, penalty of double the tax undercharge for a tax-only offence, plus a fine up to $5,000, imprisonment up to 3 years or both. Section 95(1) provides a 100% penalty for the specified basic offence | [ITA section 95](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr95-) |
| Wilful intent to evade tax, section 96 | On conviction for a tax-only offence, penalty of 3 times the undercharge plus a fine up to $10,000, imprisonment up to 3 years or both | [ITA section 96](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr96-) |
| Serious fraudulent evasion, section 96A | On conviction for a tax-only offence involving conduct such as false records, penalty of 4 times the undercharge plus a fine up to $50,000, imprisonment up to 5 years or both | [ITA section 96A](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr96A-) |

Keep records for at least 5 years from the relevant YA.

### 8. Cross-border pointers

**Withholding tax on payments to non-residents.** The paying company files and pays by the 15th of the second month following the payment month. Determine the actual or deemed payment date using the earliest applicable date under the contract or invoice, crediting and actual payment rules. Check the specific timing rules for a director's fee. [ITA section 45](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr45-) and [IRAS deemed payment guide](https://www.iras.gov.sg/docs/default-source/e-tax/etaxguide_determining-the-date-of-payment-or-deemed-payment-for-the-purpose-of-complying-with-withholding-tax-obligations.pdf).

| Payment to a non-resident | Rate | Source |
|---|---|---|
| Interest, commissions and fees in connection with a loan | 15% | [IRAS](https://www.iras.gov.sg/taxes/withholding-tax/basics-of-withholding-tax/types-of-payment-and-withholding-tax-rates) |
| Royalties for the use of movable property such as intellectual property | Generally 10%, subject to the separate rules for royalties paid to authors, composers or choreographers and to applicable treaty or exemption | [IRAS rates table](https://www.iras.gov.sg/taxes/withholding-tax/basics-of-withholding-tax/types-of-payment-and-withholding-tax-rates) |
| Rent for the use of movable property | 15% | [IRAS rates table](https://www.iras.gov.sg/taxes/withholding-tax/basics-of-withholding-tax/types-of-payment-and-withholding-tax-rates) |
| Covered technical assistance, service and management fees to a non-resident company | 17% of gross fees attributable to work performed in Singapore, subject to treaty relief. Tax withheld can be reconciled against tax on net income | [IRAS payments subject to withholding](https://www.iras.gov.sg/taxes/withholding-tax/payments-to-non-resident-company/payments-that-are-subject-to-withholding-tax) |
| Remuneration of a non-resident director | 24% | [IRAS](https://www.iras.gov.sg/taxes/withholding-tax/basics-of-withholding-tax/types-of-payment-and-withholding-tax-rates) |

The ordinary 15% and 10% reduced rates apply to gross payments and are final where the non-resident derives the income through operations outside Singapore and meets the statutory conditions. For in-Singapore operations check the prevailing corporate rate for a non-individual. Check the separate 24% rate and phased concession for qualifying individual authors, composers and choreographers. Test whether withholding applies and retain the treaty and certificate of residence when claiming treaty relief. Late payment under section 45 carries 5% on the unpaid tax. After 30 days overdue, a further 1% applies per completed month of non-payment, capped at a 15% additional penalty. [ITA section 45(4)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr45-) and [IRAS rates table](https://www.iras.gov.sg/taxes/withholding-tax/basics-of-withholding-tax/types-of-payment-and-withholding-tax-rates).

**Foreign tax credit.** For foreign income that is taxed in Singapore, a resident company gets a credit equal to the lower of the foreign tax paid and the Singapore tax on the same income (net of expenses). It is given under a treaty (double tax relief) or unilaterally where there is no treaty. A company in a loss position gets no credit. Claim it in Form C. Source: [IRAS, foreign tax credit](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-reliefs/foreign-tax-credit).

**Transfer pricing.** Related-party transactions must be at arm's length. Use [singapore-transfer-pricing](singapore-transfer-pricing.md).

**Global minimum tax.** For financial years beginning on or after 1 January 2025, Singapore applies multinational enterprise top-up tax under the income inclusion rule and domestic top-up tax. Test the 15% jurisdictional effective tax rate, exclusions and any safe harbour. A multinational group meets the revenue test when consolidated revenue reaches EUR 750 million for at least 2 of the preceding 4 financial years, with the statutory adjustment for periods other than 12 months. Refer an in-scope group for the full computation. [Multinational Enterprise (Minimum Tax) Act 2024, section 8](https://sso.agc.gov.sg/Act/MEMTA2024?ProvIds=pr8-) and [IRAS GloBE rules and DTT](https://www.iras.gov.sg/taxes/pillar-2-top-up-taxes/global-anti-base-erosion-(globe)-rules-and-domestic-top-up-tax-(dtt)).

## Boundary and exception table

| Situation | Action |
|---|---|
| Company in its first 3 YAs | Test every start-up condition for that YA: incorporated in Singapore, resident, 20 shareholders or fewer, the individual-shareholder test, and not investment holding or property development. If any fails, use the partial exemption. |
| All shares held by a company | Start-up exemption fails (no individual holds 10%). Partial exemption applies. |
| Loss or nil income in a first-3 YA | The YA still counts toward the 3. No exemption is carried forward. |
| Losses or capital allowances brought forward and shareholders changed | Run the 50% shareholding test on the two dates before deducting anything. |
| YA 2027 computation | Use the baseline at the cutoff and check any later YA 2027 relief before filing. |
| Cash grant company with tax of $4,000 or less for YA 2026 | 50% of the tax is $2,000 or less, so no rebate is given on top of the $2,000 grant (derived from the IRAS rule). |
| Car costs | Check the ordinary disallowance and the statutory exceptions in step 3 before adding back running costs or disallowing capital allowances. |
| Foreign dividend, branch profit or service income received | Test the 3 section 13(9) conditions. If one fails, check other exemptions or relief and foreign tax credit eligibility. |
| Payment to a non-resident | Withholding question first. It is separate from the company's own tax. |
| Concessionary rate, incentive, insurer, shipping, property developer, investment holding company | Refer. The ordinary computation here does not apply as it stands. |
| Group with EUR 750 million revenue | Check the multinational group, reference-year and period-length conditions in step 8. Refer an in-scope group for the effective tax rate, exclusions and safe harbour tests. |

## Worked cases

All amounts are in Singapore dollars and are illustrative inputs. No foreign income, no incentives, no losses brought forward.

### Established small company, YA 2026, with the partial exemption and the rebate

A trading company in its sixth year has chargeable income of $300,000 for YA 2026 (financial year ended 31 December 2025). It remained active at disbursement and made compulsory 2025 CPF contributions for 2 local employees who were not shareholder-directors. Assume the remaining grant conditions are met.

1. Partial exemption: 75% of the first $10,000 is $7,500. 50% of the next $190,000 is $95,000. Exempt amount $102,500.
2. Income taxed at 17%: $300,000 less $102,500 is $197,500. Tax is $33,575.
3. Rebate: 50% of $33,575 is $16,787.50, under the $40,000 cap. Because the company gets the $2,000 cash grant, the rebate given is $16,787.50 less $2,000, which is $14,787.50.
4. Tax payable: $33,575 less $14,787.50 is $18,787.50. The $2,000 grant is paid to the company separately, so the total YA 2026 benefit is $16,787.50.

With the same income for YA 2027, tax under the enacted baseline at the cutoff is $33,575.

```oa-check
name: Established company, chargeable income 300,000, YA 2026 partial exemption and rebate
inputs:
  chargeable_income: 300000
  cash_grant: 2000
steps:
  exempt_band1: min(chargeable_income, 10000) * 0.75
  exempt_band2: min(max(chargeable_income - 10000, 0), 190000) * 0.50
  exempt_amount: exempt_band1 + exempt_band2
  taxed_income: chargeable_income - exempt_amount
  tax_before_rebate: taxed_income * 0.17
  rebate_computed: min(tax_before_rebate * 0.50, 40000)
  rebate_given: max(rebate_computed - cash_grant, 0)
  tax_payable_ya2026: tax_before_rebate - rebate_given
  total_benefit: rebate_given + cash_grant
  tax_payable_ya2027: tax_before_rebate
expected:
  exempt_amount: 102500
  taxed_income: 197500
  tax_before_rebate: 33575
  rebate_computed: 16787.50
  rebate_given: 14787.50
  tax_payable_ya2026: 18787.50
  total_benefit: 16787.50
  tax_payable_ya2027: 33575
```

### Decision: hold a new company's shares personally or through a holding company

A founder incorporates a Singapore company in 2026. Its first YA is YA 2027 and chargeable income is $200,000. Should the founder hold the shares personally, or through an existing holding company that would own 100%?

Held personally (one individual shareholder, not investment holding or property development, resident): the start-up exemption applies. 75% of the first $100,000 is $75,000 and 50% of the next $100,000 is $50,000. Exempt amount $125,000. Tax is 17% of $75,000, which is $12,750.

Held 100% by a company: no individual holds 10% of the shares, so the start-up exemption fails and the partial exemption applies. Exempt amount $102,500. Tax is 17% of $97,500, which is $16,575.

On these facts the start-up exemption reduces pre-rebate tax by $3,825. The annual difference is $3,825 at chargeable income of at least $100,000 under the current bands. If both scenarios have at least that income in all 3 years and the personally held company satisfies the start-up conditions each year, the total pre-rebate difference is $11,475. From the fourth YA both scenarios use the partial exemption on the same ordinary chargeable income. Check other tax and commercial effects before choosing a structure.

```oa-check
name: New company, chargeable income 200,000, YA 2027, start-up exemption against partial exemption
inputs:
  chargeable_income: 200000
steps:
  startup_exempt: min(chargeable_income, 100000) * 0.75 + min(max(chargeable_income - 100000, 0), 100000) * 0.50
  startup_tax: (chargeable_income - startup_exempt) * 0.17
  partial_exempt: min(chargeable_income, 10000) * 0.75 + min(max(chargeable_income - 10000, 0), 190000) * 0.50
  partial_tax: (chargeable_income - partial_exempt) * 0.17
  saving_per_year: partial_tax - startup_tax
  saving_three_years: saving_per_year * 3
expected:
  startup_exempt: 125000
  startup_tax: 12750
  partial_exempt: 102500
  partial_tax: 16575
  saving_per_year: 3825
  saving_three_years: 11475
```

## When to refuse or refer

Refer to a qualified Singapore tax professional, and do not produce a filing figure, when:

- the company has a tax incentive, a concessionary rate, or is an insurer, shipping company, property developer, investment holding company or real estate investment trust;
- residency is in doubt (board decisions made outside Singapore, foreign-owned holding company);
- the facts suggest income was split across new companies to multiply the start-up exemption;
- shareholders changed and losses, capital allowances or donations are being carried forward, or a waiver of the shareholding test is needed;
- there is a group relief or carry-back claim, a foreign tax credit, a treaty rate, or a gain on a foreign asset in a cross-border group;
- the multinational group meets the top-up tax revenue test in step 8;
- the return is already late, IRAS has issued an estimated assessment, a composition offer or a summons, or an error in a past return needs voluntary disclosure.

For YA 2027, apply the baseline computation and verify any later relief before filing. Confirm chargeable income from the tax computation.

## Sources

| Source | URL | What was read | Read on |
|---|---|---|---|
| Income Tax Act 1947 | https://sso.agc.gov.sg/Act/ITA1947 | Read the cited provisions for income, exemptions, allowances, relief, procedural dates and offences, including sections 62, 76, 92L, 92M, 94A, 95, 96 and 96A | 2026-11-24 |
| Multinational Enterprise (Minimum Tax) Act 2024 | https://sso.agc.gov.sg/Act/MEMTA2024?ProvIds=pr8- | Section 8 revenue test and commencement | 2026-11-24 |
| Finance (Income Taxes) Act 2026 (Act 23 of 2026) | https://sso.agc.gov.sg/Acts-Supp/23-2026/Published | Commencement note for 4 November 2026, insertion of section 92M and the targeted changes to ordinary company provisions | 2026-11-24 |
| Budget 2026 statement, section B, paragraph 18(b) | https://www.singaporebudget.gov.sg/budget-speech/budget-statement/b-advance-our-refreshed-economic-strategy | Read for the 40% YA 2026 rebate as first announced. Read in a browser | 2026-11-20 |
| Budget 2026 Annex H-1, Tax Changes, item 1 | https://cms.singaporebudget.gov.sg/assets/11d18b8c-091c-4892-af60-0df181798814 | Read for the enhanced YA 2026 rebate and cash grant (7 April 2026 Ministerial Statement) and the local employee condition | 2026-11-20 |
| IRAS, Corporate Income Tax Rate, Rebates and Tax Exemption Schemes | https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes | Read for rate, rebate, cash grant, both exemption schemes | 2026-11-20 |
| IRAS, Basic Guide to Corporate Income Tax for Companies | https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/basic-guide-to-corporate-income-tax-for-companies | Read for basis period, YA, first YA, filing duties, record keeping | 2026-11-20 |
| IRAS, Tax Residency of a Company | https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/tax-residency-of-a-company-certificate-of-residence | Read for control and management test | 2026-11-20 |
| IRAS, Taxable and Non-Taxable Income | https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/taxable-non-taxable-income | Read for scope of charge, received in Singapore, capital gains | 2026-11-20 |
| IRAS, Companies Receiving Foreign Income | https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/companies-receiving-foreign-income | Read for foreign-sourced income exemption conditions | 2026-11-20 |
| IRAS, Business Expenses, and Tax Treatment of Business Expenses (M-R) | https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses | Read for deductibility tests, non-deductible list, motor vehicle expenses | 2026-11-20 |
| IRAS, Capital Allowances | https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances | Read for write-off methods, low-value assets, cars, deferral | 2026-11-20 |
| IRAS, Unutilised Items | https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/unutilised-items-(capital-allowances-trade-losses-donations) | Read for carry-forward and shareholding test | 2026-11-20 |
| IRAS, Loss Carry-Back Relief | https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-reliefs/loss-carry-back-relief | Read for 1 YA carry-back and the cap | 2026-11-20 |
| IRAS, Group Relief | https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-reliefs/group-relief | Read for conditions | 2026-11-20 |
| IRAS, Foreign Tax Credit | https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-reliefs/foreign-tax-credit | Read for credit limit and conditions | 2026-11-20 |
| IRAS, Estimated Chargeable Income (ECI) Filing | https://www.iras.gov.sg/taxes/corporate-income-tax/estimated-chargeable-income-(eci)-filing | Read for deadline, waiver, instalments | 2026-11-20 |
| IRAS, Overview of Form C-S/ Form C-S (Lite)/ Form C | https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-(lite)-form-c-filing/overview-of-form-c-s-form-c-s-(lite)-form-c | Read for which form | 2026-11-20 |
| IRAS, Corporate Income Tax Filing Season 2026 | https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-filing-season-2026 | Read for YA 2026 due date | 2026-11-20 |
| IRAS, Late filing or non-filing of Corporate Income Tax Returns | https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-(lite)-form-c-filing/late-filing-or-non-filing-of-Corporate-Income-Tax-Returns-form-c-s-form-c-s-(Lite)-form-c | Read for late filing consequences | 2026-11-20 |
| IRAS, Late payment or non-payment of Corporate Income Tax | https://www.iras.gov.sg/taxes/corporate-income-tax/corporate-income-tax-payment/late-payment-or-non-payment-of-corporate-income-tax | Read for late payment penalties | 2026-11-20 |
| IRAS, Penalties for Errors in Tax Returns | https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-(lite)-form-c-filing/penalties-for-errors-in-tax-returns | Read for penalty ranges | 2026-11-20 |
| IRAS, Types of Payment and Withholding Tax Rates | https://www.iras.gov.sg/taxes/withholding-tax/basics-of-withholding-tax/types-of-payment-and-withholding-tax-rates | Read for withholding rates, final tax conditions and phased royalty concession | 2026-11-24 |
| IRAS, Date of Payment or Deemed Payment | https://www.iras.gov.sg/docs/default-source/e-tax/etaxguide_determining-the-date-of-payment-or-deemed-payment-for-the-purpose-of-complying-withholding-tax-obligations.pdf | Actual or deemed payment dates, filing and payment deadline and late payment penalties | 2026-11-24 |
| IRAS, Payments Subject to Withholding Tax | https://www.iras.gov.sg/taxes/withholding-tax/payments-to-non-resident-company/payments-that-are-subject-to-withholding-tax | Services attributable to work performed in Singapore and prevailing corporate rate | 2026-11-24 |
| IRAS, Dormant Companies | https://www.iras.gov.sg/taxes/corporate-income-tax/dormant-companies-or-companies-closing-down/dormant-companies | Filing duty, simplified dormant return and waiver criteria | 2026-11-24 |
| IRAS, GloBE Rules and Domestic Top-up Tax | https://www.iras.gov.sg/taxes/pillar-2-top-up-taxes/global-anti-base-erosion-(globe)-rules-and-domestic-top-up-tax-(dtt) | Read for who the top-up taxes apply to | 2026-11-20 |

Not yet confirmed: a YA 2027 corporate income tax rebate or cash grant. The enacted baseline as at 22 November 2026 uses section 43, and section 92M provides the relief for YA 2026. Check for later YA 2027 relief at filing.

Not yet confirmed: the YA 2027 edition of the return forms. The 30 November 2027 date follows the IRAS annual filing rule as at the cutoff. Check the filing season notice and any specific waiver or extension.
