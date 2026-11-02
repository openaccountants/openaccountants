# Independent cessation-benefit delta review

**PASS. Zero remaining findings in the cessation monetary addition. Source freeze released.**

Reviewed on 27 October 2026, limited to the newly integrated cessation-benefit monetary method in `skills/international/spain/es-social-contributions.md`. No source edits were made. This is not a fresh whole-social-contributions, payroll or Spain-pack review and is not accountant attestation.

## Exact reviewed bytes and comparison

- Reviewed SHA-256: `fade74809d49c4a0a33f401b4d234a91c308f9edcc3f022bdece8fabb72070f6`.
- Reviewed Git blob: `bbe3394dff60c0a3453284abe7656c138d3337fc`.
- Previous social delta SHA-256: `f5a2f629e60e1d103d57a092221f88632982bf205d49e03d04ded38b4270690f`, independently matched to the social entry in `../delta-results.json` and its saved snapshot.
- The exact diff is saved as `delta-from-last-reviewed.patch`; reviewed current bytes are `reviewed-guide.md`.

Reconstructing the prior snapshot by removing the new cessation block, its three new dated source rows and the single ceased IPREM reservation reproduces the previous reviewed file **byte for byte**. Thus the previously reviewed calendar adjustment and every other social-contribution provision are unchanged. Protected frontmatter, author/team attribution, platform keys, full CTA bytes, nine authored H2 headings and both existing oa-check blocks are unchanged. The starting-fee monetary authority, equality-at-SMI extension and period-specific interest-rate reservations remain exactly as before; individual benefit awards remain conditional.

## Independent source work

Read the proposal `../cessation-addition.md`, the six supplied primary receipts and their raw source files. Independently re-fetched all six official documents/pages and saved fresh originals, extracts, SHA-256 hashes, read dates and timestamps in `sources/` and `independent-source-receipts.json`; all returned HTTP200. The three BOE documents and the official IPREM table exactly match the supplied source hashes. The SEPE and Social Security page wrappers have different fresh hashes; their relevant current monetary and operational content was independently re-read and confirms the addition. A source-wrapper hash difference was not treated as a law change.

Primary provisions read: LGSS338–339/342 and the named331 partial-case gateways; LPGE31/2022 DA90(b); RD1541/2011 art13.2(a)–(d); current SEPE2026 monthly figures; current Castilla-La Mancha2026 IPREM table; Social Security's current cessation calculation and compatibility instructions. The new Sources rows carry the actual read date2026-10-27. DA90 is correctly identified as the2022 budget enactment and not presented as a new2026 statute; the current official tables establish continuation.

## Legal and monetary conclusions

- LGSS339.4 uses monthly IPREM at the birth of the right plus one sixth. For2026,600×7/6=700. This calculation avoids an annual-IPREM-convention assumption.
- LGSS339.3's ordinary floors/caps on that reference are correct: no child560/1,225; one child749/1,400; two or more749/1,575. The70% average-base computation is correctly bounded by that floor/cap, subject to eligibility.
- RD1541/2011 art13.2(d)'s lawful lower-minimum-base category exception removes the **floor only**, while retaining the cap. The text correctly requires a legally authorised lower-minimum category and does not make every voluntarily selected low base sufficient.
- LGSS339.2–3's named331.1.a(4)/(5) and temporary-partial-force-majeure cases use50% and neither floor nor cap. There is no imported employee-hours proportional cap.
- The child test correctly uses under26 or qualifying disability≥33%, income **below** SMI excluding the proportional extra payments, and cohabitation with the regulatory maintenance/economic-support exception. The regulation's income presumption and adjustment when the child count changes are correctly anchored.
- LGSS342.1's ongoing-activity exception uses net monthly earnings **no higher than** the lower of SMI and the preceding contribution base: equality can qualify. LGSS342.3's pre-existing employee-work compatibility instead uses the preceding four months' average remuneration plus benefit **strictly below** SMI: equality fails. Current Social Security guidance expressly excludes proportional extra payments for that comparator; current SEPE gives1,221 monthly for2026. A new employee job is not established as compatible by this pre-existing-work exception.
- The preceding twelve-month average, eligibility gate,4–24 duration range and eighteen-month re-recognition interval remain consistent with the cited law. No benefit award is inferred from a bank debit or low part-time wage.

The table's whole-article339 anchors expose both subsection3's percentages and subsection4's indicator/child rules. No missing monetary input or wrong result remains within this addition.

## Verification

`controls-and-hashes.json` records **68 passing independent review controls**, including all six floor/cap values, below/equal/above boundaries, the lawful low-base and partial-case exceptions, the two different SMI equality results, child conditions, source hash/HTTP checks, exact prior-hash and scope reconstruction, and metadata/CTA/example preservation. The writer's separately supplied45controls were inspected and all pass; those45are not represented as45additional distinct legal figures.

The repo checker was run independently on the current file: `checked 1 files, 2 oa-check blocks, 0 failures, 0 missing`.

The first run of this review's own control harness exposed a Decimal evaluation-order residue from600×(1+1/6), not a Guide error. The harness was corrected to the Guide's exact rational order600×7/6, then all68checks passed. No source rule or Guide number needed correction.

**Final verdict: PASS for the exact reviewed hash above; zero remaining cessation-addition findings. Source freeze released.**
