---
name: bq-excise
description: >
  Analyse 2026 excise in Bonaire, Sint Eustatius and Saba. Use for petrol,
  alcohol and tobacco classification, taxable release or import, warehouse
  permits, quantities, rates, periods, security, exemptions, refunds and stamp
  credits. Separates Bonaire's wider goods list from petrol-only excise on
  Saba and Sint Eustatius. Includes statutory and delegated conditions,
  authority guidance and fictional boundary calculations. This source-cited
  draft holds actual classification, permits, forms, valuation, currency
  conversion and unresolved operational cases. Load with the universal
  workflow base and applicable BES references; professional review remains
  required before reliance.
jurisdiction: BQ
category: international
tax_year: 2026
tax_year_notes: "2026 excise rules checked on 17 October 2026; establish island, product and release/import date"
tier: 2
last_updated: 2026-10-17
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - bq-tax-system
  - bq-abb
  - bq-tax-compliance
---

# Bonaire, Sint Eustatius and Saba: excise in 2026

Establish island, product classification, quantity, alcohol strength or tobacco
specification, movement, licence, person and event before using a tariff.
Petrol is an excise good on all three islands; the other listed alcohol and
tobacco goods are taxed under this chapter on **Bonaire**. A common rate
table does not extend Bonaire's charge to Saba or Sint Eustatius. The current
authority business page confirms that distinction. [DAB, articles 1.1(ff)
and 4.1][DAB]; [AUTH]

Load `workflow-base` and applicable domain/BES references. Preserve source
gates, confirmed profile, refusals, four universal outputs and domain
outputs/checks. This Tier 2 reference supplies conditional components, not
a complete return or country pack. Unknown mandatory conditions hold the
complete financial output package. Import duty, import ABB and excise are
separate charges; use `bq-customs-valuation` and `bq-abb` for their bases.

## Charge, release and the responsible person

Article 4.1 charges release and import. Article 4.4 treats removal from a
designated excise warehouse, specified consumption within warehouses, and
manufacture/possession outside the required charged regime as release.
An invoice or physical sale is not the only trigger. Transfers between
qualifying warehouses and exports are excluded from release only with the
delegated conditions. Article 4.5 separately conditions transfers into an
excise warehouse from outside BES or other customs storage. A warehouse
label does not itself establish suspension. [DAB]

For ordinary release, the permit holder is the taxpayer. Article 4.34 has
different rules for specified warehouse consumption and uncharged manufacture
or possession. Its instructed-release exception is confined by decree
article 3.5 to petrol released on another petrol-warehouse permit holder's
written instruction, with the stated return disclosures. Do not apply it
to every outsourced alcohol or tobacco transaction. Article 4.45 separately
addresses carrier and other participants' joint liability for irregularities.
[DAB, articles 4.34–4.45][DAB]; [DECREE]

Release liability and the applicable rate generally arise at release under
articles 4.35 and 4.38. If that time cannot be established, article 4.35 uses
the inspector's determination day. Revoking a permit treats remaining
designated stock as released and ends the period on that day; a specific
payment decision may also shorten the term. Unexplained production,
transport/storage losses and missing goods are deemed released under
article 4.64. They are not automatically deductible stock losses. Import
excise instead follows the applicable import branch under article 4.5.
[DAB]

## Classification, quantities and tariffs

| Goods and statutory branch | Tariff and quantity rule |
|---|---|
| Petrol, HS subheading 2710.12 | Per hectolitre: **USD 31.86 on Bonaire**, **USD 24.27 on Saba/Sint Eustatius**. A partial hectolitre counts as a whole hectolitre. |
| Bonaire beer, HS 22.03, alcohol **above 0.5% vol** | **USD 67.04 per hectolitre**. Concentrated beer uses ready-to-consume volume, with the required information supplied to the inspector. |
| Bonaire wine, specified HS 22.04–22.06, alcohol **at most 20% vol** | **USD 128.50 per hectolitre**. |
| Bonaire other alcohol under article 4.13 | **USD 12.85 per hectolitre per volume percentage point of alcohol**. Includes wine above 20% vol and the specified other product categories; establish the precise branch. |
| Bonaire cigarettes, HS 2402.20 | Per 100 statutory cigarettes: **USD 5.34** if made on Bonaire for a Bonaire brand; **USD 7.01** if made there for a non-Bonaire brand; **USD 8.69** on import. Apply the length adjustment below. |
| Bonaire cigars/cigarillos, HS 2402.10 | **USD 9.78 per 100 cigars**; **USD 4.89 per 100 cigarillos**, which weigh **no more than three grams each**. |
| Bonaire smoking tobacco under article 4.20 | **USD 30 per kilogram**, including its specified partly/non-tobacco substitutes. |

[DAB, articles 4.7–4.21][DAB]; [RATES]

One hectolitre is 100 litres. Preserve the different quantity rules rather
than rounding every liquid product to a whole hectolitre. For cigarettes,
measure length **excluding filter or mouthpiece**: more than eight through
eleven centimetres counts as two cigarettes; more than eleven through
fourteen counts as three, and so on under article 4.17(2). The physical
packet count alone can understate the tax quantity. [DAB]

Article 4.14a requires reliable measuring equipment or qualifying retail-pack
quantities established under internationally recognised standards. Establish
the actual volume and strength. Declared bottle size, retail description,
weight and classification are different inputs. Fractional-cent return
rounding and disputed product/measurement classifications remain held.
[DAB]; [RULES, article 4.2][RULES]

### Fictional quantity and rate components

These examples stipulate the stated island, a taxable ordinary release/import,
established product classification and measurements, no exemption, suspension,
stamp credit or refund unless stated. They test components, not a final
return or permit entitlement. [DAB]

| Stipulated facts | Component result, USD |
|---|---:|
| Bonaire petrol, 100 litres | 1 × 31.86 = **31.86** |
| Bonaire petrol, 100.01 litres | 2 × 31.86 = **63.72** |
| Saba or Sint Eustatius petrol, 100 litres | 1 × 24.27 = **24.27** |
| Saba or Sint Eustatius petrol, 100.01 litres | 2 × 24.27 = **48.54** |
| Bonaire qualifying beer, 100 litres | **67.04** |
| Bonaire qualifying wine, 100 litres at exactly 20% vol | **128.50** |
| Bonaire article 4.13 product, 10 litres at 40% vol | 0.1 × 40 × 12.85 = **51.40** |
| Bonaire import, 100 cigarettes no longer than eight centimetres excluding filter | **8.69** |
| Same import, 100 cigarettes exactly eleven centimetres excluding filter | 200 statutory cigarettes; **17.38** |
| Same import, 100 cigarettes longer than eleven through fourteen centimetres excluding filter | 300 statutory cigarettes; **26.07** |
| Bonaire, 100 qualifying cigars weighing exactly three grams each | Cigarillo branch; **4.89** |
| Bonaire, 100 qualifying cigars each heavier than three grams | Cigar branch; **9.78** |
| Bonaire qualifying smoking tobacco, two kilograms | **60.00** |

Beer at exactly 0.5% vol does not satisfy article 4.9's beer definition. This
does not prove exemption from every other tax or product rule. Similarly,
wine imported into Saba does not acquire Bonaire excise merely because its
rate appears in a general table. Establish ABB and other applicable charges
separately. [DAB]; [AUTH]

## Warehouse permission, suspension, periods and security

A place requires the inspector's permit to operate as an excise warehouse.
Articles 4.22–4.33 govern eligibility, requests, conditions, amendment,
takeover and revocation. Storage-only quantity conditions and exceptions are
in regulation articles 4.3–4.4; a customer-facing store is not automatically
a warehouse. Production records and any required work declaration matter.
No permit is obtained by loading this guide. [DAB]; [RULES, articles 4.3–4.6][RULES]

The ordinary storage-only test concerns average stock over a year **above
20,000 litres for beer** or **above 2,500 litres for wine, other alcohol or
petrol**. The inspector can permit lower stock with conditions, and the
specified direct-sale locations have their own exceptions. Production work
declarations, when required, are filed at least **two working days** before
production. Taking over another holder's place requires their joint request
for the permit substitution; buying stock or premises does not transfer the
permit automatically. [DAB, articles 4.23 and 4.30][DAB]; [RULES]

Decree article 3.1 prescribes the movement document, despatch/receipt records,
five-working-day return and eight-working-day notification controls for
warehouse transfers, with authorised exceptions and deemed-release
consequences. Article 3.2 has its own transport order and arrival/notification
controls for entry into a warehouse. These clocks have different starting
events. Keep the actual documents, receipt quantities, permit permissions
and notification evidence; do not deem a transfer exempt from tax just
because the destination is licensed. [DECREE]

Ordinary release excise is paid on return for each warehouse separately.
The regulation normally assigns a calendar month, with another period
possible by inspector decision. A combined return needs the permission and
central-accounting conditions in regulation article 4.7. The general
Belastingwet BES article 8.11 payment term is fifteen days after the period,
including its separate nil-return obligation and authorised-extension rules;
establish the actual filing notice and any special decision. Import
payment/clearance and stamp payment do not automatically use that clock.
[DAB, articles 4.3 and 4.36–4.37][DAB]; [RULES]; [B1]

The permit holder must provide security for actual or potential excise.
The inspector determines it by decision; it is not the current month's tax
or an automatic fixed percentage. Regulation article 4.8 defines the excise
interest using average stock, releases, transfers and inbound movements,
with its stamp-deferral and combined-return rules. Security is at least
**5%**, at most **100%** of that interest, capped at **USD 6,500,000**.
Do not infer an entitlement to the minimum or double-count a consolidated
security. Actual security and any increase/acceptance decision need review.
[DAB, articles 4.39–4.43][DAB]; [RULES]

## Exemptions, refunds and tobacco stamps

Import exemptions under article 4.48 require the delegated conditions; a nil
import-duty tariff is not proof that every good meets an exemption category.
Article 4.49's petrol uses, including specified commercial vessel/aircraft
and tank-cleaning uses, have distinct conditions. Decree article 3.6 and
regulation article 4.9a require the two signed declaration copies and
specified supply/vessel/quantity records. A commercial-use assertion alone
does not establish them. Denatured-alcohol relief uses the prescribed method
through regulation article 4.9; the cross-referenced denaturing annex was
not reviewed here and actual eligibility remains held. [DAB]; [DECREE]; [RULES]

Article 4.50a provides requested refunds for specified exports, qualifying
petrol uses, unforeseeable loss/force majeure, supervised destruction and
entry into a qualifying excise warehouse. The refund cannot exceed excise
paid. Decree articles 3.7–3.7c prescribe export evidence, prompt loss notice,
proof and warehouse records. The regulation normally requires the request
within **three months after the calendar quarter** when the right arose,
unless otherwise provided, with the calculation and retained evidence.
Article 4.9d separately addresses loss/destruction records. [DAB]; [DECREE];
[RULES, articles 4.9b–4.9d][RULES]

For an export shipment, regulation article 4.9b(6) requires at least
**USD 200** excise. A stipulated shipment refund of 199 fails that threshold;
200 meets only that numerical condition, not the remaining evidence and
eligibility tests. Do not apply the export-shipment minimum indiscriminately
to every loss or stamp-refund claim. [RULES]

The statutory stamp regime has important regulatory exceptions: cigars,
cigarillos and smoking tobacco need no excise stamp on release/import, and
the stated travellers' own-baggage exception is separate. An exception from
stamping does not itself exempt tax. Stamp payment is ordinarily at
application; secured deferral under article 4.54 has its own last-day-of-the-
second-following-month term. Matching stamp amounts paid or payable reduce
the corresponding release/import liability under article 4.55. For a
stipulated 8.69 liability and matching 8.69 stamp amount, the additional
component is zero; total excise remains 8.69. [DAB]; [RULES, article 4.10][RULES]

Stamp application, attachment, returned/destroyed/lost stamps and credits
must follow their own records and deadlines. Regulation article 4.13's
lost-stamp request uses a one-month term and immediate notification, rather
than the ordinary quarter-based goods-refund term. Article 4.14 applies a
permitted offset against open deferred amounts starting with the newest
item. Do not create a second refund for the same tax. Product origin and
movement evidence, physical stock reconciliations and the statutory
manufacture, possession and stamp prohibitions remain relevant. [DAB,
articles 4.51–4.70][DAB]; [RULES, articles 4.11–4.17][RULES]

## Verification and completion conditions

Check island and HS/product category before rate; actual quantity and
strength; petrol-only upward unit rounding; cigarette length; inclusive
cigarillo weight; event, taxpayer and date; suspension documents; period
and special clocks; permit/security decisions; separate relief conditions;
stamp offsets; stock losses; and no duplicate claim. The practitioner keeps
identities, original permits, tax identifiers and bank details outside the
agent. This reference authorises no licence, return, refund or payment
submission.

Read on 17 October 2026: complete customs-law chapter IV, articles 4.1–4.70
including inserted articles; decree chapter 3; regulation chapter 4;
definitions and charge provisions; Belastingwet BES article 8.11; and both
current authority pages. A fresh law capture matches the saved source
byte-for-byte. Customs valuation and ABB have their own references.
Cross-referenced external annexes, import-exemption branches, actual forms,
monetary rounding beyond express rules, permits, security and live operating
cases were not completed here. No practitioner sign-off, engagement workbook
or comprehensive country coverage is claimed.

[DAB]: https://wetten.overheid.nl/BWBR0029236/2025-01-01
[DECREE]: https://wetten.overheid.nl/BWBR0029262/2025-01-01
[RULES]: https://wetten.overheid.nl/BWBR0029309/2025-01-01
[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[AUTH]: https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/accijnzen
[RATES]: https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-particulieren/reizigersbagage/accijnstarieven

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
