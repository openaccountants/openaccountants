---
name: cl-company-formation
description: >
  Chile company formation and entity choice for calendar 2026: ordinary SpA, Ltda., closed S.A. and EIRL,
  founder and capital conditions, the optional Registro de Empresas y Sociedades route, signatures,
  traditional registration and publication, RUT and the separate SII activity-start handoff. Distinguishes
  incorporation from tax regime, permits and bank onboarding; includes capital reconciliation and facts
  needed from foreign founders. Trigger on Chile company formation, constituir empresa, Tu Empresa en un Día,
  SpA, Ltda., EIRL, Registro de Empresas y Sociedades, RUT empresa and inicio de actividades. Excludes
  regulated entities, immigration, tax-neutral reorganisations and investment reporting; tax computations
  belong to the Chile corporate, VAT, payroll and cross-border Guides.
jurisdiction: CL
tax_year: 2026
last_updated: 2026-11-11
version: 0.1
category: formation
type: filing-howto
tier: 2
domain: formation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Chile company formation and entity choice, 2026 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** Choose the entity and the registration system separately. An ordinary SpA can have a single shareholder; an EIRL belongs to a natural person; a Ltda. requires multiple partners. The Registro de Empresas y Sociedades (RES, Tu Empresa en un Día) is an optional electronic formation system, not a tax regime. Ley 20.659 art. 21 replaces commercial-registry/publication formalities with the incorporated RES form for covered acts. Formation, RUT, SII activity registration and bank onboarding are separate milestones. The portal name is not an operating-time guarantee.

Calendar 2026; Chile; amounts in CLP unless labelled UF. The statutes were read through LeyChile's JSON service, including nested articles and current-version metadata, rather than truncated or deferred exports. The ordinary entity statutes still apply under RES except where Ley 20.659 changes a formality.

## Who this applies to

Founders choosing an ordinary Chilean SpA, Ltda., closed S.A. or EIRL, including a foreign investor arranging identification and representation. Entity choice depends on actual ownership, governance, financing and liability facts. No sourced market-share ranking establishes which vehicle foreign founders should use.

| Vehicle | Conditions and distinction | Official source |
|---|---|---|
| SpA | One or more persons; capital represented by shares; articles set rights, administration and representation. Closed-S.A. rules apply subsidiarily where compatible and the SpA rules/articles are silent | [Código de Comercio arts. 424-425](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=1974) |
| Ltda. | Two to fifty partners, limited to their capital contributions; examine the actual partnership agreement rather than treat interests as freely interchangeable shares | [RES FAQ, Ltda. section](https://www.registrodeempresasysociedades.cl/PreguntasFrecuentes.aspx) |
| S.A. | Shareholder contribution liability and board administration. The law distinguishes open, special and closed companies; this workflow covers an ordinary closed S.A. | [Ley 18.046 arts. 1-2](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=29473) |
| EIRL | A natural-person owner and separate patrimony. Specified misuse, acts outside the business and other art. 12 cases can create unlimited owner liability | [Ley 19.857 arts. 1-2,8,12](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=207588) |

Out of scope: banking, insurance, reciprocal-guarantee companies and other regulated vehicles; public securities offers; immigration and foreign-investment reporting; tax-neutral reorganisations; disputes or defective existing incorporations. Check their special capital, authorisation and reporting rules separately.

## Rates, bands and thresholds

| Item | Rule and conditions | Year | Source |
|---|---|---|---|
| SpA founders | One or more persons | 2026 | [Código de Comercio art. 424](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=1974): “una o más personas” |
| Ltda. partners | Two to fifty | 2026 | [RES entity FAQ](https://www.registrodeempresasysociedades.cl/PreguntasFrecuentes.aspx): “un mínimo de dos y un máximo de cincuenta socios” |
| Ordinary entity minimum capital | No statutory minimum in RES ordinary-company guidance; special regulated rules and committed capital still matter | 2026 | [RES help question 27](https://www.registrodeempresasysociedades.cl/AyudaRegistro.aspx): “no existe un capital mínimo establecido por la ley” |
| RES registry | Public and free; signing/notary services may cost separately | 2026 | [Ley 20.659 art. 11](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=1048718): “es público, gratuito” |
| RES signatures | All required signatures within sixty days of the first; otherwise treated as unsigned | 2026 | [Ley 20.659 art. 10](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=1048718): “dentro del plazo de sesenta días” |
| Traditional SpA extract | Registration and publication within sixty days of the formation act; this is a different period from RES signing | 2026 | [Código de Comercio art. 426, amended by Ley 21.608](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=1974): “sesenta días contados desde la fecha del acto” |
| SpA subscription/payment period | Articles set the period; if silent, five years from formation or the relevant capital increase, with statutory consequences for non-payment | 2026 | [Código de Comercio art. 434](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=1974): “el plazo será de cinco años” |
| SII activity-start notice | Within the two months following the month qualifying activities begin; art. 68 exceptions and actual start facts matter | 2026 | [Código Tributario art. 68](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=6374): “dentro de los dos meses siguientes a aquél” |

## The base

Prepare founder identities and capacity, proposed name, business and sector, domicile, entity type, capital and contributions, subscription/payment terms, share classes where applicable, administration and powers, duration and registration route. These are the SpA art. 425 and RES art. 6 matters adapted to each vehicle's own statute. Do not turn “free registry” into a total cost quote.

For an SpA, reconcile the precisely fixed capital and nominative shares under art. 434. Record committed capital separately from money actually paid. If assets require special transfer formalities, RES does not remove them (Ley 20.659 art. 8). A bank's funding/onboarding requirements are separate from a statutory capital minimum.

Incorporation does not itself establish eligibility for Pro Pyme or any tax rate. Load [cl-corporate-income-tax](cl-corporate-income-tax.md) with activity, revenue, related-party, ownership and election facts. Load [cl-vat-return](cl-vat-return.md) for taxable/exempt sales, documents and F29; [cl-payroll](cl-payroll.md) before hiring. Keep their computations and return dates in their owning Guides. The founder's residence is separately relevant to owner taxation and distributions.

## Deadlines and filing

1. **Choose the route.** For RES, open [the registry](https://www.registrodeempresasysociedades.cl/), select Constituir and the entity type, and authenticate. Check eligibility under Ley 20.659 art. 2 and actual portal support. For a traditional SpA, obtain the public deed or notarised/protocolised private instrument and comply with art. 426. Other traditional entities use their own formalities, not automatically the SpA deadline.
2. **Prepare the form/articles.** Enter founders, capital, business, administration and powers. Read the generated terms before signing: art. 10 prevents alteration of that form after the first signature. Asset transfers may require additional instruments under art. 8. Keep the input record and identify unresolved terms before signatures start.
3. **Sign correctly.** Ley 20.659 art. 9 uses advanced electronic signatures. A person without one signs before a notary who applies the required electronic signature. A simple tax certificate is not automatically sufficient for RES. Foreign powers require the applicable legalisation/apostille and representation evidence; a scan alone does not establish compliance. Complete all required signatures within the art. 10 period.
4. **Confirm registration and obtain evidence.** Use Obtener certificados and verify the signed formation/current-status and representation record. Ley 20.659 arts. 21-22 govern replacement formalities and evidential certificates. An unsigned saved draft is not proof of incorporation. Save the actual instrument and powers for tax and bank handoffs.
5. **Obtain/check company RUT.** SII's current RES FAQ directs these companies to obtain RUT through RES. Verify the assigned company identifier and representation; do not use the founder's personal identifier as the company's. Traditional-route tax registration uses the separate SII RUT procedure.
6. **Declare inicio de actividades separately.** The SII RES FAQ directs an authorised person to Servicios online → RUT e Inicio de actividades → Inicio de actividades → Iniciar Actividades, including from the post-formation link. Establish activity codes, domicile, representatives and supporting documents. Formation alone does not establish that the activity notice or document authorisation is complete. Código Tributario art. 68 requires the notice within the two months following the month activities begin; identify the first qualifying act, not merely the incorporation date. Its electronic tax folder carries the initial form and supporting records. Res. 77/2025 describes activity and location, identity and contact data; individual businesses also report capital and relevant assets. Attach the case-specific supporting identity, representation and domicile records required by its Annex II. The resolution gives supporting documents a maximum age of one year, and a five-day correction period after a request to cure an incomplete application. Article 68 preserves an office route for the specified no-connectivity, no-electricity or catastrophe cases. Check later amendments and actual portal requests before submission; the older blanket “before operating” deadline is not the statutory wording.
7. **Complete the operating handoff.** Record SII acknowledgement, activities, tax regime and invoicing status. Bank onboarding, municipal permission and sector approvals remain separate checks. No guaranteed bank-opening deadline or acceptance was established. Schedule the applicable tax returns and information declarations from the relevant current Guides and SII instructions.

## Penalties and interest

Missed formation formalities can affect existence or validity. RES art. 10 treats the unsigned-after-deadline form as not subscribed. EIRL art. 7 sets nullity/personal-liability consequences for omitted solemnities, subject to applicable curing rules. Refer defects for legal repair; do not re-date an act or assume RUT cures formation. No generic formation-fine amount or SII late-registration penalty computation is supplied here. Subsequent VAT, income-tax and payroll failures use the respective tax rules.

## Cross-border points

Foreign participation does not establish permission to work, residence, an authorised tax representative or a bank account. Check the founder's identification, legal status, foreign-document formalities and who may act before SII. Res. 77/2025 requires the stated foreign investors and foreign branches to appoint a representative with domicile or residence in Chile and sufficient powers for SII acts. RES's investor-RUT guidance does not mean every foreign investor can use every remote-signing mechanism. Use [cl-cross-border](cl-cross-border.md) for residence, permanent establishment and outbound payments. Foreign-founder participation statistics and a blanket absence of sector restrictions were not established.

## Two worked examples that recompute

### 1. Capital reconciliation

A sole founder commits CLP 8,000,000 to an ordinary SpA represented by 1,000 shares on equal subscription terms. CLP 3,000,000 is paid and CLP 5,000,000 remains committed under its articles. The assumed per-share amount is CLP 8,000. These are illustrative inputs, not statutory capital requirements. If the articles are silent on payment time, art. 434 supplies its five-year default; if they specify a period, use that term. A sole founder would not satisfy the Ltda. minimum; an EIRL needs the natural-person and separate-patrimony analysis instead.

```oa-check
name: CL SpA illustrative capital reconciliation
inputs:
  capital: 8000000
  shares: 1000
  paid: 3000000
steps:
  - amount_per_share: capital / shares
  - unpaid: capital - paid
  - reconciled: paid + unpaid
expected:
  amount_per_share: 8000
  unpaid: 5000000
  reconciled: 8000000
```

### 2. Paid capital changes, commitment stays fixed

Using the same illustrative CLP 8,000,000 commitment, the founder pays another CLP 2,000,000 under the articles. Paid capital becomes CLP 5,000,000 and unpaid capital CLP 3,000,000. A later instalment is not automatically a new capital increase: check the underlying subscribed obligation and actual instrument. This reconciles the art. 434 paid/unpaid distinction without inventing a tax result or a minimum funding level.

```oa-check
name: CL SpA subsequent payment reconciliation
inputs:
  commitment: 8000000
  previously_paid: 3000000
  instalment: 2000000
steps:
  - now_paid: previously_paid + instalment
  - remaining: commitment - now_paid
expected:
  now_paid: 5000000
  remaining: 3000000
```

## Ask the client first

1. Founder count, natural/legal-person status, identification and authority to sign, including foreign documents.
2. Business, regulated sector, domicile and non-cash contributions.
3. Capital, share classes, amounts paid, commitments and payment dates.
4. Administration, powers and future investor-entry needs.
5. Chosen registration route, signatures already made and their dates, registry/RUT/SII acknowledgements.
6. Expected turnover, ownership and staff for separate tax-regime, VAT and payroll handoffs.

## Sources

| Source and portions read | URL | Read on |
|---|---|---|
| Código de Comercio, current JSON metadata and arts. 424-426,434 | https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=1974 | 2026-11-11 |
| Ley 20.659, current JSON arts. 1-2,6,8-11,21-22 | https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=1048718 | 2026-11-11 |
| Ley 19.857, current JSON arts. 1-12 | https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=207588 | 2026-11-11 |
| Ley 18.046, current JSON arts. 1-2, board and company classes | https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=29473 | 2026-11-11 |
| RES entity FAQ, Ltda., entity choices, signing and foreign identification | https://www.registrodeempresasysociedades.cl/PreguntasFrecuentes.aspx | 2026-11-11 |
| RES help question 27, capital; current FAQ registry cost and signing | https://www.registrodeempresasysociedades.cl/AyudaRegistro.aspx ; https://www.registrodeempresasysociedades.cl/FAQ.aspx?seccion=1 | 2026-11-11 |
| SII current RES RUT FAQ and RES activity-start portal FAQ | https://www.sii.cl/preguntas_frecuentes/rut_inicio_actividades/001_105_6358.htm ; https://www.sii.cl/preguntas_frecuentes/rut_inicio_actividades/001_105_6361.htm | 2026-11-11 |
| Código Tributario, current JSON art. 68, activity-start deadline and electronic folder | https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=6374 | 2026-11-11 |
| SII Res. 77/2025, RUT procedure I and activity-start procedure II, general form and evidence sections | https://www.sii.cl/normativa_legislacion/resoluciones/2025/reso77.pdf | 2026-11-11 |

Not yet confirmed: later registration amendments and case-specific portal/document requirements beyond the portions of Res. 77/2025 read here; a guaranteed one-day or six-to-eight-week operating/bank timeline; a universal USD incorporation cost, notary/signature/publication quote or bank fee; regulated-entity capital; municipal, foreign-investment and immigration procedures. The old generic timelines, cost estimate and “most common for foreign founders” ranking are not established primary-source promises.
