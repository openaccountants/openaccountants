# Licensing

OpenAccountants is a **mixed-licence repository**. Two different licences apply,
depending on whether a file is *software* or a *tax Guide*.

## Which licence applies to what

| Files | Licence | Text |
|-------|---------|------|
| Software, tooling, docs, and project metadata — `mcp/`, `scripts/`, `tools/`, `plugins/`, `.claude-plugin/`, `docs/`, `.github/`, `Dockerfile`, and root config/meta files | **AGPL-3.0-only** | [`LICENSE`](LICENSE) / [`LICENSES/AGPL-3.0-only.txt`](LICENSES/AGPL-3.0-only.txt) |
| Tax Guides and their machine-readable exports — `skills/`, `packages/`, `workflows/`, `index.json`, `llms.txt`, `llms-full.txt` | **OA Guide License** (source-available) | [`LICENSES/LicenseRef-OA-Guide-License-1.0.txt`](LICENSES/LicenseRef-OA-Guide-License-1.0.txt) |

The machine-readable exports (`index.json`, `llms.txt`, `llms-full.txt`)
reproduce the Guides, so they carry the **Guide License** — otherwise the Guide
content could be taken via the export while ignoring the licence.

This mapping is recorded for tooling in [`REUSE.toml`](REUSE.toml) following the
[REUSE](https://reuse.software) specification.

## What each licence means, in plain terms

**Software (AGPL-3.0-only).** You can use, modify, and self-host the MCP server
and tooling. If you run a modified version as a network service, AGPL requires
you to offer users its source. Commercial use is allowed; a separate commercial
licence is available if AGPL does not fit ([COMMERCIAL-LICENSING.md](COMMERCIAL-LICENSING.md)).

**Guides (OA Guide License).** Free to read, use for your own taxes, use as a
professional reference for client work, quote, teach from, and contribute back.
A company using the Guides internally for its own books and tax affairs, including
through an AI tool or an internal retrieval workflow its own staff use, has the same
permission as an individual: no commercial licence is needed.
A **separate commercial licence is required** to embed the Guides in a
commercial AI product, index them for commercial RAG, train models on them,
bulk-extract or redistribute the collection, or run a competing hosted Guide
service. Contact **info@openaccountants.com**.

## Why the repo is no longer "purely" open source

The Guides are the work that took the most effort and are the easiest to lift
wholesale into a proprietary AI product. Keeping the *code* open (AGPL) while
placing the *Guides* under a source-available licence is the deliberate,
supported way to keep the infrastructure open while controlling commercial reuse
of the content. GitHub may therefore report this repository as AGPL-3.0 with
additional/unknown licences — that is expected for a mixed-licence repo.

## Contributions

All contributions are governed by the [Contributor License Agreement](CLA.md),
which grants Glimpse Ltd the right to distribute contributions under **both** the
AGPL and the Guide/commercial tracks. You keep your copyright.

## Third-party copyleft material

Some Guides under `packages/` incorporate third-party material made available
under a copyleft licence (AGPL-3.0 / GPL-3.0), with attribution (see the
`references.md` and provenance sections, e.g. Turkey, France, Poland, Brazil, and
several Canadian provinces). Copyleft material cannot be relicensed: any Guide
that contains or derives from it **remains under its original AGPL/GPL terms**,
notwithstanding the general mapping above. The Guide License applies to the rest
of the Guides, which are Glimpse Ltd's own work, work-for-hire, or covered by an
accepted [CLA](CLA.md).

## Effective date and prior releases

This structure is introduced on **2026-07-16**. Guide versions previously
distributed under AGPL-3.0 remain available under AGPL-3.0 for the copies already
distributed; this change is forward-looking and does not purport to revoke rights
already granted (see § 9 of the Guide License).
