# Independent corporate and cross-border source review

Frozen head: `935b20f97eca049de7809ed31d39883472dac7af`. Immutable base: `aec6ba04066bb69d1168c8028ba11dd65cb90505`. Draft PR 1202; issue 484. Reviewed on 2026-11-01.

**Four targeted placement repairs are required before accepting these as conditional source-reference workpapers.** This does not establish the whole operative 2026 law or merge readiness.

Checked all 36 corporate and 18 cross-border grouped records, including every numeric and conditional limb, all 15 predecessor corporate topics and all four fictional examples. “54” is a count of grouped records, not atomic figures. All four examples recompute. No predecessor topic was silently lost. Lost content restored: 0.

## Required repairs

| ID | Guide location at frozen head | Problem | Exact source and repair |
|---|---|---|---|
| CX-R1 / C12 / P2 | Corporate, line 43, base step 2 | “Business-asset gains” omits the depreciable-asset exclusion; the ledger's business-debt gain limb is absent from this step. The next step separately deals with pool balancing, so the shorthand can invite double counting. | ITA s.24(a)-(b), physical PDF 27: “business assets (other than depreciable assets) or on the satisfaction of business debts”. State non-depreciable business-asset disposal gains, business-debt satisfaction gains and s.39(8) balancing inclusions distinctly. |
| CX-R2 / C16 / P2 | Corporate, line 45, base step 4 | The ownership-change restriction names new business but omits new investment. | ITA s.88(b), physical PDF 56-57: “does not engage in a new business or investment except with the approval of the Commissioner”. Include new investments as well as new business; preserve the three-year condition and currentness/cross-reference warning. |
| CX-R3 / C23 / P2 | Corporate, line 55, estimate calendar | The estimate/revision dates omit the substituted-year alternatives, despite giving substituted instalment dates immediately afterwards. | ITA s.113(1)-(2), physical PDF 70-71: “on or before the end of the first month”, “on or before the end of the fourth month”, and “on or before the tenth month”. Qualify January/April/October dates as the ordinary-year baseline and add these alternatives. Keep the unusual tenth-month wording exact rather than inventing a confirmed month-end deadline. |
| CX-R4 / X12 / P2 | Cross-border, line 42, base step 6 | The foreign-branch aggregation instruction omits the resident-company limitation. It must not imply that a resident individual's branch gets the same pooling permission. | ITA s.90(4), physical PDF 58: “a foreign branch of a resident company is aggregated and considered a single receipt of income”. State this limitation next to the aggregation instruction and in its grouped ledger/table statement. |

All four findings use the [NRA-hosted Income Tax Act consolidation](https://webtestcms.nra.gov.sl/uploads/Income_Tax_Act_2000_as_amended_to_Finance_Act_2017_1_83760e046c.pdf). Its physical page 2 expressly calls it unofficial and non-authoritative. These repairs improve the accuracy of the stated historical baseline; they do not certify its full 2026 survival.

## Verified limits and preservation

Both Guides preserve the unofficial 2017 baseline limitation. The opened enacted 2021, 2023, 2024, 2025 and 2026 texts support their specifically described amendments. They do not close the full amendment or subsidiary-instrument chain. The 2026 higher-of MAT comparison is correctly restored; the interaction of the 2024 resident prior-loss 2% insertion with the broader 2023 3% insertion remains held. No universal MAT rate is approved.

Current loss/ownership interaction, financial-cost instruments, withholding finality, branch rate, foreign-employment exemption currentness, treaties, forms and payment procedures remain subject to the drafts' existing holds. The worked cases demonstrate arithmetic and conditional decisions only.

The four legacy 2025 Guides are byte-exact to the immutable base. Corporate platform fields and the complete CTA suffix are byte-exact; the new cross-border Guide has no platform fields or CTA. Both descriptions have 115 words. Versions 1.0 and 0.1 agree with their H1 headings. Both remain tier 2 with no accountant attestation. All seven domains remain partial. TP/payroll Guides and prior closure evidence remain byte-exact to the frozen head; their law was not re-reviewed.

## Validation and access

- `check-examples.py --require`, on exactly the two Guides: 2 files, 4 blocks, 0 failures, 0 missing.
- `validate-guides.py --changed-only --no-index-check`: passed; 4 changed tax Guides checked, 0 warning groups.
- `check-sync-integrity.py --base aec6ba04066bb69d1168c8028ba11dd65cb90505 --mode audit --strict-metadata`: 4 source Guides, 0 errors, 0 warnings, 0 notices.

All six distinct cached PDF hashes and byte counts match the writer manifests. Fresh `pdftotext` extraction matched each cached text after whitespace normalization. Critical 2024/2025/2026 booklet halves were visually inspected. The actual read ranges and visual page numbers are recorded in the source manifest. Temporary extraction and render copies were removed after inspection; the original hashed primary files remain in the supplied cache.

`git fetch` failed because DNS could not resolve github.com. Direct web opens of the ITA and Finance Act 2026 returned 502; the subsequent normal browser visit to the Finance Act 2026 showed a blank PDF surface. No remote content is claimed read, and no TLS or other security bypass was attempted. The substantive review uses the original hash-matched primary captures supplied for this task. It does not claim a fresh remote currentness check.

## Evidence

- `all-records.json`: all 54 source checks, article/page, quote, placement result and conditional scope.
- `old-topics-review.json`: all 15 immutable predecessor quotations and actual destinations.
- `worked-cases.json`: independent recomputation of all four examples.
- `scope-preservation.json`: exact input SHA256 scope, metadata/CTA, legacy and prior closure checks.
- `source-read-manifest.json`: source hashes, actual read ranges and visual pages.
- `findings.json`: four actionable repairs and proposed wording.
- Separate logs contain the three requested validation results.

Only this review folder was written. No Guide, writer ledger, README, existing generated file, source cache, commit, push, PR comment, merge or production system was changed.
