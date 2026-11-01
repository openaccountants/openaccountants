# South Sudan writer checks

Pinned base `8935b6fc3a7ff0f773334a45a67448f1efe37b19`; branch `codex/south-sudan-tax-2026`. This receipt records actual writer checks, not independent review, human attestation or operative 2026 acceptance.

| Guide | Parsed description words | Shape checks passed | Ledger rows | Executable examples |
|---|---|---|---|---|
| ss-company-formation.md | 117 | 15 | 10 | 2 |
| ss-corporate-income-tax.md | 110 | 15 | 18 | 2 |
| ss-cross-border.md | 113 | 15 | 20 | 2 |
| ss-income-tax.md | 95 | 15 | 17 | 2 |
| ss-payroll-social.md | 106 | 15 | 10 | 2 |
| ss-tax-overview.md | 120 | 15 | 11 | 2 |
| ss-transfer-pricing.md | 117 | 15 | 5 | 2 |
| ss-vat-gst.md | 117 | 15 | 7 | 2 |

Actual YAML descriptions were parsed with PyYAML and counted using whitespace split. All eight meet 80–150 words; shape scripts alone do not enforce that requirement. All 120 individual shape checks and 16 examples passed. The explicit eight-path validator returned 0 errors and 0 warnings. All 98 ledger short quotes match actual extracted source text/OCR under the stated normalisation; this is a locator check, not an independent legal conclusion. All 85 old-topic rows have destination files. The platform-key lines in all six old files and CTA blocks are byte-identical to the pinned base; neither new Guide contains platform keys.

Successful integrity command: `python3 scripts/check-sync-integrity.py --base 8935b6fc3a7ff0f773334a45a67448f1efe37b19 --worktree --strict-metadata`: eight source Guides, zero errors/warnings/notices. This is the local strict-metadata audit. Not run: no platform database CAS/content_revision was obtained. The initial --mode sync invocation correctly failed provenance-required. The final successful local strict-metadata audit tests pinned-base preservation and version monotonicity, not production CAS permission or publication.

The commands/results and Guide SHA 256 values are in ss-writer-checks.json. The changed-only CLI validates committed HEAD, so the writer separately checks the eight working-tree paths before commit and reruns the ordinary CLI after the freeze. The pinned-base commit comparison is the preservation boundary.

Mechanical results do not clear the statutory source gaps. All seven README domains remain partial. No enacted 2025/26+2026/27 chain, fully reconciled post-June 2021 chain, current social-insurance calculation, sales/rental conflict resolution, completed registration/return or independent acceptance is claimed. Full engineering tests and platform-generated index freshness were skipped because this change is scoped Guide/evidence work.
