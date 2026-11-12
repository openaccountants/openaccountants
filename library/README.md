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
| `source_url` | The official page: a government, legislature, official gazette, tax authority or other public body of the country, or a statutory body's own legal text. Never a firm, a vendor, a university mirror, study material or Wikipedia. The build refuses any other host (see The rule). |
| `quote` | Verbatim text from that page, in the page's own language and number style, containing the figure. |
| `read_on` | The date the page was read and the quote checked. An entry read again after the rest of its country carries its own later date. |
| `domain` | Only on a figure outside tax: its domain id from [docs/domains.yml](../docs/domains.yml). |
| `status` | Only on an announced figure: a change that has been announced or put in a bill but is not yet law. The one value today is `announced, Finance Bill not yet enacted`. |
| `used_by` | Skills in the folder with a rates-table row containing the exact value. Best effort: a common value such as `20%` also lists skills that use 20% for another rule. |

## Announced figures

When a budget or a bill changes a figure before it is law, the library keeps the figure in force and adds the announced one next to it. The announced entry has the same id plus `.announced` (`ie.cat.group-a.announced` next to `ie.cat.group-a`), a `status`, and its start date in `tax_year` (`2026, gifts and inheritances taken on or after 7 October 2026`). Its quote comes from the bill or its official explanatory memorandum. Once the bill is law, the new value replaces the old one in the entry in force and the announced entry is removed.

## sources.json

Every distinct http(s) URL cited by the skills in the folder, plus every library `source_url`, with the skills (`skills`) and figures (`figures`) citing each. It is the list of pages to watch for changes.

## The rule

A figure is in the library only if it is proven by an exact quote from the official page: the quote must be found, as written, on the page at `source_url`, and it must contain the figure. Never a computed number, a summary, a search snippet or memory. When the page changes, the figure is read again and its `read_on` moves.

Official sources only. `scripts/build-library.py` checks every `source_url` host against an allow-list in [docs/domains.yml](../docs/domains.yml): government domains (`.gov`, `.gov.ie`, `.gob.mx`, `.gouv.fr`, `.govt.nz`, `.gv.at` and the like) and the named official hosts of the figure's domain, each with whose it is. A figure is a tax figure unless its pack entry carries `domain` (an active domain id, such as `financial-reporting`); the tax hosts are `revenue.ie`, `oireachtas.ie`, `boe.es`, `legislation.mt` and the others under `tax`. A standard setter such as ifrs.org counts only for a figure in its own domain, never for a tax figure. A figure on any other host is refused and printed, and does not reach the library. A new official host is added to its domain in that file with whose it is, never by loosening the check.

The saved copies of the pages (with retrieval date and fingerprint) are kept privately, for copyright and size; only the URL, the quote and the read date are published here.

## How it is built and checked

`scripts/build-library.py <path to the research packs> --write` writes both files for each country that has a pack (dry run without `--write`). It reads each country's merged pack only and skips family and superseded pack files. Do not edit the JSON by hand: fix the pack and rebuild.

`scripts/skill_checks.py`, check (q) `figure_in_library`, warns when a rates row states a different number for a figure the library holds. A row that states either the figure in force or its announced value passes. It is a warning, not an error, and only compares a row with a figure when the match is plain; the rule is in the check's docstring.

## Review ledgers

`library/ledgers/` holds per-Guide research evidence in Markdown: claims and conditions, official URLs, exact original-language quotes, read dates, coverage limits and old-topic destinations. These companion files support review of the corresponding Guide. Their derived examples and explicitly unconfirmed branches are distinguished from supported source rules.

The ledgers do not change the generated `figures.json` or `sources.json` formats or the build process described above. Source snapshots remain in the research packet; a ledger does not confer accountant approval.

## Licence

The library is licensed like the skills: everything under `library/` is covered by the same Guide licence and annotation as `skills/` (see [LICENSING.md](../LICENSING.md) and [REUSE.toml](../REUSE.toml)).
