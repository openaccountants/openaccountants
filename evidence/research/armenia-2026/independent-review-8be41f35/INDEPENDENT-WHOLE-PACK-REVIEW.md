# Armenia 2026 independent whole-pack review

**Result: incomplete. Do not publish this commit as a completed country pack.**

Reviewed commit: **8be41f35008a35214c20e9bcd5463e46b574a228**. Review date: **26 October 2026**. Review snapshot: `/private/tmp/oa-armenia-bounded-independent-review-2026-10-26`, extracted with `git archive` from that exact commit. All ten Armenia Guides and their README were read. The source checkout was not edited. This report makes no accountant attestation and does not clear any later commit.

The seven core tax Guides have the required structure and exactly two executable examples each. Their 14 controls pass. Independent Decimal calculations also reproduce their central results. Those checks do not close the missing ordinary methods. In addition to the README's six declared partial domains, the corporate Guide omits a material ordinary deduction restriction, so the present corporate-complete assertion is premature.

## Findings requiring changes

Paths below are relative to the reviewed snapshot. Line numbers refer to the exact reviewed SHA.

### 1. Corporate tax omits the ordinary offshore management-service deduction cap

**Material ordinary-method omission.** `skills/international/armenia/am-corporate-income-tax.md:74–89` claims an ordinary capped-cost method, cites Articles 116–120, but supplies no Article 118 method. `README.md:26` says corporate ordinary methods are supplied and leaves IT-CORP outside `partial`.

Fresh native [Tax Code Article 118](https://www.arlis.am/hy/acts/215611/latest) limits qualifying management-service expense paid to the stated no-PE nonresident corporate/individual providers to **2% of annual gross income**. The registration-year permitted ceiling is **the greater of 2% of gross income and AMD 2 million**, bounded by actual qualifying expense. Article 118(3) has specified IT/computer-innovation founder and international credit/grant exceptions. Article 118(4) defines actual management and expressly distinguishes management consultancy and trust management.

Implement classification, recipient/PE status, actual expense, gross-income cap, registration-year branch, exceptions and the once-only add-back. Hypothetically, an established ordinary company with AMD 100m gross income and AMD 5m qualifying offshore management expense can deduct AMD 2m before any established exception. Omitting the cap understates its 18% tax by AMD 540,000. See `independent-arithmetic.json`.

The source is already available. This is not a portal or professional-signoff issue. Until repaired, IT-CORP needs an honest partial reason. The general pointer to other restrictions is not an executable cap.

### 2. The purported complete micro screen compresses two ordinary exclusions ambiguously

**Eligibility wording defect.** `armenia-tax-optimization.md:75` uses “medical/dental technology” and “construction/design documentation.” Current native [Article 267(5)(2)](https://www.arlis.am/hy/acts/215611/latest) separately excludes:

- medical care and services (`բժշկական օգնության և սպասարկման`);
- dental technology (`ատամնատեխնիկական`);
- construction works (`շինարարական աշխատանքներ`);
- preparation of architectural/construction design documentation (`ճարտարապետաշինարարական նախագծային փաստաթղթերի մշակման`).

Spell out all four. The compressed wording can be read as excluding only medical technology and construction documentation, leaving ordinary healthcare or construction outside the exclusion screen. Headline threshold/rate/carry arithmetic was otherwise reproduced in the tested branches; this finding concerns classification before arithmetic.

### 3. Individual personal refunds remain substantive ordinary work, although primary sources resolve much of it

**Ordinary-method omission.** `armenia-income-tax.md:128`, `:142–144`, `:237` and README IT-IND stop at identifying reimbursement, caps and applications as unimplemented. The displayed entrepreneur **23% statutory rate** and published field-88 discrepancy are correctly distinguished. Unverified live validation of that field is a filing limitation, not a reason to withhold the statutory method from a reference Guide.

The missing personal method has current primary sources:

- [Code 147.1/158](https://www.arlis.am/hy/acts/215611/latest): social-expense framework and signed annual declaration condition.
- [1067-N current annex](https://www.arlis.am/hy/acts/206432/latest): obligated declarant, noncash/direct payment and invoice identifiers, family evidence, approved service/provider tests, health/education categories and caps. Health cap AMD 50,000; education/overall cap AMD 100,000; textbook amount AMD 3,000 per pupil. Dental treatment is expressly a **2024/2025** branch, not automatically a 2026 category. The 2024 declaration reimbursement extension is separately stated. These are reimbursement limits, not deductions from salary.
- [956-N current annex 2–8](https://www.arlis.am/hy/acts/231590/latest), with [1411-N actual amendment](https://www.arlis.am/hy/acts/231583/latest): restrict eligible reimbursement to available PIT after the specified other PIT refunds; offset self-assessed annual PIT first; ordinary remaining refund enters the unified account and follows Code 327. Restricted-information employer cases have their own new form/payment path. This closes a genuine method gap; an invoice does not establish available PIT or cash refund.
- [Code 160](https://www.arlis.am/hy/acts/215611/latest) and [1321-N](https://www.arlis.am/hy/acts/200943/latest): mortgage population, loan/property/date/geographic/contract-value gates, quarterly cap, eligible paid salary PIT, lender/ACRA evidence, application and recovery rules. Use the borrower/co-borrower shared cap and actual loan date. It is a separate quarterly route.
- [Code 159(4)](https://www.arlis.am/hy/acts/215611/latest) and [1371-N](https://www.arlis.am/hy/acts/200942/latest): same-year reinvestment into the same resident payer, amount capped by relevant tax paid, current statutory disqualifications, and actual application/certificate/evidence route. This is not a generic tax-free dividend.

**Actual mortgage forms were independently located, fetched and all 12 PDF pages rendered/read**, rather than inferred from 1321-N's delegation. SRC's current index links [1274-L, incorporated by 30 July 2024 Order 940-L](https://www.src.am/storage/menu_contents_227/hr_hhpek_2021_1274l_66ab2c9012300.pdf). Detailed page map appears below. The remaining job is to implement and test these ordinary methods and their non-duplication bridge. No missing-source claim is justified for these instruments.

### 4. Payroll lacks ordinary gross entitlements, not merely a tested portal

**Ordinary-method omission.** `armenia-payroll.md:43`, `:58–71`, `:75–77` and README PR explicitly leave labour/leave/termination/statutory-benefit calculations outside the supplied net-pay formula. A fully taxable salary control does not compute the gross amount owed on ordinary leave, termination or sickness.

Current primary sources independently fetched/read:

- [Labour Code 159, 169, 170, 195, 129–130](https://www.arlis.am/hy/acts/51/latest): annual leave minima, leave pay from daily average × leave days, payment time, unused accrued leave on termination, current average-pay method and exclusions/fallback, severance by legal termination ground/service and final settlement. Current 195 uses **21/25** divisors for five-/six-day average daily pay; do not use an old 30.4 leave-pay text. Benefit-law calendar-day 30.4 is a different method.
- [Benefits Law 6, 8, 11, 22](https://www.arlis.am/hy/acts/205733/latest), actual [HO-73-N](https://www.arlis.am/hy/acts/205729/latest), [official clarification 1-2025](https://www.arlis.am/hy/acts/206406/latest), and [current 1024-N replacement procedure](https://www.arlis.am/hy/acts/196905/latest): current sickness/maternity calculation and authority/employer split, with the actual event-date transition. The current law supplies 80% sickness base, distinct caps/minimum, 30.4 calendar-day computation and multi-employer rules. For the post-transition ordinary sickness branch the first seven calendar days are employer-funded and later days state-funded. Do not transplant the old three/five-working-day split or assume the employer calculates every current state benefit.

The law is accessible. A source-based ordinary gross/benefit/withholding reconciliation is required before PR can be called complete. The full labour-law catalogue or every special occupation is not required merely to close this ordinary gap.

### 5. TP's ordinary implementing instruments exist and must be incorporated

**Ordinary local-document method omission; large-group branches need accurate routing.** `am-transfer-pricing.md:109–119`, `:227` and README TP describe prescribed implementation as unlocated/incomplete. Independent parsing of the fresh official [SRC legislation index](https://www.src.am/am/getMenusContents/222) located its actual file records. These are signed/stamped scanned orders, not merely search snippets. All **5 + 5 + 8 pages** were rendered and read:

| Instrument | Verified method details |
|---|---|
| [941-L, 9 September 2022](https://www.src.am/storage/menu_contents_227/hr_hhpekn_2022_941l_64647ea664962.pdf) | Annex 2 filer/PE scope; 3 local-file structure: taxpayer organisation/management, reporting lines/countries, business/strategy/restructurings/competitors; controlled agreements, related parties/residence, FAR, tested party/method/rejection reasons, comparables/search/adjustments, range, financial information and relevant APA/rulings. Annex 4–6: electronic delivery after written request in 30 working days, translation 10, additional info 10, interview details 5. |
| [942-L, 9 September 2022](https://www.src.am/storage/menu_contents_227/hr_hhpekn_2022_942l_64647ea6633b1.pdf) | Annex 2–3 expressly routes resident parent groups by **prior-year consolidated group revenue not exceeding / exceeding EUR 750m**, with the latter directed to CbCR. Annex 4 details organisation/geography, supply chains including >5% products/services, intragroup service/cost policies, markets/FAR/restructurings, intangibles, financing, consolidated accounts and APAs/rulings. Annex 5–7 gives electronic request delivery/translation/additional-info/interview clocks. Reconcile this implementing scope with the Code's parent/gross-income wording; do not silently use the short statutory list as the entire prescribed file or erase the statute. |
| [939-L, 9 September 2022](https://www.src.am/storage/menu_contents_227/hr_hhpekn_2022_939l_64647ea66105f.pdf) | Order 2 starts **1 January 2024**. Annex 2 includes resident reporting-parent/>EUR750m consolidated-revenue route and resident constituent notification of reporting entity by **31 December**. Annex 3: twelve-month report period. Annex 4–7: consolidated reporting currency, consistency/source explanation and correction, **electronic-only** delivery in Armenian/Russian/English. Annex 9–11 and Form 1: country aggregates, related/unrelated revenues, profit/loss, tax paid versus accrued, capital, retained earnings, average staff and tangible assets excluding cash; entity/activity list and explanatory table. |

Use an electronic delivery route that meets these implementing instructions while accurately quoting Code 376(3)'s paper-or-electronic statutory wording. The raw order-942 search extraction misleadingly suggested a draft; the actual scanned first page is a dated signed/stamped order. Current index availability is proven. No automatic-exchange arrangement, foreign surrogate filing, accepted report or professional approval has been proven.

The CbCR population is a large-group limit and should not by itself make the ordinary country domain partial. The unimplemented **local** file is ordinary for taxpayers over the controlled-transaction gate and is a real blocker. The actual source discovery makes the next task concrete rather than endless searching.

### 6. VAT late-export-proof settlement remains a precise conditional gap

**Unresolved ordinary export implementation.** `armenia-vat.md:164` and README VAT leave Armenian return-period mapping open. Fresh [Code 65/76](https://www.arlis.am/hy/acts/215611/latest) and [EAEU Treaty Annex 18(4)–(5)](https://www.arlis.am/hy/acts/202902/latest) were re-read. The treaty expressly gives 180 calendar days, shipment-period tax unless another national period is prescribed, later deduction/offset/refund under national procedure, and non-refund of already paid late penalties/fines. Code 76 establishes substantiation on the exporter's declaration submission date. The Guide correctly separates the missing buyer statement from a missing exporter declaration and cites the SRC explanation; missing buyer statement alone must not be converted into automatic domestic tax.

These provisions do not, by themselves, demonstrate the precise Armenian return fields/period for later restoration. Needed evidence is the applicable Armenian implementing return instruction or an authoritative ruling tying the late exporter-declaration event to the original/current period and recovery route. A specific legal derivation under Code 53–54/74/76 can also be presented and checked; it cannot simply be assumed from a generic correction rule. I have not established an alternative national period. I do **not** claim that no source exists.

Annual loss-norm VAT true-up is already present. It should not remain on a missing-method list merely because exhaustive commodity norms or a particular taxpayer's loss evidence are absent. Those are separate inputs/boundaries.

### 7. Cross-border personal and treaty settlement is still incomplete

**Ordinary integration work plus an unresolved procedure question.** `am-cross-border.md:145–176`, `:182–193`, `:261` and README XB openly stop at published historic treaty applications and a departure screen.

Current [Code 25/140–144/147/149–152/156/158](https://www.arlis.am/hy/acts/215611/latest) supplies much of the personal method: residence must be re-tested by year; domestic whole-year residence is not automatically split on departure; personal source is categorised under 144; tax-agent-exempt employer income has the specific monthly Article 151(2) route, while other no-agent annual income follows 151(3)/156. Integrate the actual source, asset exemption/base, agent and filing branches, with the current personal rate/form methods. A departure is not itself authority for a special invented filing deadline. Missing detailed specialist securities, pledged-property or developer cases need not block a properly bounded ordinary method.

The Guide's [01/29](https://www.arlis.am/hy/acts/20456/latest) and [01/13](https://www.arlis.am/hy/acts/20140/latest) pre-/post-withholding application map is not a verified current Code 19(7) Government-procedure integration or beneficiary refund settlement. Needed evidence is the operative Government procedure/continuation rule or authoritative modern SRC implementation, and the authorised applicant/account/approval-to-cash bridge. Code 327's available-account refund method is already in the corporate Guide, but it does not prove that a foreign recipient owns an Armenian agent's unified-account credit. No replacement instrument was established in this review; failed search is not proof of repeal or nonexistence. Treaty-rate tables and actual treaty/MLI entitlement remain separately scoped.

## Reclassification of declared gaps

| README reason | Independent disposition |
|---|---|
| IT-IND deductions/refunds | Real ordinary missing method. Current 1067-N/956-N/1321-N/1371-N and actual SRC1274-L supply substantial implementation. Write/test it; do not label it source-unavailable. |
| Personal/entrepreneur printed-form discrepancy | Current statutory workpaper controls and discrepancy is preserved. No live portal access is not independently a country-completeness blocker. It remains a pre-filing condition. |
| VAT late proof | Precisely unresolved conditional export settlement as above. No new evidence establishes a universal Armenian current-month or original-period restoration. |
| SC health calendar | **Not a missing controlling law.** Fresh current Health 46(11) explicitly states payer-status-month20. The template's statute-wins rule resolves priority over older leaflets. Preserve discrepancy for operations, but do not leave ordinary SC partial solely for that wording mismatch. |
| SC health erroneous/no-liability refund | Health 14(12) commencement depends on the Government implementing act. That act/commencement was not established. A Fund application now exists but has narrower evidential effect, explained below. Do not invent a universal refund method. This is distinct from computing ordinary contributions and the already supplied participant-excess route; assess it as a conditional exceptional-payment boundary, not automatically missing ordinary population coverage. |
| PR leave/termination/benefit | Real ordinary missing computations. Accessible Labour/Benefits/current1024-N primary sources resolve the framework; no live taxpayer login is needed to write the method. |
| TP detailed file/report | Actual941/942/939 now found and read. Local-file implementation is ordinary missing work. CbCR by itself is a large-group scope limit. |
| XB treaty/personal no-agent | Personal source/departure/period routing is largely method work using current Code. Treaty approval/settlement integration needs the stated authoritative evidence. |

The independent review is not accountant attestation. No actual taxpayer return/refund/certificate was submitted, and none is necessary to prove a published statutory method. A particular portal defect, final 31 December 2026 CBA input or taxpayer eligibility needs its own evidence. Exhaustive treaty-rate tables, special-sector relief, all commodity schedules, medical-benefit implementation, specialist financial restructurings and every litigation remedy are not automatically ordinary country blockers.

## Health erroneous-payment form scope

Independently fetched the Fund's [current documents listing](https://www.uhif.am/am/documents) and [mistaken-transfer application](https://vnxctzddivqjdrwwspgw.supabase.co/storage/v1/object/public/documents/official_docs/1788347293816_1775200508371_document.docx). Its complete rendered single page was inspected against the independently retrieved DOCX text. It asks the applicant identity/contact details, entity registration/representative documents where relevant, mistaken amount/reasons, bank/owned account, payment proof, signature and date. The statement specifically concerns money mistakenly transferred **to the Fund's account**.

It contains no Government decision number, 14(12) commencement, general Treasury/SRC refund procedure, decision clock or right to cancel later employer premiums. It does not prove that the specific deferred statutory branch is operative. The official [e-draft project10375](https://www.e-draft.am/ru/projects/10375/about) search preview concerns exactly the14(12)SRC/Fund procedure, but a proposed act cannot establish enactment. Direct retrieval returned403. That is a research limitation, not proof no act was later adopted.

The separate February2026 board participant-excess procedure was independently fetched; all five PDF pages were rendered/read. Its identity/application/registration/event-based clocks support the existing Guide's multiple-source excess route and do not cure the14(12)gap.

## Actual mortgage form map for implementation

Source: [SRC 1274-L incorporated by 940-L](https://www.src.am/storage/menu_contents_227/hr_hhpek_2021_1274l_66ab2c9012300.pdf), verified PDF pagination, **12 pages**. The current index publishes this incorporated version. This does not claim a live portal session or exclude an unlocated later amendment.

| Verified PDF page | Exact form or rule to map |
|---|---|
|1–2|Order/title/authority, actual incorporation by 30 July 2024 №940-L. Annexes 1–5; general commencement 1 January 2022, specified Annex 3 parts 15–17 from 1 July 2022. |
|3|**Annex 1/Form 1 entitlement application**: borrower full name, public-service number/absence-certificate number, identity-document series/number, TIN, Armenian residence and acquired/constructed property addresses; deceased-borrower identity fields where applicable; telephone/mobile/email, application date, actual loan date/number/lender and eligibility request statement, applicant signature/name. The starred deceased-borrower fields belong to the stated inheritance case. |
|4|**Annex 2/Form 2 quarterly refund request**: borrower identity/identifier/TIN and property; applicable deceased borrower; contact data; reporting year/quarter and loan contract date/number; bank and borrower-owned account; employer/agent TIN/name and paid PIT; consent to recover excess from later refunds; eligible paid interest, requested amount, calculated amount and actual returned amount. Do not confuse the initial entitlement application with this periodic request. |
|5|**Annex 3(1–4)**: scope including inherited rights; separate electronic request each reporting period through individual-accounts portal; first refund request after SRC confirms the entitlement application. The 15 working days describes SRC confirmation of that entitlement application, not a borrower refund-request deadline. The paragraph separately routes first use and changed paper-supplied data. |
|6|**Annex 3(5–11)**: repealed paragraph 5; portal registration/access route; request page; automatic identity/property fields; reporting period/loan selection; explicit consent to retrieve bank-account ownership information from CBA central registry. This is procedural evidence, not a tested portal login. |
|7|**Annex 3(12–14)**: automatic employer/TIN/paid PIT, lender interest information and calculated refund; reconcile available PIT, the borrower's/co-borrowers' prior refunds, consented excess recoveries and the statutory cap. Applicant may request less than the computed available amount; do not exceed computed amount. |
|8–9|**Annex 3(14–17)**: validation/rejection conditions include competing in-process request, tuition-refund overlap, missing account-information consent, absent/unpaid PIT, missing lender/ACRA data, unresolved excess, wrong account; later excess notices/recovery, corrected lender information and applicant notification. Annex 3's former Form 3 is expressly repealed by 1 April 2022 №358-L. |
|10|**Annex 4/Form 4 ACRA certificate**: loan date/number; borrower/co-borrower identity/PSN/TIN; reporting year/quarter; monthly scheduled/paid-interest amounts and payment dates; excludes subsidies and advance-paid amounts; totals/authorised signature. It is not an applicant-created substitute for lender/ACRA information. |
|11–12|**Annex 5 restricted-information payroll method/Form 5**: employer provides the prescribed identity/year/quarter/accrued-pay/PIT-paid and correction data through the permitted authority route. Keep this distinct from ordinary automatic payroll information. |

## Whole-pack findings and validation

| File | Review result at this SHA |
|---|---|
|README|Honest six-partial baseline; IT-CORP complete assertion must change or Article118 be supplied. Align overview's all-seven-partial wording with final evidence. |
|am-tax-overview|Main routing/headline-rate/year distinctions checked; stale all-seven-partial text differs from README's six. It is a map, not a missing tax computation by itself. |
|am-company-formation|Targeted registration/LLC provisions support the checked49-participant, one/two-working-day, 30-day, capital and 40-day/20-February statements. State-duty/e-identification/AML/accounts limits remain plainly bounded supporting-topic work. Do not call it a complete formation execution manual. |
|am-corporate-income-tax|Core bridge/loss calculations reproduce; ordinary management-services cap missing. Other stated specialist exclusions/portal issues remain distinct. |
|armenia-tax-optimization|Tested threshold/rate/reduction/transition methods broadly supported; correct the medical/construction exclusion wording. |
|armenia-income-tax|Tested 20%,category rates,rent excess and business23% distinctions supported; personal refund methods absent. |
|armenia-payroll|Salary controls reproduce; gross ordinary leave/termination/benefit entitlement method absent. |
|armenia-social-contributions|Tested pension/stamp/health formulas and major phase/deadline distinctions supported. Do not conflate delayed14(12)procedure with existing participant-excess refund. |
|armenia-vat|Tested 20%/16.67%/paid-only import arithmetic supported; late-export-proof restoration mapping remains unresolved. |
|am-transfer-pricing|Tested scope threshold/range arithmetic supported; actual local/master/CbCR implementation missing despite located instruments. |
|am-cross-border|Tested corporate no-PE rates/credit cap supported; ordinary personal integration/treaty approval-to-refund work remains. |

**Arithmetic and preservation evidence:**

- `scripts/check-examples.py skills/international/armenia/*.md`: **11 files, 14 blocks, 0 failures, 0 missing**.
- Independently written `independent_recompute.py`: **14 core cases + one additional boundary/cap group,0failures**. Full actual/expected values in `independent-arithmetic.json`.
- Core results: CIT4,410,000tax/1,410,000balance; prior2023loss4,000,000remaining; royalty1,000,000tax/9,000,000net; foreigncredit5,400,000/Armenianbalance3,600,000; salaryPIT200,000; rentextra1,200,000/total8,400,000; payrollnet219,200and186,500/181,700; pension15,000/35,000; healthfunding10,800; VAT200,000payable and2,200,000import; CUP20,000,000difference; quartiles3.5%/7.5%,median5.5%,profitdifference3,500,000.
- Supplementary checker: **67 blocks, 0 failures, 0 missing**. These include retained controls and later research probes; they do not make a missing method complete.
- Independent preservation check: **all 18 embedded original-candidate files exactly match their original Git blobs at df7247a47d4e9ef0aa961165bad1c09e10f9e4f7**; all 51 original oa-check blocks remain **byte-identical** in the current Guides/supplement. All 8 main-baseline files match the stored original bytes; protected platform fields and CTA suffixes remain intact. See `preservation-independent.json` and `example-byte-preservation-independent.json`.
- Current 11 snapshot files were re-compared to `git show 8be41f35:path`: exact bytes still match. See `reviewed-files.json` for hashes and headings.
- `validate-guides.py --no-index-check` passes using existing read-only PyYAML dependency path, with repository-wide warning groups:810 missing Sources, 5 stale, 5 jurisdiction warnings. The archive has no Git metadata, so the validator explicitly skipped its two US-federal deletion checks (origin/main…HEAD and working tree versus HEAD); this is not a Git deletion clearance. Armenia preservation was checked independently as described above. Initial local run lacked PyYAML; rerun succeeded. Initial example invocation incorrectly passed a directory; corrected glob succeeded. Neither initial invocation error is a candidate defect.
- Coverage report at this SHA: **AM 10 Guides, reviewed 0, IT-CORP present, IT-IND/VAT/SC/PR/TP/XB missing through partial, complete: false**. The newly found Article 118 gap means the one-present corporate claim also needs correction or completion.

## Source receipts and review boundary

Raw independently retrieved bytes and extracted text are under `review-sources/`; HTTP receipts include URL, finalURL, UTCtime, byte count and SHA256. `review-sources/RETRIEVAL-RECEIPTS.json` is the clean consolidated set; names accidentally captured with a trailing quote by the first extraction regex were discarded as extraction artefacts, not reported as broken citations. No writer research conclusion or prior pass/failure was used as legal authority. Embedded historical JSON was used only to verify preservation against actual Git objects.

Material native law re-read includes Code 20, 63, 76, 113–123 (including omitted 118), 125, 135, 144–145, 147.1, 150–152, 156/158–160, 254/258/264/267/272, 362–364/376, 401/402/402.1/402.2; targeted current 749-N scope/sign/rate/credit instructions; Pension 5–6 and Stamp 12/HO-477 commencement; Health 14/45–46; Treaty Annex 18(4)–(5); the labour/refund instruments identified above. Actual941/942/939,healthboardAnnex6,and1274-L were visually read in full after rendering. Retrieval alone is not represented as reading every line of every linked statute or as clearance of all specialist branches.

This review **fails readiness**, rather than asserting universal correctness of the unfinished pack. Required substantive closure is: corporate Article 118; precise micro exclusions; ordinary personal refund computation/forms/settlement; ordinary payroll gross entitlements/benefits; ordinary TP local-file implementation; ordinary personal cross-border/no-agent integration; and evidence-backed resolution or a clearly justified bounded treatment of late EAEU proof and treaty approval/refund integration. Health calendar priority is already resolved by statute; the separate 14(12) commencement remains unproved and must stay accurately bounded. Named accountant attestation and live taxpayer access are separate from these source/method requirements.
