# Country PR split, 24 October 2026

Michael instructed that consolidated PR #514 be split into one PR per country and that BG HR EE LV LT SK SI be recorded under Claude. This is a publication/ownership change; no tax-source body, source-read date, calculation block, original review report or professional-review state is renewed by the split.

## Exact preservation source

- Historical consolidated country head: `571c00a30fc31434c6de04fc35579e8ab76f371c`.
- Reconciled snapshot used for extraction: `9ccb3e45b121313c8044b9c5cbc2124c194495f0`. It merges published main `e05d09fc988e0d715ef000380a811d5a93146746` and preserves its Bulgaria personal-tax update.
- Every replacement branch starts from that exact published main. Only its own country directory and country-specific research records are copied from the reconciled snapshot.
- Nineteen country batches contain 121 changed source Guides and 15 README gap registers. Montenegro has ten total pack Guides, of which eight change in this split. None of Claude's seven transferred countries is included.
- All 443 changed source paths are allocated exactly once: country files/research in their country PR and seven shared ownership/provenance paths in this coordination PR. The accompanying JSON lists exact paths, input commits and subsequent PR/check evidence.
- Generated packages, indexes, llms files, agent-skills and plugin exports are inherited from main and untouched.

## Replacement PRs

All nineteen replacement PRs are open and their exact country/research blobs have been verified against the preserved snapshot. Each published country head has all five checks green (CLA, validate, guard-derived-trees, unit-tests, compare). Exact heads, run URLs, check timestamps and source blobs are recorded in the accompanying JSON. All country PRs remain drafts and retain their source-review and coverage limitations. The historical #514 branch is preserved; no force-push or branch deletion occurs.

| Country | Changed Guides | Country README | Replacement PR |
|---|---:|---:|---|
| Andorra | 4 | 1 | [#774](https://github.com/openaccountants/openaccountants/pull/774) at `5254033f`; five checks green |
| Dominica | 4 | 0 | [#775](https://github.com/openaccountants/openaccountants/pull/775) at `8553e5e6`; five checks green |
| Faroe Islands | 4 | 1 | [#776](https://github.com/openaccountants/openaccountants/pull/776) at `1db6956f`; five checks green |
| Finland | 12 | 1 | [#777](https://github.com/openaccountants/openaccountants/pull/777) at `42dcd2eb`; five checks green |
| Gibraltar | 18 | 1 | [#778](https://github.com/openaccountants/openaccountants/pull/778) at `43206e99`; five checks green |
| Grenada | 3 | 0 | [#779](https://github.com/openaccountants/openaccountants/pull/779) at `333a6780`; five checks green |
| Guernsey | 9 | 1 | [#780](https://github.com/openaccountants/openaccountants/pull/780) at `a23757a2`; five checks green |
| Haiti | 3 | 0 | [#781](https://github.com/openaccountants/openaccountants/pull/781) at `4e8aca09`; five checks green |
| Iceland | 7 | 1 | [#782](https://github.com/openaccountants/openaccountants/pull/782) at `53b9e92f`; five checks green |
| Isle of Man | 3 | 1 | [#783](https://github.com/openaccountants/openaccountants/pull/783) at `1cf2613e`; five checks green |
| Kosovo | 3 | 1 | [#784](https://github.com/openaccountants/openaccountants/pull/784) at `42c407cf`; five checks green |
| Liechtenstein | 8 | 1 | [#785](https://github.com/openaccountants/openaccountants/pull/785) at `a51c7ed4`; five checks green |
| Montenegro | 8 | 1 | [#786](https://github.com/openaccountants/openaccountants/pull/786) at `84cbbf0c`; five checks green |
| Norway | 3 | 1 | [#787](https://github.com/openaccountants/openaccountants/pull/787) at `82a7a1c3`; five checks green |
| Palestine | 5 | 1 | [#788](https://github.com/openaccountants/openaccountants/pull/788) at `aed4a558`; five checks green |
| Saint Lucia | 7 | 0 | [#789](https://github.com/openaccountants/openaccountants/pull/789) at `85ade26d`; five checks green |
| San Marino | 8 | 1 | [#790](https://github.com/openaccountants/openaccountants/pull/790) at `0ae05f36`; five checks green |
| Syria | 5 | 1 | [#791](https://github.com/openaccountants/openaccountants/pull/791) at `6577d477`; five checks green |
| Yemen | 7 | 1 | [#792](https://github.com/openaccountants/openaccountants/pull/792) at `c5ca44f9`; five checks green |

## Checks and limits

All nineteen countries passed schema validation, recomputed examples, whitespace checks and strict source-metadata comparison against the same main baseline before their single split publication. Together they recompute 362 arithmetic controls with zero failures. All 436 country/research paths were checked against the GitHub PR file SHA values: exact match. The seven shared paths plus those country paths account for all 443 original paths exactly once. No generated path or transferred-country Guide is changed. The inherited Gibraltar global-minimum-tax tax_year2024 warning remains; no source year or legal currency was silently advanced. All nineteen published-head CI sets passed at the JSON check timestamps. These checks do not repeat a legal review or establish filing/platform ingestion. Original country reports and gap registers retain their exact review scope. No country issue is closed by this reorganisation.

## Malta publication attempt

The explicitly requested `publish-malta-residence.sh --apply` was attempted after read-only preview. Both stopped at the first packet's fresh-source validation: Residency Malta's L.N.146/2025 and MPRP FAQ PDFs returned HTTP502. No apply phase, authorship-link step or database write ran. The packet check receipt is dated 24 October 2026. Preserve the existing reviewed packet and retry its ordinary gate when the official documents are reachable; do not bypass source checks.

## Fresh-session continuation

The primary chat retains Armenia. Support took Monaco under issue #410, then paused before any Guide edit to perform this split. Its private source card and official retrievals are preserved locally; resume the country in a fresh session from current main with the ownership record in coordination PR #773, rather than treating the historical multi-country branch as a new country PR. The completed split does not authorise new country prose, another independent reviewer, a main merge or a production deployment by itself.

The coordination PR's own final-head CI is checked after this evidence commit. Consolidated #514 is closed as superseded only after every country replacement has been created and checked; its branch and immutable historical sources remain available. No force push or branch deletion is used.
