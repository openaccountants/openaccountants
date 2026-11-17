---
name: ghana-references
jurisdiction: GH
category: international
tax_year: 2026
tax_year_notes: "Official source navigation checked on 2026-11-16 only; this router supplies no current tax rates or computations. Historical project claims remain non-operative."
last_updated: 2026-11-16
version: 1.1
type: router
description: Locate official Ghana PAYE and pension sources and load the existing income-tax or payroll skill. Preserve the original taxcalculatorgh project reference as unverified history, not tax authority or permission to reuse code.
tier: 2
---

# Ghana official sources and project references v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use this router to find Ghana employment-tax and pension sources before using a calculator or reusing a third-party project. It supplies no operative tax rate, contribution base, liability calculation or filing deadline. The original private-project note remains below as non-operative history.

## The method, step by step

1. Establish the tax period and whether the question concerns personal income/PAYE, employer payroll, pension contributions or code reuse. Do not infer the period from a calculator's default settings.
2. For personal income or PAYE, load [Ghana personal income tax](ghana-pit.md). Open the [GRA PAYE page](https://gra.gov.gh/domestic-tax/tax-types/paye/) for official topic guidance and the [GRA Acts catalogue](https://gra.gov.gh/acts/) to locate legislation. The catalogue separates abridged versions from Acts; a title or download listing is not a reading of the law or proof that all amendments are included.
3. For payroll or pension contributions, load [Ghana payroll and social contributions](gh-payroll-social.md) as well. The [SSNIT FAQs](https://www.ssnit.org.gh/faqs/) provide official pension-topic navigation. Establish the applicable legislation, current notice, base and period in the substantive skill before using a rate; this router does not validate those figures.
4. For a private calculator or software reuse, record the exact project and revision, then establish its licence and provenance separately. Consult the repository's [licensing map](../../LICENSING.md) for OpenAccountants material. Neither the old blanket AGPL statement nor the historical integration note below establishes permission to copy a particular artefact.
5. Hand off the question, period, selected skill, exact official URL, provision actually read, relevant publication/amendment dates and unresolved gaps. Distinguish an index visit from reading the linked document. Stop at a source gap that changes the result; do not treat a private project's popularity or implementation as authority.

## When to refuse or refer

- Do not compute from the archived PAYE tables or contribution claim below. Read the applicable official rule and the selected substantive skill for the actual period.
- Do not certify a private project's licence, maintenance, popularity, accuracy, historical incorporation or attribution from this note. Resolve code-reuse rights before reuse.
- If the official text, amendment scope or project provenance cannot be established, identify that precise gap and refer the substantive tax or reuse question. This source-navigation file cannot resolve it.

## Sources

| Official source | What was actually read | Read on |
|---|---|---|
| [GRA PAYE](https://gra.gov.gh/domestic-tax/tax-types/paye/) | PAYE heading/topic identity and navigation to Acts and tax guidance only. No rate, base, deadline or full tax-rule review for this router. | 2026-11-16 |
| [GRA Acts](https://gra.gov.gh/acts/) | Catalogue headings, including the distinction between abridged versions and Acts, and income-tax/amendment title listings only. Linked Acts were not read for this router; completeness/currentness is not inferred from the list. | 2026-11-16 |
| [SSNIT FAQs](https://www.ssnit.org.gh/faqs/) | FAQ topic index, Social Security and Act 766 labels, and navigation only. No pension rate, contribution base, eligibility or deadline review for this router. | 2026-11-16 |

Not yet confirmed: all original private-project popularity, star count, maintenance, language, historical tables, SSNIT rate, incorporation, attribution and licensing claims reproduced below. The project was not inspected for this update. The original note's last_updated was 2026-06-12; it supplied no actual source-read dates. The new dates above apply only to the stated official navigation reads. No private claim is promoted to current tax guidance or a code-reuse licence.

### Historical Ghana related open-source project note

The following original text, including its project credit and reuse claims, is retained as non-operative history. It is not an official tax source, an endorsed calculator, a verified incorporation record or a verified licence statement.

> OpenAccountants is AGPL-3.0. Projects below are used as reference for tax rate data.
>
> #### taxcalculatorgh
>
> - Repository: [Kessir/taxcalculatorgh](https://github.com/Kessir/taxcalculatorgh)
> - License: verify before code reuse (no explicit license file)
> - Stars: 32
> - Language: JavaScript (Vue.js)
> - Scope: Most popular Ghana income tax calculator on GitHub. Implements GRA PAYE (Pay As You Earn) monthly tax brackets with historical rate tables from 2021 through 2024. Includes SSNIT (Social Security) contribution calculation at 5.5%.
> - Why it matters: Actively maintained with bracket updates tracking GRA announcements. 32 stars indicates real usage among Ghanaian developers and taxpayers.
> - Integration approach: Monthly PAYE bracket tables and SSNIT rate used as reference for the income tax skill. Rate data (public domain tax law) incorporated with attribution.
