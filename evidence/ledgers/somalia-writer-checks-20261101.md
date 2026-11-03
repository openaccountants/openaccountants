# Somalia writer check receipt, 1 November 2026

Source candidate `129607cf760859de323f04aa204c572caea9e5b4` is frozen for independent source review of its statutory-baseline scope. No review acceptance or operative 2026 coverage is claimed. The separate regulation/transition gate remains unresolved.

| Check | Exact result |
|---|---|
| `validate-guides.py --changed-only --no-index-check` | 2 Guides checked; validation passed; 0 warning groups |
| `skill_checks.py` on both new Guides | All 15 checks pass for each Guide |
| `check-examples.py --require` on both new Guides | 2 files, 4 blocks, 0 failures, 0 missing |
| `check-sync-integrity.py --base db5bf4ff7d4b078421b4fedd483d9b9b91cd71a6 --strict-metadata` | 2 source Guides; 0 errors, 0 warnings, 0 notices |
| `git diff --check` and staged diff check | Pass |
| Candidate manifest SHA256 comparison | All 7 listed content files match |
| Legacy files compared to recorded base | All 6 byte-identical, including platform metadata and CTA |
| Figure/rule ledgers | 23 rows each, 46 total; act/article, official URL, short Somali quote, actual read date |

Python checks use the existing Finland validation-dependency directory on PYTHONPATH. The metadata comparison deliberately uses the recorded branch base because `origin/main` is a shared moving ref. No generator was run; no packages, index or LLM file was edited. Full source captures remain outside Git.

All seven domains remain partial. The new TP/residence jobs are useful source-baseline working papers, not completed current-year coverage. Independent review is pending. No accountant attestation, push, PR, comment or merge is represented by this receipt.
