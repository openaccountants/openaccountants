# Azerbaijan batch validation

Source review commit: `6321000977e7702ffe59ed084edee63c8b6f38a4`. This receipt records local checks; GitHub check status must be verified at the actual published head separately.

| Check | Result |
|---|---|
| `scripts/check-examples.py skills/international/azerbaijan/*.md` | 16 blocks in eight tax Guides, zero arithmetic failures |
| Changed guide validator, `--changed-only --no-index-check` | Eight Guides checked, zero warning groups |
| Full validator, `--no-index-check` | Passed: 2,247 source Guides and 6,104 generated frontmatter blocks; existing warning groups for 829 missing tax-source sections, five stale-year/date cases and five jurisdiction-agnostic cases |
| `check-sync-integrity.py --base origin/main --head HEAD --mode audit --strict-metadata` | Eight source Guides; zero errors/warnings/notices |
| Mechanical structure audit | Nine sections and exactly two checks for each tax Guide; Sources last before any unchanged platform CTA |
| Platform preservation audit | Existing platform-owned keys and full CTA marker-to-EOF blocks match main byte-for-byte; new TP/XB Guides add no platform keys or human review |
| Description/quality checks | All eight descriptions 80–150 words, tax year 2026, tier 2, no named professional reviewer |
| `git diff --check origin/main...HEAD` | Clean after normalising two new-file EOF endings |
| Owner coverage report | AZ: 10 skills, zero professionally reviewed; IT-CORP covered in ordinary scope; IT-IND, VAT, SC, PR, TP, XB remain missing/partial as explicitly mapped |
| Repository unit tests | 129 passed with canonical `TMPDIR=/private/tmp` |
| MCP unit tests | 40 passed after installing local MCP package in isolated temporary venv |

The first repository-unit run had seven errors caused by macOS temporary-directory aliases (`/var/folders` versus resolved `/private/var/folders`) in existing path-guard tests. Running with the canonical temporary directory resolved all seven without code edits. These were not suppressed tests. The first full-validator attempt lacked PyYAML; installing the pinned `PyYAML==6.0.3` dependency in `/private/tmp/oa-az-venv` resolved it.

The mechanical example checker confirms arithmetic only. The independent reviewer separately recomputed each example and checked the underlying law; see the independent-review receipt. Neither test results nor AI review constitute professional attestation. Raw downloads, scripts and logs stay in local `work/`; only the documented public evidence and source Guides are committed. Unrelated scratch `resp.txt` is not published.
