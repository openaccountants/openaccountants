# Gibraltar continuation, 31 October 2026

This is a staged country batch for existing PR #778, not full-country acceptance. No push has been made. All seven `partial:` entries remain in the country README.

## What changed

- Current main `ebbf73add3970c1e8a4a4dadc2b3cf8c018c35c2` was merged normally at `53696ccc7`. Fourteen path/add conflicts retained the accepted Gibraltar branch versions. The 170 existing research files moved byte-for-byte from obsolete `skills/research/gibraltar-2026/` to `evidence/research/gibraltar-2026/`; path-migration.json binds those files.
- `gi-global-minimum-tax` v0.3 now includes the current registration, Article 8.1.3 notification, GIR XML validation/submission and GMTA1/payment workflows. The old guidance URL returned 404 on direct fetch and normal browser. The replacement documents were discovered through the official current AEOI landing page, not guessed filenames.
- The complete 35-row ledger covers original rules as well as new workflows; all30 original substantive units are mapped in old-topics.json. Exact old calculation/election text is preserved except the version/review line and two expressly superseded operational-gap sentences. Both original oa-check blocks are retained.
- Six other Guides have only source-date/row-URL and relative-evidence-link repairs, with version/date increments. mechanical-preservation.json proves all1179 original nonblank body lines retained in order, with only known link rewrites or source URL/date suffixes; all12 executable blocks in those six files are byte-exact. Platform/author/trust metadata is unchanged.

## Sources and boundaries

The 10 February registration, 1 June notification, 11 June GIR guidance and June GMTA1 were downloaded from exact links on https://tax.egov.gi/aeoi.html (the current destination of https://aeoi.egov.gi/). Their full text was read, including neighbouring exceptions and appendices. Registration physical page8, notification physical page12, GIR physical page13 and GMTA1 page3 were rendered and read to check the visible form/receipt/payment requirements. The original Act, Allowances Rules, Income Tax Act and Model Rules Article1.1 were re-fetched for the full ledger; source-receipts.json binds raw and extracted text bytes. Existing specialist exclusions remain explicit. No tax-authority email, enrolment, live return or payment was sent.

The current payment method uses the assigned unique top-up reference; no bank details were transcribed into the Guide. The accepted-GIR amendment workflow remains unprovided in the current June note, which explicitly directs the filer to seek instructions. Technical `Submitted: Valid` status is not substantive approval. The special2024 common-understanding concession is not a general filing extension.

## Current validation

- New minimum-tax Guide: all10 mechanical skill checks PASS; both original arithmetic blocks PASS.
- All seven canonical tax Guides in this staged change: all10 checks PASS each.
- Whole Gibraltar examples: 19 Markdown files inspected,29 oa-check blocks,0 failures. `README.md` and general Guides are not forced to invent tax arithmetic by that checker.
- Whole changed-country schema/PR validation: **FAIL,11 errors and55 warning groups**. The errors are pre-existing in eight unchanged older Guides: missing Sources headings/read dates, and missing executable controls in formation(0), appeals(1), reliefs(0). The full skill-check log also records their noncanonical shapes and rates-row gaps. These results do not establish a green PR or complete country.
- `git diff --check`: PASS.

Review this exact staged batch before any push. The full objective remains every applicable tax job, a correct README and green PR #778. Remaining work is listed below and is not waived by this checkpoint.

## Remaining work before full-country acceptance

| Area | Precise unresolved work |
|---|---|
| IT-IND | Part-year ABS/GIBS eligibility and cross-reference; printed senior/dependant and special-home wording; property/energy cross-scheme/claim and credit interactions; disabled-access certificate reference; authority for SI deduction; actual future-year authenticated fields. |
| IT-CORP | Section16(6) extended-period boundaries; Schedule10 anomalous allocation dates; Schedule3 paragraph9(6) disposal wording and paragraph2(1)(o) Gazette guideline identity; current CT4 submission route, additional ordinary claim interactions. |
| Minimum tax | Full fiscal-year OECD guidance/notice reconciliation and complete GloBE income/covered-tax/deferred-tax/substance/safe-harbour/input derivation and IIR allocation; accepted-GIR amendment detail; rule3AA election/cessation operation and specialised cases. New compliance workflows do not close these computation gaps. |
| Consumption/customs | Section102 export-refund form/deadline; warehousing endpoints; any valid post12October deduction extension; commodity/traveller/aid-case evidence and remaining treaty-transition applications. |
| SC and PR | General first-employer/concurrent-job allocation; ordinary missed employee-SI wage recovery; statutory quarterly versus published annual self-employed schedules; conflicting published PAYE illustrations/grey cells; benefit-threshold wording and pension-definition reference. Do not invent an employer deduction or disregard a statutory schedule. |
| TP | PartV group-wide floor allocation/currency/current-return implementation and paragraph18(6) cross-reference; genuinely applicable documentation/reporting scope. No local-file exemption is inferred from an unlocated form. |
| XB | Domestic section37 relief claim/correction submission, FX and assessed-but-unpaid/source cases; actual exit-deferral dates/payment/interest and asset-transfer-definition mismatch; remaining Spain residence/treaty claim channels and UK arbitration operation. |
| Property/other tax jobs | B05/2025 enacted status and commencement remain unproved; stamp-duty reliefs/security/lease/gift scope and actual certificate/payment route; disposal historical aggregation/timing; domestic refund submission/interest and liquidation successor cross-reference; remaining incentives. |
| Standards and publication | Repair the11 current validation errors and inherited shape/source/rates gaps without deleting old topics; complete the applicable tax-job inventory; independent review of new substance and mechanical preservation; then push once to existing country PR, await all required checks and mark ready only on evidence. Accountant attestation is a separate trust state. |

Accounting-pack work (bookkeeping/e-invoicing/full accounts/formation alternatives) remains visible in the README and is not counted as a completed tax pack. The user's broader “every tax job” scope has not been redefined around the seven core domains or around the seven canonical Guides.
