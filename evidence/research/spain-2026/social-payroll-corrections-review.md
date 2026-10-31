# Independent correction delta review

27 October 2026. Compared the current working copies of `es-social-contributions.md` and `spain-payroll.md` against this review's frozen9784b7b4 snapshots. Repository HEAD was `eaecc16dc4841390551c11cfef620b67e679a9aa`; these corrections were uncommitted working changes. The exact reviewed file SHA256s and preserved-byte checks are in `delta-results.json`. No source edits, commit, push or attestation by this reviewer. **Both file freezes are released.**

**No remaining finding in the correction delta. SP01,SP02 andSP03 are addressed.**

- SP01 now explicitly supplies the ordinary under25/disability exception, cohabitation/dependence and8,000 income test, adoption/fostering supplement timing, ascendant half-period condition and withholding's own-return exception. These agree with current LIRPF58/59/61 and RIRPF84 already independently fetched/read.
- SP02 preserves the nominal DT1 endpoint and adds RD1415/2004 art8(b)'s preceding-business-day rule: Sunday31May2026 ordinarily becomes Friday29May, with the actual holiday-calendar qualification. The date is historical and is not offered as a fresh election.
- SP03 now correctly states LGSS142.2's prohibition on later employee recovery when the contribution was not deducted at salary payment.
- December special-IT implementation now enumerates the enacted categories, preserves the1December new-process gate, states employer salary on day1/entity benefit from day2, maps the incorporated common-IT amount to60% on days2–20 and75% from day21, retains donation100%, and distinguishes the contribution-qualification exceptions from the39th-week age test. The text explicitly labels the60/75 mapping as statutory application rather than a separately published new table.

The art173.2 issue is handled correctly in the applied prose: it invokes that paragraph for the **childbirth/risk-benefit termination rule**, not as authority to pay a day1 subsidy. The new specific art173.1 payment rule expressly puts full day1 salary on the employer and starts the subsidy the following day. Thus the revised Guide does not reproduce the still-present general “from the start” language in173.2 as a competing day1 payment instruction. The retained prior-risk-benefit route is an eligibility/termination gate, not a second concurrent benefit.

FOGASA's addition remains properly labelled a **matching derived reconstruction**: rounding `2×(40.70+2×1,221/365)` to cents gives94.78; rounding the module first then multiplying gives11,373.60/34,594.70. The prose does not falsely attribute that exact denominator formula to the FAQ and retains the directly published module. The previously spotted “below” reference now correctly reads “above”.

## Verification

`python3 delta-check.py` passes **26 preservation/arithmetic/date controls**. `delta-examples.txt` confirms **four oa-checks,0 failures,0 missing**. New boundary controls cover day1 subsidy zero, day2/day20 at60%, day21 at75%, donation day1 zero/day2 onward100%, cumulative20/21-day amounts and30November versus1December process starts. On BR100, the special non-donation subsidy through day20 is1,140 and through day21 is1,215; donation through day20 is1,900, separately from employer day1 salary.

For both files, the original frontmatter, complete CTA tail, authored nine-H2 structure and both complete oa-check blocks remain **byte-identical** to the frozen review snapshot. Only the reviewed prose/source-record deltas changed. No source body was re-fetched for this delta; the prior20 freshly fetched and hashed primary sources remain the legal evidence.

## Restoration count

The two newly restored safeguards are distinct from the previously confirmed17 families:

1. Explicit ordinary descendant eligibility, specifically the original under25/disability rule, SP01.
2. The original missed-employee-contribution deduction consequence, SP03.

This makes **19 independently confirmed social/payroll restored topic families**. The rest of SP01's expanded adoption/ascendant detail is not counted again; the December implementation, FOGASA reconstruction and historical date refinement are not additional restored families. On the whole-pack reviewer's prior39-family country ledger, adding these two disjoint restorations gives **41**, provided that ledger has not already counted SP01/SP03.

The previous report's real RETA monetary/equality conflicts and separately bounded cessation-IPREM/specialist/factual routes remain open. They were not changed or silently resolved by these corrections. The former December special-IT implementation item can be removed from the remaining-implementation ledger for this checked route.
