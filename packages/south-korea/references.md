---
name: south_korea-references
jurisdiction: KR
last_updated: 2026-11-16
version: 1.1
description: South Korea source-routing and related software inventory for 2026 research, separating official tax authority and legislation sources from third-party implementation references whose code, year and licences need separate review.
category: orchestrator
tax_year: 2026
tier: 2
type: router
---

# South Korea References and Related Projects v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Use this router to find primary authority and preserve the pack's related-software inventory. It supplies no tax calculation or filing deadline. A project's advertised year or a licence badge does not establish current Korean tax law or permission to copy every dependency.

## The method, step by step

1. **Start with the job and period.** For Korean tax law read the Korean text on the [National Law Information Center](https://www.law.go.kr), including commencement provisions and neighboring exceptions. For NTS administration use the [NTS English homepage](https://www.nts.go.kr/english/main.do) and its linked Korean guidance and HomeTax service. An English translation or software implementation is a research aid, with the operative Korean text controlling.
2. **Choose the pack workflow.** Use `kr-social-insurance` for the self-employed insurance workflow, `simplified-business-operator-registration-under-vat-act` for foreign electronic-service VAT registration, and `south-korea-crypto-tax` for crypto classification and the distinction between current obligations and scheduled future income taxation. The existing `kr-income-tax` and `south-korea-vat` files remain separate jobs. Check each file's actual period, sources and unresolved items before relying on it; this inventory does not confer approval.
3. **Use the right official source.** Pension questions begin at [NPS](https://www.nps.or.kr/eng/), health and long-term care at [NHIS](https://www.nhis.or.kr/english/index.do), and the governing law at the law register. For electronic services, [VAT Act art. 53-2](https://www.law.go.kr/LSW/lsLinkCommonInfo.do?lsJoLnkSeq=1031740015) and [Decree art. 96-2](https://www.law.go.kr/LSW/lsLinkCommonInfo.do?lspttninfSeq=112680) state the regime. Use NTS's own source pages for year-end settlement, withholding tables and current filing instructions, not a package's embedded constants.
4. **Treat related software as implementation references.** The projects below are preserved from the old inventory. Their own repository/README was read to establish advertised scope, not to validate calculations. Review the selected commit, licence files, dependencies, attribution and current official tables before copying code. Do not run or install a project merely because this router lists it. This file does not grant reuse rights.

### tax-ui-kr

- Repository: [kimtoma/tax-ui-kr](https://github.com/kimtoma/tax-ui-kr).
- Language and scope: Korean year-end settlement document visualisation and AI chat. The README names withholding receipts, income-deduction and tax-credit statements, PDF parsing, annual comparison and refund/additional-payment presentation.
- Workflow relevance: preserve it as a reference for 연말정산 document structure, 소득공제/세액공제 categorisation, receipt parsing and visual review.
- Licence: no licence identified by GitHub's repository metadata at the read date. The earlier inventory already required verification; keep it reference-only until the actual grant and upstream rights are established.
- Integration: inspect parsing patterns and document schemas against the client's actual documents and the corresponding NTS form year. A README feature claim is not validation of the parser or tax advice.

### korean-tax-calc

- Repository: [chapoleon/korean-tax-calc](https://github.com/chapoleon/korean-tax-calc).
- Language and scope: JavaScript/npm package `@chapoleon/korean-tax-calc`. Its README advertises Korean 2026 severance pay, employee-share pension, health, care and employment insurance, and estimated annual gross-to-net income/local tax.
- Workflow relevance: retain the prior inventory's payroll cycle, social-insurance, personal income-tax and severance calculation topics. The current README expressly describes a simplified annual estimate rather than the monthly withholding table; industrial-accident insurance is excluded from employee deductions in its description. It is not a source for the self-employed insurance method.
- Licence: README says MIT; repository metadata did not identify a licence. Resolve the actual licence file and dependency scope before reuse, retaining the previous reference-only restriction.
- Integration: compare any extracted formulas and parameters to the operative official rules for the precise period. Do not import its advertised year as proof its rates or calculations are correct.

### KoSimpleTax

- Repository: [hyeonki-min/kosimpletax](https://github.com/hyeonki-min/kosimpletax).
- Language and scope: Python package for Korean simplified earned-income withholding and employee-share social insurance. Its Korean README says it is based on 근로소득 간이세액표 and includes both monthly/annual pay inputs and household/dependent parameters.
- Workflow relevance: retain reference use for the withholding-table structure, monthly withholding, insurance calculation and document-field mapping. The inspected README examples import a historical year-specific module; they do not establish 2026 coverage.
- Licence: GitHub identifies MIT. This is evidence about this repository's declared licence, not a blanket compatibility opinion for copied files, data or dependencies.
- Integration: review the actual licence and selected code before reuse and replace historical withholding data only against the matching current NTS table. The previous statement that logic and rate schedules were directly usable without further review is withdrawn.

## When to refuse or refer

Do not answer a current tax figure from these projects alone. Stop if official text, effective date, software year or reuse rights are missing. Refer unresolved Korean legal classification to a qualified Korean practitioner and code-licensing questions to the appropriate reviewer. Do not repeat the previous blanket statement that MIT, Apache, GPL and AGPL material can all be incorporated merely with attribution. The repository's [LICENSING.md](https://github.com/openaccountants/openaccountants/blob/main/LICENSING.md) separates software and Guide content; any particular reuse needs its own review.

## Sources

| Source | URL | Read on |
|---|---|---|
| NTS English homepage: read official source navigation and HomeTax simplified-business banner | https://www.nts.go.kr/english/main.do | 2026-11-16 |
| VAT Act art. 53-2: read the foreign electronic-service regime and exclusions, illustrating the law-first route | https://www.law.go.kr/LSW/lsLinkCommonInfo.do?lsJoLnkSeq=1031740015 | 2026-11-16 |
| VAT Decree art. 96-2: read service scope, registration/return fields and payment provisions | https://www.law.go.kr/LSW/lsLinkCommonInfo.do?lspttninfSeq=112680 | 2026-11-16 |

The following are **software provenance only**, not tax authority: repository metadata and the complete README for [tax-ui-kr](https://github.com/kimtoma/tax-ui-kr), [korean-tax-calc](https://github.com/chapoleon/korean-tax-calc) and [KoSimpleTax](https://github.com/hyeonki-min/kosimpletax) were read on 2026-11-16. No project was installed, executed or audited. NPS/NHIS links above are navigation handoffs; this router does not claim a legal-content read of those landing pages.

Not yet confirmed: actual reuse rights and upstream dependencies for tax-ui-kr and korean-tax-calc; current-year accuracy, security and completeness of all three implementations; 2026 withholding-table coverage in KoSimpleTax. The former blanket compatibility/direct-reuse claims are not established. These holds preserve the earlier related-project topics without presenting them as tax authority.
