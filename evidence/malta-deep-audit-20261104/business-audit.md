# Malta business/company audit, 4 November 2026

Read-only audit of public repository commit ab692cc2ef1c6306de9435b63448294d30fc4052. No Guide, metadata, commit or PR changed. Eleven assigned Guides read; fresh official sources fetched with web tool. This is a substantive audit report, not professional attestation and not a claim every proposition in 2,752 lines is verified. Scope limitations below are intentional.

## Findings requiring correction or a publication hold

### B1 [P1, confirmed conflict with regulator guidance] Companies Act size thresholds use the wrong commencement test

`skills/malta/malta-financial-statements.md:75`: “accounts for balance sheet dates on or after 20 March 2026 are tested against the new limits”. Lines 76, 194–200, 223 and the completion checklist propagate uncertainty on earlier dates rather than the regulator's actual period-start instruction. Bookkeeping's final unresolved note already identifies this contradiction.

Official MBR notice, read 2026-11-04: https://www.mbr.mt/post/informative-note-entry-into-force-of-legislation-1 . Short quote: “mandatory for financial reporting periods starting on or after 20th March, 2026”. It separately prohibits early/retroactive application. The fetched Cap.386 consolidated art185 contains the new figures but does not itself supply the reporting-period transition.

Impact: calendar-year 2026 accounts started 1 January 2026 and cannot use the new limits solely because their balance sheet is dated after 20 March. A company with assets4.5m/turnover9m/30 employees can be told to omit a directors' report incorrectly. Fix the applicable-period condition everywhere, and preserve old figures. This does NOT change GAPSME limits (fresh SL281.5 still4m/8m and20m/40m), or micro46,600/93,000/2. Retain a separate legal interpretation flag if challenging the MBR instruction rather than quietly overriding it.

### B2 [P2, confirmed wrong effective-year statement] Tax planning starts the optional final tax two years late

`malta-tax-optimization.md:73`: “Available from basis year 2026 under S.L.123.217”.

Fresh primary source https://legislation.mt/eli/sl/123.217/eng/pdf reg3(2)(a), read2026-11-04, allows fiscal year preceding YA2025 onward. Short quote: “year of assessment 2025 and subsequent years”. For a calendar period this includes basis2024, not a first start in2026. mt-corporate-tax correctly gives the earlier scope. Correct the start date; preserve the five-year lock and floor.

### B3 [P1, unsafe unconditional conclusion/internal contradiction] Corporate final-tax example claims winners whose floor is unresolved

`mt-corporate-tax.md:187`: “The election wins ... profits kept in the company ... or shareholders who would not claim refunds”. The same Guide's long final-tax discussion says unregistered shareholders and the retained-profit floor are unresolved; holding-company hypothetical3 and family-office line138 correctly preserve the dependency.

SL123.217 reg3(4)(a), same URL/read date above, requires a comparison after refunds claimable by all shareholders. No source fetched authorises ignoring that floor merely because profits are retained or an owner chooses not to claim. If no refund is legally claimable, a35% ordinary-tax floor defeats the asserted15% benefit. The text should state conditional cash-flow arithmetic only after resolving entitlement and article43(6); it must not assert the election wins. This audit does not claim to settle those questions. The accompanying24,000 example also assumes own losses and group relief remain available; it already states this uncertainty, so arithmetic PASS does not establish legal applicability.

### B4 [P2, missing condition in worked TP example] Thresholds alone do not make all2026 arrangements subject to TP

`malta-transfer-pricing.md:228`: after4.5m revenue/25m capital it concludes “the Rules apply for2026”, without saying the arrangements were entered into from2024 or materially altered. Example2 does provide that fact.

Fresh https://legislation.mt/eli/sl/123.207/eng/pdf rule1(2), read2026-11-04, retains pre2024 unaltered arrangements until basis years starting2027. Short quote: “on or after 1st January 2027”. State the post2024/new/material-alteration premise in example1. The Rule9 AND exception/OR entry logic and6m/20m numbers are correct. A crossed limit does not erase grandfathering.

### B5 [P2, unconditional guidance exceeds evidence] Class2 expense prohibition is presented more strongly than the research supports

`malta-bookkeeping.md:193`: “No deduction in the Income Tax Act”. The end note and tax-optimization line94 instead say no specific provision was found and the position remains unconfirmed. Absence of a named deduction does not decide the general income-production test. Fresh Cap123 art14/26 text was fetched, but no authoritative application to Class2 was found in this pass. Classify as UNVERIFIED, not a proved deductible or nondeductible amount; do not allow an automated tax computation to turn this row into an unconditional disallowance. Parent's personal-tax reviewer should resolve centrally.

### B6 [P2, routing defect] Financial statements repeatedly send company tax work to the individual Guide

`malta-financial-statements.md:28,57,161,227,272` route company rates/refunds/return/capital allowances to malta-income-tax. That Guide's declared scope is individual/self-employed, while mt-corporate-tax is the company computation. This is a repository-internal checked defect rather than a disputed legal claim. Route company handoff to mt-corporate-tax and keep malta-income-tax only for individuals.

## Previously unresolved items that fresh sources now clarify

### B7 Audit review standard is available from MTCA

`malta-financial-statements.md` audit section says the review-report guidelines could not be read, and asks the client to check. Fresh official PDF read2026-11-04: https://mtca.gov.mt/docs/default-source/documents/personal-tax/legal-and-technical/guidelines/audit-exemption-rules---guidelines.pdf?sfvrsn=14aab6d_1 . Short quote: “International Standard on Review Engagements 2400 (ISRE 2400) (Revised)”. Its examples also substantiate two-of-three review versus all-three no-review and individual parent/group interaction. LN139/2025 freshly fetched https://legislation.mt/eli/ln/2025/139/eng/pdf . The Guide distinguishes Companies Act audit and tax relief correctly. Who is professionally permitted to sign should still be tied to qualification rules; this PDF alone names the engagement standard, not every eligibility fact.

### B8 Filing portal and2025 date can be substantiated

Fresh MBR https://www.mbr.mt/post/notice-to-the-public-submission-of-financial-statements-to-the-registrar (Oct12 notice), read2026-11-04, confirms BAROS and12December2026 for31December2025 year-end accounts. Short quote: “by 12 December 2026”. This supports Guide Case1/3 and removes blanket current-portal-unread claims. Not every BAROS click/document requirement was audited.

### B9 Participation-exempt profits' Untaxed Account allocation has official historical corroboration

`mt-holding-company-participation-exemption.md:92` and `mt-family-office-setup.md:136` leave allocation as an Act-only unsettled reading. Fresh SL123.101 rule3 fetched: https://legislation.mt/eli/sl/123.101/eng/pdf . Current rule3(i) no longer lists participation exemption, reflecting LN194/2019. Official authority's indexed2020 company-return announcement explicitly says participation-exemption dividends are now allocated to the Untaxed Account: https://cfr.gov.mt/en/News/Pages/2020/Year-of-Assessment-2020-Tax-Returns-for-Companies.aspx . Direct open403, indexed official result readable. This is stronger than the Guide's bare inference, but preserve the access distinction; obtain the migrated MTCA page or Gazette LN194/2019 before declaring every exempt gain/account-allocation circumstance resolved. It is NOT a confirmed error to allocate these profits to UTA.

## Material conditional or unverified areas to retain as holds

- Corporate tax: 175% R&D commencement notice/implementing rules; elective15% losses/group-relief interaction; resident-individual shareholder/refund bar/43(6); fiscal unit6(2) interpretation; future YA2027 extension/TRA contents. Textual law fetched does not resolve those operational points. Do not use worked examples as proof of eligibility.
- TP: TRA135 contents and YA2027 applicability still not examined. Statement145 that documentation must be ready by filing is a prudent preparation rule, not an explicit deadline found in the fetched MTCA rule6 guidance (on-request reasonable time). Label accordingly. Rule8 says TP adjustments are relevant only for Income Tax Acts, so line213 “may affect” VAT needs a separate VAT-law condition, not automatic adjustment.
- TP CbCR row158 “EUR200 to50,000” is not a usable schedule. Fresh SL123.127 reg48 has several different triggers, daily amounts and caps. The range is not itself false, but insufficient to compute late/reporting/records penalties. Notification line148 “as per EU DAC” provides no actionable local deadline. Keep CbCR explicitly incomplete or route to specialist topic.
- TP line208 says Malta implementing15% GloBE without the Article50 deferral; fresh SL123.212 regs2/11 retains deferral. Corporate Guide has the qualification. Standalone TP summary should route there and not imply Malta currently levies15% top-up.
- Bookkeeping/optimization: a full acquisition-year deduction is verified from SL123.01 rule7(a); disposal rule7(b) has a year-end-date qualification which the summaries omit. The asserted blanket no allowance for every disposal year overstates text where an event is on the last day. Special-case hold, not all examples wrong.
- Bookkeeping printer-copier example classifies as “other machinery”5years without specifications, while computers/electronic equipment4years and rule4 preponderating use can matter. Formula240 is correct conditional on classification; require asset classification fact rather than a universal printer life.
- Bookkeeping bank row “MTCA ... never a P&L expense” is a payment-posting shorthand. Nonrecoverable VAT/capitalisation, employerSSC expense, direct-tax expense and penalties need original charge entries. Do not reinterpret as no underlying expense; journal illustration would prevent ambiguity.
- Optimization14D4,500 cap lacks the Act's aggregate-per-resident ceiling across different claimants; material if multiple relatives claim. Fresh Act confirms reporting requirement and aggregate ceiling. Social/pension/part-time/VAT figures need personal/VAT reviewer acceptance, not a duplicate clean stamp from this business pass.
- Formation: latest BAROS checklist/tax-number automatic registration mechanics still unverified; nominee/licensing broad assertions require sector-specific check. Minimum capital/private20%/public25%, fee bands100/210+12/294+17/379+17, annual85,42days,10year records freshly corroborated against Cap386/SL386.03.
- Selling: MTCA preliminary notification deadline and prescribed property-company share provisional-tax amount still explicitly unresolved. Cap372 art43 and Cap36442 freshly fetched; ordinary2% versus property75%/5% structure corroborated. LN156/158 site-plan text NOT independently reopened in this pass. BAROS exempt-only procedure freshly confirmed by MBR Nov28 notice: https://www.mbr.mt/post/important-notice-single-point-of-submission-for-form-t-form-h-and-msr-form-f-via-baros . No current sale workflow certification until missing deadlines/amounts filled.
- Residence/substance: statutes support incorporation/management-control/CFC rules, but domicile/common-law/treaty guidance and licensing are not settled by only reading Acts. Do not recast as a legal absence. CFC example900k−50k=850k,10% of50k=5k,100%control, zero-tax comparison mathematically consistent; arm's-length attribution remains a factual premise.
- Foundations/trusts: Cap331, SL123.114, SL331.10 (including LN252/2026), Cap16 freshly fetched. Default company/trust routes,30day election,14day BO/31Jan annual structure found; full private-trustee conditions, civil-law every permission/exception, duty exemptions and2026LN commencement not checked row-by-row. Reg3 of SL331.10 has special new child/marriage beneficiary declaration timing and trust categories; blanket fourteen-day change summaries are not exhaustive.
- Family office: licensing and immigration deliberately unresolved. No complete regulatory setup capability should be inferred. Non-dom35k/5k question belongs central personal residence source, not a separate unresolved rule invented across every hub.

## Arithmetic and test evidence

Existing executable checker: `python3 scripts/check-examples.py` with all11explicit files returned: checked11files,10oa-check blocks,0failures,0missing. This DOES NOT mean every file has machine-tested examples; six cases in financial statements, holding/family/trust hypotheticals are prose tables.

Manual recomputation: financial Case1/3 Oct31+42days=Dec12; Case4 Oct31minus184days=Apr30, plus42=Jun11; Case5 2329+46*60=5089; formation20k fee379+17*4=447/capital4000; corporate261k*.35=91,350,6/7refund78,300/net13,050;160k*.35=56k/refund48k/net8k/election24k delta16k (legal conditions not accepted); holding1m*.15=150k,1m*.35=350k,100k*.35=35k−30krefund=5k,100k*.15=15k,2m*.35=700k; family400k*.35=140k−100krefund=40k,15%60k,990k−900k=90k*.35=31.5k (management fees omitted from investment base explicitly); trusts200k*.35=70k,200k−70k=130k,100kallocation35k+100kretained35k=70k,15%200k=30k,floor70k/7=10k. All numerical arithmetic consistent with stated assumptions. No same-fact unconditional superiority claim accepted.

## Per-file disposition and consolidation recommendation

| File | Audit disposition | Recommended home / remaining boundary |
|---|---|---|
| malta-bookkeeping | Read; core records/wear&tear/fees checked; B5 and conditional omissions | Keep as practical accounting core, remove repeated tax tables in favour of corporate/VAT/personal links; avoid universal classifications |
| malta-financial-statements | Read; core corporate/accounting sources checked; B1/B6 block clean release | Keep dedicated statutory accounts core; repair period test; incorporate official review/portal guidance |
| malta-formation | Read; core formation and fees independently checked | Keep formation workflow, route computation elsewhere; checklist/BO implementation needs next pass |
| malta-tax-optimization | Read; B2 plus overlapping tax conditions | Consolidate into individual/company comparison or retire as independent rules source; preserve useful questions and examples in canonical jobs |
| malta-transfer-pricing | Read; rules1/2/9/guideline6 checked; B4 and CbCR/deadline holds | Keep specialist TP Guide only if supported; no need to repeat CbCR as almost-empty compliance table |
| mt-company-residence-and-substance | Read; CFC/interest/exit sources inspected selectively | Consolidate into corporate cross-border section or retain specialist draft with exact unresolved scope; no attestation claim |
| mt-corporate-tax | Read; major rates/refunds/election/deadlines inspected; B3 | Keep canonical company-tax job; link specialist exemptions and prohibit unconditional elected-regime comparisons |
| mt-holding-company-participation-exemption | Read; articles2/12/48 and tax-account source selectively checked | Fold concise participation test/refund sections into corporate tax; retain advanced subtopic as unclaimed draft if needed |
| selling-a-company-in-malta | Read; duty/provisional tax and BAROS sources selectively checked | Keep share-sale specialist workflow only as draft until prescribed amounts/notification closed; no new full review claim |
| mt-family-office-setup | Read; duplicated headline figures/math checked; regulatory route unresolved | Retire as standalone tax authority or convert to navigation-only hub. Preserve useful structure/questions, invite Malta specialist author |
| mt-foundations-and-trusts | Read; primary route laws inspected; no full provision ledger completed | Keep specialist draft/unclaimed or consolidate planning hub links; needs fiduciary practitioner for law/BO/duty precision |

## Attribution and trust

Five assigned files carry `reviewed_by: Michael Cutajar`, `reviewed_on:2026-11-03`, `tier:1`: holding-company, selling-company, family-office, foundations-trusts, company-residence. Their bodies contain substantive unresolved conditions. This is a repository metadata/reliability concern, not proof a live accountant review_record is invalid: application trust state was not queried. User explicitly permits empty topics without his name and other Maltese accountants contributing. Recommendation: do not attach Michael's attestation to unresolved specialist scopes merely from metadata; preserve contribution history, remove/replace public review claims only through proper current trust workflow and recorded authorisation. Leave clearly unclaimed specialist gaps rather than multiplying weak Guides.

## Limits of this pass

No full claim-by-claim original-language ledger produced for all2752lines. Primary-law fetches and targeted provision inspections are stated above, unresolved operational/common-law/source scopes remain. No personal-tax, payroll, VAT detailed acceptance supplied by this report; parent has separate owners. No claim of zero mistakes, country completion, professional attestation, production trust-label state, or every2027Budget proposal enacted. The root shell download of Cap123 failed network before PDF creation; fresh web fetches succeeded and are the source evidence used, not a claimed locally cached PDF.

## Additional precise conditional omissions

- `mt-foundations-and-trusts.md:63` ends by asserting one ordinarily-resident/domiciled beneficiary shuts article27D(3)(b). The same sentence earlier preserves the alternative of a beneficiary wholly exempt under article12. The closing assertion needs “who is not wholly exempt under article12”; otherwise it contradicts its own quoted statutory alternatives. This is an exception-condition defect, not a claim every ordinary-resident beneficiary is exempt.
- `mt-family-office-setup.md:148` similarly says one ordinarily-resident/domiciled beneficiary changes how a trust is taxed without that exception. Keep the full test in one canonical trust Guide.
- `mt-holding-company-participation-exemption.md:45–55` describes each participating-holding route but does not define “equity holding” as excluding a property company. Cap123 article2's equity-holding definition includes that exclusion. Property-rich situations are only referred near the end. Put the property-company exclusion in the front-door test, so users do not compute an exemption first and discover the exclusion later.
