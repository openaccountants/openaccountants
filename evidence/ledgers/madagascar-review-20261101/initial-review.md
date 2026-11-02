# Madagascar initial independent pack review, 1 November 2026

**Verdict: REJECT pending four corrections.** Frozen input HEAD: `95f2800a07ece2d1d2c6e7260b474b18e8dce68b`, branch `codex/madagascar-tax-2026`. This is the original independent review, preserved before writer fixes. No Guide bytes were edited by the reviewer. Re-review must close the findings against new hashes.

## Scope and independence

A separate reviewer read the repository's actual `CLAUDE.md` and `docs/skill-template.md`, the eight source Guides, pack README, eight ledgers and old-topic destination map. There is no tracked public `AGENTS.md` in this checkout. The parent supplied the frozen commit, scope and private source locations, without writer reasoning. The reviewer did not spawn agents, publish, push, comment on a PR, alter generated indexes, or expand this into a full-coverage exercise.

112 ledger entries were checked against their source provisions, including the duplicate detail entries, not 112 distinct figures. Counts: formation 5, corporate/business 27, cross-border 10, income tax 26, payroll/social 9, overview 5, transfer pricing 14, TVA 16. The row-level results are in `ledger-row-review.json`. Every quoted fragment was located, allowing whitespace/apostrophe normalization; the code-directory fragment is in the HTML capture, not a `.txt` capture. Quote matching supports identification and is not the substantive legal review by itself.

## Required corrections

| ID | Location at frozen input | Finding and effect | Required fix | Official basis |
|---|---|---|---|---|
| F1 | `skills/madagascar/mg-vat-gst.md:30`, butane/container rates row | `same` inherits the immediately preceding luxury-rice LFR link. That amendment inserts the rice rule and is not the row's source for the existing butane 10% rule. A partial row retrieval therefore cites the wrong instrument. | Put an explicit CDI 06.01.12 link in the butane row. The 10% amount and both tariff codes themselves pass. | [DGI CDI-LFI 2026, 06.01.12](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf); [LFR amendment to 06.01.12](https://www.mef.gov.mg/assets/vendor/ckeditor/plugins/kcfinder/upload/files/2026/lfr/LFR2026%20Ampliation%20SIGNEE%20DATEE.pdf), printed page 24. |
| F2 | `skills/madagascar/mg-vat-gst.md:40`, excess-credit carryforward sentence; ledger entry 7 | The three-year carryforward is presented without its immediate statutory exceptions. Under 06.01.23, mixed taxable/non-taxable businesses must expense residual carryforward credit at year-end. A taxpayer whose assujetti status is withdrawn must also expense the residual year-end credit that is ineligible for refund under 06.01.24. The current statement would allow credits to survive when the same provision ends their carryforward. | State both year-end conditions beside the three-year rule, retaining the ordinary rule for its correct scope; update ledger entry 7 or add distinct condition rows. | [DGI CDI-LFI 2026, 06.01.23](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf), printed page 124. |
| F3 | `skills/madagascar/mg-corporate-income-tax.md:38`, loss sentence; ledger entry 10 | The Guide says losses are limited to the following five exercises. Article 01.01.10 11° says a period of five years. Those are not interchangeable in a Guide that also permits noncalendar and variable-length accounting periods. The ledger itself correctly says five years. | Replace the five-exercise assertion with the statutory five-year period. Keep year-by-year tracking and the qualifying-loss scope. Do not invent a special short/long-period expiry algorithm. | [DGI CDI-LFI 2026, 01.01.10 11°](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf), printed page 18. |
| F4 | `skills/madagascar/mg-transfer-pricing.md:38` audit-response duties and `:42` sanctions; ledger entries 6/7 | The Guide teaches the V-25 response period and V-28 fifteen-day completion notice but presents only the MGA 10m documentary sanction plus generic tax-adjustment/payment sanctions. V-28 expressly points to CDI 20.01.56.8 2°: refusal to supply requested complementary annexes after unsuccessful reminder attracts an additional 5% of the transaction concerned, alongside the 20.01.52 sanction and ex-officio adjustment. Insufficient/no response to the V-28 notice has the same consequence, with statutory cumulation where the original filing and response breaches coexist. This is a consequence of the duty already supplied, not a request to expand the TP job. | Add that bounded post-request sanction with its triggers and cumulation conditions; cite 20.01.56.8 2° and record the added rule in the ledger. | [DGI CDI-LFI 2026, 20.01.56.8 2°](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf), printed page 177; [CPF V-28](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf), printed page 93. |

## What passed

The numerical rates/bands, mandatory business/TVA threshold, IR election boundary, standard and sector minimum amounts, IS gross base and rounding, salary benefit valuations and caps, dependent reduction eligibility, remittance frequencies, service/royalty withholding rate and distinct deadline wording, residence tests, PE day tests, TP size/documentation tests and cited late/default penalties matched the inspected provisions, subject to the four findings above and the pack's declared scope limits.

The LFI 2026 amendment to 01.03.16 confirms the new marginal 25% tranche above MGA 4m. The July LFR amendments were checked directly for cooperative IR, merger-loss authorization, financial-statement annexes, nonresident dividend IR repeal, bank/credit-establishment interest scope and exception, capital-income scope, TVA rice/list/input changes, tax nonpayment sanction and disclosure date. The LFR changes `before 30 June` to `by 30 June`; the Guide preserves the earlier wording for the June 2026 deadline. No later-year entry date is substituted for these tax amendments. Article 22's radio/posted-publication trigger is real; the exact event date remains unproved and is explicitly excluded from transition computations. The last PDF page (PDF page 52, printed page 48) was visually inspected and contains the 16 July 2026 promulgation and certified-copy stamp. The LFI's final commencement provision was also read. The review does not turn a promulgation date into proof of the separate publication event.

All 66 original substantive bullet labels were compared with the destination map, with old body prose also read. Topics are either sourced in the owning Guide or retained as explicit gaps. Especially checked: formation shareholder/nationality/capital/timeline items; old territorial-only resident statement; synthetic 70% base; transport minimum; cooperative and dividend/interest distinctions; old IRSA top band, zero band/minimum and dependent classification; old business-return date; butane/export/exemption/refund/imported-service scope; CNaPS/health/training/cap and quarterly schedule. **Lost content restored: 0.** There is no silently lost old topic to restore. Six rewrites grew, so no greater-than-25% shrink condition is triggered. The original map's pending-review text should be replaced only once this review is closed.

All six existing CTA suffixes are byte-for-byte equal to baseline `db5bf4ff7d4b078421b4fedd483d9b9b91cd71a6`; platform `review_status`, `trust_label`, `license` and `tier` fields are unchanged. The two new Guides do not add platform CTA or platform-only metadata. Slugs are preserved and README routing/partial declarations match the actual limited jobs.

## Arithmetic and machine checks

All 16 `oa-check` blocks were recomputed with zero failures. Results checked: capital MGA1m/100 shares and MGA500k/100 shares; IR MGA16m/balance8m and minimum MGA7m; IRSA MGA953,500 and MGA3,000; payroll withholding MGA120k/net2.82m and semester240k; overview turnover450m and96m; TVA payable800k and credit500k; TP adjusted profits130m and45m; cross-border withholding1m/net9m and gross-up10m/withholding1m/net9m. These examples assume the documented hypothetical inputs; they do not establish social rates, treaty relief or live filing acceptance.

| Check | Result |
|---|---|
| `validate-guides.py --changed-only --no-index-check` | PASS: eight Guides, zero warning groups |
| `check-sync-integrity.py --base db5bf4ff7d4b078421b4fedd483d9b9b91cd71a6 --head 95f2800a07ece2d1d2c6e7260b474b18e8dce68b --strict-metadata` | PASS: eight Guides, zero errors/warnings/notices |
| `check-examples.py` explicit eight source paths, `--require` | PASS: sixteen blocks, zero failures/missing |

Checks used `PYTHONPATH=/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps`. The first unconfigured validator invocation failed because `yaml` was absent; the configured run passed. A subsequent attempt to query validator help executed its default full check (that script has no help parser) and reported stale `index.json` counts and `llms-full.txt`. Generated files were deliberately untouched; the intended scoped validation subsequently passed. No build or generated-index freshness claim is made.

## Sources and limits

Substantively inspected the private DGI CDI/CPF 2026 captures, government Loi 2025-021 LFI 2026 tax amendment/final provisions, signed Loi 2026-004 LFR tax amendment/final provisions, EDBM SARL and legal-form selector captures, CNaPS home FAQ and DGI code directory. All 22 source-capture manifest hashes/byte counts matched. Full captures remain outside the repository; only hashes, existing-ledger identifiers, short findings and review results are stored here. Direct web attempts for the CDI/LFR URLs timed out, so this review used the actual private official captures; no claim of a successful fresh network download is made.

The review did not authenticate filing portals or submit anything. CNaPS contribution rates/caps/calendar, health/training, full non-salary and capital-income procedures, treaty relief, specialist sectors, implementing documentary annexes, authenticated fields and exact LFR publication event stay partial as explicitly stated. No full country-coverage claim, country issue closure, accountant attestation, PR approval or release approval follows from this bounded review.

## Evidence files

- `initial-input-hashes.json`: all frozen Guide, README, ledger, map and instruction-file hashes.
- `ledger-row-review.json`: 112 row-level semantic outcomes.
- `ledger-quote-check.json`: normalized quote location results without a duplicated quote archive.
- `source-hash-check.json`: capture manifest integrity, with no source document bytes.
- `preservation-check.json`: old-topic labels, CTA/metadata comparison and length results.
- `machine-checks.json`: final scoped command outputs.

Writer corrections and closure are pending. Preserve this initial report unchanged.
