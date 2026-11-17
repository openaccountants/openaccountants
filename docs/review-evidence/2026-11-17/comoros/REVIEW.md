# Comoros: source review and finite closeout

17 November 2026. **Independent finite-delta PASS for source candidate `da82ec121b2d7b310ce0939682d4871accd8a5c8`.** The Cameroon closeout reviewer did not write or edit Comoros. This record preserves that verdict and the existing complete review; it is not accountant approval, permission to merge, or proof of ingestion.

## Exact source binding

This audit-record addition changes no Guide bytes from the independently passed source candidate.

| Source | SHA256 |
|---|---|
| `skills/comoros/km-electronic-filing-and-tax-procedure.md` | `c557be17abf6459b8f21dd43a5dcdd6104f4fe4f63bc426a68a9ecde4913fb04` |
| `skills/comoros/km-personal-tax-domicile.md` | `2e578296117c0bec985eb2f685add8e1655f57db56878a322bef240ba3ef1236` |
| `skills/comoros/km-registration-and-tax-clearance.md` | `8935b9046c73d953a3aaf359f6c485c3e6f379ec6e001354322bc2a49a6fa141` |

The original complete separate review at `85a245aefd9dc47e30e01b786f825a207450362b` covered every one of 58 ledger rows, all 193 original nonblank lines, all nine worked cases and the stated amendment/source reads. Its retained report `round-1-85a245aefd9d.md` has SHA256 `af5135011c6dd71e6d4831f2a60e4e233228f911bdedecbfa3484c64f7d0b7ca`. Unchanged work is carried forward rather than reread merely because the commit changes.

The full writer ledgers and old-line maps remain public: [electronic procedure](https://github.com/openaccountants/openaccountants/pull/2140#issuecomment-6926985458), [domicile](https://github.com/openaccountants/openaccountants/pull/2140#issuecomment-6926986092), [registration](https://github.com/openaccountants/openaccountants/pull/2140#issuecomment-6926986819). The full original and finite independent reports are retained in the firm's external evidence archive under `world-resume-2026-11-16/claude-helper/comoros/review/` and `world-nine-2026-11-17/cameroon/`, respectively. The final finite report `COMOROS-INDEPENDENT-DELTA-REVIEW.md` has SHA256 `b90d8ef683859e63af9e715fdde946c8e83b8adbb8c623e677a5cacf81bb69a7`; its machine binding has SHA256 `833349a73b8e62661706624172fb8ed11cefd4c93efd993afe41e6046e0b8c00`.

## Required findings and independent resolution

| Finding | Independent result |
|---|---|
| F1: registration-example saving and lifting of bans | PASS. Removed unsupported claims that registering caps total cost or cancels earlier no-NIF consequences. The example preserves KMF 40,000,000 turnover, 5%, KMF 20,000 and the arithmetic difference KMF 1,980,000, expressly as a bounded prospective comparison rather than remission of liabilities. |
| F2: reassessment month | PASS. L.96's 30-working-day month restored in the rates row and operative paragraph. The existing 10% rate and 50% ceiling remain. This definition is not exported to every payment-interest rule. |
| F3: neighbouring provisional-instalment interest | PASS after an independent dependency finding. L.115 bis states 10% per month and uses “tiers provisionnel”; that article states no 50% ceiling. CGI article 38 describes each instalment as a quarter of prior-year tax. The Guide discloses both wordings and holds the actual instalment/interest-base reconciliation pending tax-authority confirmation. No one-third or quarter-based interest calculation, uncapped assessment or resolution of that tension is approved. |
| F4: failed writer standards transcript | Corrected per-file output inspected: three empty finding objects. The original run passed three paths as one string and failed with FileNotFoundError; presenting that transcript as a pass was wrong. The [public check evidence](https://github.com/openaccountants/openaccountants/pull/2140#issuecomment-6926987641) must explicitly supersede it; the original failed evidence remains archived. |

For the finite delta the independent reviewer hash-verified the retained official [CGI 2023](https://justice.gouv.km/wp-content/uploads/2025/03/comores-cgi-2023.pdf), SHA256 `782515b181d62194f81ea4450130c5edfa05f07c0728c3a032ae0a8900924546`, read operative text and visually checked pages 25, 152, 153 and 155, including neighbouring provisions. The fresh web open timed out; this is a retained-primary-source read, not a new consolidated-law claim.

All nine case blocks remain byte-identical to the complete reviewed head. Domicile is wholly byte-identical. Original topics, case inputs, names, approval fields and non-usable boundaries remain. The two corrected Guides advance 0.4 to 0.5, updated 17 November; earlier source-read dates remain and article 38 is separately dated 17 November.

## Checks and source-helper dispositions

Local checks at exact source candidate `da82ec121b2d7b310ce0939682d4871accd8a5c8`: standards return three empty finding objects; changed-only/no-index validation checks three Guides with zero warnings; examples check nine blocks with zero failures or missing; strict sync audit from the actual PR merge base checks three Guides with zero errors, warnings or notices; calculator quotes are preserved. This source-only candidate is a fast-forward descendant of the original PR head. The hosted compare workflow uses the merge base, so no current-main integration is required. This audit-record-only commit preserves those source hashes. Hosted checks must still pass on the resulting PR head; earlier green checks do not establish that result.

The row helper's retained applicable check covers 14 rows, zero MISS and two UNREADABLE scan rows. These are individually supported, not waived:

- Electronic procedure, FGM 5%: [Finance Law 2025, article 20, printed page 10](https://finances.gouv.km/wp-content/uploads/2024/12/Decret-N%C2%B024-186PR-du-19-decembre-2024-portant-promulgation-loi-N%C2%B024-016PR-Portant-Loi-de-Finances-2025.pdf), original read OCR states “fixé à 5% de la valeur CAF”. The earlier independent reviewer read the OCR but could not independently re-hash the deleted original PDF; the writer-provided hash and that provenance limit remain disclosed.
- Registration, KMF 500,000: [Amending Finance Law 2024, article 10 inserting CGI 42 bis(2), printed page 15](https://finances.gouv.km/wp-content/uploads/2024/12/LOI-DE-FINANCES-RECTIFICATIVES-2024.pdf), original read OCR states “amende fiscale de 500 000 francs”. The retained PDF hash and completed independent read remain applicable.

No figure or its linked authority changed in these rows. The unresolved L.4 ter substitution, unavailable official LF2024/LFR2025, e-filing rollout/platform/provider decisions, domicile/departure interpretation and implementing-order gaps remain non-usable holds. The new instalment-base discrepancy is also an explicit non-usable calculation boundary. No source gap is converted into operative advice.

Only the assigned three Guides and this substantive review record belong to this PR. No source archive, workflow change, platform write, professional attestation, merge or ingestion is performed by this record. Root retains the no-merges-during-ingestion gate and delivery control.

Written by Codex. Not reviewed by an accountant.
