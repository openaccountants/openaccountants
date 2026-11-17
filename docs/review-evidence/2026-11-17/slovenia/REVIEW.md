# Slovenia: independent review record

Independent final-pack result: **PASS**, 17 November 2026, for source commit `77c1b97a8f3d35b99008eb6714842edc48e04862`. The publication branch preserves the accepted Guide bytes. This is a source review record; no accountant approval is represented.

| Accepted source | SHA-256 |
|---|---|
| `skills/slovenia/si-company-formation.md` | `739eb92a14cfc895137d674e9c88f62e5c13a257f46c7112fb2021d88894c67f` |
| `skills/slovenia/si-tax-overview.md` | `7418431f0f55a0b04c23170d046260dec02b5995385917a1632faf80d4e119ab` |
| `skills/slovenia/slovenia-tax-optimization.md` | `f1b8629bd774973a0b95bb58d828976831d2304e7385fd6c64267e48610a407f` |

The separate reviewer read all three final texts, checked all 110 ledger entries (107 operative entries and three explicit non-usable hold entries), all 229 original body-line destinations, six cases and the identities of eight untouched sibling/README files. Both original optimization calculation blocks remain byte-identical. No topic or case input was lost, and protected metadata and human approval fields are unchanged.

Completed full primary-source reviews were reused after one applicability check: [formation, 51 rows](https://github.com/openaccountants/openaccountants/pull/944#issuecomment-6528535418), [overview, 51 rows](https://github.com/openaccountants/openaccountants/pull/928#issuecomment-6527840973), [optimization, 32 rows](https://github.com/openaccountants/openaccountants/pull/933#issuecomment-6527890559), and the overlapping [entry/exit dependency, 37 rows](https://github.com/openaccountants/openaccountants/pull/943#issuecomment-6528272975). These are completed earlier reads, not 171 newly repeated source checks. The final reviewer checked 13 packet evidence hashes and 11 distinct retained native-capture hashes.

The final review checked the changed conditions and their direct dependencies:

- [ZPZR arts. 2-7 and 19-21](https://pisrs.si/api/datoteke/integracije/486867865): entry-only pro-rating, compulsory exit without annualising part-year revenue, zero no-activity years, prior-year insurance classes, the 75% hours test, transfer/entity and related-party conditions, current-year rates, and winter-payment exceptions. The referendum date alone does not enact ZIURS.
- [ZDavP-2 arts. 45 and 308](https://pisrs.si/api/datoteke/integracije/594731150): next-working-day carry, the first-year election deadline and rejection of late elections.
- [ZDR-1 arts. 4 and 13](https://pisrs.si/api/datoteke/integracije/358535670): employment elements, rather than one client alone, determine the civil-contract boundary.
- [ZPIZ-2 art. 145](https://pisrs.si/api/datoteke/integracije/404402718), [ZDOsk-1 arts. 55-56](https://pisrs.si/api/datoteke/integracije/358768794) and [ZDDPO-2 art. 29](https://pisrs.si/api/datoteke/integracije/393614825): the contribution insurance basis, prior-period/monthly base, floor, ceiling and new-insured adjustments; business-purpose conditions for salary; and regime comparison by tax result rather than deduction size alone.
- [ZGD-1](https://pisrs.si/api/datoteke/integracije/612427594), [ZSReg](https://pisrs.si/api/datoteke/integracije/356554736) and the [notarial tariff annex](https://pisrs.si/api/datoteke/integracije/353733416): activity permissions, both five-day routes, distinct founding-fee uplifts, large-company provisions, dual-company/consolidated audit and AJPES timing.

Independent Decimal recomputation confirmed: capital quarter EUR 1,875 and additional EUR 5,625; notarial uplift EUR 76 and fee EUR 171; annual PIT EUR 6,926.38 on the assumed net base; eligible normed tax EUR 2,400; original normed example EUR 17,900; original company example CIT EUR 22,000, dividend tax EUR 19,500, total EUR 41,500 and owner net EUR 58,500. Eligibility, lawful distributability and accounting profit are explicit assumptions; salary, contributions and other taxes are separate.

## Individual figure-check dispositions

The actual initial stock check at `6981145634a8cf56381d79a17ee349fd82d85555` examined 29 linked numeric rows: four MISS and zero UNREADABLE. It was not an all-green result.

| ID | Value | Disposition |
|---|---|---|
| SI-F1 | EUR 25,710.33 | Both writer and independent reviewer read the original [FURS 2026 Word scale](https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Dohodnina/Letna_odmera_dohodnine/Opis/Lestvica_za_leto_2026.docx) native annual-table cell: `25.710,33`. The generic extraction splits adjacent digit runs. Unchanged value confirmed. |
| SI-F2 | EUR 5,551.93 | The same original Word document's general-allowance cells state `5.551,93`. Extraction inserts spaces within the number. Unchanged value confirmed. |
| SI-F3 | 22.1% | Computed total: 15.5 + 6.36 + 0.10 + 0.14 = 22.10. The accepted row explicitly says computed; the components are in [ZPSV arts. 8, 11, 13 and 14](https://pisrs.si/api/datoteke/integracije/356720143). LTC and OZP remain separate. |
| SI-F4 | 16.1% | Computed total: 8.85 + 6.56 + 0.53 + 0.10 + 0.06 = 16.10. The accepted row explicitly says computed; the components are in [ZPSV arts. 8, 11-14](https://pisrs.si/api/datoteke/integracije/356720143). LTC and OZP remain separate. |

The original Word file SHA-256 is `c2b430cd1188d72e3824588c4a3333e4f7f1f7ca004537bbdb16ef6a36d755dd`. Current publication-head diagnostics must be compared with these individual dispositions; this record does not invent a later stock-check result.

## Scope limits and evidence identity

All three non-usable hold entries remain. They cover unconfirmed ZIURS content/effect; formation fines, interest, fee VAT/office extras, signature-certification charges and end-to-end timing; winter-allowance euro/OZP amounts; quantified owner/s.p. contributions, employment fines and whether own contributions can be deducted on top of normed expenses. None was cleared as usable guidance.

Failed CLI fetches remain recorded as failed, not read. The broken old business-income document extraction is not used to resolve own-contribution deductibility. Actual web/native reads and the applicable completed primary reads supply the quoted evidence. No new professional approval was added.

Canonical external evidence identifiers:

| Record | SHA-256 |
|---|---|
| Writer `WRITER-PACKET.json` | `0d6942e500285086d2e3db58c311286de112143007dbd450dfd333e36cd78c3d` |
| Independent `REPORT.md` | `c024a25a1760ab298337bb163c5f40366d26f13c2fdef9e65d6fe531250b00f6` |
| Independent `RECEIPT.json` | `913e7b6656de660192992467f93fc944102fcfc6a6a09ab8297e4730f2f23b48` |
| Independent `ROW-REVIEW.json` | `6dff0b4f8517bbd970bb1a29edb03fae7dea95f2283be3c7a172a3748dfb5327` |
| Independent `REVIEW-MANIFEST.json` | `306ab92365b6a9db315dc5f2a670cefac2763ac63afa8e2a60283527ec4bd9d5` |

Local source checks, six calculation blocks, committed validation, strict sync and calculator-quote checks passed as recorded in the packet. Publication CI and the coordinator's final release decision remain separate.
