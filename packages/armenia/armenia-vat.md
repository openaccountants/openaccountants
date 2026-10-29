---
name: armenia-vat
description: "Use for ordinary Armenian VAT in 2026, including taxable-person status, registration, place of supply, goods and service tax points, net or inclusive prices, output tax and input recovery. Separates domestic invoices, non-EAEU imports, EAEU imports and recipient-accounted foreign services, with timing, documentary and later-use conditions. Trigger on Armenia VAT, import VAT, tax invoice confirmation, mixed use, refunds, return preparation or foreign-service reverse charge. Includes two reproducible examples with supplementary calculations preserved as research. The current filing and form dates are distinguished from January 2027 amendments. Checked against the law; ordinary implementation gaps, specialist schemes, fresh whole-pack review and named professional attestation remain open."
version: 2.2
jurisdiction: AM
tax_year: 2026
last_updated: 2026-10-27
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Armenia VAT: ordinary 2026 computation and evidence

## Who this applies to

Checked against the law for Armenian ordinary VAT payers, including the tax-agent branch for qualifying purchases from non-resident organisations without an Armenian permanent establishment (PE). Read with `vat-workflow-base`, but use the Armenian rules below where a generic workflow differs. Currentness: 24 October 2026. This is not an accepted return or independent professional sign-off. All seven ordinary country-domain methods are supplied; the README records their boundaries.

Start with taxpayer status under Article 59, not sales alone. Organisations, individual entrepreneurs and notaries can enter ordinary VAT because they cannot use a special regime, did not file a timely regime declaration, ceased qualifying, or elected VAT. The AMD 115 million annual turnover rule is a specified cessation trigger, not a universal exemption for every smaller business. Under that threshold trigger VAT applies to the excess; record the exact trigger date and the required declaration within the following 20 days. Other status triggers have their own dates. Imports and non-resident transactions need separate liability checks. [Tax Code 59][code]

Do not produce a filing-ready return from bank movements alone. Obtain sales/purchase registers, contracts, delivery/acceptance evidence, tax invoices and their confirmation dates, import declarations and payments, prior returns and the tax-account reconciliation. Unknown supplier country, service type, regime or invoice validity is a question to resolve, not a rule assigning domestic VAT or recovery.

### Determine the actual status date

| Ordinary entry route | Start and action | Authority |
|---|---|---|
| Existing taxpayer ineligible for the special system, or missing the required timely special-system declaration | VAT from 1 January through year end, rather than only after AMD 115 million | [59(1)(1)][code] |
| New organisation/entrepreneur/notary in the same ordinary-system circumstances | From its registration/appointment date through year end | [59(1)(2)][code] |
| Micro-business status ends | Test timely lawful entry to turnover tax first. If that route is unavailable or its declaration is not timely filed, VAT begins on the micro-status cessation date; submit the VAT declaration through the following 20th day inclusive | [59(1)(3)][code] |
| Voluntary VAT | Chosen date, no earlier than the 20th day before filing, through the stated year end. An earlier mandatory cessation/threshold event takes precedence | [59(1)(4)][code] |
| Turnover-tax status ends | VAT from the actual cessation point through year end; declare the legal ground and date through the following 20th day inclusive. The threshold-specific excess rule does not apply to every other cessation ground | [59(1)(5)][code] |

Noncommercial organisations and qualifying agricultural producers have the separate prior/current-year threshold and voluntary branches in 59(2). The current native 59(2.1) catering provision is repealed; do not use the older English translation's separate catering entry schedule. Nonregistered persons can still owe transaction/import VAT under 59(5)–(7), without acquiring every ordinary input-recovery entitlement. [59][code]

Use current **190-N**, incorporating 941-N **from 1 October 2026**, for the VAT-status declaration. Its item 1 is the voluntary effective-date/year route; item 2 records mandatory grounds, legal pinpoint and cessation/threshold date. The form says not to complete item 1 where item 2 grounds apply. Preserve the filing receipt and effective date; the declaration's limited earlier-date correction provisions do not create an unrestricted backdating election. [190-N current form][registration]; [941-N paragraph 2][registrationchange]

## Rates, bands and thresholds

| Item | 2026 treatment | Official authority |
|---|---|---|
| Ordinary rate | 20% of the VAT-exclusive tax base | [63(1)][code] |
| Statutory inclusive calculation | 16.67% of VAT-inclusive compensation in Article 63(2)'s specified cases, including an ordinary taxable transaction with only a cash-register receipt | [63(2)][code] |
| Zero rate | 0% only for Article 65 transactions with their conditions/evidence | [65][code] |
| Exemption | Apply the particular Article 64 provision; distinguish it from zero rating and input recovery | [64, 72–73][code] |
| Turnover-triggered VAT | AMD 115 million annual turnover across activities; excess branch and declaration rules above | [59(1)(5)][code] |
| Ordinary period | Calendar month | [69(1)][code] |
| Ordinary filing/payment | Through the 20th of the following month, subject to applicable deadline rules | [75(1), 78(1)][code] |

Do not replace statutory 16.67% with a universal 20/120 fraction. The statutory result on AMD 120,000 in its specified branch is AMD 20,004. Ordinary VAT separately charged on a net AMD 100,000 is AMD 20,000. These calculations have different legal inputs. [61(1), 63][code]

## The base

Maintain a line ledger: parties and VAT status; goods/service classification; place and time provision; net or inclusive price; statutory rate/exemption; output; invoice or import evidence; recovery period and restriction; return mapping. [37–40, 59–73][code]

**Place.** For ordinary goods, Article 37 starts with their location at supply or export from Armenia; electronic trading has a separate branch. For services use Article 39: Armenian immovable property, relevant work on Armenian movable property, physically performed specified activities, recipient-location listed services such as consulting/accounting/software, and the residual supplier-location rule are distinct tests. Electronic services have their own recipient and location-evidence rules. A foreign invoice or foreign customer alone does not settle the result. [37, 39][code]

For an Armenian supplier's qualifying service whose place is outside Armenia under Article 39, check the **zero-rate provision in 65(2)(11)** rather than mechanically label it exempt or omit it. The official English reproduction incorrectly refers to Article 38 here; the current Armenian text refers to Article 39. Exports of qualifying goods under 65(2)(1)/(2) also require their customs/EAEU conditions; the EAEU branch refers to Article 76 documentation. Scrap-metal exceptions and other specialist supplies require their actual provision. Do not zero-rate every payment from abroad. [65–76][code]

**Time.** Ordinary goods follow the Article 38 delivery/receipt and ownership rules, with state registration and leasing exceptions. Article 40 specifies month-end public/communal services, period-end rental, and month-end or contracted phases for subscriptions. Other services use the earlier relevant completion/transfer or recipient approval of the settlement document, subject to statutory fallback provisions. Do not use invoice issue date, bank receipt or an assumed universal advance-payment trigger in place of these tests. [38, 40][code]

**Base.** Ordinary supply is monetary value excluding VAT. For non-EAEU goods released for domestic consumption, the ordinary import base is customs value plus customs duty plus applicable excise. For EAEU-status goods imported from another member state it is acquisition value plus applicable excise. Article 62 has special bases; do not apply ordinary purchase cost to every property, free, related-party or leasing transaction. Keep foreign-currency conversion evidence under Article 16. [16, 61–62][code]

### Compute output and allowable recovery

1. Sum output under each established rate/base and lawful adjustment. Add tax-agent output where Article 70(2) applies. Do not include customs import payment as domestic sales output simply to force a neutral return. [63, 70, 78][code]
2. Build a recovery ledger by source and actual entitlement period. Domestic supplier invoice VAT is recovered in the acquisition/acceptance period if the recipient confirms the tax invoice under Article 68 by the Article 75 filing deadline; otherwise it belongs to the period containing confirmation. Invoice issue date alone does not determine entitlement. [71(1)(1)][code]
3. Non-EAEU import recovery requires the declaration and payment; where those dates fall in different periods, use the later period and only the amount paid. For EAEU imports, recovery in the border-crossing period requires both submission of the import tax declaration and payment by that period's last day. Otherwise apply the later relevant declaration/payment period. Payment by next month's legal payment deadline does not retrospectively satisfy the earlier month-end recovery condition. [71(1)(2)/(3)][code]
4. For an Article 70(2) recipient-agent transaction, test the separately issued Article 56(7) tax invoice: issue by the return deadline permits the acquisition period; later issue moves recovery to the issue period. Also apply Articles 72–73. Foreign-service output does not itself establish equal same-period recovery. [71(1)(4)][code]
5. Exclude or adjust blocked recovery. Article 72 covers non-VAT persons, specified exempt/special-regime/non-object uses, defective or unreal transactions, and passenger-car conditions. The exempt-use restriction has explicit exceptions, including the July 2026 addition for government-decision donations to state/community. Do not describe every exemption as invariably blocking every input. Passenger cars, leasing, registration and subsequent disposal need the current specific branches, not an assumed business-use percentage. [72–73; HO-234-N 13/33][code] [Amendment][july]
6. Reconcile net output minus allowable input, after the adjustments below. Positive difference is current tax under Article 70; negative difference is an Article 74 refundable balance, not evidence of an immediate bank refund. [70, 74][code]

### Attribution and later changes of use

Article 73 is not a generic annual pro-rata rule. Initially, direct taxable use (including qualifying zero rate) and acquisitions not directly attributable are treated under 73(1), subject to Article 71 timing and Article 72 restrictions. Direct non-taxable use is blocked under 73(3). Track original input and subsequent actual use. [73][code]

For **previously credited non-fixed goods/work/services** subsequently used in non-taxable transactions, 73(2)(1)(a) reverses 20% of the value directly attributable to that non-taxable use. If subsequently mixed use cannot be directly attributed, paragraph (b) uses the non-taxable share of that period's total transaction tax bases to determine the tax adjustment. Establish which transactions belong in the denominator under the actual provision; do not substitute bank receipts or all financial-statement revenue. [73(2)(1)][code]

For a **previously credited fixed/intangible asset** later used exclusively for non-taxable transactions, 73(2)(2)(a) uses 20% of the Article 121 tax depreciation for the relevant period. Simultaneous mixed use adds the prescribed non-taxable proportion under (b); non-taxable disposal uses book value under (c). Previously blocked acquisitions later used for taxable transactions have separate 73(4) increases, including statutory 16.67% branches. Regime changes, losses, corrected invoices/imports and motor vehicles have additional 73 provisions. Do not carry a one-time purchase allocation unchanged through later use/disposal. [73][code]

### Stock and assets when a regime or use changes

Keep a dated stock/asset schedule with the status date, original invoice/import evidence, prior input treatment, capitalised VAT, relevant value, tax depreciation and previous reversals. The status declaration does not itself restore all historic input. [71–73][code]

**General system to special system:** Article 73(14) concerns acquisitions still held on the transition date whose VAT was previously credited. In the last VAT period **preceding** that date, reduce input by 20% of the relevant value of non-fixed goods/work/services and 20% of fixed/intangible carrying value. Use remaining stock and carrying amounts, not every historic purchase. Qualifying stock of AMD 3 million and asset carrying value of AMD 5 million produce reversals of AMD 600,000 and AMD 1 million. Previously blocked VAT is outside this previously credited population. [73(14)][code]

**Previously blocked/capitalised VAT later supporting taxable use:** establish 73(4)'s conditions and 71's evidence/timing first. For non-fixed goods/work/services directly supporting taxable transactions, restore 16.67% of the corresponding value. For the stated unallocable mixed-use case, use the **taxable** share of that period's total transaction tax bases. English 73(4)(1)(b) incorrectly says non-taxable share; native text says taxable share. For fixed/intangible assets, exclusively taxable use restores 16.67% of period Article 121 tax depreciation; simultaneous mixed use multiplies that amount by the taxable share; taxable disposal uses 16.67% of carrying value. This is not full purchase-credit recovery on registration day. [73(4)][code]

Where entitlement was only **deferred under 71**, 73(5) preserves acquisition-period taxable/non-taxable proportions rather than using the eventual confirmation month's proportions. Distinguish documentary delay from an actual later use change. Do not replace statutory 16.67% with 20/120. [71, 73(5)][code]

**Deregistration/retirement:**73(11) reverses previously credited input on assets held when an entrepreneur deregisters or a notary leaves office; fixed/intangible assets use the prior credit share corresponding to carrying value. Use the last VAT return before deregistration, including the stated entrepreneur already in a special regime. Reconcile prior transition reversals. Under 73(7), fixed-asset liquidation has a separate 20%-of-carrying-value reversal and stated restoration on later taxable sale as the same-purpose fixed asset. [73(7)/(11)][code]

**Acquisition losses:**73(6) denies input credit where the loss is not deductible under the profit-tax rules. Use the [corporate loss classification/documentation method](am-corporate-income-tax.md#inventory-and-asset-losses-classify-substantiate-then-deduct): actual 1261-N records, 122 natural/quality/accidental/technological/other-event tests and current 1467-N norm lookup. A stock-write-off entry alone is not input-credit entitlement. Where the permitted loss norm is annual, compare the year's eligible loss and related input with the credit actually taken across earlier VATperiods, and correct the difference as an increase/decrease of input credit in the year's **last VATreporting period**. Do not reopen every earlier month solely to perform that express annual-norm true-up or treat a later qualifying legal event as an automatic prior-year loss. [73(6)/122][code]; [1261-N][lossdocs]; [1467-N][naturalloss]

## Deadlines and filing

Ordinary payers submit the **unified VAT and excise calculation** monthly and pay through the following month's 20th. Registered no-PE non-resident B 2 C electronic-service/EAEU electronic-trading populations have a separate quarterly branch; they are not the ordinary monthly return in this Guide. Non-EAEU import VAT is ordinarily due before release, unless a lawful customs deferral applies. Ordinary EAEU import filing/payment uses the following month's 20th, with transaction-specific exceptions. Keep import obligations separate from the unified monthly return. [69, 75, 77–78][code]

Actual published return: **Order 298-N, consolidation applicable from 1 April 2023**, including Order 76-N. Its VAT section uses output as `կրեդիտ` and input as `դեբետ`. Preserve these legal column meanings rather than assume English accounting debit/credit orientation. [Actual form and instructions][form]

| Actual VAT row | Workpaper link |
|---|---|
| 7 | Ordinary 20% transaction base and output |
| 8 / 11 | Specified correcting tax invoice transactions; distinguish supplier and recipient-agent branches |
| 9 | Statutory 16.67% inclusive branch |
| 10 / 15 | Other output obligations (10 includes Article 70(2) agent VAT) / statutory output adjustments |
| 12 / 13 | Zero-rated / exempt bases with statutory references |
| 16 | Total output/base according to the printed formula |
| 17 / 18 | Imported / domestic acquisition bases and specified invoice/declaration VAT, before required entitlement adjustments |
| 19 / 20 | Correcting acquisition invoices / input adjustments with legal grounds |
| 21 | Total adjusted input, positive/negative columns |
| 22 | Printed legacy Article 79 reference. Article 79 is repealed; this row does not authorise a new import deferral. Historic balances need their actual transition authority |
| 23 | Positive current VAT / negative refundable balance, distinct columns |

This is a published-form map, not confirmation of the live portal or every detailed subcolumn. Do not reconstruct the earlier Guide's unsupported fourteen-part form. Check the actual instructions, period, signs and adjustments before entering figures. Row 18 base includes the prescribed domestic acquisitions even without a settlement document; its VAT column is specified tax-invoice VAT. Row 20 then implements deferred entitlement and blocked-use adjustments. Do not populate the base column from eligible VAT alone or omit the adjustment that prevents early recovery. The published total-base formula still displays a reference to repealed row 14; do not fabricate current activity there. Live validation, rounding, corrections, electronic signature and acceptance remain untested. [Form][form]

**Date gate:** Order **1000-N of 24 September 2026** changes the form, including receipt returns, exempt adjustments and electronic-platform fields, and repeals row 22, **from 1 January 2027**. It does not make those changes operative for October 2026. HO-234-N also separates July 2026 provisions from specified January 2027 amendments, including its Articles 11/12/14/16. Do not pull those future recipient, replacement-invoice or filing/payment provisions into the current method. [1000-N 2][future] [HO-234-N 33][july]

### Separate VAT credit, single-account funds and bank refund

1. Establish the Article 74 refundable amount from the filed return and lawful inputs. Under 74(3), available VAT credit can settle VAT generated by unified VAT/excise returns for any reporting period using the prescribed software command on or before the relevant payment deadline. It is not already a bank payment.
2. For an on-time **non-risky** balance, current native 74(4) credits the single account before the payment deadline if the taxpayer uses the relevant command, **or on the payment deadline**. The English wording does not accurately separate these alternatives. A non-risky late/amended return's refundable amount is credited on submission day. Preserve the return, risk result, command if used and actual ledger entry. [74(1)–(4)][code]
3. Apply current **155-N**, effective 1 January 2025. A risk flag routes the amount to 74(5)'s substantiation procedure; it does not itself rewrite Article 71's input entitlement. The taxpayer's other tax-control risk classification overrides an otherwise clean return. Older 2019 simplified-procedure 1468-N was repealed by 132-N inFebruary 2025; do not import its former thresholds or deadlines. [155-N Annex paragraphs 1 and 3][risk]; [132-N][oldrepeal]
4. A risky amount reaches the single account only after the written-application inspection/examination route substantiates it. Article 348(1) requires the authority-prescribed study application; that is distinct from the later bank-refund application. Article 327(1) requires substantiated examination amounts to be credited within three working days following effectiveness of its protocol. Do not count the unsubstantiated amount as available cash. [74(5), 348(1), 327(1)][code]
5. Once funds are actually available on the single account, apply separately for their refund using **246-N Annex 2**, current from 1 January 2025. Complete taxpayer identity/number and applicable personal identifier, address, receiving bank/account or permitted Treasury/account route, requested AMD amount and signature. Item 4 is repealed in the current printed form. Reconcile the requested amount with the actual available balance and other ledger movements. [246-N current Annex 2][refundform]; [903-N][refundchange]
6. Article 327(2)'s ordinary refund period is **20 days after receipt of the application**, or **10 days** for a taxpayer holding the valid law-abiding-taxpayer certificate. These are statutory application clocks, not a guarantee measured from the VAT return or first negative balance. Treasury transfers the requested amount through the authorised account route. Article 327 contains separate delayed-refund compensation conditions; no automatic penalty amount is computed here. Its HO-344-N amendment is marked for 1 January 2027, not current 2026 use. [327(2)][code]

The current risk-study application is **1562-L of 27 November 2024**, effective **1 January 2025**, linked on the SRC's live internal-orders page. Complete items 1–4 with taxpayer number, name, address and phone. Item 5 lists the post-1 January 2025 reporting periods: tax type, year, period and risky refundable amount from filed unified returns, including amended returns, in AMD. Item 6 separately covers the earlier periods/balances. Instruction 3 says **do not complete items 5 and 6 together**: submit separate applications for the two cohorts. Sign the application. This requests substantiation and crediting, not payment to a bank account; use 246-N separately after the funds become available. [1562-L Annex/form/instructions 1–3][studyform]

Actual **1561-L**, also effective 1 January 2025, repeals the older 670-L study/simplified-request order and 588-L conclusion order. Their continued presence elsewhere in the SRC archive does not make them current forms. The replacement 1562-L instruction's historic-balance pinpoint says 457(1); current Code 457(9) is the actual 31 December 2024 balance provision, which controls the cohort test here. [1561-L 1–2][studyrepeal]; [457(9)][code]

For 155-N's ordinary VAT risk screen, record every applicable trigger, rather than inventing a refund cap:

| Trigger group | Check against the source records | Provision |
|---|---|---|
| Status and history | Not exclusively VAT during the period; special-system/liquidation/suspended/bankrupt status when filing; a missing required return in the filing year or previous three tax years; return relating to December 2024 or earlier | Annex paragraph 1(1)–(4) |
| Output reconciliation | Understated ordinary invoice output; inclusive/exempt totals below the prescribed cash-register/bill totals; zero-rate totals below export/customs/bill evidence; the stated exempt-only/input/refund combination | Annex paragraph 1(5)–(8) |
| Output corrections | Reductions above, or increases below, correcting-invoice amounts; other liability below recipient-issued invoices; a reported reduction of calculated output VAT | Annex paragraph 1(9)–(12) |
| Input entitlement and additions | Increased input outside the specified prior-domestic-invoice confirmation exception/cap; domestic/recipient-issued, customs or EAEU recovery without 71's conditions; reported domestic/input amounts above the specified invoice amounts | Annex paragraph 1(13)–(17) |
| Remaining input comparisons | The specific unconfirmed-invoice VAT comparison in(18); purchase correction reductions below or increases above correcting documents; import input above the legally calculated import amount | Annex paragraph 1(18)–(21) |

Source: [155-N complete VAT criteria in Annex paragraph 1 and overriding paragraph 3][risk]. These checks determine routing; a taxpayer cannot certify the authority's separate risk-management result from arithmetic alone. Code 457(9) also classifies refundable balances existing on 31 December 2024 as risky, while retaining 74(3)'s VAT-settlement and 74(5)'s substantiation routes. [457(9)][code]

### Ordinary EAEU documents and corrections

For EAEU-status goods exported to another member state, current 65(2)(2)/76(1) ties domestic zero-rate substantiation to the exporter submitting the **export tax declaration**. Commission/agency cases require 76(2)'s linked export evidence for the principal. Retain contract, goods/status, price, invoice, transport/border evidence and the filed transaction number; an overseas payment alone is insufficient. **424-N Annex 1** supplies the actual declaration: buyer/member state, export date, supporting transit/airway/other document number and VAT/exempt tables. Its ordinary land-transport date instruction uses the customs officer's border endorsement; air/post uses the specified transport documents. Where ownership passes in the destination state, the instruction has its separate ownership-transfer date. [65–76][code]; [424-N Annex 1 instructions 1/12–16][eaeuform]

The export declaration's printed VAT table/instruction 15 uses a 20% computation. That form field is not authority to charge 20% domestic output on a supply qualifying for 65/76 zero rating. Keep the export document and the unified return's zero-rate row as distinct reconciliations. Complete treaty confirmation/late-proof effects still require their applicable evidence. [65(2)(2), 76][code]; [424-N Annex 1 instruction 15][eaeuform]

### EAEU export proof and late documents

Current [EAEU Treaty Annex 18, paragraphs 3–5][treaty] supplies the export framework. Paragraph 4 lists contracts, qualifying payment evidence, destination import/payment statement or permitted list, transport evidence and other national documents, with national-law/electronic-submission exceptions. Its entire list is not a universal instruction to upload every item on each Armenian export.

For the ordinary Armenian method, current 76(1) substantiates zero rating on submission of the **exporter's export tax declaration**. SRC's official explanation 82, dated 1 October 2020, reads this with treaty paragraphs 3–5: submit that declaration within **180 calendar days from dispatch/transfer (export)**; failure to supply the buyer's import/indirect-tax-payment statement **alone does not create Armenian VAT liability**. Keep these documents distinct. Current 76 was re-read; the explanation is supporting authority with its original date, not a new 2026 circular. [76][code]; [SRC explanation 82][explanation82]

Track actual dispatch/export date, declaration receipt and the proof deadline per transaction. Payment, transport evidence or an unsigned declaration does not establish filing. A finding that goods were not exported defeats confirmation under treaty paragraph 4. [Treaty Annex 18(4)–(5)][treaty]; [424-N Annex 1][eaeuform]

If required proof is late, treaty paragraph 5 makes indirect tax payable for the shipment period, or another period actually prescribed by national law, with domestic deduction/enforcement rules. Compute the tax on its established base/rate and reconcile return and payment; missing **buyer statement alone** is not that failure under the Armenian explanation. Later qualifying proof permits deduction/offset/refund of paid indirect tax under national procedure, but already paid late-payment penalties/fines are not refundable. Record proof date, paid tax, return restrictions and the credit/refund route separately. Exact Armenian amended-return period mapping remains to be confirmed; no automatic current-month input deduction or penalty refund is certified. [Treaty Annex 18(5)][treaty]; [53–54, 74, 76, 327][code]

For ordinary EAEU imports, current 77(1) requires **both** the import tax declaration and the statement of import/payment (or stated exemption/other payment route), through the 20th of the following month, following Article 53's submission procedure. **HO-234-N Article 15 removed the old four-paper-copy/electronic alternative wording from 1 July 2026**; do not use that older English paragraph as the current filing instruction. Agency/commission and goods whose ownership transfers in Armenia have the separate 77(2)/(3) date branches. **424-N Annex 2** provides the actual import declaration; keep its transaction/registration numbers, importer, member state, goods/tax base, border/ownership date and payment evidence separate from the import-payment statement and unified return. Re-test 71(1)(3)'s recovery month; next-month timely payment is not same-month paid evidence. [77–78, 71, 53][code]; [HO-234-N 15/33][july]; [424-N Annex 2][eaeuform]

Distinguish an erroneous original return from a legally adjusted transaction. Under 54, later filings for the same period/transaction are corrected returns/declarations. Under 42(4), an ordinary qualifying transaction adjustment decreasing VAT/output and corresponding input belongs to the period of the correcting document, whereas an increase belongs to the original transaction period; public services have 42(5)'s separate adjustment-period rule. An invoice correction without an actual 42(1) ground is disregarded. [42, 54][code]

Before amending, check 53(10)/(11)'s inspected/studied periods, three-year and prior simplified-credit restrictions. The separate 53(10.1) authority-prescribed route allows liability-increasing/input-decreasing returns notwithstanding the specified restrictions. Article 54(4) provides its stated understatement-fine relief for a correction creating/increasing liability; it does not say all interest and other sanctions vanish. EAEU 424-N instructions require a new corrected declaration with the original transaction number, not a duplicate new transaction. [53–54][code]; [424-N Annexes 1–2, instructions 1–2][eaeuform]

## Penalties and interest

For ordinary tax obligations, Article 401 prescribes 0.075% per overdue day on unpaid tax, capped at 730 days, with special cases in that Article. Article 402 prescribes 5% of calculated tax for each completed 15-day late-filing period, capped at calculated tax. Understatement, improper invoices and other failures have separate provisions, including Article 403. Determine taxpayer type, assessment/event, period, correction and relief facts before quantifying sanctions; neither a zero payment nor filing alone proves every obligation discharged. [401–403][code]

## Cross-border points

Where an Armenian VAT payer contracts with a no-Armenian-PE non-resident organisation for an Armenian-place taxable service, Article 70(2) makes the contractual VAT payer the tax agent and disregards the ordinary threshold. Establish the foreign entity/PE and Article 39 place, Article 61/62 base, contract pricing and tax-invoice procedure first. Ordinary consulting to an Armenian business and electronic services have distinct place branches. Imports documented in the VAT payer's name have the specific 70(2)(4) exception. Micro/turnover-regime recipients and registered non-resident consumer supplies follow other liability branches; do not apply this example universally to SaaS or all foreign suppliers. [39, 56(7), 70(2), 71(1)(4)][code]

## Two worked examples that recompute

Hypothetical AMD inputs; each assumes the stated taxpayer, classification, timing, documents and eligibility are established. Arithmetic controls do not verify those assumptions or portal acceptance.

### 1. Ordinary net output and allowable input

AMD 5 million ordinary taxable net sales, AMD 600,000 domestic and AMD 200,000 import VAT lawfully recoverable in the month, no other adjustments: current payment AMD 200,000. A separate zero-rated-only case with those same eligible inputs gives an AMD 800,000 refundable balance; it does not establish cash receipt. [63, 70–74][code]

```oa-check
name: Armenia ordinary VAT and separate negative balance
inputs:
  taxable_net_sales: 5000000
  allowed_domestic_input: 600000
  allowed_import_input: 200000
steps:
  - output: taxable_net_sales * 0.20
  - allowed_input: allowed_domestic_input + allowed_import_input
  - current_payable: max(output - allowed_input, 0)
  - zero_rated_only_refundable_balance: allowed_input
expected:
  output: 1000000
  allowed_input: 800000
  current_payable: 200000
  zero_rated_only_refundable_balance: 800000
```

### 4. Non-EAEU import base and paid-only recovery

Ordinary domestic-consumption release, customs value AMD 10 million, duty AMD 1 million, no excise/special exemption. Import VAT AMD 2.2 million. Declaration in September, lawful deferred payment in October: September recovery zero, October AMD 2.2 million after full payment and other eligibility. The deferral is an assumed issued lawful decision, not an election created by this example. [61(2), 71(1)(2), 78(5)/(5.1)][code]

```oa-check
name: Armenia import base and later paid recovery
inputs:
  customs_value: 10000000
  customs_duty: 1000000
  applicable_excise: 0
steps:
  - import_base: customs_value + customs_duty + applicable_excise
  - import_vat: import_base * 0.20
  - september_recovery: 0
  - october_recovery_after_full_payment: import_vat
expected:
  import_base: 11000000
  import_vat: 2200000
  september_recovery: 0
  october_recovery_after_full_payment: 2200000
```

## Ask the client first

- What entity, regime, effective VAT registration and election/cessation dates apply? Supply declarations and prior turnover by activity.
- What goods/services, delivery/acceptance dates, contract stages, customer/supplier locations and PEs are involved? Is the stated price net or inclusive?
- Which invoices were issued and confirmed, on what dates? Supply valid tax invoices, corrections and recipient-issued foreign-service invoices.
- Which imports are EAEU-status versus customs release, with which declarations, border dates, payment and lawful deferral evidence?
- What taxable/zero-rated/exempt/special-regime uses, common expenses, assets, cars and later use/disposal events exist?
- Which export/zero-rate documents, prior refundable balances, account commands, late returns, assessments or refund requests exist?

## Sources

| Official source and actual read scope | URL | Read on |
|---|---|---|
| [Current Armenian Tax Code][code], targeted Articles 16, 37–40, 59, 61–63, 65–66, 69–75, 77–78 and 401–403; read 24 October 2026. Linked current text marks future provisions separately. Targeted reading is not verification of every exception. | https://www.arlis.am/hy/acts/215611/latest | 2026-10-24 |
| [Official English reproduction][english], corresponding targeted provisions; read 24 October 2026 as supporting translation. It misreferences Article 38 in 65(2)(11), and its period wording does not override Armenian Article 69's monthly rule. Current Armenian text governs. | https://www.arlis.am/en/acts/231892 | 2026-10-24 |
| [HO-234-N][july], actual Articles 11–16/33; read 24 October 2026. Article 13 amends the exempt-input restriction in Article 72, not Article 73; specified other changes wait until January 2027. | https://www.arlis.am/hy/acts/226008 | 2026-10-24 |
| [Order 298-N, current 2026-applicable consolidation 175524][form], actual VAT form and targeted instructions; read 24 October 2026. The earlier [2019 consolidation](https://www.arlis.am/hy/acts/132487) is historical and is not used as current authority. | https://www.arlis.am/hy/acts/175524 | 2026-10-24 |
| [Order 1000-N][future], actual amended fields and paragraph 2; read 24 October 2026. Effective 1 January 2027, not its September adoption/publication date. | https://www.arlis.am/hy/acts/231429 | 2026-10-24 |
| Current native Code, targeted 59(1), 74, 76–77,327,457(9), 42(4)–(6), 53(10)/(10.1)/(11), 54; supporting English checked against native | https://www.arlis.am/hy/acts/215611/latest | 2026-10-25 |
| 190-N current VAT-status form; actual 941-N amendment and 1 October 2026 gate | https://www.arlis.am/hy/acts/136993/latest | 2026-10-25 |
| 941-N actual amendment/commencement | https://www.arlis.am/hy/acts/230825 | 2026-10-25 |
| 155-N current complete ordinary VAT criteria and risk override; excise catalogue not implemented here | https://www.arlis.am/hy/acts/200966/latest | 2026-10-25 |
| 132-N actual repeal of the former 1468-N simplified procedure | https://www.arlis.am/hy/acts/203101 | 2026-10-25 |
| 246-N current Annex 2 refund application and targeted instructions; actual 903-N amendment | https://www.arlis.am/hy/acts/144655/latest | 2026-10-25 |
| 903-N actual refund-form changes and 1 January 2025 gate | https://www.arlis.am/hy/acts/195736 | 2026-10-25 |
| 424-N actual export/import forms, targeted ordinary document/date/correction instructions | https://www.arlis.am/hy/acts/137009/latest | 2026-10-25 |
| HO-234-N 15 and 33, actual removal of former 77(1) paper-format wording and current July 2026 commencement | https://www.arlis.am/hy/acts/226008 | 2026-10-25 |
| Current native 73(4)–(7)/(11)/(14), supporting English/native comparison; 79 repeal | https://www.arlis.am/hy/acts/215611/latest | 2026-10-25 |
| Current EAEU Treaty, actual Annex 18 paragraphs 3–5 in full | https://www.arlis.am/hy/acts/202902/latest | 2026-10-25 |
| SRC explanation 82 dated 1 October 2020, all three scanned pages read visually; Armenian exporter/buyer-statement distinction | https://www.src.am/storage/awarenessFiles/Irazekum%2082.pdf | 2026-10-25 |
| SRC live internal-orders page: current 1561-L repeal and 1562-L replacement entries read through the rendered page | https://www.src.am/am/getMenusContents/227 | 2026-10-25 |
| Actual 1562-L: all 4 pages, form, instructions and 1 January 2025 commencement | https://www.src.am/storage/menu_contents_227/hr_pek_2024_1562_L_6757f76f7ac17.pdf | 2026-10-25 |
| Actual 1561-L: complete 1 page repeal and 1 January 2025 commencement | https://www.src.am/storage/menu_contents_227/hr_pek_2024_1561_L_6757f76f8377e.pdf | 2026-10-25 |

| Fresh native 73(6)/122 and current 1261-N complete loss-documentation method; 1467-N operative schedule lookup and Annex 2 method; exact scope in loss-debt-research.md | https://www.arlis.am/hy/acts/215611/latest ; https://www.arlis.am/hy/acts/171651/latest ; https://www.arlis.am/hy/acts/127175/latest |2026-10-26|

[code]: https://www.arlis.am/hy/acts/215611/latest
[english]: https://www.arlis.am/en/acts/231892
[july]: https://www.arlis.am/hy/acts/226008
[form]: https://www.arlis.am/hy/acts/175524
[future]: https://www.arlis.am/hy/acts/231429
[registration]: https://www.arlis.am/hy/acts/136993/latest
[registrationchange]: https://www.arlis.am/hy/acts/230825
[risk]: https://www.arlis.am/hy/acts/200966/latest
[oldrepeal]: https://www.arlis.am/hy/acts/203101
[refundform]: https://www.arlis.am/hy/acts/144655/latest
[refundchange]: https://www.arlis.am/hy/acts/195736
[eaeuform]: https://www.arlis.am/hy/acts/137009/latest
[treaty]: https://www.arlis.am/hy/acts/202902/latest
[explanation82]: https://www.src.am/storage/awarenessFiles/Irazekum%2082.pdf
[studyform]: https://www.src.am/storage/menu_contents_227/hr_pek_2024_1562_L_6757f76f7ac17.pdf
[studyrepeal]: https://www.src.am/storage/menu_contents_227/hr_pek_2024_1561_L_6757f76f8377e.pdf

Targeted commencement recheck, **25 October 2026**: [HO-234-N art. 33(1)](https://www.arlis.am/hy/acts/226008) is the general 1 July 2026 commencement and enumerated 1 January 2027 exception provision. Article 31 instead amends Tax Code 293(2); it is not the commencement authority. Other source read dates remain as recorded.

[lossdocs]: https://www.arlis.am/hy/acts/171651/latest

[naturalloss]: https://www.arlis.am/hy/acts/127175/latest

**Not yet confirmed:** return-period/restoration mapping when the exporter fails its own required export-declaration deadline. Ordinary timely-export proof and filing are supplied; the buyer statement missing alone is not that failure. The unresolved late-filing recovery is a conditional failure boundary, not a missing ordinary timely-export method. Ordinary loss classification/documentation, current norm lookup and annual VATtrue-up are supplied in the corporate/VAT methods. Specialist exemption/base/vehicle/leasing schemes and January 2027 implementation are separate boundaries. Actual taxpayer evidence, portal acceptance and professional attestation are not represented as obtained; fresh whole-pack review remains pending.

> Contributed by Michael Cutajar.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
