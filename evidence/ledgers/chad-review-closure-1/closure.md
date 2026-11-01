# Chad review closure 1

**Accepted for the narrow non-wheat listed-goods import-eligibility working paper. Original P1 is closed.** Frozen repaired candidate: `d91f12a172626fb9c4ee9ee69f860dd410856492`. Pinned baseline: `db5bf4ff7d4b078421b4fedd483d9b9b91cd71a6`. This closes the finding in `chad-review-20261101/review.md` for original candidate `0a85c3bd65f4dc30edf9319cf52d04c395a1d305`; the original finding and receipts remain intact.

The separate independent reviewer read the complete repair diff and both additive writer receipts, rechecked the actual finance-law scan on PDF page 78, and reviewed the operative September-order wording already independently downloaded and visually read during the initial review. Source hashes are unchanged. Page 78 reading covers article 65, its complete table, and neighbouring articles 64 and 66. This is not a whole-law review.

## Finding closure

| Check | Result |
|---|---|
| Original missing wheat/origin gate | Closed. Description and opening mandatory hold exclude all wheat, including unknown origin. The table excludes wheat from usable scope. Step 2 holds wheat before any classification; step 3 permits only non-wheat supported lines. Intake asks origin evidence and whether a line is wheat. |
| Source interaction at claim stage | Closed within scope. Filing instructions require origin and interacting-instrument checks. The unresolved finance-law/order interaction stays explicit in Sources. No final 5% wheat liability or speculative hierarchy/delegation conclusion is asserted. |
| Ledger row 6 | Corrected. Literal order product list retained while the wheat hold is explicit. This resolves the initial row 6 blocker by narrowing supported scope. |
| New ledger row 13 | Pass. Actual finance-law article 65 gives the 1 January 2026 start, three-year period, 5% import duty, CEMAC-origin produits du cru condition and HS 10 01 wheat entry. Those conditions appear together in the Guide's explanatory paragraph. This reports the provision and does not decide final liability after the later order. |
| New ledger row 14 | Pass as a Guide workflow restriction. All-wheat hold is deliberately broader than the statute's origin condition and expressly avoids an unsupported legal conclusion. It is not represented as a statutory duty to hold every wheat line. |
| Other product/use conditions and boundaries | Unchanged from initial source review. Supported non-wheat goods remain tied to the September order's wording; unresolved contrary instruments trigger a hold. No domestic-sales exemption, completed customs filing, valuation computation, broad-current-law or whole-country certification is introduced. |

Actual sources: [finance law 2026, article 65, PDF page 78](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=78) and [signed Arrêté 135, articles 1–3](https://ecofinances.gouv.td/wp-content/uploads/2026/09/Arrete-N135-Exoneration-des-droits-et-taxes-sur-les-produits09092026164852.pdf#page=2). No further source research was needed for this exclusion-based repair.

Ledger rows checked across initial review and closure: 14. Two new rows and the revised row 6 were checked in this closure; unchanged original rows retain their scoped initial findings. Fixes made by reviewer: 0. Parent made the repair. Outstanding review defects within the defined non-wheat eligibility job: 0. Lost content restored: 0; no legacy Guide was rewritten or removed.

## Validation and preservation

All 15 `skill_checks.py` checks pass. `check-examples.py --require` checks one file and two oa-check blocks with zero failures or missing blocks. Existing changed-only validator passes for one Guide with zero errors and zero warning groups using the pinned baseline above. `pinned-validation.py` supplies the baseline's changed/add/delete sets to the existing validator functions without moving a Git ref; derived inventory freshness is excluded exactly as in PR mode. Command argv, stdout, stderr, exit codes and all hashes are in `check-results.json`. Reproduce with `python3 evidence/ledgers/chad-review-closure-1/closure-checks.py`.

Guide and ledger hashes match the repair receipt and repaired frozen commit. The six legacy Guides, README, old-topic destination map and both original draft receipts remain byte-identical to the original candidate. Both executable example blocks are byte-identical and recompute. The initial review established all 82 legacy topics preserved; byte equality continues that evidence. No Guide, ledger, original review evidence or writer receipt was edited during closure. Only this new closure folder was added; no commit, push, PR, comment or accountant attestation was made.

Wheat legal treatment remains unresolved and every wheat line stays held. The declared unknown classification, valuation, fees, live filing workflow, current amendments, penalties and wider Chad-pack matters remain unresolved. This acceptance is source review of the defined working paper only.
