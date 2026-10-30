# Simultaneous child support and exempt progression: independent review

Read 27 October 2026. Bounded scope: the newly added combined subsection, its source-date row and remaining-work line in `es-income-tax.md`; no whole-Guide review and no source edits.

**PASS after the parent's scope correction.** The combined calculation and exact 2026 State/city control pass. The displayed formula is now expressly confined to the full-minimum branch established by the official worksheet. Lower-base minimum allocation remains separately identified, without being described as a future-form blocker.

## Identity and evidence

Pre-correction full-file SHA-256: `66f1ee12931f4c3abd4899434752f29a9b885de9bd688ab192d127c00c1de306`, matching `annuity-progression-integration.json`. Pre-correction subsection SHA-256: `3e8d30f39e808d182f8b7892dd39c62967aeb9bcdabd3464a7ad937fe79efccf`.

Final corrected file SHA-256: `1d9320f9ed602e68fc30865b2b4cf1b1091564e6f765c40fd5fe5175907caab1`. Corrected subsection SHA-256: `17ec8ff61a7359828d77cd683b9dc523cd11da309322ca906bbeb91390d0041e`.

Exact snapshots, span files, correction and delta are in `annuity-progression-independent/`. Independently re-fetched [the matching AEAT combined worksheet](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/especialidades-determinacion-cuota-integra-estatal-autonomica/supuestos-especiales-concurrencia-rentas.html) and [current LIRPF](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764), both HTTP 200. Read current arts. 56, 63–65, 74–75 and DA20. Raw responses, extracted text, hashes and UTC read receipts are in the evidence subfolder. The new Guide Sources row is dated 2026-10-27 and links the exact combined worksheet. The worksheet's income year remains 2025, used only for the unchanged statutory method; the Guide control uses its stated 2026 State/city schedules.

## Calculation verified

Arts. 64/75 require qualifying support below the **actual** general liquidable base: `C < Bg`. Exempt income added for rate-setting cannot rescue a case in which C equals or exceeds actual Bg. The other qualifying-support conditions remain in the preceding paragraph and are incorporated by the new section.

The matching official worksheet explicitly splits support C from the remainder `(Bg + Eg) − C`. Apply each half's own general schedule to both components, subtract that half's statutory augmented-minimum tax without making the result negative, divide by the entire augmented general base `Tg=Bg+Eg`, and apply the separate resulting rates to **Bg alone**. There is no choice between two independent taxes and no direct charge on Eg. State and regional minima and schedules remain independent.

The 2026 exact-rate control recomputes in each half: Tg 26,000; C 1,800; other split component 24,200; schedule amounts 171 and 2,712.75; augmented minimum 7,530 and tax 715.35. Hence augmented quota 2,168.40, exact percentage 8.34%, and actual general quota `23,000 × 8.34% = 1,918.20`, or 3,836.40 combined before credits. This example does not certify a rate-display convention because its rate is exact.

The official 2025 worksheet itself contains a parenthetical arithmetic typo, printing `5,550 + 1,980 = 7,730` in one repeated sentence, while its actual scale calculation correctly uses 7,530. Its 2,240.90/26,850 percentage is not exactly its printed 8.34%. The Guide avoids copying the typo and preserves its explicit display/truncation reservation. I do not infer ROUND_HALF_UP from the statute's two-decimal expression or from this worksheet.

## One scope finding and correction

The pre-correction generic formulas used `min(Tg,M+1980)` for every minimum fact pattern. The cited worksheet explicitly states that **actual Bg exceeds the augmented minimum** before it uses the full augmented minimum. It does not decide how a lower actual Bg interacts with art. 56's general/savings allocation and DA20's rate-setting enlargement.

The parent applied the exact correction in `correction.md`: the displayed full-minimum formulas apply where actual `Bg >= Ms+1980` and `Bg >= Ma+1980`, then subtract `S(Ms+1980)` and `A(Ma+1980)`. Below either relevant absorption threshold, establish that half's allocation under arts. 56/64/75 and DA20 before completing the affected rate or savings tax. The text expressly says this is a **formula-scope condition**, not an additional eligibility condition for annuity relief. The actual eligibility condition remains C<Bg. The 1,980 increment is not carried into savings as a new personal minimum.

That change removes the unsupported generic allocation claim while retaining the demonstrated ordinary branch. The lower-base branch is a remaining legal-computation research task; its resolution does not depend on waiting for 2026 forms. A further bounded primary-source attempt is recorded separately when complete.

## Controls and preservation

`check-controls.py` records **29 passed controls, zero failures**: exact schedule arithmetic, independent half results, actual-base equality/near-boundary gates, augmented-minimum scope boundaries, reconstruction of the source worksheet's arithmetic, and structural/hash checks. Seven additional narrow delta assertions pass for the applied scope correction. Both existing oa-check examples and the full original platform CTA are byte-for-byte unchanged across the reviewed delta; nine authored H2 sections remain.

**Zero actionable findings remain in the corrected demonstrated branch.** The separate lower-base allocation and rate-display questions remain explicit. Freeze released. This verdict does not certify the rest of the national Guide or the Spain pack.

## Lower-base follow-up completed

The single further primary-source attempt is saved in `annuity-progression-independent/lower-base-attempt/analysis.md`, with two additional HTTP-200 official receipts. It identifies the explicit enlarged-base minimum wording in AEAT phase 2, the actual-base allocation fields in the approved Modelo 100, and three diagnostic allocations. Their reconciliation in the simultaneous low-Bg branch is not expressly given by the read sources. This is a precise remaining computation/interpretation question, not a future-form or access blocker. No filing result is certified from the diagnostic alternatives.
