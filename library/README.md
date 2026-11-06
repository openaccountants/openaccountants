# The library: tax figures, each proven once

The library holds the figures the skills rely on (rates, thresholds, caps, amounts), one entry per figure, each with the official page it was read on and the exact words on that page. Skills hold the method; the library holds the numbers. A skill's rates table should state a library figure character for character.

One folder per country, named as under `skills/`: `library/ireland/` for `skills/ireland/`, `library/us/federal/` for `skills/us/federal/`.

## figures.json

| Field | What it holds |
|---|---|
| `id` | Stable dotted id, country code first (`ie.cgt.exemption.personal`). A skill row may name it. |
| `item` | Plain English: what the figure is, who it applies to, and the conditions that matter. |
| `value` | The figure as a skill must write it (`EUR 1,270`, `33%`). |
| `tax_year` | The year the figure applies to. A number means that calendar year; a string says the exact period (`2026 to 2027, from 6 April 2026`, `in force 17 Oct 2026`). Read it before using an entry: some are history or a future change. |
| `source_url` | The official page: a government, tax authority, official gazette or other public body of the country. Never a firm, a vendor or Wikipedia. |
| `quote` | Verbatim text from that page, in the page's own language and number style, containing the figure. |
| `read_on` | The date the page was read and the quote checked. |
| `used_by` | Skills in the folder with a rates-table row containing the exact value. Best effort: a common value such as `20%` also lists skills that use 20% for another rule. |

## sources.json

Every distinct http(s) URL cited by the skills in the folder, plus every library `source_url`, with the skills (`skills`) and figures (`figures`) citing each. It is the list of pages to watch for changes.

## The rule

A figure is in the library only if it is proven by an exact quote from the official page: the quote must be found, as written, on the page at `source_url`, and it must contain the figure. Never a computed number, a summary, a search snippet or memory. When the page changes, the figure is read again and its `read_on` moves.

The saved copies of the pages (with retrieval date and fingerprint) are kept privately, for copyright and size; only the URL, the quote and the read date are published here.

## How it is built and checked

`scripts/build-library.py <path to the research packs> --write` writes both files for every country with a pack (dry run without `--write`). It reads each country's merged pack only and skips family and superseded pack files. Do not edit the JSON by hand: fix the pack and rebuild.

`scripts/skill_checks.py`, check (q) `figure_in_library`, warns when a rates row states a different number for a figure the library holds. It is a warning, not an error, and only compares a row with a figure when the match is plain; the rule is in the check's docstring.
