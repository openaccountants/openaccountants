# Malta VAT and inventory audit, 4 November 2026

Repository: openaccountants/openaccountants, commit ab692cc2ef1c6306de9435b63448294d30fc4052. Scope: all four Malta VAT Guides, the Malta README, attribution inventory and mechanical checks of all 34 Guides (32 country Guides plus two orchestrators). This is source research, not accountant approval or a zero-error certificate. No live approval records were inspected successfully.

## Primary sources actually read

| ID | Source | Provisions / evidence | Read |
|---|---|---|---|
| V1 | https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20 | Cap406: arts10–13,17,19–25,27–30A,37–42,48,73; Third/Fourth/Fifth/Sixth/Eighth/Tenth/Eleventh/Fourteenth Schedules, targeted relevant paragraphs. Cached PDF SHA256 fe036f10c433944b0a2fdb4806dc288c6afaea1749fb42a67a2fd208bb17504f. | 2026-11-04 |
| V2 | https://legislation.mt/eli/sl/406.14/eng/pdf | Recapitulative statements, reg3, monthly/quarterly threshold and dates. | 2026-11-04 |
| V3 | https://legislation.mt/eli/sl/406.12/eng/pdf | Capital goods definition, exclusions, adjustment periods and records. | 2026-11-04 |
| V4 | https://legislation.mt/eli/sl/406.19/eng/pdf | Interest reg2, 0.6%; earlier balances before September2022 remain0.33%. | 2026-11-04 |
| V5 | https://mtca.gov.mt/docs/default-source/documents/registrations-and-de-registrations-faqs.pdf?sfvrsn=908511fc_1 | Updated20Feb2026; goods/services distinction, registration and practical filing concessions. This FAQ expressly is not an art75 statutory guideline. | 2026-11-04 |
| V6 | https://mtca.gov.mt/personal-tax/self-employed/vat-return-cycle | Current operational authorisation and filing page. | 2026-11-04 |
| V7 | https://mtca.gov.mt/business-tax/vat1/vat-compliance/vat-rates/vat-rates | Official rate summary. | 2026-11-04 |

## Confirmed defects / incomplete routing

### V-A [P1] One Article12 payment date incorrectly covers both goods and services

malta-vat-return.md:211 and mt-vat3-quarterly-return-malta.md:212 put all Article12 VAT/notice on the second-month invoice/receipt date. Intra-community acquisitions are payable under art20(1), art21(2): the15th of the month after chargeability. Art21(3)'s second-month rule applies to art20(2) customer-liable supplies. Ordinary EU goods acquisitions and reverse-charged services need separate rows. The detailed acquisition Guide admits it never established the Article12 due date (lines75,93,109); it does not cure this wrong generic date.

### V-B [P1] Foreign purchases are routed by invoice VAT instead of legal place/supply/liability

Both return Guides' step4 (malta-vat-return:49; VAT3:50) treats no VAT plus non-established supplier as enough to impose Malta reverse charge. V1 art20(2) first requires a taxable supply taking place in Malta, the supplier registration/establishment tests and the specified recipient. Hotel or event admission abroad and exempt services defeat the blanket rule. Foreign goods can be an acquisition or import with different rules. The detailed services Guide correctly recognises these exceptions.

The reverse-charge section also says foreign VAT means the supplier has not used reverse charge and discusses only a foreign refund. Wrongly charged foreign VAT does not discharge Maltese customer liability. The detailed services Guide:139,161 expressly says correct foreign VAT and still account for Malta VAT. Those instructions must be consistent; do not force automatic self-charge on every foreign invoice or omit it merely because the invoice includes VAT.

### V-C [P2] Actual example dates omit statutory weekend/holiday shift

V1 art73(5): a date on Saturday/Sunday/national day/public holiday moves to the first working day other than Saturday. Services Guide:150 says VAT1800 due15August2026 (Saturday and public holiday), but actual shifted date is17August2026. Lines154,156–157 use15March2026 (Sunday); actual16March. Both return Guides' historical2025 paragraph says15February2026 (Sunday), actual16February. The simple May15/May22 example remains correct. Do not extrapolate a new electronic grace deadline without applying the actual statutory date and checking the calendar.

### V-D [P2] Acquisition Guide overstates every EU service as Article12 trigger

mt-reverse-charge-acquisition-intra.md:23–27 and step2: any service acquisition, even once, triggers registration unless already Article10. V1 art12(3) limits this to services for which the recipient is liable under20(2); V5 gives the place/taxability/non-established-and-not-Article10 conditions explicitly. A hotel abroad does not trigger Malta reverse charge simply because the customer is a Maltese business. No monetary threshold for a taxable general-rule service is correct, but the missing legal predicates are material.

### V-E [P2] Acquisition Guide changes the quarterly statement boundary

mt-reverse-charge-acquisition-intra.md:73 says quarterly goods supplies must be less than50000. V2 reg3(2) allows does-not-exceed50000 for the quarter concerned and each previous four quarters. Exactly50000 qualifies if the other conditions hold. Its home-page citation is not a stable provision reference; point to V2.

### V-F [P2, retrieval] Conflicting description and scope

malta-vat-return.md:3 excludes Article12 and makes workflow-base/Directive dependencies mandatory, but body16 includes Article12. A retrieval/router using metadata can refuse a covered job or load an incompatible workflow. VAT3 description is Article10-only while its body largely duplicates the broader Guide. This is a checked internal routing defect independent of tax interpretation.

## Source/admin difference, not a wrongly stated statutory deadline

The return Guides state Article11 statutory declaration15February plus seven-day electronic penalty relief. V1 SixthSchedulePartOne5(5) and42(1)(d) support that baseline. V5 updated FAQ additionally states no administrative penalty for an electronic declaration by22March. Preserve statutory-versus-administrative distinction; do not call statutory15February itself wrong or silently replace it with a new legal date. Annual concessions require clear scope/year. Full operational2026 portal field mapping remains unverified.

## Rules substantively checked without a defect found in the stated narrow scope

This list is not approval of every application or every product CN code.

- V1 arts12/13 and ThirdSchedule: Article12 goods10000 trigger, no recovery under ordinaryArticle12; Article10/12 MT prefix, Article11 noMT, Article11A EX.
- V1 SixthSchedule: domestic35000, Union100000, preceding-calendar entry/current-calendar continuation;12wholemonth Article10 lock with no-input-credit exception; proportionate related-owner turnover over10%; capital-asset disposal excluded. Broader SME definitions and exemption cases still require the actual applicant facts.
- V1 art19/EighthSchedule:18/12/7/5 headline rates and listed service categories compared; each CN classification and special exemption was not tested with product evidence.
- V1 art22/TenthSchedule: deductible-use condition; declare reverse-charge output before claiming deduction; listed blocks and exceptions; private-use apportionment; partial-exemption provisional/definitive ratio and de-minimis strictly below20permonth; cash-accounting invoice condition; credit-note period.
- V3:1160 small-equipment/working-tool/furniture exclusion;5/20year periods; delayed first-use adjustment start; record retention. Do not infer that every asset has a universal1160cap or that VAT inclusion is resolved.
- V1 arts27/21/42:15thsecondmonth Article10 baseline, separate penalty/interest grace conditions. VAT3 step8 wrongly conflates payment with penalty relief; its own table distinguishes them.
- V1 arts37–42:20%statement penalties,10%voluntary correction before assessment, late-return250cap and low-tax specialcap, Article12 registration250/20%caps, late declaration120cap; no assertion the statutory monthly-language interpretation is settled beyond the Guide's own disclosed reading.
- V4 interest:0.6% and older0.33% balances; V1 art24 refund5months and verification extension up to12months; requested-document failure exception to refund interest remains a condition not carried in every summary.
- V2 recapitulative defaultmonthly/servicequarterly/goods50000 tests; V1 FourteenthSchedule UnionOSSquarterly monthend/10year record rule and10000 destination threshold. No actual OSS declaration/consumer location evidence validated.
- V1 record6year rule, late-return/correction restart and capital adjustment retention; actual electronic-storage compliance not inspected.

## Examples and duplication

Manually recomputed both duplicated return sets:10000*.18=1800,2000*.18=360,balance1440; software1000*.18=180; late5000:monthly50,3periods150;monthlyinterest30,3periods90. These use the Guide's disclosed monthly penalty reading. Services:4000*.18=720each/output-input0;600*.18=108;10000*.18=1800;2000*.18=360;4registrationmonths*20=80;2interestmonths*2.16=4.32; conditional2noticeperiods*10=20. Arithmetic passes, but the operative due dates and transaction classification remain necessary. No embedded executable blocks in the four VAT Guides.

vat-duplicates.diff shows near-total duplication between the return Guides. Retain malta-vat-return as canonical after fixes and retire VAT3 with an alias and full moved/not-moved map. Fold Article12 acquisitions/service distinctions into that core, retaining a genuinely distinct services specialist section only if it earns its separate maintenance cost. Preserve archived research and URLs; repository deletion alone does not unpublish the platform.

## Whole-pack mechanical/attribution results

inventory.json pins34Guide hashes:32countryGuides plus2orchestrators, excluding README. All34have some current-standard mechanical gaps; these are format/evidence gaps, not34proven legal failures. mechanical-audit.json records each result. Existing examples:18oa-checkblocks across the pack, zero arithmetic failures. --require flags five taxfiles without machine examples (payroll,SSC,bothreturnGuides,servicesreversecharge). The checker scans35paths includingREADME; it does not prove everyfile has anexample.

Ten countryGuides carry reviewed_byMichaelCutajar/tier1;16countryGuides mention his name somewhere. Three programmeGuides nameMichaelSpiteriStaines: preserve his attribution absent a separate authorised change. The live connector returnedUNAUTHORIZED; browser signed intoGuest, not an accountant/admin. No live approval or authorship change is claimed. Git history remains the original contribution record.

## Limits

This pass read the four files and checked the material VAT provisions above, not every statutory exception, every historical version, authenticated portal, CNcode or fact scenario. The Act PDF is current as fetched and prints amendments throughActIII/LN75of2026; a complete separateGazette negative search for every lateramendment was not performed. Treat this as an actionable defect audit, not certification of zero mistakes or comprehensivecountrycoverage.
