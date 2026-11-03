# Kuwait closeout validation and review handoff

Repair scope: six existing Kuwait Guides and the existing country README. Evidence only under this directory; no new Guide, generated export, unrelated country or private-application code is changed.

Actual immutable merge base: `46c01152da0fdd1b722f61190c88413d0a195d02`.
Incoming PR head: `461f81b95c397d88eae34d1729725d2956b35840`.

The six per-Guide ledgers contain 88 law/source rows covering 45 distinct rows, plus the exact 12 executable cases. The old-topic table records 107 substantive lines from the full actual merge base. Sources have official URLs, SHA-256 hashes, precise reading scopes, original-language decisive quotations and read dates. The restored topics are holds where their primary evidence is missing, not unsupported operative rules.

Pre-commit checks passed on 2026-11-01:

- Changed-only validation with `--no-index-check`: six Guides, zero warning groups. No generated inventory is rebuilt.
- All 15 `skill_checks.py` checks on each Guide: 90 passes.
- Required examples: 12 blocks, zero failures or missing blocks.
- Strict sync integrity against the complete merge base: six source Guides, zero errors, warnings or notices.
- Whole-diff whitespace against the complete merge base: clean.
- Descriptions: 85 to 105 words. Numeric H1 versions match frontmatter. All pre-existing immutable metadata and full stamped CTA tails match the incoming head exactly. The additive category correction is inherited from the existing PR.

The writer reruns these against the actual committed head before pushing and passes that exact SHA plus the logs outside Git to the independent reviewer. A successful local check is not an independent legal acceptance or a separate-account GitHub approval. No independent full-ledger review is claimed in this record.

Commands, from repository root, with validation dependency path supplied in `PYTHONPATH`:

```sh
python3 scripts/validate-guides.py --changed-only --no-index-check
python3 scripts/skill_checks.py skills/kuwait/kuwait-tax.md skills/kuwait/kw-company-formation.md skills/kuwait/kw-corporate-income-tax.md skills/kuwait/kw-payroll-social.md skills/kuwait/kw-tax-overview.md skills/kuwait/kw-vat-gst.md
python3 scripts/check-examples.py --require --changed-only
python3 scripts/check-sync-integrity.py --base 46c01152da0fdd1b722f61190c88413d0a195d02 --head HEAD --strict-metadata
git diff --check 46c01152da0fdd1b722f61190c88413d0a195d02 HEAD
```

Fresh-review task: read the full actual diff, all 88 ledger rows and their full clauses/neighbours; check the 107 old-topic rows, independently recompute the 12 cases and test the NON-OPERATIVE HOLD boundaries. Report figures/rules checked, corrections needed, lost topics restored, and unconfirmed items. A reviewer who repairs must not give final acceptance of that repaired version; a fresh reader owns final acceptance. No merge or auto-merge is performed by this writer.
