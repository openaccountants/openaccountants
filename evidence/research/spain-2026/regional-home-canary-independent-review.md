# Independent finite review: Canarias ordinary home base and State coexistence

Reviewed 27 October 2026. Reviewer did not author the change. This is a targeted tier-2 source and arithmetic review, not accountant attestation, a whole-Guide review, or whole-pack completion.

Reviewed Guide snapshot SHA256: `0d6106598f3c71c391f17b35114b5232019af316461ce69bdc61ea026ac8d008`.
Prior independently reviewed baseline: `b6a9a23397e53a5e242912c95de4d873f9c15b88ed3b37f6f5737a6fc77d533d`.

## Finding requiring a finite correction

1. **State quota input missing from numeric coexistence control (Guide line 683).** The paragraph supplies only regional gross quota 1,000/700, then asserts State relief 678 and total relief 1,506. Preserved LIRPF art.67.2, incorporated by current DT18.2, prevents negative State liquid quota. Explicitly assume at least 678 of available State quota for the hypothetical State credit. Otherwise 678 is only nominal and the stated aggregate relief is not determined. This does not affect the regional 150/22 arithmetic. A short assumption, such as “with at least 678 available State tax”, closes the finding. Source: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764&p=20111231&tn=1#a67 and current https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#dtdecimoctava .

## Figures and rules checked

- Actual current Canary arts.14,14quater,18 independently reread from raw HTML whose hashes were checked against receipts before extraction. Article14 expressly preserves State-law regional home relief and incorporates art68.1 at 1 January 2012. Current law provides 6,000 regional base, individual income bands 26,035/46,455 and 5%/3.5%, enhanced under40 to 5.5%/4%.
- Incorporated art68.1.2 and exact AEAT threshold interpretation support cumulative prior deducted home investment plus exempt reinvestment gain, rather than the tax saving or whole previous home price. `E=max(0,Y-max(0,H-P))` equals the increase in `max(0,cumulative investment-H)` for nonnegative inputs. Independently tested 4,851 integer boundary combinations plus eight monetary examples. At H30,000,P25,000,Y12,000, E7,000 and regional base6,000 yield240 at4%. At P18,000,Y12,000, E0; one more euro gives E1. Once crossed, the threshold is not deducted again.
- Art14 expressly says “sin perjuicio” for the State-law legacy regional tranche. Independently established DT18 eligibility therefore uses separate national9,040 annual base; regional6,000 does not displace it. No invented carry-forward is authorised by annual-cap excess.
- Art18.2 confines the same-asset bar to credits in the Canary chapter. Exact AEAT explains its same-home application even for different payments. The Guide correctly retains this bar among Canary acquisition/energy/disability claims while preserving the separate State-law route.
- Art14quater applies the15% gross-quota cap to arts6/14/14bis/14ter, not State-law legacy relief. Art18.1 and LIRPF77.2 retain regional nonnegative settlement. With9040×7.5%=678 legacy regional relief, gross1,000 permits min(240,150,322)=150; gross700 permits min(240,105,22)=22; at678 or below no regional quota remains for Canary credit. At gross1,000 regional credit828 leaves172. Total1,506 requires the State-quota assumption identified above.
- Art18.3 expense-covering exempt public aid base reduction is preserved. No threshold/grant mixed-order numerical case is certified here.
- Historic-cohort entitlement, joint-return mixed-rate priority, and mixed-purpose refinancings are not certified by this review. The Guide expressly retains the precise residual reservation. New2026 purchases are not conferred DT18 status.

## Source receipt and read controls

Read current primary law and exact AEAT texts after verifying raw receipt hashes; independently parsed raw HTML rather than treating the writer proposal as authority. `source-receipts.json` and `supplement-source-receipts.json` record eight verified raw-source hashes. `*-raw-verified.txt` files preserve independent text extractions. Current BOE also freshly opened with web tools. Direct Python fresh network fetch failed DNS under the sandbox; no claim of fresh raw download is made. The permitted verified-raw route was completed.

## Structural and arithmetic controls

`canarias-controls.json`, `canarias-arithmetic.json`, `canarias-existing-examples.txt` and `canarias-diff.patch` record the checks. Exactly nine author H2 sections remain, plus the protected platform CTA H2. Frontmatter, CTA and both oa-check blocks are byte-identical to the prior baseline. All bytes before the changed Canary acquisition paragraph and after the insertion are identical after reversing only the exact new source row and Canary residual-phrase replacement. No other regional addition was reviewed as integrated.

Existing example checker: `checked 1 files, 2 oa-check blocks, 0 failures, 0 missing`. Independently recomputed their property choice180, medical480, regional total660/liquid540, maternity/childcare differential−850 and Asturias carry uses700/1,000/1,000 with300 expiry and4,700 total use.

No Guide edits, commits or pushes performed. Finite outcome: core law/formula and regional arithmetic supported; one explicit State-quota assumption required before clearing this exact delta.
