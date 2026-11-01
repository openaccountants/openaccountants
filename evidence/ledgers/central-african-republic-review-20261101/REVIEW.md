# Central African Republic independent pack review

Reviewer: a fresh Codex review agent, separate from the draft writer. Read/recomputed on 2026-11-01. This is source and arithmetic review, not accountant attestation.

Candidate: `2460f6898fd1eb9bc7ddbf211377c617cc7ce7e9` on `codex/central-african-republic-tax-2026`, draft PR 1210, issue 449. Base: `59c23acba2ad66dd2bb29ffc81ffbb9289769ef8`.

**Decision: four narrow corrections are required before this exact candidate can receive independent-review acceptance.** No wrong core rate or example result was found within the explicitly conditional baseline and specifically read amendment scope. This is not acceptance of complete operative 2026 law or a filing-ready pack.

## Corrections

| ID | Exact candidate location | Required correction | Primary evidence and why |
|---|---|---|---|
| R1 | `skills/central-african-republic/cf-transfer-pricing.md:22`; rule T01 and its writer ledger | Change “Direct majority ownership” to majority capital held directly **or through an intermediary**, while retaining actual decision power, common control and privileged/non-cooperative exceptions. | Ministry CGI, art.131(2)(a), PDF p.51: “directement ou par personne interposée”. The current summary omits a material ownership limb. Confirmed in newly rendered `cgi-p51.png`. |
| R2 | `skills/central-african-republic/cf-payroll-social.md:41`; rule W04 and its writer ledger | State that **tax retained or tax due** is payable within ten days of cession/cessation, rather than mentioning only retained tax. | Ministry CGI, art.112, PDF p.35: “les retenues effectuées ou l’impôt dû”. The ten-day rule has both limbs. Confirmed in newly rendered `cgi-p35.png`. |
| R3 | `skills/central-african-republic/cf-tax-overview.md:48` and its Sources table | Link the LPF-creation statement to the signed 2024 Finance Act art.11 and add that source with the actual selective read scope. | Signed 2024 Finance Act, PDF p.35 (printed p.34): “Il est crée un Livre des Précédures Fiscales annéxé au Code Général des Impôts”. The statement is correct, but this Guide currently lists only the 2025 Act, which does not by itself source the 2024 creation claim. |
| R4 | Writer `old-topics.md:74`, item 68 | Explicitly dispose of the predecessor VAT opener’s “in force since 2006” limb: record it as removed because no authenticated primary support was established, or place it on the Guide’s Not yet confirmed line. Do not reinstate it as verified law. | Immutable old VAT blob `c86111b8090cf435809463a1cc8bbfd2c0a3ec68` contains that historical assertion. The generic V01-V14 destination has no 2006 rule or explicit hold. Every old limb must have an honest disposition, even when the old assertion was unsupported. |

Primary URLs:

- CGI: https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf
- Signed 2024 Act: https://www.finances.gouv.cf/sites/default/files/2024-03/Loi%20de%20Finances%202024.pdf

The writer/parent owns corrections. The reviewer did not edit Guides, writer ledgers, the country README, generated artifacts or source caches.

## Checked scope

- All 81 grouped rule records, their numerical and conditional limbs, and all 81 exact Guide placements were read against the primary provisions and neighbours. The count is grouped records, not a count of individual figures. `rule-review.json` records every ID, source, page range, placement and manual outcome. T01 and W04 require the above changes; the other 79 records pass within their stated source limits.
- All 18 fictional examples were independently recomputed and their assumptions compared with the source rules. `example-review.json` contains separate computations; the repository evaluator also passes all 18. A legal-currentness hold is not cleared by correct arithmetic.
- All six predecessor blobs and hashes were checked. The map contains exactly all 62 old bullets plus six opening paragraphs, 68 records in total. `old-topic-review.json` gives an individual destination/disposition check; item 68 requires R4. No rewrite is more than 25% shorter; the drafts expand the old files. Lost content restored: 0 at this review stage; R4 is an explicit unsupported historical-claim disposition, not an instruction to restore it as law.
- The known dangerous stale points were checked in law: corporate agriculture minimum is 0.3%, not 3%; corporate baseline is territorial qualified by the foreign-branch rule; individual annual return is 30 April; signed 2024 VAT replacement repeals the quarterly route, and 2025 preserves the monthly prescribed return/payment.
- OHADA SARL/SA cash payment conditions and deadlines were checked; actual p.95 confirms the single-SA-shareholder sentence missing from the PDF text extraction. National override and current local-form checks remain held. GUFE’s published route was independently opened and read.
- All seven README domains remain partial; current-law, forms, orders, treaty, CNSS and penalty-priority holds remain explicit. New Guides add no platform metadata or CTA. All six existing CTAs and platform-owned fields remain byte/value preserved.
- Parsed descriptions contain 96-100 words. H1 versions match frontmatter 0.1; current research-year labelling and baseline caveats are retained.

## Validation and receipts

`validation.json` records the independently run commands and output: shape checks pass; nine Guides/18 executable examples pass; changed-guide validation passes with the existing warning that the property-tax slug is not mapped to one of the seven domains; strict-metadata audit against the pinned base/candidate has zero errors/warnings/notices; diff whitespace check passes. These are mechanical checks, not substitutes for source review.

`invariants.json` binds the exact nine reviewed Guide blobs and SHA-256 values, six old blobs, descriptions, versions, metadata and CTAs. `source-byte-receipts.json` binds all seven actual primary PDFs and honest read scopes. `source-route.md` records source access and the repository fetch limitation. No TLS, authentication or CAPTCHA bypass was used.

## Items still not confirmed

The full operative 2026 consolidation and complete amendment chain; complete new 2024 LPF and commencement/supersession; current forms, boxes, portals, payment references and implementation orders; CNSS rates/base/ceiling/calendar; operative treaties and relief procedures; current national incorporation overrides; detailed special regimes and tax-base schedules; special/general penalty priority. These are intentionally retained limitations, not declarations that obligations do not exist. All seven domains remain partial and issue 449 must remain open.

No commit, push, PR comment, merge or production write was performed by the reviewer. Acceptance can only be given to a separately identified corrected candidate or checked correction delta; the decision above applies to the exact pinned candidate.
