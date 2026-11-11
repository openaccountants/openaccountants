---
name: gf-import-octroi-and-vat
description: "Apply French Guiana VAT non-application and octroi de mer to ordinary goods imports and local production in 2026. Covers customs-value and local-price bases, the enacted July tariff, separate external and internal OM and OMR columns, producer liability threshold, relief evidence, input deductions and DOMINO-NG quarterly filing. Use when a VAT-free invoice is mistaken for a tax-free import, when choosing a tariff column or reconciling customs and producer returns. Includes two verified product rows and recomputing import-versus-local examples. Does not determine every classification, origin preference, valuation dispute or earlier tariff; space-sector partial relief has its own linked Guide."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/gf-import-octroi-and-vat"
  jurisdiction: "GF"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# French Guiana VAT non-application and octroi de mer 2026 v0.3

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

French Guiana is a French tax jurisdiction with an exceptional indirect-tax system. **VAT is not applicable in Guyane**; CGI article 294-1 applies through 31 December 2026, with CIBS L211-7 commencing 1 January 2027 under Ordinance 2026-671 article 19. [Future-code commencement](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054526924). For 2026, do not substitute another overseas department's VAT rates. Imports nevertheless attract external octroi de mer (OM), whatever their provenance, unless exempt, with regional octroi (OMR) on the same base. Ordinary local producers can also owe internal OM/OMR. A VAT-free invoice does not establish a tax-free import. [DGFiP, CGI art. 294-1 reference](https://www.impots.gouv.fr/professionnel/questions/quels-impots-dois-je-payer-pour-mon-activite-dans-les-dom); [Customs](https://www.douane.gouv.fr/demarche/importer-un-bien-dans-un-drom); [Law 2004-639, arts. 1-3](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000253374).

Quick reference: first ask transaction date, goods or service, exact tariff code, customs value, provenance, procedure, producer turnover and relief evidence. This Guide covers the July 2026 tariff and ordinary local-production administration; earlier transactions need their earlier enacted schedule. Classification/origin/valuation disputes require a transaction-specific ruling, not an illustrative rate.

## Rates, bands and thresholds

AP-2026-47 article 4 makes the new tariff effective **1 July 2026**. Article 1 replaces the tariff annex amended in January; article 2 preserves other framework provisions. Read external/internal columns separately. Physical PDF page 5 (tariff page 2/198) contains these examples:

| Code / item | Rate or threshold and condition | Official source |
|---|---|---|
| 0101 21 00, live pure-bred breeding horses | External OM 2%, OMR 3%; internal OM 2%, OMR 3%, exact classification required | [AP-2026-47, annex p5](https://www.ctguyane.fr/www/wp-content/uploads/2026/07/delib.ctg-ap-2026-47-modif-tgom-2026-complet.pdf#page=5) |
| 0105 11 11, female breeding/multiplication chicks of laying breeds, weighing no more than 185 g | External OM 7%, OMR 3%; internal OM 0%, OMR 1%; not a rate for every bird | [Same annex p5](https://www.ctguyane.fr/www/wp-content/uploads/2026/07/delib.ctg-ap-2026-47-modif-tgom-2026-complet.pdf#page=5) |
| Local producer liability | Prior calendar-year production turnover **at least EUR 550,000**, excluding VAT/OM; threshold prorated for a start during the reference year | [Law art. 2, current 21 February 2026 wording](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000253374) |
| Space-sector partial import relief | From 1 August 2026 residual OM 7% and OMR 3%, only if all activity/goods/use conditions met | [AP-2026-57, arts. 1-8](https://www.ctguyane.fr/www/wp-content/uploads/2026/07/delib.ctg-ap-2026-57-regime-exo-partielle-activites-spatiales.pdf), [child Guide](gf-space-sector-octroi.md) |

These are enacted product-specific rates, not average rates for animals/agriculture or all goods. The producer threshold is **reached or exceeded**, unlike the looser “supérieur” wording on the Customs summary page: the current statute controls. Internal examples do not by themselves establish producer liability or exemption.

## The base

Imports use customs value, not simply invoice value or retail selling price. Reconcile invoice, freight, insurance, valuation adjustments and exchange rate under the applicable customs rules, and compute OM and OMR separately on that same confirmed base. Do not compound OMR on the OM-inclusive amount. Other customs duties/excises remain separate. Locally produced goods use price excluding VAT and excises. Article 9 has a separate fee-based rule for goods temporarily sent out for repair/transformation and returned; do not apply full new-goods valuation automatically. Liability arises on import/delivery, or release for consumption after a qualifying suspensive regime. [Law arts. 3, 9-10, 37](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000253374); [Customs base/exigibility](https://www.douane.gouv.fr/demarche/importer-un-bien-dans-un-drom).

Production includes manufacture, transformation, renovation, extraction and statutory agriculture; current article 2 tests transformation at SH4, the first four nomenclature digits. Resale of finished goods and ordinary services are not automatically local production. Below-threshold local delivery status does not exempt a business's imports. [Law arts. 1-2](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000253374).

### Relief and input deductions

Test mandatory relief under articles 4, 5 and 8 and optional relief under the **operative CTG deliberation and annex**, not the industry label. Optional economic-activity relief requires the correct activity and goods codes, end use and declaration evidence; relief from OM does not automatically remove OMR. Production/non-production annexes have different effective dates. The Excel schedules on CTG's index are convenience versions expressly labelled non-binding. For space goods use the child Guide. A simple nomenclature update can preserve corresponding goods' relief under AP-2026-47 article 3; it cannot change goods' nature/destination. Keep the correspondence. [CTG index](https://www.ctguyane.fr/octroi-de-mer-tarif-exoneration/); [AP-2026-47 arts. 2-3](https://www.ctguyane.fr/www/wp-content/uploads/2026/07/delib.ctg-ap-2026-47-modif-tgom-2026-complet.pdf); [Law arts. 6-7, 37](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000253374).

The article 6 declaration support is **Cerfa 15567**: nature, quantity, value, beneficiary/end-use commitment and undertaking to pay tax if conditions fail. It is not automatic approval of every item on an activity list. The decree's investment-goods conditions normally require three-year retention; lending/rental/disposal can trigger prior tax payment unless the qualifying recipient/end-use continuation exception applies. [Customs circular, ¶¶35-40 and decree art. 5](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf); [official forms](https://www.douane.gouv.fr/fiche/formulaires-relatifs-loutre-mer).

For a taxable producer, input OM on elements of taxable operations can be deducted under articles 14-19, with original invoices/import documents and attribution to qualifying operations. This is **OM deduction, not input VAT**. Investment goods used more than 50% for qualifying operations receive full deduction; at 50% or less none under article 19, subject to the precise asset exclusions including relevant passenger vehicles. Correct disappeared goods or non-taxed operations; for cancelled/unpaid sales rectify the original invoice before crediting. Omitted deduction may be repaired on returns filed by 31 December of the second year following omission. Excess credits carry forward; cash refunds are limited to the investment/export situations in articles 24-26 and decree conditions. Never assume every credit is refundable. [Law arts. 14-26](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000253374); [Customs circular ¶¶60-84](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf).

Article 19-1 preserves qualifying investment-goods OM/OMR incurred in the calendar year the liability threshold is reached **and the preceding calendar year**, subject to article 19 asset/use conditions. Identify it separately on the first liable quarterly return; omitted deductions follow article 16. This startup carry-in rule does not cover raw-material inputs. [Law arts. 16, 19-1](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000253374); [circular ¶¶69-72](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf).

Article 24 credit-refund requests go on plain paper with the credit return copy and quarter reference to customs at the principal establishment: annually in January where combined OM/OMR credit is at least EUR 150, or in the month after a quarter where it reaches EUR 760. Reduce available credit by the requested amount at filing so it cannot also be deducted; definitive cancellation follows payment. These thresholds do not remove the investment/export eligibility conditions. [Decree arts. 9-10; circular ¶¶82-83](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf).

Article 25 separately permits an economic operator's onward-export refund for goods exported within two years, with OM/OMR paid or invoiced and not deducted, export proof and original purchase/import evidence. Goods must be exported unused, except the limited defect/non-conformity test use allowed by the circular. Claim at least EUR 150 combined tax in the month after each quarter to competent customs. Antilles/Guyane movements are excluded except the specified article 5 goods. This is not the article 24 January/quarter credit procedure. [Law art. 25; decree art. 11; circular ¶84](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf).

## Deadlines and filing

**Imports.** Identify the actual consignee, EORI/representative and customs procedure. Give the declarant goods descriptions, code, origin, value, date and relief support before entry/release. OM/OMR are liquidated on the customs declaration; retain its reference, accepted classification/value, levy lines and payment/release evidence. Apply the date-effective external row and both levies, not an internal row. This Guide does not invent a universal import return calendar or a single DELTA field valid for every transition/procedure. [Law arts. 10, 13(1), 33](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000253374); [Customs import guidance](https://www.douane.gouv.fr/demarche/importer-un-bien-dans-un-drom).

**Local production.** Identify to the competent customs office by 31 January after the year the threshold was reached, supplying existence/Kbis and production turnover by nomenclature; liability begins 1 January, not registration day. Notify relevant production/business changes within 30 working days. Since July 2024 use **DOMINO-NG** through the authenticated Douane account; request habilitation from the competent office. File/pay each calendar quarter by the **24th of the next month**, including a nil-sales quarter. The former Cerfa 12449 is not a substitute for mandatory online submission. [Decree arts. 2, 7, 14; circular ¶¶101-106](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf); [current online route](https://www.douane.gouv.fr/demarche/declarer-votre-octroi-de-mer-interne).

Enter establishment identity, quarter, taxable turnover split by code/rate, exempt deliveries, input deductions by nature, credits carried forward, refund requested where permitted and net OM/OMR separately. Annex A details local deliveries by nomenclature/rate; annex B details exports. Fourth-quarter return includes total annual production turnover. Use draft mode, check system-calculated tax and credits, validate, keep acknowledgement and reconcile the resulting debt; pay through enabled SEPA Télépaiement with the reference. Keep distinct taxed/non-taxed accounts and original deduction evidence. Producer invoices to another taxable person show each goods code, OM rate/amount; fully relieved deliveries under arts. 7/7-1 bear “livraison exonérée d'octroi de mer”. [Law arts. 35-36](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000253374); [decree art. 7 and circular ¶¶104-107, annex V](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf); [DOMINO-NG](https://www.douane.gouv.fr/demarche/declarer-votre-octroi-de-mer-interne).

## Penalties and interest

Law article 42 applies Customs control/recovery/sanctions, not the ordinary VAT late-return schedule. For debts under the current Customs Code from **1 May 2026**, L321-3 provides **0.20% monthly late interest**, from the first day of the month after payment was due through the payment month's last day. R515-6 provides a fine of **EUR 3,000 or, if greater, twice duties/taxes evaded or compromised** for its listed offences, including its catch-all tax-evasion irregularity which is neither smuggling nor undeclared import/export. Classification/value/origin false declarations and other offences have their own provisions; this is not an automatic penalty for every error. [L321-3](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053805609); [R515-6](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053814206); [law art. 42](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000253374).

The earlier code's article numbers were recodified in May 2026. Do not apply an old article 410 summary as a current universal penalty. Check the notice's offence/date; correction and interest relief have conditions. Antilles' inter-island periodic-declaration fines are not the general Guyane quarterly-return penalty.

## Cross-border points

VAT territoriality and OM territoriality are different. Mainland-France/EU goods can still be Guyane OM imports. Guadeloupe and Martinique form the single Antillean market; Guyane does not join it. Articles 4-5 contain special Guyane/Antilles taxed-delivery and listed-goods exceptions, so preserve tax/status/dispatch evidence before claiming no double charge. Export relief likewise needs proof; use annex B rather than silently excluding turnover. [Law arts. 3-5](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000253374); [decree art. 3 and circular ch. IX](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf).

For services determine their place before concluding no VAT: a Guyane address alone does not decide every mainland B2C or special-place service. [DGFiP current services guidance](https://www.impots.gouv.fr/professionnel/questions/je-realise-depuis-la-metropole-une-prestation-de-service-pour-un-client). This Guide makes no claim that VAT non-application cancels payroll, income or corporate taxes.

## Two worked examples that recompute

**Verified import row.** Assume EUR 10,000 confirmed customs value, classification 0101 21 00, post-1-July import and no relief. OM is EUR 200 and OMR EUR 300, total EUR 500. Other customs charges excluded. [Tariff p5](https://www.ctguyane.fr/www/wp-content/uploads/2026/07/delib.ctg-ap-2026-47-modif-tgom-2026-complet.pdf#page=5).

```oa-check
name: Pure-bred breeding horses import
inputs:
  customs_value: 10000
steps:
  om: customs_value*0.02
  omr: customs_value*0.03
  total: om+omr
expected:
  om: 200
  omr: 300
  total: 500
```

**Choose the right column.** Same value, proved 0105 11 11 and its weight/breed conditions (no more than 185 g): external 7%/3% gives EUR 1,000. If instead these are an already-liable local producer's qualifying local deliveries on an assumed EUR 10,000 article 9 base, its internal 0%/1% row gives EUR 100. The EUR 900 difference is not an election: the transaction selects the column. [Tariff p5](https://www.ctguyane.fr/www/wp-content/uploads/2026/07/delib.ctg-ap-2026-47-modif-tgom-2026-complet.pdf#page=5).

```oa-check
name: Import versus local-production column
inputs:
  base: 10000
steps:
  import_om: base*0.07
  import_omr: base*0.03
  import_total: import_om+import_omr
  internal_total: base*0+base*0.01
  difference: import_total-internal_total
expected:
  import_total: 1000
  internal_total: 100
  difference: 900
```

## Ask the client first

- Chargeable-event date, goods or services, movement and customs procedure.
- Exact specifications/code, origin and binding classifications already obtained.
- Invoice, freight, insurance, customs value and declaration reference.
- Production activity, prior-year turnover, start date and registration.
- Activity/goods annex and actual destination, ownership/end-use evidence.
- Previous input credits, original invoices, exports, relief and disposals.
- Both levies, other charges, payment and filing reconciliation.

## Sources

| Source and text actually read | URL | Read on |
|---|---|---|
| Law 2004-639, read for arts. 1-10, 13-28, 33-37 and 42; current art. 2: “atteint ou dépassé 550 000 €”, art. 9 customs/local bases, arts. 14-26 deduction/refund conditions | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000253374 | 2026-11-11 |
| AP-2026-47, read for complete arts. 1-4 and annex physical p5, both external/internal columns; “à compter du 1er juillet 2026” | https://www.ctguyane.fr/www/wp-content/uploads/2026/07/delib.ctg-ap-2026-47-modif-tgom-2026-complet.pdf | 2026-11-11 |
| Customs import page, read for territoriality, base, chargeability, declaration and relief; “quelle que soit leur provenance” | https://www.douane.gouv.fr/demarche/importer-un-bien-dans-un-drom | 2026-11-11 |
| CTG index, read for enacted tariff/production/non-production/space links and non-binding Excel warning | https://www.ctguyane.fr/octroi-de-mer-tarif-exoneration/ | 2026-11-11 |
| Customs circular 10 July 2025, read for ¶¶35-40, 60-84, 101-107, ch. IX boundaries, decree arts. 2-8 and forms annex V. “au plus tard le 24 du mois suivant”; 2026 law controls later amendments | https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf | 2026-11-11 |
| Customs DOMINO-NG page, read for mandatory electronic route, draft/validation/calculation and payment functions | https://www.douane.gouv.fr/demarche/declarer-votre-octroi-de-mer-interne | 2026-11-11 |
| DGFiP DOM taxes page and CIBS L211-7 commencement note, read for Guyane VAT exception, CGI through 2026 and January 2027 recodification | https://www.impots.gouv.fr/professionnel/questions/quels-impots-dois-je-payer-pour-mon-activite-dans-les-dom, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054526924 | 2026-11-11 |
| Customs Code L321-3 and R515-6, read for complete current interest/offence paragraphs and May commencement. “0,20 % par mois”; “deux fois celui des droits et taxes” | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053805609, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053814206 | 2026-11-11 |

Not yet confirmed: full pre-July tariff/amendment crosswalk and full post-July amendment-chain review, transaction-specific classification/origin/valuation, live import-procedure field numbering, pre-May offence/sanction crosswalk. Current VAT non-application is confirmed; no unsupported general import rate or earlier-period penalty is supplied.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `gf-import-octroi-and-vat` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/gf-import-octroi-and-vat. If neither is available, confirm every figure against the official source pages cited above before relying on it.
