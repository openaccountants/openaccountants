---
name: slovakia-references
jurisdiction: SK
last_updated: 2026-11-15
version: 1.1
description: "Evaluate Priznanie Digital source and licence provenance, establish revision-specific coverage, then hand tax calculations and current form/schema checks to the Slovakia owners. Software reference only; no upstream runtime or filing acceptance is certified."
tier: 2
tax_year: 2026
type: router
---

# Slovakia: Related Open-Source Projects

Use this page to assess Priznanie Digital as a software reference, then return to the owning tax skill and current official form. Its licence permits reuse subject to its terms; neither its licence nor its contributor count establishes correct tax treatment.

## Ask the client first

- Which return type, tax period and taxpayer/income/expense facts must the integration support?
- Which exact repository revision, licence and dependency notices are being evaluated?
- Is the task to inspect a reference, reuse source code, modify it, or distribute/run a service?
- Which official form/schema and edge cases will the intended output be checked against?

## The method, step by step

### Priznanie Digital

1. Follow the original [priznanie-digital/priznanie-digital](https://github.com/priznanie-digital/priznanie-digital) link to the current canonical [slovensko-digital/priznanie-digital](https://github.com/slovensko-digital/priznanie-digital) repository. Retain the project name **Priznanie Digital**. The upstream README describes a self-employed flat-rate-expense personal-income-tax application and calculation, XML-generation and submission-handoff code. Its documentation distinguishes English code terminology from Slovak tax terminology. [Upstream README](https://github.com/slovensko-digital/priznanie-digital/blob/master/README.md).
2. Inspect the actual upstream licence before reuse. It is MIT, with the upstream copyright notice and permission notice required in copies or substantial portions, and an express warranty disclaimer. Preserve those notices and inspect dependency/asset terms separately. MIT's permission is not a blanket compatibility finding for every file or redistribution arrangement. [Upstream LICENSE](https://github.com/slovensko-digital/priznanie-digital/blob/master/LICENSE).
3. Check the destination's licence by material. OpenAccountants' software is AGPL, while its skill content follows the separately stated content licence; the repository policy also preserves terms for older derivative material. The old statement that every OpenAccountants item is AGPL and any MIT/Apache/GPL/AGPL content is automatically incorporable was too broad. Determine the particular source, destination, notices and distribution/service obligations before copying. [OpenAccountants licensing policy](https://github.com/openaccountants/openaccountants/blob/main/LICENSING.md).
4. Treat the code as implementation evidence to test, not an official source for a rate or filing requirement. Load [slovakia-pit](slovakia-pit.md) for self-employed classification, actual versus flat-rate expenses, allowances, child bonus and current return conditions; [sk-payroll-social](sk-payroll-social.md) for applicable insurance facts; and [sk-cross-border](sk-cross-border.md) if foreign facts arise. Those owners identify the operative law and the applicable form/instructions.
5. Compare the exact revision's supported period, eligibility, calculation boundaries, output schema and submission route with the actual official return and instructions. Test ordinary and edge cases against the law, reconcile the computation and inspect the generated XML before accepting output. A test framework or contributor count alone does not verify those matters. This rewrite read the README/licence and repository metadata; it did not run the upstream application or certify its current-year XML or tax calculations.
6. Hand off the repository/revision and licence evidence, intended taxpayer coverage, official form/schema, recomputation results and unresolved differences. Do not describe it as full personal-return coverage merely because it can produce a type-B output, and do not describe an XML-generation or handoff feature as an accepted filing.

### Preserve the old topics without treating them as current proof

| Earlier reference topic | Destination or boundary |
|---|---|
| Project identity, repository and MIT reuse | Canonical/original links and actual licence steps above |
| Slovak/English terminology; self-employed/type-B application | README scope and revision check above; the supported tax period still needs testing |
| Flat-rate expenses, non-taxable amounts, child bonus, social/health treatment | PIT and payroll/social owners for the law; code coverage must be established at the chosen revision |
| XML generation and electronic filing | Inspect the actual output and current official schema/submission instructions; no acceptance claim is made here |
| Old stars, contributor total and last-push observation | Historical observations listed below, not current popularity, activity or verification evidence |
| Proposed direct reuse and claimed testing quality | Source/dependency/destination licence review and independent tax/schema tests, rather than inferred accuracy |

## When to refuse or refer

- No fixed revision, current-year coverage evidence, applicable licence or official schema: do not claim the integration is ready.
- Taxpayer facts fall outside demonstrated upstream coverage: compute through the relevant tax owner and resolve the unsupported case before using the output.
- Licence conflict, unclear provenance or third-party assets/dependencies: obtain a specific licence analysis before distribution or deployment.
- General reference only: no particular person's facts, documents, elections, residence, deadlines or filing status were reviewed. A filing, payment, amendment or tax position still requires the relevant factual and professional review.

## Sources

| Primary source and scope actually read | URL | Read on |
|---|---|---|
| Original project link and canonical repository metadata; redirect/identity checked | https://github.com/priznanie-digital/priznanie-digital | 2026-11-15 |
| Upstream README, stated purpose, terminology, calculation and XML/handoff implementation; no runtime verification | https://github.com/slovensko-digital/priznanie-digital/blob/master/README.md | 2026-11-15 |
| Upstream MIT LICENSE, permission, notice requirement and warranty terms | https://github.com/slovensko-digital/priznanie-digital/blob/master/LICENSE | 2026-11-15 |
| OpenAccountants LICENSING.md, software/content split and older derivative material | https://github.com/openaccountants/openaccountants/blob/main/LICENSING.md | 2026-11-15 |

Not yet confirmed: the old observations of 18 stars, 40 contributors and a last push in April 2026; whether they were accurate on the earlier page's date; full type-B coverage, insurance/allowance/bonus coverage, current-year calculations, current official XML compatibility, accepted electronic submission or suitability of any particular upstream revision. The old contributor-count inference of well-tested real returns is not verification evidence.
