---
name: pk-sales-tax-federal
description: Use for pakistan federal goods sales-tax computation and return. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return.
jurisdiction: PK
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
version: 2.1
type: computation
---

# Pakistan federal goods sales-tax computation and return v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Pakistan registered suppliers/importers/manufacturers/wholesalers/distributors/retailers preparing federal goods sales-tax working papers for the 2025-2026 filing cycle. This skill distinguishes the 2025 amended Act and the Rules consolidation updated 1 January 2025 from later amendments: load `pk-einvoice` for 2026 digital-invoice operations and check the actual supply-period amendment before later returns. Use `pk-sales-tax-services` for provincial/ICT services and `pk-withholding-tax` for income tax. Load `vat-workflow-base` alongside this skill.

Quick answer: establish goods classification, supply date, registration, valuation, schedules/notifications and actual input evidence before computing. Unknown facts do not become 18% domestic taxable supplies simply because that was the old default.

## Ask the client first

Obtain legal identity/NTN/STRN, period/category/status, all bank/wallet statements, sales/purchase/import/export invoices and ledgers, contracts, goods/PCT descriptions, delivery/payment dates, return/purchase-data extracts, POS/digital-invoice data, customs GD s/BL/shipping and export evidence, prior carry-forward, debit/credit notes, withholding certificates, payment CPRs, stock/production movements and every SRO relied upon. Bank data alone is insufficient to substantiate tax credits or sale classification. Reconcile missing documents rather than infer tax from bank names. Keep HBL/UBL/MCB/Allied/Alfalah/Meezan/Standard Chartered, Bank Al-Habib, Faysal, JS, Soneri, Askari, Habib Metro, Silk, Summit and other historic bank-labelled records, plus JazzCash/Easypaisa/NayaPay/SadaPay, within the same completeness review.

## Rates, bands and thresholds

| Rule and conditions |2025-2026 cycle position | Official source |
|---|---|---|
| Ordinary taxable goods/imports |18% of value, subject to particular schedules/notifications; the 17 to 18 change came from Finance(Supplementary)Act 2023, not July 2024 | [Act s.3(1) and footnote 130](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf) |
| Further tax |4% in addition to applicable tax where recipient lacks registration or is not active, **subject to statutory/notified exclusions**; not universal 3% or universally due on every unregistered sale (4% rate in words on the page) | [s.3(1 A)](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf) |
| Cottage manufacturer exclusion | All four: no industrial gas/electric connection; residential location; at most 10 workers; all-supply turnover≤8,000,000 (in words on the page) | [s.2(5 AB)](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf) |
| Tier 1 retailer electricity marker | Immediately preceding 12 consecutive months' electricity bill>1,200,000; other independent markers also apply (amount in words on the page) | [s.2(43 A)](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf) |
| Input delayed claim | Relevant period **plus 6 succeeding tax periods**, subject to ss.7/8/8 B/73 (6 succeeding periods in words on the page) | [s.7(1)](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf) |
| Ordinary input adjustment restriction |90% of period output tax; fixed-assets/capital-goods exception, notified exclusions, annual adjustment/refund and risk-system branches must be tested (90% limit in words on the page) | [s.8B](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf) |
| Banking payment evidence | Transactions>50,000 aggregate to one supplier in a tax period; utilities exception; credit payment within 180 days of tax-invoice issuance; prior-approved netting conditions (amount and period in words on the page) | [s.73](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf) |
| Ordinary revised return | Within 120 days from filing, Commissioner approval; within 60 days higher tax/lower refund branch needs no approval unless risk-system restriction (120-day and 60-day windows in words on the page) | [s.26(3)-(3 A)](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf) |
| Late-return penalty |10,000; if filed within 10 days of due date,200 per default day instead (10,000/200 amounts and 10-day period in words on the page) | [s.33 item 1](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf) |
| Ordinary default surcharge | Higher of 12% yearly or KIBOR+3%; fraud 2% monthly is a separate branch, with statutory accrual windows (12%, 3% and 2% rates in words on the page) | [s.34](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf) |
| Record retention |6 years from end of relevant tax period; pending proceedings/final-decision period can extend it (in words on the page) | [s.24](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf) |

## Registration, time and value

Section 14 is category-based: manufacturer except cottage, liable retailer except specified electricity-bill scheme, importer, exporter intending refund, wholesaler/dealer/distributor and other-law levy categories. There is **no blanket 10,000,000 turnover registration rule**. Section 14(1 A)-(1 B) adds domestic digitally ordered goods and marketplace/courier registration controls, with its own exceptions. Read actual compulsory/voluntary/deregistration rules for the case. [s.14](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf).

Tier 1 also includes national/international chains, air-conditioned mall/plaza/centre except kiosks, wholesaler-retailer bulk import, acquired card/SBP-authorised digital-payment POS, notified 236 G/236 H withholding threshold and prescribed categories. The old 100,000,000 turnover/10 outlet guesses are not legal triggers. Check actual POS/integration status and remit applicable schedules; do not assume every air-conditioned shop is an air-conditioned mall. [s.2(43 A)](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf); `pk-einvoice`.

For ordinary goods the time of supply is earlier delivery/making available or receipt of payment; hire purchase uses agreement time and part-payment provisions matter. Invoice issue alone is not an independent ordinary-goods trigger in s.2(44)(a). Use actual value-of-supply law, including related-party/open-market, discount, import and retail-price branches; do not treat every bank receipt as tax-inclusive consideration. [ss.2(44),(46)](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf).

Where the legally established rate is 18% and gross includes only that tax, net=gross/1.18 and tax=gross-net. Where **both 18% and 4% further tax actually apply** on the same value, gross=value×1.22; split each levy. The invoice's real pricing agreement and statutory further-tax exclusion must be established first. [ss.3/7](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf).

## The method, step by step

1. Classify each sale as the supported taxable rate, zero-rate, exempt or outside this return; obtain actual schedule/PCT/SRO conditions. Section 4/Fifth Schedule zero-rating is different from s.13/Sixth Schedule exemption. Neither basic food, medicine, agricultural inputs, education/health goods nor solar/renewable goods receive a blanket exemption by label.
2. Compute output/further/other applicable tax separately and reconcile invoice/POS/GD/ledger. Imported goods follow Customs assessment; imported SaaS/digital services require service/recipient/authority analysis, not automatic federal 18%.
3. Test taxable-business use and s.7 documentary branches: domestic invoice in buyer's name/registration; electricity/gas bill with registration/location; own-name customs GD/import entry; auction treasury challan. Check supplier declaration/payment, purchase-data matching and applicable r 18 supplier-filing/provisional-return rules. Annex A visibility alone is not the whole entitlement, and an absent input document does not remove output liability. [ss.7/8](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf); [r 18](https://download1.fbr.gov.pk/Docs/20251141513138962Sales-Tax-Rules-2006-UpdatedUpto01-01-2025.pdf).
4. Apply s.8 exclusions: nontaxable/private/nonbusiness use; unpaid/unverifiable/fake invoice supply-chain issues; specified goods under s.3(5); information failure; immovable-property materials with resale/direct-production/prefabricated exceptions; specified vehicles/parts/appliances/furniture/office equipment with resale exceptions; barred provincial-service inputs; specified agricultural machinery and undocumented unregistered-distributor invoices. Do not replace actual statutory categories with a vague passenger-car-only rule. Mixed taxable/exempt activity requires s.8(2) apportionment and actual current rules. [s.8](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf).
5. Establish s.73 business-bank transfer evidence above the aggregate threshold, utility exception,180 day credit period from tax-invoice issuance and approved netting conditions. A cash bank withdrawal does not prove supplier payment; wallet identity alone proves no credit. The 180-day period is in words on the page. [s.73](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf).
6. Apply s.8B only after admissibility and exceptions, keeping further tax outside ordinary input offset under s.7. Preserve fixed/capital assets, notified sectors, annual certified-adjustment/refund and risk-system variation/contest branches. Do not automatically call all unadjusted tax refundable or treat a 90% ratio as a statutory audit-selection rule. [ss.7/8 B](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf).

## Invoices, digital operations and records

Section 23 requires serial/date, supplier identity/address/registration, recipient particulars, goods description/quantity, value excluding tax, tax and inclusive value, with modified-invoice rules. The NIC/NTN branch is specifically manufacturer/importer supplies to an unregistered distributor, with card/digital-payment NIC exception; the old universal unregistered-buyer 100,000 rule is not the operative text read here. Goods transport/e-bilty linkage and applicable electronic reporting need their actual implementation. [s.23](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf); `pk-einvoice`.

Keep ss.22/24 invoice, debit/credit-note, purchase/import/supply/zero/exempt, bank/payment, inventory, utilities, salary/labour/cash/rent and double-entry records. Do not confuse income-tax ATL surcharge with sales-tax active-status restoration: s.21A/rules and actual compliance status apply, not old 20,000/10,000/1,000 income-tax amounts. Suspect/flying invoices, suspended status and supply-chain mismatch require investigation; s.8(1)(ca) specifically addresses unpaid supplier tax, not a word-for-word universal supply-date ATL rule. [ss.8/21 A/22/24](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf).

## Deadlines and filing

The read Rules require STR 7 and electronic submission; applicable information must be complete. For ordinary cases whose prescribed date is 15th, r 18(9) provides payment 15th and filing 18th. It also contains special utility/power/petroleum dates and **quarterly CNG/Tenth Schedule brick-kiln branches**; no universal monthly assertion. Rule 18(3)'s supply/debit-credit data by 10 th, buyer purchase-data and seller-filing reconciliation require the actual period's amendments/extension check. More-than 6 months-late return needs Commissioner approval under r 14(3). The 6-month late-return period is in words on the page. [Rules 14/18](https://download1.fbr.gov.pk/Docs/20251141513138962Sales-Tax-Rules-2006-UpdatedUpto01-01-2025.pdf).

Rule 17's STR 10 annual return applies registered private/public limited companies, by 30 September following financial year; manufacturing alone is not that rule's trigger. For later periods check amended forms/rules rather than promise the 1 January 2025 consolidation is current to November 2026. [r 17](https://download1.fbr.gov.pk/Docs/20251141513138962Sales-Tax-Rules-2006-UpdatedUpto01-01-2025.pdf).

| STR 7 annex | Correct function in the read official form |
|---|---|
| A | Domestic purchase invoices |
| B | Imports |
| C | Domestic sales invoices |
| D | Exports |
| E | Federal excise, separately reviewed |
| F | Carry-forward summary |
| G | Sales-tax arrears |
| H | Input-consumption/stock/refund statement |
| I | Debit/credit notes |
| J | Production data for applicable manufacturers |

[Rules STR 7/annexes](https://download1.fbr.gov.pk/Docs/20251141513138962Sales-Tax-Rules-2006-UpdatedUpto01-01-2025.pdf). Actual portal return made available by the Board and subsequent changes must be checked. Reconcile books, opening credit, annex data, tax due, payment instruction/PSID, actual bank CPR and submitted acknowledgment. A CPR is payment evidence, not something merely generated before payment. Do not promise a particular authentication/upload/API screen or payment provider without current instructions.

## Worked cases

### Original Karachi garment manufacturer May 2026 case retained

Original case: registered cotton-garment manufacturer in Karachi, May 2026, active since 2022, goods B2B/export only and not a Tier 1 retailer. Preserve all 8 original lines: 3 May cotton T-shirt sale to RETAILER A (Tier 1, registered, illustrative STRN 1234567-8), gross 5,900,000; 7 May T-shirt sale to unregistered KIRYANA STORE B, gross 1,100,000; 12 May T-shirt export to ACME USA INC, 8,000,000 inward USD-equivalent, GD KHI-EXP-2026-3344; 15 May cotton-yarn purchase from registered YARN MILLS LTD (illustrative STRN 7654321-2), gross 4,720,000; 18 May dyes/chemicals import GD KHI-IMP-2026-9988 with sales tax **1,180,000 itself**; 20 May K-ELECTRIC electricity bill, gross 590,000; 22 May purchase from XYZ TRADERS, gross 944,000, later suspected/suspended supplier; and 28 May fabric-scrap sale to UNREGISTERED RECYCLER, gross 220,000. These are hypothetical labels, identifiers and references, not validated real documents.

Assume taxable classifications/rates are independently confirmed, further-tax exclusions do not apply to the 2 unregistered sales, stated gross values include the actual taxes, export conditions met, domestic yarn/utility tax admissible and import GD supports the stated tax. Hold XYZ's 144,000 input pending actual status/payment/disallowance evidence rather than claim it blindly. No exemption from s.8B or fixed/capital asset applies in this conditional arithmetic.

```oa-check
name: Garment manufacturer complete output split
inputs:
  registered_gross: 5900000
  unregistered_gross: 1100000
  scrap_gross: 220000
  export_value: 8000000
steps:
  - registered_net: registered_gross / 1.18
  - registered_tax: registered_gross - registered_net
  - unregistered_combined_net: (unregistered_gross + scrap_gross) / 1.22
  - unregistered_standard_tax: unregistered_combined_net * 0.18
  - further_tax: unregistered_combined_net * 0.04
  - ordinary_output: registered_tax + unregistered_standard_tax
  - total_output_and_further: ordinary_output + further_tax
expected:
  registered_net: 5000000
  registered_tax: 900000
  unregistered_combined_net: 1081967.21
  unregistered_standard_tax: 194754.1
  further_tax: 43278.69
  ordinary_output: 1094754.1
  total_output_and_further: 1138032.79
```

```oa-check
name: Garment manufacturer admissibility and conditional90percent restriction
inputs:
  yarn_gross: 4720000
  utility_gross: 590000
  supported_import_tax: 1180000
  held_supplier_gross: 944000
  ordinary_output: 1094754.1
  further_tax: 43278.69
steps:
  - yarn_input: yarn_gross - yarn_gross / 1.18
  - utility_input: utility_gross - utility_gross / 1.18
  - held_not_claimed: held_supplier_gross - held_supplier_gross / 1.18
  - supported_input: yarn_input + utility_input + supported_import_tax
  - ordinary_limit: ordinary_output * 0.9
  - adjusted_input: min(supported_input, ordinary_limit)
  - unadjusted_input: supported_input - adjusted_input
  - payable: ordinary_output - adjusted_input + further_tax
expected:
  yarn_input: 720000
  utility_input: 90000
  held_not_claimed: 144000
  supported_input: 1990000
  ordinary_limit: 985278.69
  adjusted_input: 985278.69
  unadjusted_input: 1004721.31
  payable: 152754.1
```

The old displayed import base 6,555,556 is a reverse calculation:1,180,000/18%=6,555,555.56 (derived), not an independently assessed Customs valuation. Amounts rounded for display; final return uses operative rounding. **No refund 570,782.30 is certified**: the old turnover-ratio shortcut on restricted input does not establish a lawful export refund. Allocate actual inputs/stocks/export consumption and apply current refund rules/FASTER eligibility. The export 8,000,000 has 0 output only after actual conditions; the import 1,180,000 is tax input, not gross invoice. Manufacturer output does not acquire a retailer concession merely because the buyer is Tier 1. May 2026 ordinary 15/18 June dates remain subject to actual extension/category evidence.

## Penalties, refunds and special regimes

Use the table's sourced late-return/default rules for that law period, preserving actual accrual windows and voluntary revised-return s.26(4) relief conditions. Fraud, failure to register/invoice/pay, nonintegration, investigation/criminal and recovery cases require exact s.33/offence/default-date assessment. Old fake-invoice 25,000/100%, POS 60% disallowance and other summaries are not cleared merely by citing s.37A. Do not promise no penalty solely because a payment was voluntary. [ss.26/33/34](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf).

Section 66's 1 year rule concerns tax paid/overpaid through error/inadvertence/misconstruction and unclaimed input, with Commissioner adjustment/judgment/provisional branches; it is not a universal deadline or entitlement for every exporter refund. Annex H/FASTER/ERS eligibility, input trace/stock and export evidence need specialist review before claiming. The 1-year period is in words on the page. [s.66](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf); [STR 7 Annex H](https://download1.fbr.gov.pk/Docs/20251141513138962Sales-Tax-Rules-2006-UpdatedUpto01-01-2025.pdf).

Keep schedule topics distinct: Third Schedule retail-price; Fifth zero-rated; Sixth exempt; Eighth other rates; Ninth mobile phones; Tenth bricks; Eleventh withholding; Twelfth commercial-import value-addition. Read the actual item/date/PCT and exceptions; do not adopt generic 25% luxury,15% textile/leather POS,5% prize/discount, sugar/soybean/steel/EV/pharma/dairy/solar or phone rates without the current entry. Extra tax is not interchangeable with further tax or a luxury-rate notification; the old “generally abolished” claim is not cleared.

## When to refuse or refer

Preserve the 9 referral groups: mixed federal/provincial supplies; unseen SRO/concession; sales-tax withholding-agent status/rates; exporter refund; partial exemption/apportionment; POS nonintegration/penalty remediation; imported digital/service and nonresident income withholding; FED/customs overlap; and audits/notices/scrutiny/post-refund disputes. Actual liability is pending where registration/status/rate/base/export evidence is missing. Do not assume domestic country, apply 18% as a legally safe unknown, classify someone Tier 1 using invented thresholds, omit withholding because status is unclear, or treat all disputed inputs as automatically refundable later.

Internal review markers retained from the earlier workflow are **firm policy, not FBR law**: single transaction 5,000,000 and derived 900,000 at 18%; concentration>40%; defaults>5; net position 500,000; input/output>90% for 3 months. Use them only to request evidence/review, never as statutory registration/audit/credit rules or permission to file with defaults.


## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for Act ss.2(5 AB),(43 A),(44),3/7/8/8 B/14,21 A-24,26,33 item 1,34,66/73 and adjacent exceptions | https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf |2026-11-14|
| Read for Rules 14/17/18 and STR 7 annex structure; consolidation only updated 1 January 2025, later amendments require period check | https://download1.fbr.gov.pk/Docs/20251141513138962Sales-Tax-Rules-2006-UpdatedUpto01-01-2025.pdf |2026-11-14|

Not yet confirmed: exact goods/actionable-claim/money/share/security boundary; continuous utility supply tax point; particular nonmonetary/associated-party/discount/retail valuation conditions; zero/exempt categories for diplomats, international organisations, conveyance stores, duty-free shops, notified machinery, food, pharmaceuticals, agricultural seeds/pesticides/tractors, education/newsprint, health and renewable equipment; historic Seventh Schedule/five-sector treatment; actual nil-return/status consequences, Tax Asaan/helpline details and authentication/2FA/CSV/API capabilities. Also, complete later 2026 amendment/extension calendar, actual current portal/form/payment-provider screens, SRO 297/1190/660 operative status and all special schedule/POS/withholding/value-addition/item rates, statutory penalty/nonintegration/fraud figures beyond the sourced table, actual exporter refund procedure/eligibility and every cross-credit arrangement with provincial services. Preserve those topics for targeted specialist work. No professional accountant approval is claimed.
