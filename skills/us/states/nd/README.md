# North Dakota state tax skills, 2026

**Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. The ordinary core jobs have current state-law research; specific final-form, local-rate and specialist gaps remain explicit.

| Core job | Status | covered_by | Boundary / partial |
| --- | --- | --- | --- |
| Individual wages/business income tax | applicable | `nd-income-tax` | 2026 published ND-1ES schedules; final 2026 return mapping and specialist credits partial |
| Sales and use tax | applicable | `nd-sales-tax` | Current ordinary 5% and remote rule; actual local rates, SaaS/digital classifications and special exemptions partial |
| Corporate income tax | applicable | `nd-corporate-tax` | Current statutory rates/base; final 2026 forms, special industries/NOL cases and comprehensive PTET status partial |
| General corporate franchise tax | not_applicable | `nd-corporate-tax` | Ordinary income-tax provisions do not create a general franchise computation; registration/industry charges remain separate |
| Employer income-tax withholding | applicable | `nd-payroll` | Actual 2026 booklet; military-spouse facts, specialist nonwage and WSI matters partial |
| Employer unemployment contributions | applicable | `nd-social-contributions` | Actual 2026 wage base/rate schedule; employer notice/elections, SOC details and special coverage partial |

## Existing separate jobs retained

| File | Retained scope and boundary |
| --- | --- |
| `nd-estimated-tax.md` | Individual 2026 estimated tax (Form ND-1ES tests, installments, Schedule ND-1UT interest and waivers), rewritten for tax year 2026 from the 2026 ND-1ES; rate schedules stay in `nd-income-tax`. 2026 Schedule ND-1UT not yet published. |
| `nd-return-assembly.md` | Tax year 2026 return-assembly orchestrator (filing how-to); links every figure to its owning skill. 2026 Form ND-1 line numbers not yet published, 2025 lines used. |
| `nd-cross-border-tax.md` | Individual cross-border job for tax year 2026: nonresident proration, Minnesota and Montana reciprocity and Form NDW-R, military residence, credit for tax paid to another state. |
| `nd-transfer-pricing.md` | Corporate connected-party job for tax year 2026: worldwide combined reporting, water's-edge election and 3.5% additional tax, single-sales-factor election, alternative apportionment. Not an ordinary corporate computation; rates stay in `nd-corporate-tax`. |

`nd-payroll` owns wage withholding and employer reconciliation; `nd-social-contributions` owns state UI. Both original slugs remain because they serve different jobs. Their UI overlap has been consolidated into the UI owner, with all old UI assertions either corrected there or explicitly reserved.

Property, oil/gas production/extraction, coal conversion/extraction, insurance-premium and other special excises are separate jobs. No new claim about estate/inheritance tax is made from the old README's absence assertion.

## How to use

Load the relevant state skill and its stated dependencies. `nd-sales-tax` requires `us-sales-tax`. Federal owners include `us-form-941-940-payroll`, `us-form-1120-c-corp`, `us-federal-income-tax-return-1040`, `us-schedule-c-and-se-computation` and `us-pl-86-272-income-tax-nexus`; state skills do not maintain competing federal figures. Resolve each closing **Not yet confirmed** item before relying on it for a filing. Taxpayer account facts and professional review remain necessary.
