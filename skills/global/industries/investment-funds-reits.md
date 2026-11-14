---
name: investment-funds-reits
description: "Cross-country fund, manager and investor tax method for 2026, including enacted UK carried-interest changes, UK REIT distributions, PFIC handoffs and explicit limits on unconfirmed country figures."
version: 1.0
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - corporate-income-tax-workflow-base
category: vertical
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: cross-country-method
---

# Investment funds and REITs v1.0

## Scope

A cross-country method for an accountant considering a regulated investment fund, hedge fund, private equity fund, mutual fund, real estate investment trust or fund manager in 2026. Separate the vehicle, manager, general partner and each investor. Regulation as UCITS or an AIF does not itself determine tax transparency, exemption, treaty entitlement or investor reporting.

Use `corporate-income-tax-workflow-base` and the current country jobs for the actual return. This is not fund formation, AIFMD authorisation, MIFID II compliance, investment advice or an investment management agreement. No global table establishes eligibility for a tax concession.

## Quick reference

| Question | Required distinction | Source |
| --- | --- | --- |
| Is UK carried interest still governed only by the old capital-gains description? | For 2026-27 and later, apply the enacted deemed-trade provisions; qualification changes the amount included, not a universal final tax rate | [ITTOIA 2005, sections 23I-23R, inserted by Finance Act 2026 section 58](https://www.legislation.gov.uk/ukpga/2005/5/part/2) |
| What must a UK REIT distribute? | Separate PIDs received from other UK REITs from the rest of its relevant property-rental profits | [HMRC IFM22050, CTA 2010 section 530](https://www.gov.uk/hmrc-internal-manuals/investment-funds/ifm22050) |
| Are UK PIDs always paid gross? | Ordinary PIDs are subject to deduction at the basic rate; an applicable exception needs its own evidence | [HMRC IFM28005](https://www.gov.uk/hmrc-internal-manuals/investment-funds/ifm28005) |
| Is every investment entity outside top-up tax? | Identify the exact excluded-entity category and parent status; do not equate an investment entity with an excluded investment-fund parent | [HMRC MTT10210, Finance (No. 2) Act 2023 section 127](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt10210) |

## Ask the client first

- What are the complete ownership chart, governing documents, regulatory permissions, residence, fiscal year and tax classifications in every relevant country?
- Which entity owns each asset, bears its risks, signs contracts, receives distributions and performs investment-management services?
- Which investors are individuals, companies, pension funds, charities, sovereign bodies or other funds? Obtain their residence, beneficial-owner and tax-status evidence.
- Are any investors subject to US tax or another country's anti-deferral rules? Are there PFIC, CFC, hybrid or treaty concerns?
- What elections, rulings, investor declarations, withholding exemptions, information statements and prior returns exist? Obtain the actual conditions and dates rather than the product's marketing description.
- How are management fees, performance allocations, carried interest, co-investment returns, expenses, capital contributions, equalisation, redemptions and clawbacks distinguished?
- For a property vehicle, what are the income and asset composition, development activity, distribution obligations and actual distributions?

## The method, step by step

1. Build the legal and cash-flow map. Keep fund-level income, manager fees, partner allocations, investor distributions and withholding in separate schedules. A feeder and master do not become a single taxpayer merely because they invest together.
2. Classify the legal vehicle separately under each relevant tax law. A transparent partnership can allocate taxable income before cash is distributed. An opaque company can face entity tax as well as investor tax. An investor may have current anti-deferral income without receiving a distribution. Neither label alone proves the final timing, exemption or rate.
3. Establish whether the fund qualifies for a particular exemption or special regime. Check legal form, regulated status, eligible investments, investor restrictions, filing duties, elections and continuing conditions. Do not infer tax exemption from UCITS, AIF, REIT or an exchange listing.
4. Reconcile accounting results to the vehicle's taxable or reportable amounts. Separate interest, dividends, rents, disposals, derivatives, foreign exchange, expenses and capital transactions. Apply the particular country's treatment and current year; do not reuse another country's distribution deduction.
5. Determine each investor's classification, allocation, withholding and reporting separately. Check source-country taxation, treaty eligibility, beneficial ownership, residence-country credits and relief, anti-deferral and hybrid rules. Non-residence does not by itself prove that no exit or withholding tax applies.
6. Analyse management compensation independently of investor returns. Identify services, employment/securities treatment, a genuine investment return, carried interest and disguised fixed remuneration. A payment called carry is not necessarily statutory carried interest. Match the applicable date, residence, work locations, holding-period tests and elections before computing tax.
7. Test every REIT's entry and continuing conditions using that country's law. Distinguish income and asset tests, permitted development, shareholder/ownership restrictions, listing or institutional-investor alternatives, distribution categories and deadlines. Compute actual tax-measure profits rather than multiplying accounting cash flow by a generic percentage.
8. Run the top-up-tax scope analysis for each group member. Record whether an exclusion depends on ultimate-parent status and whether subsidiaries qualify independently. Separate excluded entities, investment-entity computation rules, consolidation and domestic top-up differences.
9. Prepare reconciliations to filed returns, withholding certificates and investor statements. Record unconfirmed conditions before presenting a relief as available. Obtain review by an appropriately credentialed fund-sector practitioner before a filing or restructuring recommendation.

## Fund forms and regulatory routes

Retain the following as classification questions, not automatic tax outcomes:

| Structure or regime | What to establish before using a tax treatment |
| --- | --- |
| US LP or LLC, UK partnership, Cayman exempted LP, Irish ILP | Legal entity and tax classification in the fund and investor jurisdictions; elections and anti-deferral interaction |
| Luxembourg SCSp, SIF, RAIF and SICAR | Partnership or corporate form, actual elected regime, eligible assets, subscriptions, distributions and the conditions of each exemption |
| Luxembourg SICAV or FCP, Irish ICAV, French FCP or SICAV, UK unit trust | Regulatory status, legal form and separate fund/investor tax rules; a common contractual fund is not automatically treated identically abroad |
| UCITS under Directive 2009/65/EC | Confirm the current regulatory route and local tax law. The directive's name is not a tax exemption certificate |
| AIF under Directive 2011/61/EU, including hedge, private equity, property, infrastructure and hybrid funds | Confirm the applicable definition, authorisation or registration and separate tax regime. Do not assume all AIFs are transparent or low-tax |
| French FCPR or SLP, ELTIF, German Investment Tax Act arrangements | Obtain the actual law, eligible-investor and investment conditions for the relevant year before applying special treatment |

Current vehicle-specific country figures in the prior edition have not been re-established for this global method. They are explicitly held below, so they cannot silently become a 2026 filing calculation.

## United Kingdom: carried interest from 2026-27

The enacted rule in ITTOIA 2005 section 23I treats the relevant individual as carrying on a trade. Subject to the statutory definitions and exclusions, the included profit is the non-qualifying profit plus **72.5% of qualifying profit**. This is a taxable-profit inclusion factor, not a capital-gains rate or the person's complete tax and National Insurance bill. The Finance Act 2026 commencement applies for **2026-27 and subsequent years**, including services performed before that year. [ITTOIA sections 23I-23R and commencement annotation](https://www.legislation.gov.uk/ukpga/2005/5/part/2).

Apply the permitted-deduction rule in section 23N, including allocation between qualifying and non-qualifying amounts and amounts already used. Do not deduct ordinary management expenses indiscriminately: section 23N restricts what can reduce this deemed profit. Earnings and employment-related-securities taxation, the irrevocable section 23J election, deceased-individual rules, temporary non-residence, anti-avoidance and double-taxation provisions require separate review where relevant.

Qualification is determined under Schedule A1, not by calling every private-equity return qualifying. Work-location and residence facts are also separate. Section 23K apportions the deemed trade using applicable workdays, with specific non-resident exclusions. Do not assume UK residence, UK source or an employment classification from a supplied tax pack.

The HMRC page IFM37120 still describes the capital-gains framework despite its recent manual update date. It does not override the later operative law. Use the actual year and enacted provisions, not the freshness of a web page's header. [HMRC IFM37120, historical framework](https://www.gov.uk/hmrc-internal-manuals/investment-funds/ifm37120).

### Worked case: included profit, not final tax

Fabricated pounds. Assume the legal classification, period, permitted deductions, source and full qualifying status have already been established. Qualifying carry is 100,000 and the permitted deduction attributable to it is 4,000. Non-qualifying carry is 20,000 with a separately attributable permitted deduction of 1,000. The resulting included profit is 88,600. Compute the person's actual income tax and applicable contributions separately, with their other income and reliefs. This example does not determine qualification.

```oa-check
name: UK carried interest included profit after allocated permitted deductions
inputs:
  qualifying_carry: 100000
  qualifying_deduction: 4000
  nonqualifying_carry: 20000
  nonqualifying_deduction: 1000
  qualifying_factor: 0.725
steps:
  qualifying_profit: qualifying_carry - qualifying_deduction
  nonqualifying_profit: nonqualifying_carry - nonqualifying_deduction
  included_profit: qualifying_profit * qualifying_factor + nonqualifying_profit
expected:
  qualifying_profit: 96000
  nonqualifying_profit: 19000
  included_profit: 88600
```

Boundary: non-qualifying profit is not multiplied by the qualifying factor. Before using the deduction inputs, verify section 23N and its allocation rule. A loss, clawback, earlier election or foreign workday can require additional analysis; this case supplies none of those facts.

## United Kingdom: REIT distributions

The general distribution condition requires **100% of PIDs received from other UK REITs** and **at least 90% of the rest of the relevant UK property-rental profits**, using the statutory tax measure. Capital gains do not have a general compulsory-distribution requirement. The condition is tested for each accounting period and ordinarily met by the CTSA filing date. The principal company, rather than every subsidiary separately, has the group distribution obligation. Legal impediment and other specific exceptions need evidence. [HMRC IFM22050](https://www.gov.uk/hmrc-internal-manuals/investment-funds/ifm22050).

Distinguish a PID from an ordinary company dividend. PIDs are generally paid under deduction of basic-rate income tax; a valid gross-payment exception must be established, not assumed for all investors. A PID may include property gains as well as rental profits, and investors' eventual liabilities can differ. [HMRC IFM28005](https://www.gov.uk/hmrc-internal-manuals/investment-funds/ifm28005).

The former claim of a universal non-resident-investor cap is not established and must not be used. The old shorthand about a particular institutional ownership percentage, listing, asset composition and rental-income tests is held for a full current UK REIT eligibility check. Distribution compliance does not prove that all other REIT conditions are met.

## United States: investor and REIT handoff

This global method preserves the US questions but does not expand the US library or provide a new numeric US computation:

- Determine whether a non-US corporation is a PFIC under the current income or asset test, including applicable exceptions and overlap rules. Do not assume that every foreign fund is a corporation or that holding an interest through a partnership eliminates the issue.
- Compare the default excess-distribution/disposition regime with an available QEF or mark-to-market election. Check eligibility, timing, annual information, basis adjustments, loss limits and prior taint. Do not promise that a late election erases every earlier charge.
- Obtain an actual PFIC Annual Information Statement where required for QEF reporting; a marketing factsheet is not a substitute. Review active-insurance exceptions with the insurance-sector job.
- Review section 1061 carried-interest holding periods and exceptions against actual assets and dispositions. Do not label all short-term returns ordinary employment income or quote a single individual's final marginal rate.
- For a US REIT, check the separate qualifying income, asset, distribution, ownership and election tests under the current Internal Revenue Code, not the former compressed percentage string. Investor dividend treatment, section 199A and a fund-level distribution deduction require separate current analysis.

All numeric US tests and rates from the former edition are held pending the relevant current US job and sources. The former references to sections of an “ITA” are not usable statutory citations for the US Internal Revenue Code.

## Other REIT and investor regimes

- **France:** preserve SIIC and OPCI classification, rental/gain distribution conditions, exemption scope and investor taxation. Do not use the former SIIC percentages without current official law.
- **Germany and Netherlands:** identify the actual domestic property-investment regime, eligibility and taxation. Remove the unsupported German listed-vehicle census as an eligibility fact; the size of a market does not establish a tax result.
- **Spain:** preserve SOCIMI listing, asset/income, distribution, reinvestment and special-levy questions. Different levies can have different triggers; do not label one historic rate a universal charge on every dividend.
- **Singapore:** identify S-REIT tax transparency, the actual distribution condition, relevant income and unitholder categories. A listing and a distribution alone do not prove that every receipt or investor is exempt.
- **Japan:** preserve J-REIT investment-corporation status, distribution-deduction conditions and investor treatment. “Zero corporate tax” is not the starting conclusion.
- **Australia:** preserve listed or stapled trust/company analysis, managed-investment-trust eligibility and AMIT attribution. A stapled company does not become transparent simply because the trust is, and attribution can differ from cash paid.

## Blockers, anti-deferral and hybrid structures

Draw the actual structure before advising. A US corporate blocker below a partnership, a Cayman or BVI company above offshore assets, a Luxembourg SICAV/SCSp structure and a master/feeder can create different tax, withholding and reporting results. Do not interchange them.

Treat blocking effectively connected income, tax-exempt-investor exposure, CFC and PFIC analysis as questions to test. Inserting an opaque company does **not** automatically convert ordinary income into capital gains, prevent CFC attribution or avoid PFIC status. It may create additional entity tax, withholding, reporting or anti-avoidance exposure. Substantiate commercial purpose and analyse treaty benefits, substance, beneficial ownership, ATAD II/hybrid mismatches and exit consequences using current country law. No restructuring recommendation is made by this global file.

For UK top-up-tax scope, investment funds and REITs have an excluded-entity route linked to ultimate-parent status, including the specified case where consolidation statements are not produced. Subsidiaries do not inherit a blanket exclusion. Revenue of an excluded entity can still matter to the group threshold. Separate the domestic top-up rules and any elections. [HMRC MTT10210](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt10210).

## Output and self-checks

- Provide the ownership/classification chart, vehicle-level computation, manager/carry analysis, investor-by-investor allocation/withholding and reporting schedule.
- Record regulatory status separately from tax eligibility. Name the law and year beside each relief, election and country figure.
- Reconcile statutory distribution profits to accounting profit, cash and actual distributions. Distinguish PIDs received, own rental profits, gains and non-PID dividends.
- Check PFIC, QEF, mark-to-market and CFC issues only after classifying both the investor and entity. Record missing statements and election deadlines.
- Do not complete a client return, certify exemption or recommend a blocker while material conditions remain unresolved. Flag every held or judgment-dependent item for the sector reviewer.
- Preserve supporting statements, source dates, rulings and computations. Explain the effect of an unconfirmed condition rather than silently supplying an old percentage.

## Sources

| Official source | Read date | Read scope |
| --- | --- | --- |
| [UK ITTOIA 2005, Part 2](https://www.legislation.gov.uk/ukpga/2005/5/part/2) | 2026-11-14 | Read for sections 23I-23R, permitted deductions, work-location rules and the Finance Act 2026 commencement annotation; Schedule A1 qualification requires a separate facts-specific check |
| [HMRC IFM37120](https://www.gov.uk/hmrc-internal-manuals/investment-funds/ifm37120) | 2026-11-14 | Read for the older capital-gains description and its conflict with the operative 2026-27 legislation; not treated as overriding law |
| [HMRC IFM22050](https://www.gov.uk/hmrc-internal-manuals/investment-funds/ifm22050) | 2026-11-14 | Read for the two UK REIT distribution categories, timing, capital gains and exceptions, not every REIT eligibility condition |
| [HMRC IFM28005](https://www.gov.uk/hmrc-internal-manuals/investment-funds/ifm28005) | 2026-11-14 | Read for PID versus non-PID distributions and basic-rate deduction; individual gross-payment exceptions not established here |
| [HMRC MTT10210](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt10210) | 2026-11-14 | Read for excluded entities, ultimate-parent investment funds/REITs, subsidiary conditions, revenue inclusion and domestic-tax distinction |

Not yet confirmed: Luxembourg UCITS subscription-tax rates/exemptions, SIF/RAIF/SICAR/SCSp elections and investor treatment; Irish ICAV/UCITS/ILP exit-tax exemptions and declarations under current TCA provisions; French FCP/SICAV/FCPR/SLP and SIIC/OPCI figures; UK fund and full REIT listing/ownership/asset conditions and gross-PID exceptions; German and Dutch regimes; Spanish SOCIMI percentages and special levies; Singapore S-REIT and Japanese J-REIT distribution/eligibility figures; Australian MIT/AMIT and stapled-company details; US section 1061, PFIC/QEF/mark-to-market and REIT/section 199A numeric tests and current exceptions; France/Italy/Germany/Spain carried-interest treatment; detailed UK Schedule A1 carried-interest qualification, contribution liabilities and any final effective rate; jurisdiction-specific treaty, blocker, CFC, hybrid and non-UK top-up-tax treatment. The former German market census is unsupported and is not a tax rule. These are held topics, not confirmed 2026 rates or instructions to claim relief.
