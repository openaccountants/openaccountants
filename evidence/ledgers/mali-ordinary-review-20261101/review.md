# Mali ordinary follow-on independent source review, 1 November 2026

Candidate: `15a570e0ef8904526c8814232cb4d9839feb5951`. Base: `59c23acba2ad66dd2bb29ffc81ffbb9289769ef8`. Reviewer is a separate Codex agent from the writer. Review reads were against immutable candidate Git blobs and the cached official source originals; it did not edit any Guide, commit, push, attest, merge or publish.

**Initial disposition: repair required.** All 119 source-rule rows and the shared currentness row were checked against actual source passages and their relevant neighbours. Four source-condition repairs and one description correction are recorded below. These are changes to the identified older/undated source workpapers; this review does not approve operative 2026 law.

## Findings

| ID | Candidate location | Required repair | Primary source |
|---|---|---|---|
| R1 | Corporate, rates row and base step 4; ledger 06 | State that the additional art. 86 final-paragraph floor applies when turnover is at least the real-regime threshold. Below-threshold opt-ins exist, so real-regime membership alone is insufficient. Keep actual floor computation held. | CGI art. 86, final paragraph, cached text lines 1915–1919; art. 70 and 76 option neighbours; https://www.dgi.gouv.ml/CGI/ |
| R2 | Payroll, CFE rates row; ledger 09 | State the art. 159 taxpayer condition: persons subject to IS, IBIC or agricultural-profit tax. Add the condition to the example assumption. The CFE employee exemptions are a different question. | CGI arts. 159–163, cached text lines 4214–4239; https://www.dgi.gouv.ml/CGI/ |
| R3 | VAT, late-filing penalties; ledger 27 | Make the XOF 50,000 minimum apply expressly to all stated branches, including pre-notice 25%/5%, as well as the post-notice 50% branch. The source says “Dans tous les cas”. | LPF art. 119, cached text lines 10581–10601; https://www.dgi.gouv.ml/CGI/ |
| R4 | Corporate, simplified-instalment rates row; ledger 20 | Replace “local-supply petrol stations” with the explicit exclusive-local-sourcing condition for the 0.20% coefficient. Partial local procurement is insufficient. | LPF art. 276, cached text lines 12013–12031; https://www.dgi.gouv.ml/CGI/ |
| E1 | Payroll description | Replace “dated government guidance” with “undated government guidance”, consistent with the actual RSU page and body. | Undated RSU INPS page; https://rsu.gouv.ml/portail/partenaires/inps/ |

The DGI source HTML SHA-256 is `32cbd24e5cbd327d8a6c1e6b327cd62de5ffda541aa1f33c80bdb52012b737f5`. Each row in [row-verdicts.json](row-verdicts.json) carries its original source hash, extracted-text hash, exact quotation line spans, candidate Guide hash and reviewer interpretation. All seven original source hashes match the writer manifest. Short repeated quotations were located within the relevant provisions, not merely the first same string elsewhere in the code.

## What was independently checked

- All 34 corporate, 24 wage-income, 30 payroll/social and 31 VAT ledger rows, plus the one shared finance-law currentness row. The relevant CGI/LPF passages, original 2016 wage-band enactment, complete 2024-grid bulletin reply, original 2010 AMO decrees and complete relevant INPS guidance sections were read. AMO rate/base/calendar and penalty pages were visually checked against the saved page images.
- All eight worked cases were independently reconstructed with Decimal arithmetic from the source rules and stated inputs, then compared to the candidate prose and expected results. No arithmetic errors remain. Results and boundary assumptions are in [independent-examples.json](independent-examples.json).
- All 75 original headings/bullet labels and all four original introductory/prose paragraphs were checked against the full immutable base blobs and their stated destinations. Unsupported older rates/deadlines have corrected or held destinations. Lost content restored: 0. [old-topic-review.json](old-topic-review.json) records every item.
- All six existing complete CTA blocks and every listed platform-owned field were compared byte-for-byte/value-for-value. Formation, overview and the accepted historical CSS Guide are entirely unchanged. CSS retains tax year 2025, version 0.2 and its 2026 hold. All 17 prior Mali evidence records retain their base Git blobs. [candidate-and-preservation.json](candidate-and-preservation.json) binds the hashes.

The wage examples correctly stop at the articles 9–11 intermediate subtotal. The neighbouring articles 12-A/12-B formula is unresolved and is neither silently omitted nor interpreted as final ITS. The corporate cases assume the separately identified additional floor has been settled below the computed turnover minimum; that assumption does not resolve the actual floor. INPS figures are authority-guidance statements, not legislation/current-year approval. ANPE is included once and separately from insurance, housing, training and youth-employment tax. AMO headcount is below ten quarterly versus at least ten monthly, with the later ministerial-order power held.

## Currentness and preservation boundary

The shared gate is supported by Loi 2025-056 article 46 and neighbouring articles 43–49: the enacted 2026 fiscal annex is separately identified as Annex U and was not obtained/read. No complete post-consolidation chain is proved. The August 2025 DGI bulletin speaks to the 2024 grid; it is not evidence of continuity into 2025 or 2026. Original AMO decrees and undated INPS guidance likewise do not prove continuity. `tax_year: 2026` here labels a research intake, with explicit body warnings, and does not establish operative 2026 approval or any retrieval/publication safeguard.

All seven core domains remain applicable and partial. TP and XB remain missing, issue #471 remains open, and this review supplies no accountant attestation. Current-year approval/publication remains blocked by the stated source gaps. Unchanged formation/overview claims are preserved, not recertified. Existing CSS receipts apply only to their historical frozen candidates.

A fresh `git fetch origin` attempt failed because the shell could not resolve `github.com`. No current-remote assertion is made: the review is pinned to the supplied immutable candidate and base. A repaired candidate requires a separate additive closure bound to its exact Guide hashes; this record remains the initial receipt.
