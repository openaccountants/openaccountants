# Spain positive extraordinary-profit surcharge: evidence-only disposition

Read date: 27 October 2026. Worktree: `europe-spain`. Baseline HEAD: `33c86ed352ff457bb520f34389a941e3e73cd569` at commencement. No Guide, README, Git, commit, push, PR, database or client communication was changed by this subtask.

**The general ordinary positive surcharge is not ready to certify.** Fresh primary sources confirm the existing two gaps rather than closing them. The missing step is a legally specified conversion from the regulation's adjusted accounting-result growth to the corresponding taxable-base/gross-quota portions. Álava also lacks a located implementing provision defining that adjusted result and its exclusions. These are ordinary computation gaps and remain in the existing Guide; they have not been relabeled specialist cases. No narrow coincident-result example has been added to make the coverage appear complete.

## 1. The actual charging words do not specify a whole-quota rate

The complete current official PDFs were freshly downloaded, extracted and hashed. The operative pages were also rendered and visually read:

- [Bizkaia NF 11/2013, article 57 bis, PDF p.100](https://www.bizkaia.eus/documents/880307/15187815/ca_11_2013.pdf/5a463c1d-a59b-7e48-6429-80fd22f30bc6?t=1768908575887).
- [Álava NF 37/2013, article 56.7, PDF p.114](https://web.araba.eus/documents/d/araba/norma-foral-del-impuesto-sobre-sociedades_cas-3-pdf).
- [Gipuzkoa NF 2/2014, article 56.7, PDF p.137](https://www.gipuzkoa.eus/documents/2456431/8.0761374E7/NF%202-2014%20%282026%29.pdf/f1231a01-1f83-ee15-e569-7b9b84d44d54).

For each of the four bands, the actual text charges the *part of gross quota corresponding to the increase in taxable base derived from the specified excess*. It does not say that a single percentage derived from R is applied to the entire taxable base or entire gross quota. Nor does it provide a weighted-average whole-quota rate. The repeated marginal wording must not be replaced by such a rate merely because the resulting arithmetic is convenient.

Articles 57 separately define ordinary gross quota by applying the nominal rate to the taxable-base amount. Gipuzkoa's article 57 uses `base liquidable`; the other two use `base imponible`. That definition establishes the ordinary base-to-quota step. It does not specify how depreciation, timing differences, result-application reductions or loss compensation are attributed between the surcharge's R-derived slices.

[Bizkaia DF 203/2013 DA 10, PDF pp.74–76](https://www.bizkaia.eus/documents/880307/15187815/ca_203_2013.pdf/5d2f80fc-9d5b-0f71-b578-56da0a5a0c50?t=1679483614806) and [Gipuzkoa DF 17/2015 DA 9, PDF pp.87–88](https://www.gipuzkoa.eus/documents/2456431/8.0761381E7/DF%2017-2015%20%282026%29.pdf/ad233e14-7236-0450-948f-50a669df270f) define R as financial-statement profit before tax without depreciation/impairment, less the named income adjustments and authorised exceptional results. They supply zero/negative-history, credit, startup/restart and fiscal-group rules. I read the complete operative additional dispositions. Neither supplies the missing general R-to-taxable-base allocation or an explicit whole-quota formula.

B DA 34, A DA 31 and G DA 29 expressly disapply articles 59.3–5 and 67.1 for purposes of this surcharge and treat the fiscal group as taxpayer. That override is real and must remain. It does not itself define the taxable-base share belonging to each R band. An ordinary result must not silently apply or ignore credit caps based on an invented ordering.

**Exact unresolved provision:** an enacted implementation or authoritative application of B57bis/A56.7/G56.7 specifying what “corresponding” taxable-base/gross-quota portion means where the adjusted accounting measure and the final tax base differ. A binding instruction or official worked example with those differences would answer the practical question; a repeated headline of 1–4%, or an R-only definition, does not.

## 2. Ordinary practical impact, not a special-case gap

Assume a mature general-rate trading company, no medium-company status, four positive adjusted results, no excluding credit claim or authorised exceptional result. The three historical R values are each 100,000. Current accounting profit before tax is 150,000 after 30,000 depreciation; the permitted tax depreciation is also 30,000, with no other adjustment or loss. The regulation's current **R is 180,000**, while the ordinary **tax base is 150,000** and ordinary **24% gross quota is 36,000**.

R crosses the entry gate, and its four band quantities are 15,000 / 25,000 / 5,000 / zero. Weighting those quantities by 1/2/3/4% gives 800, before any disputed conversion. The following are **diagnostics of unconfirmed inferences, not approved tax answers**:

| Inference that would need authority | Arithmetic result | Missing authority |
|---|---:|---|
| Treat every R slice as an equal taxable-base slice, then its 24% quota | 192 | Does not account for the 30,000 depreciation deducted in arriving at the tax base but excluded from R |
| Derive a weighted R percentage and apply it proportionately to the whole 36,000 quota | 160 | No retrieved provision specifies the allocation factor `tax base/R` or this whole-quota percentage |
| Apply the R band boundaries directly to the 150,000 tax base | 36 | No retrieved provision authorises substituting that tax base for the regulation's R growth measure |
| Apply 1–4% directly to the R amounts as extra base-rate points | 800 | Omits the charging text's corresponding gross-quota requirement |

These competing arithmetic constructions show why matching R to the tax base in a simplified example would not resolve the ordinary issue. They are not presented as four legally valid interpretations. A source must first specify the actual conversion. The 35/50/75/100% boundaries and exclusion predicates themselves are separately recomputed in `controls.json`; those tests prove arithmetic under their stated diagnostic assumptions, not surcharge entitlement.

## 3. Álava implementation: fresh checks and precise remaining absence

Fresh [Álava DF 41/2014 current regulation](https://web.araba.eus/documents/d/araba/indice-reglamento-del-impuesto-sobre-sociedades-cas-5-pdf), 79 pages, still records amendments through DF 42/2025 and has no equivalent B/G extraordinary-profit disposition. This conclusion is based on the actual complete retained body, not only a failed web search.

I checked additional primary routes beyond the prior consolidation:

- The [live corporate normative inventory](https://web.araba.eus/es/hacienda/normativa/dispociciones-sociedades) is current through **DF 36/2026 of 13 October**, concerning crypto due diligence/information. Its later 2026 corporate entries concern that subject, exchange/information changes, crisis measures and their convalidations. It identifies no later surcharge implementing decree.
- The original [DF 42/2025, BOTHA 29 December 2025, article 2](https://www.araba.eus/botha/Boletines/2025/147/2025_147_03919_C.pdf), 32 pages, changes the corporate regulation but supplies no surcharge disposition. The complete corporate-amendment article was checked.
- Its [correction published 13 February 2026](https://www.araba.eus/botha/Boletines/2026/019/2026_019_00372_C.pdf), two pages, corrects the Basque title and underlining/format errors. It does not add a missing surcharge rule.
- The official [2026 legislative programme](https://irekia.araba.eus/documents/2908004/2938986/2.1%2B2025-12-23%2BAcuerdo%2B795%2Banexo%2BCAS%2Bcove.pdf/9730184b-0f97-2814-2e93-f465af6a5444?t=1766499116153), PDF p.3, lists further IRPF/CIT regulatory development. A programme is a plan, not an enacted implementing provision. It is not used as law or proof that no later enactment could exist.
- The current [corporate news](https://web.araba.eus/es/hacienda/sociedades/novedades-normativas) and [FAQ updated 2 July 2026](https://web.araba.eus/es/hacienda/sociedades/preguntas-frecuentes) did not supply the missing definition or numerical bridge. Their 2025 campaign context is retained.

**Exact Álava gap:** implementing text under article 56.7 that defines the adjusted result, its history and disapplication conditions, plus the R-to-taxable-base/quota bridge. A positive R under the Bizkaia/Gipuzkoa definitions cannot be imported into Álava without that authority. This is not an assertion that the surcharge is legally zero or inoperative.

## 4. Actual government filing/example routes checked

The sources were followed to their current public help rather than assuming a 2026 publication meant 2026 tax-year treatment.

- [Bizkaia current corporate landing](https://www.bizkaia.eus/es/impuesto-sociedades) is **Sociedades 2025**, filed in 2026. It links the public [individual application help](https://dfb.microsoftcrmportals.com/es-ES/sociedadesSEDE/), then the actual [60-page web-application guide](https://gidak.bizkaia.eus/content/imagenes/SOCIEDADES/Batuz_Gu%C3%ADa%20aplicaci%C3%B3n%20web%20del%20Impuesto%20sobre%20Sociedades%20-%20Individual%20-%202025%20V5%20-%2012JUNIO.pdf). The quota screen on p.40 was visually inspected. It supplies no new surcharge conversion. The authenticated filing application requires an entity representative certificate or registered authorisation; no private account or actual company return was entered.
- [Álava current campaign](https://web.araba.eus/es/hacienda/sociedades/mi-declaracion) identifies **OF 380/2026 for periods starting in 2025**. It is not an authority for the new positive 2026 charge merely because it was issued in 2026.
- Gipuzkoa's [treasury corporate page](https://www.gipuzkoa.eus/es/web/ogasuna/impuestos/sociedades) and [public model 200 page](https://www.gipuzkoa.eus/es/web/ogasuna/impuestos/modelo/200) identify **Modelo 200 (2025)**. The full [OF 259/2026](https://egoitza.gipuzkoa.eus/gao-bog/castell/bog/2026/06/24/c2604206.pdf) was downloaded; its first page expressly covers periods beginning in **2025**. Its 300-page bilingual annex is retained. This is not the 2026 surcharge campaign. The help-program navigation was checked, without installing or executing a downloaded program.
- An official [Bizkaia commission transcript, 16 October 2025](https://apps.bizkaia.eus/SIGP/servlet/MuestraArchivoServlet?archivo1=%2Fvar%2Fdatosbfafilec%2Fbfaprog%2FDATOS%2FSIGP%2Fpdf%2F12E0100001290010000276_1770280056175), contains discussion of extraordinary-profit taxation, the first-35% boundary, bank-tax compatibility and credit limits. The relevant exchanges on pp.8–9 and 18–19 were read. They provide no ordinary R-to-base numerical example and are not binding substitute computation rules.
- Focused primary-domain and exact-phrase searches sought actual surcharge examples, whole-quota rates, Álava regulations and interpretive consultations. Results primarily repeated the statute, regulation or pre-enactment proposals. Secondary commentary was treated only as a lead and is not cited as authority. The fresh underlying official B/G statutes/regulations were obtained successfully despite web search robots limitations. Earlier unrelated blocked model-232 leads were not retried.

## 5. PE interaction and disposition

The separate `pe-proposal.md` records the fresh full B/A/G IRNR bodies and their actual article 19 references. Resolving the corporate amount would not by itself resolve PE applicability. The existing nonresident Guide's careful reservation remains appropriate; there is no source-backed proposal to charge every PE or exempt every PE.

**Disposition for the parent:** keep the existing corporate ordinary-gap reservation, README partial status and separate PE applicability reservation. Do not claim this subtask completed ordinary positive surcharge coverage. The research evidence is ready for a different reviewer to assess. A future substantive correction should be based on the missing binding implementation/authoritative application, followed by source-driven numerical and boundary review.

## Preservation and checks

The corporate Guide is byte-identical to the pre-subtask snapshot, including metadata, version 0.1, full original text, URLs, byline/CTA status and both oa-check examples. The sibling nonresident Guide, README and frozen VAT files were also verified unchanged from this subtask's snapshots. `surgical.diff` is empty. Lost content restored: zero; no rewrite occurred. The corporate repository checker reports two blocks and no failures. There are 29 independent arithmetic/source-predicate controls and zero final failures. Full source receipts/hashes, rendered operative pages and exact no-loss hashes are retained. No dependency was installed. A text parser attempt found bs4 unavailable; the source extraction was completed with Python's standard HTMLParser instead.
