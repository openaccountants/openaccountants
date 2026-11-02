# Independent review: Spain foral PIT, frozen 9784b7b4

**Review date:** 27 October 2026. **Scope:** only `skills/international/spain/es-foral-income-tax.md` as stored at commit `9784b7b45b9ed5bef2d618b2fe9786fe4faa6e9c`. No source edits, commits, pushes, irreversible actions, taxpayer determinations or production writes were made by this reviewer. File freeze was released explicitly after correction text was saved. This report makes no whole-Spain completion claim.

**Final delta verdict: PASS.** All six frozen findings have been corrected and independently delta-reviewed. Zero remaining identified ordinary calculation gaps within this Guide's stated scope. The reviewed final working snapshot is SHA-256 `e092cb25f25cdec030f73236e72ab686f3665a4e9fed7de8bfd2ad3ddbaeacca`, Git blob `ff9b49384cda16f2145cf7e6ee6811fb02af7011`. Source freeze released. This verdict is limited to that exact snapshot and this single Guide.

**Frozen verdict before correction:** changes required. The printed scale/credit amounts examined and both worked examples hold up, but the ordinary business computation has fixable omissions and the declared pension/progression branches have available-law calculation methods. These must not be described as unavailable law. The writer's first legal delta fixes F1–F5, subject to the Sources table formatting noted below; pension/progression integration is a separate subsequent delta.

## Identity and reproducibility

- Guide SHA-256: `70d8e4891128aad3ff77f853a34750784afe19fc267a6478b00cee67e4ee8be7`.
- Git blob: `acdbc838df6190b53759c966a0ac0ebf2b8c2023`.
- Frozen snapshot: `frozen-guide.md` (524 lines, 12,387 whitespace-delimited words).
- Read `CLAUDE.md` and `docs/skill-template.md` before the Guide/law review.
- Preserved tier 2; no accountant attestation, reviewer attribution or platform metadata was added. This is a new file, so no prior version exists within this file for a lost-content comparison. The 22 original Spain paths and their attribution/CTA/platform references are outside this single-file review scope and were not edited.
- `hashes.json` verifies snapshot bytes against `git show` of the exact frozen commit.

## Work actually performed and counts

1. Read all nine H2 sections and the complete frozen file. The nine sections are in the required order; exactly two `oa-check` blocks exist.
2. Independently fetched all **35 unique official URLs cited in the frozen Guide**, all HTTP 200. Source-cache manifests were used only to discover additional corporate-law URLs. Independently fetched seven further official corporate/exact-publication-version sources and two pension/treaty sources: **44 independent official source receipts total**. Network receipt hashes, final URLs, read dates, raw documents and extracted text are saved. Extraction was recovered using PyMuPDF/std-library HTML parsing after the initially unavailable `pdftotext`/BeautifulSoup tooling; those initial extraction diagnostics are not source-access failures.
3. `figure-ledger.json` records **1,008 numeric field-comparison records across 122 rule/source groups** checked for the frozen text. These are not 1,008 distinct figures. The four complete schedule tables contain **34 rows and 102 schedule fields**; checking the shared Basque tables independently in all three territorial laws produces 204 source/field comparisons for those schedules. An entry is one amount, rate, boundary, duration or date for one rule/source pairing. Separate territorial scale/credit comparisons count separately; repeated prose does not. Act/article numbers and URL digits do not count. This is an explicit audit-ledger count, not a claim that there are 1,008 distinct numbers or that every lexical numeral is a tax figure.
4. Repo example checker: `checked 1 files, 2 oa-check blocks, 0 failures, 0 missing`.
5. `controls.json`: **132 passing independent numeric/boundary controls**; the script also performs the exact frozen-byte identity check, making **133 checks** in its console summary. Printed statutory lower-row quotas are used, preserving the law's tiny cumulative rounding differences.
6. No whole-repository validation or whole-Spain legal sign-off was performed by this reviewer. The source writer separately reported running pack preservation/anchor validation; that report is not substituted for this review's own scope.

## Findings on the frozen file

### F1. Navarra grants wrongly fall within the unqualified percentage-allowance method (ordinary calculation)

The paragraph gives the simplified 5% and special 10/35/45% allowances without current art 36(D)'s mandatory exclusion of taxable aid/subsidy income. Mentioning grants in the turnover selector under 36(C) is a different operation. Example: qualifying result 50,000 plus taxable grant 10,000 is 57,500 under simplified assessment, not 57,000; under ordinary special 10% it is 55,000, not 54,000. Add the grant separately after applying the qualifying allowance. **Primary:** DFL 4/2008 art 36(D), source 05. Exact proposed text is in `corrections.md`.

### F2. Basque simplified eligibility points to the wrong article and omits the ordinary selector

The correct selector is each territory's **art 25.1**, not art 26 (business assets). The ordinary aggregate turnover ceiling is 600,000 in the preceding year; the method requires the express regulated election. Start-year turnover is annualised if appropriate. These are available ordinary selection rules. **Primary:** sources 02/03/04, art 25.1. Corrective text is in `corrections.md`.

### F3. Basque ordinary new-activity reduction is missing

All three art 25.5 provisions provide the 10% male/15% female new-activity reduction for the first positive period and following period, with the first positive period within five periods; previous same-activity and majority former-employer-income exclusions apply. Qualifying result 50,000 becomes 45,000 or 42,500. **Primary:** sources 02/03/04, art 25.5. This is not a specialist-source uncertainty.

### F4. Ordinary business-credit quota incorporation is deferred rather than supplied

The file itself declares this partial. The missing arithmetic bridge is available: Basque PIT art 88 uses local corporate percentages/limits on the IRPF gross-quota portion attributable to general-base business income, with thirty-year carry and territorial exceptions. Navarra 62.3/64.2 applies the incorporated corporate limits jointly to the PIT liquid quota; current corporate 67.4 limits the stated 58/64(B)/66 pool to 25%, has a pre-activity exception and fifteen-year carry, and 67.5 supplies ordering. A blanket 25% on all credits would be wrong. Basque ordinary corporate pool is 35%, with separate 70% and 50% groups and local special overrides. **Primary:** PIT sources 02–05 and independently fetched corporate sources 35–38. Full bridge, exact local exceptions and numerical use-limit controls are in `corrections.md`.

### F5. Read-date table omits seven sources; Emanzipa age anchor is wrong

The four giving sources and three Q1 2026 decrees are cited in the body but have no dated Sources rows (indices 06–09 and 28–30). Add read date 2026-10-27 and actual provisions. Emanzipa age extension is **DA 67**, not DA 69, in both the current BOE and LexNavarra texts. DA 69 concerns filing/withholding. All body URLs fetched successfully; this is citation completeness/precision, not a broken-source claim. Source-map and proposed changes are in `corrections.md`.

### F6. Declared pension/progression branches have available primary-law methods

The final partial line names disability schemes, capital-pension transition and exempt-foreign-income progression, but these are not all future forms or genuine unresolved law. `pension-progression-corrections.md` gives directly usable calculations, legal anchors and controls:

- Basque disability contributions: art 72, own 24,250; eligible other contributor 8,000; combined 24,250, own-first then pro rata; eligible five-year carry. The separate disability annuity exemption is three times **SMI**, not Navarra IPREM.
- Navarra DA 13: eligible other contributor 10,000, own/combined 24,250, same priority; qualifying annuity reduction 3×annual IPREM=25,200; qualifying capital reduction 60% (40% residue).
- Basque current capital: eligible non-yield work component integrates at 70% for a qualifying first capital benefit; art 37(e) fixes a yield ratio and routes the positive yield to savings. The pre-2026 contribution portion has the local preserved route under Bizkaia DT 37/Álava DT 31/Gipuzkoa DT 36, disapplying that split for the elected historical portion. Old qualifying integration is 60%; independently fetched Bizkaia instruction 1/2026 section17.4 confirms it.
- Navarra DT 25: preserve eligible pre-2018 contributions only, old 40% capital reduction with its conditions, payment in contingency year plus two; pre-2018 contingencies expired at 31 December 2020. A 2026 payout cannot revive a 2023 contingency window.
- Gipuzkoa DA 38 expressly supplies progression: augmented local basket for average-rate calculation, then apply the expressed local average rate to taxable basket only. Treaty selection decides whether an exemption with progression exists; the law's arithmetic need not remain absent. The independently read Spain–Germany treaty art 22.1(b) supplies a clear example of the progression reservation, while 22.1(a) supplies the distinct credit route. Verified BOE block anchor is `#a22`.

This finding distinguishes conditional eligibility from a source blocker. It does not assert that a particular foreign pension is exempt, nor resolve every specialised occupational-insurance product, treaty or agricultural regime. Current ordinary periodic pension income must not receive a universal capital percentage.

## Housing and indicator conclusions

**Landlord methods:** confirm the Basque gross-bonus versus Navarra net-reduction distinction, property-by-property zero floor, territorial art 63 basket references and programme-only insurance exclusion. Confirm Álava's named DA 34 35% branch, separate from the <=500-person quota minoración. Basque nonhousing depreciation uses paid cost and its local land-allocation rule; Navarra's building rate is 3%, unknown land 25%, and the furniture table is separate. Navarra's all-expense cap, current-expenses-first four-year carry, >six-month doubtful-debt test and positive-net 70/90/50% reductions are correctly described. The expired COVID three-month rule is correctly excluded.

**Navarra IPREM:** the 2025 official manual explicitly sets the annual dependent gate at 8,400 and double family-unit amount 16,800 (pp227–229). Current art62.9 keeps that reference, and independently fetched official 2026 IPREM data show unchanged 7,200 twelve-month/8,400 annual-with-extra-pay figures. This is valid combined provenance and is not a claim that a 2026-income manual exists. Exactly 8,400 passes; 8,400.01 fails. The dependent gate excludes exempt income. Current art64.5's including-exempt definition expressly applies to claimant uplift under62.9(b)(b')2, not the dependent gate in ordinal1. These are different tests.

**Preserved purchase:** the DT15/17/24 branch distinctions, 7,000/15,000 annual caps, 120,000/240,000 lifetime base, strict 2017 24/27/30k and 48/54/60k income ceilings, disability additions, 15/18/30 rates and historical enhancement periods are supported. The BOE/LexNavarra DT17 consolidation discrepancy is real and correctly exposed. The auxiliary `historical-year-end-comparison.json` is a publication-version diagnostic, not an adverse finding: BOE publication dates at year-end may already display changes effective in the following year. Therefore the earlier substantive versions in the Guide are not automatically wrong simply because a year-end `p=` parameter displays different text; the transition's applicable law and effective dates govern.

**Emanzipa/DAVID:** confirm OF187E/2026's 5,000 Emanzipa minimum from18September and renewals approved from entry, all-contract-holder split, income-year matching for SARA (2025 10,919.71;2026 11,201.44), N/T formula, ordinary r boundaries and 340/280/220 caps, VAIS60%/360/two-year route with its separate minimum, rent<=700 and common asset/relationship/advance procedure gates. The guide correctly avoids indiscriminate stacking of every person/category. Preserve documentary/official award handling for overlapping special weighting circumstances; there is no justification for inventing a cumulative factor.

## Penalty and filing conclusions

All four local summaries match the read current procedure laws. In particular: Bizkaia art27 declaration surcharge is distinct from self-assessment interest under26.7; its 100–250% underpayment range and ordinary400 late-return amount are correct. Álava's delayed interest clocks differ from Gipuzkoa's original-deadline interest; Gipuzkoa's reduced collection surcharge is5%, not Álava's10%. Navarra's1/5/10/15% temporal schedule and75–180%/90–200% serious ranges are correctly distinguished. These are statutory ranges before conditional reductions, not automatic liabilities. No unsupported annual interest percentage was invented.

The Basque20,000/1,600 inclusive filing gates and Navarra17,000/1,600 strict gates are supported; sole-trader income cannot use the exclusive-salary exemption. Navarra's timely positive-return50/50 payment route is supported. Q12026 business-instalment waivers are supported by all three decrees and do not make valid voluntary payments undue. Do not recycle2025-income campaign dates as2026-income dates. The actual2026-income campaign orders remain a future annual publication dependency, unlike the available computation laws above.

## First writer delta (after freeze release)

Read the working-file diff after the writer implemented F1–F5. **Legal delta pass**: grant exclusion and examples; art25.1 selector; art25.5 reduction; territorial credit incorporation/pools/carry and examples; DA67 correction and dated source additions match the primary evidence. The writer correctly labels Bizkaia's Q1 decree DFN1/2026. One formatting correction was reported: newly appended Sources rows were separated from the existing table by a blank line without a new header/separator. Remove that gap or provide a second header/separator. A subsequent pension/progression delta is still required before closing F6; this frozen report does not pre-approve unseen edits.

**Finding count:** six findings on frozen9784b7b4. F1–F5 have passed the first legal delta, subject to the simple table-format fix. F6 awaits integration/review. No accountant attestation and no whole-country completion claim.


## Final writer delta and release

Independently read the final working file after the five pension/progression branches were integrated and compared its full diff with the frozen9784b7b4 snapshot. Saved exact reviewed bytes as `final-delta-guide.md` and the complete comparison as `frozen-to-final-delta.patch`.

**F1–F6 closed. Zero remaining identified ordinary calculation gaps within the Guide's stated scope.** The disability-plan priorities/caps/carry; Navarra disability annuity/capital distinction; Basque2026 yield split versus preserved pre2026 capital route; Navarra legacy contribution/timing window; and conditional progression method with expressed average rate now appear with legal anchors and correct arithmetic controls. They are no longer deferred as unavailable law. The Sources table formatting is fixed; all41unique officialURLs have dated entries (45rows including deliberate duplicate housing aliases), including the two new pension/treaty documents. The treaty BOE block `#a22` was independently verified.

`final-delta-controls.json` records29passing checks:16new pension/progression arithmetic controls and13structure/provenance/identity-related checks, including unchanged frontmatter/tier2, no added attestation/CTA, nine H2sections in order, exactly two oa-check blocks, dated source coverage, relative corporate-Guide target/anchor and the example-checker success. Repo checker again reports2oa-check blocks,0failures. This follows132frozen arithmetic/boundary controls and a separate frozen Git-byte identity check; no distinct-figures claim is made from summing audit records.

Final reviewed working SHA-256: `e092cb25f25cdec030f73236e72ab686f3665a4e9fed7de8bfd2ad3ddbaeacca`. Git blob: `ff9b49384cda16f2145cf7e6ee6811fb02af7011`.613lines,14,710words. **Source freeze released.**

The retained future2026-income annual campaign dates, designated project recognition, actual treaty-category eligibility and documentary elections are conditional/future facts, not omissions in the supplied ordinary calculation method. The expressly excluded employee/new-company share-investment eligibility and specialist impatriate/agricultural/forestry regimes remain separate eligibility work; this report does not attest them. It does not claim the whole Spain pack complete or confer accountant attestation.
