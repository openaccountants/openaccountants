---
name: es-foral-corporate-tax-extraordinary-profit-surcharge
description: >
  Compute the 2026–2030 extraordinary-profit surcharge in Bizkaia, Gipuzkoa and Álava corporate tax. Covers which companies are in scope by nominal rate and the art. 13 medium-company exclusion, the Bizkaia/Gipuzkoa profit measure before depreciation and impairment with its regulatory exclusions, the mean of the three prior positive measures, the 1% to 4% growth slices applied to the corresponding gross-quota portion, the ordinary attribution ledger, and Álava's own-law net-result interpretation with the tax-expense feedback. Use for gravamen sobre beneficios extraordinarios, recargo, cuota íntegra incrementada and beneficio contable in the Basque territories. Navarra has no such surcharge in this pack. Load es-foral-corporate-tax first for the base and the quota. Split unchanged from es-foral-corporate-tax on 6 November 2026.
jurisdiction: ES
category: international
tax_year: 2026
last_updated: 2026-11-14
version: 0.8
tier: 2
domain: corporate-tax
type: computation
depends_on:
  - es-foral-corporate-tax
---

# Spain: Basque extraordinary-profit corporate tax surcharge, 2026–2030 v0.8

This Guide holds part of [es-foral-corporate-tax](es-foral-corporate-tax.md), moved here unchanged on 6 November 2026 so that each Guide stays within the size the site can deliver. Built from the law; not yet approved by an accountant.

## Who this applies to

A company taxed under Bizkaia, Álava or Gipuzkoa corporate tax law at the general, bank or hydrocarbon rate, other than an art. 13 medium company, for periods 2026 to 2030, under the governing-law tests in [es-foral-corporate-tax](es-foral-corporate-tax.md#who-this-applies-to). Compute the base and the ordinary gross quota there first.

## Rates, bands and thresholds

The nominal rates, and the ordinary gross quota the surcharge increases, are in [es-foral-corporate-tax](es-foral-corporate-tax.md#rates-bands-and-thresholds). The growth slices and additional percentages are in the rules below.

| Current accounting result `R` against mean `M` of the three previous positive results | Additional percentage on the corresponding gross-quota portion | Source |
|---|---:|---|
| Above 1.35 M up to 1.50 M | 1% | [Bizkaia NF11/2013 art.57 bis](https://www.bizkaia.eus/documents/880307/15187815/ca_11_2013.pdf/5a463c1d-a59b-7e48-6429-80fd22f30bc6?t=1768908575887), [Álava NF37/2013 art.56.7](https://web.araba.eus/documents/d/araba/norma-foral-del-impuesto-sobre-sociedades_cas-3-pdf), [Gipuzkoa NF2/2014 art.56.7](https://www.gipuzkoa.eus/documents/2456431/8.0761374E7/NF%202-2014%20%282026%29.pdf/f1231a01-1f83-ee15-e569-7b9b84d44d54) |
| Above 1.50 M up to 1.75 M | 2% | same |
| Above 1.75 M up to 2 M | 3% | same |
| Above 2 M | 4% | same |

## The base

### Extraordinary-profit surcharge2026–2030

All three current Basque corporate statutes add this branch for general 24%, bank 28% and hydrocarbon 31% taxpayers other than art.13 medium companies; ordinary micro/small 20% companies do not fall within the named rate categories. Its operation is more specific than adding 1–4 points to taxable income. Statutory wording applies the additional percentage to the **part of gross quota corresponding to the taxable-base increase derived from the excess**. [B art.57 bis and DA 34; A art.56.7; G art.56.7 and art.57.](https://www.bizkaia.eus/documents/880307/15187815/ca_11_2013.pdf/5a463c1d-a59b-7e48-6429-80fd22f30bc6?t=1768908575887), [Álava NF37/2013](https://web.araba.eus/documents/d/araba/norma-foral-del-impuesto-sobre-sociedades_cas-3-pdf), [Gipuzkoa NF2/2014](https://www.gipuzkoa.eus/documents/2456431/8.0761374E7/NF%202-2014%20%282026%29.pdf/f1231a01-1f83-ee15-e569-7b9b84d44d54)

For Bizkaia/Gipuzkoa, start from pre-tax financial-statement profit before depreciation and impairment, minus the income adjustments in chapterIII of titleIV and approved exceptional results. Compare current positive measure `R` with mean `M` of the previous three positive measures. Regulations exclude any zero/negative result in current/prior three years, the first four periods from starting/restarting after at least a year inactive, and claims to the expressly listed investment/research/environment/employment credits in current/prior three periods. Exceptional-result exclusions require the local Director-General's decision. Tax groups need the regulation's consolidated-result/history rules; do not mechanically add individual surcharges. [BR DA 10; GR DA 9.](https://www.bizkaia.eus/documents/880307/15187815/ca_203_2013.pdf/5d2f80fc-9d5b-0f71-b578-56da0a5a0c50?t=1679483614806), [Gipuzkoa DF17/2015](https://www.gipuzkoa.eus/documents/2456431/8.0761381E7/DF%2017-2015%20%282026%29.pdf/ad233e14-7236-0450-948f-50a669df270f)

The growth slices are `(1.35 M,1.50 M]` at 1%,`(1.50 M,1.75 M]` at 2%,`(1.75 M,2 M]` at 3%, and above`2 M` at 4%, applied to the corresponding gross-quota portion. Use the expressly labelled attribution-ledger interpretation below to reconcile fully taxable excess profit to its corresponding gross-quota portions; this does not assume that every accounting-profit slice is taxable or permit a blanket average allocation. [B art.57 bis; A/G art.56.7.](https://www.bizkaia.eus/documents/880307/15187815/ca_11_2013.pdf/5a463c1d-a59b-7e48-6429-80fd22f30bc6?t=1768908575887), [Álava NF37/2013](https://web.araba.eus/documents/d/araba/norma-foral-del-impuesto-sobre-sociedades_cas-3-pdf), [Gipuzkoa NF2/2014](https://www.gipuzkoa.eus/documents/2456431/8.0761374E7/NF%202-2014%20%282026%29.pdf/f1231a01-1f83-ee15-e569-7b9b84d44d54)

Álava's own article 56.7 supplies the charging bands. The own-law net-result worksheet below supplies a labelled ordinary-accounting and tax-attribution interpretation for its stated PGC/current-tax population. A special delegated measurement equivalent has not been established from the retained regulation or the fresh operative amendments; the worksheet does not claim one. Do not import B/G's pre-tax/depreciation definition or regulatory exclusions. The delegated comparison and any controlling own definition or contrary interpretation remain expressly distinguished from an assumed suspension or zero charge. B DA34, A DA31 and G DA29 disapply arts.59.3–5 and67.1 for applying this surcharge and identify the fiscal group as taxpayer; they do not change the nominal rate in art.56.1. Gipuzkoa GR DA9 currently names art.66 quinquies in its exclusion list. Sources: the own statutes and regulations linked above.

**Ordinary attribution-ledger method, reasoned from each own primary law.** This interpretation reads B57bis/G56.7 together with each province's arts.15,31 and57 and its own profit-measure regulation. First record the actual local eligibility and exclusion tests above, each of the four period measures, `M`, the nominal rate and the full accounts-to-tax reconciliation. Define accounting growth slices `E1=max(0,min(R,1.50M)-1.35M)`, `E2=max(0,min(R,1.75M)-1.50M)`, `E3=max(0,min(R,2M)-1.75M)`, `E4=max(0,R-2M)`. For each slice record the taxable-base increment `I_j` actually derived from that profit, with its identifiable tax additions, exclusions, deductions and used losses. Apply the selected law's tax treatment to those facts; an unsupported allocation is not a verified input. For a constant general24% rate, the corresponding gross-quota portion is `q_j=24% × I_j` and the additional quota is `S=1%q1+2%q2+3%q3+4%q4`. Ordinary gross quota plus `S` is the increased gross quota. This is a source-derived computation, not a published provincial algebra ruling. Álava's own articles 15/31/56.7/57 also support the conditional quota step; the separate net-result worksheet below derives its own `R/M/I_j` from the stated fully taxable PGC/current-tax ledger rather than stipulating approved measurements. Other accounting and tax-adjustment populations remain bounded as stated there. Sources: B/A/G arts.15,31,56–57 and B57bis, BR DA10/GR DA9, linked above.

A fully taxable incremental-profit ledger supplies a positive ordinary B/G case. Assume a standalone general24% trading company which fails the art.13 medium-company size tests, has been active for more than four periods, has no group/restart/exceptional-result issue, and has claimed none of its own regulation's excluded credits in any of the four periods. Each previous period has pre-tax profit80,000 and deductible depreciation20,000, giving own `R=100,000` and `M=100,000`. Current pre-tax profit190,000 plus deductible depreciation60,000 gives `R=250,000`; no impairment, income adjustment, reserve deduction, other tax difference, used loss or credit changes these figures. The actual operating-profit ledger establishes that the60,000 depreciation belongs to the continuing business and that the115,000 profit above `1.35M` consists of additional fully taxable income with no attributable expense or tax adjustment. Thus the underlying business at `R=135,000` has taxable profit75,000, and adding the four excess slices15,000/25,000/25,000/50,000 reconciles exactly to actual taxable base190,000. This is factual attribution of the excess, not a rule assigning every company's depreciation to its underlying business. Sources: each own15/16/31/56.1/57 and surcharge/regulatory provisions above; art.13 tests are supplied earlier.

| Ledger component | Accounting-profit slice | Attributable taxable increment |24% gross-quota portion | Additional percentage | Additional quota |
|---|---:|---:|---:|---:|---:|
| Above35% to50% |15,000 |15,000 |3,600 |1% |36 |
| Above50% to75% |25,000 |25,000 |6,000 |2% |120 |
| Above75% to100% |25,000 |25,000 |6,000 |3% |180 |
| Above100% |50,000 |50,000 |12,000 |4% |480 |
| Total excess |115,000 |115,000 |27,600 | |816 |

Ordinary gross quota is `190,000 ×24%=45,600`; increased gross quota is `45,600+816=46,416`. Assuming the only accounting tax expense is that current charge, net accounting profit143,584 plus nondeductible tax expense46,416 reconciles to pre-tax/taxable profit190,000, and adding depreciation60,000 recovers `R=250,000`. The surcharge is a quota increase, not a deduction from taxable income. All amounts here are exact whole euros; the example establishes no intermediate or return-field rounding convention. Applying `BI/R` to every slice would instead produce620.16 without an attribution basis; using190,000 as `R` would produce264 using the wrong growth measure; applying the additional percentages directly to the115,000 profit slices would produce3,400 on the wrong charge base. The816 result follows the stated ledger and own gross-quota wording. Sources: each own15/31/57 and surcharge provisions above.

For a different case, retain a reconciliation showing where depreciation/impairment, income adjustments, reserves, interest restrictions and used losses actually affect the increment; neither whole-company `BI/R` averaging nor automatic `I_j=E_j` supplies missing facts. The ordinary method is computable where the attribution is established, including the fully taxable ledger above. A disputed attribution or interaction with a non-linear adjustment needs its own reasoned legal allocation before use; the Guide does not invent a universal allocation order. Actual zero/negative-history, excluded-credit and startup cases follow the own B/G regulation rather than this positive illustration. Álava's separate ordinary net-result interpretation follows below; its own delegation and contrary-interpretation limit remain stated. Sources: own15 and surcharge/regulatory provisions above.

### Álava: labelled ordinary net-result interpretation

**Own-law interpretation for a fully taxable PGC company.** Álava article 56.7 uses an accounting result and delegates comparison terms, but does not expressly defer its 2026–2030 charging command until a regulation exists. This worksheet gives the undefined term its ordinary technical accounting meaning under own NFGT article 11.1–2 and NF 37/2013 article 15.3: use the final net result in the applicable PGC profit-and-loss account, including its income-tax expense. Do not add back depreciation or impairment to that measure under Bizkaia/Gipuzkoa's different regulation. This is a reasoned interpretation of Álava's own operative text and accounting incorporation, not an identified special implementing definition, binding tax direction or ruling. [Own NFGT article 11](https://web.araba.eus/documents/d/araba/indice-norma-foral-general-tributaria-cas-8-pdf), [NF 37/2013 articles 15/31/56–57](https://web.araba.eus/documents/d/araba/norma-foral-del-impuesto-sobre-sociedades_cas), [Código de Comercio article 35](https://www.boe.es/buscar/act.php?id=BOE-A-1885-6627#a35), [PGC NRV 13.4 and normal profit-and-loss model](https://www.boe.es/buscar/act.php?id=BOE-A-2007-19884).

Apply this bounded worksheet to a standalone mature ordinary company subject to Álava's general 24% rate, outside article 13 medium-company status, using the same PGC basis and three actual positive prior-period net results. Establish the arithmetic mean `M` from those accounts. For the current year, require that all pre-tax profit `E` is taxable, all non-tax expenses including the stated depreciation are deductible, and the only accounts-to-tax correction is the current corporate-tax expense. There are no current credits, used losses, reserves, deferred-tax movements, tax charged directly to equity, interrupted operations or other tax differences in this worksheet. These are explicit input bounds, not a statement that other ordinary companies owe no surcharge.

PGC NRV 13.4 includes current and deferred tax in the profit-and-loss tax expense, subject to its express exceptions; the current-only conditions above eliminate those additional interactions. Own article 31.1(b) then adds back the current corporate-tax expense, including this surcharge, when determining taxable base. With `t=0.24`, additional quota `S`, and final net accounting result `R`, the current ledger is `BI=E`, `Q=t×E+S` and `R=E−Q`. The surcharge is not itself a deductible cost reducing `BI`. Álava's actual [OF 380/2026 annex for the 2025 return](https://www.araba.eus/botha/Boletines/2026/073/2026_073_01914_C.pdf) distinguishes net profit-and-loss result in field 1000 from the before-tax result in 1005. This corroborates the accounting distinction; it is not a tested 2026 surcharge form or an instruction applying this interpretation to article 56.7.

**Taxable excess and the tax-expense feedback.** At the first trigger, net result `1.35×M` corresponds to pre-tax/taxable profit `E0=1.35×M/(1−t)`, with no surcharge yet. If `E≤E0`, this worksheet produces no surcharge. Above that point, under this selected correspondence reading, use net-result band widths `0.15×M`, `0.25×M`, `0.25×M`, then an unlimited remainder, with additional quota percentages `a=1%,2%,3%,4%` respectively. For a taxable increment `I` in one band, the ordinary quota is `t×I`, its surcharge is `a×t×I`, and the resulting net-accounting increment is `I−t×I−a×t×I`. Thus a finite net-result band width `W` admits taxable increment `W/(1−t−a×t)`. Starting with the actual taxable profit above `E0`, fill those taxable capacities sequentially; call the admitted amounts `I1` through `I4`. Calculate `S=t×(0.01×I1+0.02×I2+0.03×I3+0.04×I4)`. Finally reconcile the resulting `R`, `Q` and `BI`. This expressly derives the taxable increase from the accounting excess and its own article 31 tax correction; merely applying 24% to net slices would omit that correction. The correspondence and its feedback are a disclosed source-derived attribution interpretation, not a published provincial algebra rule.

The bullets grammatically attach these percentage comparisons to the taxable-base increase derived from the accounting excess. This worksheet reads them as boundaries of that accounting excess before mapping each band to its corresponding taxable increase; a literal comparison of the taxable-base increase itself with those thresholds is a competing interpretation not settled by the cited accounting rules.

**Separating ordinary ledger.** The calendar-2026 company has operated continuously for more than four years, is not in a fiscal group, has no special regime or exceptional transaction, and has verified turnover and assets of €60 million each and an average workforce of 300 for the article 13 tests. Each actual 2023–2025 account records pre-tax profit €100,000, current corporate-tax expense €24,000 and final net profit €76,000. Therefore `M=76,000`; the statutory net trigger is €102,600 and `E0=135,000`. Current operating income less deductible operating costs before depreciation is €250,000; deductible accounting depreciation is €60,000, giving `E=BI=190,000`. The €60,000 depreciation and other non-tax costs belong to the continuing business and do not change across the excess-profit increments, which consist of additional fully taxable operating receipts. Thus the underlying €135,000 taxable profit has €195,000 operating surplus before that depreciation, and the additional €55,000 receipts reconcile to current taxable profit. The current-only/no-other-difference conditions above apply.

| Net-result band | Net band width | Attributable taxable increment | Additional quota |
|---|---:|---:|---:|
| Above 35% to 50% | €11,400 | €15,047.518479… | €36.114044… |
| Above 50% to 75% | €19,000 | €25,158.898305… | €120.762712… |
| Above 75% to 100%, used portion | €11,136.609445… | €14,793.583216… | €106.513799… |
| Above 100% | €0 | €0 | €0 |
| Total used excess | €41,536.609445… | €55,000 | €263.390555… |

The exact surcharge is `29432841/111746` euros. Ordinary quota €45,600 plus surcharge gives `Q=45,863.390555…`; final net `R=144,136.609445…` falls in the stated third band. `R+Q=190,000` reconciles the taxable base, while net excess €41,536.609445… plus its associated ordinary/additional tax correction €13,463.390555… reconciles the €55,000 taxable excess. With no credits or advance payments the charge is €45,863.39 when displayed at cents. A consistent before-tax-only comparator using the prior €100,000 pre-tax mean would give surcharge €264; it is not the selected net-result method. Scaling all profit/depreciation figures by 100 scales that difference to approximately €60.94. Displayed decimals are for readability, not a certified intermediate or return-field rounding convention.

Álava's enacted [NF 17/2025 final provision 1 / DA 31](https://web.araba.eus/documents/d/araba/norma-foral-del-imic) disapplies articles 59.3–5 and 67.1 for the surcharge and identifies the fiscal group as taxpayer. It does not define accounting result, replace the ordinary 24% nominal rate or justify reducing the surcharge by an ordinary credit-use ceiling. [NF 21/2025 article 3.Cuarto](https://www.araba.eus/botha/Boletines/2025/147/2025_147_03861_C.pdf) supplies the operative 2026–2030 article 56.7 wording. The exact delegated comparison remains relevant: a controlling own definition or contrary interpretation must be applied on its own terms. This worksheet does not establish a universal net-profit rule for banks, groups, zero/negative or incomparable history, exceptional items, deferred tax, current credits, losses or other adjustments. Their accounting/tax attribution and any authoritative challenge to the selected net-result reading remain precise ordinary limits; they are not resolved by a B/G transplant, a stipulated approved `R` or an assumed suspension of Álava's enacted charge.

## Deadlines and filing

The surcharge is self-assessed in the annual corporate tax return; deadlines and forms are in [es-foral-corporate-tax](es-foral-corporate-tax.md#deadlines-and-filing).

## Penalties and interest

See [es-foral-corporate-tax](es-foral-corporate-tax.md#penalties-and-interest).

## Cross-border points

The governing law and collection allocation are settled in [es-foral-corporate-tax](es-foral-corporate-tax.md#who-this-applies-to) before this computation.

## Two worked examples that recompute

### Example 1: Bizkaia/Gipuzkoa fully taxable incremental-profit ledger

This is the ledger stated under "Extraordinary-profit surcharge2026–2030", recomputed. `M = 100,000`, current `R = 250,000`, general rate **24%**, all excess fully taxable. Slices above 1.35M: **15,000** at 1%, **25,000** at 2%, **25,000** at 3% and **50,000** at 4%. The additional quota is `24% × (1% × 15,000 + 2% × 25,000 + 3% × 25,000 + 4% × 50,000) = 816`. Ordinary gross quota `190,000 × 24% = 45,600`; increased gross quota **46,416**.

```oa-check
name: Bizkaia/Gipuzkoa extraordinary-profit surcharge, fully taxable ledger
inputs:
  m: 100000
  r: 250000
  taxable_base: 190000
  rate: 0.24
steps:
  e1: max(0, min(r, 1.50 * m) - 1.35 * m)
  e2: max(0, min(r, 1.75 * m) - 1.50 * m)
  e3: max(0, min(r, 2 * m) - 1.75 * m)
  e4: max(0, r - 2 * m)
  surcharge: rate * (0.01 * e1 + 0.02 * e2 + 0.03 * e3 + 0.04 * e4)
  ordinary_quota: taxable_base * rate
  increased_quota: ordinary_quota + surcharge
expected:
  e1: 15000
  e2: 25000
  e3: 25000
  e4: 50000
  surcharge: 816.00
  ordinary_quota: 45600.00
  increased_quota: 46416.00
```

### Example 2: Álava own-law net-result worksheet with the tax-expense feedback

This is the "Separating ordinary ledger" stated under "Álava: labelled ordinary net-result interpretation", recomputed. `M = 76,000`, `t = 24%`, taxable profit `E = 190,000`. The trigger net result `1.35 × 76,000 = 102,600` corresponds to `E0 = 102,600 / 0.76 = 135,000`, leaving **55,000** of taxable excess. Band widths in net result: `0.15M = 11,400` at 1% and `0.25M = 19,000` at 2%, admitting taxable `11,400 / (1 − 0.24 − 0.0024)` and `19,000 / (1 − 0.24 − 0.0048)`; the remainder falls in the 3% band. The additional quota is **263.39** (263.390555… in the stated ledger).

```oa-check
name: Álava net-result worksheet, taxable capacities and additional quota
inputs:
  m: 76000
  t: 0.24
  e: 190000
steps:
  e0: 1.35 * m / (1 - t)
  excess: e - e0
  i1: min(excess, 0.15 * m / (1 - t - 0.01 * t))
  i2: min(excess - i1, 0.25 * m / (1 - t - 0.02 * t))
  i3: min(excess - i1 - i2, 0.25 * m / (1 - t - 0.03 * t))
  surcharge: round(t * (0.01 * i1 + 0.02 * i2 + 0.03 * i3), 2)
expected:
  e0: 135000
  excess: 55000
  surcharge: 263.39
```

## Ask the client first

1. Which territory's corporate tax law governs the company, and what is its nominal rate?
2. Does the company meet the art. 13 medium-company tests, and how long has it been active?
3. What were the profit measures for the current and three previous periods, and were any excluded credits claimed in those periods?
4. Which accounting and tax adjustments affect the excess profit, and is the company in a tax group?

## Sources

| Official source | Provisions read | Read on |
|---|---|---|
|[Bizkaia NF11/2013](https://www.bizkaia.eus/documents/880307/15187815/ca_11_2013.pdf/5a463c1d-a59b-7e48-6429-80fd22f30bc6?t=1768908575887) |Current provisions cited above; separate2026 amendments read alongside consolidations |2026-10-27 |
|[Álava NF37/2013](https://web.araba.eus/documents/d/araba/norma-foral-del-impuesto-sobre-sociedades_cas-3-pdf) |Current provisions cited above; separate2026 amendments read alongside consolidations |2026-10-27 |
|[Gipuzkoa NF2/2014](https://www.gipuzkoa.eus/documents/2456431/8.0761374E7/NF%202-2014%20%282026%29.pdf/f1231a01-1f83-ee15-e569-7b9b84d44d54) |Current provisions cited above; separate2026 amendments read alongside consolidations |2026-10-27 |
|[Bizkaia DF203/2013](https://www.bizkaia.eus/documents/880307/15187815/ca_203_2013.pdf/5d2f80fc-9d5b-0f71-b578-56da0a5a0c50?t=1679483614806) |Current provisions cited above; separate2026 amendments read alongside consolidations |2026-10-27 |
|[Gipuzkoa DF17/2015](https://www.gipuzkoa.eus/documents/2456431/8.0761381E7/DF%2017-2015%20%282026%29.pdf/ad233e14-7236-0450-948f-50a669df270f) |Current provisions cited above; separate2026 amendments read alongside consolidations |2026-10-27 |
|[Álava NF6/2005 arts26–28/195](https://web.araba.eus/documents/d/araba/indice-norma-foral-general-tributaria-cas-8-pdf) |Operative procedure/filing provision cited above |2026-10-27 |
| [B current art. 13.5](https://www.bizkaia.eus/documents/880307/15187815/ca_11_2013.pdf/5a463c1d-a59b-7e48-6429-80fd22f30bc6?t=1768908575887), [A current art. 13.5](https://web.araba.eus/documents/d/araba/norma-foral-del-impuesto-sobre-sociedades_cas-3-pdf), [G current art. 13.5](https://www.gipuzkoa.eus/documents/2456431/8.0761374E7/NF%202-2014%20%282026%29.pdf/f1231a01-1f83-ee15-e569-7b9b84d44d54) | Quantitative-only conditions imported for the 25%-or-greater corporate-shareholder test, separate from the taxpayer's own activity gate | 2026-10-28 |

| Official source | Scope read | Read on |
|---|---|---|
| [Álava NF37/2013 arts.53/59/61/67](https://web.araba.eus/documents/d/araba/norma-foral-del-impuesto-sobre-sociedades_cas-3-pdf), [DF41/2014 art.32bis](https://web.araba.eus/documents/d/araba/indice-reglamento-del-impuesto-sobre-sociedades-cas-5-pdf), [NF3/2025 art.12.Cuatro/DF1](https://www.araba.eus/botha/Boletines/2025/044/2025_044_01182_C.pdf), [NF21/2025 art.3.Quinto](https://www.araba.eus/botha/Boletines/2025/147/2025_147_03861_C.pdf) | Actual selected operative provisions/effect chain; own source-derived amount-threshold investment interpretation, not enacted33bis or a blanket waiver of all credit conditions | 2026-10-28 |
| [Own Álava NF37/2013 articles 15/31/56–57](https://web.araba.eus/documents/d/araba/norma-foral-del-impuesto-sobre-sociedades_cas), [NFGT article 11](https://web.araba.eus/documents/d/araba/indice-norma-foral-general-tributaria-cas-8-pdf), [PGC NRV 13.4 / P&L](https://www.boe.es/buscar/act.php?id=BOE-A-2007-19884), [NF17/2025 DF1](https://web.araba.eus/documents/d/araba/norma-foral-del-imic), [NF21/2025 article 3.Cuarto](https://www.araba.eus/botha/Boletines/2025/147/2025_147_03861_C.pdf), [OF380/2026 model 2025](https://www.araba.eus/botha/Boletines/2026/073/2026_073_01914_C.pdf) | Fresh selected own operative/accounting/amendment reads support the labelled net-result/current-tax attribution worksheet; no special measurement regulation or 2026 software ruling claimed | 2026-10-28 |

**Not yet confirmed:** a controlling Álava special delegated measurement or contrary interpretation beyond the supplied own-law net-result worksheet, and its deferred-tax/current-credit/other-adjustment or incomparable-history populations; attribution or adjustment interactions outside the supplied reasoned ordinary ledgers and return-specific rounding. The supplied B/G fully taxable incremental-profit method and Álava's labelled own-law net-result/current-tax interpretation each give a positive surcharge within their explicit input bounds; neither supplies every other accounting or tax-attribution branch. These ordinary limits are not specialist exclusions; art.13 medium companies remain statutorily excluded. No accountant attestation is claimed.
