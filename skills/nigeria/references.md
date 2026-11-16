---
name: nigeria-references
jurisdiction: NG
last_updated: '2026-11-16'
version: '1.1'
description: Nigeria source and software research routing for 2026. Use when locating Nigerian tax legislation, choosing the owning country skill, or assessing the provenance of PolicyEngine/policyengine-ng and Ahmzyjazzy/naija-tax-agent. Repository popularity and a software licence do not establish current Nigerian tax law or permission to incorporate material into this mixed-licence repository.
tier: 2
tax_year: 2026
type: router
category: international
---

# Nigeria source and software references v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## The method, step by step

1. Identify the job and period before loading software. For personal tax load [ng-personal-income-tax](ng-personal-income-tax.md); for company tax [ng-cit](ng-cit.md); for outgoing-payment withholding [ng-wht](ng-wht.md); for gains [ng-cgt](ng-cgt.md); for employee payroll [ng-payroll](ng-payroll.md); assemble the results with [ng-return-assembly](ng-return-assembly.md). The [ng-income-tax](ng-income-tax.md) companion retains the bank-narration library. VAT uses [nigeria-vat](nigeria-vat.md), subject to its stated limits. This file does not replace any computation.
2. Open the governing primary source, including the definitions and exceptions. The current National Assembly [Nigeria Tax Act](https://nass.gov.ng/documents/download/11249) and [Nigeria Tax Administration Act](https://nass.gov.ng/documents/download/11250) are different laws. Do not substitute a company income-tax exemption for VAT relief. The [JRB withholding Gazette](https://www.jrb.gov.ng/documents/withholding-regulations-2024.pdf) and [personal income tax guidelines](https://cms-api.jrb.gov.ng/api/publication-assets/file/2026-pit-guidelines-TJG3n9-T%20%281%29.pdf) supply implementation detail; the statute controls a conflict. The law-copy differences are recorded in ng-cit.
3. Treat the two original project references as research leads. Inspect the exact revision, licence file and actual rule implementation before deciding whether to use a project. Compare every proposed tax rule with the legislation for the relevant period, then recompute representative boundary cases independently.

| Original project | What was actually checked | Permitted conclusion for this reference |
| --- | --- | --- |
| [PolicyEngine/policyengine-ng](https://github.com/PolicyEngine/policyengine-ng) | Its README identifies PolicyEngine Nigeria; its LICENSE contains the GNU Affero General Public License, Version 3. GitHub describes a Nigerian tax-benefit model and identifies Python. | A possible source of modelling ideas. No code was run, no tax parameter was verified and no reuse approval is given. Keep provenance if later work incorporates material. |
| [Ahmzyjazzy/naija-tax-agent](https://github.com/Ahmzyjazzy/naija-tax-agent) | Its README describes a tax-query and CAC-search agent, a Python backend and frontend/widget directories. The README claims MIT, but the linked root LICENSE was not found. GitHub identifies TypeScript as the main repository language. | The earlier blanket Python label was incomplete. Licence permission remains unconfirmed. Do not copy code merely because the repository is public or its README says MIT. |

The old popularity observations were 3 stars for policyengine-ng and 9 for naija-tax-agent; the repository metadata returned those same counts on the read date. They are dated discovery notes, not quality scores or permanent project attributes.

4. Check this repository's [LICENSING.md](../../LICENSING.md). Software and skills have different licensing tracks. The earlier assertion that all OpenAccountants material was AGPL and therefore fully compatible was incorrect. No material from either project is incorporated by this update. Do not infer compatibility from the words "same licence family".
5. Handoff: record the tax job, period, owning skill, official provisions, proposed software revision, observed licence evidence, tests actually performed and unresolved permissions. If no implementation has been checked, say so.

## When to refuse or refer

Refer a request for a filing figure to the owning tax skill. Refuse to describe either project as a tax authority, current-law validator or accountant approval. Hold incorporation where a licence file or rights for the intended use are missing. Refer licence interpretation to an appropriate reviewer rather than promise direct reusability.

## Sources

| Source and actual read scope | URL | Read on |
| --- | --- | --- |
| National Assembly NTA: read sections6/12/33/56 to59 and the small-company definition, not a software licence | https://nass.gov.ng/documents/download/11249 | 2026-11-16 |
| National Assembly NTAA: read sections11/13/14/31/49/51 and the small-business definition | https://nass.gov.ng/documents/download/11250 | 2026-11-16 |
| PolicyEngine repository metadata, complete short README and licence identification; tax implementation not read | https://github.com/PolicyEngine/policyengine-ng | 2026-11-16 |
| PolicyEngine LICENSE: read opening identification and version | https://github.com/PolicyEngine/policyengine-ng/blob/master/LICENSE | 2026-11-16 |
| Naija Tax Agent metadata and complete README; linked root licence unavailable | https://github.com/Ahmzyjazzy/naija-tax-agent/blob/main/README.md | 2026-11-16 |
| Repository LICENSING.md: read software/content mapping and third-party copyleft sections at local main revision | https://github.com/openaccountants/openaccountants/blob/2844c309238b4fdb63be0a3d0ad9ae99a8ea89c8/LICENSING.md | 2026-11-16 |

Not yet confirmed: the intended-use licence permission for either integration; an operative licence file for naija-tax-agent; the accuracy, completeness, maintenance status and security of either project's tax logic or dependencies. The original direct-reuse and validation claims are withdrawn as usable instructions, with both project identities retained.
