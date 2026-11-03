# Committed author-repair validation

Repaired content/evidence commit: `b49920464e47d00cef963f0897ff6e8964c1bf1c`.

Full actual merge-base: `46c01152da0fdd1b722f61190c88413d0a195d02`.

All checks ran on committed content using the existing validation-deps PyYAML directory on `PYTHONPATH`:

- Changed-only validator with `--no-index-check`: six changed Guides, zero warning groups.
- All fifteen checks on each of the six actual changed Guide paths: 90 passes.
- Changed-only executable-example checker with `--require`: twelve blocks, zero failures and zero missing.
- Strict metadata against the full actual merge-base: six source Guides, zero errors, warnings or notices.
- Whole-base `git diff --check`: passed with no output.
- All six complete stamped CTA suffixes and protected platform/contributor/licence fields match the original PR head exactly.
- Current Guide hashes match each ledger header and the author-repair manifest; all fourteen source identifier hashes match the cached primary/tool-text files.
- Both original independent receipts match the SHA-256 values recorded before repair. All 692 predecessor items and nine precise destination repairs remain present.

The original independent review still records four repairs required at its own frozen head. This author response records their implementation and one restored rule, VAT carryforward. Focused independent closure on the new frozen head is pending. No outstanding hold has been silently converted into a verified filing instruction.
