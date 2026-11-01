# Independent Moldova VAT-refund delta review

Initial verdict, 31 October 2026: CHANGES REQUIRED on four narrow items before accepting this delta. The source data and preservation audit pass. This is a finite review of the new job and layout/map delta, not a fresh whole-country completion review.

Exact reviewed HEAD: `6637d0dbfa6d032194ebe24306c46e7f2d7a88e9`.
Independent input manifest: `initial-input-manifest.json`, SHA-256 `44fc12c6ce8ecf8649418fae272da6d9808b768233199833fc241043aae09718`, pins all31 files introduced/changed in that commit. New Guide SHA-256 `c69fe5df8392018bbf5836d1346a0302987b435d1fc03fa6e52364d69f58e55d`; ledger JSON `f4363fa4b19f81078a899948c103776846b57627baa1cab3e2ccf3253108cc6a`; ledger Markdown `0f3cf151d4cb794b01be47d4c22b042a49fcf50c7bca6d5a3dd65e7e9ac1c75b`. Inputs matched HEAD and were rehashed at verdict. Review creates its own files only.

Read first: applicable CLAUDE.md, docs/skill-template.md standard, docs/OWNERS.md European ownership/publishing sections. No writer conversation was supplied. The original3913-row review remains sealed and is not rewritten or retrospectively expanded.

## Four findings

1. **MD-DR-01, P2:** ordinary exempt-with-credit paid-input cutoff omitted. HG93 point35¹(2) measures paid deductible VAT at initiation of the audit. The row and connected base method need that date beside the ordinary paid-credit condition. The investment row already states its cutoff. This is a payment eligibility condition, not an arithmetic error.
2. **MD-DR-02, P2:** e-Factura route needs its registered-VAT-payer condition next to eligibility. Code101⁶(1) expressly sets it, while the Guide also serves a nonregistered vehicle route.
3. **MD-DR-03, P2:** the current Code101⁴ repeal is absent from the184-row ledger. It is correctly retained in the source capture and described in the Guide, but the first-paragraph-skipping row generator drops this one-line article. Add a separate exact-source row. Do not amend the existing sealed predecessor review.
4. **MD-DR-04, P3:** add the template's required General reference notice after the new Guide's H1. No platform CTA change is called for.

Precise fields, source URLs and quotes are in initial-findings.json. No writer tax claim was rejected on memory or secondary commentary. These findings require small documented repairs and a bounded follow-up hash check; no broad research restart is required.

## Every source binding and actual sources

184/184 source bindings checked:50 operative HG93 point blocks (including full conditions/subpoints),62 current Code text fragments,29 approved application field/paragraph fragments and43 official worked-control fragments. The count is source bindings, not184 independent tax figures: some rows are headings, labels and split original paragraphs. Each row's quote membership, context hash, date and official URL were recomputed independently; all pass. Full current HG93 body and the selected current Code provisions were independently read and assessed against the actual Guide prose. This source reading, not the membership script alone, produced the two missing-condition findings and the missing repeal receipt.

Direct fetches were inaccessible/403. Normal browser visits succeeded for [HG93/2013](https://www.legis.md/cautare/getResults?doc_id=152472&lang=ro) and [Fiscal Code1163/1997,157050](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro). Current HG93 body shows HG829 effective1January2026; current Code shows LP235 effective30October2026. Entire HG93 body was read in three overlapping ranges; Code101 through101⁸ (including adjacent101⁵),176 and266 were read. No CAPTCHA or disguised requests; no archive necessary. The current regulation's actual two attachment hrefs match the retained official DOCX URLs.

Both original DOCX SHA-256 hashes match the source manifest. All72 application/control fragments independently match the original OOXML, not merely a writer-produced text reader. The complete saved render of each one-page original was visually inspected: named identity/amount/law/period fields, same-month note, IBAN, future-tax allocation table, arrears note, date and manager signature; official2¹ example table and unpaid-first ordering. No blank-form field was invented as a numbered portal box. Read-only inspection used the documents skill; no original document was edited.

| Source block | Review result |
|---|---|
| HG93 points1–8,11–18 | Correct ordinary request, amount, matching return, ordering, audit/deferred-audit tests and special exclusions; no portal acceptance claimed. |
| HG93 points19/19¹,22–30 | Correct ordinary45 days, return-deadline start,60-day disagreement route,22/4/8 stages inside the total, decisions, Treasury stage, historical/supplementary-claim tests. |
| HG93 point31 and full32 | Registers/e-Factura paper exception and actual export/service/transport/zone/investment proof read. Guide states ordinary goods/services method and directs special supply proof to its exact subparagraph; remaining specialist programmes stay open. |
| HG93 points34¹,35¹,36–38¹ | Vehicle condition and ordinary amount/order supported. MD-DR-01 requires the ordinary audit-start payment cutoff in operative prose. Utility-specific source paragraphs are retained as evidence, not claimed as a new comprehensive utility method. |
| HG9339¹,41,42¹–44,45¹–47¹ | Producer, leasing and investment caps supported. PPP text remains in the regulation, but is not promoted above the repealed Code article. Programme-specific implementation remains open. |
| HG9347³–47⁵,48–51 |70% and paid-excess/e-Factura chronology, energy cap/payment date, historical gas special route and late-authority responsibility read. Historical gas scheme is expressly left incomplete, not silently treated as ordinary45 days. |
| Code101,101¹,101³,101⁴ | Excess-credit distinction, paid caps, current commissioned-and-used building rule, nonregistered8702 vehicle route, creditor/assignee bar and PPP repeal correct. Add repeal ledger receipt. |
| Code101⁶–101⁸ | e-Factura per-period cap and requested-refund carry reduction, reverse-charge taxpayer/supply conditions and storage route read. MD-DR-02 requires local registration condition. Storage implementation stays outside a completed-method claim. |
| Code176,266 | Statutory interest formula, criminal-proceeding suspension, submitted calculation/authority approval and six-year application limit correctly described. |
| Annex1 and2¹ | Actual form fields/notes and official paid-unpaid worked control match; both supplied examples recompute. |

The Guide correctly gives the current commissioned-and-used Code101¹ building rule priority over older regulation text and states that HG93 PPP references cannot revive repealed Code101⁴. It distinguishes paid VAT from deductible invoices, unpaid-first output allocation, separate e-Factura chronology and per-route ceilings. The source hierarchy is sound; its repeal evidence needs the ledger binding noted above.

## Examples and preservation

All22 pack oa-check blocks recompute with0 failures (11 Guides plus README passed to the checker). The new Guide passes all10 mechanical skill checks; the required notice/operative-condition omissions demonstrate why those checks do not replace this review.

New example1 was manually recomputed against actual annex2¹: total paid1300/unpaid2200, output2000 against unpaid, remaining overall1500, refund min(1500,1300,1200)=1200; carry300=paid100+unpaid200. New example2: paid excess15000,70% cap7000, confirmed7000; offset1500, bank5500, carry8000. The second case assumes actual wholly eligible facts and zero old/unpaid credits; it does not prove scheme eligibility or Treasury cash receipt.

Independent old/new comparison proves all10 predecessor tax methods and stamped CTA suffixes unchanged, apart from evidence/documentation path repair, monotonic matching version/H1 changes and the VAT refund pointer. One substantive old-topic sample per Guide was also checked; the VAT destination ledger has242 units. All669 relocated historical evidence files match both recorded hashes and the remote predecessor Git blobs exactly. The shortened README's predecessor is preserved byte-exact under layout-20261031. Lost content restored:0; no predecessor tax rule removed. The immutable3913-row/58-case/80-topic prior review was preserved, not rerun.

## Coverage honesty and remaining work

All seven applicable domains retain partial flags. The concise README is a map, links the new refund job and the prior bounded review, and makes no professional attestation or country completion claim. Its general property/local/other-tax audit sentence is consistent with the separately retained current-Code job inventory: excise, property, wealth, local, resources, roads and tax administration still need complete operative methods. New Guide explicitly keeps agricultural/storage, legacy PPP workflow, historical gas/machinery/project routes, authentic submission/acceptance, taxpayer-specific payment validation, appeal facts, FX and historical transitions open. These gaps are still part of the full objective.

No GitHub CI, push, platform-ingestion or authenticated filing was performed. Existing writer validation results are evidence of mechanical checks only. After the four fixes, issue a new input manifest and append a bounded closure record without overwriting this initial report or prior review evidence.
