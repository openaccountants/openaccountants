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
| `nd-estimated-tax.md` | 2026 individual ND-1ES workflow and payment/interest owner; final2026ND-1UT remains a stated update gap. |
| `nd-return-assembly.md` | 2026 reviewer-package preparation; actual2025-2026filing-cycle mapping clearly labelled, final2026forms remain a filing gate. |
| `nd-cross-border-tax.md` | 2026 source/residence, reciprocity and credit method; final2026ND-1NR/ND-1CR mapping remains partial. |
| `nd-transfer-pricing.md` | Separate transfer-pricing job, unchanged existing 2026 scope; not an ordinary corporate computation or new independent approval. |

`nd-payroll` owns wage withholding and employer reconciliation; `nd-social-contributions` owns state UI. Both original slugs remain because they serve different jobs. Their UI overlap has been consolidated into the UI owner, with all old UI assertions either corrected there or explicitly reserved.

Property, oil/gas production/extraction, coal conversion/extraction, insurance-premium and other special excises are separate jobs. No new claim about estate/inheritance tax is made from the old README's absence assertion.

## How to use

Load the relevant state skill and its stated dependencies. `nd-sales-tax` requires `us-sales-tax`. Federal owners include `us-form-941-940-payroll`, `us-form-1120-c-corp`, `us-federal-income-tax-return-1040`, `us-schedule-c-and-se-computation` and `us-pl-86-272-income-tax-nexus`; state skills do not maintain competing federal figures. Resolve each closing **Not yet confirmed** item before relying on it for a filing. Taxpayer account facts and professional review remain necessary.
