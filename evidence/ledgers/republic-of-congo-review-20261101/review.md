# Republic of Congo independent full-pack review

Reviewed on 2026-11-01. **Changes required. This is not acceptance.**

This review is bound to published commit `5ca4e55e6d601b99dad0d1b73e3f5d2688e4717a`, branch `codex/republic-of-congo-tax-2026`, against pinned public base `59c23acba2ad66dd2bb29ffc81ffbb9289769ef8`. Scope: eight `skills/republic-of-congo/cg-*.md` Guides, country README, and the writer evidence in `evidence/ledgers/republic-of-congo-draft-20261101/`. PR #1211 and issue #450 are context only; this reviewer has not commented, committed, pushed, merged, or changed production.

## Findings requiring repair

### F01: Carry the widow(er) exception into the family-parts rule

**P2.** `cg-income-tax.md`, line 50, ledger I15, corresponding writer ledger and register.

The row states married/widowed with one child gets 2.5 parts. The same CGI 116B, immediately below the basic table, gives a different result if the supported children were not born of the marriage with the deceased spouse:

> Le veuf qui a, à sa charge, un ou plusieurs enfants non issus de son mariage avec le conjoint décédé est traité comme célibataire ayant à sa charge le même nombre d’enfants.

Source: [initial 2026 Gazette, physical/printed page 65, left column, CGI 116B](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf#page=65). Checked in a newly rendered page from the hash-verified PDF. This is a 116B exception, so the row's referral for special **116C** situations does not cover it. An example with one qualifying child from outside that marriage would otherwise receive 2.5 rather than 2 parts.

Repair: add this condition to I15 and its Guide placement; keep the separate 116C referral. Improve the merged `1child2`/`1child2.5` text while correcting the row. No existing worked case depends on the omitted exception: payroll case 2 expressly uses a married employee with no children.

### F02: Hold the contradictory deferred-depreciation carryforward treatment

**P2.** `cg-corporate-income-tax.md`, line 44, ledger C07, corresponding writer ledger and register; its loss-treatment hold and any dependent route.

The ordinary five-year loss rule and the exclusion of losses from exempt years match CGI 75. But the Guide presents depreciation booked in loss years as ordinary losses without recording the contrary wording in the same enacted replacement:

- CGI 53, Gazette page 41, right column: “Les amortissements régulièrement comptabilisés et réputés différés en période déficitaire, sont déductibles sans limitation de durée.” It also requires their declaration in the depreciation schedule.
- CGI 75, Gazette page 43, right column: “Les amortissements régulièrement comptabilisés en période déficitaire sont assimilés à des déficits ordinaires.” Ordinary losses run through the fifth following financial year.

Source: [initial 2026 Gazette, page 41](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf#page=41), [page 43](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf#page=43). Both were independently extracted and newly rendered, then visually read.

Repair: retain the ordinary five-year loss rule and the exempt-year exclusion, but explicitly hold the interaction of articles 53 and 75 for deferred depreciation. Do not choose unlimited carryforward or ordinary-loss expiry without a controlling reconciliation. The initial-law text itself is internally inconsistent; the later-currentness hold alone does not explain this narrower uncertainty. No worked case uses brought-forward losses or depreciation.

### F03: Link each instrument named in mixed-source authority cells

**P2.** Most clearly `cg-vat-gst.md`, lines 30–31, V01/V02. Several mixed-source labels send the reader to only one of the named instruments.

- V01 labels VAT 17/36B and the 2026 invoice rule, but the only hyperlink goes to the Finance Act. Historical VAT 36B's non-deductibility rule is in the ministry compilation, physical page 309, printed page 324: “Les centimes additionnels à la TVA ne donnent pas droit à déduction.” Add the direct [ministry CGI link](https://www.finances.gouv.cg/sites/default/files/documents/CGI%20Tome%20I.pdf#page=309) beside the Finance Act link.
- V02 labels the calendar and the Finance Act annexes, but the only link goes to the calendar. Add the [Finance Act pages 77–78](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf#page=77) for Annexes 3 and 5. The calendar establishes its displayed 18%/5%/0% rate line, not the enacted tariff lists.

Apply the same repair to mixed-source cells C10 (add calendar), P03 (add prior Gazette), V08 (add calendar), F03 (add national SARL decree), F06 (add ACPCE checklist), and F14 (add Finance Act or a direct clickable route to the owning corporate rule). Keep the existing links too. The cited underlying clauses were read and support the stated limited rules; this finding concerns direct, honest source attribution when a row is fetched by itself. Adjust the relevant writer-ledger links/source references consistently.

### F04: Preserve the constitution-based existence-declaration limit

**P2.** `cg-corporate-income-tax.md`, line 54, ledger C11, corresponding writer ledger and register; formation's C11 route.

C11 gives only CGI 128's 15 days from beginning operations. CGI 86E also applies to the article-2 corporate entities covered by this Guide and requires the declarations:

> dans les trois mois de leur constitution définitive et au plus tard dans les quinze jours du commencement d’activité

Source: [initial 2026 Gazette, page 47, right column, CGI 86E](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf#page=47); compare [CGI 128, page 66](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf#page=66).

A company constituted more than three months before it starts operations cannot rely only on a 15-day clock beginning when trade starts. Repair C11 to retain both statutory conditions and cite 86E alongside 128. Do not silently drop either provision. The current operative portal/form hold remains appropriate.

## Coverage and checks

This was a full source review of **89 grouped records**, not a claim that the pack has only 89 individual legal figures. Every numeric and conditional limb was compared with the relevant complete source pages and neighbouring provisions. All 89 indexed Guide rows and their writer-ledger counterparts were checked. The eight complete Guide bodies were also read, covering repeated narrative, route and worked-example placements. `numeric-placements.json` inventories all **310 body lines containing a digit**, including source-scope text and example variables; this is an occurrence inventory, not a distinct-rule count. Findings above take precedence over any otherwise supported row.

`rule-coverage.json` gives per-record source pages, checked limbs and exact Guide hashes/line placements. All **180 supplied French quote anchors** were context-checked. The independent full-page Poppler locator found 136 contiguously; 44 required reading across two-column ordering or scanned OCR. `quote-locators.json` distinguishes those methods. A text hit was never treated as proof of the remaining limbs.

All **eight official source URLs** were independently fetched with normal curl TLS, without custom impersonation headers, authentication, CAPTCHA handling, or disabled certificate checks. All eight fetched SHA256 hashes exactly match the writer manifest and sibling cache. Python urllib initially received 403 responses from some hosts; a normal browser opened the ACPCE creation checklist, and ordinary curl then fetched all eight sources successfully. No archive route was needed. `reviewer-fetches.json` preserves the initial results and `reviewer-curl-fetches.json` the successful comparisons.

The source pages support the major initial-law changes: IS 28%, the special 25%/28%/33% company rates, IBA 30%, the separate IRCM/IRF/ITS architecture, the fixed XAF 1,200 salary-band item, every remaining salary-band edge, and CGI 81–85's TP requirements. The national 2017 decree does freely fix SARL capital while keeping the XAF 5,000 nominal-share floor. The source's greater-than VAT cash test differs from IS's greater-than-or-equal test. These were checked directly, not inferred from the prior Guides.

All **16 cases** were independently recomputed with Decimal arithmetic separately from the repository example evaluator. They match their expected outputs. `cases.json` records values and legal assumptions. The examples preserve the required qualifications: hypothetical actual retirement amount, proper family evidence, minimum-tax comparisons, legally different cross-border fact patterns, supported TP comparability, cash-boundary conditions, fee versus capital, and VAT centimes on VAT. The three substantive findings do not change these stated example outcomes.

All **73 old topics** were checked against the six immutable old blobs, including **70 bold bullets and three substantive opening paragraphs**. SHA256 and Git blob IDs match the pinned base. There is a destination or an explicit hold for every topic; no old topic disappeared. The family-quotient destination needs F01's condition repair, and the corporate base/existence routes need F02/F04. Detailed per-topic evidence is in `metadata-old-topics.json`.

Independently checked metadata: all eight descriptions are 80–150 words (105–115); frontmatter versions match H1 versions; all are tier 2 / 2026. All six old platform metadata sets and stamped CTA byte sequences are exact. The two additions have no new author/trust/platform fields and no stamped CTA. No accountant attestation was added.

Validation was rerun against this frozen tree with the requested validation dependencies:

- `scripts/skill_checks.py` on the eight Guides: pass.
- `scripts/check-examples.py --require` on the eight Guides: 16 blocks, zero failures or missing cases.
- `scripts/validate-guides.py --changed-only --no-index-check`: eight Guides, zero warning groups.
- `scripts/check-sync-integrity.py --base 59c23acba2ad66dd2bb29ffc81ffbb9289769ef8 --mode audit --strict-metadata`: eight sources, zero errors, warnings or notices.

`validation.json` preserves command arguments, exit codes and complete stdout/stderr. Passing scripts do not resolve the legal findings.

## Holds that must remain

All seven domain entries remain partial. This review does not establish consolidated operative 2026 law, a filing service, a successful submission, sanctions clearance or accountant attestation.

The later 2026 rectifying law remains a currentness hold. A fresh official-source search found the ministry's [23 July 2026 parliamentary adoption report](https://finances.gouv.cg/en/node/4975), but did not establish a promulgated full text reconciling this pack's rules. An adoption report is not substituted for the law. The two source defects F01/F02 were also checked against current official-source search results; no controlling later reconciliation was established.

Keep the four-month CGI 86F versus ACPCE 15 May annual-filing conflict. Additional nearby provisions deserve attention in any later reconciliation: CGI 132 on Gazette page 67 retains category return dates, and the new 461bis on page 72 addresses monthly due dates, including an August exception. Neither was used here to invent a universal filing date or dissolve the hold.

Keep the CNSS conflict: the 2025 Gazette article 9 prints employee 4.55% / employer 20.28%, whereas the 2026 calendar prints combined 24.28%; the 2026 continuity provision does not by itself reconcile them. No live payroll split, caps or remittance assurance is accepted. Keep VAT's historical compilation/amendment-chain qualification and SFEC, threshold, refund and procedure holds.

## Review boundary

The writer and parent own repairs and publication. After fixing the findings, review the changed Guide/ledger/register placements and bind any acceptance to the new exact hashes. This evidence does not accept a future revision automatically. Country issue #450 must remain open, and the pack must retain its explicit unfinished scope.
