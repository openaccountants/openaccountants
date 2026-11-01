# Benin property and rental: independent source review

Accepted for the two stated partial working-paper jobs at frozen commit `29102d1f721ee3bd8feaffa01d520e7fe92f6344`. No substantive correction is required. Review/read date: 1 November 2026. Base: `59c23acba2ad66dd2bb29ffc81ffbb9289769ef8`; branch: `codex/benin-property-2026`.

This is a fresh independent AI source review, not an accountant attestation, a live assessment, an authenticated filing, a country-completeness finding or merge/publication approval. All seven Benin domains remain partial. The original writer evidence and earlier review findings remain immutable.

## Exact scope and identities

The review covers `skills/benin/bj-property-tfu.md`, `skills/benin/bj-rental-income-tax.md`, the limited README routing/status changes, and `evidence/ledgers/benin-property-20261101/`. The 17 changed frozen files, including the freeze receipt and committed validation, are individually Git-blob/SHA256 bound in `mechanical-preservation.json`.

| Frozen Guide | SHA256 |
|---|---|
| bj-property-tfu.md | `40cac2bdcacf7ecaf1f70e5deedffade2fd40dccf66956356fa1a1c402114637` |
| bj-rental-income-tax.md | `4124bd25b23cbf3998c1fcbb436ac151588bbee4335e7a77201c2f9883b229a9` |
| README.md | `981b92a3dbda2bb3b4cb706d2cafa4b90418f67187c062e0e8d66f1badb2cb60` |

Read governing parent AGENTS instructions, repository CLAUDE.md, docs/OWNERS.md, docs/GOAL.md and docs/skill-template.md. No subagents were used. The reviewer attempted the prescribed `git fetch origin`; it failed DNS resolution. This does not change the local frozen source-fidelity verdict. Parent reported a successful origin fetch immediately before branching from the stated base and owns final GitHub status reconciliation.

## Primary sources actually read

Cached official PDFs were sufficient; no replacement rule was inferred from search snippets and no new source acquisition was needed. Full PDFs stay outside Git in the sibling sources directory. Hashes/byte lengths were independently checked against actual bytes. CGI text was freshly extracted from the PDF with Poppler, rather than relying only on the writer's text file.

| Official source | Source SHA256 | Independent read scope |
|---|---|---|
| [CGI 2026](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf) | `dcade7868686940c963411c53f60bbb015331c52b90741d785329def7dd7691a` | Full relevant arts51-52,66,101-107,151-165 and neighbouring chapter boundaries on PDF32,37,53-57,73-79; sanctions/cost context on PDF216-217,279. Not the whole CGI. |
| [Law 2025-22, original 2026 finance law](https://budgetbenin.bj/storage/2025/12/Loi-des-finances-2026.pdf) | `ff575a6c6a6425d69f5270168a302f34314ddc971b5f4dd519d18eaa80272264` | Fiscal arts1-17 and final arts47-48 read with adjacent context; signed scans PDF2,4,14 visually confirmed. |
| [Law 2026-10, 24 June rectifying law](https://apisiteweb.impots.bj/media/6adcb8249c4ab_B%C3%A9nin-Loi%20de%20finances%20rectificative%202026.pdf) | `13b0a13816d27940b33eb402f63f8d1f0e6b37fa9dbeb47f36967a1f586b211a` | Fiscal arts1-19, article20's scope and final arts48-49 read; signed scans PDF1,4,17 visually confirmed. Public-domain rental/sale prices are not treated as a private-property TFU valuation instrument. |

## Figures and rules checked: 42

All 22 TFU and 20 rental rows were individually checked for legal meaning, conditions, source-file hash, short French quote and official page locator. The human/JSON ledger pairs agree. `row-verdicts.json` preserves each complete writer row beside the independent reason and locator result; `row-verdicts.md` is the readable 42-row table.

The CGI161(3) anchor crosses PDF77-78, with the printed page footer in between. Reading the continuous sentence confirms the quote and 10 December deadline. The checker initially stopped on that footer; `checker-history.json` preserves the extraction issue and narrow correction. No Guide/ledger rule changed.

The sensitive points checked were:

- **Property category, base and local rate:** CGI152's commercial/industrial-land and commercial/income-producing-light-structure overrides are preserved. CGI157 built rental value is distinct from CGI158 non-built administrative assessment. CGI159's 3%-7% and 4%-8% ranges require the actual local decision. Its 5%/6% defaults are expressly conditional on no rate at Code commencement. The unusual preceding-quinquennium “taux” in CGI158(3) is not silently rewritten into an invented valuation rule.
- **Actual principal-residence exemption:** CGI154 gives taxation in the fourth following year, exclusive owner/family use, principal residence only, once per person, valid letter/permit/title and timely declaration, and the pre-existing-property TFU condition. Changed use ends the remaining relief from the conversion year. It is not a standing exemption for every owner-occupied building.
- **Rent advances and status:** CGI106(4) remits the advance by the 10th following actual payment. CGI106(2)'s exemption belongs to qualifying natural-person tenants. CGI106(1)'s 10% branch is only withholding for IBA/IS landlords, not the individual IRF charging rate.
- **Final withholding and credits:** CGI106(3) says the withholding is final while (5) deducts amounts actually withheld and remitted and (8) offsets instalments. The Guide retains all three provisions. It does not resolve final IBA/IS liability, grant a refund or certify live ORTB settlement. The FCFA11,200 example is accepted only as the explicitly labelled arithmetic reconciliation before instalments. It is not a certified amount to pay. Those boundaries must remain visible.
- **June platform amendment and commencement:** LFR13 actually adds CGI106(9), including Benin property, Beninese/foreign electronic matching operators, the hotel-beneficiary exclusion and platform-owner responsibility. LFR1's prior-year income wording and LFR48-49's repeal/execution clauses do not establish a clean operational first-payment cutover for this new collection duty. The Guide records the enacted text and holds the first withholding period/catch-up for evidence. It does not claim 24 June is that cutover or treat the statutory duty as absent.
- **Original-law overlay:** LF15's cadastral amendment matches consolidated CGI156(4); LF48 expressly commences on 1 January 2026. LF2's listed TFU late-charge relief retains both full payment and landowner IFU conditions. The June fiscal amendments read do not replace CGI151-165 or original LF2. This is a bounded overlay check, not certification of every later instrument.

## Independent cases and mechanical checks

All four examples were recomputed independently with decimal arithmetic and their legal switches were checked, separately from rerunning the repository example engine:

| Case | Independent result | Decision checked |
|---|---|---|
| TFU categories | 72,000 built + 400,000 non-built = 472,000 | Two supported category-specific bases; example local rates are supplied facts. |
| Principal residence/use change | 2023 + 4 = 2027; 2026 full commercial conversion yields 900,000 x 6% = 54,000 | Continued exclusive qualifying residence is exempt in 2026; conversion ends the remaining relief from that year, without invented proration. |
| Adjusted rental base | 2,400,000 + 120,000 - 60,000 = 2,460,000; 12% = 295,200; +4,000 -288,000 = 11,200 | Actual remittance evidence, separate ORTB and instalments, no refund or live payment certification. |
| Advance/status boundary | Advance 900,000; ordinary withholding 108,000; direct exempt tenant 0; IBA/IS withholding 90,000 | 5 May payment remits by 10 June; tenant and landlord switches are different; no platform case assumed. |

Both Guides pass all 15 shape checks, 30 passes in total. Four `oa-check` blocks pass. Changed-Guide validation, strict sync-integrity audit and frozen diff whitespace check pass. Exact commands and output are in `mechanical-preservation.json`.

Validation emits two warnings: the TFU slug has no standard tax-domain token, and rental IRF shares IT-IND with the distinct salary ITS job. These are legitimate distinct jobs explicitly routed in the README. No new platform-written frontmatter field, accountant-review field or platform CTA was added.

## Preservation and routing

All eight pre-existing Guide blobs and all 28 pre-existing evidence blobs equal both the base and frozen candidate byte-for-byte; materialized working files also match. Sparse-checkout-omitted evidence was checked from Git objects. The old README can be reconstructed exactly using only the two declared partial-explanation substitutions and the appended property/rental routing section. Earlier review paragraphs and links are preserved.

Zero old Guide body units were rewritten or reduced. Lost content restored: 0, because this is two new jobs rather than a rewrite. The new old-topics destination record accounts for all eight unchanged existing Guides. The pre-existing 81-topic map and its prior review/closure evidence remain exactly intact. Spot-checks confirm salary-only scope still routes nonsalary property income separately; unsupported family-quotient/CNSS topics remain expressly held; overview still separates property receipts from salary/business/capital; the cross-border Guide still routes rent-platform calculations rather than using dividend/service rates. No old topic is silently treated as newly settled by these additions.

## Holds that remain

Actual 2026 communal decisions and valuation instruments, article157 methodology/application to a live property, specific exemption facts, first-year TFU instalments without prior assessment, disputed title, authenticated filing/payment/receipts, the platform's first operational withholding period and transition, final business-tax/overpayment/ORTB assessment interaction, transaction/registration/lease duties, property-sale gains, treaty/foreign-credit results and later unidentified instruments remain open. Source review does not close these implementation or separate-job gaps. CNSS remains unverified and all seven country domains remain partial.

## Narrow status-only reconciliation allowed

Parent may update only the two new Guides' pending-independent-review sentence and the README's property-addition status text to record this completed independent AI source review, link this evidence and retain the same bounded jobs, holds, all-seven-partial statement, no-accountant-attestation statement and no-authenticated-filing statement. Parent may also update the README's matching IT-IND “pending-review drafts” wording without expanding scope. The earlier eight-Guide review history and all writer/freeze evidence remain historical and unchanged.

No rule, figure, example, source quote, substantive scope or held implementation question is covered by that allowance. Any such edit needs a new frozen identity and a focused independent review. This review itself changes no Guide, ledger, README, queue, commit, branch or GitHub state.
