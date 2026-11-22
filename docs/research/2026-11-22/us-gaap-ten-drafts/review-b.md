# Independent review B: five new US GAAP publication-held drafts

Reviewer: independent Codex reader, 22 November 2026. Scope: ASC 330 inventory, ASC 360 fixed assets/impairment, ASC 350 goodwill/intangibles, ASC 810 consolidation, ASC 230 cash flows. I did not write these Guides. I read their complete bodies, source tables and writer ledgers; the applicable firm instructions, repository CLAUDE.md, docs/skill-template.md and docs/domains.yml; and the original FASB passages identified below. I made no Guide edits, commits or pushes.

## Conclusion and limits

The five files are legitimate **publication-held research drafts**, not complete current-ASC Guides. Retain `status: needs_sources`, tier 2 and every individual non-usable hold. The named amendment-basis propositions are supported after the four narrow findings below were corrected and re-read; all four are closed in the final bound files. Ten worked cases, all 44 hypothetical block inputs and all 38 named expected block outputs were independently checked; every calculation matches. Additional prose comparisons are separately recomputed below. This is a complete review of the assigned limited draft content; **current-ASC completeness has not been reviewed or cleared**, because the missing current authoritative text is expressly outside the recovered evidence.

The fixed-assets historical FAS 144 comparison is effectively held: the Scope, method step 4, example introduction, example conclusion, refusal section and Sources all prohibit its use as current ASC 360 authority or a booking instruction. Historical arithmetic is correct. The neighboring depreciation sentence has now also been made conditional (finding B3, closed).

No inherited accountant approval is created. The working tree showed only ten new Guide additions, with no edit/deletion to the four pre-existing US GAAP Guides; their existing bodies, names and approvals are outside this review and preserved. No full standards capture or render should enter the public repository.

## Objective findings and exact fixes

**B1: ASC 360 effective-date boundary (wrong in initial draft; correction requested).** The initial `effective_date: 2014-12-16` and Scope explanation used periods beginning *after* 15 December 2014. [ASU 2014-08](https://storage.fasb.org/ASU%202014-08.pdf), 205-20-65-1(a)–(b), printed pp.46–47, uses annual periods beginning **on or after** 15 December 2014. Set `effective_date: 2014-12-15` and say “annual periods beginning on or after 15 December 2014.” Preserve the distinction between PBEs/qualifying securities-issuing NFPs and all other entities' interims (on or after 15 December 2015), the prospective transaction conditions, pre-effective held-for-sale exclusion and limited early adoption. The existing wording “entity/interim and transaction transition conditions must be checked” holds those details rather than claiming all ASC 360 became effective then. The coordinating writer reported the narrow date correction during review; final closure is bound below.

**B2: ASC 360 later-amendment locator (wrong in initial draft; correction requested).** The removal of obsolete 360-10-40-2 is **Issue 8**, ASU 2025-12 paragraphs 30–31, printed p.37, not Issue 11 (which corrects a repurchase-option example). Replace “issue 11” with “Issue 8” in the body citation, Sources read-scope cell and ledger. The substantive removal statement is correct; 105-10-65-10 is the correct transition reference. [ASU 2025-12](https://storage.fasb.org/ASU%202025-12.pdf). The writer reported the narrow locator correction during review.

**B3: ASC 360 depreciation instruction leaks beyond the held source scope (unverified, not found wrong).** Step 2 originally said “Do not stop depreciation because an asset is merely idle or management wishes to sell it.” Reproduced 360-10-45-15 establishes held-and-used classification for nonsale disposal; it refers to the held-and-used measurement sections without reproducing the operative depreciation cessation rules. The Guide expressly holds those current rules. Replace with “Do not infer a depreciation cessation from idle status or sale intention; obtain the held current depreciation and held-for-sale rules before deciding.” This keeps the evidence warning without purporting to clear an unsourced policy. No finding that continued depreciation is substantively wrong is made. [ASU 2014-08](https://storage.fasb.org/ASU%202014-08.pdf), 360-10-45-15, printed p.38.

**B4: ASC 810 acquisition-date equality and early-adoption condition (wrong/incomplete initial boundary).** Scope initially said prospective to acquisitions “after initial application.” The operative 805-10-65-5(c) includes acquisition dates **on or after the date of initial application**. The summary itself says “after”; use the operative paragraph to resolve that difference. Also place the not-yet-issued/made-available condition next to the early-adoption statement. Replacement: “Early adoption is permitted in an interim or annual reporting period for which financial statements have not yet been issued or made available for issuance; interim adoption may apply from the beginning of that interim period or the containing annual period. Application is prospective to business combinations with acquisition dates on or after the date of initial application.” [ASU 2025-03](https://storage.fasb.org/ASU%202025-03.pdf), 805-10-65-5(a)–(c), printed p.8. The 15 December 2026 boundary itself is correct.

No other wrong substantive proposition or calculation was found within the expressly limited amendment-basis scope. Current-source gaps below remain unresolved, rather than being silently counted as verified GAAP.

## Method and source provenance

The initial manifest's “downloaded; not yet read” flags were treated as download history only. I independently read the retained operative passages and adjacent conditions. All eleven PDF byte hashes match their successful manifest entries; fresh `pdftotext -layout` output matches each retained `.txt` byte-for-byte. The initially failed ASU 2017-04 URL is not the successful source: its successful alternate official URL and hash are in supplemental-manifest.json. ASU 2021-03 and FAS 144 are in additional-manifest.json. Provenance and readable retained originals did not fail, so no re-fetch was needed. No secondary source, CAPTCHA solution or terms acceptance was used.

Read scope (not a claim to have read every page of each standard):

| Retained official source | Original passages and adjacent conditions independently read |
|---|---|
| ASU 2015-11 | Summary, NRV glossary, 330-10-35-1A–35-11 and preceding/superseded redlines, 330-10-65-1; adjacent 330-10-50-2/55-2 and 270-10-45-6 seen to avoid importing a blanket interim/reversal conclusion. |
| ASU 2014-08 | 360-10-45-3/5/9/11/14/15; 205-20-65-1(a)–(d); relevant summary. All six held-for-sale criteria and every one-year exception branch read. |
| Historical FAS 144 | Paragraphs 7–10, physical PDF pp.9–10, including recognition versus measurement, recoverability date, trigger examples, estimate/method sequencing and independent-cash-flow grouping. Paragraph 11 adjacent context seen; no current authority assigned. |
| ASU 2025-12 | Issue 8 paragraphs 30–31 / 360-10-40-2 removal and history; Issue 11 inspected to resolve erroneous locator; 105-10-65-10(a)–(f), including annual-beginning interim adoption and individual transition-election categories. |
| ASU 2017-04 | 350-20-35-1–35-8B, 35-12/13, 35-28–30; adjacent qualitative factors and removed step-two text distinguished. |
| ASU 2021-03 | 350-20-05-4A–05-6; 15-3A–15-6; 35-62–35-67,35-79 and adjacent 35-81/83–86; 65-2–65-4. The corrected general-test date and separate trigger-alternative date are not conflated. |
| ASU 2015-02 | 810-10-15-8/8A/10; 15-13–15-14, including every equity-risk, power, expected-loss/return and disproportionate-voting subcondition; 25-38–25-38C and adjacent context. No full later related-party review claimed. |
| ASU 2018-17 | 810-10-15-17AC–17AF, including four cumulative conditions, all-eligible-entities election, continued other guidance, disclosure exception and consequence of ceasing eligibility/PBE change. |
| ASU 2025-03 | Summary scope; 805-10-25-1/4/5; 55-10–55-15 factors; 65-5(a)–(c). Legal-acquiree business limitation checked against summary and operative amendment. |
| ASU 2016-15 | Issue 1/2 descriptions; 230-10-45-13/15/17/25; 50-4 and ASC 842 pending-content version; 45-22/22A and transition 65-2. Repeated paragraphs in separate issues do not override cumulative amendments. |
| ASU 2016-18 | 230-10-45-4/5/24;50-7/8;55-12A/13 illustrations;65-3; adjacent 830-230-45-1 exchange-rate reconciliation. |

Visual redline review: rendered and inspected physical PDF pages 12 of ASU 2015-11;44 of ASU 2014-08;12/14 of ASU 2017-04;20 of ASU 2021-03;9/10 of ASU 2025-03;32/33 of ASU 2016-15;17 of ASU 2016-18. These confirm added versus deleted grouping language, separate held-for-sale presentation, removal of implied-goodwill step two, corrected adoption dates, VIE-acquirer exception and specific-guidance/components-before-predominance ordering. Local renders: `reviews/visual-b/`.

## Consequential rule and condition inventory

“Checked/match” means matched to the named historical amendment passage, **not** independently cleared as complete current ASC. “Checked/workflow” identifies evidence gathering, arithmetic sequencing or referral instructions, without inventing an external GAAP rule. “Unverified/held” means non-usable pending current authority. Grouped rows enumerate their complete consequential conditions; they are not a fabricated legal-figure count.

Common to all five: general-reference notice; tier2/no accountant approval; current-ASC/publication prohibition; source-linked working paper/proposed entries/disclosure checklist/reviewer brief; no issued statements/opinion/return; assumptions separated; all six intake bullets in each Guide; return/reconcile/refer instructions. **Checked/workflow**: complete text read, no conflict with limited research scope. The held source lists are controlling. Descriptions, standard labels, jurisdiction US, financial-reporting domain, computation shape, dependency, v0.1 and source read dates were checked for agreement with each body. The 2026-11-21/22 read dates describe the writer's stated passage reads, not an independently observable timestamp of their reading. I independently read on 2026-11-22.

### ASC 330

| ID | Assertion/condition inventory | Source and disposition |
|---|---|---|
| I1 | ASU2015-11 fiscal years after15Dec2016; PBE interims within those years; other-entity interims after15Dec2017; prospective; early interim/annual beginning; 2016-12-16 first possible start | 330-10-65-1(a)–(d): checked/match. Existing below-cost amount is cost at adoption under(c); Guide does not purport to clear general reversal rules. |
| I2 | Quantity/ownership/cutoff/cost evidence first; approved cost-method recomputation; cost inclusion/idle capacity/waste not decided by this amendment | Checked/workflow and explicit hold; no invented capitalization rule. |
| I3 | Non-LIFO/nonretail including FIFO/average: lower cost/NRV; loss in earnings in period evidence exists; LIFO/retail separate market branch | 330-10-35-1A/B/C: checked/match; not blanket FIFO formula for market. |
| I4 | Ordinary-course selling estimate less reasonably predictable completion, disposal, transportation; positive cost excess only; item-level examples assume exceptions cleared | Glossary NRV;35-1B: checked/match. |
| I5 | Item/total/major-category selection based on character/composition and periodic income; year consistency; balanced component quantities; excess components/unrelated products/turnover differences; no concealment by arbitrary offset | 35-8–35-11: checked/match. Guide does not ban every category method. |
| I6 | Market reflects utility; replacement-cost exceptions/firm sales/recoverability; no automatic write-down for sustained operating loss; hedge basis adjustment separate; ceiling/floor/full exceptions held | 35-3–35-7A: checked/match for stated limited rules; remaining market definition unverified/held. |
| I7 | Conditional Dr loss/expense Cr inventory/valuation; gross-to-net bridge; shortages/cost errors/value decline separate; no uplift above cost merely because NRV higher | Checked/workflow/conditional entry; lower-of-cost rule supports no uplift. Specific expense caption/new basis/reversals/full disclosure: unverified/held. |
| I8 | Complete current scope/initial cost, overhead/capacity/waste, cost-flow changes, LIFO/retail ceiling/floor/exceptions, annual/interim reversals/new basis, full disclosures/later amendments | Unverified/held, expressly non-usable. No completeness approval. |

### ASC 360

| ID | Assertion/condition inventory | Source and disposition |
|---|---|---|
| D1 | ASU2014-08 date boundary, entity/interim and transaction transition; no all-ASC360 effective-date claim | 205-20-65-1(a)–(d): initially wrong boundary B1; remaining detailed conditions expressly to be checked, not cleared. |
| D2 | Register cost/additions/disposals; accumulated depreciation/impairment/net carrying bridge; approved date/life/residual/method recomputation does not prove compliant policy | Checked/workflow, conditional arithmetic. |
| D3 | Nonsale/abandonment held-used until disposal; idle/desire-to-sell does not itself establish sale classification; depreciation consequence separately source-held | 360-10-45-15: classification checked/match. Positive depreciation instruction originally unverified, B3. |
| D4 | All six sale criteria: authorized committed plan, present immediate availability/usual terms, active buyer/completion program, probable completed sale within1year, reasonable price relative to current fair value, unlikely significant change/withdrawal | 45-9(a)–(f): checked/match. Listing alone insufficient. “Reasonable active marketing price” is read with source's fair-value condition; no price safe harbour. |
| D5 | One-year delay only specified conditions: expected nonbuyer conditions needing firm commitment first/probable commitment within1year; unexpected conditions after firm commitment/timely response/favorable resolution; previously unlikely circumstances within initial year/responsive actions/reasonable revised price/all45-9 criteria | 45-11(a)–(c): checked/match to warning to use actual specified conditions; Guide does not invent general extension. |
| D6 | Historical undiscounted recoverability gate, fair-value loss; independent-flow grouping; not current GAAP booking instruction | FAS144¶7–10: checked/match strictly historical; current model unverified/held. |
| D7 | Nondiscontinued sale gains/losses in continuing income before tax, included operating subtotal if shown; disposal-group assets/liabilities separately/no offset; ASC205-20 separate eligibility | 45-5/14: checked/match; current eligibility unverified/held. |
| D8 | ASU2025-12 removes obsolete40-2, no new general disposal permission; annual years after15Dec2026/interims; early adoption/transition options | Issue8¶30–31;105-10-65-10: substance checked/match; initial issue locator wrong B2. Transition options explicitly refer to operative text rather than asserting unconditional early adoption. |
| D9 | Current initial cost/depreciation/life-residual revisions; held-used impairment/groups/cash flow/allocation/reversals; held-sale measurement/depreciation; disposal recognition/full disclosures; ASC205-20 eligibility | Unverified/held. Historical source cannot clear any of these. |

### ASC 350

| ID | Assertion/condition inventory | Source and disposition |
|---|---|---|
| G1 | General-test periods after15Dec2019 for SEC-filer PBEs excluding SRC-eligible; one-time SRC eligibility most recent determination15Nov2019; all others after15Dec2022; prospective; early tests measurement on/after1Jan2017 | 2021-03 350-20-65-3(a)–(c): checked/match; 2022-12-16 date key valid. Not confused with trigger-alternative65-4 dates. |
| G2 | Subsequent goodwill versus acquisition allocation/software/other intangibles; general recognized goodwill not amortized, annual/interim tests; private-company/NFP alternatives separate and neither compulsory/preclusive of other | 2017-04 35-1/28/30;2021-03 15-4–15-6: checked/match; scope/eligibility/full election requirements retained. |
| G3 | Optional qualitative more-likely-than-not is above50%; unconditional bypass to quantitative; carrying including goodwill versus unit fair value; cap allocated goodwill; implied-goodwill step2 removed | 2017-04 35-3A/B,35-4–35-8/removed35-9–11: checked/match. No assertion that single qualitative event forces test. |
| G4 | Tax-deductible goodwill changes deferred tax/carrying amount; associated calculation required and capped; adjusted goodwill new basis; no later reversal | 2017-04 35-8B,35-12/13: checked/match. Actual computation unverified/held; case excludes tax effect. |
| G5 | Elected amortizable goodwill unit: straight-line10years or justified shorter; existing/future relevant goodwill; all related requirements; elected entity/reporting-unit test; trigger-end election does not eliminate triggered test | 2021-03 15-5/6;35-63/65/66 and adjacent35-83–86: checked/match. No general annual-test exemption assigned to nonamortizing branch. |
| G6 | Alternative-guidance simultaneous other-asset/group test first, recognize loss before goodwill; no borrowing goodwill cap/election for brand/patent/customer asset | 35-79: checked/match for expressed branch; other intangible rules held. |
| G7 | Rollforward/assumption/source/disclosure list; internally generated goodwill development/maintenance/restoration not capitalized | Checked/workflow;05-4A: checked/match for goodwill costs only. |
| G8 | Complete current ASC350/later amendments; reporting-unit allocation/valuation/disclosures; tax calculation; finite/indefinite initial recognition/life/amortization/impairment; alternative eligibility/transition beyond read passages | Unverified/held. Failed2014-02/2012-02 downloads not falsely credited. |

### ASC 810

| ID | Assertion/condition inventory | Source and disposition |
|---|---|---|
| C1 | 2025-03 annual periods after15Dec2026/interims; early interim/annual beginning; prospective initial application boundary | 805-10-65-5(a)–(c): date checked/match, initial equality/issuance-condition defect B4. |
| C2 | Entity-by-entity scope/exceptions; majority >50% usual pointer except LPs; contract lesser interest/control restrictions can change result; LP substantive-rights branch | 2015-02 810-10-15-8/8A/10: checked/match. Not unqualified majority=control. |
| C3 | VIE separate status test: insufficient qualifying equity at risk; equity group lacking power/loss obligation/residual right; disproportionate vote AND substantially-all-activity conditions; substantive terms/purpose/design | 15-13A/B–15-14: checked/match as high-level inventory plus requirement to document whole test. Full definitions/exceptions held; no capital-ratio shortcut. |
| C4 | Primary beneficiary BOTH power over most significant activities and potentially significant losses OR benefits; design/related parties/substantive rights; exposure alone no fixed percent | 25-38–38C: checked/match for read amendment; all later related-party refinements held. |
| C5 | Private alternative all4conditions: common control; neither common-controlled by PBE; legal entity notPBE; no general-subsection controlling interest; all eligible entities election; continued other guidance/disclosures; parent's direct/indirect votes only for specified common-control test | 2018-17 15-17AD–AF: checked/match. No exemption for genuinely general-model controlled subsidiary; eligibility loss/PBE change not cleared beyond source/referral. |
| C6 | Adopted2025-03 branch: primarily equity exchange, legal acquiree VIE and business; 805 factors replace always-primary-beneficiary accounting-acquirer outcome; not asset-acquisition rule | 2025-03 Summary;25-5;55-10–15: checked/match; legal/accounting identities separate from consolidation. |
| C7 | Conditional full-TB/acquisition/policy/intercompany/unrealized profit/NCI worksheets; do not merely multiply assets by ownership; supplied eliminations not current-rule clearance; combined versus consolidated distinction | Checked/workflow, explicitly conditional, no asserted complete mechanics. |
| C8 | Current scope/exceptions/variable-interest definitions/related-party-fee refinements; full control/NCI/elimination/deconsolidation/disclosures/later applicability | Unverified/held. Neither worksheet gives posting authority. |

### ASC 230

| ID | Assertion/condition inventory | Source and disposition |
|---|---|---|
| F1 |2016-18 nonPBE years after15Dec2018/interims after15Dec2019; PBE after15Dec2017/interims; retrospective; early interim adoption adjusts from annual beginning; date2018-12-16 | 230-10-65-3: checked/match. 2016-15 dates independently checked to65-2, same main dates with its impracticability exception/all-content early-adoption condition; Guide does not state a conflicting adoption method. |
| F2 | Reconcile cash/cash equivalents/restricted cash-equivalent totals; several balance-sheet lines require face/note disaggregation summing to total; explain restrictions; no new boundary definition | 2016-18 45-4/24;50-7/8: checked/match; definitions held. |
| F3 | Transfers inside perimeter excluded from operating/investing/financing; noncash investing/financing outside cash totals, separate disclosure work; debt-to-equity and asset for directly related liability examples | 45-5;2016-15 50-4: examples/transfer rule checked/match. Complete noncash disclosure requirements held; separate-disclosure preparation is a workflow deliverable. |
| F4 | Operating suppliers/employees/tax/interest; direct classes customer/ordinary interest-dividend receipts subject special exceptions; productive-asset purchase investing including capitalized interest; seller debt principal financing; borrowing principal/debt issue/extinguishment qualifying costs financing | 2016-15 45-13(c),15,17,25: checked/match as limited ordinary transactions, not ledger-caption classification. |
| F5 | Direct actual receipts/payments; indirect income plus noncash/investing-financing effects; operating movements excluding acquisition/disposal/noncash/FX; gains removed while full disposal proceeds investing | 2016-18 55-13 illustration: checked/match for illustrated depreciation/gain/acquisition-adjusted movements; broader transaction-analysis caveat checked/workflow, not claimed complete current indirect guidance. |
| F6 | Directly related debt premium/third-party/extinguishment costs financing except accrued interest; zero/insignificant coupon accretion operating and principal financing; no split of discount accretion for every debt | 2016-15 Issue1/2;45-15(g)/(b),17(d): checked/match. Ordinary settlement example excludes special instrument branch. |
| F7 | O+I+F plus separate supported FX reconciles perimeter; mixed flows specific guidance first, separately identifiable sources/uses by nature, predominance only when inseparable | 2016-18 45-24/830-230-45-1;2016-15 45-22/22A: checked/match; suspense/evidence trace is workflow. |
| F8 | Complete current ASC230; cash/restricted definitions/policies; gross/net exceptions; specialized classifications; complete direct/indirect disclosures/later amendments; proposed change not enacted | Unverified/held. Referrals for factoring, consideration, derivatives, insurance, leases and exceptions consistent with limited scope. |

## Independent example inventory and recomputation

Every input below is explicitly hypothetical/assumed. “Match” certifies arithmetic and the stated historical/amendment-basis branch only. It does not clear actual entity policy, scope, adoption, valuation, current source or posting.

| Case | Complete input inventory | Independently recomputed outputs and additional prose boundaries | Disposition |
|---|---|---|---|
| Inventory NRV | units100; cost20/unit; selling19; completion1; disposal0.50; transportation0.50 | Unit NRV19−1−.5−.5=17; total cost100×20=2,000; NRV100×17=1,700; min=1,700; loss300. Selling-only loss2,000−1,900=100, so misses200 of300. | Checked/match all5block outputs and prose comparison. Assumes item FIFO/average, no exception. |
| Inventory separate products | costA1,000;NRVA700;costB1,000;NRVB1,400 | A700;B1,000;total1,700;loss300; pooledNRV700+1,400=2,100 exceeds pooled cost2,000 and could hide loss under expressly assumed individual grouping. No B gain400 booked. | Checked/match all4outputs and prose. Not universal category ban. |
| Fixed-asset depreciation | cost60,000;residual6,000;life5years;inservice6months; straight-line/no impairment assumed | Depreciable54,000;annual10,800;6/12 depreciation5,400;closing54,600; equal Dr/Cr5,400. | Checked/match all4outputs/prose/entry balance; policy itself held. |
| Historical impairment | carrying100,000; first undiscounted110,000; second90,000; fair value80,000 | First headroom10,000; fair-value gap20,000 alone insufficient gate, historical loss0 in first scenario; second recoverability shortfall10,000; measured historical loss100,000−80,000=20,000. | Checked/match all3block outputs and both prose cases, including first no-loss outcome. No current journal. |
| General goodwill cap | unitcarrying300,000 inclgoodwill40,000;unitFV250,000; no tax effect/prior tests assumed | Positive excess50,000;min(50,000,40,000)=40,000;goodwill0;unit residual deficit10,000 after goodwill loss not another goodwill write-down; Dr/Cr40,000. | Checked/match all3outputs/prose/entry. |
| Goodwill amortization election | goodwill200,000;life10years;elapsed6months;eligible/elected/no impairment assumed | Annual20,000;half-year10,000;closing190,000; Dr/Cr10,000; general nonamortizing branch would not amortize merely for passage of time. | Checked/match all3outputs/prose/entry, election condition explicit. |
| Conditional group assets | parent500,000;sub250,000;investmentelimination100,000;receivableelimination20,000; companion eliminations assumed | Combined750,000;eliminations120,000;conditionalassets630,000. All ownership/measurement/NCI instructions supplied, not inferred. | Checked/match all3outputs; not a complete balanced statement/acquisition illustration. |
| Conditional inventory profit | sale50,000;sellercost35,000;retainedfraction40%=.4; reviewer elimination instruction assumed | Profit15,000;retained15,000×.4=6,000;outside-sale fraction0 gives0; tax/NCI not silently assumed zero. | Checked/match all3outputs/prose, accounting fraction/treatment held. |
| Direct cash/restricted bridge | customer120,000;supplieremployee80,000;interest5,000;tax10,000;cashPPE20,000;principal3,000;openingcash7,000/restricted3,000;closingcash7,000/restricted5,000; no FX/special exceptions assumed | Operating25,000;investing−20,000;financing−3,000;net2,000;openingtotal10,000;closingtotal12,000;difference0. Internal restricted transfer2,000 not additional outflow (otherwise false net0). | Checked/match all7outputs and prose transfer. |
| Ordinary debt settlement | principal50,000;directpremium3,000;accruedinterest2,000;noothercomponent | Financingoutflow53,000;operating2,000;total55,000. All-financing55,000 misclassifies2,000; adding premium to operating again would double count3,000. | Checked/match all3outputs/prose. Excludes zero/insignificantcoupon accretion branch. |

There are exactly ten `oa-check` blocks across these five Guides, with 44 input entries and 38 named expected output entries. Those totals describe the enumerated blocks, not independently countable legal propositions. The paragraph-level workflow and hold inventory above is exhaustive for substantive body assertions; no sampling is represented as full review.

## Required remaining work

Before current publication, obtain lawful readable current authoritative Codification access and clear each Guide's individually listed current-source gaps, including intervening amendments and operative scope/transition. The access failure itself is not an instruction to solve a CAPTCHA. Retain the holds until that substantive work is completed; this report must not be used to remove `needs_sources` or claim accountant approval. No further research from Michael is required for the narrow objective fixes above.

The initial writer ledgers grouped entire methods into a single row and sometimes used nonoperative fragments (“Not for redistribution”; introductory authority statement). During closure the writer regenerated them with operative fragments, corrected the ASC360 locator, and rebound all five hashes. I checked the replacement historical undiscounted-cash-flow fragment and common-control alternative fragment against the original passages and confirmed each final ledger hash matches its Guide. Grouping remains an index convention, not a count of independent legal figures. This report supplies the complete independent rule/condition inventory.

## Closure and final hash binding

After the writer's narrow corrections I re-read the affected final frontmatter, ASC360 Scope, step2 and later-amendment/Sources locator, plus ASC810 Scope, against the unchanged original passages. **B1–B4 are closed**: ASC360 date now2014-12-15/on-or-after; ASU2025-12 locator nowIssue8; depreciation cessation now a held-rule decision; ASC810 early-adoption issuance condition and on-or-after acquisition-date boundary now explicit. Full current-source holds remain unchanged. Metadata `last_updated: 2026-11-22` is now present; title punctuation changes do not alter rules. No full repeat review of unchanged passages was needed.

The following SHA-256 values bind the reviewed final files. Body hash means the exact UTF-8 bytes following the second YAML `---` delimiter (including its following newline), so metadata-only changes can be distinguished from body changes.

| Guide slug | Whole file SHA-256 | Body SHA-256 |
|---|---|---|
| us-gaap-asc330-inventory | `219b8c102c41b754dd770a832a863810c634d39cbd6071dcbb9f9340de3bc969` | `f893370379d00f66f59bbafc92ca70a4fb6fcf030f18cea4b0b12f552a305877` |
| us-gaap-asc360-fixed-assets-and-impairment | `0bd13ed7d572ff8144ead8029c9b218edd975586e797cf15a9b008ebc2dee377` | `e9ef254153dfe481844bbed35270fb854b315c57cd834adf1621a2a7d7b191a9` |
| us-gaap-asc350-goodwill-and-intangibles | `d008abb598b6dc38d38b46c9780f4f4a6eab76c940c65d359febfa464ebaf3dc` | `34a6727aeae913cd61d8a6c2a20b799af6ec97215e9949008bcf6dc38487a81d` |
| us-gaap-asc810-consolidation | `9428f4fce34197c43c4fa7630bea50e12b3f1f85cb01872fe7164a7603ea6439` | `c74ae3c71811609083998aaf7f767717ad347237f351c8f1024ad087e820b119` |
| us-gaap-asc230-cash-flow-statement | `86b1393566140af499d2d8270b474541dd1826044e826d1c1582f1411c510edf` | `090997395e74df33b0b1ed1ed335e24eaaa82487da8d5f01ee01ecdcbc12f6e3` |

| Retained original PDF | SHA-256 (matches successful official-source manifest) |
|---|---|
| asu-2015-11.pdf | `58a30af19513f3960738acf00e2b46b03675eb88df495ad4816f1c1ceb220f88` |
| asu-2014-08.pdf | `3cb13caf42f351f98255d12148768e909ac310d88b472442361316e5887b0c27` |
| fas144.pdf | `46f968b6901be476533689bd92f551bdb86ecf27f1d30f9e83bfa7ee7f7ed78a` |
| asu-2025-12.pdf | `f0298e50cfa9b433741363bda0e7af8df900dc543c1018d8ce15b26addab35ea` |
| asu-2017-04.pdf | `e2ee3d7f5672615190b8e14719576e110e4ad77f40fec4043b03fe387177f648` |
| asu-2021-03.pdf | `0146c002f1d24a34689e3f15f47303c27252601249f289026bcdcb3ac8201a4e` |
| asu-2015-02.pdf | `5bcfb726a1afcc4fd766233b6d91d3dac844c59f17a0c2cd8d12d06f25b6e203` |
| asu-2018-17.pdf | `a1b88856ec821293a8a9d03d903cec4b7fcd62d1032c9e0bd7f3487521360073` |
| asu-2025-03.pdf | `bfae7eb1a6b25e9e45d32265d29ad5809082f63a06dd3081124aedf1729cd837` |
| asu-2016-15.pdf | `6508b9ee54086a8426e5d87cb4d1ab4cc91c59b8135fa77845e78291d47ed4fd` |
| asu-2016-18.pdf | `56db5b47cdc0d741f8420273d59e6effe90d19bd4e66f70219a3337fe2ada71c` |

Review coverage status: **complete for all five assigned draft bodies, all consequential stated amendment-basis rules/conditions/date boundaries, all ten prose/block cases, and the explicitly historical comparison**. No current-ASC completeness clearance, accountant attestation, publication or production delivery is represented. The only unresolved substantive tasks are the already documented current-source holds. Final ledger rebinding and the operative-fragment corrections were checked and completed; those holds are not unperformed checks disguised as passes.
