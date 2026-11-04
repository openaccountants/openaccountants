# Independent review: seven property and residence corrections

**PASS for the bounded changed claims and executable examples**, read 4 November 2026. Reviewer: independent non-author agent `/root/malta_audit_personal`. No Guide edits were made by this reviewer. Exact candidate and ledger hashes are in `property-independent-review.json`. This is not professional attestation, approval by any named accountant, full-Guide certification or complete Malta coverage.

## Scope and results

| Guide | Changed claim independently checked | Result |
|---|---|---|
| how-to-account-for-rental-income-in-malta | Trading classification alone does not exclude qualifying rental receipts from article31D; separately identified service receipts are not automatically rental receipts. | PASS. [MTCA Article31D note](https://mtca.gov.mt/docs/default-source/documents/mtca-guidance-note-art31d.pdf), paragraph(b), expressly includes both article4(1)(a) and4(1)(e). The candidate keeps VAT, licensing, statutory tenement and unrelated-commercial gates separate. |
| how-to-submit-capital-gain-taxes-in-malta | Undervalue denominator is declared value versus85%of market/real value, not market versus115%of declaration; buyer duty and seller income tax assessment rules remain distinct. | PASS. Cap123article5A(12)(d) and [Cap364article52(1)](https://legislation.mt/eli/cap/364/eng/pdf) independently checked. Other assessment grounds are expressly preserved. |
| mt-capital-gains | Retrieval metadata no longer says securities gains generally escape tax; ordinary single-table boundaries are inclusive of16000/60000; property-company duty denominator excludes current assets other than immovable property, with indirect holdings separate. | PASS. Cap123article5 listed securities; [MTCA2026single table](https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026); Cap364article42(2)(a)-(b). |
| mt-rental-income | Ordinary garages/stores are not automatically taxable just because of their label; designated parking, permanently installed equipment, safes and limited-company-to-Article10 economic-user exclusions are distinct. | PASS. [Cap406FifthSchedulePartTwo1(1)(b)-(e)](https://legislation.mt/eli/cap/406/eng/pdf) independently read. Both added VAT cases state registration and absence/presence of other exclusions. |
| mt-property-transfer-tax-the-sale-immovable | Restoration limb10% versus expressly historical7%proviso for qualifying2015transfers; historical notice condition not promoted into2026relief. | PASS. [Cap123article5A(5)(d)](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c) has10%principal limb and a proviso limited to transfers before1January2016. Candidate assumes no overriding relief; no automatic10%claim for every restored-property sale. |
| mt-global-residence-programme | Corrected15%quotation removes PDF marginal-heading artifact;15%minimum/35%other-income examples conditional on programme facts. | PASS. [S.L.123.148rule5](https://legislation.mt/eli/sl/123.148/eng/pdf) and [S.L.123.160rule5](https://legislation.mt/eli/sl/123.160/eng/pdf) freshly fetched. The actual rate phrase is “rate of fifteen cents (0.15) on every euro”. |
| mt-residence-programmes-for-wealthy-families | Same quotation repair; existing family hypothetical gets executable calculations, without asserting immigration eligibility. | PASS. Same programme rules; ordinary married35%less10550table independently checked. Qualifying-child tables are explicitly excluded in this hypothetical. |

All seven changed-claim ledgers were read. Their15primary table rows and the added executable-example citations are supported within the stated targeted scopes. These are changed-claim ledgers, not replacement full-law coverage ledgers for all unchanged material.

## Computation and preservation

Executed `check-examples.py --require` on the authoritative seven-file inventory: **17 oa-check blocks, zero failures, zero missing**. Read the surrounding hypothetical conditions as well as recomputing arithmetic. The new illustrations yield rent3600; rent/services comparison4050versus3600; undervalue thresholds98600and102000; single taxes600and11600; ordinary garage VAT0versus company letting216; restoration30000versus historical21000; GRP16400and18000; family GRP18500versus ordinary married20950. Existing examples included in the17were also executed.

Required repository changed-file `check_guides` validation: **seven Guides, zero required errors**. The existing shape/source-row warnings in `property-residence-validation.json` remain visible; this review does not describe them as all15shapechecks passing. Whole scoped whitespace diff passes.

Every old heading is retained, allowing only the explicit display-version change, checked against attribution baseline63d81783. All seven old-topic destination tables preserve the old research in the same Guide. Existing held source/form/treaty/immigration branches remain held; no old evidence was deleted.

## Attribution and untouched Guides

The modified GRP Guide no longer carries Michael Spiteri Staines' previous `reviewed_by`/`reviewed_on` approval and is tier2. This correctly prevents a previous human review being carried onto modified text. Historical Git evidence preserves the original attribution. No Michael Cutajar approval is asserted by these fixes.

The separate `mt-nomad-residence-permit.md` and `mt-permanent-residence-programme.md` are **byte-for-byte unchanged from public revision ab692cc2ef1c6306de9435b63448294d30fc4052**. Their original named review evidence is not altered. SHA256 values are recorded in JSON.

## Remaining limits

This review accepts the actual targeted corrections only. Unchanged legacy rates/reliefs, return forms, detailed VAT or treaty questions, prescribed inherited acquisition-base adjustments and immigration conditions outside the fetched scopes are not newly approved. The failed oversized MPRP brochure fetch is not described as a successful read. No full-country completion or accountant attestation should be inferred.
