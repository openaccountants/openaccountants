---
name: fi-corporate-cross-border-tax
description: "Finland corporate cross-border income tax for tax year 2026. Covers Finnish company residence, effective management, foreign companies and permanent establishments, outbound dividends, interest, royalties and nonwage payments, foreign-tax credits and corporate exit taxation. Use for Finnish branches, overseas business income, withholding, residence certificates, treaty relief, credit carryforwards and asset or residence transfers. Distinguishes net-basis income tax from withholding and reporting, with ordinary computations and two executable examples. Read alongside the corporate, transfer-pricing and individual-residence skills; specialist fund, hybrid, restructuring and minimum-tax regimes require separate analysis."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/fi-corporate-cross-border-tax"
  jurisdiction: "FI"
  tax_year: "2026"
  last_updated: "2026-10-27"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Finland Corporate Cross-Border Tax v0.1

**Tax year:** 2026. Scope: ordinary commercial corporations, Finnish PEs and Finnish payers. Domestic law establishes a liability before a treaty or EU exemption restricts it. Independent source-review evidence and remaining publication gates are recorded in the [pack README](README.md); this skill does not establish worldwide-goal completion.

## Who this applies to

A Finnish-incorporated corporation is resident and taxable on worldwide income. A foreign corporation is also resident if its place of effective management is in Finland: the location where its board or other governing body makes its most important decisions on top-level daily management, considering the organisation and business facts together. A Finnish address or one meeting alone is not the complete test. A nonresident corporation is liable on Finnish-source income; a Finnish PE brings income attributable to that PE within Finnish taxation. [Income Tax Act 1535/1992, sections 9–10][ita].

Assess corporate residence before PE. For a nonresident, section 13a's domestic PE rule identifies a permanent business place, with examples such as a management place, branch, office, factory and workshop. Then apply the actual treaty's PE definition, agency provisions, construction/project threshold and any effective MLI changes. There is no universal six-month or 183-day exemption for a foreign company. Finnish immovable-property income and other section 10 source income require their own treaty classification even without a PE. [Income Tax Act, sections 10 and 13a][ita]; [Vero, nonresident corporations][pe].

Foreign funds require separate treatment, including the current section 9a management-company exception; this skill's ordinary-corporation route does not decide a fund's residence. A registered Finnish branch and an income-tax PE are different classifications. [Income Tax Act, sections 9–9a][ita].

## Rates, bands and thresholds

| Item | 2026 domestic rule | Primary source |
|---|---|---|
| Ordinary corporation / Finnish PE | 20% of taxable income; PE-attributable income is assessed on a net basis. | [Income Tax Act, section 124][ita]; [Nonresident Income Tax Act 627/1978, section 15][source-act] |
| Ordinary dividend or taxable interest/royalty to a nonresident corporation | 20% gross starting rate, subject to statutory exemptions, special recipient categories and treaties. | [Nonresident Income Tax Act, sections 3 and 7(1)(2)][source-act] |
| Unidentified recipient of listed-company nominee-registered dividend | 35% where the payer/intermediary lacks the required recipient information. | [Nonresident Income Tax Act, section 7(2)][source-act] |
| Nonwage compensation to a foreign corporation / partnership | 13% where withholding is required; determine Finnish work, register/card and treaty conditions first. | [Nonresident Income Tax Act, sections 7(1)(6), 10f][source-act] |
| Qualifying nonresident interest | Exempt under section 9(2), including specified deposits, debt securities and loans from abroad that are not equity-equivalent capital investments. | [Income Tax Act, section 9(2)][ita] |
| Foreign-tax-credit ceiling | Finnish tax attributable to eligible taxable foreign income, calculated by income source from net income after related costs/interest. | [Double Taxation Relief Act 1552/1995, sections 3–4][relief-act] |
| Unused eligible credit | Carry forward into the following five tax years; use oldest first, before current-year credit. | [Double Taxation Relief Act, section 5][relief-act] |
| Corporate exit income | Exit value less undepreciated tax acquisition cost, plus relevant reserve recapture; not a separate flat exit-tax percentage. | [Business Income Tax Act 360/1968, section 51e][business-act] |

The source-tax table is a starting classification. Section 7 includes special rates for specified investment-asset/pension recipients. Section 3 provides exemptions, including the qualifying EU parent-subsidiary route; sections 3b–3f address qualifying EU associated-company interest/royalty relief. A certificate showing an EU address does not establish every exemption condition. [Nonresident Income Tax Act][source-act].

## The base

### Permanent establishment and taxable business income

Work through each possible fixed place, including a home office or space regularly at the company's disposal, and establish geographical and temporal permanence and actual business activity there. A dependent agent habitually exercising authority to conclude contracts or receive orders can create a PE; check the actual treaty, including any broader effective agency wording. An independent agent acting in its ordinary business needs both legal and economic independence. Test the real business function before treating storage, information collection or another activity as preparatory/auxiliary; an essential part of the enterprise's business is not made auxiliary by its label. Construction thresholds vary by treaty, and connected projects require aggregation analysis. These are decision steps, not a universal safe harbour. [Income Tax Act, section 13a][ita]; [Vero, nonresident corporations, sections 3.2–3.5][pe].

Attribute the income and costs that an independent enterprise performing the PE's functions with its assets and risks would earn or incur. Reconcile the separate PE profit computation to head-office accounts, documented internal dealings and the Finnish return; do not tax all group turnover or merely use invoicing location. Related-entity pricing and PE attribution require separate factual analyses. [Income Tax Act, section 9(3)][ita]; [Assessment Procedure Act, section 31][assessment]; [Vero, nonresident corporations][pe].

For a resident Finnish company, determine foreign business profits, dividends and gains under the ordinary domestic tax-base rules before calculating relief. A foreign tax assessment does not prove the corresponding income is taxable in Finland or that every foreign charge is creditable. Participation exemptions, losses and interest limits belong in [corporate income tax](fi-corporate-income-tax.md). [Business Income Tax Act, sections 4, 6a–6b and 18a–18b][business-act].

### Outbound payments

Identify the legal recipient, residence, beneficial ownership, payment category, PE connection and payment/credit date. If ordinary corporate source taxation applies and no relief is proved, calculate gross payment multiplied by the domestic rate and give the recipient a withholding certificate. For a net-of-tax contract, determine the contractual gross-up before applying the rate. Treaty benefits require evidence before reduced withholding; nominee dividends use the separate intermediary rules. [Nonresident Income Tax Act, sections 7–10b][source-act].

For work performed in Finland, a Finnish payer or comparable foreign payer generally withholds 13% nonwage compensation tax from a foreign corporation unless valid prepayment registration or a 0% source-tax card removes collection. Evidence of treaty protection can suffice for other work, but construction, installation, shipbuilding, transport, cleaning, care/nursing and specified leased-workforce sectors require registration or a 0% card. A later registration alone does not prove withholding was unnecessary at payment. Tax withheld on PE business income is credited in assessment rather than automatically refunded. [Nonresident Income Tax Act, sections 7 and 10f][source-act]; [Vero, 2026 nonwage guidance][trade].

### Ordinary EU exemptions: record every condition

For the parent-subsidiary dividend exemption, establish that the recipient qualifies as a company under Directive 2011/96/EU article 2: a listed legal form, EU tax residence without third-country treaty residence, and liability without an option or exemption to the listed corporate tax. Record direct ownership of at least 10% of the payer's capital at distribution. Nonresident Income Tax Act section 3 implements this exemption; an indirect 10% interest or an EU postal address alone is insufficient. Apply the Directive's anti-abuse rule and domestic anti-avoidance provisions to non-genuine arrangements. EEA comparability and investment/pension/fund exemptions are distinct routes and require their own proof. [Nonresident Income Tax Act, section 3][source-act]; [Directive 2011/96/EU, articles 1–2 and Annex I][parent-directive].

For EU interest/royalty relief, identify the payment under section 3a and its actual beneficial owner. The owner must be a qualifying company in another EU state or its qualifying EU PE. The company must have a Directive-listed form, be subject without exemption to the relevant listed tax and be EU resident without third-country treaty residence. One company must directly hold at least 25% of the other's capital, or an EU company must directly hold at least 25% of each. For a PE, the debt/right must be actually connected with it and the receipt subject to the qualifying tax there; a third-country PE does not qualify. Keep ownership, legal-form, residence, tax-status and beneficial-owner evidence before applying zero withholding. [Nonresident Income Tax Act, sections 3a–3e][source-act].

### Foreign-tax credit and exemption

1. Establish the same income, period, foreign tax paid and its legal/treaty eligibility. Foreign tax above the treaty's permitted amount must be reclaimed from the source state; it is not automatically Finnish credit.
2. Calculate taxable foreign **net** income and the corresponding total taxable income within the income source. Section 4's limitation is the source's Finnish tax multiplied by the ratio of eligible taxable foreign net income to the source's taxable income. Exempt income is excluded. Do not divide gross foreign receipts by total turnover.
3. Apply confirmed, unexpired prior credits first; then current eligible credit, within the remaining limitation. Keep a five-year vintage schedule. A zero/loss tax base can prevent current utilisation.
4. Claim credit with supporting assessments/payment evidence and report later foreign-tax changes. If the treaty instead requires exemption, exclude that income; section 7 also addresses related expense/interest restrictions and its dividend exception.

[Double Taxation Relief Act, sections 3–5 and 7–9][relief-act]; [Vero, corporate relief][relief].

### Asset and residence transfers

Section 51e applies when Finland loses taxing rights through an asset transfer to a foreign PE, a foreign company's Finnish PE transferring assets to foreign headquarters/PE, a corporate tax-residence transfer (except assets effectively remaining with a Finnish PE), or transfer of a Finnish PE's business abroad. Compute each affected asset's arm's-length exit value less its remaining tax basis; recapture reserves that cease to be effectively connected to Finland. The 12-month return exception is limited to the statutory securities-financing, collateral, prudential-capital and liquidity transfers; it is not a general temporary-move exemption. [Business Income Tax Act, section 51e][business-act].

An eligible EU/qualifying EEA destination permits a request for payment over five years under section 50a; tax is not eliminated. Review the request deadline, interest, recovery-assistance condition and acceleration events such as onward disposal/transfer, insolvency or unpaid instalments. Inbound tax basis follows section 51f's rules; an automatic market-value step-up cannot be assumed for every non-EU inbound transfer. Cross-border reorganisations have separate sections 52e/52g/52i tests. [Business Income Tax Act, sections 51e–51f and 52e–52i][business-act]; [Assessment Procedure Act, section 50a][assessment]; [Vero, exit taxation][exit].

For an eligible exit deferral, section 50a preserves the original five-year clock even when tax is later imposed on appeal or reassessment. Request ordinary deferral before assessment closes; for later tax, request it before that tax's first due date. Security is possible where a demonstrable actual recovery risk exists. Deferral accelerates on disposal of the transferred assets/business, an onward move outside the EU other than a qualifying EEA recovery-assistance destination, bankruptcy/liquidation, or instalment default not cured within 12 months (six months for a second consecutive year of default). A taxpayer can terminate deferral voluntarily. Track each asset and instalment through the full period. [Assessment Procedure Act, section 50a][assessment].

## Deadlines and filing

| Obligation | Deadline / route | Official source |
|---|---|---|
| Corporate return | Within four months after the end of the accounting-period end month; follow the next-business-day rule. Resident corporations use 6B; nonresident corporations use 6U. | [Vero, corporate calendar][calendar]; [2025/2026 Form 6U instructions][form6u] |
| Foreign company's no-PE position | Where required, file 6U with Form 80, Account of local operations. A no-PE assertion does not by itself remove filing. A binding advance ruling can remove this filing route while facts remain unchanged, subject to authority requests. | [Vero, foreign-company income tax][foreign] |
| Foreign-tax relief | Claim through the corporate return / Form 70 with foreign income, tax and evidence. Later claims follow adjustment rules; report foreign-tax changes. | [Double Taxation Relief Act, sections 8–9][relief-act]; [Vero, corporate relief][relief] |
| Dividend/interest source tax | Collect when paid/credited; no collection when that recipient's same-payer monthly source tax is at most EUR 10. For a monthly tax period, report/pay by the next month's 12th; an approved quarterly period is due on the 12th of the second month after the quarter. Weekend/holiday due dates move to the next business day. | [Nonresident Income Tax Act, sections 8a–10][source-act]; [Vero, source-tax calendar][source-calendar] |
| Dividend/interest annual information return | Report the recipient/payment details by the end of January following the payment year, including relevant zero-withholding payments. This is separate from the tax-period return. | [Vero, payer procedure, section 6.4][payer] |
| Royalties / reportable trade income | Report royalties to nonresidents to the Incomes Register even with zero withholding; foreign-company trade income where reporting is required follows its own classification. Earnings payment report within five calendar days after payment, next business day if the fifth is a weekend/holiday. Tax payment remains a separate next-month 12th route for monthly employer taxes. | [Vero, payer procedure][payer]; [2026 nonwage guidance][trade]; [Incomes Register deadlines][ir-deadline]; [payment instructions][payment] |
| Excess dividend/interest/royalty source tax | Payer correction during the payment year, or corporate recipient refund application using Forms 6163/6167. Refund claim within three years after the payment calendar year ends. | [Nonresident Income Tax Act, section 11][source-act]; [Vero, corporate refund instructions][refund] |
| Exit-tax instalment request | Request before the exit year's assessment ends; later reassessment has its own timing route. Report on the income-tax return, with the asset/reserve computation. Form 80 is the foreign-operations form, not an exit-tax form. | [Assessment Procedure Act, section 50a][assessment]; [Vero, exit taxation][exit] |

Provide the recipient with a payment/source-tax certificate. Correct dividend/interest tax-period details by a replacement return for that period; correct royalty details in the Incomes Register. Do not make the recipient wait for the annual return to correct an identified error. In-kind distributions require a separate collection check: the tax base includes the in-kind amount but collection cannot exceed available cash; a recipient assessment can therefore be needed. [Vero, payer procedure, sections 6.1–6.4][payer].

## Penalties and interest

Corporate income-tax omissions follow Assessment Procedure Act sections 32–32b: the ordinary income-based increase is 2% of added income, with different statutory routes for aggravation, estimation, unclear cases and voluntary correction. A company's minimum is EUR 150, subject to the statutory exceptions; a relevant late filing before assessment closes uses the separate EUR 100 charge under section 33. Payer withholding/reporting failures have a separate self-assessed-tax regime, set out below. [Assessment Procedure Act][assessment]; [Vero, foreign-company filing][foreign].

In 2026 ordinary late-payment interest is 9.5% annually; interest with relief is a separate 4.5% route. Use the relevant assessment, type and period, not a single interest rate for every liability. Count actual calendar days from the day after the due date through payment; the 2026 denominator is 365. [Vero, interest][interest].

For dividend/interest self-assessed returns, Act 768/2016 sections 35–36 charge EUR 3 per day late, capped at EUR 135; after 45 days add 2% of the late positive tax. The **tax-based component** is capped at EUR 15,000 per tax type/period. A replacement return within 45 days has no late fee; later positive-tax corrections use the 2% component without another daily charge. Section 35 provides valid-reason/non-taxpayer-cause exceptions and prevents a late fee on tax subject to a tax increase. Under sections 37–38 a failure to collect source tax or a deficient return normally produces an increase of 10% of tax imposed, 15–50% for repeated/manifestly negligent failures, 25% on estimated tax or 3% in specified unclear/unreasonable cases; if no tax is imposed the maximum is EUR 200. Incomes Register late-report penalties follow their separate Act, not this self-assessed-return daily formula. [Self-assessed Tax Procedure Act, sections 35–38][self-act].

## Cross-border points

Apply the actual treaty, protocols, MLI effective provisions, beneficial-owner and anti-abuse conditions for the income and date. The official 2026 dividend/royalty table is an index to country rates, not proof of entitlement. In particular, the new Finland–France treaty applies starting in 2027; do not use its new provisions for a 2026 payment merely because the text has been signed or published. [Vero, 2026 treaty-rate index][rates]; [Vero, France commencement notice][france].

Domestic corporate residence and treaty residence need separate conclusions. VAT fixed establishment, payroll/employer status, social-insurance coverage, customs, TP/CbCR, CFC, hybrid and minimum-tax rules also have their own tests. Keep individual residence in [the individual skill](fi-individual-cross-border-residence.md). No universal treaty-rate schedule or specialist fund/reorganisation conclusion is supplied here.

## Two worked examples that recompute

**1. Ordinary corporate dividend source tax.** Assume a Finnish payer pays EUR 100,000 gross to an identified nonresident ordinary corporation, no PE attribution, no special recipient treatment and no proven statutory/EU/treaty relief. Domestic source tax at 20% is EUR 20,000, leaving EUR 80,000. Classification and entitlement are explicit assumptions, not decisions made by this arithmetic.

```oa-check
name: Finland ordinary corporate dividend source tax
inputs:
  gross_dividend: 100000
  domestic_source_rate: 0.20
steps:
  source_tax: gross_dividend * domestic_source_rate
  net_dividend: gross_dividend - source_tax
expected:
  source_tax: 20000
  net_dividend: 80000
```

**2. Corporate credit ceiling and prior-year ordering.** Assume one source with EUR 500,000 Finnish taxable net income including EUR 100,000 eligible foreign net income, Finnish tax before credit EUR 100,000, EUR 25,000 eligible current foreign tax and a usable EUR 5,000 prior credit. The cap is EUR 20,000. Use EUR 5,000 prior credit and EUR 15,000 current credit; EUR 10,000 current credit remains unused. This assumes tax/treaty eligibility, no exempt income or special hybrid limit, no other credits and a valid prior vintage.

```oa-check
name: Finland corporate foreign tax limitation and vintage ordering
inputs:
  source_taxable_net_income: 500000
  eligible_foreign_net_income: 100000
  finnish_tax_before_credit: 100000
  current_eligible_foreign_tax: 25000
  valid_prior_credit: 5000
steps:
  credit_ceiling: finnish_tax_before_credit * eligible_foreign_net_income / source_taxable_net_income
  prior_credit_used: min(valid_prior_credit, credit_ceiling)
  current_credit_used: min(current_eligible_foreign_tax, credit_ceiling - prior_credit_used)
  current_credit_unused: current_eligible_foreign_tax - current_credit_used
  finnish_tax_after_credit: finnish_tax_before_credit - prior_credit_used - current_credit_used
expected:
  credit_ceiling: 20000
  prior_credit_used: 5000
  current_credit_used: 15000
  current_credit_unused: 10000
  finnish_tax_after_credit: 80000
```

## Ask the client first

1. Where is the entity incorporated, where are its highest management decisions actually taken, and what treaty residence evidence exists?
2. What Finnish premises, staff, agents, contracts, projects and property produce the income, and on what dates?
3. What payment is made, who is its legal/beneficial recipient, and what PE, register, card, treaty or EU-relief evidence is valid at payment?
4. What foreign net income, deductions, paid foreign tax and confirmed credit vintages reconcile to the Finnish tax computation?
5. Will assets, a business or tax residence move, which Finnish taxing rights cease, and what valuations, reserves and destination conditions apply?
6. Which returns, authority requests, assessments, source-tax certificates and prior claims already exist, with what service and due dates?

## Sources

| Official source | Provisions / scope | Read on |
|---|---|---|
| [Income Tax Act 1535/1992][ita] | Sections 9–10, 13a, 124; residence, source, interest and PE | 2026-10-26 |
| [Nonresident Income Tax Act 627/1978][source-act] | Sections 3–3f, 7–11, 15; source-tax structure and rates | 2026-10-26 |
| [Business Income Tax Act 360/1968][business-act] | Sections 51e–51f; exit triggers, value, reserves, inbound basis | 2026-10-26 |
| [Double Taxation Relief Act 1552/1995][relief-act] | Sections 3–5, 7–9; credit, exemption, ordering and claims | 2026-10-26 |
| [Assessment Procedure Act 1558/1995][assessment] | Sections 32–33, 50a; sanctions, deferral conditions and acceleration | 2026-10-26 |
| [Self-assessed Tax Procedure Act 768/2016][self-act] | Sections 35–38; payer late filing and tax increases | 2026-10-26 |
| [Directive 2011/96/EU][parent-directive] | Articles 1–2, Annex I; parent-company qualification and anti-abuse | 2026-10-26 |
| [Vero, source-tax calendar][source-calendar]; [Incomes Register deadlines][ir-deadline]; [payment instructions][payment] | Tax-period/annual reporting, five-day earnings reports and payment dates | 2026-10-26 |
| [Vero, residence][residence]; [nonresident corporations][pe] | Administrative interpretation; English translations | 2026-10-26 |
| [Vero, corporate relief][relief] | Form 70, relief routes and foreign-tax evidence | 2026-10-26 |
| [Vero, payer procedure][payer]; [2026 nonwage guidance][trade] | Source collection, register/card exceptions, reporting routes | 2026-10-26 |
| [Vero, exit taxation][exit] | Finnish guidance, including deferral and tax-return request | 2026-10-26 |
| [Vero, foreign-company filing][foreign]; [Form 6U for 2025/2026][form6u]; [corporate calendar][calendar] | Return choice, no-PE account and ordinary dates | 2026-10-26 |
| [Vero, corporate refund instructions][refund] | Forms 6163/6167 and three-year refund period | 2026-10-26 |
| [Vero, interest][interest] | 2026 ordinary and relief rates | 2026-10-26 |
| [Vero, treaty-rate index][rates]; [France notice][france] | 2026 rate-table availability; new France treaty starts 2027 | 2026-10-26 |

Not yet confirmed: transaction-specific treaty/MLI entitlement and nonordinary fund, CFC, hybrid, restructuring and minimum-tax conclusions. Those specialist cases require a separately scoped analysis. Independent review of the ordinary procedures is recorded in the pack README; no professional attestation is claimed.

[ita]: https://www.finlex.fi/fi/lainsaadanto/1992/1535
[source-act]: https://finlex.fi/fi/lainsaadanto/1978/627
[business-act]: https://finlex.fi/fi/lainsaadanto/1968/360
[relief-act]: https://finlex.fi/fi/lainsaadanto/1995/1552
[assessment]: https://www.finlex.fi/fi/lainsaadanto/1995/1558
[residence]: https://www.vero.fi/en/detailed-guidance/guidance/95551/resident-and-nonresident-tax-liability-of-corporate-entities5/
[pe]: https://www.vero.fi/en/detailed-guidance/guidance/47806/income-taxation-of-nonresident-foreign-corporate-entities4/
[relief]: https://vero.fi/en/businesses-and-corporations/business-operations/international-operations/income-taxation-of-finnish-companies-in-other-countries/relief-for-double-taxatio/
[trade]: https://www.vero.fi/en/detailed-guidance/guidance/49136/paying-non-wage-compensation-to-a-non-resident-foreign-company2/
[payer]: https://www.vero.fi/en/detailed-guidance/guidance/108027/withholding-tax-at-source-on-dividends-interest-and-royalties-and-the-payors-obligations/
[exit]: https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/85299/maastapoistumisverotus2/
[foreign]: https://www.vero.fi/en/businesses-and-corporations/business-operations/foreign-business-in-finland/income-tax/
[form6u]: https://www.vero.fi/en/About-us/contact-us/forms/filling-instructions/6u-income-tax-return-foreign-corporate-entity-instructions-for-completing-the-tax-return-2025/
[calendar]: https://www.vero.fi/en/businesses-and-corporations/important_dates_and_deadlines_for_corporate_taxpayers/
[refund]: https://www.vero.fi/en/About-us/contact-us/forms/filling-instructions/form-6163e-enclosure-6167e-application
[interest]: https://www.vero.fi/en/individuals/payments/paying-taxes/interest-on-late-payments/
[rates]: https://www.vero.fi/en/detailed-guidance/guidance/49131/tax_rates_on_dividends_and_other_paymen/
[france]: https://www.vero.fi/en/About-us/newsroom/news/uutiset/2026/new-tax-treaty-between-finland-and-france-to-be-applied-starting-2027/

[self-act]: https://www.finlex.fi/fi/lainsaadanto/2016/768
[parent-directive]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02011L0096-20150217
[source-calendar]: https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/omaaloitteiset-verot/lahdevero-osingoista-osuuskunnan-ylijaamista-ja-koroista/
[ir-deadline]: https://vero.fi/en/incomes-register/companies-and-organisations/deadlines-for-reporting/
[payment]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/self-assessed-taxes/paying-self-assessed-taxes/

> Contributed by Michael Cutajar.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-27. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `fi-corporate-cross-border-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/fi-corporate-cross-border-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
