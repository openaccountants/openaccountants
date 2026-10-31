---
name: monaco-vat
description: "Monaco VAT working paper for 2026 using the Monaco turnover tax code and the France Monaco convention. Covers standard rate calculations, ordinary franchise thresholds, start date and threshold crossing tests, input deduction, business service reverse charge, monthly or permitted quarterly filing, Monaco DSF procedures and statutory penalties. Use for Monaco TVA, VAT returns, small business exemption and foreign service questions. Requires transaction evidence and the assigned filing calendar. Includes input recovery coefficients, capital adjustments, refunds, exports, imports, EU reporting and documented portal onboarding, and awaits a named Monaco professional review."
version: 2.3
jurisdiction: MC
tax_year: 2026
last_updated: 2026-10-27
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Monaco VAT v2.3

> **Source-cited draft.** Checked 25 October 2026. No named Monaco professional has reviewed this Guide. It produces a working paper, not a filing or a final tax position. Read the [country gap register](README.md) before use.

## Who this applies to

Tax year 2026. Apply Monaco's Code des taxes sur le chiffre d'affaires to taxable transactions, establishments and recipients. The France–Monaco convention aligns turnover taxes on the same bases and rates; it does not justify replacing Monaco filing rules with an assumed Nice tax-office procedure. Ordinary taxable business services use article 11's recipient/provider location tests, subject to the special rules that follow. Establish transaction type, tax point, customer status and the establishment receiving the service before assigning a rate. [Convention, art. 15](https://legimonaco.mc/tai/convention/1963/05-18-tai1l000235/); [Code, arts. 1, 11–14, A-139](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

This Guide covers ordinary taxable/franchise businesses, domestic supplies, imports, exports and general B2B goods/services trade. Classify each supply from its legal facts before applying the rate, exemption, recipient liability or input deduction. Property developments, travel/margin/online schemes and specialised sector exemptions need a separate scheme-specific working paper. Never infer exemption or deduction from a bank merchant’s name.

## Rates, bands and thresholds

| Item | Amount | Period | Official source |
|---|---|---|---|
| Standard rate | 20% | 2026 | [Art. 51](https://legimonaco.mc/code/code-taxes-chiffre-affaires) |
| Reduced rate, specified food/books and other listed supplies | 5.5% | 2026; category conditions apply | [Art. 52-0](https://legimonaco.mc/code/code-taxes-chiffre-affaires) |
| Intermediate rate, specified goods/services | 10% | 2026; category conditions apply | [Arts. 52–53, 56–56 bis](https://legimonaco.mc/code/code-taxes-chiffre-affaires) |
| Special rate, specified medicines and press | 2.10% | 2026; category conditions apply | [Arts. 59, 95](https://legimonaco.mc/code/code-taxes-chiffre-affaires) |
| Ordinary franchise, prior-year national turnover | Total EUR 85,000; relevant service subset EUR 37,500 | 2026 screen | [Art. 87(I)](https://legimonaco.mc/code/code-taxes-chiffre-affaires) |
| Ordinary franchise, current-year national turnover | Total EUR 93,500; relevant service subset EUR 41,250 | 2026 screen | [Art. 87(I), (III)](https://legimonaco.mc/code/code-taxes-chiffre-affaires) |
| Quarterly filing permission | Annual tax strictly below EUR 4,000 | 2026 | [Art. 70(2)](https://legimonaco.mc/code/code-taxes-chiffre-affaires) |
| Late-payment interest | 0.20% per month | 2026, statutory conditions | [Art. 110](https://legimonaco.mc/code/code-taxes-chiffre-affaires) |

## The base

For an established ordinary business, test both total national turnover and the service subset excluding on-premises consumption and accommodation. The prior-year and current-year tests differ. Crossing either current-year ceiling ends franchise for transactions from the crossing date. Special authors/artists thresholds are outside this ordinary screen. Article 89 defines included/excluded turnover and prorates thresholds for a mid-year start. Article 88 has exclusions. Its July 2026 amendment and article 89 changes specify application from 21 February 2026: inspect the transaction date. [Arts. 87–89](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

A franchise business cannot deduct input VAT or show VAT on invoices; article 90 prescribes “TVA non applicable, article 87 du Code des taxes”. Article 91 allows an option effective the first day of the declaration month, covering two years including that year, with renewal conditions. Reverse-charge obligations require a separate test; franchise is not a universal exemption from all recipient obligations. [Arts. 62, 87–91](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

**Taxable business.** The consideration includes directly price-linked subsidies, incidental transport/insurance/packing and other taxes, but excludes VAT itself, direct customer discounts and qualifying documented disbursements made in the principal’s name/account. Convert foreign currency using the last ECB rate published at the tax point. Goods are ordinarily due at delivery, and advance receipts trigger VAT on the received amount. Ordinary services are due on receipts unless authorised for debits; recipient-accounted services use performance or advance-receipt timing. Intra-community acquisitions and qualifying exempt deliveries use the fifteenth of the next month, or an earlier non-advance invoice. Reconcile by legal tax point, not bank export date. Return liquidation rounds taxable sums and tax-calculation elements to the nearest euro, with EUR 0.50 upwards. [Arts. 35–36, 40–41](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

**Rate classification.** Article 52-0 covers 5.5% qualifying food (with express exclusions including alcohol, confectionery subject to the chocolate exceptions, margarine and caviar), books and specified essential supplies. Articles 52–53/56 cover 10% listed goods, non-reimbursable authorised human medicines, qualifying hotel accommodation, passenger transport, restaurant sales and prepared food for immediate consumption, excluding alcohol at 20%. Article 59 gives 2.10% for the specified reimbursable/approved human medicines; article 95 has qualifying press. Article 56 bis gives 10% for qualifying work on housing completed over two years previously, with customer certification and exclusions for new-building/over-10%-extension, cleaning, gardens and fossil-fuel boilers; energy works under article 52-0 bis have their own conditions. Save the exact category and evidence; “food”, “property” or “medical” alone is insufficient. [Arts. 51–59, 95](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

**Input recovery.** Article 42 requires tax legally charged, a compliant invoice or import/acquisition evidence, the relevant output declaration and use in operations giving deduction. The right arises when tax becomes due at the liable person; correct deductions when the invoice is corrected. Compute `deductible VAT = eligible VAT × deduction coefficient`. Under A-72–A-73, the coefficient is the product of (1) business use within VAT scope, (2) use for activities giving recovery, and (3) legal admission. For mixed taxable/exempt use, the taxation coefficient is annual turnover giving recovery divided by total in-scope turnover, excluding VAT, capital-asset disposals and the narrowly defined incidental property/finance operations. Use the relevant separate sector where required. Round **each coefficient and the product upwards to two decimals**; settle the definitive coefficients before 25 April next year, or by 31 December next year for a person becoming liable during the year. This is a sourced method, not a default 50% deduction. [Art. 42; A-72–A-76](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

Admission is zero for the specified exclusions, including over-90%-private use, free staff/director lodging (except qualifying security staff), passenger transport except listed business transport, ordinary passenger/mixed vehicles and related costs, subject to the express resale/rental/driving-school/public-transport and other exceptions. For diesel and petrol used in excluded passenger vehicles, or rented vehicles whose rent VAT cannot be deducted, article 100 ter(4)(a) disallows **20%** of fuel VAT: use an admission coefficient of **0.80**, then apply the business-use and taxation coefficients. Natural-gas/LPG fuel for those vehicles has **50%** disallowance, hence **0.50** admission. Jet fuel for excluded aircraft and petroleum lubricants for excluded vehicles have zero admission under (d)–(e). Article 100 ter(4 bis) separately preserves the resale/processing exception, and (4)(a) the motor-manufacturing test exception. Do not transfer a vehicle-purchase exclusion indiscriminately to fuel. Keep an item-level recovery calculation. [Art. 100 ter(4)–(4 bis); A-73(IV)](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

**Capital adjustments and credits.** For fixed assets, track initial tax and reference coefficients over five years including acquisition year; buildings use twenty years. Annual adjustment is one fifth (one twentieth for buildings) of initial tax times the difference in deduction coefficients, with the A-74 test that the absolute change in business-use × taxation coefficients exceeds 0.10. Adjust before 25 April next year. Disposal, change of admission/use or movement between sectors can require the remaining-period adjustment under A-74(III), distinct from the annual test. Properly evidenced destruction/theft has specified exceptions. Omitted deductions can be entered distinctly before 31 December of the second year after omission. Carry excess credit forward or request an annual refund in January of at least EUR 150; an interim return-credit refund requires at least EUR 750. Remove the requested credit from available offsets so it is not claimed twice. Cessation can refund the whole residual credit; DSF can require a guarantee. [A-74–A-75, A-109–A-118](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

**Exempt supplies.** Before charging 20%, screen the ordinary exemptions: medical and paramedical care and specified education and training (article 23); granting, negotiating and managing credit, other specified financial operations, and insurance and reinsurance with related broker services (article 25); and letting of agricultural land and buildings, bare land and unfurnished premises (except parking) and furnished residential accommodation (article 26), unless the letting is hotel-type accommodation of up to thirty nights with at least three of breakfast, regular cleaning, linen and reception, or another listed exception. Exempt supplies carry no output VAT and reduce the article A-72 taxation coefficient. [Arts. 23, 25, 26](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

**Recipient-accounted services.** A general-rule B2B service supplied by a taxable supplier outside both Monaco and France to a Monaco taxable recipient is screened under articles 11 and 62(2). Self-assess output VAT and determine input recovery separately. Check special place rules first, including property, transport, events, hire and electronic services; the invoice address is not decisive. [Arts. 11–14, 42, 62(2)](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

## Deadlines and filing

Declare commencement to DSF within fifteen days under article 66 and obtain the article 68 identification appropriate to taxable supplies, acquisitions/imports or recipient-accounted services. A franchise recipient can still need identification for cross-border services. Article 70 requires an administration-prescribed return to the Recette des taxes, ordinarily monthly with monthly payment. Annual tax below EUR 4,000 permits quarterly declarations; exactly EUR 4,000 does not meet that condition. Cessation requires a declaration within thirty days. [Arts. 66, 68, 70](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

Under A-139, file ordinary declarations with Monaco DSF. A-144 allows DSF category-specific filing periods; absent one, the declaration must be submitted **before the 25th**. It moves the deadline to the next working day when it coincides with a public holiday or deemed holiday. Nil returns remain required, with the stated seasonal-closure exception. A-145 governs authorised extra time, not an automatic extension. Confirm the taxpayer's assigned calendar and actual form with DSF; no live return was filed for this research. [Annex, A-139, A-144–A-145](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

The government’s [e-TVA registration procedure](https://monentreprise.gouv.mc/en/themes/accounting-obligations-and-tax/tax/statements/how-to-register-for-e-vat), updated 27 August 2026 and read in the normal browser, specifies adhesion form **353-0013_01-2013**, SEPA mandate **353-0010_01-2013**, representative designation **353-0014_01-2013** if relevant and the bank-account identification document. Send/lodge the file with DSF’s Tax Division. DSF confirms the effective date, credentials and mandate reference by registered letter and sends the six-year security certificate to the nominated email. Use e-TVA from the confirmed effective date. Portal access is not created by merely recording a VAT number. No taxpayer account was accessed or return submitted for this research.

**Non-established liable persons.** First apply article 62 to identify who owes the tax: recipient accounting is a transaction-specific rule, not automatic for every foreign supplier. If a person established outside Monaco owes VAT or has declaration duties, article 72(I) requires a Monaco-established taxable representative accredited with DSF to undertake the formalities and payment; without one, the taxable operation’s recipient owes tax and related penalties. Do not import France’s general EU-person representation exceptions. Article 72’s second paragraph has its own narrow non-EU suspension/energy-only exception. Article 72 bis separately permits a qualifying agent where a person is neither established nor identified in Monaco/France and performs only the specified fully deductible imports or qualifying third-territory goods operations. That agent needs at least one year’s Monaco VAT identification and returns, DSF agent recognition, a written mandate and the specified goods-entrustment contract; the agent keeps separate mandated-operation declarations and bears statutory joint tax/penalty liability. Identify the applicable route with DSF, then apply article 68 identification and article 70 returns/payment. [Arts. 62, 68, 70, 72–72 bis](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

**Invoices and records.** Issue ordinary B2B invoices at supply; qualifying EU deliveries and recipient-accounted EU services have the fifteenth-of-next-month limit. Record names/addresses, relevant VAT IDs, issue and supply/advance dates, continuous unique number, precise quantities/descriptions, net unit prices, discounts, rate-by-rate net/tax totals, legal exemption reference or “Autoliquidation” where applicable. Keep invoice copies and a reliable audit trail; a credit note must specifically identify the original invoice. Article 66 requires six-year books/support retention; the general ten-year commercial-books duty remains separate. Electronic invoices require authenticity, integrity, readability and recipient acceptance under article 71, using documented controls, qualified signature/seal or the permitted structured-message system. Do not automatically import France’s staged platform mandate into this Monaco provision. For a French establishment, the French calendar requires receipt capability from 1 September 2026, with issue/e-reporting starting then for large/intermediate enterprises and 1 September 2027 for SMEs/micro-enterprises. French CGI article 290(I)(4)(a) expressly includes specified France–Monaco goods and service flows in the **French operator’s** transaction reporting. Article 290(II) separately covers non-established persons’ French-situated operations for which they are VAT liable, subject to its scheme exclusions. Classify the actual operator, establishment, supply and liable person; a Monaco VAT number alone does not establish a French reporting duty. [CGI art. 290, version at 25 October 2026](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546668/2026-10-25); [French government calendar](https://entreprendre.service-public.gouv.fr/vosdroits/F37169). [Arts. 66, 71-0–71; A-153–A-153 bis](https://legimonaco.mc/code/code-taxes-chiffre-affaires); [Commercial Code, art. 13](https://legimonaco.mc/code/code-commerce/).

## Penalties and interest

Article 110 sets 0.20% monthly late-payment interest on unpaid or deferred amounts, calculated from the first day of the month following the due month through the last day of the payment month. Article 111 adds a 10% late/non-declaration surcharge, escalating to 40% after the first unanswered thirty-day formal notice and 80% after the second; hidden activity also attracts 80%. Article 112 adds 40% for established bad faith on inaccurate/insufficient declarations, 80% for fraud. These provisions have different triggers; do not stack percentages without establishing the facts and applicable procedural rule. [Arts. 110–112](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

## Cross-border points

Treat Monaco–France movements under their common VAT/customs framework; a movement to France alone is not an intra-community export. For another EU member state, distinguish the following ordinary flows. [Convention, art. 15](https://legimonaco.mc/tai/convention/1963/05-18-tai1l000235/); [Code, arts. 2, 9, 31, 73–74](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

| Flow | Computation, evidence and reporting |
|---|---|
| Goods dispatched to an identified taxable customer in another EU state | Article 31 exemption requires actual dispatch, the communicated qualifying customer VAT ID, and the article 73 recapitulative statement. Keep contract, invoice, customer-ID validation, carrier/receipt and movement evidence; do not exempt an unreal destination or a sale merely because the buyer is foreign. Failure of the statement removes exemption unless duly justified to DSF |
| Goods acquired from another EU state for Monaco | Establish article 2/9 acquisition liability, assess Monaco VAT at the applicable goods rate and tax point, and claim article 42 input only to the proven recovery extent. Record acquisition and related VAT separately on the return |
| General B2B service to an identified business in another EU state | Establish recipient liability and absence of a special place rule, issue the appropriate reverse-charge invoice and file the article 73(III)/A-160 A service statement with DSF electronically by the tenth working day of the next month; franchise businesses have the stated paper-form option |
| Goods exported outside the EU | Article 29 requires actual export by/on behalf of seller or the qualifying non-Monaco/non-France buyer. Retain customs declaration/exit evidence, invoice and transport link; deduction can remain available under article 42(V). Tourist baggage/private craft and other special exports have additional conditions |
| Goods imported from outside the common customs area | Under articles 81/83/85 identify the actual liable importer, declare the valid VAT identifier to customs and reconcile customs data to the VAT return. Base = customs value plus non-VAT import duties/taxes and incidental costs to the first destination, plus known onward EU/Monaco destination costs. The customs representative must supply the base and import evidence for article 42 deduction. Do not book a foreign supplier invoice as domestic input VAT |

**Small-acquisition screen.** Before charging acquisition VAT to a non-taxable legal person or a taxable person carrying out only operations without a deduction right (including relevant franchise businesses), apply article 2(I)(2). Ordinary qualifying EU goods acquisitions remain outside acquisition VAT if the relevant VAT-exclusive acquisitions did not exceed **EUR 10,000 in the preceding calendar year** and do not exceed **EUR 10,000 in the current year at the acquisition**. Exactly EUR 10,000 meets the derogation; the acquisition that takes the total over it loses that condition, rather than taxing only the excess. Exclude new means of transport and excise goods from this derogation; they need their own liability test. Declare loss of the conditions under article 67 and obtain the article 68 identifier. A person eligible for the derogation can instead request taxation under article 18: effective from the first day of the election month, mandatory through **31 December of the second year after the election year**, then tacit two-calendar-year renewals unless cancelled before expiry. A 2026 acquisition election therefore runs through 31 December 2028; it is different from article 91's domestic-franchise election. Neither acquisition taxation nor identification creates an automatic input deduction for an exempt/franchise business. [Arts. 2(I)(2), 18, 42, 67–68](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

For EU goods, the Monaco declaration is lodged with **DSF**, by the tenth working day after the relevant month, separately for introductions/acquisitions and dispatches/deliveries. Dispatch fiscal data apply regardless of value for identified non-franchise suppliers; introduction/statistical obligations use A-154/A-158's EUR 460,000 annual flow threshold and the prior-year/current-year tests. For introductions/acquisitions, A-154(2) triggers the declaration at **EUR 460,000 inclusive**. The additional statistical-information test in A-156(3)/A-158(II) instead says prior-year flow **above** EUR 460,000 or a current-year crossing above it. Keep the declaration trigger separate from that additional-field test at exact equality; do not suppress the declaration by applying the latter to both. Correct known errors promptly under A-160. Keep the customer IDs, values, flow, period and statistical fields required by A-156; retain article 73 supporting documents six years. [Arts. 73–74; A-154–A-160 A](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

## Two worked examples that recompute

### Ordinary domestic standard-rated sale

Assume a correctly classified EUR 12,000 VAT-inclusive sale at 20%, and EUR 600 documented deductible input VAT in the same period. Net sales are EUR 10,000, output VAT EUR 2,000 and net payable EUR 1,400. No other transactions or carried credit exist.

```oa-check
name: Standard-rate VAT inclusive sale and allowed inputs
inputs:
  gross: 12000
  allowed_input: 600
steps:
  - net: gross / 1.2
  - output: gross - net
  - payable: output - allowed_input
expected:
  net: 10000
  output: 2000
  payable: 1400
```

### Foreign service with incomplete input recovery

Assume a taxable supplier established outside both Monaco and France supplies a EUR 2,000 general-rule B2B service that meets articles 11 and 62(2), has no special place rule and is standard-rated. Recipient VAT is EUR 400. A separately established deductible-use fraction of 50% gives EUR 200 input credit and EUR 200 net tax. The fraction is an assumed result of a separate deduction analysis, not a Monaco default.

```oa-check
name: Recipient VAT with a separately established deduction fraction
inputs:
  service: 2000
  deductible_fraction: 0.5
steps:
  - output: service * 0.2
  - input_credit: output * deductible_fraction
  - payable: output - input_credit
expected:
  output: 400
  input_credit: 200
  payable: 200
```

## Ask the client first

- What are the establishment, registration, franchise/option and assigned filing details?
- What are the transaction, tax point, goods route or service type, and customer status?
- What are prior/current-year national turnover and the relevant service subset?
- What invoice, taxable-use and deduction evidence supports each input?
- What prior credits, imports, foreign supplies, special schemes or cessation dates exist?

## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| French CGI art. 290(I)(4)(a), II–III and current version note, browser read | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546668/2026-10-25 | 2026-10-25 |
| French government company obligations, electronic issue/e-reporting calendar | https://entreprendre.service-public.gouv.fr/vosdroits/F37169 | 2026-10-25 |
| Code, arts. 2, 9, 11–14, 18, 29, 31, 35–42, 51–59, 23, 25–26, 62, 66–68, 70–74 (including 72 bis), 81–91, 95, 100 ter(4)–(4 bis), 110–112; annex A-72–A-76, A-109–A-118, A-139, A-144–A-145, A-153–A-160 A | https://legimonaco.mc/code/code-taxes-chiffre-affaires | 2026-10-25 |
| France–Monaco convention, art. 15 | https://legimonaco.mc/tai/convention/1963/05-18-tai1l000235/ | 2026-10-25 |
| Government e-TVA onboarding, all three procedure steps, read in normal browser | https://monentreprise.gouv.mc/en/themes/accounting-obligations-and-tax/tax/statements/how-to-register-for-e-vat | 2026-10-25 |
| Commercial Code, art. 13 | https://legimonaco.mc/code/code-commerce/ | 2026-10-25 |

**Not yet confirmed:** special margin/travel/online schemes, development property and the detailed classification of specialised reduced-rate products; these require their own primary-law analysis. Ordinary rates, input coefficients, trade and filing methods above do not establish eligibility for those schemes. Version 2.3 builds on the retained correction of the earlier unsourced Nice route and bank-name defaults.

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
