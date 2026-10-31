# Bounded contribution-workflow addition: independent closure

**Accepted at `4f2539df8ac40f8496c1de98488284630c014d11` as an accurate addition to the previously accepted partial draft. No findings.** The whole-pack verdict at `e98e95296a5f61fa4e30745a47a1eee3bdc7997d` remains applicable with this bounded extension. This does not close the SC partial, establish a complete assessable-income formula, authorize merge or claim professional attestation.

Reviewed 28 October 2026. I read the complete diff from e98e9529 and all eight pages of the three supplied official forms, independently checking their PDF byte lengths and SHA256 hashes against `../work/contribution-form-receipts.json` (all match):

| Source | Actual read scope | Verified claims |
|---|---|---|
| [Commencing self-employment Form 366/CF30 (2020)](https://gov.gg/CHttpHandler.ashx?id=101485&p=0) | Both pages | Start/cessation and continuing-employment facts, full/part-time status, first accounting date, 12-month estimate/separate materially different first-part-year estimate; completing the form accepts assessment on estimated profit instead of the maximum; the eventual actual Income Tax figure replaces the estimate, producing a contribution account or refund. |
| [Under-pension-age CF130b (01/26)](https://gov.gg/CHttpHandler.ashx?id=197037&p=0) | All three pages | Relevant-year estimate pending final tax assessment; earnings, occupational pension and other income-source disclosures; beneficial interest in a Guernsey investment company receiving Guernsey rent, with company/shareholding/estimated rent; interim assessment states quarterly payments and payment dates. |
| [Over-pension-age CF130a (01/26)](https://gov.gg/CHttpHandler.ashx?id=197038&p=0) | All three pages | Same assessment/disclosure workflow, separately specifying post-pension-age earnings and Guernsey States' pension. The investment-company rental disclosure appears on page 2 rather than page 3. |

The two new payroll paragraphs and two Sources rows accurately describe these administrative processes. They do not assume every disclosed amount enters the final contribution base. The cross-reference to ordinary business-profit preparation does not import the income-tax personal allowance or decide mixed-class adjustments. Class 3 continues to use Revenue Service's interim/final assessment rather than the Class 1 monthly formula. The existing explicit exclusions for complete Class 2/Class 3 assessable-income, mixed-class/partial periods, contribution allocation and repayment machinery remain unchanged.

Form 366's June/December income-tax payment instructions are genuinely historic. Their explicit rejection for 2026 is consistent with the already independently checked current [Income Tax Law s81(1A)](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=253819). No new contribution payment dates are invented from that form.

This read used the supplied official PDF/text copies with HTTP200 receipts, not a fresh direct download by this reviewer. No additional statutory reconciliation or exhaustive form-link currency search is claimed.

## Integrity and scope

- The complete commit diff changes only the payroll Guide and research log. The payroll change consists of the stated two paragraphs and two Sources rows.
- The README and all other eight Guide blobs match the accepted e98e9529 blobs exactly.
- Payroll frontmatter, protected metadata, dependencies, original wording outside these additions, both `oa-check` blocks, and marker-to-EOF CTA are unchanged.
- Independently reran the nine main Guide controls: **18 blocks, 0 failures, 0 missing**. The addition introduces no executable blocks or numerical contribution formula.
- The original whole-pack `report.md` and `result.json` were left untouched; their hashes are recorded in the companion closure JSON.
- No Guide edits, git mutations, push, public comment or merge were performed by this reviewer. **Lost content restored remains 2** from the original whole-pack review; this addition introduces no loss.

A later change limited to archiving these exact reviews and updating review-status prose/receipts can receive a final administrative blob confirmation. Any further operative change requires its own bounded review.
