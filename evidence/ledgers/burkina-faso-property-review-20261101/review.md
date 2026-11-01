# Burkina Faso company property tax: independent conditional source review

Accepted for the limited, conditional source fidelity of this ordinary TFS workpaper at frozen commit `13a38f884550d6d220f79100a8fbc1404842a1de`, read on 1 November 2026. **30/30 ledger rows checked; zero substantive corrections required; both executable cases independently recomputed.** This is an independent AI source review, not accountant attestation, certification of all 2026 amendments, authenticated filing verification, country completion or permission to merge.

## Frozen inputs and source identity

The branch was `codex/burkina-faso-remaining-guides-2026`; the earlier accepted ten-Guide checkpoint is `f7482aabcf34d114499f3b621beb1027cc406d5c` and main base is `59c23acba2ad66dd2bb29ffc81ffbb9289769ef8`. Remote fetch succeeded after the sandbox's initial DNS failure. HEAD matched the frozen review request. [Input manifest](input-manifest.json) records the Git blobs, SHA-256 hashes and working-file identities of the Guide, README, standards and all existing property writer evidence.

The accepted Guide SHA-256 is `cd4f4f84ee95d7469f40835acd9dab58d8d4fc36de2c6b0e714c26c29f1ea16d`. The JSON ledger SHA-256 is `2c1b42368b96c1bb14238716f60a1a05549a20d6650e16c8860842a0ff8b3fe2`; the human ledger SHA-256 is `c45ac1f39574b3f32d1f355eec4954c1af852cd7128c220310cbcd9cf438cc92`.

Both cited official URLs timed out in the web reader. Independent direct retrieval from those same official URLs succeeded; each PDF is byte-for-byte identical to the writer's binary. Actual full clauses and neighbouring boundaries were then read from the PDFs/extractions, with the controlling property and penalty pages visually checked:

| Primary source | Identity and scope actually checked |
|---|---|
| [Official CGI 2026](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) | SHA-256 `a8acc390c74bc605540ad493c09e6f9381b5a20148b8804810a164256f7f8c5c`. Full arts.251–257, printed/physical pp.107–108; preceding licence and following residence boundaries pp.106–109; full general contribution exemption clauses arts.271 and 273 with chapter/taxable-person/base neighbours pp.112–115; full collection arts.669–679 pp.286–288 and neighbouring enforcement clauses; full art.772 and adjacent other-tax penalty branches pp.307–309. Edition identity/preface/warning also read. Pages 107–108 independently rendered and visually checked. |
| [Signed Finance Law 021-2025/ALT, Gazette spécial1, 2 January2026](https://dgi.bf/wp-content/uploads/2026/01/JOURNAL-OFFICIEL-N%C2%B001-SPECIAL-LOI-DE-FINANCES-2026.pdf) | SHA-256 `24242939052ac8dc40b6b59e9dd5e89b5e72e5f29aaeed6362cefa97a02f7d6a`. Promulgation p.2 visually read; full art.34 and replacement CGI 772 p.18 independently rendered and visually read, including chapeau, all three branches and express commencement. Neighbouring arts.30–36 pp.17–19 read. Printed/physical Gazette p.18 includes embedded law manuscript footers 31–32; those footers are not the Gazette locator. |

[Source read log](source-read-log.json) records actual scopes and outside-Git paths/hashes. Fresh downloads, independent selected-page extractions and renders remain in sibling `sources/property-review-20261101/`, outside Git. This is not a reading or certification of the complete CGI, Gazette, special exemption chain or later amendment chain. No additional-source research was needed: no substantive cited-source check failed.

## Every row and legal conditions

[Row verdicts](row-checks.json) record a separate conclusion and clause/condition note for all P 01–P 30, comparing the JSON ledger, human ledger and actual Guide text. The count is 30 article/rule records, not 30 distinct numerical figures.

The company scope is the five enumerated forms in art.251, not every entity paying IS. January 1 owner/usufructuary liability for the entire year and the construction-lease landowner rule are preserved. Both art.253 exemptions retain their conditions; the exclusive-object share-company exemption does not cover exploited or non-sale properties. Foreign-form equivalence and special regimes are held.

The Guide correctly separates statutory rental value from cash rent, follows the art.255 valuation sequence and includes the indispensable immediate land dependency. The construction-lease annuity is stated as the legal rule, with its operative computation held. Art.254 gives the ordinary 50% deduction but removes it where the tenant bears major repairs. The 10% tax is on the applicable base; an unconditional 5%-of-rent shortcut would be wrong. Disputed contract classification is not resolved by the illustration.

Art.257's before-November 1 declaration deadline and production-day particulars remain distinct from the January assessment date and from payment. All three statutory declaration items are carried: tenant particulars/rent/charges, rent-free occupation, vacancy. P 18's locator 257(2)–(3) is overinclusive: the rent-free clause is item 2; item 3 is separately covered in P 30. This includes the right operative provision and causes no substantive error.

The signed art.34 expressly applies **from 1 January 2026**. All three full replacement branches match the Guide: inaccurate/omitted assessment elements 25% with XOF 100,000 floor; late payment 10% plus 1% per month or fraction; taxation d'office 25% with XOF 500,000 floor. The Gazette publication date is not substituted for commencement. The two floors are not interchangeable. Neither sanction stacking nor the first late-payment day is established.

General contribution foncière exclusions in arts.271/273 are kept separate from TFS and from IS, residence tax, IRF, lease/transfer charges. General collection arts.671–678 are used only as such. They do not supply an invented ordinary TFS payment calendar or an authenticated portal workflow.

## Cases, shape and preservation

[Independent cases](independent-cases.json) use separate Decimal arithmetic and legal decisions, rather than merely executing the Guide expressions:

| Case | Independent result and decision |
|---|---|
| Owner-occupied SARL, assumed supported annual rental value XOF 6,000,000 | Deduction 3,000,000; base 3,000,000; TFS 300,000. Art.255(1) supplies hypothetical rental value for self-occupation; zero cash rent is not zero statutory rental value. |
| Same assumed supported annual rental value XOF 12,000,000, alternate legal repair burdens | Owner major repairs: base 6,000,000, TFS 600,000. Tenant major repairs: base 12,000,000, TFS 1,200,000. Difference 600,000. Art.254's second paragraph changes the calculation; this is not a free election. |

[All15 shape checks pass](shape-checks.json). The independent [actual committed validation](validation.json) selects 10 Markdown paths including README and checks 9 Guides; it passes with the known warning that the property slug has no seven-domain classifier. README explicitly routes this distinct property job, so this warning does not establish a duplicate or a new completed domain. Strict metadata audit checks 9 source Guides with zero errors, warnings or notices. The actual property executable checker passes 2 blocks; pinned-base committed whitespace check passes. No full-tree inventory regeneration, live filing, production sync or full-suite country validation is claimed.

[Preservation checks](preservation-checks.json) independently compare every earlier Guide and Burkina evidence blob to `f7482aabcf34d114499f3b621beb1027cc406d5c`: **10/10 earlier Guides and 102/102 earlier evidence files are exact**. Working files also match where materialized; sparse-absent files are checked as Git blobs. README equals the exact predecessor plus the recorded append. Zero old bodies replaced; zero predecessor topics moved/retired. **Lost content restored:0**, because no predecessor content was removed by this additive job. The old files themselves are their complete destinations. All seven domain-partial declarations remain unchanged.

## Limits and permitted status reconciliation

No substantive findings remain in this frozen scope; [findings record](findings.json) preserves the one nonblocking locator observation. No Guide or writer evidence was edited by this reviewer. The initial writer ledgers, freezes and all validation receipts remain historical evidence.

The Guide's explicit holds remain: actual valuation/comparables/yields, construction-lease annuity execution, disputed major-repair/foreign-company classification, current declaration model/fields/submission/acknowledgement, ordinary payment calendar, special investment/convention/sector exemptions, wider amendments, detailed enforcement/objection/interest-counting/sanction accumulation and the separate property jobs. These are not silently certified, invented or converted into demands for live credentials. All seven country domains remain partial.

The parent may reconcile only the two exact stale status literals in [status-only permission](status-only-permission.json). That receipt binds the accepted before-hashes, exact old/new wording and computed after-hashes. It covers no tax-rule, figure, case, coverage, metadata or attestation change. Preserve this initial review and all initial writer evidence; append a status-identity receipt and rerun relevant validation. Any other substantive content change requires fresh review. This review grants no commit, push, PR action, merge, issue closure, attestation or country-completion authority.
