# Utah tax skills,2026

Written by Codex. Not reviewed by an accountant. Source-cited drafts; accountant review pending.

|Core job|covered_by|Coverage and limits|
|---|---|---|
|Individual wage income tax|`ut-income-tax`|Enacted 2026 4.45% rate, correct federal AGI bridge and verified 2025-2026 filing-cycle taxpayer-credit/exemption/filing path. Partial: final 2026 annual forms, indexed amounts and credit changes.|
|Sales/use tax|`ut-sales-tax`|Current Pub 25 Sept 2026 classification, sourcing,3% grocery, current 100,000 economic nexus, software, TC-62 electronic filing and use tax. Partial: special transactions, facilitator exceptions and dated local rate input.|
|Corporate franchise/income tax|`ut-corporate-tax`|2026 4.45% rate and 100 minimum, ordinary TC-20 bridge/filing-cycle prepayments. Partial: final 2026 forms/conformity, multistate/special entities and credits.|
|Payroll withholding and SUI|`ut-payroll`|Both owned here. Published WH for pay periods beginning 1 June 2026, filing/deposit path; actual 2026 SUI 50,700 base and assigned-rate computation/reporting. Partial: pre-June WH tables, UI industry/min/max parameters, transmission and special coverage.|

The old README assertion that Utah has no estate/inheritance tax is Not yet confirmed in this pack. Existing income/sales slugs preserved; new corporate/payroll skills fill missing core jobs. No skill deleted or renamed. Each job has one owner. Other property, motor fuel, severance/mining, estate/inheritance, local business licensing and industry levies remain outside this four-job pack; existing ancillary topics are retained as bounded decisions/referrals in their owners rather than expanded without research.

## Files

[ut-income-tax.md](ut-income-tax.md),[ut-sales-tax.md](ut-sales-tax.md),[ut-corporate-tax.md](ut-corporate-tax.md),[ut-payroll.md](ut-payroll.md).

## Primary sources and use

Individual/corporate 2026 rates:[enrolled SB 60](https://le.utah.gov/~2026/bills/sbillenr/SB0060.pdf). Annual return structure:[final 2025 TC-40 instructions](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf) and [final 2025 TC-20 instructions](https://files.tax.utah.gov/tax/forms/current/tc-20inst.pdf), labeled **2025-2026 filing cycle**. Sales:[current Pub 25](https://tax.utah.gov/forms-pubs/pub-25/). Payroll:[June-effective 2026 WH publication](https://files.tax.utah.gov/tax/forms/pubs/pub-14.pdf),[actual 2026 UI base](https://jobs.utah.gov/ui/Employer/public/Questions/ExcessWages.aspx) and [DWS reporting](https://jobs.utah.gov/UI/Employer/Public/Questions/QuarterlyReporting.aspx).

Load linked federal owner skills from `skills/us/federal/` and methods from `skills/global/methods/`. Federal figures have one home there. Read each Sources and Not yet confirmed section before filing. Do not treat 2025 annual credit values as 2026 or June withholding tables as applicable to earlier pay periods. Save accepted returns and payment confirmations separately.
