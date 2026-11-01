# Writer validation record

Date: 2026-11-01. Frozen content source base: `aec6ba04066bb69d1168c8028ba11dd65cb90505`. This record is mechanical validation, not an independent legal review or accountant attestation.

| Check | Result |
|---|---|
| Per-Guide skill checks | 8 Guides, all 15 checks each passed, 120 passing checks |
| Arithmetic | 8 files, 16 `oa-check` blocks, 0 failures, 0 missing |
| Pinned changed-scope Guide validator | 8 Guides plus pack README selected, 0 errors, 0 warning groups |
| Descriptions | 110-120 words each, within 80-150 |
| Legacy source hashes and dates | Six Guide hashes match pinned base; last-updated dates advance to 2026-11-01; version 1.0 added where predecessor had no version |
| Legacy platform metadata and CTA | All existing platform keys and exact key lines preserved; complete six stamped CTAs byte-identical |
| New Guide metadata | No platform attribution/trust/review fields or stamped CTA in either new Guide |
| Loss on rewrite | All 66 original substantive bullets mapped; no Guide shrank by more than 25%; no Guide deleted |
| Scope | skills/libya plus country research evidence only; no generated package, index, ownership or existing research deletion |

Commands used the pinned repository scripts and PyYAML from `/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps`:

```text
python3 scripts/skill_checks.py skills/libya/ly-*.md
python3 scripts/check-examples.py --require skills/libya/ly-*.md
```

The stock validator hardcodes `origin/main...HEAD`. For this candidate, a wrapper outside Git ran that exact script with `--changed-only --no-index-check` and replaced only those subprocess diff references with the immutable pinned base, including staged changes. No validator source was edited. This avoids a moving-main comparison and includes the two staged new Guides. Exact output:

```text
changed-only mode: validating 9 changed guide file(s)
checked 8 guides (0 non-guide .md files skipped)
checked 0 generated package frontmatter block(s)

validation passed (0 warning group(s))
PINNED BASE: aec6ba04066bb69d1168c8028ba11dd65cb90505
PINNED DIFF: git diff --name-only --no-renames --diff-filter=d aec6ba04066bb69d1168c8028ba11dd65cb90505
PINNED DIFF: git diff --name-status -M100% aec6ba04066bb69d1168c8028ba11dd65cb90505
PINNED DIFF: git diff --name-status -M90% aec6ba04066bb69d1168c8028ba11dd65cb90505
PINNED DIFF: git diff --name-status -M90% aec6ba04066bb69d1168c8028ba11dd65cb90505
PINNED DIFF: git diff --name-status aec6ba04066bb69d1168c8028ba11dd65cb90505 -- packages/us-federal
PINNED DIFF: git diff --name-status HEAD -- packages/us-federal

```

Strict metadata check output:

```text
ly-company-formation: legacy platform fields and complete CTA byte-identical; date/version monotonic; no shrinkage; description 120 words
ly-corporate-income-tax: legacy platform fields and complete CTA byte-identical; date/version monotonic; no shrinkage; description 111 words
ly-cross-border-tax: new Guide has no platform attribution/review fields or CTA; description 117 words
ly-income-tax: legacy platform fields and complete CTA byte-identical; date/version monotonic; no shrinkage; description 113 words
ly-payroll-social: legacy platform fields and complete CTA byte-identical; date/version monotonic; no shrinkage; description 110 words
ly-tax-overview: legacy platform fields and complete CTA byte-identical; date/version monotonic; no shrinkage; description 120 words
ly-transfer-pricing: new Guide has no platform attribution/review fields or CTA; description 115 words
ly-vat-gst: legacy platform fields and complete CTA byte-identical; date/version monotonic; no shrinkage; description 111 words
PASS: 8 Guides; 6 legacy metadata/CTA matches; 2 new Guides clean; all descriptions80-150words.

```

No full-tree validator or index rebuild was run, because generated inventories are outside this country batch. Source PDFs were read locally from the recorded official downloads; no bulk link checker or private filing session was treated as legal proof. Source currentness, current contribution rates, VAT status and live filing procedures remain the explicit partial gaps in the pack README. Independent review of this exact content is still required.
