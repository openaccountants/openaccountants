# Independent review: Iraq PR #1208

Reviewed frozen pushed head: `738555d48c711d7212305f2af625beb4c26cb818`.
Actual merge base: `79cc1bb401ad9268b7c07d1ac1a78d4b137be630`.
Original PR head: `2b761b3fd33b65ec0b658a0db3987d787d9877fa`.
Reviewer: fresh Codex independent-review agent, 2026-11-01. This is a source review, not an accountant attestation. No Guide, commit, PR approval or merge was made by this reviewer. No earlier thirteen-figure receipt was adopted.

## Verdict

**Focused corrections required before approval.** All 51 ledger rows were independently read against their cached source originals or reviewed as holds/recommendations. Forty rows pass at their stated source-version/hold scope; eleven have the corrections below. None establishes complete current 2026 law. The limited source-version pack is acceptable in principle once these focused issues are closed. It must remain partial, and issue435 must remain open.

## Required corrections

1. **IQ-021, payroll allowance table:** the 2019 PDF3 table specifies `الموظفة الأرملة أو المطلقة المستقلة بذاتها`. Retain the condition that the widow/divorced woman is independent in her own right beside IQD3.2m, in the Guide and ledger claim. The general family-condition caveat does not name this condition.
2. **Exact-quotation repairs, JSON and corresponding per-Guide Markdown ledgers:** IQ-005 and IQ-010 replace `المائة` with `المئة` in the fifteen-percent quotation (law PDF16); IQ-009 replace the altered `تبليغ` construction with `على السلطة المالية أن تبلغ المكلف خطيا بدفع الضريبة معينة مقدارها وتاريخ استحقاقها` (PDF33); IQ-011 starts `نسبة %15 ثابتة من دخل الشركات ذات المسؤولية المحدودة`, not `بنسبة` (PDF16); IQ-036 ends `الشهر الذي تحققت فيه الضريبة` (hotel PDF2), not `الشهر الذي تحققت الضريبة فيه`; IQ-037 ends `موقعا منه او ممن يمثله قانونا` (sales PDF3), not `او من يمثله`. These do not change the rates but matter for an exact-quote ledger. Visual comparison allows line wrapping, spacing, equivalent numeral glyphs and standard Arabic hamza transcription; the listed lexical alterations are not mere layout differences.
3. **IQ-040:** repair note `hotelquoteinIQ029` to refer to IQ-031.
4. **Explicit predecessor-topic preservation:** add the risk-allowance exemption, employee-social-contribution deduction and undocumented-taxpayer single/unmarried fallback to the PIT-BASE hold (IQ-045). Add the Iraqi unified accounting framework to CORP-RETURN (IQ-046). Add assessment/calendar-year basis to OVERVIEW-ADMIN (IQ-049). These inherited subjects are archived and have broad nearby holds, but the new Sources lines do not name them. Record their precise hold destinations in the predecessor map. Do not restore the old figures as current law.
5. **Manifest read status:** all ten source entries currently say `read:false`, including the six sources relied on with explicit actual-read scopes/read dates. Set actual-read sources true at their limited recorded scopes, or use a clearly named field such as `complete_document_read:false` plus `scope_read:true`. Preserve the downloaded-only entries as unread. In particular, law PDF18 was read for art17 context in addition to PDF19; the payroll Sources scope should include both. This does not require claiming every law page was read.

## Source and scope inspection

I read AGENTS.md and docs/skill-template.md. I read all six changed Guides, the pack README, all per-Guide ledger rows, the JSON claim inventory, manifest and initial provenance, and the predecessor destination structure. I opened the rendered original pixels for law PDF pages5,6,13,14,16,17,18,19,20,21,25,26,33,34; payroll PDF3–6; sales PDF1–3; and hotel PDF1–3. The original property HTML main rent/payment text and neighbouring land/transfer/use-change text were read. The PDF text/OCR helped locate clauses; original pixels controlled scan quotation and amounts. Law article17 begins on PDF18 and continues on PDF19. Printed page numbers run one below PDF locators.

The sources support the historical nationality/source distinction, year/category timing, marginal scale, listed-company rate, same-year versus carried-loss distinction, foreign-credit conditions, narrowly framed outward-payment rule, public-sector pension/base/family cases, historical sales classifications/base/timing and undated property-page formula. The 2003/early2004 loss transition, art13 transitional neighbour, art19 annual-payment/bank/dividend neighbours, family notes4–8, local-producer/report conditions and2005 exchange amendment were inspected. No later full amendment chain was verified. No source acquisition was equated with a full read. No beyond-citation research was needed to resolve the listed transcription/condition issues: the cited originals themselves resolve them.

All six Guides prominently keep IQ-CURRENT and describe 2026 as routing only. Full filing workflows, private payroll/social insurance, oil, TP, treaties/PE and formation remain held. I found no current liability, zero-VAT, input-credit absence, bank-description exemption or automatic EXCLUDE conclusion escaping those holds. All seven core jobs remain partial. Formation is byte-identical inherited2025 material explicitly held by README/overview; it is not cleared by this review.

## Preservation and mechanical checks

- Source manifest: all10 cached SHA256 values match; no mismatches.
- Predecessor provenance: all14 snapshots match their recorded commit blobs and SHA256 values.
- `old-lines.json`: all931 nonblank lines exactly match both frozen stages, with no missing/extra/reordered line (343 actual-base,588 original-PR). Complete archival coverage is verified; semantic destination spot checks are listed below. Broad generic destinations do not independently establish every old legal statement.
- Protected platform metadata and **complete stamped CTA text** match actual merge base for all7 country Guides, including formation. The two original-PR colon changes are absent from the repaired head. Formation bytes match actual base exactly.
- Changed scope is six existing Guides, README and evidence only. No new Guide or generated package/index/llms output changed.
- Independently reran six `skill_checks.py` files:90/90 pass.
- Independently reran required examples:6 files,12 blocks,0 failures,0 missing. Cases were also reviewed in prose against law/formula/classification and recomputed; payroll uses the source scan’s rounded monthly method.
- Independently reran `validate-guides.py --changed-only --no-index-check`:6 Guides,0 warning groups,pass.
- A preliminary `validate-guides.py --help` invocation was not a help mode and executed full validation: it failed on pre-existing stale index/llms outputs and warnings in archived evidence Markdown. Those generated files were not edited. The required changed-only mode then passed as recorded above; no full-tree clean result is asserted.

Semantic predecessor spot checks at both stages: nonresident rate restriction; child dependency/proration; risk allowance and missing-document fallback; old March personal deadline versus historical report trigger; company oil/remuneration/return lines/manager ceiling/depreciation/dividends/resident interest/KRI royalty/contract instructions; private employer/employee contribution/base/cap/15-day remittance; property transfer exemption allegation; hotel instruction identifier/telecom/VAT-absence/registration/reverse-charge claims; bank patterns/agriculture/Arabic-books/KRI-dual-filing/old expected-answer cases. Supported topics are retained or linked; unestablished topics route to named holds, with the five precise subject-name gaps above requiring closure. Unsupported predecessor text remains nonoperative in the preserved snapshots.

**Lost content restored: 0 in this review.** The reviewer did not edit Guides. Five inherited subject names need explicit hold restoration by the writer as specified above. This is not a statement that all predecessor assertions were correct. No new tax entitlement or obligation is cleared by archival preservation.

## Every-row results

Machine-readable results: [independent-row-verdicts.json](independent-row-verdicts.json). Each row below records the original source/conditions check, not a current-law attestation.

| Row | Verdict | Independent finding |
|---|---|---|
| IQ-001 | Pass within scope | Law PDF6 arts5(1)–(3) supports nationality/source distinctions; foreign-credit neighbour read. No residence test inferred. |
| IQ-002 | Pass within scope | PDF16 art13(1)(a) first band and allowance precondition match. |
| IQ-003 | Pass within scope | PDF16 next250000, upper500000 match. |
| IQ-004 | Pass within scope | PDF16 next500000 through1m match. |
| IQ-005 | Fix | Rate correct; exact quote has المائة but PDF16 fifteen-percent line has المئة. Correct quote, also IQ010. |
| IQ-006 | Pass within scope | PDF16 nonresident scale and art19 exclusion match; no blanket allowance conclusion. |
| IQ-007 | Pass within scope | PDF5 arts3–4 read: year/category distinction and exceptions retained. |
| IQ-008 | Pass within scope | PDF26 art27(1)–(3) supports requested21days / before1June / legitimate excuse extension. |
| IQ-009 | Fix | Historical notice/payment description correct. Exact quote is not verbatim: PDF33 says على السلطة المالية أن تبلغ المكلف خطيا بدفع الضريبة معينة مقدارها وتاريخ استحقاقها, rather than تبليغ. |
| IQ-010 | Fix | Arithmetic correct; same quote correction as IQ005. |
| IQ-011 | Fix | Listed company rates correct. PDF16 quote starts نسبة %15 ثابتة من دخل الشركات ذات المسؤولية المحدودة, not بنسبة. |
| IQ-012 | Pass within scope | PDF20–21 art19 supports payment classes, due-abroad cash/credit trigger, bank exemption and annual-payment scope. Dividend exception not used as a current conclusion. |
| IQ-013 | Pass within scope | PDF13–14 supports same-year cross-source offset, five consecutive years/half/same-source carry and transition exclusions. |
| IQ-014 | Pass within scope | PDF6 art5(4) supports cap, five-year excess carry, first-vintage priority, per-country and receipt/authority proof. |
| IQ-015 | Pass within scope | Both source-conditioned loss computations correct; qualifying carried/current losses not conflated. |
| IQ-016 | Pass within scope | Circular PDF3 heading and5–6 distinguish state/public sector and temporary/permanent cases. |
| IQ-017 | Pass within scope | PDF3 note2 and5–6 permanent example support ten-percent nominal pension deduction; not extended to private insurance. |
| IQ-018 | Pass within scope | PDF3 note3 amount2.5m matches named single/separate-spouse cases; other table cases not represented as unavailable. |
| IQ-019 | Pass within scope | PDF3 note3 amount4.5m matches; qualifying merger language and notes4–8 retained. |
| IQ-020 | Pass within scope | PDF3 note3 amount5m supports incapacitated-husband case; medical/merger conditions retained. |
| IQ-021 | Fix | Amount3.2m correct. Source PDF3 expressly says الموظفة الأرملة أو المطلقة المستقلة بذاتها. Add independent-in-her-own-right condition beside rate in Guide and ledger claim. |
| IQ-022 | Pass within scope | PDF3 age strictly above63 and extra300000 match. |
| IQ-023 | Pass within scope | PDF3 qualifying children regardless of number /200000 match, complete eligibility remains held. |
| IQ-024 | Pass within scope | PDF3 note1 salary/overtime/other amounts excluding allowances matches only public-sector scope. |
| IQ-025 | Pass within scope | PDF4 notes4–8 read fully. Court custody, one-housewife spouse, signed January request/branch proof, incapacity report and otherwise own single allowance retained. |
| IQ-026 | Pass within scope | PDF4 note9 permits within-year over/underdeduction correction; source-limited wording correct. |
| IQ-027 | Pass within scope | PDF19 art17(3),18 supports employer liability even if undeducted and authority-set information period; PDF18 context also read. |
| IQ-028 | Pass within scope | PDF19 art17(4)21days from Minister-set timetable; no universal monthly date substituted. |
| IQ-029 | Pass within scope | PDF5–6 nominal700000/housewife/nochildren cases42083 and31583 match scan and difference10500. Monthly endpoint rounding explained. |
| IQ-030 | Pass within scope | All hotel PDF1–3 read: Decision36/1997, Instructions7/1997 and4/2005 identifiers correct. |
| IQ-031 | Pass within scope | Hotel PDF1–2 all-service value/excellent-first class/10percent match. |
| IQ-032 | Pass within scope | Sales PDF3 art4(3) imported tobacco/alcohol300percent customs-declaration base and separate local-producer clause match. |
| IQ-033 | Pass within scope | Sales PDF2 art4(1) imported cars15percent customs-declaration base match. |
| IQ-034 | Pass within scope | Sales PDF1–2 arts1(6),(9),4(2) national-carrier definition/domestic-international ticket scope match. |
| IQ-035 | Pass within scope | Hotel PDF2–3 invoice/bookkeeping and2005 replacement central-bank announced market conversion match. |
| IQ-036 | Fix | Timing/records correct. Exact hotel PDF2 wording ends الشهر الذي تحققت فيه الضريبة; ledger instead ends الشهر الذي تحققت الضريبة فيه. Correct quotation. |
| IQ-037 | Fix | Quarterly certified-form/signed report/first-half following-month rule and border-unit separation correct. PDF3 quote ends موقعا منه او ممن يمثله قانونا; ledger misses م in ممن. |
| IQ-038 | Pass within scope | Hotel PDF2 art6 collected/uncollected distinction and overdraft interest match; no unsupported current rate. |
| IQ-039 | Pass within scope | Sales PDF2 art2 historical installation-inside/outside scope matches; levy currentness/rate held. |
| IQ-040 | Fix | Both hotel/import arithmetic cases correct. Note cross-reference hotelquoteinIQ029 is wrong; hotel quotation is IQ031. |
| IQ-041 | Pass within scope | Original cached HTML main rent paragraph supports10percent after10percent=9percent. Authority page undated; statute/currentness not inferred. |
| IQ-042 | Pass within scope | HTML neighbouring transfer/use-change/land workflow paragraphs distinguish these from recurring rent; no transfer calculation. |
| IQ-043 | Pass within scope | HTML basic/additional/audit/manager/cash/receipt/posting steps and one/two instalment options match. Actual date windows not asserted current. |
| IQ-044 | Pass within scope | Both conditional property computations and180000 difference recompute; no entitlement inferred. |
| IQ-045 | Fix | Holds are operationally kept. Preservation needs named PIT-BASE topics: risk-allowance exemption, employee-SSC deduction, undocumented-taxpayer single/unmarried fallback, rather than broad exemption/allowance wording alone. |
| IQ-046 | Fix | Holds are operationally kept. Name inherited Iraqi unified accounting framework in CORP-RETURN hold (pre-pr corporate tax base). |
| IQ-047 | Pass within scope | Payroll/private/social/procedure/currentness holds kept; no private contribution conclusion escapes into body. |
| IQ-048 | Pass within scope | Sales/currentness/VAT-absence/telecom/customs holds kept; no zero-VAT/credit/registration conclusion escapes into body. |
| IQ-049 | Fix | Holds kept. Name inherited assessment/calendar-year basis in OVERVIEW-ADMIN hold; generic remit/workflow does not identify it. |
| IQ-050 | Pass within scope | Router TP/XB/currentness/legacy holds kept, not operative legal answers; formation expressly held. |
| IQ-051 | Pass within scope | Review flags retained as recommendations, automatic EXCLUDE removed, evidence-count arithmetic correct. No legally required document count inferred. |
