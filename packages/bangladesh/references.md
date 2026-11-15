---
name: bangladesh-references
jurisdiction: BD
last_updated: 2026-11-14
version: 1.1
description: "Primary-law source routing for Bangladesh in 2026 and a historical note on the ssi-anik/bd-income-tax-calculator software; legacy calculator logic is not current legal evidence."
tier: 2
tax_year: 2026
type: router
category: orchestrator
---

# Bangladesh source and legacy-software routing v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Source-selection helper. It does not supply rates or compute a return. Historical software credit remains here; current legal rules live in the linked tax skills.

## Ask the client first

- The job, jurisdiction, earning period and assessment year.
- Whether a supplied calculation comes from legislation, a current authority instruction or old software.
- The exact version and licence of any code proposed for reuse.

## The method, step by step

1. Use the [Income Tax Act](https://bdlaws.minlaw.gov.bd/act-1429.html), [Finance Act](https://bdlaws.minlaw.gov.bd/act-1725.html?lang=en) and [VAT Act](https://bdlaws.minlaw.gov.bd/act-1106.html) as primary-law entry points; open the operative section and neighboring exceptions. Use [PIT](bangladesh-pit.md), [corporate tax](bd-corporate-income-tax.md) and [VAT](bangladesh-vat.md) for current computations.
2. The historical project is [ssi-anik/bd-income-tax-calculator](https://github.com/ssi-anik/bd-income-tax-calculator), described in the old file as a JavaScript/React project under MPL-2.0. Its old category thresholds, component salary exemptions and tiered investment rebate were incorporated into earlier skills. These are provenance facts, not authority for current tax law. Do not run the old algorithm for a current return.
3. Do not repeat the old popularity/star-count or claim it implements current NBR law. Any software integration must separately review the actual version and licence obligations. The old assertion that MPL-2.0, MIT and Apache-2.0 are all automatically compatible with every OpenAccountants component is not a licence determination; consult this repository's LICENSING.md before reuse.
4. For unfamiliar or unconfirmed rules, retain the question in the reviewer exception list and find an official source. Do not substitute a GitHub project, blog or tax-firm summary for that source.

## When to refuse or refer

Refer a licence-compatibility conclusion to the relevant legal/licensing review. Refuse to certify a current tax result solely because it matches the legacy calculator.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for current investment rebate, replacing old tiered logic, section 78 | https://bdlaws.minlaw.gov.bd/act-1429/section-51908.html | 2026-11-14 |
| Read for enacted Finance Act and rate authority | https://bdlaws.minlaw.gov.bd/act-1725.html?lang=en | 2026-11-14 |

Not yet confirmed: The current upstream software licence/version, star count and current-year correctness have not been verified; no software integration or universal licence-compatibility claim is made.
