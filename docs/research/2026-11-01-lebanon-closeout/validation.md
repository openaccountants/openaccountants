# Committed validation receipt

Validated Guide/evidence commit: `3e8de607a03685e2511516d48dcdfa82cf96ec05`.

Full actual merge-base: `46c01152da0fdd1b722f61190c88413d0a195d02`.

All Python validation used the existing validation-deps PyYAML directory on `PYTHONPATH`. No tool or dependency files were changed.

- `python3 scripts/validate-guides.py --changed-only --no-index-check`: six actual changed Guides, passed, zero warning groups. The README is the seventh changed country Markdown file and is not a Guide.
- `python3 scripts/skill_checks.py` over all six changed Guide paths on the committed tree: all fifteen checks passed for each, ninety passes.
- `python3 scripts/check-examples.py --changed-only --require`: twelve executable blocks, zero failures, zero missing. Its file count includes non-Guide review Markdown which has no computation requirement.
- `python3 scripts/check-sync-integrity.py --base 46c01152da0fdd1b722f61190c88413d0a195d02 --head HEAD --strict-metadata`: six source Guides, zero errors, warnings or notices.
- `git diff --check 46c01152da0fdd1b722f61190c88413d0a195d02...HEAD`: passed, no output.
- Compared complete CTA suffixes and all existing protected platform/contributor fields byte for byte with original head `581bde2b4b59ae820f17c46e13b570c2e73edb05`: unchanged in all six Guides. Export licence strings remain v1.0.
- Commit author and committer are both Michael Cutajar with the linked GitHub noreply email; no attribution trailers.

Independent legal/content review remains pending. These checks do not close the named legal currentness or filing holds and do not establish professional attestation.
