---
name: yt-vat-and-goods-imports
description: >
  Mayotte goods-tax boundary and routing reference for 2026. Separates local VAT non-application from customs declarations, external octroi de mer, regional octroi and destination taxation. Identifies shipment evidence and the mainland-France example without inventing a product tariff. Reconciles the VAT recodification dates using the July 2026 ordinance and its conditional invoice-reference transition. Current product tariffs, exemptions, detailed valuation, services and electronic reporting require separate evidence. This is a routing Guide, not a tax assessment or a complete territorial tax pack; professional approval is pending.
version: 0.3
jurisdiction: YT
tax_year: 2026
last_updated: 2026-11-17
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: router
---

# Mayotte: VAT boundary and goods imports

## Scope

Use this Guide to route a goods movement involving Mayotte to the right tax and customs questions for 2026. French customs distinguishes Mayotte's membership of the French/EU customs territory from its exclusion from the EU VAT territory. **VAT is not applicable locally; this does not exempt an import from customs declarations or octroi de mer.** CGI article 294(1) states the local VAT non-application. [Customs: trade with Mayotte](https://www.douane.gouv.fr/fiche/vos-echanges-commerciaux-avec-mayotte); [CGI art. 294](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000027978194/2026-11-01).

This is a source-cited draft. It does not determine a service's place of supply, tax registration elsewhere, a supplier's complete invoice obligations, or a product's tax amount.

## Ask the client first

- What goods, commodity codes and intended uses are involved?
- Where were they dispatched, what is their origin and customs status, and where will they arrive?
- What are the shipment and tax-point dates?
- What do the purchase, freight, insurance and customs-value documents show?
- Is a product-specific exemption claimed, and what decision and conditions support it?
- Is the request about goods, a service, invoice wording or electronic reporting?

## The method, step by step

1. **Establish the territory and movement.** Record dispatch, destination, customs status and origin separately. EU customs-territory membership does not make the movement an ordinary domestic VAT sale. The customs page requires an import declaration at the import customs office. Its reference to the DAU identifies a declaration obligation, not a verified instruction for a particular 2026 electronic screen or field. [Customs, import section](https://www.douane.gouv.fr/fiche/vos-echanges-commerciaux-avec-mayotte).

2. **Separate the charges.** Customs identifies external octroi de mer and regional octroi for imported goods, subject to the applicable rules and exemptions. Local production has its own conditional treatment. An invoice without local VAT establishes neither an octroi exemption nor a universal product rate. The national circular separates fiscal imports from remunerated local producer deliveries and explains the regional rate-setting framework. [Customs](https://www.douane.gouv.fr/fiche/vos-echanges-commerciaux-avec-mayotte); [2025 national circular, paragraphs 1 to 5, 16 to 22 and 87 to 97](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf).

3. **Build the goods file before calculating.** Obtain the classification, origin, dispatch location, customs status, value evidence, shipping costs, use, claimed exemption and effective regional decision. These are research inputs, not a tariff or valuation formula. The competent Mayotte authority sets octroi rates by product nomenclature; no single rate can be taken from the fact that VAT is not applicable. [Law 2004-639, art. 27, operative 2026 version in the retained consolidated section](https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294/).

4. **Apply the original mainland-France shipment case.** Goods ordered from mainland France for delivery into Mayotte still require destination customs and octroi analysis. The absence of Mayotte VAT does not establish zero landed-tax cost. This case assumes no product, exemption, value or tariff. [Customs](https://www.douane.gouv.fr/fiche/vos-echanges-commerciaux-avec-mayotte).

   A supplementary cost-reconciliation illustration shows why the charges must remain separate. Assume goods cost EUR 1,000, freight EUR 100, and independently established import documents show EUR 80 external octroi and EUR 25 regional octroi, with no other costs in this illustration. The total is EUR 1,205. **The two supplied tax amounts are hypothetical document inputs, not rates, statutory calculations or confirmation that those amounts apply to any shipment.** No customs value or octroi base is computed. The illustration cannot authorise a declaration.

```oa-check
name: Reconcile supplied shipment costs without inventing an octroi tariff
inputs:
  goods_invoice: 1000
  freight: 100
  supplied_external_octroi: 80
  supplied_regional_octroi: 25
steps:
  - supplied_border_taxes: supplied_external_octroi + supplied_regional_octroi
  - illustrated_total_cost: goods_invoice + freight + supplied_border_taxes
expected:
  supplied_border_taxes: 105
  illustrated_total_cost: 1205
```

5. **Route goods leaving Mayotte to the destination's rules.** The Mayotte customs page says taxes normally due at arrival must be considered. CGI article 294 treats mainland-to-Mayotte movements as exports for VAT and entry into mainland France from Mayotte as imports. Its other DOM routes also depend on the stated departure and destination. Do not infer octroi in mainland France from the customs page's generic overseas list of possible destination taxes. No destination tax amount is supplied here. [CGI art. 294(2) and (3)](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000027978194/2026-11-01); [Customs, export section](https://www.douane.gouv.fr/fiche/vos-echanges-commerciaux-avec-mayotte).

6. **Use the correct legal-reference period.** The original VAT recodification ordinance scheduled its general commencement for September 2026. Ordinance 2026-671 article 17 changed that date to **1 January 2027**. The current article 49 retains an express list of exceptions with their own dates; the postponement is not a claim that every provision waits until 2027. The CGI VAT-chapter repeal is in article 9, including article 294, and must be read with the applicable commencement rather than its displayed future repeal label alone. [Current art. 49](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000054587047); [art. 9](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000053100831); [July amending art. 17](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000054497326).

   Article 46 maps the specified CGI references to the corresponding replacement provisions in existing legislation, administrative acts, invoices and contracts at the applicable commencement dates. Its paragraph II also covers administrative acts, invoices and contracts capable of producing effects through **30 June 2028**. This conditional reference transition does not establish the correct future CIBS citation or complete invoice wording for a particular transaction. The October BOFiP announcement explains the postponement and administrative-doctrine continuity. [Current art. 46 I to III](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053100905); [BOFiP, 7 October 2026](https://bofip.impots.gouv.fr/bofip/15140-PGP.html/ACTU-2026-00126).

## When to refuse or refer

Hold any tariff calculation or exemption conclusion until the exact product, effective decision, valuation rules and operative conditions are supported. Do not turn the local producer turnover regime into a blanket small-business import exemption. Do not use VAT non-application to decide service treatment, electronic reporting or every invoice obligation. An uncertain destination or customs status stops the routing result.

For a completed shipment assessment, hand off the goods file and the unresolved tax components for the specific Mayotte tariff, exemption and customs-value analysis. For goods leaving Mayotte, hand off to the destination's import rules. For future invoice references, obtain the exact operative replacement provision before prescribing wording.

## Sources

| Source and actual scope read | URL | Read on |
|---|---|---|
| French customs, Mayotte: complete operative import/export guidance, including territory, VAT, declaration and octroi distinctions; page updated October 2025 | https://www.douane.gouv.fr/fiche/vos-echanges-commerciaux-avec-mayotte | 2026-11-17 |
| CGI art. 294: paragraphs 1 to 3 and future-repeal context; dated November 2026 display | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000027978194/2026-11-01 | 2026-11-17 |
| National octroi circular: retained official text extraction, paragraphs 1 to 5, 16 to 22 and 87 to 97; not a read of every page or a current product tariff | https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf | 2026-11-17 |
| Law 2004-639: arts. 1, 2, 27 and 37; retained Légifrance section displays consolidation at 14 November 2026 | https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294/ | 2026-11-17 |
| Ordinance 2025-1247 art. 49: complete general commencement and listed exceptions, current November display | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000054587047 | 2026-11-17 |
| Ordinance 2025-1247 art. 9: consolidated repeal list including the VAT chapter and art. 294; read with art. 49 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000053100831 | 2026-11-17 |
| Ordinance 2026-671 art. 17: complete amendments to arts. 46 and 49 | https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000054497326 | 2026-11-17 |
| Ordinance 2025-1247 art. 46: I to III, including the conditional reference transition | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053100905 | 2026-11-17 |
| BOFiP announcement: postponement, reference transition and administrative-doctrine continuity | https://bofip.impots.gouv.fr/bofip/15140-PGP.html/ACTU-2026-00126 | 2026-11-17 |

Not yet confirmed: current product tariffs and exemption eligibility, detailed customs valuation, current electronic customs screens/fields, service transactions, electronic invoicing/reporting, the precise future CIBS invoice citation and transaction-specific invoice duties. These remain non-usable holds. This bounded read is not a full amendment-chain or territorial tax-pack review; independent source review of this bounded scope is complete; professional approval is pending.
