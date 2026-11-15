---
name: no-tax-overview
description: "Route a Norway tax question for income year 2026 to the owning skill: individual income, investments and gains, company tax, payroll, social contributions, VAT, residence, transfer pricing, formation and the Switzerland wealth/exit corridor. Establish entity, period, residence, income and requested job before loading a computation. This router keeps rates, allowances, thresholds and dates in their owning skills. Trigger on Norway tax overview, how does tax work in Norway, Norwegian tax system, which Norwegian tax skill, skattemelding, formuesskatt, trinnskatt, merverdiavgift."
version: 0.3
jurisdiction: "NO"
category: international
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: router
---

# Norway Tax Overview

## Scope

Use this as the entry point for a Norway tax job for income year 2026. It selects the method and handoff; it does not compute a liability or repeat another skill’s rates. The ordinary calendar-year rule and permitted accounting-year exception are in [Tax Administration Regulation § 8-2-2](https://lovdata.no/dokument/SF/forskrift/2016-11-23-1360/*). The selected owner must establish the client’s actual period, taxpayer type, residence and applicable regime.

## Ask the client first

- What result is needed: explanation, computation, registration, return, payment, correction or a relocation decision?
- Which income period and entity/person, with which domestic and treaty residence facts?
- What income, activity, assets, employees, foreign transactions and registrations are involved?
- Which original documents, prior returns, assessments and payment records already answer those questions?
- Which submitter has authority, what event is time-sensitive, and what remains unsupported?

## The method, step by step

1. Read the available records and identify the requested job. Do not ask for information already supplied or infer a legal form from a bank narration.
2. Fix the period and taxpayer category. Separate an individual’s ordinary income, personal income and wealth, an employer’s payroll liabilities, a company’s income and a VAT return. They are separate bases and obligations.
3. Resolve domestic/treaty residence before applying a full-year resident method. The [Tax Act §§ 2-1 to 2-3](https://lovdata.no/dokument/NL/lov/1999-03-26-14/*) sets different individual/company and resident/non-resident scope; the owning residence skill carries the conditions.
4. Select the owning skill below. Load any linked companion needed for the same facts, then read its Scope, intake, method, exceptions and Sources. A router result is not evidence that a computation has been completed.

| Requested topic | Route and boundary | Owning skill | Where to continue |
|---|---|---|---|
| Tax year and currency | Confirm the income year and any permitted accounting-year exception. Keep the income period separate from the following return/assessment year. Amounts use Norwegian kroner. | [no-income-tax](no-income-tax.md) | Scope; Currency and rounding |
| Authority and channels | Skatteetaten administers tax; the selected method names its service and current submission authority. Brønnøysundregistrene owns company-register and annual-accounts filings. A tax return and an accounts filing are separate. | [no-company-formation](no-company-formation.md) | Submit and follow up |
| Resident versus non-resident scope | Determine domestic residence, treaty position, arrival/departure timing and Norwegian-source items before choosing an income or investment calculation. Do not apply a full-year resident computation to another profile. | [no-individual-residence](no-individual-residence.md) | Who this applies to; The base; Cross-border points |
| Presence tests and leaving Norway | Use the residence owner for rolling presence windows, the long-resident tail, available dwellings, close relatives and the holiday-home exception. Physical relocation alone does not settle tax residence. | [no-individual-residence](no-individual-residence.md) | The base; Deadlines and filing |
| Ordinary individual income and regional components | Keep ordinary net income apart from gross personal income. The owner’s computation scope is a full-year Norwegian-resident ENK owner, with or without wages/pension; it refuses part-year, non-resident and dual-resident profiles. For an employee without an ENK, it supplies component reference only: obtain the separate employee method before a complete assessment. Establish local rates and northern-area eligibility. | [no-income-tax](no-income-tax.md) | Tax on alminnelig inntekt; Two income bases |
| Bracket tax | Use the income-year schedule once on the correct combined personal-income base, with the owner’s scope restrictions. Do not apply the bracket schedule to net ordinary income. | [no-income-tax](no-income-tax.md) | Trinnskatt on personinntekt |
| National insurance and the low-income limit | Establish scheme membership, age and income type; use the social-contribution owner for the phase-in limitation, combined-income treatment and employer liability. Tax residence alone does not decide membership. | [no-social-contributions](no-social-contributions.md) | Who this applies to; Trygdeavgift; Cross-border points |
| Salary marginal rate | Load the individual and social component references together. The income owner’s ENK scope does not provide a complete method for an employee without an ENK. Keep marginal rate distinct from average tax and distinguish the employee result from the employer’s total cost. | [no-income-tax](no-income-tax.md) | Rates, bands and thresholds; Computation order |
| Personal allowance and minimum deductions | Use the owner’s year-specific allowance, salary/pension deduction caps, combined-income restriction and business-income prohibition. Missing personal facts are unresolved inputs. | [no-income-tax](no-income-tax.md) | Allowances and fixed deductions; Expenses |
| Business income, assets and losses | For an ENK, bridge the accounts to ordinary business income and calculated personal income separately. Preserve asset elections, shield inputs and the separate loss schedules. | [no-income-tax](no-income-tax.md) | Næringsinntekt; Beregnet personinntekt; Depreciation; Losses |
| Pensions and special reductions | The income owner identifies pension credit and tax-limitation parameters but does not compute them. Refer the affected calculation; do not treat listed parameters as a completed pension method. | [no-income-tax](no-income-tax.md) | Allowances and fixed deductions; Operational hold |
| Trial employment deduction | Establish actual selection and eligible facts before using the income owner’s trial deduction. It is not a general allowance for everyone in the age group. | [no-income-tax](no-income-tax.md) | Allowances and fixed deductions |
| Dividends and share gains | Use the investment owner for the shareholder model, usable shielding, uplift, losses, lots and reporting; an account’s product name does not determine tax treatment. | [no-capital-gains](no-capital-gains.md) | Share shielding and estimated tax; Return completion and corrections |
| Other investments, property and crypto | Select the actual asset/account branch before applying any capital rate, exemption or loss rule. Ordinary custody, ASK, funds, insurance accounts, property and virtual assets have different methods. | [no-capital-gains](no-capital-gains.md) | The method, step by step; Worked cases |
| Company income tax | Use the company owner for ordinary versus financial-sector treatment, participation exemption, interest limitation, depreciation, group contributions, losses and special-sector boundaries. | [no-corporate-income-tax](no-corporate-income-tax.md) | Rates, bands and thresholds; The taxable base |
| Company residence | Establish incorporation, board-level/day-to-day management and the treaty exception. A shareholder’s move and a company’s residence require separate conclusions. | [no-corporate-income-tax](no-corporate-income-tax.md) | Who this applies to; Cross-border points |
| Outbound dividend withholding | Identify recipient type, residence, beneficial ownership and treaty/EEA entitlement before selecting a withholding result. A domestic headline does not establish treaty relief. | [no-corporate-income-tax](no-corporate-income-tax.md) | Cross-border points |
| Employer contributions | Use the employer’s registration zone, activity, membership and aid position; reduced zones and allowances are conditional. Keep employer contributions apart from employee withholding. | [no-employer-payroll](no-employer-payroll.md) | Rates, bands and thresholds; The base |
| Pay run and reporting | Use the payroll owner for tax cards, withholding breaks, PAYE, payment after payday and the a-melding. Do not use the employer-contribution cycle as the withholding-payment cycle. | [no-employer-payroll](no-employer-payroll.md) | The base; Deadlines and filing |
| VAT rates and registration | Norwegian VAT is separate from EU intra-community rules. The VAT owner supplies supply classification, ordinary/special registration, rates, input restrictions and cross-border treatment. | [no-vat-return](no-vat-return.md) | Who this applies to; Rates, bands and thresholds; Cross-border points |
| VAT return preparation | For the reconciliation workflow, preserve registration transition, invoice/import evidence, access checks, period selection, correction and payment records. The legal conditions and mid-year service changes control over older guidance wording. | [norway-mva](norway-mva.md) | The method, step by step; When to refuse or refer |
| Personal and company returns | Select the actual taxpayer category and period: the income owner’s workflow covers full-year resident ENK owners; employees without an ENK and its refused residence profiles need a separate method. Use the corporate owner for companies. Keep submission, correction and assessment comparison in the handoff. | [no-income-tax](no-income-tax.md); [no-corporate-income-tax](no-corporate-income-tax.md) | Deadlines and filing |
| Advance and final payments | Use the owning individual/company schedule, notice timing, acceleration on default, credits and settlement rules. Do not copy a return date into a payment field. | [no-corporate-income-tax](no-corporate-income-tax.md) | Deadlines and filing; see also no-income-tax for individuals |
| Net wealth tax and spouses | The Norwegian part of the corridor covers the resident wealth calculation, municipal-rate condition, spouse thresholds and year-end condition. Its Swiss treaty conclusions do not apply to other destinations. | [norway-to-switzerland-wealth-tax-exit](norway-to-switzerland-wealth-tax-exit.md) | Part 1; Part 2; When to refuse or refer |
| Wealth valuation and debt | Use the Norwegian valuation rules for the actual share/property class and valuation date, with debt adjustments. The current home-law amendment controls over an older advance-tax summary. | [norway-to-switzerland-wealth-tax-exit](norway-to-switzerland-wealth-tax-exit.md) | Part 1: Valuation; Sources |
| Business-wealth payment deferral | Keep the eligible asset scope, minimum deferred liability, interest periods and final due event together. A payment deferral does not remove the wealth tax. | [norway-to-switzerland-wealth-tax-exit](norway-to-switzerland-wealth-tax-exit.md) | Part 1: New in 2026; Sources |
| Interest and enforcement | Use the domain owner for the liability, relevant half-year interest, fine basis, exceptions and procedural conditions. A late payment, missing return and incorrect return are different events. | [no-corporate-income-tax](no-corporate-income-tax.md) | Penalties and interest; use VAT/payroll owners for those domains |
| Exit and Norway-Switzerland planning | Identify the event date and covered assets before choosing the historic/current exit regime. The corridor retains Norwegian and Swiss residence, treaty, wealth, company and lump-sum branches with their stated source boundaries. | [norway-to-switzerland-wealth-tax-exit](norway-to-switzerland-wealth-tax-exit.md) | The method, step by step; Worked cases; Sources |
| Related-party pricing | Map related parties and PE dealings, then apply the transfer-pricing owner’s statement, documentation, exemption and CbC tests independently of the corporate tax computation. | [no-transfer-pricing](no-transfer-pricing.md) | Who this applies to; The taxable base; Deadlines and filing |
| Start a business | Choose legal vehicle, funding, directors, required registrations and annual follow-up using the formation owner. An NUF or partnership needs its own branch; do not assume every enterprise is an AS. | [no-company-formation](no-company-formation.md) | Entity choice and legal parameters; Submit and follow up |

5. Follow the selected owner’s computational order and current official sources. Where a rule changed during the year, establish the transaction/event date before selecting a branch. Do not choose between contradictory statements by convenience: reconcile them against the operative statute and preserve the result.
6. Build a handoff that separates confirmed records, computed amounts, elections, unresolved inputs and tasks still requiring another method. Where an owner has an operational hold or does not compute the requested taxpayer profile, carry that boundary forward explicitly.
7. For an actual filing, use the owner’s service, authorisation, period and confirmation steps. Retain the submitted return, assessment comparison, payment reference and evidence. This router supplies no authority to file or pay.

### What to return

Return the requested job and period; the chosen owner and necessary companions; the facts/documents that selected the branch; the exact calculation or workflow still to perform; unresolved source or client inputs; and the records needed to prove completion. If the request spans domains, give an ordered handoff with a separate result for each liability. Keep rates and dates in their owning skills so a partial fetch cannot mix incompatible versions.

### Coverage limits carried forward

The income owner is limited to full-year Norwegian-resident ENK owners, with or without wages/pension. It refuses part-year, non-resident and dual-resident profiles and has a cross-border refusal; employees without an ENK need another complete method. Its component tables do not expand that scope. The pack’s self-employed income workflow carries an explicit operational hold. It identifies pension credit and tax limitation without computing them, and the final annual business shielding rate is not supplied before publication. The corridor does not provide every destination’s treaty result, cantonal rates, immigration permission or a final case-specific wealth assessment during the domestic residence tail. The formation method does not establish a case-specific licence or bank acceptance. Those are disclosed gaps, not completed outputs.

The older overview’s numeric topics have destinations in the table: residence, ordinary income and regional components, brackets, national insurance, marginal salary rate, allowances, shares, company/withholding tax, employer contributions, VAT, returns, advance payments, wealth rates/spouses/valuation/deferral and interest remain in their owners. The per-file old-topic map preserves the original figures and exact destination anchors for review.

## When to refuse or refer

- Do not calculate from a headline alone, from another income year, from a future budget proposal, or without a material residence/entity/transaction fact.
- Do not apply the Norwegian company or individual method to Svalbard, petroleum or another excluded special regime. Fishing, farming and seafarer deductions need the regime-specific work identified by the income owner.
- A foreign residence, PE, treaty, unusual investment wrapper, restructuring or disputed classification needs the relevant cross-border or specialist method before filing.
- Do not invent an unpublished annual rate, treat a pre-filled return as confirmed, or turn the router’s handoff into a filing-ready assessment.

## Sources

| Actual scope read | Official URL | Read on |
|---|---|---|
| Read for individual/company domestic residence, worldwide/limited scope and relevant exceptions: Tax Act §§ 2-1 to 2-3 | https://lovdata.no/dokument/NL/lov/1999-03-26-14/* | 2026-11-15 |
| Read for ordinary calendar year, accounting-year exception, filing categories and separate VAT periods: Tax Administration Regulation §§ 8-2-2, 8-2-3 and 8-3-1 | https://lovdata.no/dokument/SF/forskrift/2016-11-23-1360/* | 2026-11-15 |
| Read for current emigration/global reporting instructions and claim: Skatteetaten | https://www.skatteetaten.no/en/person/to-from-norway/from/tax-when-you-move-abroad/tax-emigration/ | 2026-11-15 |

Not yet confirmed: inheritance/gift-tax conclusions, which the old overview also left unread; the final annual shielding rate for income year 2026; and every client-specific entitlement or live filing field not established by the selected owner. This router does not independently re-attest the passing siblings or resolve their stated source boundaries.
