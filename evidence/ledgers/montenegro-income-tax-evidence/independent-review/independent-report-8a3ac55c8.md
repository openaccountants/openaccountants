# Independent Montenegro PIT review

Candidate: `8a3ac55c83def25a74fc39f3d184afb87c543603`. Result: **NEEDS FIXES**.

This review covers the bounded publication of the pausal scale and promulgated GPP-FL schedules, the complete changed PIT Guide and its figure ledger. It is an independent source review, not accountant attestation or a declaration of complete Montenegro coverage. OWNERS.md and docs/skill-template.md were read. No publication file or history was changed.

All 167 ledger groups, including their constituent figures and rules, were read against the complete retained corresponding articles or form pages. All 159 unique cited source contexts were checked. All actual PDFs independently re-extract byte-for-byte to the saved text; both actual Word originals match their XML text after whitespace normalization. All manifest hashes/byte lengths match. The mislabeled administration original and the notice provenance are findings below. Invisible PDF/Word formatting markers are removed for word matching; raw context hashes match except the notice.

The original pausal scale was independently rendered and visually checked in full. The main and all 13 attachment field pages were independently rendered and viewed. All 29 GPP-FL pages were read as complete page text, including the instructions. The pausal table has 16 correct ceiling-based annual rows: PIT alone in column 5; column 6 = PIT + 11% contributions. Exact 30000 is within less-than 30000.01; 30000.01 is excluded. Principal/profession/VAT/own-product gates, four activity classes, ordinary/seasonal payment routes, ZPO chronology and KPP fields were checked. A rulebook group never overrides a statutory activity exclusion.

The A loss-row 9/10, A1 total 2.1+2.2, F11 income/tax-column, F13/14 cap-row, main occasional-work note and H withholding conflicts are real printed-source discrepancies. The Guide correctly prioritizes statute over those directions. A/PPG five-year loss limits, A band separation, A1 component balances, B/D/E certificates and destinations, C same-year losses, F categories/proof/certified translation and G authority assessment were checked. Foreign salary requires each month's salary bands. Partial-year rounding is properly not certified: 23.01 × 302 = 6949.02 versus full precision 6950.14.

The independent Decimal implementation recomputed all 34 affected blocks and every expected field: 11 originals plus 23 new controls, with zero arithmetic differences. CTRL19 fails its tax assumptions until distinct source-country facts/caps are supplied. Arithmetic success does not validate those assumptions. All 14 classification boundaries pass against the statute and printed source, subject to actual taxpayer facts.

Nine other current Guides are byte-identical to frozen predecessor files, manifest hashes and Git base `6d3d2d5c64103b37d4859c1b1a597a55f063f4f8`. All 11 original oa-check blocks remain verbatim: 2 in the current Guide and 9 in the linked appendix. All 415 nonblank predecessor lines have destination-map records with correct text/hash; all exact destinations resolve. CTA and protected metadata are unchanged. Original business, relief, property, share, gambling and cross-border topics were spot-checked against predecessor in addition to full ledger review. Prior 24 October review files remain retained historical evidence and were not freshly attested. README retains IT-IND partial and explicitly denies re-attestation of nine other Guides. It needs the additional foreign-salary-advance mapping gap below.

Fresh official webpage checks confirmed the 27 February paper ZPO deadline and Gazette publication 20 May/in force 21 May dates. A bounded fresh PIT PDF request failed DNS in the local shell and direct web-open timed out; an official-domain indexed result confirms the retained article 44 wording. This did not change the retained-source evidence or resolve unsupported portal mappings.

## Findings

### ME-R01: tax_rule

Stake deduction applied to lottery, betting and global jackpot alike.

Guide lines: [145]; ledger: ME-PIT-083. Source: PIT Law 37s(2)(1)-(3); 160/25 art. 10.

Required: Restrict stake deduction to lottery/betting; global jackpot uses total accumulated prize as defined in 37s(2)(3).

### ME-R02: missing_eligibility_gate

New-hire relief gives conditions without former founder/related-employer employment exclusion.

Guide lines: [150]; ledger: ME-PIT-085. Source: PIT Law 32b(3).

Required: Include exclusion for someone previously employed by a founder or related employer, regardless of break in employment.

### ME-R03: unsupported_credit_basket

Universal source/category cap and prohibition on using credit against another income source.

Guide lines: [228, 234, 252]; ledger: ME-PIT-138, ME-PIT-142, ME-PIT-150, ME-PIT-164. Source: PIT Law 44(1)-(2), 45; GPP-FL pp. 24–26.

Required: Anchor foreign credit to relevant foreign country and treaty; do not invent category baskets. Specify separate foreign countries and no treaty variation forCTRL 19. Preserve original appendix verbatim with separate qualifying note restricting its prohibition to single-dividend facts.

### ME-R04: ordinary_return_gap

Settlement crosswalk contains foreign-salary tax but no route for crediting its Montenegro five-day self-payments.

Guide lines: [232, 351]; ledger: ME-PIT-141. Source: PIT Law 42(4), 46(7); GPP-FL main pp. 3–6.

Required: State statutory credit for Montenegro advances and explicitly retain unresolved printed/live field for prior Montenegro payments on foreign salary in Guide and README. Do not invent portal field or require tax twice.

### ME-R05: ledger_bindings

Cross-act same-number selectors add unrelated articles; lettered ranges and operative rate/commencement mappings omitted.

Guide lines: []; ledger: ME-PIT-001, ME-PIT-013, ME-PIT-061, ME-PIT-062, ME-PIT-063, ME-PIT-083, ME-PIT-090, ME-PIT-098, ME-PIT-157, ME-PIT-161, ME-PIT-163, ME-PIT-165, ME-PIT-166, ME-PIT-167. Source: Current retained primary sources.

Required: Repair explicit article mappings listed in ledger-dispositions. Retain Gazette publication/commencement record for 21 May date. CorrectCTRL 21/22 source-ledger IDs.

### ME-R06: provenance

Administration-law.pdf is actually Word; notice extraction unmanifested and context hash unreproducible.

Guide lines: []; ledger: ME-PIT-124, ME-PIT-147. Source: File signatures/ZIP XML; source manifest; notice original HTML.

Required: Name/declare administration original DOCX preserving bytes. Parse operative notice text excluding scripts/JSON-LD, add TXT to manifest, quote operative deadline/paper words and hash full identified context reproducibly.

### ME-R07: overbroad_payer_duty

Other payers 31 January duty stated for all other income.

Guide lines: [174]; ledger: ME-PIT-102. Source: PIT Law 47(5): ostalim ličnim primanjima iz člana 14.

Required: Specify payers of other personal earnings under article 14.

### ME-R08: scope_ambiguity

All VAT payments called neither income nor expense.

Guide lines: [112]; ledger: ME-PIT-065. Source: Guide 94 own distinction between output VAT/recoverable input VAT; PIT 18/20 accounting base.

Required: Constrain line to output VAT remittances/recoverable input VAT; nonrecoverable VAT follows relevant expense or asset treatment.

## Ledger/control binding repairs

- 001: commencement is 160/25 amendment art. 21, not consolidated PIT art. 21; remove unrelated consolidated art. 3 selection.
- 061: add rate art. 10 or 49a. 062/063: add rate art. 10 or 50. 157: add art. 10 for business bands.
- 161: add arts. 37b/c; 163: add art. 37p; 165: add arts. 37j/k/l/lj. Full lettered ranges cannot be reduced to endpoints.
- 090: remove unrelated PIT arts. 24/42/55; 166: remove unrelated PIT arts. 8/9; 098: remove unrelated VAT selectors.
- 001/013/083/167: retain and bind Gazette record supporting actual 20 May publication / 21 May commencement.
-CTRL21:source IDs needA 1 andcontribution rules, not generic 140-143.CTRL22:source IDs needZPO/KPP 124/125, not 140-143.

The dividend appendix should remain verbatim with a separate explanatory qualification. Same-country category credit allocation is not established by the cited statute; the printed aggregateF 15 and live statutory country-cap workpaper interface must remain a gap unless verified. Other ordinary 2026 gaps must remain in README.

No push, GitHub comment, commit or tax filing was performed. Recheck the exact repaired commit before PASS.

Formatting correction: restored exact Git hashes and compact identifiers (including A1, CTRL19 and lettered statutory articles), and repaired spacing. The original findings and NEEDS FIXES conclusion are unchanged; no repaired candidate has been rechecked in this correction.
