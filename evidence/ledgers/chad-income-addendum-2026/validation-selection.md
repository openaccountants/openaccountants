# Validation selection and limits

Immutable country base: `59c23acba2ad66dd2bb29ffc81ffbb9289769ef8`.

The committed validation adapter uses the actual Git diff against that base, asserts seven changed source Guides, and asserts the working files equal their committed blobs. It runs all fifteen skill checks, every executable example in those Guides, the existing changed-only validator with `--no-index-check`, strict synchronization metadata audit and whole-base whitespace. Current report records sixteen new cases. The accepted unchanged import Guide has two additional cases.

Two exploratory invocations are not acceptance evidence:

- `validate-guides.py --help` is not a supported help interface; it ran full-tree validation and reported stale generated `index.json`/`llms-full.txt`. Those generated files were not edited, as required. The actual changed-only/no-index validation passes without warnings.
- `check-examples.py --changed-only` with a SHA in `BASE_REF` prepends `origin/` and falls back to `HEAD~1`. That selected only twelve cases. The pinned adapter instead passes the exact seven changed Guide paths explicitly and recomputes all sixteen final new cases. The earlier fallback is not presented as full coverage.

Review evidence is scoped. Passing schema/examples/CI does not resolve the README’s legal, source or procedure gaps. No accountant attestation is inferred.
