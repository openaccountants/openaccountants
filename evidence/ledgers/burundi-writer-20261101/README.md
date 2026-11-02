# Burundi writer checkpoint: 1 November 2026

This is writer evidence for independent review, not independent acceptance, accountant attestation, publication approval or country-complete coverage.

- Pinned base: `8935b6fc3a7ff0f773334a45a67448f1efe37b19`; branch `codex/burundi-tax-2026`.
- Eight Guides, 114 physical rule-ledger rows, 65 legacy labeled topics plus introductory destinations, sixteen recomputing cases.
- All seven tax domains remain partial in the pack README; Guide presence is not completed coverage.
- Six pre-existing platform field sets and complete CTA suffixes preserved byte-for-byte. The two new Guides carry no platform-written fields or copied CTA. Required tier is 2; no professional review metadata added.
- Raw PDF/HTML/image/OCR captures, baseline copies, provenance and candidate hashes are outside Git in the sibling source directory and pack root. Public ledgers identify actual law/article, URL, short French wording, location and read date.

## Mechanical checks run

Using `PYTHONPATH=/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps`:

| Check | Result |
|---|---|
| `skill_checks.run_checks` on each of eight Guides | 15 checks each, no failures |
| `check-examples.py --require` on eight explicit paths | 16 blocks, zero failures, zero missing |
| `validate-guides.py --no-index-check` in sparse country worktree | 8 Guides, passed; informational zero same-job-groups warning |
| Strict sync, exact pinned base, worktree, strict metadata and eight CAS entries | 8 source Guides, zero errors/warnings/notices |
| Description counts from parsed final YAML | See below; all80–150 words |
| Six baseline platform fields / suffix comparison | Exact preserved |

Changed-only validation before commit saw zero committed changes and was not counted as validation. A preliminary full run incorrectly included generated-index freshness checks, which are intentionally out of scope. The first private CAS-generation attempt treated git's failed new-file lookup echo as a token; corrected to null for new files, then strict sync passed. These were invocation/data-preparation issues, not evidence to bypass failed content checks. No generated inventory or validation script was edited.

## Final description word counts

| Guide | Whitespace words in YAML description |
|---|---|
| bi-company-formation | 107 |
| bi-corporate-income-tax | 103 |
| bi-cross-border-tax | 98 |
| bi-income-tax | 103 |
| bi-payroll-social | 98 |
| bi-tax-overview | 103 |
| bi-transfer-pricing | 101 |
| bi-vat-gst | 101 |

## Source integrity

These are raw source capture SHA-256 values, not a substitute for the read scope recorded by each Guide.

| Source | SHA-256 |
|---|---|
| income2020 | `f682bd7f9aa20eea85fa0892222eed2fa157aef7f9c8dbe958824056977d590c` |
| vat2020 | `789fe003bd42b6e7e9555226258a55b2b74275a31c748cfba12ac90119a62fa4` |
| procedure2020 | `9b66e75e5c2d9005de26ca3dd35d3b10b6bade6c60a73ad26362581af750b241` |
| budget2026 | `a62d4bdb5ecdcc490b56cfbb0a3084db7b4a6c6a01ad04cdeba63ef80a3973be` |
| budget2025mod | `0dc9d9cf986bfcd2a10bae822c28724e570151f5d9f7bc6f4e9d980674ba1d4e` |
| companies2011 | `27373ca33495fea051417101410677e154fa782e30ded00811ec3a7b368e1faf` |
| morocco-ratif2026 | `8c3746be4e0e1db9680e69d1166dab269a453b5d69667f2c7893af388feb2842` |
| adb-fee2024 | `98c99dacb5c9073aeb6286a440c44ec5d8749f1b6daddc238fc5308e92769e13` |
| social2026 | `3f664d8832c0c26d7c85d5a4f23c2ffebb6ad765161dd29042401b867fb8570d` |
| gazette202105 | `7580008499453fa4621c83bd64b002a97ede298d71a880ec06b0ff36e7ed8d16` |
| portal-login | `62582e9e897dff6351f16bbbfb82da6c5b40ceb6c90810343b91aa0df1d250fe` |
| portal-space | `bc288f4a134bc8e9e0d9c8af025ba6917e227fcafc4d60d982c15208d809f1e4` |
| form-corporate | `a02e64daa5c552825bcaca4293fffbcbcabda08b729d5a0bd8e30c538ee8948c` |
| form-individual | `7a35ba979bcd5eb35a24398529b7aea92e2acd74fae1814ab534e6e59434f954` |
| form-micro | `8fd82401c046a52128f794569b656599c978b709fc866ef51ac3bcf5c4cfa720` |
| form-monthly | `91ee1ad81c5f2b2abc7352861db8331ada8b6e5b7b1db20c89da8b7d7fb16e4b` |

## Material writer limitations

The ordinary computations are substantive but incomplete for named jobs: quarterly natural-person due-day calendar, first-half land-rent base interaction, July VAT cutover cases/refund execution, operative TP implementing-order detail and annual financing cutover, diplomatic residence scan condition, treaty effectiveness/relief procedures, health/training scheme applicability and authenticated filing completion. The current interest order and specialised incentives/sectors are excluded explicitly. The old alleged branch remittance tax and unsupported aggregate contribution percentages are not operational rules.

Actual enacted budget commencement is 1 January and 1 July2026. Private raw captures include the actual principal laws and budget PDFs, not only catalogue abstracts or comparison proposals. The April2026 pension amendment concerns pension-benefit reform. The actual Morocco treaty art30 requires instrument exchange and following-year tax effect; domestic ratification is not treated as a2026 reduced rate. The 2013TP direct link, an alternate income PDF and portal order/annual recap links returned404; the Espace Connecté link opens a bank manual. These failures are recorded, not marked as completed current-law verification.

The independent reviewer must read the actual primary text and neighboring conditions for every row, recompute the examples and spot-check the old-topic map. The writer has not performed or claimed that independent review. No push, pull request, merge or external filing was made.
