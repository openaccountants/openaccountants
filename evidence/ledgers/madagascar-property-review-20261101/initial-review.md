# Madagascar annual property-tax independent review, 1 November 2026

**Verdict: CHANGES REQUESTED at frozen HEAD `b3e5620d1062e0881d699d3d7ca0c5c3e8e76264`.** Two narrow source-fidelity repairs are required. The remaining bounded rules and the two hypothetical computations are supported. This review is not accountant attestation, complete country coverage, verification of a live municipal filing, permission to publish, or merge approval.

Review identity: property follow-on on `codex/madagascar-property-2026`, draft PR #1224; content commit `15695d500186ca1b1d1d6d418b57d1e5d79a54d4`; preservation base `59c23acba2ad66dd2bb29ffc81ffbb9289769ef8`. Guide SHA-256 `75f8d4a60134a9d9347aee72b6c3d57b35077bda3622bfaa2aa3da8daefec30d`; JSON ledger SHA-256 `4007dfb36023adbd7c81a47d64201062163a7ed51677cb3269132ae450f98333`. The reviewer changed no Guide, writer ledger, README or existing review evidence. Only this new review directory was added; extracts and six rendered pages are outside Git in `../sources/property-review-20261101/`.

## Findings requiring repair

### F1. Preserve the ordinary notice period but hold the notified collection-title interaction

The Guide's filing step 5 and P31 accurately reproduce the three-month payment rule in [CPF VII-01, printed p.127 / PDF p.128](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf). However, the same code's full VII-33, printed p.133 / PDF p.134, explicitly covers debts in VII-01 as well as VII-32 and requires the collection-title notification letter to demand payment **“sans délai”**, with the sums **“immédiatement exigibles.”** The Guide describes simultaneous title issue but does not collect the title's notification facts or hold this interaction before giving the notice-based payment period.

The chapter-II heading does not alone remove property debts from VII-33: the article expressly cross-refers to VII-01. Baseline simultaneous issue applies to IFPB; the July LFR adds IFT. Neither text proves an actual title notification, nor does either establish the unproved radio/posted-publication activation date. This review does **not** decide that every property tax is payable immediately or that the three-month provision has been repealed.

Required repair: retain the three-month VII-01 wording as its statutory rule; state the separate VII-33 notification demand and explicitly hold how it interacts with that period; obtain the collection title, notification/mise-en-demeure document and dates; refuse a final payment-deadline conclusion where that interaction matters. Add the same hold to the unknowns, necessary client facts and ledger. No replacement activation date or unsupported priority rule should be invented. Source read: complete CPF VII-32–33, including notification paragraphs; original LFI printed pp.77–78; July LFR printed pp.32–33 and art.22.

### F2. Preserve the different conjunction in the IFPB permanent exemption

The IFPB base paragraph and P24 use “free social/medical works.” [CDI 10.02.03(2), printed p.147 / PDF p.148](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf) says **“à des œuvres gratuites à caractère social et médical”**. In contrast, the IFT exemption at 10.01.03(2), printed p.144 / PDF p.145, says **“à des œuvres gratuites à caractère médical ou social”**. A slash loses that explicit distinction and can be read as alternatives.

Required repair: for IFPB use “free works of a social and medical character,” retaining the gratuitous/exclusive assignment conditions. Preserve the IFT medical-or-social limb. Retain the exact combined-condition quote already present in P24 and correct the corresponding English wording in P24/the human ledger. This is a fidelity correction, not a conclusion that any unspecified charity is eligible.

## Clause review and statutory boundaries

All **50 ledger entries**, not 50 distinct figures, were checked against complete relevant clauses and neighbours. Forty-eight are accepted within the stated holds; P24 and P31 require the repairs above. The full row verdicts, independent condition observations, exact French quote anchors, PDF/printed page locators and read date are in `ledger-row-review.json`. The human ledger was read alongside the JSON and Guide. Quote substring checks supplement, and do not replace, the clause reading.

The review covered CDI 10.01.01–10 and 10.02.01–13 in full; 20.01.51–54 and 20.01.56.1–5 with surrounding text; 30.01.14–15; and the complete 30.02.22–23 including the continuation of the mining regime. CPF I-106–108, VII-01–06 and VII-32–33 were read with their headings and neighbouring clauses. The original LFI property, declaration and collection amendments and the July LFR penalty/collection amendments were compared with the codes. LFR tax headings were searched for property-scope changes. This is not a whole-law opinion on every amending provision.

The six IFT categories, local per-hectare tariff requirement and four-year vote/fallback, category-6 exclusions and statutory 1%, and MGA 2,000 per-assessment floor are supported. IFPB's 5%, MGA 5,000 per-building floor, principal-owner residence 30% **base**, approved industrial limb, local flat-charge criteria and council decision, and valuation-revision conditions are supported. No local tariff, commission value, flat amount or automatic annual compounding was invented. Permanent and temporary exemptions, first-cut/tree-density condition, separate fiscal-centre exemption applications, annual commune declarations and their different October wording, corrective declaration, notice authentication, seasonal deferment, acceleration events and disaster-relief window were checked.

The book-II 1%-monthly late-remittance clause is distinct from the turnover-based first-month scale. CDI 20.01.51's general application, 53's MGA 10,000 floor/started-month rule, 53.4 and 54's neighbouring sanctions were read. The Guide appropriately holds the floor/started-month interaction and complete sanction computation. The specific missing-declaration MGA 20,000 and IFPB access-refusal MGA 200,000 figures match their clauses. July's replacement of general 20.01.52 does not itself replace property-specific 52.2.

The nearby July insertion into VII-32 rounds an amount down to the next lower hundred ariary under its stated conditions. That provision sits under declaration-spontanée administration, while property assessment is under chapter I; applicability to a particular property assessment and operative timing are not decided here. Both examples already produce exact hundreds and therefore do not test a rounding conclusion. No final assessment or payment workflow is certified.

## Commencement remains held

Original LFI art.24, printed p.129 / PDF p.131, and signed/ampliation LFR art.22, printed p.48 / PDF p.52, condition entry on radio or posted publication independently of Gazette insertion. The LFI's 20 December 2025 promulgation and LFR's 16 July 2026 promulgation/ampliation do not prove those events. The rendered originals were visually checked. No operative calendar-year date, including 1 January or 16 July, is inferred. The Guide's 2026 label is a baseline identification, not evidence settling a commencement dispute.

## Independent computations and decision switches

The reviewer independently used decimal arithmetic before comparing the executable blocks. Case 1 gives MGA 1,500 before the floor and MGA 2,000 after it on market value MGA 150,000; MGA 400,000 gives MGA 4,000. The exact IFT break-even is MGA 200,000. Case 2 gives rented base MGA 240,000 and tax MGA 12,000; the owner's principal-home base is MGA 72,000, percentage tax MGA 3,600 and tax after the floor MGA 5,000. The alternative-use comparison is valid only with the stated actual-use conditions, not a discretionary tax election.

`independent-cases.json` records the calculations, adjacent floor cases, the principal-residence threshold, urban agricultural exclusions, industrial-land double-tax switch, 20-are/1,500-tree limits, completion/permit/Q4/1-April and inheritance boundaries, filing-date distinction and held title/rounding/penalty interactions. Relative exemption examples assume the provisions apply; they do not establish commencement.

## Preservation and machine checks

All eight prior Guides and 21 prior evidence files match their base Git blobs byte for byte. The 21 older evidence files are present in Git but not materialised in this sparse worktree; they were read/hashed through Git, not declared missing. All **86** destination ranges/headings were checked against the base and frozen Guide bytes. Content samples from base/deadline/cross-border sections were read across all eight Guides. `preservation-review.json` records exact hashes, all destinations and the samples. **Lost content restored: 0.**

README is exactly its original bytes plus the documented property-job append. The seven `partial:` entries remain byte-identical; the addition claims neither an extra completed ordinary domain nor a ninth previously reviewed draft. New Guide frontmatter contains no platform-written attribution/review/licence keys, no platform CTA, and carries the general-reference notice. Tier remains 2 with no accountant name.

All **15 shape checks** pass. The example checker passes one file/two blocks with zero failures or missing blocks. Stock `validate-guides.py --no-index-check` passes nine Guides with its retained `WARN: 0 same-job groups, see skills/DUPLICATES.md` warning group. An initial attempted `--help` invocation was not recognised as help by the stock script and ran default generated-index checks, reporting the expected stale `index.json` and `llms-full.txt`; no generated artefact was changed. The documented scoped check was then run and its actual output is recorded. Scripts test shape/arithmetic/preservation, not legal accuracy.

`initial-input-hashes.json`, `source-integrity.json`, `machine-checks.json` and the original writer freeze receipt bind this review to the exact candidate. Four PDF originals and four original text captures match their recorded SHA-256 hashes. Newly generated full-page extracts and six rendered pages remain outside Git. No live login, portal submission or payment acceptance was requested or claimed.

## Closure and status permission

**No acceptance or status-only permission is granted yet.** The writer can make the two factual repairs and submit a new frozen head/diff for independent closure. Keep this initial report and its row verdicts unchanged as historical evidence. A later accepted closure must state the exact new hashes and any narrow literal status-only substitutions it allows. All seven ordinary domains remain partial; this review supplies no accountant attestation, full-coverage claim, permission to close the country issue, permission to merge, push, publish, or alter a queue.
