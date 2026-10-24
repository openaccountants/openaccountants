---
name: ps-corporate-income-tax
description: >
  Palestine corporate income-tax research draft based on the Official Gazette Bureau's consolidated Decree-Law 8 of 2011. Covers ordinary and specified company rates, deductible business expenditure, loss carry-forward, registration, return attachments, records and statutory late-filing provisions. Includes three reproducible calculations with explicit assumed eligibility. The portal lists amendments through 2016; later amendments, emergency measures, territorial application and current filing operations remain unverified. This is not a statement of uniform administration throughout the Palestinian territories or complete country coverage.
jurisdiction: PS
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.2
verified_by: pending
sources:
  - url: "https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين"
    title: "Official Gazette Bureau consolidated Income Tax Decree-Law 8 of 2011, articles 1–4, 8–10, 16 and 18–36"
    as_of: "2026-10-22"
---

# Palestine: corporate income-tax calculation and filing framework

## Scope and source status

This Guide translates selected provisions of the Official Gazette Bureau's Arabic consolidated text. Its amendment list identifies Decree-Laws 4/2014, 5/2015 and 14/2016. That list is not proof that every subsequent change, instruction or emergency measure has been incorporated. Confirm the governing administration, location, taxpayer status and applicable period before using a result. Application in the West Bank, Gaza and East Jerusalem has not been reconciled; no uniform operational treatment is asserted. [Official consolidated text](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

## Entity status and accounting period

Article 1's resident legal-person definition combines **registration in Palestine** with a local centre or branch exercising management and control of the business there. Do not replace that combined wording with incorporation alone or a foreign treaty's residence test. Its legal-person and company definitions include foreign companies, and the company definition includes their operating branches. Registration, domestic residence and treaty residence remain distinct questions. [Article 1](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

Article 4 uses the calendar year as the default. A taxpayer closing accounts on another date needs the Director's **prior approval** to calculate tax on its financial year. A bookkeeping software setting does not establish approval. [Article 4](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

## Registration and company rates

Article 2 requires a person undertaking business or investment activity to register from commencement. Registration is distinct from investment-relief approval or business licensing. Article 16(2) specifies **15% of taxable income for legal persons**, with **20% for telecommunications companies and companies enjoying a concession or monopoly in the Palestinian market**. Establish classification before choosing the rate. [Articles 2 and 16](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

Life insurers have a separate **5% charge on total life-insurance premiums due** under article 16(3); other income follows the ordinary legal-person rule. Do not apply 5% to their net accounting profit or use 15% indiscriminately for all insurers' income. This draft does not calculate insurance or investment-incentive cases. [Article 16(3)](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

## From accounts to taxable income

Article 8 requires deductible expenditure to be incurred or accrued wholly and exclusively to produce gross income during the tax period, subject to its detailed conditions. It includes business operating costs and specified financing costs. Establish supporting evidence and the applicable exclusion before treating a ledger expense as deductible. Capital allowances, provisions, related-party restrictions and the complete article 9 exclusions need separate analysis. [Articles 8–9](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

Article 10 offsets a loss from a taxable source against other net income in the same period. The unused balance carries to immediately following periods, for at most **five tax periods**. A loss from a source whose profit would not be taxable is not deductible. Article 10(4) also requires the taxpayer to produce proper, correct accounts before a loss can be deducted or carried forward. Keep those accounts and a loss schedule by originating period and source; this provision alone does not settle reorganisations or changes of ownership. [Article 10](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

### Non-deductible expenses and withholding condition

Article 9 excludes personal/household expenditure, capital improvements and capital expenditure, recoverable insured/indemnified losses or expenses, income tax paid, asset revaluation losses and criminal fines. General provisions/reserves are excluded subject to article 8(1)'s specified insurance and bank/lending exceptions. Determine the statutory category rather than treating an accounting provision as a tax deduction. [Article 9](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

Article 9(7) also denies deduction for taxable salaries, wages or other taxable amounts unless the tax has been withheld and paid to the department. An expense invoice or payroll accrual does not prove that condition. Establish the relevant withholding obligation, remittance and evidence; this paragraph does not by itself determine every withholding rate or exemption. [Article 9(7)](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

For illustration, assumed accounting profit of ILS100,000 already includes ILS6,000 personal costs and ILS4,000 income-tax expense. Adding back both gives ILS110,000 before other tax adjustments. At an independently established 15% rate, this produces ILS16,500 before credits. This example assumes both costs were charged in profit and makes no claim about unexamined deductions.

```oa-check
name: Palestine personal and income-tax expense addbacks
inputs:
  accounting_profit: 100000
  personal_cost: 6000
  income_tax_expense: 4000
  rate: 0.15
steps:
  - adjusted_profit: accounting_profit + personal_cost + income_tax_expense
  - tax: adjusted_profit * rate
expected:
  adjusted_profit: 110000
  tax: 16500
```

## Worked example 1: ordinary company

Assume an ordinary legal person within article 16(2), no relief or special regime, and independently verified taxable income of ILS200,000 after all adjustments. At 15%, tax is ILS30,000. Accounting profit is not automatically the taxable base. No instalment credit or early-payment discount is assumed.

```oa-check
name: Palestine ordinary company tax on established taxable income
inputs:
  taxable_income: 200000
  rate: 0.15
steps:
  - tax: taxable_income * rate
expected:
  tax: 30000
```

## Worked example 2: qualifying loss and special rate

Assume a company established to fall within the 20% category, current net taxable-source income of ILS300,000, and an eligible, unexpired ILS50,000 loss available under article 10, supported by proper, correct accounts as required by article 10(4). Taxable income is ILS250,000 and tax is ILS50,000. If the loss is from an exempt source, article 10(3) denies that deduction and tax on the assumed ILS300,000 is ILS60,000. These alternatives test classification, not entitlement to use any particular historic loss. [Articles 10 and 16](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

```oa-check
name: Palestine eligible loss versus exempt-source loss
inputs:
  current_income: 300000
  eligible_loss: 50000
  rate: 0.20
steps:
  - taxable_income: current_income - eligible_loss
  - tax: taxable_income * rate
  - tax_without_deductible_loss: current_income * rate
expected:
  taxable_income: 250000
  tax: 50000
  tax_without_deductible_loss: 60000
```

## Return, attachments and records

Article 19 requires the approved return within **four months following the tax period's end**. For an assumed period ending 31 December, that points to 30 April, subject to separately verified extensions and deadline rules. Article 20 requires the specified legal persons to attach final accounts, a licensed auditor's certificate and an auditor-certified tax adjustment statement. Article 18(2) retains a return duty for income exempt under investment legislation. An exemption is not automatic exemption from filing. [Articles 18–20](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

Article 23's five-year record period follows the tax period in which tax became final. Do not start it automatically on the transaction date or original return date. Preserve records at the place of business management and check additional legal holds. [Article 23](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

Article 30 distinguishes advances, withholding and payment accompanying the return. Advance-payment dates depend on implementing instructions not verified here. Its final-assessment payment rule uses 30 days from notification where the assessment or court decision has become final; do not substitute that rule for the return-payment requirement. [Article 30](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

## Late filing and payment

The retrieved article 36 prints 2% per month for late tax/advance payment; late returns attract 3% of tax due per month, capped at 20%, with a legal-person minimum of ILS3,000. The interaction of that minimum with small or zero liabilities, month counting, overlapping charges, later amendments and available relief requires confirmation before producing a penalty assessment. The statutory figures are not a certified current penalty quote. [Article 36](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

## Facts needed and remaining work

Obtain incorporation and management locations, actual operating territory, business activity/concession status, period dates, adjusted income, loss provenance, investment approvals, auditor evidence, payments and any assessment/service records. Remaining work includes current-law reconciliation, complete residence/source rules, remaining deductions and incentives, distributions/withholding, treaties, objections, operational channels and territorial administration. No professional attestation or comprehensive-coverage conclusion follows from these examples.

## Sources

- [Official Gazette Bureau consolidated Decree-Law 8/2011](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين), read 22 October 2026. Article references above identify each claim; Arabic controls over this research translation.

## Disclaimer

Source-cited draft, not professionally attested. Verify the applicable law, administration, facts and current procedures before filing or paying.
