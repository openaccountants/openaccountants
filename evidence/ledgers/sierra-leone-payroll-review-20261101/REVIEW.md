# Independent Sierra Leone payroll source review

Review date: 2026-11-01. Frozen revision: `48a6568aa0346659987b56f60ab13552f2dc5419`. Original base: `aec6ba04066bb69d1168c8028ba11dd65cb90505`. Guide SHA-256: `e0445980105f60e8bdf55c0eb23c71e2ceebf441247e714591014d1ff08ddcae`.

**Changes requested before source-bound closure:** all 28 ledger rows and their relevant neighbours were checked. Three narrow body conditions/computation clarifications and one citation correction remain. This review does not certify operative 2026 law, a complete payroll filing method, full-country coverage or accountant attestation.

The review read the public `CLAUDE.md` and `docs/skill-template.md`. It independently re-fetched both official PDFs with valid TLS and matched the cached/writer hashes. The Act is 34 pages, SHA-256 `2a4150e7bf3acb633eb03a20234cb075c6255d3dad24506cc9c3588f94c827d8`; Regulations are 40 pages, SHA-256 `f6d0074cacf34c7b2d30c426e9969281002d568c9a62489d819055c32b42a7e2`. Actual scan pages visually read: Act 4–7, 15–18, 21–22; Regulations 4–9. OCR was a helper, not the sole basis for material wording. Full page-image hashes and exact read limits are in `source-read-manifest.json`. Current authority contributions/compliance main bodies were independently opened, including their split, timing, categories, SS4A and enforcement instructions. These pages do not prove a complete later-law chain.

## PR01: Carry the contractor normal-work condition into the body

Frozen Guide line(s): 22, 44. The draft says the definition includes work through contractors but never states that this contractor limb concerns employment in or in connection with the normal work of the establishment. Section2 also requires remunerated employment linked to an establishment. Keep the condition beside the contractor statement so the paragraph cannot be read as covering every contractor arrangement.

Required repair: State that persons employed by or through a contractor in or in connection with the normal work of the establishment are included, subject to the definition’s remaining conditions. Update SC02 wording consistently. Source: [NASSIT Act2001 s.2; physical PDF6–7](https://nassit.org.sl/images/NASSIT_Reports/act2001.pdf).

## PR02: Include self-employed people in the change-notice row

Frozen Guide line(s): 36, 54. The table labels the10day name/address/location change duty as an employer duty. Regulation2 expressly applies it to every employer or self-employed person, while the Guide’s scope and rates include opted-in self-employed people. Omitting that actor can cause a reader to miss their change notice.

Required repair: Label the row employer/self-employed business name/address/location change and name the Director-General as recipient; retain10days after change. Keep SC15 actor scope explicit. Source: [NASSIT Regulations2004 reg.2; physical PDF4](https://nassit.org.sl/images/NASSIT_Reports/Regulations.pdf).

## PR03: Make the invalidity exception usable as a workpaper rule

Frozen Guide line(s): 47. The whole-month trigger is correctly retained, but “specific credited-contribution treatment” does not state that no contribution is payable for that member or identify the credited amount. Section26 supplies both. Its prior12month reference matters because the general average-monthly-earnings definition elsewhere uses a different reference period.

Required repair: State no contribution is payable for a month throughout which entitlement exists; instead credit the contribution that would have been payable on that member’s average monthly earnings during the12months preceding the month entitlement began. Do not turn this source rule into a new benefit-eligibility claim. Update SC10. Source: [NASSIT Act2001 s.26; physical PDF17; neighbouring s.2 PDF5](https://nassit.org.sl/images/NASSIT_Reports/act2001.pdf).

## PR04: Link the Act provisions to the Act

Frozen Guide line(s): 34, 47. The base step4 link names Act ss.24,26,28 but points only to Regulations.pdf. The Regulations support the same-membership sentence, not the private-pension and invalidity provisions. The remittance row likewise names Act s.25(3) in a Regulations-only link, although reg.8 independently supports the timing.

Required repair: Split the citations by document, linking Act references to act2001.pdf and reg.8 to Regulations.pdf. In the timing row either give two links or label only the supporting reg.8 source. Source: [Act ss.24,26,28 and Regulations reg.8; physical ActPDF15–18,RegPDF6](https://nassit.org.sl/images/NASSIT_Reports/act2001.pdf).

## Every ledger row

The source hash for each row, article, page locator and visual excerpt check is in `review.json`. The following notes record the actual substantive checks.

| Row | Result | Check |
|---|---|---|
| SC01 | Verified | Act15–16 ss.23–24: every employer/worker within defined scope; self-employed opt-in and conditions; other-law exemption preserved; private pension does not exempt. Ceased-employment voluntary continuation in s.23(2) was read as neighbour; no exhaustive eligibility claim made. |
| SC02 | Repair PR01 | Act6–7: remunerated employment/establishment definition; by/through contractor normal-work limb; Sierra Leone non-crew limb; permanent-resident ship-owner office/agent or overseas Sierra Leone employer limbs. Territory/permanent-residence conditions correct; contractor normal-work condition should be explicit. |
| SC03 | Verified | Act5: paid/payable cash emoluments at fixed/determined intervals, normal work/tasks/volume and leave; all listed exclusions match. Printed “cost of leaving” is real in scan and held rather than silently changed. No no-cap or gross-pay assumption adopted. |
| SC04 | Verified | Act16 s.25(1):5%, immediately month end, irrespective of actual payment. Matches table/base and example premise. |
| SC05 | Verified | Act16 s.25(2):10% per worker/month. No employer-share recovery under s.25(5)(a) and no remuneration reduction under s.29. |
| SC06 | Verified | Act16 s.25(4)15% income each month from profession/vocation/business/occupation for self-employed person agreeing to membership; s.23(1)(b)regulation conditions remain adjacent. |
| SC07 | Verified; citation PR04 | Act16 s.25(3)15days after month end for employee/employer contributions; Reg6 reg.8(1)also states deadline for employer/self-employed. No PAYE-calendar inference. Source labelling correction requested. |
| SC08 | Verified; ledger precision note | Act16–17 s.25(5):own-share recovery prohibited; prior-period member deduction prohibited except accidental mistake OR clerical error, with written Trust-inspector instructions. Guide slash phrasing is consistent; writer ledger compressed “accidentalclericalmistake” should spell the OR out when touched. |
| SC09 | Verified | Act17 s.25(6):deducted contributions deemed held in trust until paid; Guide does not claim all unpaid payroll amounts are trust money. |
| SC10 | Repair PR03 and PR04 | Act17 s.26:whole month of entitlement to invalidity pension; no payable contribution; credit equivalent to contribution on member’s average monthly earnings during12months preceding entitlement month. Correct direction/whole-month trigger but draft needs explicit no-payable and credit-base rule; link points to wrong document. |
| SC11 | Verified; citation PR04 | Act18 ss.28–29:each concurrent employer responsible only for own obligations; no direct/indirect reduction of earnings/other emoluments because of statutory liability/charges. Reg8(2)does not replace Act28. |
| SC12 | Verified | Act15 s.20(2):contributions tax deductible. Body explicitly withholds current PAYE-return/limit implementation; no invented return field or automatic complete deduction computation. |
| SC13 | Verified | Act21–22 s.38:old-age pension/gratuity,retirement grant,invalidity pension/grant,survivors pension/grant plus conditional prescribed benefits. Guide uses non-exhaustive class summary, makes no eligibility/amount promise; s.39 neighbour read incidentally not certified. |
| SC14 | Verified | Reg4 reg.1(1):employer/self-employed,30days from Regulations commencement or Act-applicability date;SS2A/SS3. Reg1(2)branches deemed one establishment read. No simple30days-from-incorporation substitution. |
| SC15 | Repair PR02 | Reg4 reg.2:every employer OR self-employed business name/address/location change; furnish Director-General new details within10days after change. Timing correct; self-employed actor missing in table. |
| SC16 | Verified | Reg5 regs.3–6:registration numbers;SS1A appropriate parts certified by Trust inspector; unable employee supplies necessary particulars; self-employedSS1A/SS3 and other required forms; existing member supplies certificate or other membership/number evidence. Draft says certified as prescribed and records issued numbers; no invented current portal flow. |
| SC17 | Verified | Reg5–6 reg.7:employer notifies Director-General within30days after employee ceases or establishment ceases; employee may also notify. Draft correctly retains two clocks, no claim employee report replaces employer duty. |
| SC18 | Verified | Reg6 reg.8:15days after contribution month;concurrent employers’ amounts credited under same membership. Reg14(4)repeat condition also read; no one-employer exemption. |
| SC19 | Verified | Reg6 reg.9:person assuming employer responsibility for establishment liable for contribution/other monies and document defaults of previous employer. Workpaper reference is bounded by its terms; no share-sale/asset-sale universal safe-harbour claim. |
| SC20 | Verified within stated scope | Reg6 reg.10:nearest Area Office;specified instruments/approved delivery points;other manner Director-General authorises in writing. Draft intentionally does not reproduce a fully authenticated current electronic filing/payment method; hold is explicit. Current authority page’s cash/cheque/bank transfer instruction independently read but not treated as full legal authorisation chain. |
| SC21 | Verified | Reg7 reg.11:SS4A accompanies all contribution payments or other forms/media authorised in writing; consolidated branch/sub-office/depot payment conditional on separate schedules and distinct unit amounts. Both conditions retained. |
| SC22 | Verified | Reg7 reg.12(a)–(g):employer identity/location/postal address/number;payment manner;each employee identity/number;earnings;deduction;employer contribution;period total. Draft covers all7statutory field groups. Actual current electronic boxes remain outside approval. |
| SC23 | Verified | Reg7 reg.13:officialSS4B dated,stamped,endorsed by authorised Trust official is prescribed discharge receipt for contributions/other monies. Draft distinguishes bank movement from receipt and holds current electronic equivalent. |
| SC24 | Verified | Reg8 reg.14(1)–(4):Director-General satisfied payment not due;refund discretionary;no refund if benefit already paid to member/dependants;may withhold against monies due;may require written application/information. Draft says conditions apply and does not promise automatic refund. |
| SC25 | Verified | Reg8 regs.15–16:employee name,SSnumber,pay,deductions;necessary modifications for self-employed records;minimum12years after end of relevant pay period. Draft table plus record step preserves core employer record/retention rule; actor-specific modern record format unclaimed. |
| SC26 | Verified | Act17 s.27(1)(a):90dayTreasurybill rate plus20%OFthat rate,compounded monthly. No20percentage-point or flat20%penalty error. Applicable rate and period conversion explicitly unresolved. |
| SC27 | Verified | Act17–18 s.27(1)(b):demand served;unpaid contribution+interest30days later;further10%OF90daybill rate on total outstanding for each default month. Legal recovery/criminal proceedings separate. s.27(2)remission text read with printed cross-reference defect; no remission implementation certified. |
| SC28 | Verified | Act18 s.30:non-registration offence;immediate registration;contribution arrears+interest/penalty under s.27. OriginalLe5million/3month wording read; draft withholds current monetary fine pending denomination/later law. No offence-fine conversion invented. |

## Examples, preservation and mechanical checks

Both legal premises and arithmetic pass within the explicitly hypothetical source-bound assumptions. Case 1 gives 500 employee, 1,000 employer, 1,500 remittance and 11,000 wage-plus-NASSIT cost. Case 2 gives 13,000 gross, 1,500 correctly classified contribution versus 1,950 on gross, a 450 overstatement. Case 2 is a classification decision, not an optional election. Neither case certifies PAYE, an operative ceiling or a current filing.

All ten old payroll bullets match their exact pinned texts and whole-file hash, and have an independently checked new section or explicit hold. PAYE’s old 0%–30% range/calendar, old NLe 800 minimum wage, no-cap approximation and generic 10%–12% employer-cost claim are held rather than applied. **Lost content restored: 0.** No silent loss was found. Five other 2025 Guides are byte-identical to the original base. The initial 69-topic/six-file snapshot remains historical; the README correctly links the ten-topic payroll delta instead of treating the old payroll file as still unchanged.

All six compared platform metadata fields, the additional historical platform keys and the entire payroll CTA suffix are exact against the pinned predecessor. Description length is 114 words; YAML version and heading both say 1.0. All 15 shape checks pass, both `oa-check` blocks pass, PR-mode validation has zero warnings, strict metadata audit has no errors/warnings/notices, and pinned diff whitespace passes. Full outputs are in `validation.json`. One `--help` probe unexpectedly ran the validator’s full-tree mode and failed on stale generated `index.json`/`llms-full.txt`; these were not changed, and the correct PR-mode check passed. A sandbox `git fetch origin` failed DNS resolution; local HEAD and the existing tracking ref both equal the frozen revision. This review makes no claim that those cached refs establish the live remote tip.

README correctly describes two source drafts, five legacy 2025 Guides and seven partial tax domains. Prior transfer-pricing content review was not repeated. Ordinary current authority pages are corroboration only; independent source review is not professional review.

## Limits and closure

- Complete commencement and subsequent amendment/instrument chain, operative2026 consolidation and additional exemptions/earnings ceiling were not proved.
- Printed included-allowance “cost of leaving” interpretation remains unresolved; no silent correction to “living”.
- PAYE bands/base/deduction/return fields/penalties and separate remittance calendar, minimum wage and generic employer-cost estimate remain held.
- Detailed benefit eligibility/amounts, treaty/social-security agreements, applicable interest rates/conversion/remission and redenominated fines remain held.
- No current e-registration/payment/SS4B-equivalent authentication or successful live filing test.
- No accountant attestation, full-country coverage signoff, merge/publication authority, or repetition of already closed TP source review.

Writer repairs PR01–PR04 and updates the ledger/freeze, then the reviewer checks only the repaired text, affected ledger rows, citations, hashes and checks for closure. Preserve all current-law and implementation holds. No Guide, writer ledger, country README, source cache or writer manifest was edited by this reviewer. No commit, push, PR comment, merge or production action was performed.
