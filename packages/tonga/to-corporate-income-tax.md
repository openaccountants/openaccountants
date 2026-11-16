---
name: to-corporate-income-tax
description: >
  Compute ordinary Tonga company chargeable income and current published company tax, classify resident/non-resident withholding and prepare a fiscal-period filing reconciliation for 2026. Hold special industries, unresolved rate Orders, live form mapping and uncertain source/PE applications.
jurisdiction: TO
category: international
type: computation
tax_year: 2026
last_updated: 2026-11-16
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: 0.1
---

# Tonga Corporate Income Tax v0.1

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Compute ordinary Tonga company chargeable income and identify payment-withholding obligations during 2026. First determine the actual company fiscal year and residence. A partnership is treated as a company for income-tax purposes; a sole-trader small-business regime must not be applied to an incorporated company. Residents generally include worldwide non-exempt income; non-residents include Tongan-source income. Apply exemptions, separate/final-tax classes and PE attribution before multiplying a net profit by the company rate.

| Item | Amount / rule and complete conditions | Official source |
|---|---|---|
| Ordinary company income tax | 25% of chargeable income for resident and non-resident companies; determine taxable scope/base first. | [Business Income Tax Rates; ITA s 5](https://www.revenue.gov.to/company-partnership-corporative-society-trust) |
| Resident company | Formed/incorporated in Tonga, or centre of administrative management in Tonga at any time during the year, or partnership with a resident partner; any applicable alternative suffices. | [s 4(6)](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf) |
| Fiscal year and ordinary return | Company: 12 months ending on annual accounts balance date; ordinary return within 4 months after that year, subject to statutory notice/exemption/actual extension. | [s 2 fiscal year; ss 68-69](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf) |
| Tongan-source non-resident interest, royalty, dividend, technical service fee | 15% gross under current MORC guidance; subject to source, type, exemption and effective-PE-connection exceptions, not every foreign invoice. | [Tax on Non-residents/Withholding tax; ITA ss 6,60,79-80](https://www.revenue.gov.to/non-residents-and-visitors) |
| Non-resident insurance premium | 5% gross under current MORC guidance for a Tongan-source non-exempt premium, including the applicable PE exception. | [Tax on Non-residents; ITA ss 6,79-80](https://www.revenue.gov.to/non-residents-and-visitors) |
| Independent services to non-resident | 10% gross Tongan-source business-income payment for independent services other than payments already in s 79(2); classify technical/managerial/consultancy fees first. | [s 79(3); definitions and s 60(4)](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf) |
| Interest paid to resident non-financial recipient | 10% gross only where payer is resident company or Tonga PE of non-resident company; exemption/finality/credit rules are separate. | [ss 77,80,89-90](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf) |
| Withholding time/remittance | Earlier of account credit or actual payment; remit within 28 days after month end, with statutory next-business-day rule. | [ss 81-82; RSAA Regulations 2021 reg 25](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf) |

## Ask the client first

Obtain legal form, incorporation/management/partner-residence facts and actual accounts balance date; trial balance, asset disposals, private/capital items, tax adjustments and prior business losses/ownership changes; Tongan and foreign activity/PE facts; every payee's residence, contractual service type and source/PE connection; withholding certificates, foreign tax evidence and instalment/payment receipts; actual tax registrations, filing notices and extensions. Obtain exemption/approved-fund/sector documents rather than infer relief from an entity name.

## The method, step by step

### Establish the taxable base

Under [ss 10-14,25-26 and 38](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf), reconcile accounts to gross taxable income less deductions actually allowed. Company business income/expenditure normally uses accrual accounting; unpaid sales invoices can therefore belong in income. Include taxable business-asset disposal gains and balancing adjustments; exclude proved exempt/final-tax income. Do not deduct owners' drawings, private expenditure, income tax, penalties or other prohibited costs. Capital assets use their statutory allowance route rather than an automatic immediate deduction. Retain the expenditure purpose and source documents. A salary/payment subject to withholding is not deductible until the required withheld tax has been paid (s 26(2)); recording the gross wage alone is insufficient.

Business losses carry forward against business income under s 37; do not offset them against separately taxed gross payments. If underlying ownership changes by 50% or more, s 58 disallows pre-change carried losses unless the entity continues the same business until the loss is fully used and, until then, does not enter a new business/investment where the principal purpose of the entity or its owners is using that loss to reduce tax on income arising from the new business/investment. Check both conditions throughout utilisation. Resident-company dividends to a resident member are exempt under s 21; this does not exempt the paying company's ordinary business profit. Cross-border foreign-source business and other income have separate loss/credit rules; do not pool them without ss 62-63.

Apply the current [MORC company rate](https://www.revenue.gov.to/company-partnership-corporative-society-trust) to established chargeable income. The Act s 5 authorizes rates by Order; the table is not presented as statutory wording of s 5. Apply foreign credit first and eligible withholding/instalment credits after it under s 5(3), checking ss 89-91 and actual receipts. Foreign credit under s 62 is the lesser of foreign tax paid and Tonga tax on the net taxable foreign-source income, computed with the average Tonga pre-credit tax rate, defined as Tonga income tax before any credit divided by chargeable income. Compute foreign business and other foreign income separately; the foreign tax must be paid within 2 years after the relevant fiscal year, and unused credit is neither refunded nor carried back/forward. If any input or classification is missing, hold the foreign-credit calculation. A final withholding tax is not a credit against ordinary chargeable-income tax.

### Classify non-residents and withholding

Apply the source tests to the actual payment. Physical work, payer residence, an overseas business/PE exception, use of rights and property location can change the result; a foreign bank account is not the source test. Sections 6(2)-(3) move effectively connected interest, royalties/rent/resource rights or services rendered through the Tonga PE into the ordinary PE analysis. Section 64 treats the PE as a separate independent enterprise and restricts head-office royalties, service fees and interest, with its actual third-party reimbursement/banking exceptions. Refer uncertain PE/withholding overlap before describing a gross payment as final or a net amount as the tax base.

For payments within the confirmed withholding rows, determine source, classification and exemption first. Technical services include managerial/technical/consultancy services, but exclude employment; independent services are a separate statutory category. Do not apply both rows to the same payment. Do not withhold from proved exempt income (s 80). Withhold at the earlier credit/payment event, remit by the proper monthly due date and issue the approved certificate. Gross-basis separate/final taxes under ss 9 and 90 do not allow expenses, losses or credits to reduce that payment tax; s 90 also prevents refund of final withheld tax. Classification is a prerequisite, not an election to choose the cheaper gross or net calculation.

Resident-interest withholding applies only to the specified payer and recipient population. A financial-institution payment to an individual can be final under s 90(1)(b); other eligible withholding can instead be creditable under s 89. Do not call every resident-interest withholding final or treat it as a business expense.

### File, pay and preserve the reconciliation

The ordinary return is Form 11 for a non-individual business under [MORC annual filing guidance](https://www.revenue.gov.to/Tax-Due-Dates-and-Extensions). Confirm the accepted current version and submission route. Complete the actual taxpayer/TIN, fiscal-period, business-income, allowable-expense, chargeable-income and credit fields, attach the accounts/reconciliation/supporting certificates required by the actual approved form, submit through the authorized channel and keep its acceptance and payment receipt. Exact live box mapping is not verified here; hold transmission if it affects the return.

The company fiscal year is its annual accounts period. A 30 June year end ordinarily gives 31 October; a 31 December year end ordinarily gives 30 April in the next calendar year, each derived from s 68's 4-month rule and subject to the next-business-day/actual notice rules. Ordinary income tax is payable by the return due date under s 72. Quarterly instalments under s 91 fall 28 days after the 3rd, 6th, 9th and 12th fiscal months; obtain the actual amount methodology before calculating the instalment. Do not infer that an extension of filing extends payment: RSAA 2021 s 11 requires the filing extension application before the due date, reasonable cause and the written decision. It is available only once, ordinarily for no more than 30 consecutive days unless exceptional circumstances justify longer, and leaves the original payment date/late interest intact.

For withholding use the appropriate current resident/non-resident return (MORC identifies Forms 5/6) and certificates, with the monthly deadline above. Section 86 also requires the approved annual withholding statement within 2 months after 30 June, ordinarily 31 August, plus any actual additional periodic requirement; reconcile the annual statement to the monthly returns, certificates and receipts. For wages use the [payroll skill](to-payroll-social.md). Use TOP in tax returns/financial statements and payments under RSAA Regulations 2021 regs 14-16. Follow the Minister's actual electronic directions or the prescribed permitted physical method; retain the official receipt. Do not enter an invented bank account or unverified portal field.

## Boundary and exception table

| Issue | Treatment |
|---|---|
| Company turnover is small | ITA s 8 expressly excludes a company; use the company route. The simplified regime is for qualifying non-company businesses solely in Tonga, non-CT-taxable and under its turnover limit, excluding professional services and subject to elections/associate rules. Route an actual individual to [individual tax](to-income-tax.md). |
| Related party, foreign-controlled debt, insurance, mining or petroleum | Obtain the applicable provisions/implementing rules before settling deductions or a special-industry bill. |
| Non-resident receipt effectively connected to Tonga PE | Apply ss 6,60,64 and actual withholding interaction; do not automatically use the final gross-tax case. |
| Rent rate or treaty asserted | Hold the affected rate until the actual current Order/treaty conditions are recovered. |
| Late filing/payment | Interest and possible penalties need the operative commencement, dates and correct inputs; no blanket percentage is supplied. |

## Worked cases

All amounts are hypothetical TOP inputs. The examples assume the stated tax classification is established, no incentive or other exemption, and no unresolved ownership/source/PE issue. Outputs are derived.

### Ordinary resident company: accounts profit is not the taxable base

Accounts profit is TOP 100,000 after TOP 4,000 of private shareholder expenditure. Add that disallowed cost back to obtain TOP 104,000 chargeable income. Tax is TOP 26,000; proved current-year instalments of TOP 16,000 leave TOP 10,000 to pay. The expenditure is not deductible merely because the company paid it.

```oa-check
name: Ordinary company private-expenditure adjustment and instalment credit
inputs:
  accounts_profit: 100000
  private_cost_in_accounts: 4000
  proved_instalments: 16000
steps:
  chargeable_income: accounts_profit + private_cost_in_accounts
  income_tax: chargeable_income * 0.25
  balance_due: income_tax - proved_instalments
expected:
  chargeable_income: 104000
  income_tax: 26000
  balance_due: 10000
```

### Non-resident technical fee: gross final-tax basis

A Tongan-source non-exempt technical fee of TOP 20,000 is within the 15% row and the final-tax category, with no effective Tonga PE connection. The recipient incurred TOP 5,000 of its own costs. Withholding is TOP 3,000 and net remittance TOP 17,000. Applying the rate to fee less those costs would produce TOP 2,250 and underwithhold TOP 750. The costs do not reduce this gross tax. A different service/PE classification requires a fresh analysis, not this example.

```oa-check
name: Final non-resident technical-service withholding on gross rather than profit
inputs:
  gross_fee: 20000
  recipient_costs: 5000
steps:
  withholding: gross_fee * 0.15
  net_payment: gross_fee - withholding
  incorrect_net_base_tax: (gross_fee - recipient_costs) * 0.15
  underwithholding: withholding - incorrect_net_base_tax
expected:
  withholding: 3000
  net_payment: 17000
  underwithholding: 750
```

## When to refuse or refer

Refuse to finalize a company return without its actual fiscal period, complete tax-base reconciliation or payment/credit evidence. Refer uncertain source/PE, related-party, incentive, treaty and special-industry positions. Do not use an approximate universal filing date, a sole-trader concession for a company, a secondary rate or a blanket gross-withholding default.

## Filing and payment

Use the return/payment sequence above and the actual approved form. Reconcile accounts, tax base, gross tax, each credit and balance; match receipts to period and TIN. Preserve accepted Form 11, attachments, withholding returns/certificates and the subsequent payment/account confirmation. Calendar instalments and ongoing [CT](to-vat-gst.md)/PAYE separately.

## Completion checklist

Confirm legal/tax classification and year; tested taxable scope; documented adjustments and losses; current rate source; foreign/final/non-final credit distinctions; correct withholding category/event; actual form acceptance and payment; and a list of unresolved applications. This is a source-cited draft without accountant approval.

## Sources

| Source and actual reading scope | Official URL | Read on |
|---|---|---|
| Income Tax Act, Cap.11.05, 2020 consolidation: Read for ss 2-14,21-26,34-38,58-65A,68-69,72,76-86 and 89-91, with their exceptions; not mining/petroleum computations | https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf | 2026-11-15 |
| Income Tax (Amendment) Act 2020: Read for all published ss 1-14, including conditional commencement and procedure changes; no repeal assumed operative | https://ago.gov.to/cms/images/LEGISLATION/AMENDING/2021/2021-0036/IncomeTaxAmendmentAct2020.pdf | 2026-11-15 |
| MORC company/partnership guidance: Read for complete residence, business-base, partnership/company and rate guidance | https://www.revenue.gov.to/company-partnership-corporative-society-trust | 2026-11-16 |
| MORC Non Residents and Visitors: Read for complete residence, non-resident/source/withholding guidance; conflicting rent passages identified | https://www.revenue.gov.to/non-residents-and-visitors | 2026-11-15 |
| MORC Tax Due Dates and Extensions: Read for complete monthly, quarterly, annual deadlines, weekend and extension text | https://www.revenue.gov.to/Tax-Due-Dates-and-Extensions | 2026-11-16 |
| Revenue Services Administration Act 2021: Read for ss 1,9-13,33,79-83 and 91 including commencement and extension limits | https://www.revenue.gov.to/sites/default/files/inline-files/RevenueServicesAdministrationAct2021_1_4.pdf | 2026-11-15 |
| Revenue Services Administration Regulations 2021: Read for regs 14-18 and 24-26 including currency, interest formula, payment and weekend conditions | https://www.revenue.gov.to/sites/default/files/inline-files/RevenueServicesAdministrationRegulations2021_FINAL_Eng_0.pdf | 2026-11-15 |

Not yet confirmed: The published Income Tax Amendment Act 2020 and Consumption Tax Amendment Act 2020 make commencement conditional on the Revenue Services Administration Act 2020, whereas the recovered administration Act is named 2021. No official provision resolving that identity/commencement condition has been recovered; do not infer it from an index or passage history. No amendment-dependent procedure repeal is assumed; current approved-form/administration instructions below have independent current Ministry/RSAA 2021 support. The underlying post-2021 rate Order and any 2026-specific amendment to the published company rate have not been recovered as a complete instrument; the currently published MORC company table is the direct authority for the rate below, not a claim that the rate is printed in s 5. Exact live eTax screens/box mapping, current instalment amount methodology, sector incentives, mining/petroleum/insurance computations, transfer pricing/thin-capitalisation implementation and treaty-specific relief require separate current sources. Non-resident rent is excluded from the numerical withholding table because the same MORC page contradicts itself; determine the operative rate Order before using a rent rate. Current commencement of RSAA 2021 Part 14 and the actual quarter-specific lending-rate input have not been established, so no numeric administrative-penalty/interest bill is supplied. The old universal 30 April return date is withdrawn: it is only the derived 4-month date for an actual 31 December company balance date, not Tonga’s universal deadline. Small-business tax is not a company concession.
