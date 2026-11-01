# Gabon independent review, 1 November 2026

**Changes requested.** The eight Guides can remain an explicitly unfinished research draft. This review does not approve an operative 2026 tax pack, a completed country, accountant attestation, or merge. Four focused corrections are required before the source review can pass. All seven domain `partial` entries must remain.

## Immutable review boundary

- Repository: `openaccountants/openaccountants`, public PR 1212, issue 458.
- Candidate: `d90a78e28adb1804d0e1fd904886dc16c00cd2bb`.
- Base: `59c23acba2ad66dd2bb29ffc81ffbb9289769ef8`.
- Reviewed the actual candidate Guide files, eight writer ledgers, source manifest, rules, inventory, old-topic records, old blobs and pack README against `CLAUDE.md` and `docs/skill-template.md`.
- This was a separate reviewer. No Guide, writer ledger, writer README, generated file or production data was edited. No commit, push, public comment or merge was performed. Parent owns repairs and publication.

## Required corrections

### F1. Apply VAT prorata only after direct attribution

**P2, Guide and ledger:** `skills/gabon/ga-vat-gst.md:46`, ledger `V-PRORATA`.

“Partial activities need the statutory ratio: no credit at or below 10%” can deny credit on inputs used exclusively for taxable operations. CGI article 226 first requires attribution to taxable, non-taxable or shared activity. Its third bullet applies prorata when inputs serve both categories. This scope must sit beside the 10% and 90% conditions.

Primary source: [DGI CGI 2025, art. 226](https://dgi.ga/wp-content/uploads/dgi-content/d1dde772234076c5d2bc0a8d8d3db573ed3d8fdd6c3e869c8c57cd181a81bb70/assets/dgi/2d50ab6c2e-Gabon-CGI-2025.pdf), PDF page 84, SHA-256 `69fdb3d87ede508e412fed7561a256ced70401778ca25489ec90454b1fefdca9`. Exact relevant wording: « lorsque les biens et services concourent exclusivement à la réalisation d’opérations ouvrant droit à déduction, la TVA qui les a grevées est déductible » and, for shared inputs, « seule la fraction de la taxe qui les a grevées est déductible par application d’un prorata ».

The July law changes article 227(3), not this allocation gateway. Its page 7, printed page 6, expressly says « Le reste sans changement ». Keep the exact 90% case on hold: the text says over 90%, and strictly between 10% and 90%; it does not resolve equality at 90%.

**Repair:** state direct attribution first, then restrict the quoted ratio to shared inputs; add article 226 and the relevant quote to the ledger. This correction uses the same historical baseline status as the rest of the Guide, without certifying its 2026 currency.

### F2. Carry the car/travel allowance non-cumulation condition

**P2, Guide and ledger:** `skills/gabon/ga-payroll-social.md:45`, ledger `P-CAR`.

The own-vehicle, professional-use, no employer vehicle and XAF 100,000 conditions are supported. The surrounding article also states that car/maintenance and displacement allowances cannot be combined. The July amendment replaces article 91 bis paragraph 5; it is not a replacement of the whole article. The adjacent restriction must accompany the exemption or be explicitly held pending reconciliation.

Primary source: [DGI CGI 2025, art. 91 bis](https://dgi.ga/wp-content/uploads/dgi-content/d1dde772234076c5d2bc0a8d8d3db573ed3d8fdd6c3e869c8c57cd181a81bb70/assets/dgi/2d50ab6c2e-Gabon-CGI-2025.pdf), PDF page 40, same CGI hash. Exact wording: « L’indemnité de voiture ou d’entretien de véhicule et l’indemnité de déplacement ne sont pas cumulables. » The [July law](https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178593988623.pdf), PDF page 3, printed page 2, identifies « Article 91 bis alinéa 5 nouveau » and retains « dans la limite de 100.000 FCFA par mois. »

**Repair:** add the non-cumulation condition and its baseline source to the ledger and payroll explanation, retaining the commencement/currency hold. Do not silently present July's reproduced cap as a newly established effective-date rule.

### F3. Remove the unsupported CNSS employer aggregate from the evidence

**P2, writer evidence only:** `docs/research/2026-11-01-gabon-pack/rules.json`, `P-CNSS`, and the corresponding payroll ledger block.

Both still assert “employer total18%, worker5%”. The Guide itself correctly withholds a combined employer total; this finding is **not** that the Guide computes or publishes 18%. The evidence record must not contradict its own allocation hold.

Primary source: [Decree 0487/PR/MASI, art. 2](https://journal-officiel.ga/22255-0487-pr-masi-/), SHA-256 `95b41f5246eb0fab6bbcd817299f0fbcee1fe5189f908596262ba49d91d2ec13`. Exact wording: « Prestations familiales et prestations de maternité : 5% », « Accident de travail et maladies professionnelles : 2% » and « Assurance vieillesse, invalidité et décès: 16%, soit 11% part employeur et 5% part travailleur. » This text expressly allocates the pension branch but does not expressly allocate the other two branches to the employer. The live CNSS issuer announcement repeats the same branch split, without settling that allocation.

**Repair:** delete the unsupported combined employer assertion from `P-CNSS` and its ledger, leaving the supported pension split, branch rates and monthly cap. Preserve the original-gazette/publication and employer-allocation holds. No employer aggregate is certified here.

### F4. Correct two VAT threshold page locators

**P2, writer evidence only:** rules and VAT ledger rows `V-DOMCAP`, `V-FORESTCAP`.

The values are correct baseline values. Their “main quote” locators are false matches to the same numbers elsewhere in the code:

| Rule | Recorded page | What that page actually contains | Correct source |
|---|---:|---|---|
| `V-DOMCAP` | 53 | Arts. 137-138, professional income regime turnover limits | Art. 208, PDF page 73 |
| `V-FORESTCAP` | 69 | Art. 195, investment conditions for new activity relief | Art. 208, PDF page 73 |

Primary source: DGI CGI, same hash as F1. Art. 208 says « si leur chiffre d’affaires hors taxes est supérieur ou égal à 60.000.000 FCFA. » followed by « Ce seuil est porté à 500.000.000 FCFA pour les personnes qui exercent des activités d’exploitation forestière. »

**Repair:** change both locators to page 73. Read the complete article 208 and 208 bis for the two-year continuation and option conditions. Main-quote substring presence alone is not article verification.

## Full rule and placement coverage

Checked **93 unique rule records and all 127 Guide-ledger placements**, including the grouped numeric conditions, not just each row's first snippet. `all-rule-review.csv` records a separate verdict and condition note for every unique rule. `rule-coverage.json` pins source hash, article, quote and page matches. `placement-coverage.json` checks every ledger block and all **215 quote placements**. Every quote matches the independently extracted source with whitespace-only normalization; this does not make an incorrect page/article association valid, as F4 shows.

Five unique rule records are affected by F1-F4: `V-PRORATA`, `P-CAR`, `P-CNSS`, `V-DOMCAP`, `V-FORESTCAP`. The other 88 match the read baseline or identified amendment within the expressly stated holds. This is a count of rule bundles, not a fabricated count of individual numeric tokens.

Eight of the 127 placements are explicitly “supporting evidence for the linked article”, rather than direct numerical statements in that Guide: overview `C-SECTOR`, `C-MIN`, `C-FLOOR`; income `I-BANDS`; cross-border `V-NONRES`; corporate `G-INTEREST`; formation `G-PAY`; TP `T-CBCRRATE`. They were checked as supporting context, not counted as eight additional public figures or literal headings. The automated literal-heading field is empty for those composite descriptions by design.

Minor ledger wording improvement: `I-SHARES` says “up to6”. Its accompanying exact quote correctly says « dans la limite de six enfants. » Spell out **six children**, so it cannot be read as a six-share cap. The Guide's one-share/two-share examples are correct and do not depend on that shorthand.

Checked bundled conditions include corporate rounding, one-quarter/one-third instalments, turnover classes and relief restrictions; residence alternatives and worldwide income; all eight IRPP bands, shares and declaration-conditioned deductions; distinct social ceilings and payer categories; VAT threshold continuation/option, exemptions, origin conditions, invoice/inventory timing, ratio boundaries and digital option; payment classification and PE duration thresholds; TP/CbCR period, entity, exchange, floor and cap conditions; and capital subscription/funding dates and national derogations.

## Source acquisition and actual reading

The initial sandbox fetch failed DNS resolution. A subsequent authorized direct fetch used normal certificate-validated HTTPS and returned HTTP 200 for all eight source URLs. No TLS, authentication or CAPTCHA bypass was used, and no archive was needed. A normal browser attempt for the DGI PDF gave no usable text, so no reading claim rests on that view. Web-tool access to the CGI and July PDF failed, but the validated direct downloads succeeded.

The four PDFs were independently extracted from the hashed originals with `pdftotext -layout`, rather than trusting the writer's `.txt` files. Read the cited provisions and surrounding scope/exception provisions; the per-rule notes identify them. Relevant actual ranges included CGI pages 1, 4-8, 15-17, 21-28, 35-36, 40-43, 46-47, 53, 58-63, 69, 72-74, 80-85, 87-89, 120-121, 187-194, 228-231 and 261-266; initial finance-law pages 1, 3-7, 71-72; July pages 1-13, 16 and 86; and the relevant OHADA formation, registration, SARL/SA/SAS provisions. This is not a claim to have read every paragraph of each full source document. Independently rendered and visually inspected the full IRPP table page and July VAT/input/prorata page.

| Source | Original cache SHA-256 | Direct verification |
|---|---|---|
| CGI 2025 | `69fdb3d87ede508e412fed7561a256ced70401778ca25489ec90454b1fefdca9` | Fresh original bytes identical |
| Law 041/2025 | `6e649f3716bb847cd9f3c23bd95afb426710230f1eaa0b6854e8bf5e4aaf380e` | Fresh original bytes identical |
| Law 002/2026 | `85c30d2292bd57008059b83fa9bb0cfdec9ba1c24b061a44eed052f4379cc941` | Fresh original bytes identical |
| OHADA WTO-deposited act | `c7a6c71adeabb69aa588cad72f8d6e34e24353b25d4ff469f24777970d9f713c` | Fresh original bytes identical |
| CNSS decree HTML | `95b41f5246eb0fab6bbcd817299f0fbcee1fe5189f908596262ba49d91d2ec13` | Fresh original bytes identical |
| CNAMGS HTML | `7965c033a34cdc05defe2c51d43e75f9fe7b64df3edc080540dd94bd8af8e9e2` | Fresh original bytes identical |
| ANPI HTML | `1d3282a10d05ac997523b385e2019251ff58a34e7f9891bde894c8621c5f08aa` | Fresh HTML differs; displayed dossier/licensing/circuit wording re-read and matches relied-upon content |
| CNSS announcement excerpt | `e59d658bb289dcb8acabba463eada3c2aaf33a394ed8fe6b413ee7f934f3354e` | Writer cache is a transcription; fresh original issuer HTML independently obtained and article body read, confirming 1 January and first DTS 30 April 2026 |

`source-checks.json` records direct-response hashes and outcomes. Large extraction/render/HTML working files are retained in sibling `../review-cache/`, outside the public repository; original cache remains in `../sources/`. No live private account was accessed.

## Old-topic preservation and metadata

Checked **all 77 old headings, introductions and bullets**, not just selected examples: formation 18, corporate 18, payroll 15, overview 13, VAT 13. `preservation.json` verifies each base Git blob and SHA-256 against the actual immutable Git object. `old-topic-coverage.json` includes the exact old text, target and disposition for every item. Every pre-CTA nonblank baseline line has a mapped destination. Existing scopes are retained, corrected against primary text, routed to the owning calculation, or expressly held in Sources; no old job is deleted. The old approximate totals, unsupported timelines/fees, incorporation UBO claim, construction/property generalization, excise range and territorial-individual claim are not quietly converted into current rules.

**Lost content restored: 0.** No old-topic restoration was needed in this review. The new conditional corrections F1-F2 are distinct from preservation of old topics. None of the five rewritten files is more than 25% shorter; all grew.

All five old CTAs are byte-identical, with SHA-256 `8cd4c4808bbe51717a9a0affbd4b4bb61a162cd4b7befd12886e425ebb7d68c1`. Platform-written fields are exactly preserved. All three new Guides omit platform/author/trust fields and CTAs. Descriptions parse to 103-110 words; all H1 versions match numeric frontmatter version `0.1`. Exact candidate Guide Git blobs and SHA-256 values are in `metadata.json`.

## Recomputed cases and validation

Independently recomputed every one of the **16 cases**, including the eight factual decision comparisons. All declared outputs agree. `example-review.json` records every output and the limited legal assumptions. Key results include the 1,000,000 corporate floor, IRPP 474,000 versus 138,000, separate pension/health caps, local rebar comparison 300,000 versus 1,800,000, CbCR threshold differences, 25% versus ordinary 20% withholding, SARL/SA/SAS funding assumptions, and separate-liability/residence inventories. A correct hypothetical calculation does not close current-law or filing-route holds.

Reran with the supplied validation dependencies:

- `check-examples.py --require` on all eight Guides: 16 blocks, zero failures/missing.
- `validate-guides.py --changed-only --no-index-check`: eight Guides, zero warning groups.
- `check-sync-integrity.py --base 59c23acba2ad66dd2bb29ffc81ffbb9289769ef8 --head d90a78e28adb1804d0e1fd904886dc16c00cd2bb --mode audit --strict-metadata`: eight source Guides, zero errors/warnings/notices.

Logs are retained alongside this review. These checks do not test tax-law currency or prove source interpretation.

## Unresolved acceptance limits

Keep open the intervening 2025/2026 amendment chain, first taxable periods/July commencement, full VAT item consolidation and exact 90% case; original CNSS Gazette/publication and branch allocation; CNAMGS underlying decree/version; monthly salary tables and annual payroll workflow; complete individual category computations; current instructions, forms, boxes, payment references and accepted receipts; national formation derogations/dossier/fees; and treaty, exchange, special-regime and other domain gaps listed in the pack README. The read law's promulgation provisions do not by themselves choose a first taxable period. The CNSS issue heading still predates its decree date. No current-law approval is inferred from the successful fetches or from a source/AI review.

The parent should make F1-F4 repairs, preserve this original review evidence, and request a bounded recheck of the changed candidate. This review cannot be relabeled as a pass for an unexamined later commit.
