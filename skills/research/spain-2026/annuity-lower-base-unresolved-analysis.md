# One bounded lower-Bg primary-source attempt

Read 27 October 2026. This is a follow-up to the scoped independent review, not a new whole-Guide verdict. No Guide edits. The search pass ends here; the issue is not classified as a future-form or external-access blocker.

## Additional exact primary evidence

1. [AEAT 2025 general-progression instructions, phase 2](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/especialidades-determinacion-cuota-integra-estatal-autonomica/rentas-exentas-progresividad/tratamiento-liquidatorio-rentas-exentas-progresividad-big.html) expressly test the minimum against general BL **or, where appropriate, general BL increased by exempt progression income**. Thus the ordinary progression instruction is not confined to a minimum below actual Bg. This is stronger evidence than the combined worked example alone. It supports the enlarged general minimum calculation; it does not explicitly state the simultaneous savings-residual consequence.
2. [Approved 2025 Modelo 100, Orden HAC/277/2026 annex I, printed declaration page 21, PDF page 41](https://www.boe.es/boe/dias/2026/03/27/pdfs/BOE-A-2026-7041.pdf#page=41): state general-minimum field 0521 is min(actual general BL field 0505, total minimum field 0519); savings-minimum field 0522 is min(0519−0521, savings BL 0510). Regional fields 0523/0524 use the independently established regional minimum 0520. Exempt progression incomes are separate fields 0525/0526. The accompanying special-income note says the tax-output fields must take those exempt amounts into account; it does not supply the low-base combined allocation algorithm.
3. Current [art. 56.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a56) allocates the minimum to general BL up to that base and the remainder to savings. [Arts. 64/75](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a64) add the 1,980 tax-calculation increment to the general-base minimum. [DA20](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#davigesima) enlarges the relevant base for calculating the average rate, then applies the rate to taxable base alone. None of these provisions expressly spells out the simultaneous low-Bg savings-remainder reconciliation.

Both additional official sources returned HTTP 200; raw files, extracted text and dated/hash receipts are in this folder. The current-law and combined-example receipts are in the parent evidence folder.

## Exact remaining question

For each half, when actual Bg is below total personal/family minimum M but enlarged Tg exceeds it, does the general rate-setting use of M also extinguish the art. 56 savings remainder, or do the actual-base allocation fields continue to supply that remainder to savings while the special general-rate computation uses M against Tg? A second related issue is whether the 1,980 increment is capped by actual Bg or by Tg when it crosses actual Bg. The special increment itself is never a new minimum carried into savings.

Do not collapse those questions into “annuity/progression worksheet unavailable”. The main sequence is published and verified. Do not say the official model lacks minimum-allocation fields: those fields exist and their ordinary formula is explicit. The unresolved point is their reconciliation with the simultaneous enlarged general-base tax calculation at this boundary.

## Diagnostic controls, not approved filing results

Use one State/city half: Bg 3,000; Eg 10,000; Tg 13,000; qualifying C 1,800; M 5,550; savings BL 5,000; no exempt savings income. C<Bg is satisfied.

General split tax before minimum: S(1,800)+S(11,200)=171+1,064=1,235.

| Candidate allocation | General minimum tax base | Enlarged split quota | Ordinary minimum remaining for savings | Savings half quota |
|---|---:|---:|---:|---:|
| Enlarged general minimum, retain actual-base remainder | 7,530 | 519.65 | 2,550 | 232.75 |
| Enlarged general minimum, allocate all M to enlarged general base | 7,530 | 519.65 | 0 | 475.00 |
| Allocate ordinary M by actual Bg before the general-only 1,980 increment | 4,980 | 761.90 | 2,550 | 232.75 |

For the first two candidates, the exact unrounded actual general quota is `519.65 × 3,000 / 13,000`; for the third it is `761.90 × 3,000 / 13,000`. These are diagnostic rational amounts before any independently determined display convention. No candidate is represented as an approved tax-engine result. The first two differ solely in savings minimum allocation by 242.25 per half. This control isolates a material consequence instead of hiding the issue with a fact pattern whose Bg absorbs all M.

A second useful boundary is Bg 7,000; Eg 6,000; M 5,550; C 1,800. Ordinary M is wholly in actual general BL, but augmented M is 7,530. This isolates whether the annuity-only increment crosses into the enlarged rate base; it does not involve an ordinary savings-minimum remainder.

The Guide's corrected full-minimum branch avoids both contested boundaries. A future matching primary worked example, explicit administrative algorithm, or verified official-engine diagnostic can settle the edge; the present sources do not justify claiming that the current full-minimum example has already done so. This bounded pass is complete and should not be repeated with the same general queries.
