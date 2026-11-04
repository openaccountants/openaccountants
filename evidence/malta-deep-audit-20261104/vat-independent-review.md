# Independent review: four Malta VAT corrections

Reviewer: /root/malta_audit_property_residence. Writer: root. Read date: 2026-11-04. Result: PASS for the bounded corrections at the hashes below. This reviewer did not write these four Guides. This does not attest the full pack or resolve disclosed holds.

## Sources and ledger checks

All eleven shared ledger rows were checked for actual applicability rather than assuming every row occurs in each file. Inspected the current cached official VAT Act PDF/text and fetched official subsidiary sources. Checked article 20(2) supplier, taxable-supply and recipient predicates and its non-intervening-establishment proviso. Invoice VAT absence alone is no longer treated as liability proof. Article 21(2) goods-payment rule and article 21(3) customer-liable-supply rule are correctly separated; Fourth Schedule item 6 chargeability precedes the goods payment date. Article 12 threshold and service-liability gates match. The foreign VAT value hold is preserved rather than inventing a universal net exclusion.

Current Act: https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20. Relevant exact short quote, article 21(2): “the fifteenth day of the month following”. Calendar rule article 73(5): “the first working day, other than a Saturday”. Read 2026-11-04.

S.L.406.14 regulation 3 permits the goods quarterly boundary inclusively and looks at the current and previous four quarters; services-only reporting has its separate rule. Exact quote: “does not exceed”. https://legislation.mt/eli/sl/406.14/eng/pdf, read 2026-11-04.

S.L.406.19 regulation 2: 0.6% current rate, old balances payable before 1 September 2022 at 0.33%, confirmed. Exact quote: “zero point six per cent”. https://legislation.mt/eli/sl/406.19/eng/pdf, read 2026-11-04.

S.L.406.12 definition, exclusion, reference/adjustment periods and record retention checked. The EUR1,160 threshold is the specified small-equipment exclusion, not a universal all-assets capitalisation rule. The Guide retains special scope conditions. https://legislation.mt/eli/sl/406.12/eng/pdf, read 2026-11-04.

MTCA registration FAQ, last updated 20 February 2026, page 4: the Article11 administrative electronic-declaration penalty concession is expressly distinguished from statutory dates and future-year applicability remains held. Exact quote: “if submitted electronically by the 22nd of March”. https://mtca.gov.mt/docs/default-source/documents/registrations-and-de-registrations-faqs.pdf?sfvrsn=908511fc_1, read 2026-11-04.

Current holiday source confirms 15 August: https://legislation.mt/eli/cap/252/eng/pdf, Schedule. Exact quote: “15th August Feast of the Assumption”. Read 2026-11-04. Python calendar recomputation confirms 15 February/15 March 2026 are Sundays, 15 August is Saturday followed by Sunday16th, and 10 January is Saturday followed by Sunday11th. Shifted dates 16 February,16 March,17 August and12 January are Mondays. No intervening listed holiday defeats these four results.

The browser fetch of the cited 2025 historical Act timed out. I inspected the cached official historical PDF/text in parent sources/vat-act-20250101 instead: the calendar-2025 SME threshold and declaration rule are present. This is cache verification, not a claim that the live download succeeded.

## Preservation, examples and closure

Compared each Guide against base ab692cc2ef1c6306de9435b63448294d30fc4052 and its ledger old-topic map. All original headings remain, including specialist/refusal sections. Canonical VAT and VAT3 remain compatibility copies, with their topics preserved. Existing prose examples and their disclosed penalty assumptions/holds were not silently removed. Recomputed all eight executable blocks: four Guides, two blocks each, zero failures. Manual arithmetic agrees with tax/rate/deduction assumptions; this does not independently verify a taxpayer's actual classification.

Found malformed source-column pipe delimiters in the first candidate. Writer repaired these without changing legal figures; inspected the corrected table structure. CLOSED.

Remaining explicit holds include authenticated portal fields, particular invoice/performance timing disputes, special product classifications, penalty interpretation before registration, partial exemption and unrecovered wrongly charged foreign VAT valuation. No new named-accountant approval is asserted.

## Accepted file hashes

- `skills/malta/malta-vat-return.md`: `4200092b75ef40b1ee816a2dd0892b317a168b758a70f80a03a805fa253d0a7a`; checked 1 files, 2 oa-check blocks, 0 failures, 0 missing; missing old headings: 0.
- `skills/malta/mt-vat3-quarterly-return-malta.md`: `5e57eaf8fb736042f79a691583ac3c4497b8c8ee5fdb635a0bac821219c8d1e1`; checked 1 files, 2 oa-check blocks, 0 failures, 0 missing; missing old headings: 0.
- `skills/malta/mt-reverse-charge-acquisition-intra.md`: `6777e006930f7d907832cf0e63650b7531423548be21f3d893be90ca4a5ffc65`; checked 1 files, 2 oa-check blocks, 0 failures, 0 missing; missing old headings: 0.
- `skills/malta/mt-reverse-charge-vat-services-received-from.md`: `3e1b71e2983d0214a11d2428e3cfdf8f912db977e185bfc9f29d0a8aa2861a38`; checked 1 files, 2 oa-check blocks, 0 failures, 0 missing; missing old headings: 0.

## Focused YAML closure, 4 November 2026

Strict YAML found an unquoted description containing a colon in mt-reverse-charge-acquisition-intra. Writer quoted the identical description string. Independently decoded the new quoted string, reconstructed the old line and reproduced previous accepted whole-file SHA256 `6777e006930f7d907832cf0e63650b7531423548be21f3d893be90ca4a5ffc65`. No body, date, rule or example changed. Failure is preserved here and in JSON; focused closure PASS. Updated accepted file hash: `1ad2d4ad3dd0a847c19f83e4e5f3d21abcee58f072c866f51a38efd918f323ab`.
