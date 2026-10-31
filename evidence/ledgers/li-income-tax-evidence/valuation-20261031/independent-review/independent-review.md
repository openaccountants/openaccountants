# Independent review: ordinary unquoted-share valuation addition

**REPAIRS REQUIRED.** All 21 added source groups and all six arithmetic controls pass. One P3 provenance repair remains: advance the Guide’s `last_updated` from 30 to 31 October 2026.

Candidate: `6656f8a86a02d98aa5548790be1ba672b47a3786`. Base: `b41220632936e5c1a211254030b6acb659f6870a`. Reviewed 31 October 2026. Scope is the 12-file valuation follow-up delta. Earlier country-pack reviews remain historical to their exact reviewed snapshots. This report is source/editorial review, not accountant attestation or a new comprehensive country certificate. The current README’s IT-IND municipal-rate partial is unchanged.

## Required repair

**VAL-F1, P3, Guide line 18, frontmatter.** The material new version 0.4 and all 21 new source rows are researched/read 31 October; `last_updated` still says `2026-10-30`. Set it to `2026-10-31`, refresh the exact Guide hash in both ledger files, and submit the exact repair for recheck. Evidence: Guide line 18, new helper Sources entry, VAL01–VAL21 read dates and source-receipt.json. This is a provenance finding, not a tax-law defect. No source/public file was altered by this review.

## Source and formula review

I read article 7a across printed pages 4–5 and independently rendered and personally viewed printed pages 34–36 of the original 56-page [official ordinance](https://www.gesetze.li/konso/pdf/2010437000), consolidated 1 July 2026. The formula images are absent from text extraction, so text/quote binding alone was not used. My rendered previews are retained here.

I independently opened the original 25,232-byte [official 2026 workbook](https://www.llv.li/servicekonto/steuerverwaltung/unternehmensanteile-ohne-kursnotiz-bewertung-2026.xlsx) as read-only native OOXML. Sheet Bewertung 2026 contains the reviewed date instructions, P44/P57 ROUNDDOWN formulas and the shared F70 allocation/discount input. `workbook-original-ooxml.json` records the original formula text and stored values. This is no assertion of native Excel recalculation. Cached blank-workbook results and an imported engine’s blank-sheet #N/A are not proof of tax correctness or a native defect.

The Guide correctly separates operating A from substance-only B, retains banks/insurers’ exclusion from B finance companies, uses K=20% only for the supervised regulated category and K=15% otherwise, removes and restores the article 54 asset pool once, keeps the 60% operating-substance plus 100% excluded-assets minimum, and bases C’s minority bands on votes. It separates votes from economic interest and does not automatically extend C to B. Helper rounding is expressly separate from statutory valuation, total-wealth rounding and final-tax rounding.

Annex A(3) does not state a universal zero-floor for S. Although helper P26/AB27 uses MAX(...,0), the Guide does not turn that helper operation into a statutory rule or claim extraordinary/insolvency/unequal-class cases are complete. No extra repair is warranted for that boundary in this ordinary-method addition. Actual classifications, valuations, consolidated reserve adjustments and exceptional results still require their stated evidence.

## Every added ledger group

| Group | Result | Original evidence | Independent conclusion |
|---|---|---|---|
| LI-IND-VAL01 | PASS | SteV7a(3); printed pages 4–5 | Article 7a(3), across printed pages 4–5, supplies last closed accounts before holder tax-year start, commercial-law consolidation and permitted equity/result deductions for unrecorded tax-permitted reserves. Guide preserves these gates. |
| LI-IND-VAL02 | PASS | SteV7a(2)(a); printed page 4 | Article 7a(2)(a) permits departure when taxpayer proves ordinary valuation is not market value. Guide requires proof rather than giving an elective preference. |
| LI-IND-VAL03 | PASS | SteV7a(2)(b); printed page 4 | Article 7a(2)(b) makes independent-party actual purchase price market value while economic situation has not materially changed; Guide carries both conditions. |
| LI-IND-VAL04 | PASS | SteVAnnex1A(1); printed page 34 | Personally inspected the printed page 34 formula image: U=(2E+S)/3 for operating trade, industry and services. Formula and operating classification match. |
| LI-IND-VAL05 | PASS | SteVAnnex1A(1); printed page 34 | Printed page 34 removes shareholder/non-business assets from substance weighting and corrects earnings for their capitalised net result, then restores the asset pool once. Guide and positive-earnings control do this. |
| LI-IND-VAL06 | PASS | SteVAnnex1A(1); printed page 34 | Printed page 34 minimum is 60% operating substance plus 100% shareholder/non-business asset pool, not 60% of total assets. Guide and asset control use that distinction. |
| LI-IND-VAL07 | PASS | SteVAnnex1A(2); printed page 34 | Personally inspected printed page 34 earnings formula: (2R(n)+R(n-1))*0.85/(3K). Current/prior weights and denominator match. |
| LI-IND-VAL08 | PASS | SteVAnnex1A(2); printed page 35 | Printed pages 34–35 combine 0.85 risk factor with commercial net results corrected for non-business expenses. Guide separates adjusted R and capitalised E. |
| LI-IND-VAL09 | PASS | SteVAnnex1A(2); printed page 35 | Printed page 35 expressly sets negative earnings value to zero; Guide max(0,...) and negative-result control match. This is an E floor, not a blanket S floor. |
| LI-IND-VAL10 | PASS | SteVAnnex1A(2); printed page 35 | Printed page 35 annualises any non-twelve-month period and uses substance until new-company results are representative; Guide preserves both. |
| LI-IND-VAL11 | PASS | SteVAnnex1A(2); printed page 35 | Printed page 35 permits authority adjustment for fundamentally changed activity or materially exceptional results, to obtain representative values; Guide does not give taxpayer an unrestricted adjustment election. |
| LI-IND-VAL12 | PASS | SteVAnnex1A(2); printed page 35 | Printed page 35 capitalisation rate is 20% for regulated financial institutions/service providers under FMA supervision and 15% for all other legal persons. Guide and FMA control match. |
| LI-IND-VAL13 | PASS | SteVAnnex1A(3); printed page 35 | Personally inspected printed page 35 formula image: S=EK+SRB+SR. EK is after profit appropriation; participation hidden reserves and taxed hidden reserves are distinct additions. |
| LI-IND-VAL14 | PASS | SteVAnnex1A(3); printed page 35 | Printed page 35 requires underlying unquoted-company interests valued under A(1) and carrying value retained when higher. Guide correctly retains this floor. |
| LI-IND-VAL15 | PASS | SteVAnnex1B; printed page 36 | Printed pages 35–36 Annex B uses A(3) substance for holding, finance, property, liquidation and inactive companies. Guide does not route all such companies to earnings weighting. |
| LI-IND-VAL16 | PASS | SteVAnnex1B; printed page 36 | Printed page 36 excludes financial institutions, particularly banks and insurers, from B finance companies. Guide keeps this exclusion separate from FMA rate selection. |
| LI-IND-VAL17 | PASS | SteVAnnex1C; printed page 36 | Printed page 36 C refers specifically to A company value and voting-right share; private contracts are disregarded. Guide separates capital economics from voting and does not automatically extend C to B. |
| LI-IND-VAL18 | PASS | SteVAnnex1C; printed page 36 | Personally inspected printed page 36 voting table: <20% ->20%, >=20% and <50% ->10%, >=50% ->0%. Exact 20% and 50% control boundaries match. |
| LI-IND-VAL19 | PASS | Official 2026 helper, Bewertung 2026 cells A1,A3; Bewertung 2026: A1, A3 | Independently read original native OOXML shared strings A1/A3: 2026 title, 1 January 2026 date, 31 December 2025 calendar accounts, last preceding closed accounts and twelve-month annualisation. No cached-result inference used. |
| LI-IND-VAL20 | PASS | Official 2026 helper, Bewertung 2026 cells P44,P57; Bewertung 2026: P44, P57 | Independently read native formula text P44=ROUNDDOWN(P43,-2), P57=ROUNDDOWN(IF(W56=0,V62,AB27),-2). Guide labels these as helper company rounding, not statutory total-wealth or final-tax rounding. |
| LI-IND-VAL21 | PASS | Official 2026 helper, Bewertung 2026 cells F69,G70,J70,K70; Bewertung 2026: F69, G70, J70, K70 | Independently read native formulas G70=$P$57*F70 and J70=LOOKUP(F70,U83:W85), K70 applies returned discount; lookup thresholds 0/.2/.5 give .2/.1/0. Guide identifies the single-input limitation and requires separate economic/voting facts. |

## Arithmetic and preservation

My independent Decimal evaluator recomputed four new controls and the two existing Guide blocks: **6 executions, 46 expected fields, all PASS**, using absolute tolerance CHF0.000001 for displayed repeating six-decimal values. Detail: `arithmetic.json`. The ordinary case gives E=623,333.333333…, U=582,222.222222…, helper company value 582,200, and separate-vote holder amounts 46,576 / 52,398 / 58,220. The negative-earnings case uses E=0 and the 300,000 substance minimum. The non-operating-asset case gives total 682,222.222222… and minimum 360,000. The supervised FMA case gives E=467,500 and U=478,333.333333…; qualifying B/new-company cases use 500,000 substance.

The controls’ company classifications, reserves, article 54 pool, no-transfer override and representative-results facts are stated assumptions, not conclusions about a real taxpayer. The existing tax example retains an illustrative municipality rather than claiming a verified 2026 municipal rate. The repository checker independently reports 6 blocks and zero failures; targeted schema validation reports one Guide, zero errors/warnings. The first schema import lacked the scripts path; the corrected import passed.

Compared directly with the stated base: all original 121 rule objects, 94 old-topic destination objects and the explicit successor map are unchanged; both original Guide blocks are exact. All old source table rows, URLs and read dates survive. Markdown references are unique and resolve. The CTA is exact. Protected metadata is unchanged except the authorised version increase. The old broad unquoted-valuation workpaper gap is narrowed to the supplied ordinary method, while actual classification/value evidence, foreign assets, disputed/actuarial rights and unequal classes remain stated limits. No meaningful prior topic was lost. Machine detail: `continuity.json`.

All 12 changed candidate files were hashed before/after review and remained byte-identical; the worktree stayed clean. `exacthash-manifest.json` records every path, byte count and SHA256. Guide hashes:

- `skills/international/liechtenstein/README.md`: `eb1e599fe663290ed700e24a63c58e9a7af07288caf06866d5b7aabba17029a8`
- `skills/international/liechtenstein/li-income-tax.md`: `c68edca525d15b86768503ad8cb6b9d77e64bbf7e6a3c4faac839e56bdf849e2`

The sole open action is VAL-F1. Source content is suitable for this bounded publication once that provenance repair is verified. No review status, named accountant attestation or remaining country coverage is upgraded by this report.
