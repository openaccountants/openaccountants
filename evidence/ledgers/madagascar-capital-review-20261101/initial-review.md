# Independent Madagascar capital-income review

Read on 2026-11-01. Reviewer role only, separate from the writer. This is a source-fidelity and preservation review, not accountant attestation, merger approval or a complete-country opinion.

Frozen pushed target: `b60a51a4adb08da4ea3eb4a8a5e1962b1a2b8a78`.
Source content commit: `918a4af3712e455678bf6084874a2f01313bdb12`.
Prior accepted property head: `abe41a37adcb9d3f58a377b8b7219a73674cb234`.
Actual local `origin/main` and merge base: `59c23acba2ad66dd2bb29ffc81ffbb9289769ef8`.
The only target change after the source content commit is the writer's committed-validation receipt. Guide and README hashes are bound in `initial-input-hashes.json`.

Decision: one precise role-wording repair is required before accepting this capital addition. All 46 rows' French quotes match their actual cached PDF pages. Forty-five rows pass their substantive rendering within the stated partial scope; C28 needs the Guide repair below. No rate, amount, example result, deletion overlay or preserved-topic loss failed this review.

## F1: preserve the exact executive role in the exemption

Location: `skills/madagascar/mg-capital-income.md:62`, the Actual direction functions table row; ledger C28.

The Guide calls the second exempt role a "director-general deputy". The statute instead names `à l’administrateur adjoint au président à titre de directeur général`. This identifies an administrator in relation to the chairman, serving as director general. The current English shorthand can instead be read as a deputy to the director general and omits the chairman relationship. Because this wording decides whether administrator remuneration is exempt, the precise office must be preserved.

Source: [CDI 01.04.10, printed p.44, physical PDF p.45](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf), PDF SHA-256 `d542ae2d3c3f5648c9c4a89e0ba2b95a92e6af77a8c07555d83444e71dfc5254`. The whole article and the preceding board-remuneration charge were read. The signed LFR deletes the final deduction-cap paragraph, not this role or the direction-function condition.

Exact repair requirement: replace "director-general deputy" with a rendering that retains the administrator, chairman relationship and director-general capacity, and include the exact French designation. The safest compact version is "the administrator described as `l’administrateur adjoint au président à titre de directeur général`". Keep the chairman role, temporarily delegated administrator role, income-for-direction-functions test, baseline cap and operative-LFR deletion unchanged. Do not turn this into an exemption for every deputy director general. Preserve this initial finding and original writer evidence; record the repair and changed Guide hash in a new closure record. A focused independent closure check of C28 and the Guide diff is sufficient if the repair changes nothing else.

## Source and currentness checks

The reviewer read the applicable founder/engineering instructions, `docs/OWNERS.md`, the full writing standard in `docs/skill-template.md`, the pack README and licensing mapping in `LICENSING.md`. Madagascar remains Ryan's regional ownership; review does not transfer writing or professional responsibility. No platform keys, generated exports, old Guides or prior evidence were edited.

Fresh page-specific `pdftotext -layout` extractions were made directly from the four hash-bound official PDF caches. Every one of the 46 rows was checked against its stated printed/physical page, not just the writer's text cache. Complete relevant clauses, neighbouring scope and exception provisions were read. Ten decisive pages were freshly rendered and visually inspected: CDI physical 44/45/46, CPF 17/18, LFI 44/131 and LFR 24/26/52. The read scopes, raw-cache hashes and render identities are in `source-integrity.json`; full captures remain outside Git. `ledger-row-review.json` records an individual semantic verdict and reason for all 46 rows; `independent-page-quote-check.json` records every exact French anchor.

The actual [LFI 01.04.02(6), 01.04.04 and 01.04.10, printed p.42](https://www.mef.gov.mg/assets/vendor/ckeditor/plugins/kcfinder/upload/files/2026/janv/LOI_n%C2%B0_2025-021_VF_LFI__2026.pdf) confirms the baseline disposal limb for individuals, the 20% ordinary rate, 50% dividend allowance, conditional 10% annual cooperative distribution rate, justified finality and deletion of the external-financing exemption. The compiled CDI still prints that deleted exemption; the Guide correctly follows the original law when operative.

The actual signed [LFR printed pp.20 and 22](https://www.mef.gov.mg/assets/vendor/ckeditor/plugins/kcfinder/upload/files/2026/lfr/LFR2026%20Ampliation%20SIGNEE%20DATEE.pdf) repeals II-B, adds II-D, extends the disposal wording to resident/nonresident natural/legal persons, and deletes 01.04.10's final deduction-limit paragraph. The Guide preserves these separate changes. CDI residence, IR exemptions and II context were read to distinguish charges. The additional original LFI sanctions amendments and July 20.01.52 replacement were also read; the Guide states no final IRCM penalty calculation and imports neither salary nor nonresident-service sanctions.

LFI article 24 and LFR article 22 expressly require radio or posted publication for activation independently of Journal Officiel insertion. Neither the signature nor the July amplification stamp establishes that event's actual date. The draft correctly holds publication dates, transition transactions and historical nonresident-dividend II-B/IRCM interaction. No complete later-law search or operational-date opinion is asserted by this review. Live official LFI refresh succeeded; the LFR refresh timed out, so its signed cached PDF, hash and read scope are the basis. `git fetch origin` also failed DNS resolution; target and base were verified from the frozen local Git objects, without claiming newly refreshed remote state.

The securities-disposal limb is a charge, not a complete method for cost, expenses, loss use, lot selection, noncash valuation or intermediary/return mechanics. Those rules are expressly held. The draft supplies no unsupported gain formula and does not use gross proceeds, the dividend allowance or property-gain mechanics as substitutes. Variable/deemed redemption issue-price calculations also remain held.

The separate nonresident bank/credit-establishment lending-interest IR rate remains in `mg-cross-border.md` at line 45. The new Guide links that owner without duplicating the rate. Its own 10% figure belongs to the separate annual cooperative IRCM rule. Full treaties, foreign collection/credits, special regimes, actual forms/boxes/payment references and complete IRCM sanctions remain held. These limits are substantive, not matters cleared by quote matching or passing scripts.

## Independent examples, preservation and mechanical checks

Both cases recompute independently with Decimal arithmetic and also pass the repository example engine:

| Case | Independent result |
|---|---|
| Dividend MGA 10,005,999 | Allowance leaves MGA 5,002,999.50; rounded base MGA 5,002,000; IRCM MGA 1,000,400; net MGA 9,005,599 |
| Annual cooperative share interest versus nonexempt term placement, each MGA 1,234,567 | Rounded base MGA 1,234,000; cooperative IRCM MGA 123,400; ordinary IRCM MGA 246,800; difference MGA 123,400 |

Case 2 is a facts/category decision rather than an election. Annual distribution, membership and assembly decision must be supported and the exemptions checked. Both cases condition their result on proven post-LFR application, ordinary rules and no treaty/special override. Neither resolves the historical II-B problem or calculates securities disposal gains.

Independent Git-tree enumeration, rather than reliance only on the writer's selected list, found exactly nine prior Madagascar Guide files and 48 relevant prior evidence blobs. Every blob, complete file bytes and supplied hash matches the prior head and frozen target. Twenty-one evidence files absent from this sparse checkout were compared through Git objects. `preservation-review.json` records all 57 files. `complete-old-topic-map.json` maps every line of all nine prior Guides through 96 complete preamble/section ranges back to its unchanged file and line range. The earlier original-topic map was read from Git and retained exactly. Lost content restored: 0; no topic was removed. README changes add routing for IT-IND/IT-CORP/XB and a follow-on section; all seven partial entries and prior review claims remain unchanged and correctly scoped to their earlier accepted drafts.

All 15 shape checks pass. The committed changed-only validator passes with two explicit warnings: property and capital slugs have no recognised tax-domain name, so their country cells were not checked. This is not domain-completeness proof. Strict metadata audit against the actual local merge base passes for both cumulative added Guides with zero findings. Committed and working-tree whitespace checks pass. Commands and exact output are in `machine-checks.json`; `independent-check.py` reproduces the frozen-target checks without editing content.

## Status and required next step

Fix F1, bind the repaired Guide hash, rerun affected mechanical checks and obtain focused independent closure. Keep this review, writer evidence and the earlier property acceptance immutable. This reviewer made no Guide, README or writer-evidence edit, status reconciliation, commit, push or GitHub mutation.

The country remains partial in all seven ordinary domains. Closing this single wording finding would accept only this stated source-fidelity scope. It would not prove operational filing completeness, securities-disposal computation completeness, actual statutory activation dates, accountant attestation or justify closing country issue #470.
