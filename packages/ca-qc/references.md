---
name: canada-references
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-14
version: 2.0
description: Route Canadian research to official legislation, the correct annual CRA package and the existing tax methods. This source directory does not calculate tax or grant permission to incorporate external software.
tier: 2
type: router
---

# Canada official sources and method routing v2.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## The method, step by step

1. Establish task, tax year, taxpayer/entity, residence dates, province or territory and any permanent establishments. A currency, company name or mailing address alone does not select the applicable law.
2. For federal income-tax law use the [Justice Canada Income Tax Act directory](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/). Check its displayed consolidation/amendment date, previous versions, coming-into-force notes and the actual provision. Reading its contents page is not verification of every section. Provincial/territorial tax also needs its own applicable legislation.
3. For individual returns and schedules use the [CRA T1 package selector](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package.html). Its current annual package read here is explicitly the **2025-2026 filing cycle**. Use the special-situation route for newcomers, emigrants, non-residents and deceased returns. Do not relabel a prior-year form as final calendar 2026. Obtaining a paper package and using tax software are different routes.
4. Load the existing task owner, read its scope/sources and verify the material rule against the appropriate official source. A directory entry, software library or passing example is not proof of current law.

| Work needed | Existing method to load | Boundary |
|---|---|---|
| Residence and intake | `ca-tax-residency`, `ca-freelance-intake` | Establish actual status and period before a resident calculation |
| Federal return and assembly | `ca-fed-t1-return`, `ca-return-assembly` | Use the correct annual forms and preserve special-situation workpapers |
| Sole-proprietor classification | `ca-fed-t2125` | Separate business income, expenses, capital assets and personal transfers |
| Employment payroll and contributions | `canada-payroll`, `ca-fed-cpp-ei` | Use applicable employment jurisdiction and current contribution rules |
| Instalments and settlement | `ca-fed-instalments` | Separate preparation, authorised filing, acceptance and payment |
| Gains and non-resident property | `ca-capital-gains`, `ca-nonresident-cgt` | Establish classification, residence, disposition and clearance facts |
| Provincial/territorial work | Exact place/topic method returned by skill search | Check jurisdiction and annual edition; do not load an unrelated same-abbreviation country or US state |

5. Preserve the old reference's separate **external software evaluation** job: inspect the exact project/version, licence, compatibility obligations, maintained period, supported provinces, exclusions and independently recomputed outputs before incorporating code. The old PolicyEngine-Canada entry's star count, licence, coverage and blanket permission to reuse calculation logic were not established from an official tax source. Those assertions are not authority or an incorporation clearance here.
6. Retain the URL, provision/form edition, actual read scope/date and selected method in the workpaper. When official sources disagree, read the applicable law and commencement. If that text cannot be read, name both sources and the unresolved claim instead of guessing or asking the client to choose the rule.

## When to refuse or refer

Do not issue a definitive tax computation, deadline, exemption, credit or software-licence clearance from this source router alone. Load the substantive method and actual source. Refer missing or contested status, law, special allocation or licence issues with the evidence required to resolve them. Missing current figures remain explicit gaps. This router does not file, register, post journals or make payments.

## Sources

| Source and actual read scope | Official URL | Read on |
|---|---|---|
| Read for federal Act title, displayed consolidation/amendment dates, contents, prior versions and commencement warning; not the entire Act or all tax figures | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/ | 2026-11-14 |
| Read for the actual annual edition, jurisdiction selector, software/paper distinction and newcomer/emigrant/non-resident/deceased routes; not verification of every linked form | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package.html | 2026-11-14 |

Not yet confirmed: final calendar 2026 annual packages and task-specific rates, thresholds, deadlines, exceptions and provincial/territorial provisions, which need verification in the selected substantive method. The previous external project's current licence/version, statistics, coverage, incorporation rights and calculation accuracy remain unconfirmed. Its evaluation job is retained without making it tax authority or creating accountant approval.
