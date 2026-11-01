# Sierra Leone payroll: focused independent closure

**Source-bound corrections accepted.** PR01–PR04 are closed, and the SC08 wording clarification is accepted. This closes the correction findings from the first payroll review. It does not establish operative 2026 law, full payroll/PAYE coverage, current electronic filing, full-country coverage or accountant attestation.

Accepted working-tree Guide: version **1.1**, SHA-256 `a05a0713c51cf92cd7b438f698833e4fd0157759de0b3a3f373da0dead894ab2`. Prior commit: `48a6568aa0346659987b56f60ab13552f2dc5419`. Exact input hashes, ledger records, source hashes and preserved original-review receipts are recorded in `closure.json`. The writer’s candidate hashes all match. Original review and writer-freeze files are preserved.

| Finding | Closure evidence |
|---|---|
| PR01 | Contractor employment now retains normal work of the establishment and the remaining worker-definition conditions. SC02 matches Act s.2, physical PDF6–7. |
| PR02 | The 10-day change-notice row now covers employer or self-employed person and names the Director-General. SC15 matches Regulations reg.2, PDF4. |
| PR03 | Whole-month invalidity entitlement, no payable contribution and the prior 12-month credit base are explicit. SC10 matches Act s.26, PDF17. |
| PR04 | Act references link to `act2001.pdf`; Regulation 8 references link separately to `Regulations.pdf`, in both the remittance row and base paragraph. |
| SC08 clarification | Accidental mistake OR clerical error plus written inspector instructions is explicit in Guide and ledger; employer-share recovery remains prohibited. |

Actual Act scan pages 6 and 17 and Regulations page 4 were visually re-read. Both original official PDF hashes remain unchanged. The other 24 ledger records are identical to the reviewed freeze. Both preservation artifacts still cover all 10 old payroll topics. Lost content restored: 0.

All 15 shape checks pass, both unchanged examples recompute, PR validation has zero warnings, strict metadata audit of the **working tree** has no errors/warnings/notices, and whitespace checks against both original base and prior candidate pass. Both case prose and calculation blocks are unchanged, retaining their accepted hypothetical legal premises. Full command outputs are in `closure-validation.json`.

The six compared platform fields, additional historical platform keys and entire CTA suffix remain exact. The five other 2025 Guides remain byte-identical to the original base and prior freeze. Description length remains 114 words, with YAML and heading version 1.1. README is unchanged; it describes the pre-closure checkpoint with two drafts, five legacy 2025 Guides and seven partial domains. This later closure supplies the source-review outcome. Current-law and filing holds all remain.

## Exact status reconciliation

Only the following top-level `/status` replacements are authorized, as clerical reconciliation after this acceptance:

- `evidence/ledgers/sierra-leone-payroll-20261101/rules.json`: `Corrected after independent review; focused closure pending` → `source-bound corrections accepted`. Pre-change SHA-256 `23e42b4cd562b4d0802d492ccba8080b2cf3df66bf2ad2bd196194e94507d00c`; expected post-change SHA-256 `1560c5e84de2fa69370c53b3e1dc3cf1d716d0c9c57adf43c97ec020b2e218da`.
- `evidence/ledgers/sierra-leone-payroll-20261101/writer-corrections.json`: `Repairs PR01-PR04 complete; independent focused closure pending` → `source-bound corrections accepted`. Pre-change SHA-256 `08c7b47fa2f1ea74c9ea23848f2b69345328093eaae70dd710bb732c820738ba`; expected post-change SHA-256 `79d8a740851f51cd71680c5edf5b1756f51b62ee55f69ada679714b53225e8a5`.

Every other byte must remain unchanged, including historical candidate hashes. The existing writer-corrections candidate map records the reviewed pre-status inputs; the separate authorization/receipt records post-status hashes. Apply no Guide, README, rule-record, source or professional-review change under this authorization. After applying, record actual hashes and exact status-only diffs in a separate receipt and require agreement with the predicted hashes. See `status-reconciliation-authorization.json`. No status edit was applied by this reviewer.

All original substantive limits in `REVIEW.md`/`review.json` remain. Only new closure evidence was created; no Guide, writer evidence or README was edited, and no commit, push, PR comment, merge or production action was performed.
