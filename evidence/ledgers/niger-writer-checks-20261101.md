# Niger writer checks, 1 November 2026

The candidate is frozen for independent source review, which remains pending. These are writer checks only.

| Check | Result |
|---|---|
| `skill_checks.py` on the two new Guides | All 15 checks pass for each Guide |
| `check-examples.py --require` on both new Guides | 2 files; 4 blocks; 0 failures; 0 missing |
| `validate-guides.py --changed-only --no-index-check` | Pass; 2 warnings because the two distinct extra-tax slugs have no seven-domain cell mapping |
| `check-sync-integrity.py --base db5bf4ff7d4b078421b4fedd483d9b9b91cd71a6 --strict-metadata` | 2 source Guides; 0 errors, warnings or notices |
| Five original Guide SHA256 comparisons to the recorded baseline | All byte-identical, including platform metadata and CTA |
| Ledger rows | Cash-payment 22; TDTA 18; 40 total, each with article, official URL, short French quote and actual read date |
| `git diff --check` | Pass |

All Python validation uses the existing Finland validation-dependency directory on PYTHONPATH. No generated package, index or LLM file is edited.

The shared `origin/main` advanced 16 commits after this branch was created. A preliminary strict worktree comparison to that moving tip therefore reported 86 unrelated upstream additions as source deletions; comparison to the recorded starting main commit above passes. The changed-only validator uses the merge base and checks only this candidate's Guides. An accidental `--help` invocation of the validator (which has no help parser) ran the full sparse-tree mode and reported expected generated index/LLM staleness plus legacy Guide warnings; the documented scoped mode passes. Neither preliminary output changes the checked source files.

The two new jobs are limited in scope. All seven tax domains remain partial, with TP and comprehensive XB missing. Current form/portal/acknowledgement details, numerical sanctions, supplier-requested cash computation and historic/transition TDTA procedures remain expressly unresolved in the Guides. Raw source captures are outside Git.
