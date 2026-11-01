# South Sudan independent pack review, 1 November 2026

**Disposition: changes requested for F1.** This is an independent AI review of a limited source-baseline draft. It is not a professional attestation, acceptance of operative 2026 law, or a country-completion certificate.

Reviewed freeze: `f494e992b8dc888530c2998ac9aba0e6db29aaab`. Pinned comparison base: `8935b6fc3a7ff0f773334a45a67448f1efe37b19`. Candidate manifest SHA-256: `ba2eebf0a690a2f65e55496215c6019abbf946804de1a808540a2abbcdf2a36b`. All 23 manifest files matched both their declared hashes and the frozen Git objects. All 11 downloaded PDFs matched the source manifest hashes.

## Finding F1, P2: condition the private-company annual-return package

Locations: `skills/south-sudan/ss-company-formation.md:37` and `:48`; `evidence/ledgers/ss-company-formation.md` row 6.

The table says the s.180 balance sheet, auditor report and director report are attached to the share-capital company return. The adjacent statutory exception is missing. Companies Act s.180(5), PDF 114, says: “Subsection (1) does not apply to a private company unless at least one shareholder is a public company.” A private company with no public-company shareholder is therefore given the wrong attachment requirement even within the opened-law baseline. The general later-law stop gate does not cure an incorrect account of the source already read.

The same annual-return step also omits s.181, immediately below it on PDF 114–115. That section requires a private company's s.177 return to be endorsed with or accompanied by a certificate signed by both a director and the secretary confirming that the company has issued no public invitation to subscribe for shares/debentures since incorporation. Where the return shows more than 50 members, the additional certificate must establish that the excess consists wholly of persons excluded from that limit.

Source actually read: [Companies Act 2012, archived official Justice PDF, capture 9 June 2026](https://web.archive.org/web/20260609050816/https://mojca.gov.ss/wp-content/uploads/2023/03/Companies-Act-2012.pdf), ss.177–181, PDF 111–115. The downloaded PDF is hash-bound in the source manifest. I freshly extracted the actual PDF pages, read s.180(1)–(5), and followed the s.181 continuation onto PDF 115. This is a source-condition finding, with no claim that later company-law amendments have been exhausted.

Required correction: retain the annual-return obligation and s.177 exceptions; state that the copy is signed by **both** a director and the secretary; condition the s.180(1) attachments on s.180(5); add the private-company certificates under s.181. Update ledger row 6, its short quotation/read scope, and the Guide's citation/source range. Keep the current-law/registry stop gate. Recheck the revised Guide and changed ledger row before any limited acceptance.

No Guide, ledger, topic map or original evidence file was edited by this reviewer. Fixes made: 0. Lost content restored by this reviewer: 0. No other substantive contradiction was identified in the other 97 ledger rows within their stated source periods and stop conditions.

## Checks completed

| Check | Actual result |
|---|---|
| Eight Guides read with their ledgers | 98 ledger rows checked against the cited primary-source provisions and nearby conditions; 97 source-period statements supported, row 6 of formation needs F1 correction |
| Exact short quotations | 98/98 found in actual fresh selectable-PDF extraction or captured scan OCR after case, whitespace and typographic quote normalisation; quote matching is additional to, and not a substitute for, the legal reading |
| Arithmetic | All 16 examples independently recomputed from the stated assumptions; repository example evaluator also reports 16 blocks, 0 failures, 0 missing |
| Old-topic destinations | All 85 mapped rows read, checked against the six legacy files at the pinned base, and traced to a named destination or explicit unresolved gap; the five old PIT bands are separately accounted for |
| Descriptions | Parsed actual YAML descriptions: 117, 110, 113, 95, 106, 120, 117 and 117 words in filename order; all meet 80–150 |
| Versions/titles | All eight use version 0.1 and matching title v0.1; pinned-base local strict-metadata audit passes |
| Legacy preservation | All six CTA blocks byte-identical to pinned base; all platform-owned metadata lines exact |
| Two added Guides | No platform-owned keys and no platform CTA introduced |
| Scoped validation | Eight explicit Guide paths; 0 errors, 0 warnings; new-job check uses additions derived from pinned base |
| Source-guide integrity | Local `--base … --worktree --strict-metadata`: 8 source Guides, 0 errors, 0 warnings, 0 notices |
| Whitespace | Pinned-base to freeze `git diff --check` passes |
| Production CAS | Not run. No authentic platform `content_revision` was obtained. No sync/publication permission or pass inferred from a local audit |

The detailed row, source hash, manifest, topic, metadata and arithmetic receipts are in [review-checks.json](review-checks.json). The reproducible local checks are in [review-checks.py](review-checks.py). [scoped-validation.json](scoped-validation.json) records the exact scoped validation boundary.

## Actual source-reading scope

- **Taxation Act, revised edition 2021:** read the definition passages (related persons, residence, tax period), ss.17,24–25,36–39,49,53–59,61–84,92–96 and105–113 as relevant to the ledger. This included wage exclusions and pension provisions, entrepreneur capital restrictions, loss/disposal rules, reciprocal-credit conditions, the peculiar s.92(g) connective, old finality/exemption wording, sales taxable events and manufacturing commencement. The title expressly consolidates amendments only through 30 June 2021. Fresh PDF extraction was used for quotations; other source-reading excerpts came from the actual captured PDF text. No cover-to-cover read claimed.
- **Financial Act FY 2024/25:** selected body, amendment, schedule, company-agency, customs-penalty and assent provisions read in the captured scan OCR. Independently viewed actual images at PDF 11,22,40,42,164,165. The 25 November 2024 assent is handwritten on PDF 165. The body/schedule differences are present in the actual pages; no unsupported precedence rule is adopted. Unrelated tariff/fee pages were not read as a complete tariff.
- **Second ministry FY 2024/25 copy:** compared the captured body/schedule passages and independently viewed PDF 41, which repeats the replacement schedule's 18% sales lines and 30% investment-rental line. The ministry copy corroborates the conflicting publication; it does not resolve legal precedence or later amendments.
- **Companies Act 2012:** freshly extracted/read PDF26–28,32–33,111–115,156–157, covering company/member definitions, memorandum, incorporation, annual returns and directors. The new finding came from the nearby s.180(5)/s.181 clauses. This archived official source does not prove that no later company-law amendment exists.
- **2012 Taxation Regulations:** read reg.1.94's principal/non-principal-employer distinction, marginal method, old paper forms, deadlines and old pension figure. The Guide properly does not adopt the old monetary bands, 8% pension deduction or the old monthly acceleration wording as operative current law.
- **eTax filing manual:** all 19 pages read in fresh PDF extraction. It supports the historical TIN/profile/activity/currency/period/withholding/template/declaration/File Returns/invoice/bank/card sequence. **Registration manual:** PDF26–37 freshly extracted/read, including business certificate/validation, director TIN, old TIN, optional agent and final verification. No live return or registration was tested.
- **Operationalisation circular:** both pages read in captured OCR; actual first-page image independently viewed. It distinguishes 25 November signature from 2 December operationalisation and says until replaced. That does not establish absence of replacement.
- **2 March 2021 pension circular:** full actual image and OCR read. It is addressed to NGOs through RRC and concerns withholding suspension/eligible accumulated payments. It is not a general 2026 contribution-rate instrument.
- **2025/26 draft:** first three PDF pages freshly extracted/read for identity, showing Finance Bill FY2025/2026. No proposed rate is treated as enacted. The FY2023/24 PDF was hash-checked and remains a context source, not a reviewed intervening-law chain or a certification that historical bands stayed unchanged.

No repeated web requests were needed to decide the ledger claims because the actual primary documents and source capture receipts were available offline. This review does not claim an exhaustive fresh catalogue, gazette or amendment search. No access block was bypassed.

## Remaining acceptance boundary

All seven domains remain partial. A correction of F1 can support only limited source-baseline acceptance on a new hash-bound candidate. It cannot establish operative 2026 law. The June 2021 to FY2024/25 intervening chain is not fully reconciled; enacted FY2025/26 and FY2026/27 are not established; an official draft is not a substitute. Sales body 20%/produced1–20% versus replacement-schedule18% and valuation differences remain unresolved. Rental body20% versus schedule30% and taxpayer scope remain unresolved. Current social-insurance enactment, coverage, rates, base, registration and remittance remain unresolved.

The Guides correctly separate pension deduction caps from contribution rates, rent withholding from net-rent liability, government-contract withholding from private invoices, foreign-credit reciprocity from automatic relief, and a documented manual from a completed present-day filing. Those useful distinctions do not close the remaining gaps. No current filing, payment, accountant attestation, production write, PR, commit, push or country-issue closure was performed.
