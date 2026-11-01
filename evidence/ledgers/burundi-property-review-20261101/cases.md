# Independent case recomputation

Frozen Guide `f2ae4ea5b9463c5e959b2e3e44147e49facafbed`. Independently applied the read statutory rules before running the repository arithmetic checker. All amounts are BIF.

| Case | Independent calculation | Decision/conditions | Verdict |
|---|---|---|---|
| 1: title | 61 ares × 50,000 = 3,050,000; statutory maximum gives 3,000,000; separate missed-July-deadline fine = 3,000,000 × 50% = 1,500,000 | July arts. 150–151. Authority-confirmed C and 61 ares assumed, no invented category. Timely 2026 application has no automatic late fine. | Pass |
| 2: wealth tax | Second acquisition 499,000,000 does not reach 500,000,000. Second at equality: 500,000,000 × 5% = 25,000,000. Third at equality: 500,000,000 × 10% = 50,000,000. Difference 25,000,000. | January art. 138(b)–(c) and July 146(b)–(c). Established VAT-exclusive base assumed equal to the proved higher valuation; exact second/third count assumed. No stacking, later-count inference or first/second sub-threshold exemption from other taxes. | Pass |
| 3: mortgage | 12,000,000,000 × 0.5% = 60,000,000. January cap gives 50,000,000. July full replacement gives 60,000,000. Difference 10,000,000. | January art. 140 and July art. 148. Relevant chargeable period assumed established; cross-period determination remains held. Text change governs; no taxpayer election. | Pass |
| 4: construction | 80,000,000 × 1/1,000 = 80,000. Separate unauthorised case: 80,000,000 × 1/1,000 + 1,000,000 = 1,080,000. | January art. 139 / July 147. Validated estimate for ordinary case, authorised expert estimate for unauthorised case. Expert cost is separate; display fine is not automatically added. R2 permit-insurance application hold does not change this bounded tax arithmetic. | Pass |

`check-examples.py --require` separately reports four blocks, zero failures and zero missing. These four results were independently derived with exact decimal arithmetic in cases.json, without using its expression evaluator.
