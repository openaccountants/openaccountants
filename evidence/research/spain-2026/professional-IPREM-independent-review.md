# Independent review of the TP/IPREM copy delta

Verdict: **PASS for this finite full-calendar-year 2026 statutory construction and its presentation.** No unresolved actionable finding remains in the final candidate. This is not a whole-Guide or whole-country completion verdict, an accountant attestation, or a numerical AEAT/DGT ruling.

Reviewed file: `skills/international/spain/spain-transfer-pricing.md`, v1.2, 31,683 bytes. Final SHA-256: `5da4e1f814f1fbb09c3b2c4fa0d22906df09af2b927b08e28e892f9ebb543f0d`.

The reviewer did not author this Guide or delta. The writer supplied the frozen candidate after a different reviewer's source assessment. I independently read the complete before and final Guides, the actual current primary bodies listed below, and the original 2014 LIS provision. I did not edit any Guide, README or Git state. The I03 writer evidence remains untouched.

## Findings and disposition

| Finding | Evidence and disposition |
|---|---|
| The €36,000 full-year minimum is a supported statutory construction, not an express administrative numerical determination | LIS art. 18.6 directly names five times IPREM. DA 90(c) gives annual IPREM of €7,200. The current SEPE page actually places that amount alongside the 2026 SMI context and points to Law 31/2022. For the expressly stated full-calendar-year population, five times annual €7,200 is €36,000. The Guide consistently labels the conclusion as its reasoned statutory construction. PASS. |
| The €8,400 figure is conditional | DA 90(d) applies to the specified annual SMI references replaced through RDL 3/2004. That is not a free-standing instruction to increase every direct annual IPREM reference to fourteen payments. RDL art. 2.3 concerns references in existing state rules. The original LIS of 2014 already directly used IPREM in art. 18.6. The Guide explains that distinction rather than asserting a located ruling resolving it. PASS. |
| Both 75% denominators and their different equality rules are preserved | Professional revenue must be more than 75% of all entity revenue. Cohort service remuneration must be at least 75% of the result before all professional shareholder service remuneration. The example uses €80,000/€100,000 and €72,000/€80,000 respectively. PASS. |
| Individual qualification, prerequisites and general fallback are preserved | Each person's contribution criteria must be written; adequate material and human resources and the qualifying services/relationship remain necessary. Comparable employees invoke the 1.5-times limb. The explicit c(2) saving for other shareholders is correctly confined to an individual minimum failure. The new text calls the rule optional and directs a failure back to evidenced general valuation, not to a compulsory €36,000 salary or automatic adjustment. PASS. |
| Original content and distinct example populations are preserved | Seventeen preservation checks pass. Example 1's entire block is byte identical. All original fields in Example 2 remain unchanged, including every expected output; its professional variant uses separately named inputs and is expressly described as separate from Modelo 232. Both original example narratives, original source rows and order, platform metadata, byline and full CTA remain intact. PASS. |
| Missing spaces in the first candidate | Reported promptly to the writer. The writer corrected only the added prose/source-row presentation and supplied a new hash. I reread those paragraphs and source row and reran preservation and arithmetic checks on the final hash above. RESOLVED. |

## Sources personally read

All five bodies were independently fetched successfully on 27 October 2026. Full HTML and extracted text are retained here; `fresh-source-receipts.json` records exact URLs, UTC read times, HTTP status, byte count and SHA-256. The four BOE bodies match the writer/earlier review's retained bodies byte for byte. SEPE's fresh raw hash differs while the relevant 2026 context, statutory link and amount cells remain the same; the independent fresh body is retained rather than assigning the old hash to it.

| Primary body | Relevant reading and consequence |
|---|---|
| [Current LIS](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a18) | Personally read art. 18.1 through 18.6, including every limb of 18.6 and its final individual-failure sentence. Current consolidated version records the 2 September 2026 update. General market valuation and the optional special rule are distinct. |
| [Original LIS publication](https://www.boe.es/buscar/doc.php?id=BOE-A-2014-12328) | Personally read complete original art. 18.6: direct IPREM wording, both 75% tests, written criteria, employee comparison and individual-failure exception already appear in the original 2014 law. This is stronger support for the direct-reference distinction than relying only on present consolidated wording. |
| [Law 31/2022, DA 90](https://www.boe.es/buscar/act.php?id=BOE-A-2022-22128#da-90) | Personally read complete DA 90, all four limbs. The title and opening refer to 2023; the Guide does not pretend that it is a newly enacted 2026 budget provision. Current continuation is corroborated by SEPE's actual current page. Annual €7,200 and the conditional €8,400 remain separate. |
| [RDL 3/2004, art. 2](https://www.boe.es/buscar/act.php?id=BOE-A-2004-12010#a2) | Personally read the complete art. 2, especially the conditional annual SMI rule and substitution of references in then-existing state provisions under art. 2.3. This does not itself impose fourteen payments on the direct 2014 LIS reference. |
| [Current SEPE amounts](https://www.sepe.es/HomeSepe/prestaciones-desempleo/Cuantias-anuales.html) | Personally read the SMI 2026 explanation, link to Law 31/2022, table headings and monthly/annual cells: IPREM €600 monthly and €7,200 annually. The fourteen-payment notation is attached to the SMI cell. This is a public employment authority amount table, not a responsive tax ruling. |

The earlier assessment's blocked DGT attempt is not treated as a full ruling body, nor as affirmative numerical authority. I did not certify that every possible administrative interpretation has been exhaustively searched. The Guide's explicit statement that this is a construction rather than a located numerical ruling is essential to the verdict.

## Arithmetic and preservation

`check.py` and `controls.json` retain 49 independent calculation, boundary and source-condition controls, all passing. These include €35,999.99, €36,000, €36,000.01, €37,000, €39,000, €41,999.99 and €42,000. The cases from €36,000 through €41,999.99 pass the direct annual €7,200 individual construction and fail an imported €8,400 comparator, making the choice operationally visible rather than arithmetically vacuous.

The controls distinguish revenue equality (fails) from cohort-remuneration equality (passes), verify the result denominator when professional revenue and result differ, show one shareholder's shortfall despite sufficient aggregate remuneration, test the other shareholder's preservation, and show that €40,000 can fail when analogous employees average €30,000. Missing resources, written contribution criteria or qualifying services fail despite passing all numerical tests. Source-condition confirmations and the explicit absence of a part-year conclusion are labelled in the controls; they are not claimed as numerical authority or a tax engine.

Both complete Guides were run through the repository example runner: one file, two blocks, zero failures and zero missing blocks in each run. The three original outputs of Example 1 are €324,000, €24,000 and €74,000; the four original outputs of Example 2 are €150,000, 60%, €30,000 and €70,000. The added professional variant recomputes 80%, €60,000 aggregate minimum, €72,000 paid, €36,000 individual minimum, €12,000 cohort headroom, zero individual headroom and a €0.01 shortfall.

`no-loss.json` proves final reconstruction using exactly six surgical replacement regions and no other changes. All 48 original URL occurrences are retained among 54 final occurrences, with zero missing occurrences. Original source rows remain in their original order. Only version, content date and matching heading advance; the remaining frontmatter values and keys are unchanged. The full example narratives and platform CTA are byte identical. `surgical.diff` retains the exact comparison.

Part-year entitlement/apportionment, a responsive numerical administrative interpretation beyond this construction, and the pre-existing other reservations remain expressly unresolved. No part-year multiplier, fourteen-payment entitlement, Model 232 relief or whole-country completion is inferred.

The Guide runner is the relevant executable check for this copy delta. I did not run a repository-wide build or change generated packages. Final artifacts are frozen in `frozen-manifest.json`; that manifest hashes every other artifact in this review directory and excludes itself to avoid a recursive hash.
