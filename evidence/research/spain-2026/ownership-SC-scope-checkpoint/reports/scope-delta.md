# Independent ownership and SC scope correction review

**PASS for the exact bounded two-file correction below.** This is not a whole-country readiness finding or accountant attestation. The separate frozen `bafc0f62` whole-pack assessment is not closed by this report.

| Exact final file | SHA-256 | Bytes |
|---|---|---:|
| es-capital-gains.md v1.3 | `68cf44dfa49c22d16ae570775b20916ae4429073c72976e41f608a5a9c966b97` | 35,655 |
| README.md | `efac24ff3ccc93cfc6bb38574ca70c6ff29fcbc1c4f120d9eccaa8d577d12e4d` | 12,967 |

Baseline: `bafc0f62bb889781dd24aead563eccdd785c4725`. Final proposal and whole29 composition are in `spain-ownership-SC-scope-table-precision`; exact independent copies and original composition manifest are retained here. Only these two of the 29 files differ from that baseline. All live baseline hashes remained unchanged during this review. No live Guide, branch, PR or generated repository file was edited.

## Operative source reading and substantive result

I read the actual source text independently. The writer's tests, earlier source report, and manifest integrity are not the legal proof. Six unchanged raw bodies and corresponding readers are retained under `sources/`; `own-actual-primary-read-ledger.json` records exact URLs, hashes, bytes and selected native LF intervals. Downloaded/copied scope is distinct from actual read scope. Readers and excerpts are derivative artifacts; raw bodies were not normalized.

| Source and exact actual read scope | Distinguishing conclusion |
|---|---|
| [AEAT current main-home ownership page](https://sede.agenciatributaria.gob.es/Sede/vivienda-otros-inmuebles/que-ocurre-cuando-vendo-inmueble/transmision-vivienda-habitual-mayores-65-anos.html), full retained reader LF1–33; fresh official substantive page text also read | AEAT expressly distinguishes an owner over65 transferring bare ownership while retaining life usufruct from a pre-existing split between bare owner and usufructuary. The former can qualify; the latter parties do not obtain this exemption on transferring their pre-existing split rights even if this was their habitual residence. |
| [LIRPF33.4(b)](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764), retained LF3197–3206 | Statutory exemption concerns disposal of the main home by a person over65 or with the specified severe/great dependency. This selected reading is not a fresh whole capital-gains law audit. |
| [RIRPF41bis](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820), retained LF1318–1335 | Main-home residence/occupation conditions and current/preceding-two-year context remain relevant. Existing dated relocation/spouse amendment language is preserved; this delta did not require a fresh audit of that separate dated enactment chain. |
| [RD2064/1995 arts44.3(f),46.1](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579), retained LF2569–2581 and2710–2733 | Art44.3(f) expressly uses equal-or-higher SMI for extension-year ordinary bases. Art46.1 retains its narrower literal wording about income exceeding SMI. Initial-period non-regularisation remains separate. |
| [LETA38ter](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409), retained LF2413–2453, operative paragraphs1–12 | Extension eligibility requires income strictly below the annual SMI and is tested for each relevant calendar year. Paragraph6 retains the narrower literal exceeding-SMI wording; no challenge outcome is established here. |
| [TGSS published Prórroga Tarifa Plana guidance](https://www.seg-social.es/wps/portal/wss/internet/HerramientasWeb/9d2fd4f1-ab0f-42a6-8d10-2e74b378ee24/44b5f09d-6c25-4dcd-8210-c21700c67096?changeLanguage=es), retained LF492–495, complete relevant paragraph; fresh official LF174–176 also read | Published administration guidance explicitly reclaims the unpaid difference for extension-year net income equal to or above SMI and assesses each affected calendar year independently. This establishes the supplied published route, not an adjudication of the literal statutory/regulatory challenge. |

The AEAT ownership raw body is `fa8a17d2254d7e85396d627daf389fdcc1f9e38ac9cb4041fa1e9f682ffb2348` (12,458 bytes); the retained page footer is24March2026. The new Guide paragraph follows its two ownership configurations and preserves the main-home and other exemption gates. The new bare-transfer explanation is explicitly for the over65 owner; it does not extrapolate that administrative explanation to a dependency-only claimant. It also does not treat the whole-property proceeds or gain as the measured gain on the actual right transferred. Valuation, basis, other reliefs and retained DT9 boundaries are not supplied by this page.

The README SC correction accurately describes what the unchanged `es-social-contributions.md` LF156–160 already supplies: the published equal-or-higher-SMI extension reassessment route. It retains the distinct unresolved legal-challenge wording and new-2026 reduced-fee authority/discrepancy questions. It creates no new equality rule and does not remove SC.partial. The five partial domains remain exactly IT-IND, IT-CORP, VAT, SC and XB; all four non-SC partial descriptions and every other README field remain unchanged.

## Independent controls

All17 own source/gate controls pass (`independent-source-and-scope-controls.json`). Six ownership controls separate full owner, pre-existing bare owner and pre-existing usufructuary; non-main-home and age64 configurations fail the specific over65 route. An already measured positive gain of40,000 on the transferred right is exempt in the qualifying full-owner case and zero is exempt under this specific route for either pre-existing split party. A250,000 qualifying gain is not capped by the separate annuity240,000 proceeds limit. These controls do not calculate bare-right valuation or establish another available exemption.

SC controls compare annual net income9999.99,10000 and10000.01 against a deliberately hypothetical SMI10000, yielding no/yes/yes extension reassessment under the published route. This is not an actual2026 SMI amount. An initial period remains non-regularised; a two-calendar-year extension with first-year income below and second-year income equal to threshold produces independent no/yes outcomes. Six additional actual-text assertions discriminate the two AEAT configurations and the inclusive published wording from the preserved narrower literal challenge wording. No control purports to settle the challenge, compute a final fee or establish an unresolved2026 award amount.

## Presentation finding and exact closure

Initial capital candidate `da70ecb842ba9e80b9e36f9822e25824c868f215c6421aa902cb7665a1abdc9f` had one low-severity finding, OS-FMT01: the new AEAT Sources row at LF223 followed inherited blank-separated rows, so it did not belong to the actual contiguous GFM Sources table. The requested correction was solely to move this new row after the existing RIRPF42/DA9/DT18 annuity row, before the first blank at old LF217. No legal or numerical defect was identified.

The exact final successor68cf44df closes OS-FMT01. I independently proved that removing the one new AEAT row from both initial and final candidates recovers identical bytes and that the final equals insertion of that same row directly after the existing annuity row. The final row now belongs to the valid contiguous Sources table. All legal/calculation prose is unchanged. Inherited detached source rows were not silently moved. The initial candidate, finding, tests and original42-member writer manifest remain preserved; final disposition is separately recorded in `findings-final-disposition.json` and `exact-source-row-move-proof.json`.

## Preservation, metadata and actual validation

Exact inverse reconstruction and line-level before/after evidence account for every original edit. Final capital preserves all70 original URL occurrences in order (72 after the two added AEAT links), all H2 headings, the CTA and both full original oa-check blocks. README preserves all12 original URL occurrences. Capital frontmatter changes only version1.2 to1.3; its H1 follows the same version change. Tier2, existing date and all other metadata remain unchanged. No author/verification attestation is introduced. Other reliefs, conditions, annuity method and DT9 reservations remain intact. README changes only the existing SC partial value. The SC Guide itself is byte-identical to baseline.

Actual tests on the independently copied final29-file composition:

- Canonical validator `check_guides` on all28 schema Guides: **0 errors,0 warnings**. The isolated root and explicit country list are recorded in `check-final-move.py`; no index check or full repository validation is implied.
- `check-examples.py --require` on29 country files: **44 oa-check blocks,0 failures,0 missing**.
- Separate changed capital Guide: **2 oa-check blocks,0 failures,0 missing**.
- `git diff --no-index --check` between retained baseline files and the private final directory: **no whitespace diagnostics**. Its exit1 records file differences, not a whitespace failure; exact stdout/stderr and command are retained.
- All29 source/composed candidate hashes and live baseline hashes independently matched the final composition manifest; only two rows are changed.
- The original source4 and writer42 artifact manifests were rehashed, with46 member identities matching. Own copied raw/readers were separately checked. This integrity evidence does not enlarge the actual legal reading scope.

The source-row move does not require a fresh legal analysis: every word is identical to the already assessed initial candidate. Final actual validation outputs, exact move proof, source excerpts, controls, source identities, preservation ledger and private snapshots are included in the artifact manifest. These bounded checks support applying this exact two-file correction while retaining all five partial domains and the separate whole-pack assessment.
