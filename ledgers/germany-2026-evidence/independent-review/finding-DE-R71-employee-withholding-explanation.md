# DE-R71: employee example's classV derived-withholding explanation omits 2026 unemployment room

Independent review,29October2026. This is a finite source/cross-Guide finding discovered while actually recomputing the twentieth full-cycle payroll pair, not a country restart or a change to the earlier true certificate-based return algebra.

Current accepted `de-employee-income-tax` LF190 says Jonas72,000/classIII tax7,564 and Mia18,000/classV tax1,850 were worked out with §39b2 for the stated facts, combined9,414, with a few-euro payroll variance qualifier. With the stated full-year statutory insurance, fund2.9%, parent care1.8%, Mia's2026VSP is:
- RV18,000×9.3%=1,674.
- KV/PV18,000×(7%+1.45%+1.8%)=1,845.
- ALV18,000×1.3%=234; there is55 remaining room below the1,900 combined KV/PV/ALV cap.
- VSP=1,674+max(1,845,min(1,900,1,845+234))=3,574.
- Taxable annual amount18,000−1,230−36−3,574=13,160; classV14%minimum floor=1,842. The double-difference branch does not exceed that minimum here.

The incorrect1,850 is obtained if the actual2026ALV room55 is omitted: VSP3,519; taxable13,215;14%floor1,850. Jonas's7,564 and Lena's8,060 remain correct. Annual reference sum is9,406. This is not a few-euro period-rounding assumption: at monthly1,500 for Mia, annual1,842 divides exactly into153.50×12.

Actual sources already read: EStG39b2sentence5no3(e), native8–26 quote `WITHHOLD` (`Ue94e0982f22d5e03`); PAP2026 MVSPHBprinted28; MVSPKVPVprinted27; UP5-6printed30 and MST5-6printed29 (`U04c9d8868081bd75`). Official source URLs are https://www.gesetze-im-internet.de/estg/__39b.html and https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2. We actually read selected native1478–1585/1640–1700 and visually checked27/29/30; the general statute and all prepared quotations were read. Do not label entire40pagealgorithm visually read.

Own exact-Fraction implementation retained as `germany-payroll-PAP-independent-calc.py`: reproduces **all15 supplied official test vectors** (20k/60k/100k acrossI/II/III/V/VI), plus8060/7564/1842. First helper parse typo was corrected before calculation and is recorded in tool history/comment; no source or Guide mutation.

**A recommended, preserving all original examples:** keep the fictional certificates' actual withholding input9,414 and the correctly calculated resulting balance1,910, but remove the false assertion that those certificates/classV1,850 are the result of the stated2026PAP. Label them expressly stipulated certificate amounts and treat the case as reconciliation of actual withholding; retain every original executable block and its input/expected amounts. An optional short separately labelled reference calculation can state9,406 for the specified simple annualPAP assumptions, without changing what was actually stipulated withheld.

**B:** preserve the entire original fixture as an explicitly historical worked case, add the corrected2026computed-reference fixture with9,406/balance1,918 beside it, and update current directions accordingly. This is more copy and duplicates a case unnecessarily; preferA.

Scope: one bad explanatory parenthesis and mechanical version/current/old-topic binding only. Preserve original certificate facts/return algebra and immutable earlier independently reviewed evidence. The earlier reviewer truthfully recomputed return balances against **stipulated certificates**; that earlier scope did not yet independently prove the delegated payroll outputs. Do not retroactively relabel it as proof of the incorrect1,850.
