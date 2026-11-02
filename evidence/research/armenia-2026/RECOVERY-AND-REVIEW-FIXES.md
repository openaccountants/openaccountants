# Armenia: recovery and review fixes, 26 October 2026

This is a recovered local candidate, not a completed country or publication approval. The temporary writer/reviewer checkouts and raw source caches disappeared after restart. Work is now in persistent permitted storage, on `codex/armenia-country-recovery-2026`, based on freshly fetched main `d8930170`.

## What was recovered

All eighteen original candidate files, including the eleven country files and seven source records, match their recorded SHA-256 and Git-blob identifiers from `df7247a47d4e9ef0aa961165bad1c09e10f9e4f7`. They were reconstructed from recorded authoring operations and compared with the pre-restart Git inventory. Their exact contents remain in `original-candidate.json`; the seven source records remain in `prior/`. The original commit object and intervening temporary branch history are not claimed present. The full 83-line continuation record was recovered from its complete, untruncated saved read.

Later Guide corrections and all 86 executable controls were reconstructed from recorded patches and file-only authoring scripts. No archived shell, network, Git push, GitHub comment or publishing command was replayed. Skipped replay contexts are recorded in `corrections-recovery-events.json`: historical continuation insertions, an originally failed VAT patch followed by its corrected patch, and a missing source-fetch helper. The chronological continuation was subsequently restored as described above. No recovered Guide patch remains silently skipped.

The original initial-review output and the later independent whole-pack **INCOMPLETE** report at `8be41f35` are retained as historical evidence. The original 28-artifact initial-review directory and 91-source raw cache/receipt set are not claimed fully recovered. A missing receipt is not replaced with an invented timestamp or response. Fresh source receipts belong to the new review.

## Fixes prepared after the independent review

| Review finding | Recovered correction | Primary authority |
|---|---|---|
| Corporate management expense omitted | Actual-management classification, ordinary 2% cap, registration-year greater-of cap, exceptions and add-back | [Tax Code 118](https://www.arlis.am/hy/acts/215611/latest) |
| Ambiguous micro-business exclusions | Medical care/services, dental technology, construction works and design documentation stated separately | [Tax Code 267](https://www.arlis.am/hy/acts/215611/latest) |
| Ordinary personal refunds missing | Social-expense limits and offset/cash sequence; mortgage population/date/cap/entitlement/request and actual 1274-L forms; reinvested-dividend evidence/refund cap | [1067-N](https://www.arlis.am/hy/acts/206432/latest), [956-N](https://www.arlis.am/hy/acts/231590/latest), [1321-N](https://www.arlis.am/hy/acts/200943/latest), [1371-N](https://www.arlis.am/hy/acts/200942/latest) |
| Gross payroll entitlements missing | Working time, minimum-pay gross-up, leave average and pay, ground-specific severance/final settlement, current calendar-day sickness and maternity method | [Labour Code](https://www.arlis.am/hy/acts/51/latest), [Benefits Law](https://www.arlis.am/hy/acts/205733/latest), [1024-N](https://www.arlis.am/hy/acts/196905/latest) |
| Prescribed transfer-pricing documentation missing | Actual local/master contents, written-request clocks and electronic delivery; parent/reporting-entity notice, country-report tables/currency/language; statutory/order large-group scope difference explicit | [941-L](https://www.src.am/storage/menu_contents_227/hr_hhpekn_2022_941l_64647ea664962.pdf), [942-L](https://www.src.am/storage/menu_contents_227/hr_hhpekn_2022_942l_64647ea6633b1.pdf), [939-L](https://www.src.am/storage/menu_contents_227/hr_hhpekn_2022_939l_64647ea66105f.pdf) |
| Ordinary personal cross-border integration missing | Personal source/property/exemption/gross base, agent/no-agent monthly versus annual filing and whole-year residence after departure | [Tax Code 25, 140–158](https://www.arlis.am/hy/acts/215611/latest) |
| Ordinary coverage mixed with conditional failure cases | Timely export method separated from late own-declaration recovery; controlling health statute separated from old leaflet; exceptional erroneous/suspended/age-65 refund procedures bounded explicitly | Historical independent report and cited current law in the VAT/social/payroll Guides |

The VAT version was found to have regressed from main's 2.0 to 0.2 in the pre-restart draft. The recovered version is **2.2**, advancing both main and the original candidate's 2.1. This was detected by the strict metadata checker; the first check failed and the correction passes.

## Remaining substantive publication gap

XB remains partial. Current Tax Code **19(7)** delegates treaty-benefit procedure to Government. The active historic **01/29**, as amended by **01/13**, supplies application/form instructions but has not been tied to an operative current Government continuation/procedure and the authorised applicant/account **approval-to-foreign-beneficiary-refund** settlement. Code 327's available-account refund method does not establish that a foreign beneficiary owns the agent's credit. Needed evidence is the current Government instrument/continuation rule or authoritative modern SRC procedure establishing that bridge. No repeal/nonexistence claim is made from unsuccessful searches. Actual bilateral/MLI entitlement and specialist rate tables remain distinct.

The README identifies six supplied ordinary domains and this one XB gap, subject to fresh review of the recovered candidate. It does not claim country completeness, accepted filing/refund, named professional review, public content push, PR, comment, issue closure or merge.

## Revalidation

Recovered country plus research: **86 oa-check blocks, zero failures, zero missing**. Full repository schema validation: **2,252 Guides and 6,122 generated frontmatters**, passes with three pre-existing warning groups (810 missing Sources, five stale and five jurisdiction notices). Strict metadata: **ten source Guides, zero findings** after the VAT version correction. Original eighteen-file hashes, all 51 original control bytes, seven canonical core shapes, inherited eight protected metadata/CTA sets and final candidate hashes are checked separately in `recovered-candidate-validation.json`. A changed-only run before any recovery commit selected zero files and is not counted as ten-Guide validation.

The old 129 repository/40 MCP passes are historical pre-restart results only. New review and any new test runs must be recorded with their actual scope and commit. The historical INCOMPLETE report is not relabelled PASS.
