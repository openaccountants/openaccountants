# Andorra source review record, 17 November 2026

This coordinator record preserves the completed independent review for PR [#2141](https://github.com/openaccountants/openaccountants/pull/2141). It adds no tax rule, source read, professional approval or new review requirement.

The original pack was written by Claude. A separate Claude reviewer checked the full candidate `72bdbe740c139f9739d22b2a14f4894bfedcc37d`: all 164 ledger rows (67 formation, 54 overview, 43 transfer pricing), all 236 original nonblank-line destinations and all six worked cases. That review returned five findings. A separate Codex reviewer, neither the pack writer nor the correction author, checked all eight finite correction units and their operative dependencies at `17bbd18c938fb7439b1f9fbd978dd932cc26e87f`: **PASS**, all five findings cleared, no new blocking finding.

The [complete prior full review, independent delta PASS and finite source ledger](https://github.com/openaccountants/openaccountants/pull/2141#issuecomment-6945038262) are preserved together in the public PR discussion. The [original writer evidence index](https://github.com/openaccountants/openaccountants/pull/2141#issuecomment-6927040595) links the three original figure ledgers and old-line maps. The prior full report's SHA256 is `ab6074015bd500f651b09e19f9ea53c102de86bf169bd98bf99ca144f57b9495`; the finite correction ledger's SHA256 is `c628962b069f87b486bc31b6d87ef9d47640841c5ab33186bed6b4c07d075801`.

## Exact reviewed source set

These SHA256 values cover each complete UTF-8 source file, including frontmatter. They were independently checked in the delta report and rechecked after the current-main integration published at `5e5a504e761a86c80ecdcd4009a17addadbcd48c`. That integration changed none of these three blobs; this record changes none of them either.

| Source file | SHA256 |
|---|---|
| `skills/andorra/ad-company-formation.md` | `bf1d282f2f7a93f67437e9d3365111506b309eb51cee1d9845951e4021431615` |
| `skills/andorra/ad-tax-overview.md` | `dbe853de2e420e95200687430881b5eaed85ff12b3ff2e4fdc7461b21589e0ec` |
| `skills/andorra/ad-transfer-pricing.md` | `0d6d9c4c78e9cef63113d8dd183612abc522e1878934c7c2bd56200bca8ce6bb` |

## Finite delta and preservation

The eight units cover the first-year IS payment exception; the director startup CASS base and its multiple-activity, application and sole-member/family conditions; company-law nominal-value and unlawful-gain fine floors; the securities wording; the precise IRPF bonus minimum; and late-filing interest/sanction coordination. The complete report identifies the operative articles and records what was read. These are eight overlapping rule units, not eight distinct numerical figures or a second full-pack source scan.

All six worked blocks and original case inputs remain byte-identical to the fully reviewed candidate. The transfer-pricing file is entirely unchanged by the finite correction. Original topics, refusals, source dates, human names, credits, approval metadata, CTA blocks and calculator quotations were preserved. Earlier legal and arithmetic evidence is reused for the exact unchanged source set; this coordinator record does not claim those checks as new work by its author.

## Preserved limits

The Guides continue to hold, rather than resolve: transfer-pricing Article 16(6) whole-cost versus excess-only practice; formation account-deposit and foreign-investment procedure regulations, notary fees, possible later registry-fee updates and a later payment based on a short prior tax period; and overview wealth/inheritance/gift-tax absence inferred from the Govern list, plusvalua interaction, parish ordinances and the unread ITP statute. No unsupported held rule is promoted to verified usable guidance. Portal consolidations expressly lack official status; the BOPA text governs. No accountant has approved this version.

## Validation evidence

Completed results below bind to the exact source set above, published at `5e5a504e761a86c80ecdcd4009a17addadbcd48c`; they are not a prediction about CI on later commits.

| Check | Observed result |
|---|---|
| Standards and changed-only validation | All standards passed for three Guides; validation: three Guides, zero warning groups |
| Worked examples | Six blocks, zero failures, zero missing; unchanged cases and prior independent recomputations reused |
| Calculator quotations | Every quoted line preserved |
| Actual current-main strict sync | Three Guides, zero errors, warnings or notices, against integrated main `fe4002fa24814fbefee6f5499f7316f2f3c2a690` |
| [Validate Guides](https://github.com/openaccountants/openaccountants/actions/runs/44061977942) | guard-derived-trees, validate and calculator-quotes SUCCESS; figures SUCCESS: 51 rows (17/29/5), zero misses and zero unreadable sources |
| [Sync Integrity](https://github.com/openaccountants/openaccountants/actions/runs/44061977852) | compare and unit-tests SUCCESS |

Later documentation-only changes still require their hosted gates. No workflow or gate is altered by this record. Merge ownership and the fresh no-active-ingestion check remain with the root coordinator.

Recorded by Codex as coordinator; independent source-review attribution belongs to the separate reviewers identified above. Original pack written by Claude. Not reviewed by an accountant.
