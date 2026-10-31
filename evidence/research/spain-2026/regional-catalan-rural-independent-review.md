# Catalan legacy/rural and Cantabria clarification: independent review

Read **27 October 2026**. Evidence-only bounded review of the newly integrated legacy-home expenditure/base paragraphs, rural arts. 57–61 section, Cantabria denominator paragraph and their dated Sources in `es-irpf-deductions.md`. Proposal writer: a different agent. No public Guide edits, commits, push or attestation by this reviewer.

**Pre-correction result: one inclusion-scope finding, C1. The examined rates, bases, limits, timing and arithmetic otherwise pass.** Exact C1 wording is in `catalan-rural-independent/correction.md`. Existing July and Valenciana reviewed spans are unchanged.

## Identity and scope

Reviewed Guide SHA-256: `ddde4c243a40c9281de6b9c7f92788305b52ce02763e807d9ae17c82fe14e47d`, matching `catalan-integration-hashes.json`. Git blob `83c2c8de628ee484a2c3ac533cba55fc466d58e9`.

| Span | Lines at capture | SHA-256 |
|---|---:|---|
| New Catalan legacy method | 153–160 | `780b0193ff175db7ce476a49d3da3b1b0e0cf271108b4e773e9579e8bf1201ba` |
| Rural section | 161–181 | `8aa8dd281fcf5db9f37c2908a3e376bf5bf150a45e2781aca20439b84d7a2939` |
| Cantabria denominator paragraph | 614–615 | `26f71fa588044ac32e97b3cd13870b63efb6b4caee3d31a842ff076c63b33d53` |

The exact snapshot, individual spans and four new Source rows are retained in `catalan-rural-independent/`. The combined Source-row hash is `95206f9ef46031db2143ea759aea725a98c600bbd47e67755f245b914718f501`.

## Sources independently read

Twelve fresh official URLs returned HTTP 200, recorded with UTC fetch timestamps, raw hashes and extracted text in the evidence subfolder. These include current [Catalan code art. 613-1](https://www.boe.es/buscar/act.php?id=BOE-A-2024-6951#a6-13), [LIRPF DT18](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#dtdecimoctava), valid preserved [LIRPF 68.1/70/78/84](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764&p=20121031&tn=1#a68), valid preserved [RIRPF57](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820&p=20111220&tn=1#a57), current [RIRPF59](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a59), [Ley8/2025](https://www.boe.es/buscar/act.php?id=BOE-A-2025-16833), current [ATC explanations](https://atc.gencat.cat/es/tributs/irpf/deduccions-tram-irpf/), the exact [AEAT home-base instructions](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c16-deducciones-generales-cuota/deduccion-inversion-vivienda-habitual-regimen-transitorio/modalidades-deduccion/adquisicion-construc-rehabilitacion-ampliacion-vivienda-habitual/cantidades-satisfechas-derecho-deduccion-base-deducible.html), [Cantabria art.2/DA1](https://www.boe.es/buscar/act.php?id=BOCT-c-2008-90028#a2), exact [AEAT Cantabria rent instructions](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025-deducciones-autonomicas/comunidad-autonoma-cantabria/arrendamiento-vivienda-habitual-jovenes-mayores-discapacidad.html), and current official PRE415 publication/notice pages.

Read the **actual official PRE/415/2026 PDF annex**, not just the shell HTML: 22 pages, DOGC9611, 24 February 2026, CVE-DOGC-B-26050004-2026. Its previously downloaded official raw PDF hash is `6b1c783e15484f55a6099c341fa0acd5932c5a4c1491ac9601410bb3bdfe5edd`; the reuse receipt accurately distinguishes this independent reading from a fresh HTTP retrieval. Independent extraction finds 590 municipality rows, including 16 DA1 ap1 and two DA2 entries.

Also reread [Ley11/2026 actual art.126](https://www.boe.es/ccaa/dogc/2026/9706/f00001-00146.pdf#page=120) and the full [2 October](https://www.boe.es/buscar/doc.php?id=DOGC-f-2026-90237) and [27 October](https://www.boe.es/buscar/doc.php?id=DOGC-f-2026-90249) corrigenda already independently fetched for the separate July review. Art.126 changes DA1.2; neither corrigendum changes this provision or rural arts.57–61. The BOE rural consolidation expressly remains “update in process”, so its unamended DA1.2 is not treated as the current enacted wording.

## C1: included DA1.1 municipalities must be explicit

The new opening scope names only legally classified rural or special-attention municipalities. DA1.1 expressly includes additional municipalities in the regime, and PRE415 labels 16 entries **DA1 ap1**, separate from MR/MRAE. For example, Bordils is code170255, DA1 ap1. The current scope can incorrectly exclude a listed automatically included municipality merely because its annex category differs from MR/MRAE.

Add the exact scoped wording in `correction.md`: include DA1.1 municipalities, do not reject an annex DA1 ap1 entry because of that label, and retain the actual legal designation for the rate. This does not assign the special-attention enhancement to every included municipality. Keep DA1.2 applicants conditional on the inclusion decision and DA2 partial-area limits.

DA2 is correctly limited to qualifying aggregated nuclei: the annex lists Artesa de Segre250349 and Tremp252347 as DA2. Their capitals do not become eligible merely because the municipality appears. The Guide links municipal location evidence and says to record the actual nucleus. Art.126's rural-county capital addition allows an **application** for qualifying 2,000–3,000 population capitals despite the specified density/growth shortfall; it is not automatic inclusion.

## Legacy-home method: pass

DT18 incorporates the preserved end-2012 regime. The valid 2012/2011 snapshots contain the actual historical home/adaptation provisions. Their dates are not the rejected selectors noted in the writer's evidence.

The ordinary annual deduction **base** is9,040 in aggregate, including a joint return. Eligible traced principal, interest net of hedge receipts, finance charges, costs/taxes and the prior-home/reinvestment/wealth conditions are correctly identified; no excess-payment carry is invented. The agency page explicitly confirms the identical joint ceiling. Ordinary Catalan regional7.5% plus preserved State7.5% gives1,356 at the full base; qualifying regional9% gives813.60, and combined relief1,491.60. The enhanced route correctly requires pre-30July2011 acquisition/construction payments and a current qualifying circumstance plus individual income-after-minimum≤30,000, including on a joint return. Rehabilitation/extension alone does not acquire the9% rate.

Adaptation has its separate12,080 annual base, State10% and Catalan15%:1,208+1,812=3,020. Pre-2013 payments, completion before2017, certified necessity and the specified occupants/relationships/status remain conditions. An old house does not make new2026 adaptation spending eligible. The ordinary and adaptation bases are not merged.

The mixed9%/7.5% joint-cap method is correctly expressed only after each contributor's deductible base is established. The text does not invent priority among competing payments above the one9,040 ceiling. That narrow allocation reservation is retained rather than disguised as a completed control.

## Rural ordinary methods: pass subject to C1

The move rates750/1,000 and monoparental1,500/2,000 match art.57. The Guide applies the enacted **1,000** special-attention ordinary move amount and discloses the current ATC page's conflicting **1,500**. Art.126 and the read corrections do not amend57. The first qualifying move, move-year claim, age18–35 alternative, dependent-child/local-school route and≤30,000 individual/≤45,000 joint income gates are represented correctly. No per-return multi-mover multiplier is invented.

Acquisition and qualifying rehabilitation use15% ordinary/20% special-attention, each with a6,000 annual base; the separately tested per-investing-contributor income gate is36,000 even on a joint return. Art.84.2 prevents automatic base multiplication on a joint return. Acquisition's child/local-school gate is not imported into rehabilitation. Rehabilitation requires a pre-1970 house and the structural-reconstruction cost **strictly above25%** of the land-excluded comparator, using the two-year acquisition rule. Same-year qualifying public aid reduces the **computed rehabilitation credit**, as art.59.5 expressly says:6,000×15%−500=400. The text does not silently reduce the expense base instead.

The acquisition/licence-start year plus14 following years is a15-year period for actual qualifying payments and conditions, not a carry or permission to repeat one payment. The separate DT1 four-year new-event window and1January2026 IRPF commencement are distinguished. No unsupported31December2029 cutoff is substituted. The text preserves12-month acquisition/24-month rehabilitation occupation, three-year continuity, statutory exceptions, former-family-home continuation, prior-investment/reinvestment restrictions and wealth-increase testing. RIRPF59.1/2(c) correctly restores lost regional relief to regional tax with interest.

Rent uses15%/20%,600 individual and1,200 qualifying joint caps, with the stated age/child/school and30,000/45,000 gates. The1,200 shared-home ceiling and division among entitled declarants do not become1,200 per occupant. Rural acquisition's DT18-entry incompatibility, rehabilitation/ordinary-rehabilitation incompatibility and rural/ordinary-rent incompatibility are stated. The text does not grant duplicate acquisition/rehabilitation bases for identical expenditure.

## Cantabria paragraph: precise conditional comparator passes

Current art.2.1 uses a strict rent-greater-than10%-of-income condition. Neither that text, DA1 nor the retrieved exact agency page defines the denominator as BI, BL or another specified measure or expressly settles joint aggregation. The added paragraph correctly leaves `R` as the legally established denominator and makes the examples conditional: atR20,000, rent2,000 fails and2,000.01 passes. It does not certify a particular person's R, import a removed old income ceiling, import another credit's BL-minus-minimum test or use gross salary automatically. This is a narrow statement about the read sources, not proof that no interpretive authority exists anywhere.

## Controls and preservation

**76 independent controls passed; zero failed.** They cover rates/base arithmetic; income, age, date and strict-cost thresholds;15-year versus four-year distinction; conditional rent-burden comparisons; selected official-annex categories and counts; raw-response receipt hashes; and structural/preservation checks. These are actual assertions, not a count of numeric tokens or an endorsement of expressly reserved allocations.

The July section, its three table rows and Valenciana methods are byte-for-byte identical to their reviewed snapshots. Both existing oa-check blocks and the entire platform CTA are unchanged; nine authored H2 sections remain. No whole-catalogue or Spain-pack completion claim is made. Final delta status after C1, if applied, follows below.

## Applied C1 delta: PASS

The exact C1 replacement, including DA1.1, actual-designation qualification and primary citations, is present. The previously reviewed Catalan legacy, rural body other than that opening sentence, Cantabria denominator and July spans are unchanged. Eight narrow delta assertions pass; existing examples, CTA and nine authored H2 sections are preserved. **C1 is closed; zero remaining actionable findings in this bounded review.** Previously stated mixed-rate/duplicate-claim and Cantabria denominator reservations remain expressly outside the certified calculations.

Current file SHA-256: `3c27368f02bf904ae0c7439668ab328a235053319b2a4264634d031b1344657a`; Git blob: `ac8e5e265fbd9010080f52af2d3a681a43891b62`. Final rural span SHA-256: `f39ee549b6ad1a3fd180dddb79010f542a05a2846b9ad1c2afc6223686131a77`. Legacy and Cantabria span hashes remain those above; exact final hashes and snapshot are saved in the evidence subfolder. The parent separately applied independently reviewed VAL-F01 to Valenciana f during this delta; this report neither re-reviews that correction nor claims that the older Valenciana span remains byte-identical after it. Freeze released.
