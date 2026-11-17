---
name: lithuania-references
jurisdiction: LT
last_updated: 2026-11-17
version: 1.1
description: Primary source references and related open-source projects for this jurisdiction.
tier: 2
category: international
domain: references
tax_year: 2026
tax_year_notes: "2026 reference inventory only; no claim that the third-party code implements current tax law or VMI formats."
type: router
---

# Lithuania: related open-source project reference

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Identify the existing investment-report project and its license before a separate technical and tax review. This inventory routes research; it does not compute tax, validate code or authorize an integration. Use the Lithuanian PIT, payroll and cross-border skills for the actual legal classification of shares, benefits, disposals and residence.

## Ask the client first

Obtain the exact project commit, license files and notices, report type and sample fields, issued versus sold shares, currencies, acquisition/disposal dates and intended VMI schema/year. Use synthetic or appropriately protected data for a separate review; no code is executed or installed by this reference.

## The method, step by step

1. Open [sarunas/income-tax-calculator](https://github.com/sarunas/income-tax-calculator) at the proposed commit and inspect its own README and license. The retained README concerns issued/sold share reports, including ESPP and RSU input examples. Its documentation is project evidence, never Lithuanian tax authority guidance.
2. Preserve the prior catalogue's scope: an IBI investment-brokerage-to-VMI conversion project, described as TypeScript and intended for Lithuanian investment/capital-gains reporting. These are catalogue/project descriptions, not a completed current tax-code or filing-schema validation.
3. The project license read is MIT. Retain the original copyright and permission notice, license terms and disclaimer if copying or adapting it. The earlier statement that all projects are compatible with OpenAccountants' AGPL licensing does not itself establish compatibility with this repository's separate code/content licenses; obtain the actual integration review before reuse.
4. The old catalogue's Stars: 21 is retained only as a historical observation without a recorded observation date. It is not a current popularity count, quality test or maintenance claim.
5. The prior integration suggestion was to adapt IBI-to-VMI conversion logic and declaration mappings with attribution. Keep that only as a proposal: establish the exact inputs, gain/basis/FX logic and current filing fields in a separate reviewed task before any production use. The README's install/run instructions are not an authorization to run dependencies or file a return.
6. Output a project/commit pointer, the retained license/notice requirements, the documented input/output purpose and a list of unanswered legal, schema, security and compatibility questions. No tax answer or integration clearance is produced.

## When to refuse or refer

Do not run or install the project, upload taxpayer data, calculate liability or promise a compatible VMI declaration from this inventory. Refer tax correctness, security, dependency and license questions to the appropriate separate reviewer. MIT availability and a star count do not resolve those questions.

## Sources

| Project primary source | Read for | Read on |
|---|---|---|
| https://github.com/sarunas/income-tax-calculator/blob/master/README.md | Actual project README: issued/sold share inputs, ESPP/RSU examples, own usage instructions and disclaimer; not tax law | 2026-11-17 |
| https://github.com/sarunas/income-tax-calculator/blob/master/LICENSE | Actual MIT permission, original notice and disclaimer; retained unchanged, no current-tax or integration approval | 2026-11-17 |

| https://api.github.com/repos/sarunas/income-tax-calculator | Actual project metadata: default branch master, TypeScript language, IBI-to-VMI description and MIT identification; no code or current tax validation | 2026-11-17 |

Not yet confirmed: exact proposed commit and current maintenance; independent code/security or Lithuanian tax validation; current VMI schema and filing support; final license compatibility for a particular integration; the date of the legacy 21-star observation.
