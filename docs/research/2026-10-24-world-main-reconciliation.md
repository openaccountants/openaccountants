# Shared worldwide branch reconciliation, 24 October 2026

## Trigger and exact scope

Published shared country head: `ee349c5d0814ee137f655d81ea2242fa64fc6798`. Published main merged: `e3f71b3cb36440fed320a8826b9c4128f05c1886`. PR #514 could not start its ordinary pull-request CI because nine earlier source files conflicted with platform export metadata/boilerplate on main. Liechtenstein has no conflict and its one country content push is preserved.

The clone's origin fetch refspec tracked only `codex/world-coverage-consolidated`, so ordinary fetch left `origin/main` stale. An explicit main fetch revealed the conflict. The local refspec now also tracks main. This is a shared published-base reconciliation, with no new country-law research, professional approval or coverage claim.

## Resolution

For each of the nine files, preserved the complete prior published substantive tax/research body and all source citations, including existing limitations and original source-read dates. Copied exact platform-authorship, licence, trust and pending-review metadata from main and preserved its contributor attribution. Kept the newer research description and advanced content versions/matching headings for the neutral footer addition. Used the maximum existing last_updated date from the two published inputs; no source was re-read or given a fresh legal-verification date.

The neutral CTA is the exact current-Guide/professional-review-status wording already reviewed in the Liechtenstein pack. It retains the platform CTA marker and makes no currentness or professional-approval promise. Full source/editorial and named-accountant review requirements remain as stated in each existing pack and dated review report; this mechanical merge does not renew their legal-review scope.

| File | Version before → after | Preserved controls |
|---|---|---:|
| `skills/international/faroe-islands/fo-individual-income-tax.md` | 0.2 → 0.3 | 2 |
| `skills/international/gibraltar/gi-corporate-tax.md` | 0.16 → 0.17 | 8 |
| `skills/international/gibraltar/gi-individual-income-tax.md` | 0.8 → 0.9 | 8 |
| `skills/international/gibraltar/gi-payroll-social-insurance.md` | 0.13 → 0.14 | 8 |
| `skills/international/gibraltar/gi-property-stamp-duty.md` | 0.3 → 0.4 | 3 |
| `skills/international/gibraltar/gi-transaction-tax-transition.md` | 0.7 → 0.8 | 3 |
| `skills/international/guernsey/gg-corporate-tax-substance.md` | 0.8 → 0.9 | 2 |
| `skills/international/guernsey/gg-individual-income-tax.md` | 0.7 → 0.8 | 5 |
| `skills/international/guernsey/gg-payroll-social-insurance.md` | 0.6 → 0.7 | 8 |

The accompanying JSON records both published input blobs, final candidate blobs, exact imported platform fields and SHA256 comparison of the substantive body before/after normalising only the H1 version and appended contributor/CTA suffix. All nine body comparisons match and all 47 original calculation blocks are byte-identical.

## Preservation and checks

- Compared all 105 source Guides in the existing consolidated workstream: no substantive body changed after the documented nine footer/heading normalisations. This comparison does not independently verify those legal rules.
- All nine Liechtenstein country blobs remain identical to final reviewed source `ede184f9`; all thirteen Finland country blobs remain identical to final reviewed source `c83ca9f5`.
- Generated paths are identical to published main; generated changes brought in by the main merge are inherited published work and are absent from the final PR diff against main.
- All 47 executable controls in the nine conflict files pass. Final committed schema/sync/full-workstream arithmetic and exact pushed-head CI are recorded externally on PR #514.

No other country topic was written, no issue was closed, no tier promoted and no authenticated filing/payment/production data operation occurred. The draft PR and unchecked contributor declaration stay in place. This source merge requires passing exact-head checks and the existing maintainer/publication gates before merge into main.
