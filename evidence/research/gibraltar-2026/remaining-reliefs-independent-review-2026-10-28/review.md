# Independent review of Gibraltar individual relief additions

**Later disposition:** the bounded repair is accepted at **6f53123a0306500efec732d97e42abc5ef764388**, with no open findings. See the [separate closure](closure-6f53123a/closure.md). The original review and finding below retain their initial immutable scope.

Reviewed immutable head **933e6993fe5305609c849551765a27ba9a116e8b**, individual Guide **v0.11**, SHA-256 **a9b85de524d87989dfc10c57ae7646bc545182b3920e3e791a88a224981f39ff**, on **28 October 2026**.

**The new tax rules and calculations pass. One ledger location correction remains before unconditional acceptance of this evidence package.**

## Finding GI-REL-01: correct the new ledger locations

Priority 3, provenance location accuracy. REL-02, REL-03, REL-05, REL-06, REL-07, REL-08, REL-09, REL-10, REL-11 and REL-12 name “Rates, bands and thresholds”, “Deadlines and filing” or “Who this applies to” as a location, alone or alongside “The base”. All four new relief subsections actually sit inside **The base**. Those other H2 sections contain no new relief text.

Correct the ten new `guide_section` fields and corresponding Markdown ledger labels to the actual location, preferably with the relief subsection title. The applicable requirement is the figure ledger's Guide-section mapping. The rules, legal sources and figures do not need to change. The reviewer has not edited any writer files.

## Verified new scope

All **14 new rows**, **six source-proof units** and **57 snippets** were checked against their own cached official source. The four complete operative documents and both complete targeted amendments were read, including commencement, eligibility, limits, additional-relief provisions, allocation, certification, evidence and claim requirements. The eight energy-performance rating/rate pairs and the relevant disabled-access and EV provisions were also inspected visually.

| Source | Checked scope |
|---|---|
| [Energy (Deductions) Rules 2015](https://www.gibraltarlaws.gov.gi/legislations/energy-deductions-rules-2015-3877/download) | All rules; £6,000 aggregate, equal amounts over two assessment years, Town Planner certification and two-year written claim |
| [Energy Performance (Deductions) Rules 2018](https://www.gibraltarlaws.gov.gi/legislations/energy-performance-deductions-rules-2018-2840/download) | All rules and Schedule; all eight achieved-rating percentages, EPC cost, property-zone exclusion, certification and claims |
| [EV Charger (Deductions) Rules 2018](https://www.gibraltarlaws.gov.gi/legislations/electric-vehicle-charger-deductions-rules-2018-4465/download) | All rules; legal title, £2,000 aggregate, allocation, certificate and written claim |
| [LN 2022/170](https://www.gibraltarlaws.gov.gi/legislations/electric-vehicle-charger-deductions-amendment-rules-2022-6610/download) | Complete amendment; former 30 June 2021 cutoff deleted, effective on publication, 7 July 2022 |
| [Disabled Access to Property (Deductions) Rules 2020](https://www.gibraltarlaws.gov.gi/legislations/disabled-access-to-property-deductions-rules-2020-5618/download) | All rules; business-property eligibility, £15,000 aggregate, conditional approvals, authority split, letter and two-year claim |
| [LN 2026/125](https://www.gibraltarlaws.gov.gi/legislations/disabled-access-to-property-deductions-amendment-rules-2026-8467/download) | Complete amendment; work deadline becomes 30 June 2030, effective on publication, 18 June 2026 |

The disabled-access eligibility provision's reference to rule 6 is printed in the source although certification is in rule 5. The Guide retains the mismatch and does not decide actual certification or retrospective gap-period eligibility. The EV wording does not import a different scheme's two-year claim period or assert absence of general time limits. Wider ABS/GIBS and claim interactions remain explicit limits.

All recorded source-file hashes matched. Snippet normalization removed only repeated Government copyright and page-number footer lines and collapsed whitespace. Running headers and all substantive text remained. The detailed offsets, source URLs, read dates and hashes are in [source-proof-results.json](source-proof-results.json).

The official EV and disabled-access index pages were also reopened and matched the cached update dates. The web tool could not fetch the two energy index pages; the hash-verified cached official indexes and full PDFs were read. No failed substantive check required research beyond the cited sources.

## Independent arithmetic

| Scenario | Independent result |
|---|---|
| Solar, £8,000 actual cost, £6,000 cap, 60:40 split | £6,000 total, £3,000 each year; £1,800 and £1,200 per claimant each year |
| Performance, rating D, £10,000 works plus £200 EPC | £10,200 base × 30% = £3,060 income deduction |
| EV, £2,800 actual cost, £2,000 cap, 75:25 split | £2,000 total; £1,500 and £500 |
| Disabled access, £18,000 qualifying cost | £15,000 capped deduction |
| Preserved main GIBS example | £2,720 + £1,520 + £3,750 = £7,990 |
| Preserved main ABS example | £888 top-up; £20,000 taxable income; £560 + £2,040 + £1,560 = £4,160 before credit |

These calculations were independently written with Decimal arithmetic and compared with the writer's expected results. The repository checker separately passed all six controls. The four new scenarios assume statutory eligibility and certification; they calculate deductions from income, without claiming a tax refund or actual tax saved.

## Preservation and validation

The completed prior country review was preserved rather than reopened. The **60 accepted individual rows and 87 proof units are data-exact**. All **39 unaffected blobs** in the prior **41-entry accepted-content manifest** remain exact. The individual Guide and README are the two expected changes. The prior review's archived evidence hashes also match.

The v0.10 baseline snapshot matches the published Guide at `f7d59d7c4679192f0e5d3bbe286742fb78531c11`. Its complete **90-paragraph** map was independently reconstructed. **88 paragraphs remain byte-exact**. The two changed paragraphs replace the unfilled property/energy authority gap with sourced conditions and explicit remaining cross-scheme, claim and certificate-reference limits. No original topic was lost. Protected metadata, prior source entries, CTA and both main controls are preserved. The Guide has all **nine canonical H2s** and **exactly two main oa-check blocks**.

All seven `partial:` domain entries remain. The other six partial reasons are exact. The individual reason retains the remaining substantive gaps. There is no complete-country or accountant-attestation claim.

Country schema validation checked 18 Guides with zero errors. The existing, unchanged global-minimum-tax Guide produces its tax-year-2024 freshness warning. Strict metadata validation passed with zero errors, warnings or notices. The supplied YAML-enabled interpreter was used after system Python lacked PyYAML. No application tests, deployment, live transactions, commits, pushes or external messages were performed.

Detailed evidence: [all new rows](all-new-row-results.json), [independent arithmetic](independent-arithmetic.json), [preservation and all paragraph destinations](preservation-results.json), [schema results](schema-results.json), [repository examples](repository-examples.log), [metadata integrity](metadata-integrity.log), [machine-readable review](review.json).

The next review is bounded to corrected new location labels and invariant hashes. The substantive source and arithmetic checks above remain completed evidence.
