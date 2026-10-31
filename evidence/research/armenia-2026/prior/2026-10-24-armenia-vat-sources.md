# Armenia VAT: current computation and form gates

Read 24 October 2026, issue #378, branch `codex/armenia-country-completion`, shared base `532a1568`. Prior status-only goal turn was no progress; this continuation revalidated the clean worktree and fetched origin, then rebuilt the retained VAT method. Known shared ownership-only change remains separate. No new PR or country-content push.

## Evidence actually read

- [Current Armenian Code](https://www.arlis.am/hy/acts/215611/latest), reused actual extracted text with anchored article headings. Targeted status/115-million trigger (59), statutory inclusive 16.67% (63), monthly period (69), recipient-agent liability (70), domestic invoice confirmation (71), exempt-input restriction/July exception (72), subsequent direct/mixed/fixed-asset use (73), risk/account-command refundable balance (74), filing (75). Current Armenian 65(2)(11) confirms Article **39**, not English reproduction's Article 38. Existing actual Armenian source/date and sanctions reading reused. Full Articles 62/64 exception catalogues are not certified.
- [Official English reproduction](https://www.arlis.am/en/acts/231892), actual targeted extracted Articles 37–40, 61, 65–66, 70–71, 74/78, 401–402. Used for ordinary place/time/base, customs and EAEU payment/recovery and agent invoice timing, subject to current Armenian and amendment gates. Its English period and cross-reference errors do not override the current Armenian. Oversized combined Armenian slices were truncated; only inspected targeted passages are represented as read, not collateral full articles.
- [HO-234-N actual law](https://www.arlis.am/hy/acts/226008), actual Articles 11–16 and commencement 31. Article 13 is **Article 72's** government-decision state/community donation input exception, not a change to Article 73's mixed-use calculation. Articles 11/12/14/16 wait until January 2027; do not import the replacement-invoice, no-PE liability and form/payment changes into October 2026.
- [Order 298-N historical 132487](https://www.arlis.am/hy/acts/132487): actual form and metadata show **1 August 2019–1 January 2020** consolidation. Followed incorporation links rather than presenting this as current. `/latest` open failed. Search download results were discovery only, no PDF relied on.
- [Applicable consolidated 298-N, 175524](https://www.arlis.am/hy/acts/175524): actual form, metadata and targeted instructions, applicable from **1 April 2023**. Output/input credit/debit language; rows 7–23 and targeted instructions 14 (agent VAT row 10), 15–17, 21–24, total formulas/signs. Acquisition base is not merely eligible VAT: row 18 includes specified bases even absent a settlement document, while row 20 carries delayed/blocked entitlement adjustments. The printed total-base formula still references repealed row 14; this is flagged, not silently repaired or assigned fictitious activity. Entire excise section not implemented.
- [Order 76-N](https://www.arlis.am/hy/acts/173728), actual amendment and commencement: 1 April 2023; mainly excise row and non-resident name instruction. Its existence does not establish live portal acceptance.
- [Order 1000-N](https://www.arlis.am/hy/acts/231429): actual added receipt-return/exempt/platform fields, row 22 repeal and paragraph 2. **Effective 1 January 2027**, despite September 2026 adoption/publication. Future printed formula/instruction discrepancies were not resolved or encoded for 2026.

Two initial shell metadata attempts failed due to missing `requests`/`bs4`; standard-library HTML parsing then succeeded. No dependencies installed. No PDF downloaded/rendered, private taxpayer data, portal session, accepted filing, actual customs deferral, issued certificate or refund obtained.

## Result and limits

Rebuilt VAT v2.1, retaining original at `c5219ae1` in Git and platform attribution/review/licence/CTA. Removes unsupported fourteen-part return, unknown-country/domestic and unknown-SaaS defaults, bank-only filing and arbitrary statutory-looking review thresholds. Adds current ordinary status, place/time/base, statutory 16.67 versus net 20%, actual invoice confirmation/import payment timing, later use adjustments, separate output and recovery gates, published form and 2027 changes.

Eight conditional controls: ordinary positive/negative difference; statutory inclusive receipt; late domestic confirmation; customs base/later payment; EAEU recovery month; subsequent mixed use; fixed-asset period reversal; recipient-agent timely versus late input. These prove arithmetic under assumptions, not liability, evidence completeness or accepted filing.

README v0.5 keeps all seven domains partial. Thirty-five controls across five methods; payroll/social still lack controls. Five other retained Guides are not verified by this rewrite. Complete exemptions/special bases, all EAEU/export/car/leasing cases, correction/portal/rounding/refund implementation, full-country independent review/fixes and accountant attestation remain open.

Michael authorised one fresh **Montenegro** reviewer during this turn; that separate read-only review is running. This is not authorisation or evidence of an Armenia independent review. No professional label upgrade.

## Checks

Working-tree and exact-commit checks follow below. No full software test suite, generator freshness, remote CI or publication claimed.

Exact content `08ece09e`, base `532a1568`: strict metadata five source Guides, zero errors/warnings/notices; contributor validation 397 Guides/345 generated frontmatters across 876 inherited/new changed paths passes with 47 inherited warning groups; whitespace passes. Required country examples exits 1: 11 Markdown files, 35 controls, zero arithmetic failures, payroll and social missing controls. Fresh in-memory AM coverage: ten Guides, reviewed 0, all seven domains partial/missing, complete:false. No independent Armenia review, remote CI or publication claimed.
