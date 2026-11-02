# Benin independent closure review, 1 November 2026

**PASS within the stated partial preparation scope.** F1–F3 and all six semantic topic-map corrections are closed at exact repaired HEAD `3a14e7b7bbb9ac80425e046325b0b946e66fb927`. No further repair was identified in those deltas. This is the focused completion of the initial 113-row independent review, not a new whole-country review or accountant attestation.

Initial reviewed candidate: `a61fda399fa613455862d3cc72d5c403cd330ccc`. Original comparison base remains `a7888d0d6c1f7cb0fed13d8d3f6b7e05f1d12297`. The initial failed review and its receipts remain preserved under `benin-review-20261101/`; this closure is a separate directory. Both repair receipts in `benin-repair-1/` were read and independently checked, not accepted solely on their assertions.

## Closed findings

| Finding | Independent closure result |
|---|---|
| F1, description length | All eight descriptions now contain 102–112 words, meet the 80–150 requirement and describe their existing bounded jobs without adding an unsourced rate. All eight frontmatter versions and title versions are 0.2. Apart from description/version, all frontmatter values are identical to the initial candidate. |
| F2, ordinary-interest tax event | `skills/benin/bj-cross-border-withholding.md:30` now includes payment **or** debit/credit accounting entry, including unpaid interest. Base steps at lines 37 and 40 collect the accounting dates and distinguish the tax event from dividend approval and foreign-service expense events. The deadline paragraph at line 46 explicitly reads CGI 85(2) with article 91 and rejects a cash-only calendar. It retains article 91's actual remittance wording instead of inventing a new cash-only trigger or a new statutory deadline. Ledger row 7 now cites 85(1)–(2) and includes the exact French unpaid-sums excerpt. |
| F3, audit turnover definition | `skills/benin/bj-transfer-pricing.md:45` now defines the turnover limb by any tax in any year under audit, including the current year, and warns against selecting one favourable return/year. This matches signed LFR 17's final sentence. The existing two/four-month limits, possible four-month extension and reasoned three-day notice remain intact. Ledger row 10 now records that condition and an exact French excerpt. |
| Six topic-map targets | All six were checked by their actual legacy topic cells: reverse-charge and digital-services topics now point to VAT cross-border points; input VAT to the VAT base; corporate tax base to corporate base; advance payments and the overview annual-return deadline to corporate deadlines. All destination headings exist and contain the relevant operative rule. All 81 original topic cells and treatment/reason cells are unchanged. |

Description counts and content hashes are bound to the reviewed files:

| Guide | Words | SHA-256 prefix |
|---|---:|---|
| Formation | 102 | `54d0ea8a8947` |
| Corporate IS | 105 | `6512023da176` |
| Cross-border withholding | 108 | `44cb59483238` |
| Salary ITS | 105 | `667232b7bb87` |
| Payroll VPS | 105 | `b1f8c33b1121` |
| Overview | 112 | `38fbf678be18` |
| Transfer pricing | 109 | `98eb611a0f7b` |
| VAT | 104 | `5c1f55f07451` |

Full SHA-256 values, receipt hashes, all unchanged initial writer/reviewer record hashes and command results are in `closure-receipt.json`.

## Source confirmation and limited reread

Only the two repaired legal rows were reopened. I independently re-extracted/read the actual downloaded CGI PDF pages 48–50, including arts. 85(2) and 91, and visually read the critical article-85 page and signed LFR page 5 again. The new ledger quotes agree with the actual French text:

- CGI 85(2): « même si les sommes concernées ne sont pas encore payées ».
- LFR 17: « l’une quelconque des années sous contrôle, y compris celle en cours ».

The actual PDF hashes still match the independent successful official-host fetch performed earlier on 1 November 2026 at 10:18:09 UTC:

| Actual official PDF | SHA-256 |
|---|---|
| [DGI CGI 2026](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf) | `dcade7868686940c963411c53f60bbb015331c52b90741d785329def7dd7691a` |
| [Signed LFR 2026-10](https://apisiteweb.impots.bj/media/6adcb8249c4ab_B%C3%A9nin-Loi%20de%20finances%20rectificative%202026.pdf) | `13b0a13816d27940b33eb402f63f8d1f0e6b37fa9dbeb47f36967a1f586b211a` |

This closure used the independently authenticated same-day source captures offline. Ten unchanged sources were not redundantly fetched again; no new freshness claim beyond that prior fetch is made. The other 111 original ledger rows were not re-reviewed because the ledger comparison confirms they did not change and no focused check failed. The count remains 113. The eight description replacements were read as routing/scope text; they do not broaden the legal approval boundary.

## Preservation and validation

- All 16 executable example blocks are byte-identical to the initial candidate and separately pass `check-examples.py --require`: 8 files, 16 blocks, 0 failures, 0 missing. Their initial independent Decimal recomputation remains applicable.
- All six legacy CTA tails and all platform/human metadata are exact. Both new Guides still have no added platform-owned keys. Tier 2 and the absence of accountant attestation remain unchanged.
- Initial writer evidence is byte-identical to the initial frozen commit. Initial reviewer evidence remains in its own committed files, without replacement; its exact hashes are frozen again in the closure receipt. The closure process wrote only this new directory.
- Diff inspection confirms only description/version/title changes in the six other Guides, the stated F2 interest additions in the cross-border Guide, and the F3 turnover-definition addition in TP. Only cross-border ledger row 7 and TP ledger row 10 change among legal ledger rows. The six topic-map corrections change destination cells only.
- All 15 scoped Guide checks pass for all eight files. The validator uses the pinned base above, passes with zero errors and the same one disclosed heuristic warning about cross-border withholding/VPS job classification. Both whitespace checks pass. Full command argv, outputs and exits are retained in `closure-receipt.json`.
- Country README bytes are identical to the initial candidate. All seven domains remain partial. Current CNSS rates, bases, ceilings and deadline are withheld; the earlier unavailable-source issue is not represented as resolved.

No Guide/ledger/map was changed by this closure reviewer. No commit, push, merge, publication, authenticated filing or external message was performed. The original review's residual gaps still apply, including CNSS, threshold instruments, specialist computations, actual treaty entitlements, forms/CbCR details and live submission evidence. The pack passes independent AI review only for its expressly bounded preparation jobs at the repaired hash above.
