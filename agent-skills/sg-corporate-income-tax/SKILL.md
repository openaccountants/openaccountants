---
name: sg-corporate-income-tax
description: "Corporate income tax in Singapore for a company, for Year of Assessment 2027 (financial year ending in 2026), with Year of Assessment 2026 figures alongside where a relief is set year by year. Covers the 17% rate, the preceding-year basis, what income is taxed, the foreign-sourced income exemption, the partial tax exemption, the start-up exemption, the YA 2026 corporate income tax rebate and cash grant, deductions, capital allowances, losses, group relief, one-tier dividends, ECI, Form C-S, Form C-S (Lite), Form C, instalments and penalties. Use for: how is my Singapore Pte Ltd taxed, Singapore company tax rate, corporate tax Singapore, start-up tax exemption, partial tax exemption, CIT rebate, ECI filing, Form C-S deadline, tax on company profit Singapore. Out of scope: sole proprietors and partners (sg-income-tax), GST (singapore-gst, sg-gst-return), CPF (sg-cpf-medisave), forming the company (singapore-formation), individual residency (sg-tax-residency), capital gains detail (sg-zer"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sg-corporate-income-tax"
  jurisdiction: "SG"
  tax_year: "2026"
  last_updated: "2026-11-20"
---

# Singapore Corporate Income Tax v1.0

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
7. For the YA 2026 cash grant: did the company make CPF contributions in 2025 for at least one local employee who is not a shareholder-director.
8. Is the company part of a group with consolidated revenue of EUR 750 million or more.

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
| Subject to tax | The income was subject to tax of a similar character to income tax in the territory it is received from. For a dividend, the underlying tax paid by the paying company counts | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/companies-receiving-foreign-income) |
| Headline rate | The highest corporate tax rate of that territory is at least 15% at the time the income is received in Singapore | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/companies-receiving-foreign-income) |
| Benefit | The Comptroller is satisfied the exemption is beneficial to the company | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/companies-receiving-foreign-income) |

Other foreign income (interest, royalties, rent) is taxable when received, with a foreign tax credit under step 8.

### 3. Compute chargeable income [ITA sections 14 and 15](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr14-)

Start from accounting profit and adjust.

**Deductible.** Section 14(1) allows "all outgoings and expenses wholly and exclusively incurred during that period by that person in the production of the income". IRAS reads this as four tests: incurred solely to produce income, actually incurred (the legal liability has arisen), revenue and not capital in nature, and not prohibited by the Act. Source: [IRAS, business expenses](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses).

**Not deductible** [ITA section 15(1)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr15-):

| Item | Rule | Source |
|---|---|---|
| Private or domestic expenses | Section 15(1)(a) | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses) |
| Capital expenditure, including the cost of incorporating the company and buying fixed assets | Section 15(1)(c). Claim capital allowances instead where they exist | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses) |
| Depreciation and amortisation | Add back. Claim capital allowances instead | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses) |
| Private cars (S-plated) and business cars (Q-plated or RU-plated, registered on or after 1 April 1998) | Section 15(1)(k). No deduction for running costs, even when the car is used for business and even when paid as a reimbursement. Goods and commercial vehicles (vans, lorries, buses) are deductible | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses/tax-treatment-of-business-expenses-(m-r)) |
| Donations | Not a business expense. Approved donations are relieved separately | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses) |

Revenue expenses incurred up to 1 year before the deemed date of commencement of business are deductible. Earlier set-up costs are not. Source: [IRAS basic guide](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/basic-guide-to-corporate-income-tax-for-companies).

**Capital allowances** [ITA sections 19 and 19A](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr19A-). Claimed on plant and machinery used in the trade. The company chooses the method per asset:

| Method | What is allowed | Source |
|---|---|---|
| 1 year, computers and prescribed automation equipment (section 19A(2)) | 100% of cost | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances) |
| 1 year, low-value assets (section 19A(10A)) | 100% of cost for an asset costing not more than $5,000. Total claim for all low-value assets capped at $30,000 per YA | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances) |
| 3 years (section 19A(1)) | One third of cost each year, for any qualifying asset | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances) |
| Working life (section 19) | Initial allowance of 20% of cost, then the other 80% spread evenly over a working life of 6, 12 or 16 years as elected | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances) |

The 2-year write-off applied only to assets acquired in the basis periods for YA 2021, YA 2022 and YA 2024. It is not available for YA 2026 or YA 2027 purchases. No capital allowance is given on private cars (S-plated) or business cars (Q-plated, RU-plated), unless registered and used as private hire cars or for driving instruction. Vans, lorries and motorcycles qualify. A claim can be deferred to a later YA. On sale of an asset, compute a balancing allowance or balancing charge.

**Unutilised losses, capital allowances and donations** [ITA sections 23 and 37](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr37-). Brought-forward losses must be set off first; the company cannot hold them back to make more use of an exemption. A capital allowance claim can be deferred.

| Item | Carry forward | Conditions | Source |
|---|---|---|---|
| Trade losses | Indefinitely | Shareholding test | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/unutilised-items-(capital-allowances-trade-losses-donations)) |
| Capital allowances | Indefinitely | Shareholding test, and the company carries on the same trade or business | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/unutilised-items-(capital-allowances-trade-losses-donations)) |
| Approved donations | Up to 5 YAs | Shareholding test | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/unutilised-items-(capital-allowances-trade-losses-donations)) |

Shareholding test: the same persons must hold 50% or more of the shares on two dates. For losses and donations the dates are the last day of the year in which the loss was incurred and the first day of the YA in which it is deducted (section 37(12) and (14)). For capital allowances they are the last day of the YA in which the allowance arose and the first day of the YA of deduction (section 23(4)). Look through to the shareholders of the ultimate holding company. If the test fails, the items are lost unless the Minister waives the test because the change was not for a tax benefit (sections 23(5) and 37(16)).

**Carry-back** [ITA section 37D](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr37D-). Current-year unutilised capital allowances and trade losses can be carried back 1 YA, to the immediately preceding YA. The maximum is $100,000. Capital allowances go first, then losses. The shareholding and same-business tests apply, and the company must claim it. Source: [IRAS, loss carry-back relief](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-reliefs/loss-carry-back-relief).

**Group relief** [ITA section 37B](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr37B-). Current-year unutilised capital allowances, trade losses and donations can be transferred to another group company if both companies:

- are incorporated in Singapore;
- are in the same group: one beneficially holds at least 75% of the ordinary shares of the other, or a third Singapore-incorporated company holds at least 75% of each. Holdings through a foreign company are ignored;
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
- have its total share capital beneficially held directly by no more than 20 shareholders throughout the basis period, where either all are individuals, or at least one is an individual holding at least 10% of the issued ordinary shares.

Excluded whatever the shareholding, under [ITA section 43(11)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr43-), for a company incorporated on or after 26 February 2013: a company that "undertakes property development in the basis period for that year of assessment, whether or not that is the only activity it carries out", and a company whose "only activity in that basis period is the holding of investments". The same applies where the company is a partner of a partnership that does either. IRAS words the two exclusions as companies whose principal activity is investment holding and companies that undertake property development for sale, for investment, or both. Both still get the partial exemption. A foreign company or its branch cannot claim the start-up exemption. A sole proprietorship or partnership converted into a company can claim it if the conditions are met. IRAS audits companies set up to split an existing business's income across shell companies. Source: [IRAS, exemption schemes](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes).

Tax payable before rebate = (chargeable income less the exempt amount) at 17%, less foreign tax credit and other set-offs.

### 5. Corporate income tax rebate and cash grant [ITA section 92M](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr92M-)

A rebate is set one year at a time: announced in the Budget, then written into the Act as its own section (section 92L for YA 2025, section 92M for YA 2026). Never carry one year's rebate into another year.

| YA | CIT Rebate | Cash grant | Cap on rebate plus grant | Source |
|---|---|---|---|---|
| 2026 | 50% of tax payable | $2,000 | $40,000 | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes); ITA section 92M(1) and (3) |
| 2027 | None announced as at 20 November 2026; the Act has no section for YA 2027 | None announced | Not applicable | See "Not yet confirmed" under Sources |

How YA 2026 got to these figures: the Budget 2026 statement (paragraph 18(b)) gave a 40% rebate, a minimum benefit of $1,500 and a cap of $30,000. Budget 2026 Annex H-1, item 1, records the update announced in the 7 April 2026 Ministerial Statement: a 50% rebate, a minimum benefit of $2,000 and a total maximum of $40,000 per company. Both sets are for the same YA 2026; the second replaced the first. The enhanced figures are the law: section 92M, inserted by the Finance (Income Taxes) Act 2026 (Act 23 of 2026, in force 4 November 2026), remits "50% of the tax payable for that year of assessment" less "the cash grant of $2,000", up to "$40,000, less the cash grant of $2,000". IRAS applies the same figures.

Rules for YA 2026:

- The rebate goes to every taxpaying company, resident or not. It is computed on tax payable after set-offs such as foreign tax credit. It does not apply to income subject to a final withholding tax: section 92M(1)(a) leaves out tax levied under section 43(3), (3A), (3B) and (3C).
- The cash grant goes to an active company that met the local employee condition: it made CPF contributions in calendar year 2025 for at least one Singapore citizen or permanent resident employee, not counting shareholders who are also directors (section 92M(3) and (7): the definition of employee "excludes any individual who is a shareholder and also a director of the company"). No grant is paid to a company that, at the time of payment, is not carrying on a trade or business, is in liquidation, is in receivership over all its property, or has ceased to exist (section 92M(4)). The grant is exempt from tax (section 92M(6)).
- A company that gets the cash grant: if 50% of tax is $2,000 or less, no rebate is given. If it is more, the rebate is the 50% amount (capped at $40,000) less $2,000 (section 92M(1) and (2)).
- A company that does not get the cash grant: the rebate is the 50% amount, capped at $40,000.
- IRAS computes the rebate automatically. Do not deduct it in the ECI or the return.
- A company that met the condition but did not receive the grant (for example staff hired through a group company) can appeal by myTax Mail by 30 November 2026.

For YA 2027, compute tax with no rebate and tell the client that a rebate, if any, would be announced in Budget 2027.

### 6. Dividends and capital gains [ITA section 13(1)(za)](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr13-)

**One-tier system.** The company's tax is final. Section 13(1)(za) exempts "any dividends paid on or after 1 January 2008 by any company resident in Singapore". The shareholder pays no further Singapore income tax on the dividend. The IRAS withholding tax rate table has no line for dividends.

**Capital gains.** There is no general capital gains tax. IRAS: "Capital gains are not taxable", for example gains on the sale of fixed assets. Whether a gain is capital or trading income is a question of fact (the badges of trade). Use [sg-zero-cgt](sg-zero-cgt.md) for that test and for the section 13W equity disposal rule. Source: [IRAS, taxable and non-taxable income](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/taxable-non-taxable-income).

**Gains on foreign assets** [ITA section 10L](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr10L-). An exception to the rule above. A gain from the sale of an asset situated outside Singapore, sold on or after 1 January 2024, is taxed as income when the gain is received in Singapore, if the seller is an entity of a "relevant group". A group is a relevant group if its entities are not all incorporated in one jurisdiction, or any entity has a place of business in more than one jurisdiction. An "excluded entity" with adequate economic substance in Singapore is outside the rule (other than for intellectual property). A Singapore company whose group is all in one jurisdiction, with no place of business elsewhere, is outside the definition of a relevant group as read. If the client is in a cross-border group and sold a foreign asset, refer.

### 7. File and pay

**Estimated Chargeable Income (ECI)** [ITA section 63](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr63-). File within 3 months from the end of the financial year. State ECI before the partial or start-up exemption; IRAS applies it.

| ECI rule | Figure | Source |
|---|---|---|
| Deadline | 3 months from the financial year end | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/estimated-chargeable-income-(eci)-filing) |
| Waiver, both needed | Annual revenue of $5 million or below, and ECI is nil | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/estimated-chargeable-income-(eci)-filing) |

Revenue here is the main income source, not interest or other separate-source income. The waiver is self-assessed; there is nothing to send to IRAS. The waiver does not remove the duty to file the return.

**The return.** Every company files Form C-S, Form C-S (Lite) or Form C by 30 November each year, even with no income or a loss. Filing is electronic at mytax.iras.gov.sg.

| Form | Who can use it | Documents | Source |
|---|---|---|---|
| Form C-S | Incorporated in Singapore; annual revenue of $5 million or below; only income taxable at 17%; not claiming carry-back relief, group relief, investment allowance, foreign tax credit or tax deducted at source | Keep accounts and tax computation; send only if asked | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-(lite)-form-c-filing/overview-of-form-c-s-form-c-s-(lite)-form-c) |
| Form C-S (Lite) | Meets the Form C-S conditions and has annual revenue of $200,000 or below | Same as Form C-S | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-(lite)-form-c-filing/overview-of-form-c-s-form-c-s-(lite)-form-c) |
| Form C | Every other company | File financial statements and tax computation with the form | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-(lite)-form-c-filing/overview-of-form-c-s-form-c-s-(lite)-form-c) |

One-tier exempt Singapore dividends and foreign income exempt under section 13(8) do not stop a company using Form C-S. A foreign tax credit claim does: it needs Form C.

**Payment** [ITA section 85](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr85-). Tax is payable within one month after the notice of assessment is served, even if the company objects. An objection must be filed within 2 months from the date of the notice.

**Instalments.** A Singapore-registered company that pays by GIRO can pay its ECI tax by instalments. The earlier it files, the more instalments:

| ECI filed within | Instalments | Source |
|---|---|---|
| 1 month from financial year end | 10 | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/estimated-chargeable-income-(eci)-filing) |
| 2 months | 8 | same |
| 3 months | 6 | same |
| After 3 months | None | same |

File by the 26th of the month to count for that month. The minimum monthly GIRO deduction is $50.

**Penalties.**

| Failure | Consequence | Source |
|---|---|---|
| Tax not paid by the due date (section 87) | 5% penalty on the unpaid tax | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/corporate-income-tax-payment/late-payment-or-non-payment-of-corporate-income-tax) |
| Still unpaid 60 days after the 5% penalty | A further 1% for each completed month, up to 12% of the unpaid tax | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/corporate-income-tax-payment/late-payment-or-non-payment-of-corporate-income-tax) |
| Return not filed by the due date (section 94A(1)) | IRAS may issue an estimated assessment (pay within 1 month), offer composition of up to $5,000 per offence, or summon the company. On conviction, a fine of up to $5,000 | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-(lite)-form-c-filing/late-filing-or-non-filing-of-Corporate-Income-Tax-Returns-form-c-s-form-c-s-(Lite)-form-c) |
| Return not filed for 2 years or more (section 94A(3)) | On conviction, a penalty of twice the tax assessed and a fine of up to $5,000 | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-(lite)-form-c-filing/late-filing-or-non-filing-of-Corporate-Income-Tax-Returns-form-c-s-form-c-s-(Lite)-form-c) |
| Director does not comply with a notice under section 65B(3) (offence under section 65C) | Fine of up to $10,000, or imprisonment of up to 12 months, or both | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-(lite)-form-c-filing/late-filing-or-non-filing-of-Corporate-Income-Tax-Returns-form-c-s-form-c-s-(Lite)-form-c) |
| Incorrect return without reasonable excuse or through negligence (section 95(2)) | Penalty of double the tax undercharged (IRAS: up to 200%); fine of up to $5,000; imprisonment of up to 3 years. Where there is no negligence, section 95(1) sets a penalty equal to the tax undercharged | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-(lite)-form-c-filing/penalties-for-errors-in-tax-returns) |
| Wilful intent to evade tax (section 96) | Penalty of treble the tax undercharged; fine of up to $10,000; imprisonment of up to 3 years | [ITA section 96](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr96-) |
| Serious fraudulent evasion: false books or records, or "any fraud, art or contrivance" (section 96A) | Penalty of 4 times the tax undercharged (IRAS: up to 400%); fine of up to $50,000; imprisonment of up to 5 years | [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-(lite)-form-c-filing/penalties-for-errors-in-tax-returns) |

Keep records for at least 5 years from the relevant YA.

### 8. Cross-border pointers

**Withholding tax on payments to non-residents** [ITA sections 45 and 45A](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr45-). The paying company withholds and files by the 15th of the second month from the date of payment.

| Payment to a non-resident | Rate | Source |
|---|---|---|
| Interest, commissions and fees in connection with a loan | 15% | [IRAS](https://www.iras.gov.sg/taxes/withholding-tax/basics-of-withholding-tax/types-of-payment-and-withholding-tax-rates) |
| Royalties for the use of movable property such as intellectual property | 10% | same |
| Rent for the use of movable property | 15% | same |
| Technical assistance, service and management fees to a non-resident company | Prevailing corporate income tax rate, which is 17% | [IRAS rates table](https://www.iras.gov.sg/taxes/withholding-tax/basics-of-withholding-tax/types-of-payment-and-withholding-tax-rates) and [IRAS rate page](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes) |
| Remuneration of a non-resident director | 24% | [IRAS](https://www.iras.gov.sg/taxes/withholding-tax/basics-of-withholding-tax/types-of-payment-and-withholding-tax-rates) |

The 15% and 10% rates apply to the gross payment and are a final tax, where the non-resident earns the income through operations outside Singapore. If the operations are carried on in Singapore, the prevailing corporate rate applies to a non-individual. A tax treaty may lower the rate; the return must still be filed. Test first whether the payment is within the withholding rules at all, and get the treaty and a certificate of residence before using a lower rate. Late payment under section 45: a 5% penalty, then 1% per completed month up to 15%.

**Foreign tax credit.** For foreign income that is taxed in Singapore, a resident company gets a credit equal to the lower of the foreign tax paid and the Singapore tax on the same income (net of expenses). It is given under a treaty (double tax relief) or unilaterally where there is no treaty. A company in a loss position gets no credit. Claim it in Form C. Source: [IRAS, foreign tax credit](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-reliefs/foreign-tax-credit).

**Transfer pricing.** Related-party transactions must be at arm's length. Use [singapore-transfer-pricing](singapore-transfer-pricing.md).

**Global minimum tax** [Multinational Enterprise (Minimum Tax) Act 2024](https://sso.agc.gov.sg/Act/MEMTA2024). Enacted. For financial years beginning on or after 1 January 2025, Singapore charges a multinational enterprise top-up tax (the income inclusion rule) and a domestic top-up tax, to a minimum rate of 15%. They apply only to a multinational group whose consolidated revenue is EUR 750 million or more in at least 2 of the 4 financial years before the year in question. The undertaxed profits rule has not been implemented. A small or medium company outside such a group is not affected. If the client is in such a group, refer. Source: [IRAS, GloBE rules and DTT](https://www.iras.gov.sg/taxes/pillar-2-top-up-taxes/global-anti-base-erosion-(globe)-rules-and-domestic-top-up-tax-(dtt)).

## Boundary and exception table

| Situation | Action |
|---|---|
| Company in its first 3 YAs | Test every start-up condition for that YA: incorporated in Singapore, resident, 20 shareholders or fewer, the individual-shareholder test, and not investment holding or property development. If any fails, use the partial exemption. |
| All shares held by a company | Start-up exemption fails (no individual holds 10%). Partial exemption applies. |
| Loss or nil income in a first-3 YA | The YA still counts toward the 3. No exemption is carried forward. |
| Losses or capital allowances brought forward and shareholders changed | Run the 50% shareholding test on the two dates before deducting anything. |
| YA 2027 computation | No rebate. Do not reuse the YA 2026 rebate or cash grant. |
| Cash grant company with tax of $4,000 or less for YA 2026 | 50% of the tax is $2,000 or less, so no rebate is given on top of the $2,000 grant (derived from the IRAS rule). |
| Car costs | S-plated, Q-plated and RU-plated cars: add back running costs and claim no capital allowance. |
| Foreign dividend, branch profit or service income received | Test the three section 13(9) conditions. If one fails, tax it and claim a foreign tax credit. |
| Payment to a non-resident | Withholding question first. It is separate from the company's own tax. |
| Concessionary rate, incentive, insurer, shipping, property developer, investment holding company | Refer. The ordinary computation here does not apply as it stands. |
| Group with EUR 750 million revenue | Top-up tax applies. Refer. |

## Worked cases

All amounts are in Singapore dollars and are illustrative inputs. No foreign income, no incentives, no losses brought forward.

### Established small company, YA 2026, with the partial exemption and the rebate

A trading company in its sixth year has chargeable income of $300,000 for YA 2026 (financial year ended 31 December 2025). It paid CPF for two local employees in 2025, so it gets the cash grant.

1. Partial exemption: 75% of the first $10,000 is $7,500. 50% of the next $190,000 is $95,000. Exempt amount $102,500.
2. Income taxed at 17%: $300,000 less $102,500 is $197,500. Tax is $33,575.
3. Rebate: 50% of $33,575 is $16,787.50, under the $40,000 cap. Because the company gets the $2,000 cash grant, the rebate given is $16,787.50 less $2,000, which is $14,787.50.
4. Tax payable: $33,575 less $14,787.50 is $18,787.50. The $2,000 grant is paid to the company separately, so the total YA 2026 benefit is $16,787.50.

The same income for YA 2027 gives tax of $33,575, because no rebate has been announced for YA 2027.

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

The figure that decides it: holding personally saves $3,825 for the year. The saving is the same $3,825 at any chargeable income of $100,000 or more, and it is available for the first 3 YAs only, so at most $11,475 over the 3 years. If the holding structure is worth more than that to the founder for other reasons, the tax cost is known. From the fourth YA both routes give the same tax.

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
- the group meets the EUR 750 million threshold for the top-up taxes;
- the return is already late, IRAS has issued an estimated assessment, a composition offer or a summons, or an error in a past return needs voluntary disclosure.

Do not apply a rebate to YA 2027. Do not treat cash in the bank as chargeable income. This skill does not authorise filing, payment or an election.

## Sources

| Source | URL | What was read | Read on |
|---|---|---|---|
| Income Tax Act 1947, current version (site banner: as at 21 Nov 2026) | https://sso.agc.gov.sg/Act/ITA1947 | Read for Sections 10(1), 10(25), 10L, 13(1)(za), 13(8) to (10), 14(1), 15(1), 19, 19A, 23, 37, 37B, 37D, 43 (including 43(11)), 45, 45A, 63, 65B(3), 65C, 85, 87, 92M, 94, 94A, 95, 96, 96A. The list of sections has no rebate section after 92M. Read in a browser; the site does not answer curl | 2026-11-20 |
| Multinational Enterprise (Minimum Tax) Act 2024, current version | https://sso.agc.gov.sg/Act/MEMTA2024 | Read for Sections 7, 8, 11, 12. Read in a browser | 2026-11-20 |
| Finance (Income Taxes) Act 2026 (Act 23 of 2026) | https://sso.agc.gov.sg/Acts-Supp/23-2026/Published | Read for the long title, and for its commencement note on section 92M of the Income Tax Act (4 November 2026). The rest of the Act was not read | 2026-11-20 |
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
| IRAS, Types of Payment and Withholding Tax Rates; WHT Filing and Payment Due Date | https://www.iras.gov.sg/taxes/withholding-tax/basics-of-withholding-tax/types-of-payment-and-withholding-tax-rates | Read for withholding rates and due date | 2026-11-20 |
| IRAS, GloBE Rules and Domestic Top-up Tax | https://www.iras.gov.sg/taxes/pillar-2-top-up-taxes/global-anti-base-erosion-(globe)-rules-and-domestic-top-up-tax-(dtt) | Read for who the top-up taxes apply to | 2026-11-20 |

Not yet confirmed: any corporate income tax rebate or cash grant for YA 2027. None is in the Budget 2026 statement, its Annex H-1, the IRAS rebate page or the Income Tax Act (the last rebate section is 92M, for YA 2026) as read on 20 November 2026; the Budget for 2027 has not been delivered.

Not yet confirmed: the YA 2027 edition of the return forms, and whether the Finance (Income Taxes) Act 2026 changes anything in this skill beyond section 92M. The sections cited above were read in the current version of the Income Tax Act, which includes that Act, but the amending Act itself was not read in full. The 30 November 2027 due date is the IRAS "30 Nov each year" rule applied to YA 2027.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-20. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sg-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sg-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
