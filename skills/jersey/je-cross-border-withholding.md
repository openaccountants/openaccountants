---
name: je-cross-border-withholding
description: >
  Jersey cross-border individual tax and collection rules for 2026, covering
  residence, non-resident income exemptions, landlord deductions and treaty
  relief checks. Use for Jersey non-resident withholding, foreign income,
  short-term business visitors, rental agents or double taxation relief.
  Identifies payment categories and statutory conditions before any rate
  is applied, and distinguishes collection from final liability. Includes
  a bounded rental-agent deduction example. Treaty-specific benefits,
  corporate transfer pricing and complete relief calculations require
  further primary evidence. This source-cited draft awaits professional
  review and does not support a blanket statement that Jersey has no
  withholding or taxes no foreign income.
jurisdiction: JE
category: international
tax_year: 2026
tier: 2
type: situation-rules
last_updated: 2026-11-14
version: 1.1
depends_on:
  - workflow-base
  - cross-border-workflow-base
---

# Jersey cross-border income and withholding

Tax year: the 2026 year of assessment. Currency is GBP. Authority: Revenue Jersey. Law: Income Tax (Jersey) Law 1961, Article 118B.

## Who this applies to

The [residence guidance](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/IncomeTaxCircumstances/Pages/ResidencyForJerseyTax.aspx) distinguishes ordinarily resident worldwide liability, resident but not ordinarily resident Jersey income and remittances, and non-resident Jersey-source liability. Retaining available accommodation, habitual visits, contract changes, arrival and departure can affect the result. Do not use nationality, immigration status or a single day count as a complete residence test.

This guide covers individuals receiving Jersey income while not resident, and the payers, agents and tenants who collect tax from them. Company residence and corporate tax are in `je-corporate-income-tax`; resident individuals are in `je-income-tax`.

## Rates, bands and thresholds

| 2026 item | Rate or amount | Conditions | Source |
|---|---|---|---|
| Non-resident income tax on Jersey income | 20% | Salary, self-employment, property income and most pension income; non-resident tax relief may apply | [Tax on your Jersey income if you live abroad](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/IncomeTaxCircumstances/pages/nonresidencytax.aspx) |
| Managing agent deduction from a non-resident landlord's rent | 20% of net rental income | Legal obligation on the agent; a valid good compliance certificate or a Revenue Jersey notice can change it | same |
| Tenant deduction threshold, no agent | Rent of GBP 25,000 or more per year | Tenant ordinarily deducts at 20%; Revenue Jersey can issue a deduction notice below that amount | same |
| Short-term business visitor | No more than 60 days in the assessment year | Employment income exception; whole or part days counted; conditions in Article 118B | [Income Tax Law, Art. 118B](https://www.jerseylaw.je/laws/current/l_29_1961) |
| Dividends with tax deducted under Article 88(3) | 10% | Treated separately by Article 118B; verify both provisions | same |

## The base

For each payment, record the recipient's residence, payer, source, payment category, company profit history where relevant, treaty and evidence of any clearance.

[Income Tax Law, Article 118B](https://www.jerseylaw.je/laws/current/l_29_1961) exempts specific non-resident income, including qualifying bank deposit interest, interest paid by a Jersey resident company, specified pension and annuity income, patent royalties and qualifying trust distributions. Company distributions and preference dividends have profit-source conditions; the ordinary zero-taxed-profit exemption is not a general exemption for all dividends. MCIT-taxed MNE dividends have a separate provision. Article 118B also treats dividends with 10% deducted under Article 88(3) separately. Verify both provisions before determining a dividend's deduction or final liability.

Article 118B provides an employment-income exception for a qualifying short-term business visitor present for no more than 60 days in the assessment year, counting whole or part days. It also addresses employer tax registration and return deductions. Business licensing, social contributions and treaty questions remain separate.

The [non-resident landlord guidance](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/IncomeTaxCircumstances/pages/nonresidencytax.aspx) requires a managing agent to deduct 20% of net rental income. Without an agent, the tenant ordinarily deducts at 20% if annual rent is GBP 25,000 or more; Revenue Jersey can issue a deduction notice below that amount. A valid good compliance certificate can permit payment without deduction, while the landlord remains responsible for tax.

## Deadlines and filing

The landlord collection, employer registration and return deductions follow the Revenue Jersey notices and Article 118B. A good compliance certificate is applied for by a landlord who has consistently complied; it usually lasts one year. Payment and return dates for agents and tenants are not set out in the captured pages; see Not yet confirmed.

## Penalties and interest

Income-tax return and payment penalties are in [je-income-tax-compliance](je-income-tax-compliance.md). This guide sets no separate penalty.

## Cross-border points

1. Determine domestic liability and the relevant payment-category exemption before applying a treaty.
2. Check whether the agreement is a full or partial double taxation agreement, its entry into force and its effective date for the relevant tax.
3. Read the actual residence, income, relief and anti-abuse provisions, including protocols. An agreement listing alone does not establish a benefit.
4. Obtain required certificates, claims and supporting evidence; reconcile foreign tax relief with the Jersey assessment.
5. For taxation contrary to an agreement, inspect the applicable mutual agreement procedure and its time limits.

Primary directories distinguish [full agreements](https://www.gov.je/TaxesMoney/InternationalTaxAgreements/DoubleTaxation/Pages/FullDoubleTaxation.aspx) and [partial agreements](https://www.gov.je/TaxesMoney/InternationalTaxAgreements/DoubleTaxation/Pages/PartialDoubleTaxation.aspx). The [mutual agreement procedure](https://www.gov.je/TaxesMoney/InternationalTaxAgreements/DoubleTaxationProcedure/pages/treatydisputes.aspx) supplies the dispute route. A tax information exchange agreement does not by itself confer double-tax relief.

## Two worked examples that recompute

**Example 1: managing agent, net rent GBP 10,000.** GBP 10,000 of established net rent received by a managing agent, with no valid certificate or special notice, produces a GBP 2,000 deduction and GBP 8,000 remittance to the landlord. This is collection under the [landlord guidance](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/IncomeTaxCircumstances/pages/nonresidencytax.aspx), not a computation of rental profit or a final assessment. Follow any applicable Revenue Jersey notice instead of the ordinary example.

```oa-check
name: Jersey 2026 non-resident landlord, agent collects 20% of GBP 10,000 net rent
inputs:
  net_rent: 10000
  rate: 0.20
steps:
  - deduction: net_rent * rate
  - remitted: net_rent - deduction
expected:
  deduction: 2000
  remitted: 8000
```

**Example 2: does the agent deduct, or does a certificate apply?** An agent collects GBP 18,000 of rent and pays GBP 3,000 of established allowable expenses, so net rent is GBP 15,000 (derived). Without a certificate the agent deducts GBP 3,000 (derived) and remits GBP 12,000 (derived). With a valid good compliance certificate the agent pays the full GBP 15,000 without deduction, and the landlord still accounts for the tax on assessment. Whether the expenses are allowable is a separate question; this example assumes it is established.

```oa-check
name: Jersey 2026 non-resident landlord, deduction with and without a good compliance certificate
inputs:
  rent: 18000
  expenses: 3000
  rate: 0.20
steps:
  - net_rent: rent - expenses
  - deduction_no_certificate: net_rent * rate
  - remitted_no_certificate: net_rent - deduction_no_certificate
  - remitted_with_certificate: net_rent
expected:
  net_rent: 15000
  deduction_no_certificate: 3000
  remitted_no_certificate: 12000
  remitted_with_certificate: 15000
```

## Ask the client first

1. Where is the recipient resident and ordinarily resident for 2026, and since when?
2. What is the payment (salary, rent, interest, dividend, pension, royalty, trust distribution) and who pays it?
3. For rent: is there a managing agent, what is the annual rent, and is there a good compliance certificate or Revenue Jersey notice?
4. For employment: how many whole or part days was the person present in Jersey in the year?
5. For dividends: from what profits was the dividend paid, and was 10% deducted under Article 88(3)?
6. Which treaty, if any, is claimed, and what certificates are held?

## Sources

Complete dividend deduction mechanics, annual payments, treaty-specific rate tables and claims, non-resident relief formula, tax credit ordering, transfer pricing and international reporting remain research gaps. Do not infer no withholding from a zero corporate tax rate. Check notices and certificates before applying the rental example.

Primary guidance and Article 118B were read on 11 October 2026; the non-resident page was re-read on 14 November 2026 and its figures matched. The current Income Tax Law governs the stated snapshot. Its conditions resolve broader wording in the generic non-resident summary. See `references.md`. This draft has no professional sign-off.

| Source | URL | Read on |
|---|---|---|
| Revenue Jersey, Tax on your Jersey income if you live abroad: read for the 20% rate, agent and tenant deduction, GBP 25,000 threshold, certificate and 60-day rule | https://www.gov.je/TaxesMoney/IncomeTax/Individuals/IncomeTaxCircumstances/pages/nonresidencytax.aspx | 2026-11-14 |
| Income Tax (Jersey) Law 1961, Arts. 88(3) and 118B: read for non-resident exemptions, the short-term business visitor and the 10% dividend deduction | https://www.jerseylaw.je/laws/current/l_29_1961 | 2026-10-11 |
| Revenue Jersey, Residency for Jersey income tax: read for the residence categories | https://www.gov.je/TaxesMoney/IncomeTax/Individuals/IncomeTaxCircumstances/Pages/ResidencyForJerseyTax.aspx | 2026-10-11 |
| Government of Jersey, Full double taxation agreements: read for the list of full agreements | https://www.gov.je/TaxesMoney/InternationalTaxAgreements/DoubleTaxation/Pages/FullDoubleTaxation.aspx | 2026-10-11 |
| Government of Jersey, Partial double taxation agreements: read for the list of partial agreements | https://www.gov.je/TaxesMoney/InternationalTaxAgreements/DoubleTaxation/Pages/PartialDoubleTaxation.aspx | 2026-10-11 |
| Government of Jersey, Resolving treaty disputes (MAP): read for the dispute route | https://www.gov.je/TaxesMoney/InternationalTaxAgreements/DoubleTaxationProcedure/pages/treatydisputes.aspx | 2026-10-11 |

Not yet confirmed: the payment and return dates for agents and tenants who deduct; the base for a tenant's 20% deduction (gross or net rent); the non-resident relief formula; complete dividend deduction mechanics and treaty-specific rates.
