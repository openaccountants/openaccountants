---
name: uzbekistan-vat
description: "Use this skill whenever asked to prepare, review, or create an Uzbekistan VAT return or any VAT filing for an Uzbek business. Trigger on phrases like \"prepare VAT return\", \"Uzbekistan VAT\", \"STC filing\", \"soliq.uz\", \"E-faktura\", \"factura.uz\", or any request involving Uzbekistan VAT. Covers the 12% standard rate, E-faktura mandatory invoicing, input credit rules, turnover tax interaction, import VAT, and monthly filing to the State Tax Committee. ALWAYS read this skill before touching any Uzbekistan VAT work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/uzbekistan-vat"
  jurisdiction: "UZ"
  tax_year: "2026"
  last_updated: "2026-11-15"
---

# Uzbekistan VAT

## Scope

Prepare and review the Uzbekistan VAT computation, evidence schedule and monthly return workpaper. Distinguish ordinary VAT, the optional simplified VAT regime, turnover tax, imports and foreign-supplier tax-agent obligations. Currency is UZS. Contributor: Open Accountants Community.

Sources read on 14 November 2026 include the selected current Code and Presidential Decree PF-100. The Code's older turnover ceiling, importer-registration and certificate-suspension text must be reconciled with the later operative decree and official Tax Committee guidance. This Guide does not certify authenticated portal boxes or the historic numbered return layout. [PF-100, paras. 2, 5–9, 13](https://lex.uz/docs/-8236831); [Tax Committee current explanation](https://gov.uz/oz/soliq/news/view/196345).

## Ask the client first

- Obtain taxpayer identity/TIN and registration evidence, legal form, activity, special status, actual reporting month, annual cumulative turnover, regime elections/notices and transition dates. Check the actual TIN/registry record; the original nine-digit format assumption is not certified here.
- Obtain all bank/e-wallet/cash statements and sales/purchase ledgers, contracts, supply/completion dates, E-faktura/EHF records, returns/discounts and unpaid transactions. Reconcile gross card/platform sales separately from settlement fees.
- Obtain import/export customs documents, customs value/duty/excise/VAT payment evidence, transport route/contracts and export proceeds; identify foreign services, supplier registration and place of supply.
- Obtain taxable/zero/exempt/outside-scope activity evidence, FEZ/IT Park certificates and the specific applicable relief instrument; obtain business-use and common-cost allocations.
- Obtain prior returns, negative-balance/refund records, fixed-asset register, opening stock and transition inventory, invoice-risk/payment evidence and corrections. Establish whether the optional simplified VAT regime was actually elected.

## The method, step by step

### Rates, thresholds and regime dates

| Regime question | Rate / operative treatment | Official source |
| --- | --- | --- |
| Ordinary domestic VAT | Standard 12%; statutory zero rate for qualifying transactions; exemptions require an actual provision | [Code, arts. 243–245, 258–264](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Turnover/general-regime ceiling before 1 June 2026 | Older UZS 1,000,000,000 annual ceiling (source: “бир миллиард”, in words on the page), subject to activity exclusions and transition rules | [Code, arts. 237, 461–462](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| From 1 June 2026 | General-regime transition ceiling becomes 12,000 times BCV (source: “oʻn ikki ming baravari”, in words on the page); importer status alone no longer forces goods importers into VAT | [PF-100, paras. 2, 9(b), 13](https://lex.uz/docs/-8236831); [Tax Committee](https://gov.uz/oz/soliq/news/view/196345) |
| Derived ceiling June–August 2026; from 1 September 2026 | UZS 4,944,000,000 = 12,000 × 412,000; UZS 5,280,000,000 = 12,000 × 440,000 | [PF-100, para. 2](https://lex.uz/docs/-8236831); [PF-91, para. 3](https://lex.uz/docs/-7553322); [PF-115, para. 3(b)](https://lex.uz/docs/-8283656) |
| Voluntary ordinary VAT/general-regime election or threshold transition | Obtain election/effective date; crossing obligations and remaining activity exclusions still matter. Existing VAT payers below the new ceiling do not automatically switch back midyear; the following-year turnover route requires notice at least 10 days before that tax period | [Code, arts. 461–462](https://lex.uz/docs/4674902?ONDATE=21.10.2026); [Tax Committee FAQ I](https://gov.uz/oz/soliq/news/view/183078) |
| Turnover-tax rate context | Ordinary company default 4% with activity/location exceptions; IE/self-employed 1% from 1 January 2026. These are turnover-tax rates, not ordinary VAT rates | [Code, art. 467](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |

A turnover-taxpayer generally does not charge ordinary domestic VAT or claim ordinary input credit, but import VAT and tax-agent obligations can remain. Never infer no VAT obligation merely from the turnover return. [Code, arts. 237, 255, 461–462](https://lex.uz/docs/4674902?ONDATE=21.10.2026); [PF-100, para. 9](https://lex.uz/docs/-8236831).

The optional simplified VAT regime runs from **1 June 2026 until before 1 January 2030** for businesses whose main activity is catering, trade or services, excluding enterprises with state ownership **50% or more** and large taxpayers. It applies **6% to all sales turnover**, including exports; **0% profit tax** and no profit-tax return; **no input VAT credit**, no ordinary VAT exemptions/preferences/partial-VAT-refund benefits, and write-off of existing negative VAT. Customers may still claim VAT under their own credit conditions. Entry or exit takes effect on the **first day of the month after notification**. On return to ordinary VAT, prescribed credit may be available for VAT in the carrying value of remaining inventory and long-term assets. Do not combine this regime's output rate with ordinary input recovery or export zero-rating. [PF-100, paras. 5–7](https://lex.uz/docs/-8236831); [Tax Committee FAQ II–III](https://gov.uz/oz/soliq/news/view/183078).

### Classify the supply and tax point

For ordinary VAT, separate domestic taxable, zero-rated, exempt, outside-scope and non-supply movements. Goods place-of-supply follows dispatch/location rules. Services generally follow the buyer's location, with exceptions for immovable property, work on movable goods, specified physically performed activities, transport and electronic services. A foreign customer does not automatically make a service zero-rated: an outside-Uzbekistan place is outside scope, while statutory zero-rating requires its own category. Related-party, barter, free supplies and personal withdrawal of company assets require the deemed-supply/valuation rules; a personal bank transfer is not proof that a business asset withdrawal is untaxed. [Code, arts. 238–241, 248](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

Use the statutory invoice/dispatch/completion tax point, not bank receipt alone. Continuous utilities and relevant long contracts have monthly rules. The ordinary domestic base is agreed value excluding VAT and including applicable excise, subject to statutory market-value/special-base provisions. For VAT-inclusive ordinary consideration, extract VAT using **12/112**; do not add VAT again to an already inclusive amount. [Code, arts. 242, 247–248, 258, 265](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

| Original topic retained | Current ordinary-regime boundary | Official source |
| --- | --- | --- |
| Goods exports/transit and international transport | 0% only in the statutory category with contracts, customs/border or route evidence. “Export services” alone is insufficient | [Code, arts. 260–263](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Agricultural products | From 1 January 2026, listed products sold by qualifying growers may be 0%, excluding cotton and grain; no blanket agriculture exemption | [Code, art. 264](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Financial services/interest | Listed financial operations can be exempt; fixed-fee and nonqualifying services require separate analysis. Loan principal itself is not sales income | [Code, arts. 238, 244](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Education, childcare, funeral/religious and government services | Apply only the exact listed service, licensing/status and statutory conditions; do not exempt all government or education receipts | [Code, art. 243](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Medical services, public transport, residential rent, cultural/sporting services | The original broad exemption labels are not authority for these categories; check the current surviving provision or applicable special instrument before exempting | [Code, art. 243, including repealed items](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Insurance | Qualifying insurance/professional operations under the separate statutory conditions | [Code, art. 245](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Imports/CIS or other origin preferences | Check customs classification, qualifying import exemption and origin documentation; no blanket CIS VAT exemption | [Code, arts. 246, 254](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |

Ordinary goods-export input credit is generally proportional to currency proceeds received into the Uzbekistan bank account, with bank evidence. The disciplined-exporter exception requires timely receipts over the preceding **1 year** and no overdue export receivables; credit must be reversed proportionately if proceeds do not arrive within **180 calendar days** of export customs release. This is distinct from proving the output zero rate. Inputs to exported services whose place is outside Uzbekistan may qualify under article 266's specific credit rule. [Code, arts. 261, 266](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

### Match invoices, imports and foreign-supplier obligations

E-faktura/EHF is generally electronic, with statutory cash-receipt/other prescribed-document exceptions. Do not prescribe factura.uz as the exclusive authorized system. Ordinary invoices are issued/presented on the dispatch/service calendar date. Specified continuous utilities, communications, rail/forwarding/pipeline and long-construction cases use month-end invoices presented by the following month's **10th**; this is not a universal grace period of ten days after every supply. Reconcile supplier/customer identifiers, date, base, rate, VAT and receipt/acceptance status. [Code, art. 47](https://lex.uz/docs/4674902?ONDATE=21.10.2026); [Cabinet Resolution 489, Annex 2, paras. 1–9](https://lex.uz/docs/4948595).

Import VAT base = customs value + customs duty + applicable excise. Obtain the actual customs declaration and paid VAT; do not substitute a bank payment or invoice value for the customs base. Excise is computed before VAT for this base; rates/classification require the current excise chapter and customs evidence. [Code, art. 254; Chapter 41](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

For foreign suppliers, first establish Uzbekistan place of supply, supplier registration and the statutory tax-agent category, including any electronic-service rule. No permanent establishment alone is insufficient. Article 255 generally treats supplier income as VAT-inclusive unless the contract excludes VAT from that income. Thus a net-of-VAT contract and an inclusive contract produce different liabilities; document the wording before computing. Payment/credit periods must follow the applicable agent and input conditions, including for a non-VAT/turnover payer. [Code, arts. 241, 255, 266, 273](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

### Determine ordinary input credit, blocked amounts and adjustments

Credit generally requires actual receipt, taxable/zero-rated business use, supplier VAT registration and an invoice **or legally qualifying other supplier document separately showing VAT**; imports and statutory agent cases require actual budget payment. A bank debit or missing EHF alone does not establish either permanent entitlement or permanent denial. Reconcile missing documents and timing before claiming. Sham transactions remain excluded. [Code, arts. 266–267](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

High-risk invoices require the article 266¹ buyer/tax-agent budget-payment route to unlock credit. Generally the paid-tax period controls; where payment occurs before the invoice period's filing deadline, the statutory invoice-period rule can apply. A supplier's high-risk output invoice does not by itself remove its own valid input rights. Low-risk status does not validate a sham transaction. PF-100 cancels the temporary VAT-certificate suspension procedure; do not continue to apply that older Code mechanism as current. Invoice risk and actual tax-payment checks remain a separate issue. [Code, arts. 266¹–267](https://lex.uz/docs/4674902?ONDATE=21.10.2026); [PF-100, para. 9(a)–(b)](https://lex.uz/docs/-8236831).

Blocked/noncreditable categories include exempt-use inputs/capital projects, purchases by nonpayers, representation expenses, free receipts except where the recipient pays the tax, and qualifying nondeductible personal-use costs. Cars, motorcycles, aircraft, boats, other motor vehicles/fuel, alcohol and tobacco are blocked **when unrelated to the business activity**, not by an absolute vehicle ban or an “only producers” exception. Gifts must be analyzed as free receipts/supplies under their actual facts. Ordinary VAT is not charged on salary or tax payments. [Code, arts. 238–239, 267](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

For mixed taxable/exempt operations use documented separate allocation and/or the proportionate method. Directly allocate attributable costs; common costs that cannot be separated use the taxable-to-total turnover ratio, excluding VAT, determined cumulatively in the current calendar year. The **5% or less taxable-share** option permits the statutory full cost treatment; it is not a general right to recover all input. Do not multiply every purchase indiscriminately by a single monthly ratio. Capital assets, changes to exempt/personal use, losses, cancellations/corrected invoices, status changes and bad debts have their own credit adjustment/recredit rules. [Code, arts. 268–271](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

On entry to ordinary VAT, qualifying opening inventory acquired in the previous **12 months** and still held can receive credit; long-term assets use the VAT-bearing residual carrying value without revaluation, subject to evidence/conditions. Prepare an inventory and asset schedule; the old blanket denial of pre-registration input is wrong. Simplified-to-ordinary transition also has PF-100's balance-sheet credit rule. [Code, art. 266](https://lex.uz/docs/4674902?ONDATE=21.10.2026); [PF-100, para. 7(b)](https://lex.uz/docs/-8236831).

### Bank-language evidence and return workpaper

Preserved narration library - establish the contract, gross amount, tax point, regime and supporting invoice before assigning VAT:

| Pattern | Classification lead |
| --- | --- |
| PEREVOD OT [client], TRANSFER FROM; KARTA POPLNENIYE, KARTA POPOLNENIYE, CARD CREDIT | Customer/card receipt or transfer; match sales and own-account movements |
| PAYME SETTLEMENT, PAYME CREDIT; CLICK SETTLEMENT, CLICK UZ; UZCARD SETTLEMENT; HUMO SETTLEMENT | Reconcile gross sales, settlement fees and VAT separately |
| PROTSENTY, INTEREST | Test listed financial exemption and contract; not every “interest” credit qualifies |
| KREDIT, LOAN | Match principal/financing movement, separate interest and charges |
| ARENDA OFISA, OFFICE RENT | Business rent: ordinary input only with qualifying tax/documentation |
| ELEKTR ENERGIYA, ELEKTRENERGIYA, ELECTRICITY; GAZ, NATURAL GAS | Utilities: business use, invoice and month-end rule |
| BEELINE, UCELL, UZMOBILE, MOBIUZ | Telecom: establish business share and qualifying document |
| YANDEX TAXI, TAXI | Document business purpose and actual invoice/receipt eligibility |
| AVTOMOBIL, VEHICLE | Apply business-related use test, not a blanket motor-vehicle exclusion |
| PRAZDNIK, BANKET, ENTERTAINMENT | Representation restriction and actual underlying event |
| NALOG, TAX PAYMENT, STC | Tax payment reconciliation, no ordinary purchase VAT |
| ZARPLATA, SALARY | Employee salary, no purchase VAT |
| LICHNIY PEREVOD, PERSONAL | Match private transfer; examine any separate deemed business-asset supply |

Preserved export-format specimens are **not certified current bank specifications**: NBU PDF `Data / Opisaniye / Debet / Kredit / Ostatok`; Kapitalbank CSV/PDF `Sana / Tavsif / Chiqim / Kirim / Qoldiq`; Ipoteka Bank CSV `Date / Description / Debit / Credit / Balance`; Hamkorbank PDF `Sana / Bayonnoma / Chiqim / Kirim / Qoldiq`; Uzpromstroybank CSV `Date / Narration / Debit / Credit / Balance`; InfinBank CSV `Date / Details / Withdrawal / Deposit / Balance`. Read actual supplied headers/signs. General banking terms retained: `PEREVOD / TRANSFER`, `OPLATA / PAYMENT`, `POSTUPLENIE / RECEIPT`, `NALOG / TAX`, `ZARPLATA / SALARY`, `PROTSENTY / INTEREST`, `KREDIT / LOAN`.

Retain the original internal workpaper structure: **A1** taxable turnover, **A2** output VAT, **A3** zero-rated turnover, **A4** exempt turnover (add outside-scope separately); **B** domestic input, import input, blocked input and allowed credit, with agent/high-risk/adjustment schedules; **C** output less allowed credit, brought-forward negative balance, adjustments, net payable/credit and refund request. For simplified VAT create a separate all-turnover/no-input calculation and opening negative-balance write-off.

The old “13 parts” are retained as **internal workpaper destinations only**, not certified current form boxes: **1** taxpayer identity; **2** taxable turnover; **3** zero-rated turnover; **4** exempt turnover; **5** total; **6** output VAT; **7** domestic input; **8** import input; **9** total allowed credit; **10** net; **11** carryforward; **12** payable/credit; **13** adjustments. Reconcile ledgers, invoice registers, customs, payments, taxable dates, prior carryforward and current return before submission. A numbered destination in an original case below refers to this workpaper only.

## Boundary and exception table

| Condition | Action |
| --- | --- |
| Unknown regime or election date | Stop return finalization; do not assume ordinary VAT from bank credits |
| Turnover taxpayer | R1 routes domestic turnover returns; separately test imports and agency obligations |
| FEZ, IT Park, foreign-investment or special agricultural relief | Obtain exact current instrument, registration, qualifying activity and expiry. FEZ status or IT Park name alone gives no blanket VAT/import exemption |
| Exports/services/foreign suppliers | Verify supply place, output category, contract VAT clause, customs/route/proceeds and credit conditions |
| Missing invoice, registration or payment evidence | Hold the disputed credit; obtain statutory alternative/correction evidence; do not label it permanently lost without analysis |
| Mixed activity/capital assets/transition | Apply separate/common allocation and actual inventory/residual-value adjustments |
| Complex holdings, transfer pricing or subsoil activity | R3/R4 referral; do not improvise ordinary simplifications |

### Not yet confirmed - unusable legacy assertions

The old default treating every business bank credit as taxable at the standard rate is unusable without supply/regime evidence. The old universal quarterly filing, universal ten-days-after-supply invoicing, blanket medical/public-transport/residential-rent/cultural-sport/agricultural exemption, immediate “register within ten days” shortcut, and no opening-stock credit are not usable instructions. The preserved TIN-format and bank-export descriptions need actual registry/client-file evidence. Current authenticated portal fields and the old numbered return parts are not certified. Factura.uz was an original example, not a verified exclusive filing/invoice provider.

The old penalty claims - **1% per day capped at 10%**, fixed **0.04% daily** interest, **50%** underdeclaration and **200%** fraud - are retained solely as rejected legacy assertions, not permissible rates for any calculation. Use a dated offence-specific assessment under the sources in Filing and payment below. Original chapter/article pointers for import VAT, blocked input and excise are replaced by the operative provisions cited above.

## Worked cases

These retain the complete original amounts, currency assumptions and counterparties. The historical source amounts are inputs, not current exchange rates. Ordinary-regime cases require actual eligibility/documents and no simplified-regime election. [Original case record](https://github.com/openaccountants/openaccountants/blob/264a22625593d55de372f43cfb8f697f8c4a2589/skills/uzbekistan/uzbekistan-vat.md).

### Original domestic sale; ordinary versus simplified regime decision

Original input: domestic net sale **100,000,000**, VAT **12,000,000**, ordinary regime, E-faktura issued. Ordinary output is **12,000,000**; internal workpaper Part **2** base **100,000,000**, Part **6** output **12,000,000**. An otherwise eligible simplified-regime taxpayer on the same tax-exclusive turnover has **6,000,000** output and no input recovery; ordinary credit/refund benefits cannot be mixed into that result. Before choosing, model actual costs/credits, existing negative balance, exemption/export loss and customer pricing; the output difference alone does not establish total tax savings.

```oa-check
name: Ordinary versus simplified output on identical net turnover
inputs:
  net_sales: 100000000
steps:
  ordinary_output: net_sales * 0.12
  simplified_output: net_sales * 0.06
  output_difference: ordinary_output - simplified_output
expected:
  ordinary_output: 12000000
  simplified_output: 6000000
  output_difference: 6000000
```

### Original imported equipment

Original customs value **200,000,000**, duty **20,000,000**, excise assumed **0**: import VAT base **220,000,000**, VAT **26,400,000**. Internal workpaper Part **8** records import VAT. Full ordinary input credit of **26,400,000** requires actual customs payment, taxable business use and the other statutory conditions; simplified VAT gives no input credit. “Full credit allowed” in the old fixture was conditional, not automatic.

```oa-check
name: Equipment customs base and conditional ordinary input
inputs:
  customs_value: 200000000
  duty: 20000000
  excise: 0
steps:
  base: customs_value + duty + excise
  import_vat: base * 0.12
expected:
  base: 220000000
  import_vat: 26400000
```

### Original foreign IT service, contract-clause decision

Original input: Uzbek company pays **USD 10,000**, recorded as **UZS 128,000,000**, to a **Russian IT firm**; no VAT charged and original no-PE assumption. Preserve that historic currency conversion solely as the fixture. It is not an exchange-rate instruction. First prove Uzbekistan supply place and the statutory unregistered foreign-supplier agent conditions; no PE alone does not settle liability.

If **128,000,000 is contractually VAT-exclusive**, agent VAT is **15,360,000**. If it is the supplier's **VAT-inclusive income**, extracted VAT is **13,714,285.71** (derived, rounded for this illustration; actual return rounding must follow the form). The original output/input **15,360,000** and **net zero** result is available only in the exclusive-contract scenario with actual paid tax and all ordinary-credit/timing conditions. Do not net the cash remittance to zero or give a turnover/simplified taxpayer ordinary input credit.

```oa-check
name: Foreign-service VAT-inclusive versus exclusive contract
inputs:
  contract_amount: 128000000
steps:
  exclusive_vat: contract_amount * 0.12
  inclusive_vat: round(contract_amount * 12 / 112, 2)
  ordinary_credit_if_all_conditions: exclusive_vat
  eventual_net_if_same_period_allowed: exclusive_vat - ordinary_credit_if_all_conditions
expected:
  exclusive_vat: 15360000
  inclusive_vat: 13714285.71
  eventual_net_if_same_period_allowed: 0
```

### Original purchase without E-faktura

Original purchase net **30,000,000**, stated VAT **3,600,000**, no supplier E-faktura. The old fixture recorded input VAT **0**, “BLOCKED,” and VAT as a cost. Preserve the missing-document scenario, but reject its absolute permanent-denial conclusion: first check a lawful alternative supplier document, supplier VAT registration, actual business use and any required risk/agent payment. Pending adequate evidence, claim **0** in this workpaper; if all statutory conditions are subsequently established, assess credit **3,600,000** in the correct period. Do not manufacture an invoice or claim from the bank debit alone.

## When to refuse or refer

**R1:** domestic turnover-tax return belongs to that regime, while import/agent VAT remains separately tested. **R2:** FEZ relief requires the exact current decree and documentary conditions; hold any unsupported exemption. **R3:** refer transfer pricing and subsoil-user special regimes. **R4:** refer complex multi-entity/holding structures. Also hold unresolved tax points, foreign supply place, contract VAT clauses, simplified-regime election, missing invoice/payment evidence and refund disputes.

Prohibitions retained: do not confuse exempt supplies with zero-rated supplies, claim credit from a bank statement alone, invent E-faktura data, treat a vendor as the exclusive authorized system, automatically credit personal/nonbusiness or exempt-use purchases, import foreign VAT as Uzbek input VAT, apply exemptions merely from a sector name, mix turnover and VAT computations, omit customs/agency VAT, carry the old penalty figures forward, or submit without qualified Uzbekistan professional review. Do not apply ordinary export zero-rating/input credit inside the simplified regime.

## Filing and payment

For tax filing, payment and notice deadlines expressed in days, count working days unless the provision expressly says calendar days; apply the next-working-day rule when the final date is nonworking. [Code, art. 5](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

| Obligation | Due/procedure | Official source |
| --- | --- | --- |
| Ordinary domestic VAT | Calendar-month period; return and payment by the following month's 20th, including the actual liability/negative balance | [Code, arts. 259, 272–273](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Goods imports | Customs-law payment/release procedure; retain paid-tax evidence | [Code, arts. 254, 273](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Specified non-VAT tax agent | By the 20th of the month following the foreign-supplier payment month; confirm the exact agent category and corresponding filing | [Code, art. 273](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Negative VAT | Ordinary carryforward/refund rules and evidence apply. PF-100 provides automatic no-application/no-associated-refund-audit treatment for negative amounts up to UZS 10,000,000; do not promise automatic processing for a different amount/category | [Code, arts. 272–274](https://lex.uz/docs/4674902?ONDATE=21.10.2026); [PF-100, para. 9(g)](https://lex.uz/docs/-8236831) |

Use the [Taxpayer Cabinet](https://my.soliq.uz) with the currently applicable VAT calculation, invoice registers, import/agency and adjustment schedules. The unauthenticated portal fetch timed out and authenticated screens were not inspected; the internal numbered workpaper is not authority for form boxes. Match actual screen labels, tax period, regime, taxpayer, sales categories, allowed input, carryforward/adjustments and payment; resolve form differences with a qualified Uzbekistan practitioner before filing. Keep the submitted return, acknowledgement, invoice/customs evidence, refund request/status and payment reconciliation. Separate ordinary chapter-39 foreign digital-supplier rules if applicable rather than assigning quarterly filing to all domestic taxpayers.

For late payment, article 110 uses daily interest at **1/300 of the then-current Central Bank refinancing rate**, subject to its exceptions. Article 220 addresses late reporting through administrative responsibility; article 223's hidden-base offence uses **20% of the hidden base** plus the tax, while article 224's incorrect underpayment offence generally uses **20% of unpaid tax** subject to its exclusions. Article 225's wrongly stated VAT offence uses **20% of the stated VAT** plus payment of that VAT. These offences have different triggers/bases; refer the actual facts before assessing, rather than stacking all penalties. [Code, arts. 110, 220, 223–225](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

## Completion checklist

- Registration, threshold/date windows, exclusions and any simplified election/exit are evidenced.
- Sales and bank settlements reconcile gross/net, tax points, supply place, rate, exemption/zero evidence and invoices; unmatched items remain flagged.
- Credits reconcile supplier documents, actual receipts, customs/agent payments, risk rules, business use, mixed-cost allocation, capital/transition adjustments and export proceeds.
- Ordinary versus simplified calculations use their own output/input/carryforward rules; no invented form boxes or blanket sector exemptions remain.
- The current return, monthly due date, net payment/refund and supporting schedules reconcile; a qualified professional reviews before submission and acknowledgements/payment evidence are retained.

## Sources

Opened/read **14 November 2026**: [Tax Code, Uzbek original, selected 21 October 2026 edition](https://lex.uz/docs/4674902?ONDATE=21.10.2026), arts. 5, 47, 110, 220, 223–225, 237–274, 461–470 and Chapter 41; [Russian parallel text](https://lex.uz/ru/docs/4674893?ONDATE=21.10.2026) alongside the original; [PF-100, 26 May 2026, current 28 August edition](https://lex.uz/docs/-8236831); [Tax Committee threshold/regime explanation](https://gov.uz/oz/soliq/news/view/196345); [Tax Committee June FAQ](https://gov.uz/oz/soliq/news/view/183078); [PF-91, base values](https://lex.uz/docs/-7553322); [PF-115, 2026 changes](https://lex.uz/docs/-8283656); [Cabinet Resolution 489, current invoice/refund regulations, 15 October 2026 edition](https://lex.uz/docs/4948595). Sector/FEZ/IT Park relief and authenticated portal fields remain conditional as identified above. Historical changelog retained: **1.0**, **2025**, initial version; **2.0**, **April 2026**, rewrite with bank formats, Payme/Click/UzCard/Humo patterns, cases and E-faktura integration. Earlier **2.0** content is preserved by topic and historical fixture, with corrected source boundaries in this **2.1** revision.


Not yet confirmed: authenticated current return fields; any uncited sector/FEZ/IT Park relief; the legacy assertions and bank/registry specifications held above are unusable pending evidence.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed auditor or tax consultant practicing in Uzbekistan) before filing or acting upon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-15. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `uzbekistan-vat` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/uzbekistan-vat. If neither is available, confirm every figure against the official source pages cited above before relying on it.
