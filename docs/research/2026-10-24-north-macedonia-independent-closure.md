# Independent North Macedonia correction closure

Reviewed exact commit: `62006ea5a4a642a77bda9650a9568eccff23ebd5`. Initial review: `39ab9ebefcb5fb54b924372568a70c83faca613a`. Read date: 24 October 2026.

**Ready for a draft PR as a tier 2 source-cited partial pack.** All six initial findings are addressed. No new material finding was identified in the correction. This is AI source/arithmetic review, without accountant sign-off.

## Findings closed

| Finding | Closure |
|---|---|
|MK-R 1|PIT base, intake and XB routing now state the 1 January 2023 taxpayer/predecessor acquisition boundary and chronological FIFO. Independently re-read Gazette 274/2022 transitional arts.21-22, PDF pp.38-39; identical fresh PDF hash confirms source bytes. Property-gift transitional art.24 is also explicitly preserved.|
|MK-R 2|Domestic intermediary reporting by 15 January, UJP assessment by 15 February and payment 15 days after service now have their own route, separate from foreign receipts and general monthly reporting. Re-read PIT 85-a, 91-a, 93(4), 87-88.|
|MK-R 3|PIT 27(7) matching-maturity EURIBOR(FX)/SKIBOR(MKD)+one percentage point deductible-interest fallback is explicit. Corporate/TP independently cites Profit Rulebook art.4 for the borrowing ceiling AND lending-income floor rather than importing PIT. Fresh official rulebook matches SHA-256 `975e0e98c986e69593e5f26887c70c836ff77216b3ccfc734a6a0f5fb8aa11ca`; re-read art.4 pp.2-3.|
|MK-R 4|The administrator change is tied to the July amendment and UJP 13 July notice, earlier self-calculation periods/corrections are kept distinct, and exact commencement/correction transition is explicitly unconfirmed in SC Sources and README. The original unsupported whole-year assignment is removed. This closes the drafting defect; it does not certify the still-unverified operational cutover.|
|MK-R 5|PIT 43-46 own-product category now includes 80% costs, the separate 1, 000, 000 income tests, activity registration by 15 January, other taxable/nontaxable-income qualifications and exceptions, confirmed annual return/ministry verification and end-of-following-year refund. Re-read law pp.15-16. No general exemption-at-source is inferred.|
|MK-R 6|Official net-wage release 23.3.2025.1/11 published 21 January 2026 gives 45, 961 for November 2025. PIT 94(2) explicitly uses 50% of the January-published net wage. Independent Decimal calculation gives 22, 980.50 base and 2, 298.05 at 10%; payment-rounding qualification and distinction from gross contribution reference retained.|

MK-R 4 closes the unsafe undated administration statement through accurate dating and an explicit unresolved boundary. It does **not** certify the exact transition or handling of historical corrections. The SC partial flag now names that remaining issue.

## Added rule and numerical controls

Statute expressly applies the National Bank official middle exchange rate valid on the last day of the month for which contributions are calculated/paid to salary received in foreign currency. The new paragraph accurately distinguishes PIT 93(2) receipt-date foreign-income conversion. It does not apply the salary conversion rule indiscriminately to every contribution category. [Contributions Law art. 14(3)](https://www.ujp.gov.mk/files/attachment/0000/1616/Precisten_tekst_na_ZPZSO_07_2026______________.pdf).

The official net-wage parameter recomputes as **45, 961 × 50% = 22, 980.50**, then **22, 980.50 × 10% = 2, 298.05**. Operational rounding remains qualified. All 14 original `oa-check` blocks are byte-for-byte unchanged from the initial snapshot. Independent Decimal recomputation again matches all 61 stated expected values exactly. Changed schema validation passes for seven Guides with zero warnings.

## Source and integrity checks

All 27 final cited official URLs were independently fetched again into separate closure evidence. All returned HTTP 200; all 13 PDF hashes match the initial independently retrieved statutory copies. The key corrected PIT transitional/assessment/agricultural/interest provisions, Profit Rulebook art. 4, UJP July notice and the added social FX provision were re-read. Full URLs, hashes, retrieval dates and exact correction locations are in `independent-closure.json`.

The five existing computational Guides preserve every platform-owned field and marker-to-EOF CTA tail against main. New TP/XB files contain no added platform-owned fields or hand-stamped CTAs. All three legacy supporting files remain unchanged. No professional-review metadata was added. The country files in local main and newly fetched origin/main are identical, so the preservation result applies to both base states.

The README retains the same four core partial domains:

- **IT-IND:** Business-loss carryforward and cross-category business-loss relief beyond confirmed negative DLD-DB reporting remain unconfirmed.
- **SC:** First-calendar-year professional minimum, part-time/partial-month bases beyond the confirmed mixed work/sickness formula, and exact July lump-sum administration cutover remain unconfirmed.
- **PR:** Part-time/partial-month contribution bases beyond UJP's confirmed mixed work/sickness formula remain unconfirmed.
- **XB:** Standalone migration/deemed-disposal or exit-tax rules and their filing/payment procedure remain unconfirmed.

No absent provision was converted into a zero charge or exemption. Specific gaps continue to block a claim of complete coverage.

## Exact country source tree

Country tree: `a9ce11ab40b25254f13d573d90a17b03cf2b70cb`.

| Country file | Git blob at reviewed commit |
|---|---|
|README.md|`2cddd9ac894c8a1732b4be74063e2c27aaae7c43`|
|mk-company-formation.md|`df4fdda393a42becc18a5ad91ee509752ec476d5`|
|mk-corporate-income-tax.md|`4f5404e848202fa5f1a3aee76e7b7a113d476359`|
|mk-tax-overview.md|`11f4cb142907e8c2608cb58d4a369dae2faefc7a`|
|north-macedonia-cross-border.md|`a9d9ca0c90ea9a82c1e65690a4eae891c68405c8`|
|north-macedonia-income-tax.md|`58d7672758d33f354fbb5ee98a56f851c57eeac7`|
|north-macedonia-payroll.md|`8f1b295476fb49716c131f0ec718094b6d19c9ca`|
|north-macedonia-social-contributions.md|`befe8f01bafa5427ef63c04e0217fed7e55f886a`|
|north-macedonia-tax-optimization.md|`851c724f285041eecf34ed54348e8478c5adfc5a`|
|north-macedonia-transfer-pricing.md|`7727eea1dd8fc62fd03b80ff492932de296b7785`|
|north-macedonia-vat.md|`e4cf169e67307c73640b0d3ec5eac43383e587aa`|

All 11 files match the reviewed commit byte-for-byte. SHA-256 content hashes are also recorded in the JSON. The reviewer made no tracked source edit and no commit.

This exact source is suitable for a **draft** PR with the identified core gaps disclosed. It remains tier 2; issue #413 must not be described as complete or professionally signed off.
