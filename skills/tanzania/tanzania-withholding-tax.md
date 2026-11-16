---
name: tanzania-withholding-tax
description: >
  Compute 2026 Tanzania income withholding by payer, recipient and payment head; reconcile finality, date-specific amendments, certificates, treaty evidence and supported royalty subtype conditions.
jurisdiction: TZ
category: withholding
type: computation
tax_year: 2026
last_updated: 2026-11-16
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
version: 2.0
---

# Tanzania income withholding tax v2.0

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

### Quick reference

Compute 2026 Tanzania income withholding at source on supported investment, service, goods and other specified payments. Identify payer/payee residence, legal character, source, PE, exemption and payment date before choosing the rate. Standard income-WHT payment and statement deadline is 7 days after month-end; VAT withholding is separate. This version is research material, not accountant approval.

## Ask the client first

- Payment date, contract/invoice, gross or net-of-tax terms, VAT and reimbursement components.
- Payer/payee residence and legal form, source of payment and domestic PE connection.
- Exact payment character, including royalty subtype, extractive technical service, construction split, agent role and licence/status.
- Dividend listing/share holding/voting evidence; recipient business/nonbusiness facts for finality.
- Actual exemption instrument, loan/bond/zone conditions, and in-force treaty/article, residence, beneficial ownership and anti-abuse evidence.
- Prior deductions, returns, receipts, certificates and any arrears or deemed-distribution determination.

## Rates, bands and thresholds

| Item | Figure / rule and complete conditions | Official source |
|---|---|---|
| General dividend | 10% resident/nonresident (in words on the page), subject to source, payer and exemption rules. Do not say only resident individuals can receive final dividend withholding: ss 54/111 govern finality. | [ss 54,105,111; First Schedule 4(b)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| DSE-listed corporation dividend | 5% resident/nonresident (in words on the page). Establish the distributing corporation is listed. | [First Schedule 4(b)(i)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| Resident corporate holding recipient | 5% only where BOTH payer and recipient are resident corporations and recipient holds at least 25% shares AND controls at least 25% votes, directly or indirectly (numbers in words on the page). A nonresident holding company does not obtain this domestic concession merely by ownership. | [s 54(2); First Schedule 4(b)(i)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| Interest | 10% resident/nonresident (in words on the page) where s 105 applies, subject to its exceptions and actual exemption. Resident deposit interest is final only for s 111 qualifying resident individuals, excluding business/other statutory exceptions; not all resident interest is final. | [ss 105,111(1)(b); First Schedule 4(b)(ii)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| Rent: land/building, aircraft, construction equipment, hired vehicle | 10% (in words on the page) where within s 105. Construction equipment/machinery was brought into resident withholding by 2024 s 39; hired motor vehicles from 1 July 2025 by 2025 s 55. Resident land/building rent finality differs from commercial vehicle-hire business rent. | [s 55; ITA 105/111/First Schedule 4(b)(ii); FA 2024 s 39](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2025.pdf); [ss 105/111, First Schedule 4(b)](https://elibrary.osg.go.tz/bitstreams/d8e39776-4616-4386-bd1c-8ce8eb2caa3c/download); [s 39 construction equipment](https://www.tra.go.tz/images/uploads/acts/Finance_Act_2024_%281%29.pdf) |
| Other asset rent | Resident rent outside listed s 105(2)(d) asset exceptions is excluded from that withholding obligation, rather than universally tax-free. Nonresident rent 10% under First Schedule. Equipment lease must first be classified as rent or royalty; statutory definitions control. TRA aircraft/other-asset 15% cells conflict with the rent clause; do not choose a rate from the label alone. | [ss 3 and 105(2)(d); First Schedule 4(b)(ii)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf)  [official OSG Act, ss 3 and 105; First Schedule 4(b)(ii)](https://elibrary.osg.go.tz/bitstreams/d8e39776-4616-4386-bd1c-8ce8eb2caa3c/download) |
| General royalty / natural resource payment | 15% resident/nonresident where s 105 applies (in words on the page), excluding an actually applicable special royalty head. Royalty includes intangible rights/know-how and specified equipment/media; natural-resource payment is separately defined. TRA generic royalty 10% does not establish the general statutory rate. | [s 3;105; First Schedule 4(b)other payments](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| Special film/media and resident sports royalties | Cinematography film, videotape, sound-recording or like-medium royalty within definition(c) remains 10% after 1 July 2026. The official 2025 supplement has 4(b)(iii)sports/Tanzania Football Federation 5%,(iv)film 10%,(v)other 15%; FA 2026 s 27(c) deletes(iii), renames(iv)/(v)to(iii)/(iv). Thus film 10% survives and the sports-specific 5% is removed; test actual subtype/source/exemption/treaty and general 15% where no special head applies. Rates in words on law pages. | [s 27(c); FA 2024 s 46(b); ITA First Schedule 4(b)](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2026.pdf); [First Schedule 4(b) before 2026 deletion](https://elibrary.osg.go.tz/bitstreams/d8e39776-4616-4386-bd1c-8ce8eb2caa3c/download) |
| Professional service fee | 5% resident;15% nonresident (rates in words on the page) for a United-Republic-source service fee, subject to 106 scope/exemptions. Professional services include the statutory independent-service categories, not only a person with a licence. Not every ordinary domestic goods payment is a service. | [s 106(1)(c),(4); First Schedule 4(c)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| Resident extractive technical/management fee | 10% from 1 July 2025, final where 106(1)(a)/111(1)(d) applies: resident extractive mining/oil/gas payer, resident provider, services wholly and exclusively for that business. Nonresident service fees generally 15%, with finality depending on domestic PE connection. Do not guess general 5% when sector is unresolved. | [s 60(e)(i); ITA 106(1)(a),111](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2025.pdf); [ss 106(1)(a)/111](https://elibrary.osg.go.tz/bitstreams/d8e39776-4616-4386-bd1c-8ce8eb2caa3c/download) |
| Construction professional-service allocation | Where 106(1)(c)(ii) service involves construction, split payment 3:2 materials/services; apply resident professional withholding to the service component. Do not mistake this for the separate VAT mixed-supply rule. | [s 106(4)proviso](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| Non-full-time director fees | 15% resident/nonresident; non-final per TRA PAYE guidance. Full-time service directors follow employment PAYE; do not apply flat director-fee withholding to all salaries. | [Directors other than full time service directors; ITA Sch 4(a)](https://www.tra.go.tz/page/pay-as-you-earn) |
| Nonresident insurance premium | 10% from 1 July 2025 on s 106(1)(b) Tanzania-source premium; final if qualifying nonresident payment not through domestic PE. No general resident-premium withholding under this head is not a promise of overall tax exemption. | [s 60(e)(ii); ITA 106/111](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2025.pdf); [ss 106(1)(b)/111](https://elibrary.osg.go.tz/bitstreams/d8e39776-4616-4386-bd1c-8ce8eb2caa3c/download) |
| Money-transfer, bank-agent, digital-payment-agent commissions | 10% under 106(1)(d), with resident finality under 111(1)(d). Identify actual agent/payment; do not apply this to every customer transfer or bank charge. | [ss 106(1)(d),111; First Schedule 4(c)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| Gaming advertisement/promotion commission | 10% from 1 July 2025 for added 106(1)(d)(iv), subject to actual scope/finality. Ordinary gambling stakes/prizes are not automatically this commission. | [ss 56(a),60(e)(iii)](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2025.pdf) |
| Resident digital-content creator | 5% withheld by resident or nonresident payer under 2024 s 41/46. This was introduced by the recovered 2024 Act, not the old claimed 2023 introduction. Confirm recipient residence and actual content payment. | [FA 2024 ss 41,46; published 83B; current Schedule 4(c)(ix)](https://www.tra.go.tz/images/uploads/acts/Finance_Act_2024_%281%29.pdf); [s 60(e)(iv) renumbering](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2025.pdf); [published digital provision and Schedule 4(c)](https://elibrary.osg.go.tz/bitstreams/d8e39776-4616-4386-bd1c-8ce8eb2caa3c/download) |
| Resident digital-asset owner | 3% withheld by resident/nonresident platform owner or facilitator paying resident person on exchange/transfer. Statutory payment is gross fair market value received/receivable at exchange/transfer; not automatically platform fee or taxable profit. Do not extend this provision to a nonresident payee without another basis. | [FA 2024 ss 41,46; published 83C; current Schedule 4(c)(x)](https://www.tra.go.tz/images/uploads/acts/Finance_Act_2024_%281%29.pdf); [s 60(e)(iv) renumbering](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2025.pdf); [published digital provision and Schedule 4(c)](https://elibrary.osg.go.tz/bitstreams/d8e39776-4616-4386-bd1c-8ce8eb2caa3c/download) |
| Government-financed goods payer | 2% (in words on the page) on goods from resident business supplier where payer is a resident corporation wholly/substantially government-budget financed under 107. Not a universal 2% on all private purchases or all nonresident suppliers. | [s 107; First Schedule 4(c)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| Specified mineral purchases | 2% for statutory covered minerals supplied by primary-licence holder/artisanal miner;2024 extends industrial/other metallic minerals and 2025 removes salt exclusion. Finality under 2024 s 42 is for an INDIVIDUAL holder/miner; do not assert all mineral corporate receipts or any nonresident sale has this treatment. | [ss 40,42,46(c); FA 2025 s 56(b)](https://www.tra.go.tz/images/uploads/acts/Finance_Act_2024_%281%29.pdf); [s 56(b) salt-exclusion removal](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2025.pdf) |
| Verified carbon reduction | 10% on covered resident carbon-reduction payment. Finality under 2024 s 42 for local authority, local community or resident individual; do not automatically extend it to every resident corporation/nonresident recipient. | [s 106(1)(g), First Schedule 4(c); FA 2024 ss 40-42](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf); [ss 40-42 carbon/finality](https://www.tra.go.tz/images/uploads/acts/Finance_Act_2024_%281%29.pdf); [s 106(1)(g) current identity](https://elibrary.osg.go.tz/bitstreams/d8e39776-4616-4386-bd1c-8ce8eb2caa3c/download) |
| Deemed undistributed profits | 33A is Commissioner determination, not automatic dividend every year. Old 30% deemed share introduced 2025 becomes 15% from 1 July 2026, after 12 months from year-end, with 96(6) and new listed/financial/insurance/framework-mining exceptions. Apply the actually applicable dividend withholding rate, not necessarily 10% for every recipient. Later actual distribution is relieved only for the amount already deemed. Figures in words on law pages. | [s 22; FA 2025 s 49; ITA 33A](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2026.pdf); [s 49 original 33A](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2025.pdf); [s 33A context](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| Income WHT deadlines/certificates | Payment AND monthly statement within 7 days after month-end; ordinary WHT certificate covers month and is served within 30 days after month-end. PAYE certificate instead by 30 January or within 30 days cessation. Figures 7/30 in words on law page. Do not substitute VAT withholding 10 day deadline. | [ss 109-110](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| Failure to withhold | Agent must pay the tax notwithstanding failure; payer/payee joint/several rules and agent recovery in 109 apply. Do not recover statutory interest from payee as if it were the withheld tax; obtain actual arrears allocation and legal review. | [s 109(3)-(6); TAA 87](https://elibrary.osg.go.tz/bitstreams/d8e39776-4616-4386-bd1c-8ce8eb2caa3c/download); [s 87 separate interest](https://www.tra.go.tz/images/uploads/acts/Tax_Administration_Act.pdf) |
| TAA penalty and currency point | s 89 monthly/part penalty higher of 2.5% (in words on the page) tax assessable less paid at period start or 5 points individual/15 corporate. Current point TZS 20,000 under 2024 s 97, giving 100,000/300,000 minima derived. s 87 interest prevailing BoT discount compounded monthly; no invented current rate. | [definition; ss 87-89; FA 2024 s 97](https://www.tra.go.tz/images/uploads/acts/Tax_Administration_Act.pdf); [s 97 currency point](https://www.tra.go.tz/images/uploads/acts/Finance_Act_2024_%281%29.pdf) |
| Treaty download list | TRA lists Canada, Denmark, Finland, India, Italy, Norway, South Africa, Sweden, Zambia:9 listed partners (derived count). A download list alone is not proof of entry into force, coverage for period, beneficial ownership or an actual lower rate. | [Double taxation agreement](https://www.tra.go.tz/resource-center/9) |
| Treaty priority and anti-abuse | Use actual in-force treaty/article and residence, beneficial-ownership, PE and condition evidence. Under 154(5), relief is blocked for an entity resident in the other contracting State where at least 50% underlying ownership is held by individuals OR entities in which no individual holds any underlying ownership, and those holders are treaty-resident outside BOTH contracting states. Preserve statutory look-through classes; residence certificate alone is insufficient. Do not raise lower domestic tax to a treaty ceiling. 50 in words on page. | [s 154(1),(4)-(6)](https://elibrary.osg.go.tz/bitstreams/d8e39776-4616-4386-bd1c-8ce8eb2caa3c/download) |
| Interest exceptions | 105 excludes interest to resident financial institution; strategic-investor nonresident-bank interest excludes associated/related loans. 2024 s 39 qualified interbank/fund relief requires government agreement, lower-rate onward lending and no related nonresident loan. Corporate/municipal DSE bond withholding exception from 1 July 2022 differs from government bond income exemption below. | [s 105(2); FA 2024 s 39](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf); [s 39 interbank loan conditions](https://www.tra.go.tz/images/uploads/acts/Finance_Act_2024_%281%29.pdf) |
| Government bond / project exemption | Second Schedule 1(1)(x): government bonds at least 3 years, issued/listed DSE from 1 July 2021. Project loan interest/fees/financing charge exemption requires the actual government loan agreement granting exemption; item(v) retrospectively 1 June 2017. Do not merge all bonds into one rule. Dates/numbers in words on page. | [Second Schedule 1(1)(v),(x),1(2)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| Zone / strategic / mining relief | No exemption merely from EPZ/SEZ label. Read actual exemption/incentive instrument, payment, period and domestic-sale restrictions. 2026 s 21 adds Cabinet-approved mining framework/state interest and strategic-investment agreement categories; construction-phase mining exemption ceases at production. | [s 21, ITA 10(3); FA 2025 s 61](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2026.pdf); [s 10 source context](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf); [s 61 zone/strategic amendment](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2025.pdf) |
| Small nonbusiness residential rent | 111(4)resident individual landlord letting residence to another individual, not business, and total qualifying annual rent no more TZS 500,000 has no 4(1)(c)liability (amount in words). This narrow recipient exception is not a general rental business exemption or instruction for a business payer to ignore 105. | [s 111(4)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |

## The method, step by step

1. Establish the payment date and actual payer/payee residence, legal form and PE connection. Identify the payment's statutory character and Tanzanian source. The payer obligation and recipient final tax are separate questions. An individual paying outside business and a qualifying exempt amount may be excluded under 105/106; do not impose business-payer withholding without checking.
2. Read the contract/invoice and determine the gross payment subject to withholding. Separate the fee, VAT and reimbursed/disbursement components; a net-of-tax promise may require gross-up, while a tax-inclusive invoice needs its own base reconciliation. This skill does not invent a universal VAT exclusion or gross-up clause without contract/law evidence.
3. Apply the supported payment head, all exemptions and actual date-specific rate. Unknown extractive-sector scope is a hold, not the general service rate by default. The recovered 2025/2026 royalty chain above preserves film 10% and removes the sports-specific 5%; actual subtype and other conditions remain required.
4. Check an actual in-force treaty and 154 anti-abuse before relief. Preserve the domestic rate where a treaty claim is unsupported for an estimate, but flag the unresolved treaty position before filing; do not claim a definitive final liability. There is no sourced treaty-rate matrix in this skill. The nine listed partners remain routing candidates, not nine pre-approved concessions.
5. Calculate withholding and net payment; decide final/nonfinal under 111 with recipient facts. Non-final tax is a potential recipient credit requiring the actual certificate/return rules; it is not an additional business expense or automatic refund. Final withholding settles that income, not every unrelated return obligation.
6. Withhold, remit and file the monthly statement within 109 timing; issue 110 certificate and retain contract, source/head, residence/PE/exemption/treaty evidence, calculation, control number, payment receipt, statement acknowledgment and certificate. TRA's portal allows certificate printing after payment; this does not remove the statutory issue deadline. Refer failure-to-withhold/arrears recovery for actual remediation, interest and penalties.

### Finality and exclusions

111 covers dividends subject to its business/individual exceptions; qualifying resident individual financial-institution deposit interest and nonbusiness land/building rent; resident extractive/agent service heads specified there; qualifying nonresident payments not through a domestic PE; unit-trust interest; and the 2024 individual-mineral/local-authority/community/individual-carbon rules. A resident corporation is not automatically excluded from every final payment. A nonresident payment through domestic PE is not automatically final. Vehicle-hire business rent remains non-final under this analysis; non-full-time directors are non-final. The recipient's annual return and credit/refund computation is a separate workflow. [ITA 54,105-112](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf),[FA 2024 s 42](https://www.tra.go.tz/images/uploads/acts/Finance_Act_2024_%281%29.pdf).

Narrow small-residential-landlord treatment, qualified government/project loans, government vs corporate/municipal bonds, strategic/interbank loans, zone licences and actual Cabinet-approved agreements must each retain their own conditions. Do not treat an exemption certificate as proof that every payment by or to that entity is exempt. For Zanzibar, income withholding and indirect-tax administration must be distinguished; this skill does not supply Zanzibar VAT/levy rates.

### Adjacent 2026 provisions and boundaries

Finance 2026 s 25 replaces forest-produce single-instalment tax 2% with earlier-of-payment/transport/possession/forest-cess timing and a defined gross base. It is not automatically payer withholding; route that activity to its actual single-instalment rules. The 2026 First Schedule 4(d)also references 1% payments under 109A, but the recovered operative amendment does not establish that section's complete scope; hold any purported livestock/fish/milk payer rule pending the actual enabling text. Digital-asset 3% is distinct from nonresident electronic-services tax under 116, which changed 2% to 3% from July 2026. VAT withholding 3%/6% and its 10 day deadline are a separate [VAT](tanzania-vat.md)workflow, not income WHT.

## Worked cases

All amounts are hypothetical TZS; outputs derived. Cases assume the actual source, payer, payee, base and exception checks support the specified head.

| Preserved original case | Gross | Withholding | Net paid | Conditions |
|---|---:|---:|---:|---|
| Resident consultancy |20,000,000|1,000,000|19,000,000|5%; ordinary non-final professional fee. Original 15 March 2025 date is historical, with 7 April 2025 remittance illustration; same supported rate applies to an equivalent 2026 case. |
| Nonresident consultancy |20,000,000|3,000,000|17,000,000|15%; no substantiated treaty relief; final only if qualifying no domestic PE connection. |
| Private-company dividend to resident individual |50,000,000|5,000,000|45,000,000|10%; establish 111 final-payment facts, not a blanket no-return promise. |
| Dividend to resident company holding 30% shares/votes |80,000,000|4,000,000|76,000,000|5%; both 25% tests met. Nonresident holder in an unlisted general case would pay 8,000,000 at 10%, net 72,000,000. |
| Resident mining technical provider |100,000,000|10,000,000|90,000,000|10% final where 106(1)(a)facts met; original 1 August 2025 date after rate change retained as historical. Before 1 July 2025 old 5% would have been 5,000,000. |
| Resident hired-vehicle business rent |12,000,000|1,200,000|10,800,000|10% non-final after 1 July 2025; original 10 September 2025 case retained historically. |
| General nonresident royalty |30,000,000|4,500,000|25,500,000|15%; general non-film head; the film 10% head is separate. |
| Covered government-financed goods purchase |40,000,000|800,000|39,200,000|2%; resident business supplier and 107 payer facts. |

```oa-check
name: Residence and extractive head determine withholding on the same service amount
inputs:
  gross_fee: 100000000
steps:
  ordinary_resident_wht: gross_fee * 0.05
  extractive_resident_wht: gross_fee * 0.10
  nonresident_wht: gross_fee * 0.15
  extractive_net: gross_fee - extractive_resident_wht
  wrong_head_underwithholding: extractive_resident_wht - ordinary_resident_wht
expected:
  ordinary_resident_wht: 5000000
  extractive_resident_wht: 10000000
  nonresident_wht: 15000000
  extractive_net: 90000000
  wrong_head_underwithholding: 5000000
```

```oa-check
name: Holding-company dividend rate needs both statutory ownership tests
inputs:
  dividend: 80000000
steps:
  qualified_resident_wht: dividend * 0.05
  qualified_resident_net: dividend - qualified_resident_wht
  general_unlisted_nonresident_wht: dividend * 0.10
  difference: general_unlisted_nonresident_wht - qualified_resident_wht
expected:
  qualified_resident_wht: 4000000
  qualified_resident_net: 76000000
  general_unlisted_nonresident_wht: 8000000
  difference: 4000000
```

Retained regressions: ordinary resident professional fee 10,000,000→500,000; nonresident 20,000,000→3,000,000; general dividend 50,000,000→5,000,000; listed dividend 50,000,000→2,500,000; interest 10,000,000→1,000,000 subject to exceptions; resident/nonresident commercial rent 10,000,000→1,000,000 subject to scope/finality; general royalty 30,000,000→4,500,000; natural-resource payment 20,000,000→3,000,000; nonresident insurance 10,000,000→1,000,000 under post July 2025 rate; mining 100,000,000→10,000,000. Unknown recipient residence, sector, exemption, treaty or finality is a hold before filing. The film 10% contrast is retained and confirmed by the 2025 supplement/2026 renumbering chain above. A resident digital-asset owner paid 5,000,000 gross fair market value by a covered platform/facilitator has 3% withholding 150,000 and net 4,850,000 (derived); recipient residence/platform/payment conditions must be proved.

## When to refuse or refer

Hold unknown residence, source, PE, sector, royalty subtype, date, base, exemption, ownership or finality; do not guess the general service rate for possible extractive fees. Refuse unsupported treaty reduction, blanket finality for all nonresidents/resident individuals, automatic zone relief, nonresident digital-asset 3% from the resident-recipient provision, or treating withholding as every recipient's entire tax liability. Refer disputed royalty subtype/source/exemption/treaty facts,109A enabling scope, deemed distributions, gross-up disputes, agent failures/arrears, actual treaty claims and Zanzibar indirect taxes. Annual income/CIT returns and credit/refund positions are separate. Obtain qualified review before filing/payment.

## Disclaimer

This withholding working-paper template does not establish a treaty entitlement, exemption or completed return. Use actual supporting records, current official procedures and qualified local review before implementing the position.

Published-numbering caution: the official 2025 supplement retains the inserted digital provisions under 83B/83C and their older Schedule references(viii)/(ix), while Finance 2025 s 60(e)(iv) renames the rate entries to(ix)/(x). Apply the substantive resident-creator 5% and resident-digital-asset 3% heads with their actual conditions; do not treat a bare old cross-reference as proof that the payment head changed.

## Sources

| Source and actual reading scope | Official URL | Read on |
|---|---|---|
| Income Tax Act, Cap. 332 R.E. 2023: Read for definitions rent/royalty/natural resource;54 whole;61;104-111 whole including the small residential exception; First Schedule 1-5; Second Schedule 1(v),(x),1(2);154 whole; not all source/exemption provisions | https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf | 2026-11-15 |
| Finance Act 2024, Act No. 6: Read for income Part 32-46 including digital/minerals/finality/royalty amendments and neighboring 47; s 97 currency point; not whole Act | https://www.tra.go.tz/images/uploads/acts/Finance_Act_2024_%281%29.pdf | 2026-11-15 |
| Finance Act 2025, Act No. 11: Read for ss 1-2; income 46-61 whole and neighbors 62-67; VAT 122-134; not whole Act | https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2025.pdf | 2026-11-15 |
| Finance Act 2026, Act No. 2: Read for ss 1-2; complete income Part 20-27; administration 70-80; VAT/SDL 88-98; not whole excise schedules | https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2026.pdf | 2026-11-15 |
| TRA: Withholding Tax: Read for whole operative intro, duties, certificate, finality and rate matrix; reconciled rent/royalty conflicts against statute | https://www.tra.go.tz/page/withholding-tax | 2026-11-15 |
| TRA: Pay As You Earn: Read for whole operative PAYE guidance including director fees/finality | https://www.tra.go.tz/page/pay-as-you-earn | 2026-11-15 |
| TRA: Double taxation agreement download list: Read for complete 9-entry download list; individual treaties and effective-date records not read | https://www.tra.go.tz/resource-center/9 | 2026-11-15 |
| Tax Administration Act, Cap. 438 R.E. 2023: Read for statutory rate definition;87-89 whole and 90 opening | https://www.tra.go.tz/images/uploads/acts/Tax_Administration_Act.pdf | 2026-11-15 |
| Income Tax Act R.E.2023 A.S.2025: Read for definitions royalty;7(2)-(4);64(8);105-112;154; First Schedule 4(b)-(c); Fifth Schedule car table, as relevant to the linked corrections; not whole consolidation | https://elibrary.osg.go.tz/bitstreams/d8e39776-4616-4386-bd1c-8ce8eb2caa3c/download | 2026-11-15 |
| Official OSG Income Tax Act R.E.2023 A.S.2025 corroboration: Read for s 3 rent/royalty definitions, complete s 105 and First Schedule 4(b), with adjacent context; same body as earlier independent source 27, not a fresh whole-consolidation read or a new contract-classification finding | https://elibrary.osg.go.tz/bitstreams/d8e39776-4616-4386-bd1c-8ce8eb2caa3c/download | 2026-11-16 |

Not yet confirmed: Actual treaty texts, entry-into-force/effective-period evidence and rates for each claim; complete source/exemption application; live WHT form/boxes and gross-up/VAT-base rules for disputed contracts; complete s 109A enabling scope for the 2026 Schedule 1% reference; actual deemed-distribution transitional application; dated BoT discount rate and official arrears allocations. Old exemption topics and historical cases remain subject to their specific supported conditions or hold.
