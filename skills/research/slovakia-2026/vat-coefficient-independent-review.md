# Independent Slovakia §50 coefficient delta review

27 October 2026. **PASS for the ordinary mixed-input method where the actual annual included-supplies denominator is positive.** Final Guide SHA-256: **ed89e131b285eb476a96020734d33bbe3ce506a1abf2b386d99cb2fe4691c531**. This is source review of a tier-2 draft, not accountant attestation or whole-country completion.

Baseline: committed restoration checkpoint `169d1855`, Guide SHA `7509ed359239a39aa2e136e9c018a7cdc4b496094021222e21d1a41097198766`. I did not write the integrating author's method or edit the Guide.

## Actual primary review

I rehashed the full official 2026 VAT Act DOM body (`acc5a74c44c5efe077cdcd84dfe42b53c26faf1e95ddb1861767b2f26ff699c6`) before actually rereading §50(1)–(5), with §49(3)–(6). A fresh official-law web open confirmed the 1 January–31 December 2026 version. The statutory extract is `vat50-verified-extract.txt`.

I independently opened and read the actual Financial Administration deduction page, including direct attribution, the coefficient and overseas supplies. The integrating author subsequently supplied the full current HTML; I independently verified its SHA `9d5bd8a293ee66fbb86f6743ba80973ef8857fedc07924d8ee5aa8463d8c0829` and extracted the body myself. The failed local fresh-fetch attempt is retained honestly; the fresh web read and hash-verified HTML are separate receipts. See `verified-source-receipt.json`, `fresh-fs-web-read.json` and `fs-verified-independent-extract.txt`.

Sources: [2026 VAT Act §§49–50](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-50), [Financial Administration deduction guidance](https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/odpocitanie-dane).

## Supported concrete method

1. Attribute eligible inputs to their actual use first. Full-right-only inputs follow the ordinary entitlement rules; exclusively no-credit inputs give no deduction. Apply §50 to the eligible common pool serving both. Applicable private-use and statutory restrictions remain relevant.
2. For positive annual D, N is VAT-exclusive supplies carrying deduction rights; D is VAT-exclusive supplies generally. Supplies outside Slovakia enter according to their actual deduction entitlement. Exclude from both sides the four §50(2) classes: business/independent-part transfers; sales of used business assets except inventory; occasional exempt §39 financial services; occasional property transfers/lettings. The category alone does not exclude ordinary financial/property activity.
3. Calculate `k = ceil(100 × N / D) / 100`; multiply the eligible common input VAT by k. This rounds the coefficient upwards to two decimals. It does not create the old 95%-means-100% rule. Exactly 0.95 remains 0.95; 0.9501 becomes 0.96; 0.9901 becomes 1.00 through ordinary rounding.
4. During the year use the previous year's coefficient. If unavailable, use an activity-based estimate with tax-administrator consent. Recalculate using actual completed-year values and settle the difference from deductions actually taken in the last tax period. Entry/exit part-years follow the same principle. An accounting financial year replaces calendar year for §50(2)–(4).

The old pre-PR737 coefficient section was read directly. Its prior-year and annual-adjustment topics are now concretely covered; its section citations were wrong. Its whole-percent wording is now the precise statutory two-decimal coefficient calculation. Its separate ≥95% full-recovery shortcut has no support in the reread §50 and was not reintroduced. A targeted scan of the full current VAT body found no `0,95`/`95 %` formulation either; this scan supplements rather than replaces the actual §50 read.

## Independent computations

| Case | Independent result |
|---|---|
| N240,000; D360,000; excluded used-asset disposal50,000 | k0.67; the disposal does not inflate either side |
| Common VAT23,000; provisional0.60 | Deducted13,800; final15,410; increase1,610 |
| Separate case: provisional0.67 and actual deductions15,410; final0.61 | Final14,030; reduce1,380 |
| Actual provisional0.60 instead, final0.61 | Increase230; this distinguishes the separate downward-case assumption |
| Exact0.95; common23,000 | Deduction21,850, not23,000 |
| Direct full4,600; direct no-credit input; common2,300 at0.67 | Deduction6,141; direct no-credit input contributes zero |
| Domestic N60,000/D100,000 plus foreign right-bearing30,000 | N90,000/D130,000; k0.70 |
| Domestic N60,000/D100,000 plus foreign no-credit20,000 | N60,000/D120,000; k0.50 |

The exact rational-arithmetic harness also checks rounding just above boundaries, zero numerator with positive denominator, full-right ratio, ordinary versus excluded financial receipts, inventory versus used-business-asset sales and an explicit refusal to assign a value to0/0. These controls substantiate the stated formula; they do not resolve untested specialist combinations.

## Findings fixed and preservation

The integrating author fixed two finite clarity/format findings: the downward example now explicitly changes the provisional assumption to0.67/15,410, and the new source row belongs to the existing table. A final schema correction puts the purpose in Source and actual URL in URL, matching the three-column header. All are closed in the final hash above.

**54 independent assertions pass**, including both unchanged executable examples, raw-source hashes and exact preservation. Original examples independently recompute restaurant output10,080/payable5,480 and consultancy output7,360/input4,485/payable2,875. All current metadata except the intended version2.1→2.2 change, all nine content H2s plus CTA H2, both complete code blocks, contribution line and entire CTA tail are unchanged. Reversing only the inserted method, new source row, intended version and precise reservation replacement reproduces the entire committed baseline byte-for-byte.

The prior broad coefficient reservation is legitimately narrowed to an actual annual zero-denominator case. The other existing reservations on form layout, date-specific ECB input and control-statement first-breach sanctions remain byte-identical. The zero-denominator follow-up is separate in `zero-denominator-research.md`; it does not block this positive-D method closure. No Guide edits, commits or push were performed by this reviewer.
