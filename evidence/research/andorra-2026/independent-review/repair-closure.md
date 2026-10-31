# Andorra repair closure

27 October 2026. Narrow review of **32d4e3e8c3121fa37fa7648b5343116dacd08cc4 → ce1666a9ef976cb9b42bcbea4a1d9d2adc08efe9**. This checks only the original review findings and repair preservation. It is not a second whole-pack review. The original report.md is unchanged; its request-changes decision remains the historical assessment of the original candidate.

**All four P2 findings and the P3 clarification are closed in the repair commit.** No new issue was found in the repair diff. Publication remains held, and the unresolved IT-IND benchmark is not certified by this closure.

## Finding dispositions

| Finding | Repair location | Disposition and source check |
|---|---|---|
| F1: digitalisation minimum | ad-corporate-income-tax.md:95 | **Closed.** The 2% method remains; EUR 1 million is now the prior-certification threshold rather than a minimum project size. Checked against [IS art.44(2)](https://www.portaljuridicandorra.ad/L2010095). |
| F2: lost resident movable-capital withholding | ad-income-tax.md:74–78 | **Closed and restored.** Ordinary gross withholding, reduction election and changed-estimate procedure, custodian credit, exemptions, quarterly payment, January reporting and the financial/insurance audit-report exception are supplied. Capitalisation is distinguished from a return of capital. Checked against [IRPF arts.50–51](https://www.portaljuridicandorra.ad/L2014005) and [regulation arts.37–39](https://www.portaljuridicandorra.ad/R20231229D). The source table and removed-and-why inventory now agree with the restored body. |
| F3: salaried partners' minimum base | ad-payroll-social.md:52 | **Closed.** The separate article98(4) floor and both dated 2026 wage periods are explicit, and distinguished from the health complement and own-account classification. Checked against [Social Law arts.18,98(4)](https://www.portaljuridicandorra.ad/L2008017) and the two wage circulars already checked in the original review. |
| F4: ordinary CASS-pension relief | ad-income-tax.md:53,179 | **Closed by supplying the method.** The pre-2015 history test, fifteen-year eligibility condition at benefit start, fraction rounding, annual receipt reduction and cap match [IRPF additional provision5 and final provision5](https://www.portaljuridicandorra.ad/L2014005). The broad pension exclusion is removed; the method does not wrongly create a pension 3% expense allowance. |
| P3: employment-credit maintenance period | ad-corporate-income-tax.md:95 | **Closed.** The workforce and enhanced-category maintenance period is now anchored to the year following period close. Checked against [IS art.44(1)](https://www.portaljuridicandorra.ad/L2010095) and [regulation art.33(2)](https://www.portaljuridicandorra.ad/R20231229C). |

These source checks use the retained primary article texts reread for this closure, plus the independent live-source checks documented in the original whole-pack report. Writer conclusions were not used as legal authority. The same portal-consolidation/authentic-text qualifications continue to apply.

## Rule 11 restoration

**Lost content restored: 1**

Evidence: the original income Guide's section5.9 resident investment-withholding topic, absent from candidate32d4e3e8, is now substantively restored at repair lines74–78, with the verified rate/election and supporting reporting method. The repair updates removed-and-why.md to identify that same one topic group. This count concerns lost original content; F3 and F4 are additional ordinary-method corrections, not extra restorations from the original. The original report's “Lost content restored: 0” records the earlier state when the reviewer was prohibited from editing Guides and the writer had not yet repaired F2.

## Preservation and tests

The diff contains only three Guides and the cut inventory: 19 inserted lines and 5 removed lines. There are no changes to the README, other three computational Guides, supporting documents, generated packages or the four supplementary/boundary-control files.

Machine evidence is in **repair-verification.json**. It confirms:

- Worktree Guide/control bytes match the reviewed repair commit.
- All frontmatter bytes, Guide slugs/dependencies/bylines/platform fields and CTA suffix bytes remain unchanged from the original candidate.
- Every oa-check block is byte-exact unchanged by the repair. Each of the six computational Guides still has exactly two blocks; the complete reviewed set still has **20 controls**, including the four moved original and four boundary controls.
- `check-examples.py`: **9 files, 20 blocks, 0 failures, 0 missing**, exit0.
- `validate-guides.py --no-index-check`: **passed**, exit0; 2,263 Guides and 6,122 generated package frontmatter blocks checked. The same repository warning groups remain: 795 missing Sources, 5 stale, 5 jurisdiction exceptions. Index freshness is intentionally excluded by that command; generated files were not edited.
- The original report's SHA-256 is identical before and after this closure.

## Continued exact limitation

README.md is byte-exact unchanged, including this precise entry:

> IT-IND: "The exact 2026 annual dependent-income minimum-wage benchmark after July's wage change remains unconfirmed; the general family-relief method is supplied."

Michael has no DTF clarification to resolve that choice. No weighted or year-end annual comparator is inferred. The pack remains partial and publication remains held under the current instruction. Closing F1–F4 is not a country-complete claim or permission to publish.

No Guide was edited by this reviewer. No commit, push, merge, public message, filing or CLA consent was performed. Only new repair-review files were written beside the original report. `resp.txt` was not read, deleted or staged.
