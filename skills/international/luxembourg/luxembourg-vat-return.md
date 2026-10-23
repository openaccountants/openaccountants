---
name: luxembourg-vat-return
description: "Luxembourg VAT (TVA) for tax year 2026 in the deep-tax shape: who must charge VAT, the four rates in art. 39 of the VAT law of 12 February 1979 (17%, 14%, 8%, 3%) and the goods and services in annexes A, B and C, the small business franchise under arts. 57 to 57quater (EUR 50,000, tolerance to EUR 55,000, EU SME scheme at EUR 100,000), the filing frequency set by turnover (annual up to EUR 112,000, quarterly to EUR 620,000, monthly above), due dates (before the 15th after the period; annual-only filers before 1 March; annual recap before 1 May), reverse charge, recapitulative statements, fines under art. 77 and interest under art. 85. Trigger on: Luxembourg VAT return, TVA Luxembourg, AED, eCDF, déclaration TVA, régime de franchise, état récapitulatif. Out of scope: income tax of the owner in luxembourg-income-tax; companies in lu-corporate-tax; non-residents in lu-cross-border; funds, SOPARFI and VAT groups (refer)."
version: 2.1
jurisdiction: LU
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
verified_by: pending
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Luxembourg: VAT (TVA), periodic and annual returns (2026)

> **Source-cited draft: not reviewed by an accountant.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any business's facts. Do not rely on it to file or pay without review by a qualified professional in Luxembourg.

**Which text of the law.** Loi modifiée du 12 février 1979 concernant la taxe sur la valeur ajoutée (LTVA), in the coordinated text published by the Administration de l'enregistrement, des domaines et de la TVA (AED) at 1 January 2026, which includes every change up to the law of 20 December 2024 (Mémorial A 574). The AED states that its coordinated text is not legally binding; only texts published in the Mémorial are. Article numbers below follow that text.

**Sibling skills.** The owner's income tax is in [luxembourg-income-tax](luxembourg-income-tax.md). Companies are in [lu-corporate-tax](lu-corporate-tax.md), and non-residents and treaties in [lu-cross-border](lu-cross-border.md). This skill does not repeat them.

## Who this applies to

- **Taxable persons making supplies in Luxembourg.** Anyone who carries on an economic activity independently and supplies goods or services in Luxembourg for consideration charges VAT and is identified with the AED (art. 62 LTVA). The supplier owes the tax unless it passes to the customer (art. 61).
- **Small businesses under the franchise (art. 57bis).** A taxable person established in Luxembourg whose annual Luxembourg turnover, net of VAT, does not exceed EUR 50,000 is exempt. It charges no VAT, deducts no input VAT, and writes "TVA non applicable – Article 57bis de la loi modifiée du 12 février 1979" on its invoices. VAT groups, flat-rate farmers, persons who opted to tax property under art. 45 and occasional sellers cannot use it.
- **Businesses established in another member state.** They can use the Luxembourg franchise only through the EU SME scheme: EU-wide turnover not above EUR 100,000, Luxembourg turnover not above EUR 50,000, and an "EX" number from their home state (art. 57ter).
- **Customers who owe the tax.** A business or VAT-identified legal person receiving B2B services from a supplier not established in Luxembourg owes the VAT itself; so does the buyer of goods from another member state (intra-EU acquisition), and certain buyers of gas and electricity from abroad (AED, débiteur de la taxe).
- **Refer:** holding and fund structures (SOPARFI, SIF, RAIF, SICAR), fund management, VAT groups (art. 60ter), and businesses with both taxable and exempt supplies, which are common in the financial sector and need a deduction ratio.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate (art. 39(3), art. 40(2)) | 17% | 2026 | https://pfi.public.lu/dam-assets/pdf/legislation/tva/loi/loi-tva-2026-01-01.pdf |
| Intermediate rate, annex C: wine of 13% alcohol or less, solid mineral fuels and fuel oils, cleaning products, advertising print, heat not from a heating network, custody of securities, credit management by a third party | 14% | 2026 | https://pfi.public.lu/dam-assets/pdf/legislation/tva/loi/loi-tva-2026-01-01.pdf |
| Reduced rate, annex A: gas, electricity, network heat, firewood, plants and flowers, hairdressing, small repairs, cleaning of private homes, bicycles | 8% | 2026 | https://pfi.public.lu/dam-assets/pdf/legislation/tva/loi/loi-tva-2026-01-01.pdf |
| Super-reduced rate, annex B: food (not alcohol), books and newspapers, children's clothing and shoes, water, medicines, restaurant services (not alcohol), accommodation, passenger transport, admissions, waste collection, authors and performers, certain housing works, solar panels on homes | 3% | 2026 | https://pfi.public.lu/dam-assets/pdf/legislation/tva/loi/loi-tva-2026-01-01.pdf |
| Franchise threshold, Luxembourg annual turnover net of VAT (art. 57bis(1)) | EUR 50,000 | 2025 onward | https://pfi.public.lu/fr/professionnel/tva/sme.html |
| Tolerance in the year it is crossed (art. 57bis(6)) | 10% (to EUR 55,000) | 2025 onward | https://pfi.public.lu/fr/professionnel/tva/sme.html |
| EU SME scheme, EU-wide annual turnover (arts. 57ter, 57quater) | EUR 100,000 | 2025 onward | https://pfi.public.lu/fr/professionnel/tva/sme.html |
| Annual returns only if prior-year turnover (or intra-EU acquisitions and services received) did not exceed | EUR 112,000 | 2026 | https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/tva/declarations/declaration-tva.html |
| Quarterly plus annual returns if above EUR 112,000 and not above | EUR 620,000 | 2026 | https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/tva/declarations/declaration-tva.html |
| Monthly plus annual returns if above | EUR 620,000 | 2026 | https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/tva/declarations/declaration-tva.html |
| Quarterly recapitulative statement for intra-EU supplies of goods if they total less than | EUR 50,000 | 2026 | https://pfi.public.lu/fr/professionnel/tva/en-cours-activite-economique/etat-recapitulatif.html |

## The taxable base

- **Base.** The consideration net of VAT for each taxable supply, set by arts. 28 to 38 LTVA. Amounts in a foreign currency are converted at the last selling rate published by the Banque centrale du Luxembourg or the ECB when the tax becomes due (AED, déclarations).
- **Rate timing.** The rate in force when the chargeable event occurs; for intra-EU acquisitions and imports, the rate when the tax becomes due (art. 39(1)).
- **Exempt supplies.** Financial services, insurance, most letting of property, medical care and education are exempt (arts. 43 and 44); input VAT on related costs is not deductible, and a business with both kinds of supply apportions.
- **Input VAT.** Deductible on purchases used for taxable supplies, reported in the return of the period. Not deductible on spending that is not strictly professional, such as luxury, entertainment and representation costs (art. 54(1)). An excess of input VAT is carried to the next period (art. 55(1)); a refund of a credit balance is claimed by request.
- **Franchise turnover.** Counts taxable supplies and certain exempt ones (art. 57, point 2), net of VAT. Sales of the business's own capital assets are left out.
- **Reverse charge.** The customer enters the tax as output VAT and, if entitled, deducts it as input VAT in the same return. Intra-EU acquisition VAT and import VAT for a VAT-identified importer are declared, not paid at the border (AED, débiteur de la taxe).

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Monthly return and payment | Before the 15th day of the month after the month (art. 64(6)) | LTVA; guichet.lu |
| Quarterly return and payment | Before the 15th day of the quarter after the quarter. Q2 2026: before 15 July 2026 | guichet.lu |
| Annual return for monthly and quarterly filers, and balance | Before 1 May of the following year (art. 64(7)). 2026: before 1 May 2027 | LTVA; guichet.lu |
| Annual return for annual-only filers (turnover up to EUR 112,000), and payment | Before 1 March of the following year (art. 64(9)(a); guichet.lu). 2026: before 1 March 2027 | LTVA; guichet.lu |
| Business that stops trading | Final return within two months of stopping (art. 64(7)) | LTVA |
| Franchise business | No return, if it has no tax to pay and made no cross-border B2B services; tell the AED its prior-year turnover in writing before 1 March (art. 57bis(4)) | LTVA |
| Recapitulative statement (intra-EU goods and B2B services) | Before the 15th of the month (or quarter, for goods under EUR 50,000) after the period; the 25th when filed electronically | AED, état récapitulatif |

Returns are filed electronically through eCDF (art. 64(8)); payment goes to the AED's central receipt office and must name the VAT number and period (AED, paiement). The AED reviews the filing frequency each year from the turnover, so the frequency can change from one year to the next. Returns filed for a period other than the one the business is registered for are not taken into account.

**Correction to earlier versions.** Earlier versions of this skill gave 1 May as the annual deadline for every filer. A business that files only an annual return files it, and pays, before 1 March.

## Penalties and interest

| What | Figure | Source |
|---|---|---|
| Fine for breaching filing, identification, invoicing and record duties (arts. 62 to 66bis, 70, 71 and others) | EUR 250 to 10,000 per infraction (art. 77(1)) | LTVA |
| Fine for paying late | Up to 10% a year of the tax outstanding (art. 77(1), third paragraph) | LTVA |
| Daily fines for failing to provide records after a formal warning | Up to EUR 25,000 per day of delay (art. 77(2)) | LTVA |
| Fine where the breach aims at or results in evading tax or an undue refund | 10% to 50% of the tax evaded, at least EUR 125 (art. 77(3)) | LTVA |
| Interest after a formal payment demand (contrainte) | 7.2% a year from the day the demand is served (art. 85) | LTVA |
| Aggravated fraud | Above a quarter of the tax due and at least EUR 10,000 per period, or above EUR 200,000 per period: prison and fines (art. 80) | LTVA |

Fines are set by the AED director and are payable within one month of notice; a reasoned objection can be filed within three months (arts. 78 and 79). Missing or doubtful returns can lead to an ex officio assessment (taxation d'office, arts. 73 to 76).

## Cross-border points

- **Services to EU businesses.** A general-rule B2B service is taxed where the customer is. Invoice net with a reverse-charge note, show the amount in the return as a service supplied in another member state (art. 64(2)), and report it in the recapitulative statement.
- **Services bought from abroad.** The Luxembourg business customer owes the tax and deducts it if entitled. Check the invoicing entity: several large platforms invoice from Luxembourg entities (for example Amazon EU Sàrl), and those invoices carry Luxembourg VAT, not a reverse charge.
- **Goods.** Intra-EU supplies to a buyer identified in another member state are exempt and go in the recapitulative statement. Intra-EU acquisitions are taxed in Luxembourg at the Luxembourg rate and deducted in the same return.
- **EU SME scheme.** A Luxembourg small business that wants the franchise in another member state notifies the AED in advance through MyGuichet.lu, gets an "EX" number, stays under that state's limit and the EUR 100,000 EU-wide limit, and reports its turnover per member state to the AED every quarter (art. 57quater; AED SME page).
- **Frontier workers and non-resident individuals:** see [lu-cross-border](lu-cross-border.md). Owner's income tax: [luxembourg-income-tax](luxembourg-income-tax.md).

## Worked examples

### Example 1: Quarterly filer, Q2 2026, with a reverse-charged US subscription

A consultancy in Esch-sur-Alzette had 2025 turnover of EUR 300,000, so it files quarterly plus an annual return. For April to June 2026 it invoiced EUR 30,000 net to Luxembourg clients at 17%. It paid EUR 2,000 for a US software subscription, which is reverse-charged at 17%. Input VAT on Luxembourg invoices is EUR 2,100.

Output VAT is 5,100, plus 340 on the reverse charge, EUR 5,440. Input VAT is 2,100 plus 340, EUR 2,440. The return shows EUR 3,000 to pay, filed on eCDF and paid before 15 July 2026. If the payment is 60 days late, the late-payment fine under art. 77(1) cannot exceed 10% a year: 3,000 x 10% x 60 / 365 = EUR 49.32 at most.

```oa-check
name: Luxembourg quarterly return Q2 2026 with reverse charge and late-payment fine cap
inputs:
  sales_17: 30000
  rc_service: 2000
  domestic_input_vat: 2100
  days_late: 60
steps:
  - out_17: sales_17 * 0.17
  - rc_vat: rc_service * 0.17
  - output_total: out_17 + rc_vat
  - input_total: domestic_input_vat + rc_vat
  - payable: output_total - input_total
  - max_late_fine: round(payable * 0.10 * days_late / 365, 2)
expected:
  out_17: 5100
  output_total: 5440
  input_total: 2440
  payable: 3000
  max_late_fine: 49.32
```

### Example 2: Franchise business crosses the threshold, inside and then outside the tolerance

A graphic designer established in Luxembourg had 2025 turnover of EUR 42,000 and is under the franchise in 2026. Turnover to 31 October 2026 is EUR 49,000 net. A EUR 4,500 job in November takes the year to EUR 53,500: over EUR 50,000 but within the 10% tolerance (EUR 55,000), so the franchise continues for 2026 (art. 57bis(6)(a)). Because 2026 went over EUR 50,000, the franchise is lost for 2027.

On 10 December a EUR 2,000 job takes the year to EUR 55,500, more than 10% over the threshold. The franchise ends from the day after that day (art. 57bis(6)(b)), so the 10 December job stays exempt, but a EUR 1,500 job on 15 December is taxable at 17%: VAT EUR 255. The designer must be identified for VAT from 11 December and file returns from then on.

```oa-check
name: Luxembourg franchise threshold, tolerance and first taxable sale (2026)
inputs:
  turnover_to_october: 49000
  november_job: 4500
  crossing_job: 2000
  later_job: 1500
  threshold: 50000
  tolerance_pct: 10
steps:
  - tolerance_ceiling: threshold + pct(threshold, tolerance_pct)
  - after_november: turnover_to_october + november_job
  - after_crossing: after_november + crossing_job
  - excess_over_ceiling: after_crossing - tolerance_ceiling
  - vat_on_later_job: later_job * 0.17
expected:
  tolerance_ceiling: 55000
  after_november: 53500
  after_crossing: 55500
  excess_over_ceiling: 500
  vat_on_later_job: 255
```

## Ask the client first

1. What was your turnover (and intra-EU purchases) in 2025? It sets the franchise and whether you file annually, quarterly or monthly.
2. Are you under the franchise, or did you opt for the normal regime (and when)?
3. Are you in financial services, funds or a holding structure, or do you have any exempt income? That needs a deduction ratio.
4. Which entity invoices you for each foreign service, and does the invoice show Luxembourg VAT?
5. Do you sell goods or B2B services to other EU countries, and do you hold your customers' VAT numbers?
6. Is there a credit balance or an earlier return that was late or wrong?

## Sources

| Source | URL | Read on |
|---|---|---|
| AED, coordinated LTVA at 1 January 2026 (arts. 39, 40, 54, 55, 57 to 57quater, 61, 64, 73 to 80, 85; annexes A to C) | https://pfi.public.lu/dam-assets/pdf/legislation/tva/loi/loi-tva-2026-01-01.pdf | 2026-10-23 |
| AED, publication page for the 2026 coordinated text | https://pfi.public.lu/fr/publications/textes-de-loi/tva010126.html | 2026-10-23 |
| Legilux, law of 20 December 2024 amending the LTVA (Mémorial A 574) | https://legilux.public.lu/eli/etat/leg/loi/2024/12/20/a574/jo | 2026-10-23 |
| AED, SME franchise from 1 January 2025 | https://pfi.public.lu/fr/professionnel/tva/sme.html | 2026-10-23 |
| AED, national rates | https://pfi.public.lu/fr/professionnel/tva/taxe-valeur-ajoutee/taux-nationaux-applicables.html | 2026-10-23 |
| AED, who owes the tax | https://pfi.public.lu/fr/professionnel/tva/taxe-valeur-ajoutee/debiteur-taxe.html | 2026-10-23 |
| AED, VAT returns (frequency and deadlines) | https://pfi.public.lu/fr/professionnel/tva/en-cours-activite-economique/declarations-tva.html | 2026-10-23 |
| AED, payment of the tax | https://pfi.public.lu/fr/professionnel/tva/en-cours-activite-economique/au-sujet-paiement-taxe.html | 2026-10-23 |
| AED, recapitulative statement | https://pfi.public.lu/fr/professionnel/tva/en-cours-activite-economique/etat-recapitulatif.html | 2026-10-23 |
| Guichet.lu, VAT return frequency and deadlines | https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/tva/declarations/declaration-tva.html | 2026-10-23 |

Not yet confirmed: the AED coordinated text is not binding and the consolidated text on Legilux was not available, so article wording should be checked against the Mémorial before a dispute; the grand-ducal regulation that sets the EUR 112,000 and EUR 620,000 filing bands was not read (the figures come from the AED and Guichet.lu pages); whether "before the 15th" allows filing on the 15th itself was not settled.
