---
name: ca-bookkeeping-monthly-close
description: >
  Use this skill whenever an AI must perform California bookkeeping or a monthly
  close from bank, card, payroll, merchant-processor, marketplace, invoice, or
  receipt records for a sole proprietor, disregarded single-member LLC,
  partnership, multi-member LLC, S corporation, C corporation, employer, or
  operating nonprofit. It covers US-CA chart-of-accounts mapping, balanced
  journals, bank and processor reconciliations, FTB, CDTFA, EDD, and Secretary
  of State control accounts, financial statements, compliance calendars, and
  tax-return handoff schedules for tax year 2026. Trigger on California
  bookkeeping, monthly close, trial balance, payroll-tax reconciliation,
  sales-tax clearing, or agency-control questions. It does not prepare returns
  or give legal advice.
jurisdiction: US-CA
category: bookkeeping
tax_year: 2026
tax_year_notes: "2026 calendar-year controls; fiscal-year entities use their own year-end and the current agency calendar"
tier: 2
last_updated: 2026-09-20
version: 0.1
review_status: pending_review
depends_on:
  - bookkeeping-workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# California Bookkeeping and Monthly Close v0.1

> **Source-cited draft — not reviewed by an accountant.** This guide is
> general bookkeeping reference material for AI-assisted workflows. A
> credentialed California reviewer must review the working papers before a
> return is prepared, a payment is made, a journal is posted to a client ledger,
> or a compliance position is taken.

## What this file is

This is the California companion to the universal
[bookkeeping-workflow-base](../../foundation/bookkeeping-workflow-base.md).
It supplies the California chart of accounts, management-reporting layout,
transaction patterns, agency-control reconciliations, 2026 calendar inputs, and
tax-return handoff rules that the base requires. The base supplies the
nine-step close, three classification tiers, five core outputs, and twelve
integrity checks.

This guide is a bookkeeping and working-paper guide. It does not calculate or
file a California or federal return, choose an entity classification, decide
worker status, decide whether a sale is taxable, give employment-law advice,
respond to a notice, or resolve an audit. California rules are separated from
federal inputs. When a federal or California tax skill is loaded, that skill
owns the tax computation; this guide owns the ledger tie-out and handoff.

**Tax-year coverage.** The control-account rules and cited 2026 figures in this
draft were checked on 2026-09-20. Rates, assigned filing frequencies, agency
notices, and deadlines can change. Refresh the linked agency source before
using a number in a client workpaper.

## Section 1 — Scope statement

### In scope

Use this guide for:

- Sole proprietors.
- Disregarded single-member LLCs (SMLLCs).
- Multi-member LLCs and partnerships.
- S corporations and C corporations.
- California employers and entities with California payroll.
- Operating nonprofits with ordinary revenue and expense streams. Full fund
  accounting, donor-restricted fund releases, and grant compliance are outside
  this guide.
- Calendar-year or fiscal-year monthly closes, provided the entity year-end is
  confirmed before the calendar is built.
- Bank, credit-card, merchant-processor, marketplace, invoice, receipt,
  payroll-register, and general-journal data.

The close produces a balanced trial balance, a profit and loss statement, a
balance sheet, a transaction register, a reviewer brief, California agency
control reconciliations, a compliance calendar, tax-return handoff schedules,
and a missing-information report.

### Explicit exclusions and hard stops

Stop and refer to a qualified reviewer when the request asks the AI to:

- Prepare, sign, submit, or amend a tax return or payroll return.
- Choose federal or California entity classification, make a tax election, or
  decide whether an S election or PTE election should be made.
- Decide worker classification, apply the AB 5 test, or give a
  reasonable-compensation opinion.
- Decide sales-tax nexus, taxability, exemption, resale, district allocation,
  or marketplace liability when the source records do not establish the
  treatment.
- Calculate payroll, advise on wages, benefits, workers' compensation, leave,
  termination, or other employment-law matters. Payroll registers may be
  posted and reconciled when a payroll provider or reviewer supplies the
  amounts.
- Resolve tax notices, audits, appeals, liens, levies, penalty abatement, or
  collection matters.
- Prepare trust, estate, public-company, regulated-industry, assurance, or
  cannabis accounting.
- Prepare full nonprofit fund or grant accounting.
- Calculate city or county business taxes.

An excluded request becomes a handoff item with the source documents, ledger
balance, and exact question for the reviewer. It is never silently answered.

## Section 2 — California agency map and source register

The following sources are primary agency sources for this guide. They describe
filings and control evidence; they do not authorize this guide to file
anything.

| Area | Primary source | Bookkeeping use |
|---|---|---|
| FTB forms and entity returns | [FTB business e-file forms](https://www.ftb.ca.gov/tax-pros/efile/business-entity-efile-forms.html), [business due dates](https://www.ftb.ca.gov/file/when-to-file/due-dates-business.html), and [FTB forms](https://www.ftb.ca.gov/forms/) | Map the entity, return, payment, extension, withholding, and handoff balances. |
| FTB LLC tax and fee | [FTB business due dates](https://www.ftb.ca.gov/file/when-to-file/due-dates-business.html) and [Form 568 materials](https://www.ftb.ca.gov/forms/) | Keep the annual LLC tax, LLC fee, estimated fee, payments, and return balance separate. |
| FTB PTE elective tax | [FTB PTE elective tax](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/) and [PTE help](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) | Track the June payment, return payment, credit support, and payment-to-year mapping. |
| FTB withholding | [2026 Form 592 instructions](https://www.ftb.ca.gov/forms/2026/2026-592-instructions.html) and [Form 592-B](https://www.ftb.ca.gov/forms/2026/2026-592-b.pdf) | Reconcile California-source withholding, payee schedules, vouchers, and statements. |
| CDTFA sales and use tax | [Publication 51 filing frequencies](https://www.cdtfa.ca.gov/formspubs/pub51/tax-and-fee-rates-and-filing-frequencies.htm), [marketplace facilitator guide](https://www.cdtfa.ca.gov/industry/MPFAct.htm), [Publication 109 Internet sales](https://cdtfa.ca.gov/formspubs/pub109/), and [Publication 116 records](https://www.cdtfa.ca.gov/formspubs/pub116/) | Separate gross sales, taxable sales, district tax, use tax, marketplace tax, prepayments, returns, and payments. |
| EDD payroll | [2026 payroll calendar](https://edd.ca.gov/en/Payroll_Taxes/Due_Dates_Calendar), [rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding), [required filings](https://edd.ca.gov/en/Payroll_Taxes/Required_Filings_and_Due_Dates), [payroll deposits](https://edd.ca.gov/en/Payroll_Taxes/Timely_Payroll_Tax_Deposits), and [Employer Guide DE 44](https://edd.ca.gov/pdf_pub_ctr/de44.pdf) | Reconcile payroll journals, wage bases, deposits, DE 9, DE 9C, DE 88, new-hire, and contractor-reporting evidence. |
| EDD new hires and contractors | [New Employee Registry](https://edd.ca.gov/new_hire_reporting) and [Independent Contractor Reporting](https://edd.ca.gov/en/payroll_taxes/independent_contractor_reporting) | Create a reporting handoff; do not decide employee versus contractor status. |
| Secretary of State | [Statement of Information tips](https://www.sos.ca.gov/business-programs/business-entities/statements) and [entity FAQs](https://www.sos.ca.gov/business-programs/business-entities/faqs) | Maintain the entity-compliance calendar and proof of filing. |
| IRS federal inputs | [Employment tax due dates](https://www.irs.gov/businesses/small-businesses-self-employed/employment-tax-due-dates), [2026 Form 941 instructions](https://www.irs.gov/instructions/i941), [2026 Forms 1099 instructions](https://www.irs.gov/instructions/i1099mec), and [employment-tax recordkeeping](https://www.irs.gov/businesses/small-businesses-self-employed/employment-tax-recordkeeping) | Tie federal payroll and information-return schedules to the ledger; delegate federal tax calculations. |
| California record retention | [FTB keeping tax records](https://www.ftb.ca.gov/file/after-you-file/keeping-your-tax-records.html) and [CDTFA Publication 116](https://www.cdtfa.ca.gov/formspubs/pub116/retaining-records.htm) | Keep a retention index and preserve records during audits or disputes. |

## Section 3 — Filing requirements and compliance calendar

### Close cadence

The calendar has two layers. The close cadence is an internal accounting
control. Agency due dates are external obligations and are copied from the
current agency calendar only after the entity, filing frequency, and tax year
are confirmed.

| Frequency | Close action | Evidence |
|---|---|---|
| Every month | Lock the source-data period, reconcile every bank and card, reconstruct processor and marketplace activity, post payroll-provider journals, update agency controls, and review suspense. | Bank reconciliations, processor roll-forward, payroll register tie-out, control-account roll-forward. |
| Each payroll | Post gross-to-net and employer-tax journals supplied by the payroll provider; reconcile the cash withdrawal to the payroll clearing account. | Payroll register, provider journal, funding report, deposit confirmation. |
| Each CDTFA period | Reconcile sales, exemptions, district allocation, use-tax purchases, marketplace evidence, prepayments, return, and payment. | CDTFA workpaper and filed-return copy supplied by the reviewer. |
| Each quarter | Tie the EDD DE 9 and DE 9C wage totals to the payroll register and GL; tie DE 88 deposits to the liability roll-forward. | DE 9, DE 9C, DE 88, payroll register, and bank confirmation. |
| Year-end | Freeze the close, count or verify inventory, update fixed-asset and loan schedules, reconcile all agency balances, and package the tax-return handoff. | Final trial balance, statements, reconciliations, handoff worksheet, reviewer brief. |

### 2026 California events

The dates below are control-calendar inputs, not filing instructions. If a due
date falls on a weekend or legal holiday, use the agency's next-business-day
rule and preserve the source page in the calendar.

| Obligation | 2026 control rule | Bookkeeping action |
|---|---|---|
| EDD DE 9 and DE 9C, Q1 | Due April 1, 2026; the EDD calendar shows April 30 as the delinquent date. | Close March payroll, tie the wage file, and attach the filed reports and payment evidence. |
| EDD DE 9 and DE 9C, Q2 | Due July 1, 2026; the EDD calendar shows July 31 as the delinquent date. | Same tie-out for April–June. |
| EDD DE 9 and DE 9C, Q3 | Due October 1, 2026; the EDD calendar shows November 2 as the delinquent date. | Same tie-out for July–September. |
| EDD DE 9 and DE 9C, Q4 | Due January 1, 2027; the EDD calendar shows February 1, 2027 as the delinquent date. | Close December payroll and carry the calendar item into the next work year. |
| EDD DE 88 | Quarterly, monthly, next-day, or semi-weekly cadence depends on the employer's federal deposit schedule and California PIT withheld. | Read the assigned schedule from EDD; never infer a deposit frequency from the bank feed. |
| FTB C corporation | Form 100/100W original return and payment are generally due the 15th day of the fourth month after year-end; the FTB page gives the applicable extension rule. | Set the client year-end, attach the FTB estimate and return handoff, and keep payments out of expense until the reviewer directs the tax entry. |
| FTB S corporation | Form 100S original return and payment are generally due the 15th day of the third month after year-end; the extended date is the 15th day of the ninth month. | Reconcile shareholder payroll, distributions, estimates, and return handoff. |
| FTB SMLLC | The annual $800 LLC tax is due by the 15th day of the fourth month after the beginning of the tax year. Form 568 and the LLC fee follow the entity's return due-date rules. | Keep Form 3522, Form 3536, Form 568, and payment confirmations in separate control schedules. |
| FTB PTE elective tax | The first payment is due June 15 during the election year; the second payment is due by the original return due date without extension. | Maintain a PTE payment-to-tax-year schedule and do not net it into owner distributions. |
| FTB withholding | 2026 Form 592 remittance periods end March 31, May 31, August 31, and December 31, with the due dates in the current Form 592 instructions. | Tie each period's payee ledger, withholding payable, remittance, and Form 592-B support. |
| CDTFA sales/use tax | CDTFA assigns quarterly prepay, quarterly, monthly, fiscal-yearly, or yearly frequency based on the account. | Record the assigned frequency and exact due dates from the CDTFA account; file a zero return when the assigned return requires one even if no taxable sales occurred. |
| Secretary of State | California and out-of-state stock corporations generally file annually; California nonprofits and LLCs generally file every two years. LLCs file an initial statement within 90 days. The filing window is tied to the registration month. | Calendar the next window from the SOS record and retain the filed Statement of Information. |
| Federal Forms 941 and 940 | Form 941 is quarterly; Form 940 is annual when required. | Tie each federal return or provider report to the payroll register and federal liability accounts. |
| Federal W-2/W-3 and 1099 series | W-2/W-3, 1099-NEC, 1099-MISC, and 1099-K handoffs use the current IRS instructions and recipient/agency dates. | Complete the payee and wage schedules, then hand them to the preparer; do not make a filing determination from a vendor name alone. |

Sources for this calendar are the [FTB business due-date page](https://www.ftb.ca.gov/file/when-to-file/due-dates-business.html),
[FTB Form 592 instructions](https://www.ftb.ca.gov/forms/2026/2026-592-instructions.html),
[FTB PTE guidance](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html),
[EDD 2026 calendar](https://edd.ca.gov/en/Payroll_Taxes/Due_Dates_Calendar),
[CDTFA filing-frequency guidance](https://www.cdtfa.ca.gov/formspubs/pub51/tax-and-fee-rates-and-filing-frequencies.htm),
[SOS filing guidance](https://www.sos.ca.gov/business-programs/business-entities/statements), and the
[IRS employment-tax calendar](https://www.irs.gov/businesses/small-businesses-self-employed/employment-tax-due-dates).

## Section 4 — 2026 rates, thresholds, and control facts

These facts are used to set up reconciliations. They are not a return
calculation. If a tax skill or the current official source gives a different
year-specific value, stop and escalate the difference.

| Control fact | 2026 value or rule | Source and treatment |
|---|---|---|
| California statewide sales/use tax base | 7.25%; district taxes vary by location. | [CDTFA Publication 51](https://www.cdtfa.ca.gov/formspubs/pub51/tax-and-fee-rates-and-filing-frequencies.htm). Use the current CDTFA rate lookup in the sales-tax workpaper; do not apply 7.25% to every transaction. |
| Marketplace economic-nexus test | Combined sales of tangible personal property for California delivery by the retailer and related persons exceeding $500,000 in the preceding or current calendar year is an important registration test. | [CDTFA Marketplace Facilitator Act guide](https://www.cdtfa.ca.gov/industry/MPFAct.htm). The guide does not decide nexus or taxability; it flags the threshold for reviewer review. |
| California LLC annual tax | $800 for an LLC doing business in California or registered with the Secretary of State. | [FTB Form 568 materials](https://www.ftb.ca.gov/forms/) and [FTB business due dates](https://www.ftb.ca.gov/file/when-to-file/due-dates-business.html). Post the payment against the FTB LLC-tax control, not automatically to expense. |
| PTE elective tax | 9.3% of qualified net income for the qualified entity's election computation. | [FTB PTE elective tax](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/). This guide only reconciles the payment and handoff; the PTE skill or reviewer computes it. |
| EDD UI | 2026 schedule is 1.5%–6.2%; a new employer rate is 3.4% for the period stated by EDD. | [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding). Use the employer's DE 2088 or e-Services rate for the journal. |
| EDD UI and ETT wage base | First $7,000 of subject wages per employee per calendar year. | [2026 Employer Guide DE 44](https://edd.ca.gov/pdf_pub_ctr/de44.pdf). Track employee-level wage-base exhaustion in the payroll workpaper. |
| EDD ETT | 0.1% of UI-taxable wages for employers to which the ETT applies. | [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding). Do not apply when the employer's notice or EDD guidance says the employer is exempt. |
| EDD SDI | 1.3% for 2026; all wages are subject to SDI contributions after the wage-ceiling change described by EDD. | [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding) and [EDD taxable wages](https://edd.ca.gov/en/payroll_taxes/Determine_Taxable_Wages). |
| EDD PIT withholding | No universal rate belongs in the chart of accounts. Use the employee's DE 4 and the current EDD withholding schedules. | [EDD 2026 rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding). |
| California backup withholding | 7% of the payment when California backup withholding applies. | [2026 Form 592 instructions](https://www.ftb.ca.gov/forms/2026/2026-592-instructions.html). Use a separate withholding control and refer classification questions to the reviewer. |
| Record retention | CDTFA records should generally be kept at least four years; FTB generally uses a four-year examination period, with longer periods for exceptions, audits, disputes, and property-basis records. | [CDTFA Publication 116](https://www.cdtfa.ca.gov/formspubs/pub116/retaining-records.htm) and [FTB record keeping](https://www.ftb.ca.gov/file/after-you-file/keeping-your-tax-records.html). IRS employment records also generally require at least four years. |

## Section 5 — California chart of accounts

The codes below are a compact management chart, not a mandated California
chart. Map them to the client's existing ledger before posting. Do not invent
codes in a transaction register: if the client's chart differs, show the
client code and this guide's suggested mapping side by side.

| Code | Account | Type | Normal balance | California use |
|---:|---|---|---|---|
| 1000 | Operating bank | Asset | Debit | Primary operating account. |
| 1001 | Payroll bank | Asset | Debit | Separate payroll funding account. |
| 1002 | Savings or tax reserve bank | Asset | Debit | Reserve account; reconcile like any bank. |
| 1010 | Undeposited funds | Asset | Debit | Cash, checks, and card receipts awaiting deposit. |
| 1020 | Stripe clearing | Asset | Debit | Gross Stripe activity before fees, tax, refunds, and payout. |
| 1021 | PayPal or Square clearing | Asset | Debit | Gross processor activity before payout. |
| 1022 | Marketplace clearing | Asset | Debit | Gross marketplace activity and settlement deductions. |
| 1030 | Accounts receivable | Asset | Debit | Accrual-basis invoices not yet collected. |
| 1040 | Inventory | Asset | Debit | Goods held for resale. |
| 1050 | Prepaid expenses | Asset | Debit | Insurance, software, rent, and other future-period items. |
| 1060 | Security deposits | Asset | Debit | Refundable deposits. |
| 1070 | CDTFA tax receivable | Asset | Debit | Refunds or overpayments supported by a CDTFA workpaper. |
| 1080 | FTB tax prepayments | Asset | Debit | Estimates, PTE, or other payments awaiting return application. |
| 1090 | EDD overpayment receivable | Asset | Debit | EDD credit supported by an account statement. |
| 1100 | Computer and equipment | Asset | Debit | Fixed assets; capitalization and depreciation are reviewer decisions. |
| 1110 | Furniture and fixtures | Asset | Debit | Fixed assets. |
| 1120 | Vehicles | Asset | Debit | Fixed assets; business use is a reviewer input. |
| 1130 | Leasehold improvements | Asset | Debit | Fixed assets. |
| 1190 | Accumulated depreciation | Contra-asset | Credit | Year-end depreciation supplied by the tax or financial-reporting reviewer. |
| 2000 | Accounts payable | Liability | Credit | Accrual-basis vendor invoices. |
| 2010 | Accrued expenses | Liability | Credit | Unbilled or estimated obligations supported by a close schedule. |
| 2020 | Credit-card payable | Liability | Credit | Statement balance and unreconciled card activity. |
| 2030 | Short-term loan payable | Liability | Credit | Principal due within twelve months. |
| 2040 | Long-term loan payable | Liability | Credit | Principal due after twelve months. |
| 2050 | Customer deposits and deferred revenue | Liability | Credit | Cash received before the earning event. |
| 2060 | Payroll wages payable | Liability | Credit | Net wages and payroll-clearing amounts awaiting funding. |
| 2061 | Federal income-tax withholding payable | Liability | Credit | Employee federal withholding. |
| 2062 | Federal Social Security and Medicare payable | Liability | Credit | Employee and employer federal payroll controls. |
| 2063 | California PIT withholding payable | Liability | Credit | Employee California PIT withholding. |
| 2064 | California SDI withholding payable | Liability | Credit | Employee SDI withholding. |
| 2065 | EDD UI payable | Liability | Credit | Employer UI liability. |
| 2066 | EDD ETT payable | Liability | Credit | Employer ETT liability. |
| 2067 | Federal FUTA payable | Liability | Credit | Federal unemployment control. |
| 2068 | EDD DE 88 and DE 9 clearing | Liability | Credit | Temporary clearing when provider reports and bank payments settle separately. |
| 2070 | CDTFA state sales-tax payable | Liability | Credit | State sales-tax component supported by the CDTFA workpaper. |
| 2071 | CDTFA district-tax payable | Liability | Credit | District tax component by location. |
| 2072 | CDTFA use-tax payable | Liability | Credit | Use tax on taxable purchases where the reviewer establishes liability. |
| 2073 | CDTFA prepayment clearing | Liability | Credit | Prepayments awaiting the return period application. |
| 2080 | FTB LLC annual-tax payable | Liability | Credit | Form 3522 and annual tax control. |
| 2081 | FTB LLC-fee payable | Liability | Credit | Form 3536 and Form 568 fee control. |
| 2082 | FTB corporation-tax payable | Liability | Credit | Form 100 or 100S estimate and return control. |
| 2083 | FTB PTE-tax payable | Liability | Credit | Form 3893 and Form 3804 handoff control. |
| 2084 | FTB withholding payable | Liability | Credit | Forms 592, 592-Q, 592-PTE, and 592-B support. |
| 2085 | Other agency-tax payable | Liability | Credit | Temporary, identified control only; never a dumping account. |
| 2090 | Payroll-provider clearing | Liability | Credit | Payroll-funding and provider settlement bridge. |
| 2091 | Shareholder, member, or partner loan payable | Liability | Credit | Related-party debt with written terms or reviewer confirmation. |
| 3000 | Sole-proprietor owner capital | Equity | Credit | Owner investment. |
| 3001 | Sole-proprietor owner draws | Equity | Debit | Personal withdrawals; never a business expense. |
| 3010 | Member contributions | Equity | Credit | LLC member contributions. |
| 3011 | Member distributions | Equity | Debit | LLC distributions. |
| 3020 | Common stock and additional paid-in capital | Equity | Credit | Corporation equity. |
| 3030 | Retained earnings | Equity | Credit | Prior-year corporation or nonprofit earnings. |
| 3040 | Dividends | Equity | Debit | Corporation distributions after reviewer confirmation. |
| 3050 | Net assets without donor restrictions | Equity | Credit | Operating nonprofit presentation. |
| 3051 | Net assets with donor restrictions — tracking only | Equity | Credit | Use only when the reviewer supplies the restriction policy; full fund accounting is excluded. |
| 4000 | Service revenue | Revenue | Credit | Professional and other services. |
| 4001 | Product revenue | Revenue | Credit | Direct product sales. |
| 4002 | Marketplace product revenue | Revenue | Credit | Gross marketplace sales before fees and refunds. |
| 4003 | Other operating revenue | Revenue | Credit | Revenue supported by source documents. |
| 4010 | Operating support or contribution revenue | Revenue | Credit | Basic nonprofit operating support; restricted-grant accounting is referred out. |
| 4020 | Returns, refunds, and allowances | Contra-revenue | Debit | Reduces the related revenue stream. |
| 5000 | Inventory cost of goods sold | COGS | Debit | Cost of goods sold when the inventory schedule supports the entry. |
| 5001 | Freight-in and inbound shipping | COGS | Debit | Inventory cost when the accounting policy treats it as cost of inventory. |
| 5002 | Fulfillment and pick-pack | COGS | Debit | Product fulfillment costs. |
| 5003 | Packaging | COGS | Debit | Packaging treated as COGS under client policy. |
| 6000 | Bank fees | Expense | Debit | Bank and wire fees. |
| 6001 | Merchant-processor fees | Expense | Debit | Stripe, PayPal, Square, and marketplace fees. |
| 6002 | Payment-gateway fees | Expense | Debit | Gateway and card-not-present fees. |
| 6003 | Advertising and promotion | Expense | Debit | Google, Meta, print, and other ads. |
| 6004 | Software and SaaS | Expense | Debit | Software subscriptions and cloud tools. |
| 6005 | Professional fees | Expense | Debit | Accounting, legal, consulting, and tax-preparation fees. |
| 6006 | Insurance | Expense | Debit | Business insurance and employee benefits insurance as directed. |
| 6007 | Rent and occupancy | Expense | Debit | Office, studio, and storage rent. |
| 6008 | Utilities | Expense | Debit | Electricity, water, gas, and other utilities. |
| 6009 | Internet and telecom | Expense | Debit | Internet, phone, and data plans. |
| 6010 | Office supplies | Expense | Debit | Consumable office supplies. |
| 6011 | Postage and shipping | Expense | Debit | Outbound shipping and postage not treated as COGS. |
| 6012 | Travel | Expense | Debit | Travel with source support. |
| 6013 | Meals | Expense | Debit | Meals held for reviewer tax treatment; no deduction is inferred. |
| 6014 | Vehicle and mileage | Expense | Debit | Vehicle costs held for reviewer-apportioned treatment. |
| 6015 | Repairs and maintenance | Expense | Debit | Repairs not identified as capital improvements. |
| 6016 | Wages and salaries | Expense | Debit | Gross wages from the payroll provider. |
| 6017 | Employer payroll taxes | Expense | Debit | Employer UI, ETT, federal payroll taxes, and other provider-supplied taxes. |
| 6018 | Employee benefits | Expense | Debit | Benefits from payroll or benefits-provider reports. |
| 6019 | Contractors and subcontractors | Expense | Debit | Vendor payments after the reviewer supplies worker-status treatment. |
| 6020 | Dues, licenses, and permits | Expense | Debit | Ordinary business registrations and licenses. |
| 6021 | Depreciation | Expense | Debit | Reviewer-supplied depreciation entry. |
| 6022 | Bad debt | Expense | Debit | Accrual-basis bad debt only after reviewer approval. |
| 6023 | Non-income taxes and licenses | Expense | Debit | Property, business-license, and similar items only when in scope. |
| 6024 | Interest expense | Expense | Debit | Loan and credit-card interest. |
| 6025 | Charitable contributions | Expense | Debit | Held for reviewer treatment; no tax deduction is inferred. |
| 6026 | Nonprofit program expenses | Expense | Debit | Operating nonprofit expenses without fund-accounting allocation. |
| 6027 | Review suspense | Temporary | Debit/Credit | Temporary only; every balance requires a question and resolution. |
| 6028 | Penalties and interest — review | Expense | Debit | Separate account; no deductibility conclusion is made. |
| 6029 | Cost-of-sales adjustments | COGS | Debit/Credit | Inventory count and period-end adjustment bridge. |

### Financial-statement presentation

Use a vertical, current/non-current balance sheet. Treat an item as current when
the client's accounting policy and expected settlement place it within twelve
months; document the policy rather than presenting a legal conclusion. Present
the P&L as:

1. Revenue by service, product, marketplace, or operating support.
2. Less returns and allowances.
3. Less COGS, when inventory or fulfillment records support it.
4. Gross profit.
5. Operating expenses.
6. Operating profit.
7. Non-operating income and expense, if any.
8. Net income before tax. Tax expense and tax-basis adjustments belong to the
   reviewer or tax skill.

For a sole proprietor, show owner capital, owner draws, and current-period
profit. For an LLC or corporation, show contributions, distributions or
dividends, retained earnings, and shareholder or member loans separately. For
an operating nonprofit, show net assets with the client's policy labels and
refer restricted-fund accounting out.

### Accounting basis and local GAAP handoff

California does not supply a universal internal-bookkeeping basis for every
entity in this guide. Confirm whether the client and reviewer require cash-basis,
tax-basis, or US-GAAP management statements before finalizing the presentation.
The sole-proprietor and disregarded-SMLLC defaults in Section 10 are workflow
starting points, not accounting elections or tax conclusions. If statutory,
GAAP, audit, grant, or full nonprofit fund-accounting statements are required,
load the applicable financial-statements skill and have the reviewer set the
policy. This guide records the ledger and California control evidence; it does
not certify GAAP compliance or choose a depreciation, inventory, accrual, or
fund-accounting policy.

## Section 6 — Classification rules

Apply the bookkeeping base's three states: Tier 1 (confident), Tier 2
(assumed and flagged), and Tier 3 (needs input). Every source line appears
exactly once in the transaction register, either posted or excluded with a
reason.

| # | Pattern | Debit | Credit | Control or handoff |
|---:|---|---|---|---|
| 1 | Direct customer payment with a matching invoice or sales report | Bank or A/R | Service or product revenue | Separate any tax amount only when the reviewer or tax skill supplies the treatment. |
| 2 | Stripe, PayPal, Square, or other processor settlement | Processor clearing | Bank | The payout is not revenue; reconstruct gross receipts, fees, refunds, and tax. |
| 3 | Processor fee on a settlement | Merchant-processor fees | Processor clearing | Tie to the processor fee report. |
| 4 | Marketplace settlement | Marketplace clearing | Bank | Post gross sales and deductions from the marketplace report before the payout. |
| 5 | Marketplace facilitator-collected tax | Marketplace clearing or tax clearing | CDTFA tax control only when the source establishes the seller's liability | Do not infer marketplace responsibility; retain the facilitator statement. |
| 6 | Customer refund or chargeback | Returns, refunds, and allowances | Bank or processor clearing | Link to the original sale. |
| 7 | Inventory purchase for resale | Inventory or freight-in | A/P or bank | Do not post all merchandise purchases directly to expense when an inventory schedule is required. |
| 8 | Cost of goods sold at shipment or period end | Inventory COGS | Inventory | Use the client's inventory method and reviewer-approved count. |
| 9 | Untaxed business purchase that the reviewer identifies as use-taxable | Expense or asset plus use tax | A/P or bank plus CDTFA use-tax payable | The guide records the control; a sales-tax skill decides taxability and rate. |
| 10 | Bank, wire, and monthly account fee | Bank fees | Bank | Match the bank statement line. |
| 11 | Payroll-provider gross wages | Wages and salaries | Wages payable and payroll withholdings | Use provider journal; never reconstruct gross-to-net from a single bank debit. |
| 12 | Employer payroll taxes in a provider journal | Employer payroll taxes | EDD UI, ETT, federal, or other payroll payable | Tie employee-level wage bases and rate notices. |
| 13 | Net payroll funding | Wages payable or payroll-provider clearing | Bank | The clearing account must return to zero after provider settlement. |
| 14 | EDD DE 88, DE 9, or DE 9C payment | EDD liability or EDD clearing | Bank | Match the payment to the report period and account number. |
| 15 | FTB LLC annual tax payment | FTB LLC annual-tax payable or FTB prepayment | Bank | Use the FTB Form 3522 evidence; do not assume expense treatment. |
| 16 | FTB LLC fee payment | FTB LLC-fee payable or FTB prepayment | Bank | Tie Form 3536, Form 568, and payment year. |
| 17 | FTB corporate or individual estimated payment | FTB tax prepayments | Bank | Keep taxpayer/entity and tax year separate. |
| 18 | FTB PTE payment | FTB PTE-tax payable or FTB tax prepayments | Bank | Link the payment to Form 3893 and the election year. |
| 19 | California withholding remittance | FTB withholding payable | Bank | Tie Forms 592, 592-Q, 592-PTE, or 592-B support. |
| 20 | Owner or member contribution | Bank | Owner capital or member contributions | Confirm owner and entity before posting. |
| 21 | Owner draw or member distribution | Owner draws or member distributions | Bank | Never post to wages or an operating expense without a reviewer-provided payroll entry. |
| 22 | Shareholder or member loan advance | Bank | Related-party loan payable | Require terms, counterparty, and repayment schedule. |
| 23 | Shareholder or member loan repayment | Related-party loan payable and interest expense when supported | Bank | Principal and interest must be separated from the source. |
| 24 | Fixed-asset purchase | Fixed asset or expense suspense | Bank or A/P | Ask before capitalizing; attach invoice and placed-in-service date. |
| 25 | Depreciation journal from the reviewer | Depreciation | Accumulated depreciation | Do not invent a tax or book life. |
| 26 | Contractor invoice or payment | Contractors and subcontractors or A/P | Bank or A/P | Do not decide employee status; create a DE 542 and 1099 handoff flag when the facts indicate one. |
| 27 | DE 34 new-hire evidence | No journal | No journal | Calendar and document control only; the form is not a ledger transaction. |
| 28 | SOS Statement of Information fee | Dues, licenses, and permits or prepaid compliance cost | Bank or A/P | Keep entity-compliance evidence with the calendar item. |
| 29 | Federal Form 941, 940, W-2/W-3, or information-return handoff | No journal unless the provider supplied an unposted liability | No journal | Tie the schedule to federal payroll and information-return controls. |
| 30 | Transfer between two business bank accounts | Receiving bank | Sending bank | Exclude from revenue and expense; match both sides. |
| 31 | Credit-card payment from the operating account | Credit-card payable | Bank | Exclude the payment from expense; expense was recorded on the charge. |
| 32 | Duplicate bank-feed and processor line | No journal | No journal | Exclude one line with a duplicate source reference. |
| 33 | Unexplained round-number transfer | Review suspense | Bank or receiving account | Tier 3; ask whether it is a contribution, draw, loan, refund, or revenue. |
| 34 | Mixed personal and business purchase | Business portion of expense only | Bank or card | Ask for the business percentage; if the user selects “do not know,” use 0% business and post the personal portion to the owner account. |
| 35 | Nonprofit donor receipt | Bank | Operating support or contribution revenue | If restricted or grant-conditioned, stop and refer to the nonprofit reviewer. |

### Conservative defaults

These are bookkeeping defaults, not tax positions:

- Unknown entity type or accounting basis: Tier 3; do not produce final
  statements until confirmed.
- Unknown owner transfer: Tier 3 review suspense; do not call it revenue or
  expense.
- Unknown personal/business purpose: ask. If the user selects “do not know,”
  treat the business percentage as zero and record the personal side as owner
  draw, member distribution, or shareholder distribution as appropriate.
- Unknown processor settlement composition: hold in processor clearing and
  request the gross activity report; never book the payout as gross revenue.
- Unknown marketplace tax responsibility: hold the tax component in review
  suspense and request the facilitator statement; do not decide nexus or
  taxability.
- Unknown FTB, CDTFA, EDD, or IRS payment period: hold in the relevant
  prepayment or agency-clearing account until the notice or confirmation is
  obtained.
- Unknown capital-versus-expense treatment: flag the invoice and use expense
  suspense until the reviewer approves capitalization or expense.
- Unknown contractor-versus-employee status: do not classify the worker; post
  only the supplied provider or invoice amount to a clearly labeled review
  account and create the EDD and federal handoff.
- Unknown current rate or due date: use the agency's current source and record
  the retrieval date; never copy a prior-year rate.

### Materiality policy

California does not supply one universal bookkeeping materiality threshold for
this guide. The reviewer must set a threshold for the client and period.
Until the reviewer does so, treat every uncategorized item as material, do not
group sundry transactions, and do not suppress a Tier 2 or Tier 3 flag.

## Section 7 — Supplier and payee pattern library

These are recognition patterns, not proof of tax treatment. Confirm the
account, period, and source report before applying a recurring pattern.

| Payee or description pattern | Default mapping | Required evidence or flag |
|---|---|---|
| Stripe, Stripe Payments | Stripe clearing and merchant-processor fees | Stripe balance and payout reports. |
| PayPal, Venmo Business | PayPal clearing and merchant-processor fees | PayPal transaction and fee reports. |
| Square, Block | PayPal/Square clearing and merchant-processor fees | Square deposit and fee report. |
| Shopify Payments | Marketplace or processor clearing | Shopify Payments report and order export. |
| Amazon, Amazon Marketplace | Marketplace clearing, fees, refunds, and product revenue | Settlement report and facilitator-tax evidence. |
| Etsy, eBay, Walmart Marketplace | Marketplace clearing | Settlement report, returns, and tax statement. |
| Gusto, ADP, Rippling, Paychex | Payroll-provider clearing | Payroll register and funding report. |
| Employment Development Department, EDD | EDD payroll liability or clearing | DE 88, DE 9, DE 9C, and account statement. |
| Franchise Tax Board, FTB | FTB tax prepayment or liability | Form, voucher, tax year, and payment confirmation. |
| CDTFA | CDTFA sales/use-tax liability or prepayment | Return, prepayment schedule, and payment confirmation. |
| Internal Revenue Service, IRS, EFTPS | Federal payroll or income-tax control | Form, tax period, and EFTPS confirmation. |
| Secretary of State, bizfile | Compliance fee or prepaid filing cost | Statement of Information confirmation. |
| Google Ads, Microsoft Advertising, Meta Ads | Advertising and promotion | Invoice and business purpose. |
| Amazon Web Services, Microsoft Azure, Google Cloud | Software and SaaS | Invoice and service period. |
| Adobe, QuickBooks, Xero, Zoom, Slack | Software and SaaS | Invoice and prepaid-period review. |
| Verizon, AT&T, T-Mobile, Comcast | Internet and telecom | Business-use support for mixed-use plans. |
| PG&E, SCE, SDG&E, municipal utility | Utilities | Business premises or reviewer-approved allocation. |
| USPS, UPS, FedEx | Postage, shipping, or COGS fulfillment | Order or shipment support. |
| Bank, wire, ACH, service charge | Bank fees | Statement detail. |
| Insurance carrier or broker | Insurance or prepaid expenses | Policy term and coverage period. |
| Owner, member, shareholder by name | Capital, draw, distribution, or loan | Tier 3 unless the description and support are explicit. |

## Section 8 — Exclusion and duplicate patterns

Exclude a line from posting only with a reason in the transaction register:

- Transfer between two accounts belonging to the same entity.
- Payment of a business credit-card statement when the underlying card
  charges are already imported.
- Bank-feed duplicate of a processor or payroll-provider line.
- Repeated import of the same invoice or receipt.
- Opening-balance or feed-reconnect adjustment without source support.
- Reversal of a journal that has already been reversed.
- A marketplace payout when the settlement report has already posted the same
  payout.
- A personal purchase: it is excluded from the P&L but remains in the ledger as
  an owner, member, or shareholder transaction when the evidence supports that
  treatment.
- A tax payment: it is not an expense merely because cash left the bank; post
  it against the agency liability or prepayment control.

## Section 9 — Bank, card, and merchant-processor handling

### Bank statement normalization

- Normalize dates to ISO YYYY-MM-DD internally while preserving the source
  date and statement page.
- Accept US MM/DD/YYYY, ISO dates, and a client's documented export format; do
  not reinterpret an ambiguous date without asking.
- Use USD as the default currency for California books. Store ISO code USD,
  use a period as the decimal separator, a comma as the thousands separator,
  and retain two decimal places. Keep foreign-currency source amounts and
  conversion evidence when a non-USD account exists.
- Reconcile from opening statement balance to closing statement balance. A
  bank-feed balance is not evidence of completeness.
- Preserve check number, ACH trace, processor payout ID, invoice number, and
  statement page where available.

### Processor and marketplace roll-forward

For each processor or marketplace and each close:

1. Start with the prior clearing balance.
2. Add gross sales and other receipts from the settlement report.
3. Subtract refunds, chargebacks, fees, reserves, advertising, shipping, and
   tax withheld as separately identified.
4. Add or subtract currency or rounding adjustments only with source evidence.
5. Agree the resulting clearing balance to the report and clear the payout to
   the bank statement.

A payout without a settlement report is Tier 3. A payout must never be posted
as gross revenue merely because its description says “payout.”

## Section 10 — Entity-type defaults

These are workflow defaults, not entity-classification advice.

| Entity | Default ledger approach | Equity and handoff controls |
|---|---|---|
| Sole proprietor | Cash basis unless the client or reviewer confirms accrual; simple chart with owner capital and draws. | Owner draws are equity; federal Schedule C and California Form 540 handoff are separate. |
| Disregarded SMLLC | Separate entity books; cash basis only when confirmed; maintain owner-equity and FTB LLC controls. | Form 568, Form 3522, Form 3536, and owner return handoff; do not collapse the LLC's $800 payment into owner tax. |
| Multi-member LLC or partnership | Accrual management books unless confirmed otherwise; track member capital, distributions, guaranteed payments, and loans separately. | Form 565 or 568 and K-1 support; PTE and withholding controls require reviewer instructions. |
| S corporation | Accrual management books unless confirmed otherwise; payroll and shareholder accounts must be separate. | Form 100S, payroll, shareholder basis/distribution, K-1, and optional PTE handoffs. |
| C corporation | Accrual management books unless confirmed otherwise; corporate equity, loans, dividends, and payroll are separate. | Form 100/100W, estimates, payroll, fixed assets, and tax-provision handoffs. |
| Operating nonprofit | Accrual management books; ordinary operating revenue and expense only. | Form 199 or 109 handoff as directed; refer restricted funds, grants, and full fund accounting. |

Calendar-year versus fiscal-year status is confirmed in Step 4 of the base
workflow. All return and payment dates are keyed to the confirmed year-end,
not to the month in which the books happen to be closed.

## Section 11 — California agency-control reconciliations

### 11.1 FTB

Maintain a roll-forward for each entity and tax year:

| Roll-forward line | Evidence |
|---|---|
| Opening FTB payable or prepayment | Prior-year trial balance and FTB account statement. |
| Form 3522 annual LLC tax | Voucher, confirmation, and entity year. |
| Form 3536 estimated LLC fee | Voucher, confirmation, and fee workpaper. |
| Form 100, 100S, 100W, 565, 568, 199, or 109 return balance | Signed or preparer-supplied return and payment schedule. |
| Form 3893 PTE payments and Form 3804/3804-CR support | Election year, entity, owners, and payment confirmation. |
| Forms 592, 592-Q, 592-PTE, 592-B, and 593 | Payee schedule, withholding payable, remittance, and recipient statement. |
| Payments, refunds, notices, and closing balance | FTB confirmation or account transcript. |

An FTB payment with no tax year or form number is an FTB tax prepayment and
remains flagged. Never net an owner's estimated payment into the entity's
ledger.

### 11.2 CDTFA

The sales-tax reconciliation must contain:

1. Gross sales by channel and period.
2. Returns, refunds, discounts, and chargebacks.
3. Taxable, exempt, and nontaxable sales with the support for each category.
4. State and district tax collected, separately where the source reports it.
5. Marketplace-facilitator tax and the facilitator's collection evidence.
6. Taxable purchases on which the reviewer directed use-tax treatment.
7. Prepayments, assigned filing frequency, return liability, remittances,
   refunds, and the closing CDTFA balance.

CDTFA assigns quarterly prepay, quarterly, monthly, fiscal-yearly, or yearly
frequency. A no-sales period still requires the assigned return when the
account instructions require it; the workpaper records zero taxable sales and
the filed zero return. See [CDTFA filing-frequency guidance](https://www.cdtfa.ca.gov/formspubs/pub51/tax-and-fee-rates-and-filing-frequencies.htm)
and [Publication 116](https://www.cdtfa.ca.gov/formspubs/pub116/) for records.

Do not decide whether a sale is taxable, whether a marketplace facilitator is
the retailer, or whether the $500,000 registration test applies. Those are
reviewer or sales-tax-skill questions. The bookkeeping output preserves the
facts, source reports, and unresolved difference.

### 11.3 EDD

Reconcile each payroll period and quarter:

- Gross wages per payroll register to account 6016.
- UI-taxable wages by employee to the EDD rate notice and wage-base schedule.
- ETT-taxable wages and employer ETT to account 2066.
- SDI withheld to account 2064 using the current EDD rate.
- California PIT withheld to account 2063 using the DE 4 and withholding
  schedule supplied by the payroll provider.
- Employer payroll taxes to account 6017.
- Net payroll funding to account 2060 or 2090.
- DE 88 deposits to the deposit confirmation and period.
- DE 9 and DE 9C quarterly wages and liabilities to the register and GL.
- DE 34 new-hire evidence and DE 542 contractor-reporting handoff evidence to
  the compliance calendar.

EDD requires new or rehired California employees to be reported through the
New Employee Registry within 20 days of the start-of-work date. EDD's
independent-contractor reporting page describes a $600 contract or payment
trigger and a 20-day reporting period for covered service providers. The guide
does not decide whether a person is a contractor. See [EDD required filings](https://edd.ca.gov/en/Payroll_Taxes/Required_Filings_and_Due_Dates),
[new hires](https://edd.ca.gov/new_hire_reporting), and
[independent-contractor reporting](https://edd.ca.gov/en/payroll_taxes/independent_contractor_reporting).

### 11.4 Secretary of State

The SOS control is a calendar and evidence control, not a tax liability:

- Record the entity type, SOS number, formation or registration date, agent,
  principal address, and next filing window.
- Calendar an initial Statement of Information within 90 days where required.
- Calendar annual corporation or biennial LLC/nonprofit filing windows based on
  the registration month.
- Attach the filed statement, confirmation, fee, and any change-of-information
  evidence.
- Escalate a delinquency or suspended status; do not calculate a cure or
  penalty in this guide.

Use the [SOS filing tips](https://www.sos.ca.gov/business-programs/business-entities/statements)
and [SOS FAQs](https://www.sos.ca.gov/business-programs/business-entities/faqs).

### 11.5 IRS

The federal handoff ties:

- Form 941 quarterly totals to payroll registers, federal withholding, Social
  Security, Medicare, and deposits.
- Form 940 annual FUTA to the federal unemployment control.
- W-2/W-3 totals to annual payroll registers and Forms 941.
- Form 1099-NEC and 1099-MISC payee schedules to contractor and vendor
  ledgers.
- Form 1099-K to processor and marketplace gross receipts; reconcile the form
  to the ledger rather than treating it as a second revenue stream.
- Depreciation and basis schedules to fixed-asset additions, disposals, and
  reviewer-approved entries.

The [IRS employment-tax calendar](https://www.irs.gov/businesses/small-businesses-self-employed/employment-tax-due-dates)
and [2026 Form 1099 instructions](https://www.irs.gov/instructions/i1099mec)
control current filing details.

## Section 12 — Required outputs

The five bookkeeping-base outputs are mandatory. This California guide adds
seven schedules to make agency handoff reviewable.

### Output 1 — Trial balance

Use the base columns: account code, account name, debit balance, and credit
balance. Add columns for entity, period, and source schedule when multiple
entities or fiscal years share a workpaper. Total debits must equal total
credits exactly.

### Output 2 — Profit and loss

Present revenue, returns, COGS, gross profit, operating expenses, operating
profit, non-operating items, and net income before tax. Do not include an FTB,
CDTFA, or EDD cash payment as expense unless the reviewer supplies the tax
accounting entry.

### Output 3 — Balance sheet

Present current and non-current assets, agency and operating liabilities,
related-party balances, and equity/net assets. The balance sheet must agree to
the trial balance and satisfy assets = liabilities + equity.

### Output 4 — Reviewer brief

Use the base template and add:

- Agency balances by FTB, CDTFA, EDD, SOS, and IRS.
- Highest-risk processor, payroll, marketplace, owner, and tax-control items.
- Tax-year and fiscal-year assumptions.
- Source documents still missing.

### Output 5 — Transaction register

Use the base columns and add entity, tax-control tag, source report ID, and
reconciliation status. Every line is classified, assumed, user-answered,
excluded with a reason, or unresolved.

### Output 6 — California agency-control reconciliation

| Agency | Opening balance | Current-period charges or withholdings | Payments/refunds | Adjustments | Closing GL | Agency evidence | Difference | Action |
|---|---:|---:|---:|---:|---:|---|---:|---|
| FTB |  |  |  |  |  | Voucher, return, statement |  |  |
| CDTFA |  |  |  |  |  | Return, prepayment, statement |  |  |
| EDD |  |  |  |  |  | DE 88, DE 9, DE 9C, statement |  |  |
| SOS |  |  |  |  |  | Statement and confirmation |  |  |
| IRS |  |  |  |  |  | 941, 940, W-2/W-3, 1099 support |  |  |

### Output 7 — Sales-tax reconciliation

Include channel totals, taxable and exempt classifications, district
allocation, marketplace collection, use-tax purchases, prepayments, return
liability, remittance, and unresolved taxability questions. No tax rate is
invented from a merchant or ZIP code.

### Output 8 — Payroll-tax reconciliation

Include employee-level wage-base detail, gross wages, employee withholdings,
employer taxes, provider clearing, DE 88 deposits, DE 9/DE 9C totals, federal
941/940 totals, and amendments. A zero payroll period is an explicit status,
not a blank row.

### Output 9 — Compliance calendar

For every obligation show entity, agency, form or filing, period, due-date
source, due date, responsible person, evidence received, status, and next
action. Separate recurring agency filings from internal close dates.

### Output 10 — Tax-return handoff worksheet

| Return or form | Ledger package | Reviewer input required | Filing owner |
|---|---|---|---|
| FTB 100, 100S, 100W | Final TB, P&L, BS, fixed assets, estimates, payments | Tax adjustments, apportionment, credits, tax provision | Tax preparer |
| FTB 565 or 568 | Final TB, member/partner capital, distributions, loans, FTB payments | Classification, K-1, fee, withholding, PTE decisions | Tax preparer |
| FTB 199 or 109 | Final TB, support revenue, program expenses, investments | Exemption and unrelated-business analysis | Tax preparer |
| FTB 3522, 3536, 3893 | Liability roll-forward and payment evidence | Amount, year, and election confirmation | Tax preparer |
| FTB 3804 and 3804-CR | PTE payment ledger and owner allocation | Election, qualified net income, credit allocation | Tax preparer |
| FTB 592, 592-B, 592-PTE, 593 | Payee ledger and withholding controls | Withholding classification and recipient statements | Tax preparer |
| CDTFA returns and prepayments | Sales-tax reconciliation and facilitator evidence | Taxability, exemptions, district allocation, assigned frequency | Sales-tax preparer |
| EDD DE 9, DE 9C, DE 88 | Payroll reconciliation and deposit confirmations | Payroll corrections, rate and filing status | Payroll provider or reviewer |
| EDD DE 34, DE 542 | New-hire and contractor report log | Worker status and reportable event confirmation | Employer or payroll reviewer |
| SOS Statement of Information | Entity calendar and confirmation | Entity data changes and filing authorization | Entity owner or filing agent |
| IRS 941, 940, W-2/W-3 | Payroll reconciliation and annual wage file | Federal deposit and filing treatment | Payroll or tax preparer |
| IRS 1099-NEC, 1099-MISC, 1099-K | Payee ledger, W-9 log, processor forms | Reportability, corrections, recipient data | Tax preparer |

### Output 11 — Missing-information and exception report

List each missing bank statement, invoice, processor report, payroll register,
agency notice, tax-year identifier, owner confirmation, or filing copy. For
each item show financial impact, affected control account, question, owner, and
deadline. Never fill a missing source with a guessed rate or date.

## Section 13 — Worked journal examples

The amounts below are fabricated inputs to demonstrate mechanics. They are not
tax thresholds, rate claims, or client advice.

### Example A — S corporation with Stripe and payroll

Suppose a settlement report shows gross customer receipts of 1,000.00, a
processor fee of 30.00, and a bank payout of 970.00. The close posts:

| Debit | Credit | Amount |
|---|---|---:|
| Stripe clearing | Service or product revenue | 1,000.00 |
| Merchant-processor fees | Stripe clearing | 30.00 |
| Operating bank | Stripe clearing | 970.00 |

A payroll-provider journal then posts gross wages, employee withholdings,
employer payroll taxes, and net wages to their separate accounts. The bank
funding entry clears payroll-provider clearing. The EDD and federal payments
debit the appropriate liability accounts. No worker-status, payroll-rate, or
deductibility opinion is made.

### Example B — Disregarded SMLLC owner transfers and contractor

An owner deposits 2,000.00 to fund the business and later withdraws 500.00.
The entries are:

| Debit | Credit | Amount |
|---|---|---:|
| Operating bank | Member contributions | 2,000.00 |
| Member distributions | Operating bank | 500.00 |

A contractor invoice is posted to Contractors and A/P, then the payment clears
A/P. The register creates an EDD DE 542 and federal 1099 handoff flag when the
source facts meet the reporting description; it does not classify the worker.

### Example C — Marketplace e-commerce LLC

The settlement report shows 1,200.00 of product sales, 120.00 of marketplace
fees, and an 1,080.00 payout. The entries are:

| Debit | Credit | Amount |
|---|---|---:|
| Marketplace clearing | Marketplace product revenue | 1,200.00 |
| Merchant-processor fees | Marketplace clearing | 120.00 |
| Operating bank | Marketplace clearing | 1,080.00 |

Inventory and COGS are posted from the inventory schedule. Marketplace-collected
tax is not assumed to be the LLC's CDTFA liability; the facilitator statement
and the sales-tax reviewer determine the treatment.

### Example D — Fiscal-year operating nonprofit

For a fiscal-year nonprofit, the close first records the fiscal year-end and
does not force a December calendar. A supported operating receipt is posted to
Operating Support or Contribution Revenue. A receipt described as restricted,
grant-conditioned, or donor-directed is held for nonprofit-review input; full
fund-accounting entries are outside this guide.

## Section 14 — Realistic test suite and refusal behavior

Run these cases with fabricated inputs before treating the guide as ready for a
client:

1. **S corporation:** Stripe settlements, payroll provider journal, DE 88
   payments, and a 941 handoff. Expected: processor clearing and payroll
   clearing reconcile to zero or documented outstanding items; all debits equal
   credits.
2. **SMLLC consultant:** owner deposits, owner withdrawals, contractor
   payments, FTB 3522, and an unexplained transfer. Expected: owner activity is
   equity or related-party debt, not revenue; the unexplained transfer is Tier
   3; Form 568 and FTB payment evidence are in the handoff.
3. **Multi-member e-commerce LLC:** inventory, marketplace settlements,
   returns, facilitator tax, direct sales, and a CDTFA prepayment. Expected:
   gross settlement reconstructs, inventory and COGS are separate, and
   unresolved taxability is not guessed.
4. **Fiscal-year nonprofit employer:** payroll, zero-payroll month, operating
   support, and a restricted-grant description. Expected: fiscal-year calendar,
   EDD controls, and a nonprofit reviewer escalation.
5. **Boundary cases:** missing statements, unexplained transfers, mixed
   personal/business expense, amended DE 9C, a tax payment with no period,
   zero payroll, and a duplicate processor payout. Expected: questions,
   suspense, or exclusion with reasons; no silent guess.
6. **Out-of-scope:** “file Form 568,” “decide whether this worker is an
   employee,” “tell me whether this sale is taxable,” or “answer this FTB
   notice.” Expected: stop, preserve the workpaper, and refer to a qualified
   professional.

The reviewer records the fabricated inputs, expected control balances, actual
outputs, and any correction. A test passes only when the base checks and the
agency-control checks below pass.

## Section 15 — Self-checks

Run the twelve checks in the bookkeeping base plus these California checks:

- [ ] The entity type, state identifier, tax year, and fiscal year-end are
  confirmed before any calendar or equity account is selected.
- [ ] Every bank and card statement has an opening and closing balance, source
  period, and documented difference.
- [ ] Every processor and marketplace payout is supported by a settlement
  report; no payout is counted as gross revenue twice.
- [ ] FTB payments are mapped to an entity, tax year, and form or remain in
  prepayment suspense.
- [ ] CDTFA sales, exemptions, district allocations, use-tax purchases,
  prepayments, return, and payment tie to the sales-tax reconciliation.
- [ ] EDD gross wages, UI/ETT/SDI/PIT controls, DE 88 deposits, and DE 9/DE 9C
  reports tie to the payroll register.
- [ ] DE 34 and DE 542 events are calendared without making a worker-status
  determination.
- [ ] SOS filing windows are tied to the official entity registration month
  and the proof of the last filing.
- [ ] Federal 941, 940, W-2/W-3, 1099-NEC, 1099-MISC, and 1099-K handoffs do
  not duplicate California revenue or payroll liabilities.
- [ ] Calendar-year and fiscal-year dates are not mixed.
- [ ] Each Tier 2 or Tier 3 item appears in the reviewer brief and exception
  report.
- [ ] No rate, threshold, deadline, taxability, worker-status, or election
  conclusion appears without a current primary source or reviewer input.
- [ ] Record retention is calendared for at least the controlling agency
  period, and longer when an audit, dispute, property-basis, or other
  exception requires it.

## Section 16 — Disclaimer

This skill and its outputs are provided for informational and computational
purposes only and do not constitute tax, legal, accounting, payroll, or
financial advice. It does not create a client-professional relationship,
prepare or file a return, decide worker classification or taxability, or
replace a current agency instruction. California and federal rules change.
OpenAccountants and its contributors accept no liability for errors, omissions,
or outcomes arising from use of this draft. A qualified professional must
review and sign off on the working papers before posting, filing, paying, or
taking a tax position.

## Change log

- v0.1 (2026-09-20): Initial California bookkeeping and monthly-close source
  draft. Added the chart of accounts, entity defaults, classification and
  supplier patterns, California agency controls, 2026 calendar inputs,
  handoff schedules, worked examples, and validation tests.
