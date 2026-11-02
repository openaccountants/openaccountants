# Catalan July 2026 credits: bounded independent review

Read date: **27 October 2026**. Scope: only the three newly integrated rows for arts. 612-13/14/15, the section `Cataluña: July2026 additions and conditional commencement`, and its Sources. The Valenciana methods received a separate **integration check against this reviewer's earlier proposal**, not a new independent legal review of the reviewer's own work. No Guide source was edited.

**Pre-correction verdict: one ordinary-method finding in 612-13. The forest method and conditional coeliac presentation pass.** Exact corrective prose and a dated Sources row were delivered in `july-independent/612-13-correction.md`, and the frozen spans were released to the parent for that correction.

## Frozen identity

Checkout HEAD at capture: `9d78e939e1648eafd1758fbd77884ccb200f505e`.

Guide SHA-256: `cc35ce2263c593a256ab65d2d2880153d7a095cbdcbbd501b0339112bb3d5cee`.

Git blob: `81e9c6569e8dd497a6165711feae5f1b7c37a9d1`.

Exact saved spans and one-based positions:

| Span | Lines at capture | SHA-256 |
|---|---:|---|
| Three new table rows | 141–143 | `6d2c26f6f4157cdf38084c53cfec4896c9fc0177b7a6fbd1d7fdf0ac5e4a7b12` |
| July section | 155–163 | `28216701a14434b17bd9bba6b03d639da1394ace5c3687e774f387c2aa004e77` |
| Valenciana integrated methods | 1046–1050 | `feaaafd34d21ca0647d8a4ecc0a7ef6e475ffff4fe3d7ea54603385aa3b25995` |

The two relevant Source rows and their exact combined hash are in `july-independent/reviewed-hashes.json`. `reviewed-pre-correction-guide.md` and individual span files retain the precise bytes reviewed.

## Primary-source checks

Independently re-fetched six official sources; all returned HTTP 200. Raw responses, extracted text, UTC fetch timestamps and SHA-256 receipts are under `july-independent/sources/` and `source-receipts.json`.

- [Ley 11/2026 original enactment](https://www.boe.es/ccaa/dogc/2026/9706/f00001-00146.pdf): read actual art. 37.1–3 on PDF page 42, DF1 on page 144, and DF8 on page 145.
- [Official publication/analysis](https://www.boe.es/buscar/doc.php?id=DOGC-f-2026-90190): DOGC 9706, publication 13 July 2026, general entry 14 July 2026.
- [2 October corrigendum](https://www.boe.es/buscar/doc.php?id=DOGC-f-2026-90237): read its full correction text. It alters arts. 21/39/87/91/100/128/144, DA3, derogation clauses and DF5; it does not alter this art. 37 or DF8. A reference to art. 37 of a different decree in the corrected derogation clause is not a correction to this law's tax-credit art. 37.
- [27 October corrigendum](https://www.boe.es/buscar/doc.php?id=DOGC-f-2026-90249): the full correction concerns art. 25 and the heading of the amended public-security training fee provision. No change to the reviewed credits or DF8.
- [Current LIRPF](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764): read arts. 63.1–2 and 74.1–2 for separate state/regional general average-rate definitions and the minimum-tax subtraction.
- [AEAT INFORMA 147637 official summary](https://sede.agenciatributaria.gob.es/Sede/irpf/novedades-impuesto/novedades-publicadas-informa-2024/novedades-publicadas-informa-mes-septiembre.html): RD 574/2023 aid is non-exempt employment income, without the 30% irregular-income reduction. This source is a 2024 published interpretation, read on the present review date; it is not relabelled as a new 2026 enactment.

The PDF page anchors used in the Guide are correct: `#page=42` for art. 37 and `#page=145` for DF8. Its existing Sources row is dated 2026-10-27 and links actual official URLs.

## Finding J1: complete the ordinary thalidomide calculation

The current text restates that applicable average rates are applied but does not identify them or calculate them. That is an ordinary missing method, distinct from the expressly retained mixed-income/base-reduction attribution question. It also omits the aid's employment-income classification, creating a risk of treating it as a general-base capital gain or adding gross aid directly to BL.

Use the supplied replacement. Its steps are:

1. Classify RD 574/2023 aid as non-exempt employment income with no 30% irregular-income reduction; apply the normal employment-income computation.
2. Establish the aid amount actually included in general BL (`A`). Retain the specific reservation when several income sources and base reductions make that attribution unresolved.
3. For positive general BL (`B`), calculate each general average rate separately under LIRPF 63.2 and 74.2: `100 × relevant general quota after the applicable minimum-tax calculation / B`, expressed to the statutory two decimals.
4. Read art. 612-13's plural average rates together with those definitions: apply both general rates to `A`, giving `A × (rE + rC) / 100`, then the Guide's regional-quota settlement limits. This is a legal construction from the primary provisions, not a claim that Cataluña has published a worked example for this new credit. Do not substitute the marginal rate, savings rate, a combined-general-and-savings average, or only the regional general rate.

The correction deliberately **does not prescribe ROUND_HALF_UP or certify a truncation rule**. “Expressed with two decimals” alone does not establish an algorithm. Its numerical example uses already established exact 12.50% and 15.00% inputs: 10,000 included aid gives 2,750. Separate display/truncation implementation requires supporting authority if it becomes material.

The current 2023-onward scope and rectification requirement for 2023–2025 are exact statutory rules and pass. The credit reduces regional gross quota, as the Guide says; it is not an exemption or an unconditional refundable payment. The 1950–1985 range identifies the affected cohort, not the years when qualifying aid must be received.

## Forest method: pass

The enacted method is `min(15% × eligible investment, 5% × regional gross quota)`. The Guide's 10,000 investment and 20,000 regional-quota control gives `min(1,500, 1,000) = 1,000`. The two percentages are not two alternative investment rates.

The statute requires a current approved forest-management instrument, adequate documentary support and a certificate requested from Centro de la Propiedad Forestal during the first 20 days of the year for transmission to the tax authority. The Guide correctly describes the 20 days as a **certificate-request** period, not an invented investment deadline or tax-return filing deadline. It does not invent a carry period, add a cap per hectare, or imply that all forestry expenses qualify. General commencement is 14 July; no separate 1 January retroactivity is stated for this forest article. The Guide preserves the actual expenditure/certificate implementation question without selecting unsupported dates.

## Coeliac route and commencement: pass

The new nominal amount is 250 per qualifying person. The special family definition expressly includes the taxpayer, spouse and State-minimum-entitled ascendants/descendants; equal sharing is per person. Two entitled taxpayers share one person's 250 as 125 each. A practising doctor's definitive diagnosis certificate must contain the statutory identification, registration/speciality and issue/diagnosis dates. These claims match art. 612-15.

DF8.2 overrides the general entry rule for this article. DF1 directs the Government to approve the specified alternative aid system before 31 December 2026; DF8.2 permits the tax provision's commencement only if that system has not been approved by the statutory 31 December checkpoint. The Guide correctly labels the route **conditional**, refuses an unconditional 2026 credit at the 27 October read date and requires its actual operative period to be established. It does not assert automatic 14 July commencement, retroactive operation from 1 January, or a guaranteed 2027 claim. No further correction is required.

A bounded official-domain search for a specific food-cost aid-system approval on 27 October found no responsive approval. This is not evidence that no such instrument exists and is not used to certify that the condition has been satisfied. The future condition and any resulting operative period remain precisely identified.

## Valenciana integration check: faithful

Compared the integrated text to `rioja-valencia.md` and the exact proposed replacements. It preserves the third-birthday month through the month before the fifth birthday, separate contribution-date interval, March controls, F phase and contribution ceiling. It also preserves cap addition, one application of 50%, sole-employer full cap, limited equal sharing between entitled employers, and unchanged joint cap. The table and dated Sources row reflect the same methods. The two obsolete Valenciana reservations were removed; Rioja's separate age interpretation remains. This is an integration check, not a new independent review of those legal conclusions.

`july-independent/controls.json` records **29 passed controls and zero failures**, including forest cap boundaries, coeliac sharing, commencement arithmetic, exact-rate aid controls, source/structure checks and Valenciana integration assertions. No whole-Guide or whole-Spain completion verdict is made.

## Applied-correction delta: PASS

The parent applied J1. I checked the exact replacement paragraph against the delivered correction, the table method, and the new dated Sources row; the accepted forest/coeliac paragraphs and Valenciana methods are byte-for-byte preserved. Six narrow delta assertions passed. **J1 is closed; zero remaining actionable findings in the reviewed July spans.** The explicitly retained mixed-income/base-reduction attribution and coeliac commencement outcome remain scoped reservations, not newly certified calculations.

Final reviewed Guide SHA-256: `bd1c09cc1652730fef6a1b8bf75a86872849f4ac3831d68f4d61f622ad8456df`; Git blob: `955c9f48762a220275e9da74da236e480730e102`. Exact final July span hashes are in `july-independent/final-hashes.json`; saved final snapshot and delta are alongside it. The July span freeze is released.
