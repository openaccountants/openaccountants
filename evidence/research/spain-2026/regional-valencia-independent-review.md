# Independent Valenciana f/i integration review

Read date: **27 October 2026**. Scope is only the root-integrated ordinary reconciliation f and household-carer i methods. The reviewer did not write the proposal or these Guide methods. No Guide, commit, push or attestation was made. The wider deductions catalogue and July Catalan additions are outside this review.

**Result: the requested birthday-month, combined-cap, employer-sharing and annual-cap methods pass. One ordinary multi-child ceiling clarification, VAL-F01, must be integrated before unconditional closure of the f paragraph.** No missing law or future implementing act prevents that correction.

Reviewed Guide SHA256: `ddde4c243a40c9281de6b9c7f92788305b52ce02763e807d9ae17c82fe14e47d`. The frozen Valenciana family-method span SHA256 is `9a72df5a0f50b00a32dd679a47cb9cbe16e18c914488bb8e773fba27ac59c4e2`. The exact full file and span are copied into `valencia-independent/reviewed-guide.md` and `reviewed-valencia-span.md`; changes elsewhere in the shared file do not change the scope of this result.

## Source reading and current-law bridge

Independently read the cached raw bodies and extracted text of current [Ley13/1997 art4.Uno.f/i and Cuatro/Cinco](https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202#a4), the f replacement in [Ley5/2025 art22](https://www.boe.es/buscar/doc.php?id=BOE-A-2025-11959), and the i replacements in [DL14/2025 art65](https://www.boe.es/buscar/doc.php?id=DOGV-r-2025-90320) and [Ley3/2026 art82](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-15683). The latter replacements do not rewrite f; the current i text retains the 50% rate, category caps, equal-sharing clause and e/f/h incompatibility. The working Guide separately preserves its December/July accrual distinction, which this review does not replace with 2025 guidance.

Read the complete exact [AEAT reconciliation practical manual](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025-deducciones-autonomicas/comunitat-valenciana/conciliacion-trabajo-vida-familiar.html), [reconciliation return calculation §10.15.6](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-ayuda-presentacion/irpf-2025/10-cumplimentacion-irpf-deducciones-autonomicas/10_15-comunitat-valenciana/10_15_6-conciliacion-trabajo-vida-familiar.html), and [household-carer method/example](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025-deducciones-autonomicas/comunitat-valenciana/contratar-manera-indefinida-personas-afiliadas.html). Also reopened current law and the latter two exact AEAT pages through the web tool. The practical manual explicitly separates pre-June2025 deceased taxpayers from the later ordinary method; its old per-child ceiling must not be imported into ordinary2026.

Seven cached successful raw-response hashes were checked against the separately preserved `rioja-valencia-source-receipts.json`; the scoped receipt copy is `valencia-independent/source-receipts.json`. Reads are dated27October2026. These are actual official bodies, not search snippets.

## f: birthday months and VAL-F01

The integrated third-birthday month through the month before the fifth birthday is consistent with the complete provision: monthly person-status testing uses month-end, while the statute expressly starts the contribution interval on the third birthday and ends it the day before the fifth. The result remains the same for a birthday on month-end. This is the reviewer's construction of the full provision; no source is represented as containing the new March worked examples. Work registration on any day meets that month's registration condition. The contribution interval is date-based, not permission to count the entire birthday month's dues when only part falls within the interval.

The March controls independently give `460×10/12 =383.33` for a third birthday and `460×2/12 =76.67` for a fifth birthday, before the income factor/contribution limit. Month-end birthdays were recomputed for all12 months at each boundary, not just the two prose examples. The manuals phase the nominal460 amount under the ordinary BL factor; no new monthly fraction of the contribution ceiling is invented.

**VAL-F01:** the new f paragraph's “contribution ceiling” needs explicit current-year and global scope. Current law says dues accrued in each tax period; the ordinary section of the AEAT practical manual expressly explains that the post-amendment ceiling is global for the whole deduction, replacing the former per-child ceiling. With two qualifying children throughout the year and500 relevant current-year dues, the total is `min(460×2,500)=500`; applying the same500 ceiling separately to each child would wrongly give920. Prior-year dues cannot replenish the current-year ceiling.

Replace only:

> The contribution ceiling uses that actual date interval, even though deduction eligibility is tested by month.

with:

> The contribution ceiling is global for the whole deduction: count gross dues accrued in the current tax period within the applicable third-to-fifth-birthday intervals, without counting the same dues twice for overlapping children; monthly testing determines each child's entitlement.

Source anchors: [current art4.Uno.f](https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202#a4), cached `sources/valencia-reconciliation.txt` lines196–204, ordinary “B) Para el resto de contribuyentes” section. This is available-law implementation, not an unresolved legal interaction.

## i: combined caps, sharing and annual limits

The new `min(50%×eligible contributions,F×(child cap+ascendant cap))` method passes. The law's separate child660/1100 and ascendant330/550 amounts combine when both categories qualify. The exact AEAT example expressly combines1100+330=1430 even with the same worker caring for both generations. The rate applies once to the supported contribution amount. One child and one ascendant give990; two children and one ascendant give1430; one child and two ascendants give1210; higher child and ascendant categories give1650. A missing care category contributes zero.

The official page expressly attributes the deduction to the payer registered as employer. A second parent's descendant-minimum entitlement alone does not divide a sole employer's cap. Equal cap sharing applies when two entitled taxpayers each employ carers for the same qualifying relatives. Apply each claimant's own BL factor and supported paid contributions; the integrated sentence does not award a deduction to an unpaid/non-employer claimant. The unchanged individual cap also applies on joint filing.

The April-start AEAT example computes50% of2541.42=1270.71 against the full1430 annual cap, so no additional9/12 cap applies. The law limits which monthly contributions enter the calculation; that does not independently prorate the annual category caps. A one-month qualifying-contribution scenario likewise uses the statutory annual cap, with only eligible actual contributions entering the50% amount. The e/f/h incompatibility remains stated in the Guide.

## Controls, protected content and release

`valencia-independent/check.py` records **74/74 passing numerical, source-integrity and structural controls**, zero failures. Controls include24 month-end birthday cases, contribution/global/current-year limits, BL factor endpoints, mixed category sums, the exact agency example, sole/shared employer cases, joint cap and exclusion of an extra cap month fraction. They verify the stated method, not any other regional credit. The global/current-year controls currently support VAL-F01's proposed correction; they do not certify that the original sentence already spelled it out.

Compared with the preserved `rioja-valencia-reviewed-deductions.md` snapshot, frontmatter and CTA bytes and both oa-check blocks are unchanged; nine authored H2 sections and two examples remain. The examples were byte-compared, not independently re-audited for this limited task. The first local harness attempt reused the byte-buffer variable as an income-loop variable and failed before writing a result; the variable was corrected and the complete harness rerun successfully. No Guide correction arose from that harness failure.

Evidence is released for parent integration. This initial report keeps VAL-F01 pending until the exact resulting prose is independently read and a delta-closure note is appended.

## VAL-F01 delta closure,27October2026

**PASS; VAL-F01 closed.** Independently read the parent-applied global/current-tax-year ceiling sentence and the two-full-year-children/500-dues example. The current Valenciana span differs from the reviewed span only by that exact sentence replacement plus the supported control. The example correctly gives `min(920,500)=500`; it does not duplicate the same contribution ceiling per child. The wording explicitly excludes previous-year dues and double-counting overlapping children's dues.

`valencia-independent/delta-check.py` records **14/14 passing delta assertions**, zero failures, alongside the retained74/74 initial controls. Whole-file comparison confirms only the declared Catalan rural DA1.1 paragraph and the reviewed Valenciana f paragraph changed since the prior snapshot. The Catalan paragraph is recognised as the separate reviewer's change, not independently re-certified by this Valenciana delta pass. Frontmatter, CTA and both executable example blocks remain byte-identical, with nine authored H2 sections and two oa-check blocks. No Guide edit was made by this reviewer.

Current entire Guide SHA256: `3c27368f02bf904ae0c7439668ab328a235053319b2a4264634d031b1344657a`.

Current Valenciana family-method span SHA256: `590ce0e7a5ac212e81ef0aa66ff60bba0c05b848972bb33bd70e61882dd358e1`.

The final snapshots are `valencia-independent/delta-reviewed-guide.md` and `delta-reviewed-valencia-span.md`; assertions are recorded in `delta-controls.json`. The assigned Valenciana f/i methods are released with no outstanding actionable finding from this bounded review. This closes only these methods and does not assert complete Spain regional coverage.
