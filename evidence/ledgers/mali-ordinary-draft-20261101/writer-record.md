# Mali ordinary-tax research draft, 1 November 2026

Base: `59c23acba2ad66dd2bb29ffc81ffbb9289769ef8`, fetched `origin/main`. Branch: `codex/mali-remaining-guides-2026`. The former branch remains intact. Issue #471 comments and open Mali PRs were inspected before drafting; no competing writer/open PR was found. This writer did not push, create a PR, comment on an issue, merge or touch production.

## Actual work

Four legacy ordinary Guides were rebuilt in place as **conditional 2026 research workpapers**, not current-law opinions: corporate income tax (34 source-rule rows), wage income tax (24), payroll/social (30) and VAT (31). The [shared currentness gate](currentness.md) adds one row: 120 source-rule/currentness rows in total. Each ledger names the Guide section, source rule, act/article, official URL, short exact French quotation, actual read date and source scope. Hypothetical inputs in the eight examples are explicitly assumptions, not tax figures.

The sources are the DGI's older CGI/LPF consolidation, the original 2016 wage-band law, DGI's August 2025 clarification about the 2024 grid, the original 2010 CANAM AMO rate and collection decrees and an undated government INPS page. Their precise capture route, hashes and read boundaries are in [source-record.json](source-record.json). None proves an unchanged 2025 or 2026 chain. The missing enacted Annex U was not guessed or replaced by a proposed bill. All source PDFs, HTML, renderings and full OCR/text remain in the private sibling `sources/` cache, outside Git.

Substantive repairs include the corporate four-month return period; source-specific interest/payment characterisation; non-resident wage residence/work/payer tests; the housing/training/youth/ANPE distinctions; AMO bases and headcount calendar; and VAT mode, export/deduction, tax-point and shared-input rules. The neighbouring ITS articles 12-A/12-B describe additional two-point relief with an unresolved online multiplication base. The wage cases stop at the supported articles 9–11 intermediate subtotal and do not claim final tax. Corporate minimum examples assume the separately identified additional minimum floor has been settled below the computed turnover minimum; actual floor computation remains held.

## Preservation

[old-topics.md](old-topics.md) maps all 75 former headings/bullet labels and all four introductions/prose paragraphs across the six legacy Guides against immutable full Git blobs and SHA-256 values. Unsupported claims have a correction or explicit held destination, not silent deletion. [preservation.json](preservation.json) proves the six existing complete CTA blocks and all platform-owned metadata fields are unchanged. The merged CSS Guide is byte-identical to base, including its accepted historical `tax_year: 2025`, version 0.2 and mandatory 2026 hold. Formation and overview also remain byte-identical. All 17 prior Mali ledger/review records retain their base Git blobs; no previous review evidence was overwritten.

The README's seven domains remain applicable and partial. TP and XB remain missing. The original CSS review and closure continue to apply only to their historical frozen candidates. These four new drafts have not received an independent review, have no accountant attestation and close no coverage issue. Source preparation is not counted as completed current-year coverage.

## Checks actually run

- [shape-checks.txt](shape-checks.txt): all 15 checks pass on each of the four Guides.
- [example-checks.txt](example-checks.txt): eight executable cases, no failures or missing blocks. The initial wage-family expected total was wrong and was corrected to the recomputed subtotal before this final run; no final ITS is inferred.
- [pinned-working-validation.txt](pinned-working-validation.txt): the unchanged repository validator checked all four changed Guides and README with `--changed-only --no-index-check`; zero warning groups. The [wrapper](pinned-validation.py) only replaces the changed-file selector with a diff against the full pinned base and current worktree. The first unmodified precommit CLI checked zero files because it compares committed HEAD; [that no-op output](precommit-cli-no-op.txt) is preserved and is not treated as validation of these drafts. The exact stock CLI will be run after the batch commit.
- [sync-audit.txt](sync-audit.txt): audit mode with strict metadata and pinned base, comparing the working tree; four source Guides, zero errors/warnings/notices.
- Exact ledger-quotation matching against cached source text passed for every row. This is a string check; independent source interpretation remains required.
- Full legacy CTA/platform-field/unchanged-file comparisons pass. Descriptions are 105–121 words. Whitespace check passes.

No generated inventory, packages, index, owner file, application or production state was changed. No full-tree validation is claimed for this sparse checkout; the required changed-file validation is the scope. No authenticated portal, current forms/boxes, complete treaty/social-code chain, final wage relief or operative 2026 computation was verified. Independent country review must inspect every ledger row, old-topic destinations, both cases in each Guide and the explicit holds before any publication decision.
