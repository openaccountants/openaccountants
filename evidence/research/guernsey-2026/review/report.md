# Independent Guernsey whole-pack review

**Verdict: suitable to publish as an accurate, explicitly partial source-cited country draft at e98e95296a5f61fa4e30745a47a1eee3bdc7997d. No open P1/P2 findings remain after the two bounded writer fixes checked below.** This is neither a complete-country finding nor an accountant attestation, merge decision, filing opinion or claim to have reviewed the entire Income Tax Law. Keep issue #397 open and preserve the seven machine-readable partial entries.

Reviewed on 28 October 2026 by a fresh independent reviewer agent. Starting candidate: `21fe2436e7ee3333a6347a8b50eed0881bece759`; published comparison baseline: `a23757a23537adb396146d8294f3d404b7d9ac53`. Writer corrections during this review: `71cc66b67b5daf78cc6c922a7dee2b6398556aae` and `e98e95296a5f61fa4e30745a47a1eee3bdc7997d`. I inspected their complete bounded corporate diff and reread the resulting passages. I made no Guide, git, PR, publication or attestation changes. Review files alone were written under the separate review directory.

## Findings and closure

| Priority | Starting-candidate location | Finding, source and required correction | Final closure |
|---|---|---|---|
| P2 | `gg-corporate-tax-substance.md:361` | Both old explanatory paragraphs, **Established mixed income** and **Daily-penalty catch-up**, had moved with their executable controls into supplementary research. All substantive tax topics survived, but this breached the explicit requirement to move controls only and keep explanatory prose in the main Guides. Restore both original paragraphs, including their assumptions, alongside the main rate/penalty methods. Sources: [company rates](https://gov.gg/RevenueService/Companies), [penalty guidance](https://gov.gg/taxpenalties), and the byte-exact published original. | Fixed by the writer in `71cc66b6`. Verified both paragraphs byte-exact against the baseline, now at final corporate lines **88 and 151**. Exactly two main corporate blocks remain. |
| P2 | `gg-corporate-tax-substance.md:300` (the repayment-definition paragraph; line 304 after restoration) | The rule was correctly described but its pinpoint references were wrong: current s62AA has the repayment limb at **(1)(b)**, not (1)(c); the commercial-loan exclusion is in that same paragraph, with definitions in **(1)(b)(i)–(ii)**. Subsection (2) is the regulation-amending power. Correct both pinpoints and retain the commercial-loan/trading-company conditions. Source: [current Income Tax Law, s62AA](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=253819), printed pp192–193 in v.0113. | Fixed in `e98e9529`; final corporate line **304** now matches the provision. The wording also correctly says the company must **derive income from business**. |

**Lost content restored: 2.** This counts the two explanatory paragraphs restored to the main corporate Guide, not two lost tax regimes or lost executable blocks. No old substantive topic remains silently removed. No further material P1/P2/P3 correction is requested within the supplied partial methods.

## Whole-body and no-loss coverage

I read all nine candidate Guide bodies and the README, including preserved material rather than only new hunks. For the old/new comparison, shared paragraphs were read in the candidate, and every original-only paragraph and executable block was separately compared using `original-only-paragraphs.md`. This covers the full old and new bodies without pretending identical paragraphs need a second substantive interpretation. All ten archived original files were independently compared byte-for-byte with the corresponding `git show a23757a2:<path>` blobs; all match.

The substantive comparison covered:

| Guide | Old topics checked against final text |
|---|---|
| Individual income tax | Midnight residence and arrival tests; withdrawal order, relief transfers and conditions; rent-a-room; all cap categories/exclusions and contribution screens; return/agency/departure routes; filing penalties, appeal, Tribunal and onward appeal; protected pension example. New ordinary source/base, repairs transition, limited residence and payment methods supplement these. |
| Corporate tax/substance | Entity/territory scope; registration/forms/certificates and original rates; all CIGA/activity definitions, high-risk IP tests, rebuttal/return/exchange, escalation and inspection safeguards; pure-equity/no-income distinctions; distribution/loan directions; reporting/migration/minimum-tax screens; both restored explanatory examples. New ordinary base/loss and loan methods supplement these. |
| Payroll/social insurance | Class/territorial and labour-only classifications; historic director election discrepancy; Class 2 application and Class 3 allowance ordering; dividends/qualifying loans/pension age; all original benefit valuation, exemptions, employer-paid tax, homeworking, vehicles, housing/election, salary sacrifice and period limitations; ETI/corrections/records/refunds and cross-border certificates. |
| Secondary pensions | Territory/age/earnings and voluntary status; historical employer phases; contribution base/rates; scheme approval, deferral and provider-versus-Revenue timing; opt-out/refund/re-enrolment and retention; cross-border limits. New statutory choice/penalty provisions supplement these. |
| Formation | Applicant/office/director/agent; all application documents, initial capital/guarantee/cell cases; beneficial ownership/person registration/publicity; fees; certificate/handover and exclusions. |
| Accounts/reporting | Records/accounts/period/delivery; all separate waivers; validation dates/exceptions/fees; late-filing and civil penalties; conditional question map and £5m reporting boundary; register corrections, draft refresh, association-date and disclosure caveats. |
| Property | All seven graduated bands and examples; personalty; additional-rate repeal/transition; conditional downsizing; Court roles/workflow; indirect transfers, exclusions, payment and claim gaps. |
| UK corridor | Entire residence/PE/profit attribution; employment; credits and anti-abuse; investment income; associated enterprises; pensions/government/student; capital/offshore; MAP/arbitration/status conflict; collection assistance and all numerical boundaries. |
| GST | Policy-versus-law distinction; adopted safeguards; dates/rate/food direction; inflation and ISE planning; operational exclusions; both hypothetical price cases. |

### Size and cut inventory

| File | Old/final bytes | Byte change | Old/final lines |
|---|---:|---:|---:|
| README | 5,729 / 7,556 | +31.89% | 40 / 52 |
| Accounts/reporting | 19,304 / 25,191 | +30.50% | 163 / 199 |
| Formation | 8,792 / 11,882 | +35.15% | 79 / 125 |
| Corporate | 43,283 / 66,934 | +54.64% | 320 / 418 |
| GST | 8,447 / 8,984 | +6.36% | 110 / 110 |
| Individual | 29,733 / 43,385 | +45.92% | 330 / 339 |
| Payroll | 35,420 / 35,901 | +1.36% | 394 / 320 |
| Property | 15,192 / 16,537 | +8.85% | 184 / 183 |
| Pensions | 13,739 / 16,122 | +17.34% | 147 / 157 |
| UK corridor | 51,467 / 52,217 | +1.46% | 399 / 319 |

No file is more than 25% shorter by **either bytes or lines**. Largest line reduction is the corridor's 20.05%, followed by payroll's 18.78%, chiefly moved executable blocks. The supplied no-loss inventory enumerates all **20 moved original blocks**: corporate 2, individual 4, payroll 6, property 1, corridor 7. All their subject matter and explanatory qualifications remain in the main Guides after the corporate restoration. Stale access-gap text and now-resolved gap descriptions are replaced explicitly by new methods/current limitations, not silently erased. The complete old bodies and controls remain archived. There is no >25% cut requiring a further removed-content list.

## Computations and boundaries

Independently ran the checker on the nine main Guides, the full original archive and both subject-specific archives at the final head: **12 files, 57 blocks, 0 failures, 0 missing** (`checks.log`). This is **18 main + 32 original archived + 7 intentionally duplicated subject-archive blocks**. The original 32-block archive is a byte-exact multiset match to all original published controls. Each main computational Guide contains exactly two blocks.

Substantive spot-recomputations and source-boundary checks include:

- Income allowance £85,000 withdrawal start and £161,000 personal-allowance exhaustion; ordered protection of otherwise deductible £2,500 pension relief. Rental transition: £4,500 standard + £4,500 current + £2,500 historic additional repairs, £1,000 allowed interest, £17,500 rental income, £2,300 taxable, **£460** tax. The 2026 transition sum remains capped at rental value minus standard deduction.
- Corporate bridge: £200,000 + £10,000 − £8,000 − £30,000 = £172,000, at 10% = **£17,200**. Loan £8,000 net / 0.8 = £10,000 gross; tax £2,000; £3,000 timely repayment supports **£750** proportional tax repayment. £2,500 is an aggregate exemption boundary, not a deduction. Commercial interest alone no longer exempts an ordinary participator loan following the 2013 repeal effective 1 January 2014.
- s81(1A): April/July/October in the year and January next year, with **not before** 17 March / 16 June / 16 September / 17 December assessment cut-offs and 30 days from issue. s66B claim runs within 15 days of the reporting date for the repayment quarter; s66C charge is on net-grossed qualifying loans and quarterly return/payment is within 15 days. Both loan tax-payer identity and earlier-loan repayment ordering are preserved.
- Strict/non-strict boundaries: retail **exceeding** £500,000 with associated-company aggregation; Class 1 at £832 on the whole base; Class 3 exemption tested before its £11,122 allowance; cars **more than** 75% business use; audit thresholds **at least** £10.2m/£5.1m/50 in both years, ≤10-member exclusion, ≥90% waiver and >10% rescission; December incorporation exception; property £500,000 slice; treaty 183/184 days, >50% property/PE relationships, <25% investment-owner route and 30/31 offshore days.
- s234 really says **before** the last February day. The Guide preserves the Registry's conflicting **by** wording and uses 27 February 2026 for a statutory work calendar. I do not flag its earlier date as a mistake.
- New pension instrument: effective 12 May 2026; at least seven days' scheme choice; £150 fixed; £50/day first 30 chargeable days then £100/day; 30 days from issue to request review. The Guide does not present these as automatic invoices without notice prerequisites.

## Source scopes and access limits

The following are actual reread scopes, not claims to have read every page of every downloaded source:

| Primary material | Scope checked in this review |
|---|---|
| Income Tax Law v.0113, official file253819, saved PDF/text | Cited operative portions of ss2–16, 39B–39C, 47G–47I, 51–51A, 58–62AA, 66A–66C, 67, 76–76A, 80–81/81B, 84–86, 108, 133–135, 139, 141–144, 147, 193A and 199; s209 retail/reporting terms and cap/rate source passages. Not the whole 757-page Law or every incorporated/specialist enactment. |
| Rental repairs Regulations 2026 file327585 | Complete rr1–7, including current-plus-historic 2026 sum, cap cross-reference and discretionary 2027–2030 route. |
| Distribution deductions 2008 file267621; loan exemptions files267761/266936/266902 | Complete instruments and amendments; tested continuing exclusions against repeal. |
| Companies Law v.0108 file250998; audit consolidation file267485 | Cited ss17, 179, 234, 238–245, 251, 255–256A; audit rr1–4 and amendment notes. Historic dormant/asset-holding cross-reference definitions not reconciled. |
| C52, M24, C37, C44, R10, R15; Annual Allowances id2086 | Full supplied practices and both allowance-table pages. C52 is updated 23 July 2026; M24 30 December 2024. Form 651's historical date is explicitly retained. |
| 2021 substance regulations id141223 | Cited company scope, ordinary/IP/pure-equity/CIGA/reporting, high-risk definition/rebuttal, penalty/appeal/inspection provisions, definitions and commencement/revocations. No comprehensive subsequent-amendment or imported enforcement/sector-law review. |
| 2026 monetary values id185595; 2026 rates leaflet id102818; rates/withdrawal/residence/returns/penalties/employer/company pages; forms 706/707, 690(b), departure form; Tribunal guidance | Claimed rate/threshold tables and cited procedural portions, source dates and guidance conflicts. These are authority guidance/form-based scopes where labelled, not a complete statutory penalty opinion. |
| Benefits in Kind 2026 id202739; Employer Guide 2025 id175677; SIC1 id196680 | Claimed sections 1–12, relevant Fact Sheets 1–2 and cited E4/E12/E13/E15/E17/E18/E20/E24/E28/E35/E38/E46/E48 summaries; employer referenced procedures and SIC1 allocation/dated-election limits. Full statutory benefit/SI regulations remain excluded. |
| Pension employer/contribution/opt-out/reporting pages; 2026 file327675 | Claimed guidance conditions and rates; complete rr1–8 of new instrument. Full underlying pension Law and notice/appeal/commutation entitlement not established. |
| Registry handbook, incorporation/fee/waiver/validation guidance, 2026 question list, civil-penalty PDFs | Claimed ordinary methods, figures, form branches, portal instructions and discrepancies; exact civil-penalty band-date regulations remain unresolved. |
| Property/Court sources | Fresh official property-rates PDF question11/Tables1–3; Budget duty amendments ss1–5 and paras5.87–5.96/footnote16; Hansard printed pp63–65; four Court pages. All seven fetched HTTP200 by the parent during review, then independently read here. Receipt: `../work/property-primary-receipts.json`. Not full charging/valuation/exemption law. |
| UK–Guernsey Agreement and Protocol 2018; HMRC index/DT8602; exchange of letters; arbitration MOU; OECD profile | Cited allocation/threshold/credit/MAP/collection articles and Protocol, entry/effect dates; MOU Parts1–2/11/13 and signatures; historical profile Q2,5–12,16–17. HMRC's index/MOU effective-status conflict is real and correctly remains unresolved. |
| GST reform programme; vote pages2682/2787 | Saved authority timetable/current consumption detail and fresh normal-browser reads of both carried 2 October 2026 resolutions, including all commencement safeguards and the separate legislation-preparation direction. Future programme is not treated as a 2026 charge/exemption. |

Fresh `web.run` could not retrieve the legal-library printable PDFs and returned 403 for the government rates page. A normal browser loaded the rates page and its expanded **2026 Budget changes** successfully; it corroborates 20%, £15,200, £9,800, £85,000, £3,500, 50% let-interest and the published £50,000 standard-charge announcement. The PDF tab exposed no readable accessibility text, so current-law review used the saved official PDF/text plus version/hash receipts. The saved Income Tax PDF hash is `2eb6844c4cfda7d0c1d1b04828d830694ab04e5bb31d73ccac6a6bdc64f141d5`. The OECD PDF was accessible through web retrieval despite the earlier writer's HTTP403. Vote pages loaded in the normal browser despite historical TLS and web-tool failures. No CAPTCHA, certificate bypass or security-warning bypass was used. Historical failures are not current blanket access blockers.

The consolidations state they lack authoritative legal effect. This review checks the cited published text and specific instruments, not a full authentic-enactment concordance or legal sign-off.

## Metadata and publication boundary

Nine slugs remain unchanged. All existing protected/platform fields, licence, attribution/byline, reviewer fields and dependency values are preserved, including absence where originally absent. All existing `<!-- openaccountants-cta-block -->` marker-to-EOF tails match byte-exact; no new CTA was invented. Versions and dates advance from each existing PR baseline and never decrease; heading versions agree where present. The three Guides also present on origin/main exceed its stored version/date; six newer Guides are absent there, so their published PR originals are the relevant preservation baseline. See `final-integrity.json` for byte counts/hashes and per-file results.

The README truthfully remains partial for **IT-IND, IT-CORP, VAT, SC, PR, TP and XB**, with property and supporting-administration exclusions also visible. In particular, the implementing standard-charge amount, mixed-rate distribution credit, complete Class2/Class3 and mixed/partial periods, domestic TP/documentation, current consumption scope, property charging/claims and domestic cross-border operations are not closed by this review. Nor are specialist pension, cap, regulated/minimum-tax, all subsequent substance amendments or court procedures certified complete. These exclusions do not invalidate the specifically supplied methods.

This report approves only publication of this accurate **partial improvement** in the existing country batch after the coordinator's final checks. It does not authorize merge, close issue #397, establish professional attestation or replace the required public review record before any later merge. I did not rerun the parent-reported broad schema/unit suite; my independent executable run is recorded above. An unrelated untracked `resp.txt` was visible at the end; I did not create, alter or delete it.
