# Cantabria ordinary married joint rent-burden: independent finite review

**Result: PASS within the stated ordinary positive-income and married-entitlement scope. No required correction found.**

Reviewed on 27 October 2026 by a fresh agent that did not write the change. The reviewed Guide is `skills/international/spain/es-irpf-deductions.md` in `codex/spain-full-pack-2026`, baseline commit `96d45505ced79937b06ffc59c081aba776ff5eea`. Baseline SHA-256: `89f5cbe7587a1b7254162a8018db9f51cee92db6881e82fd915271d0fe00cc7f`. Frozen working SHA-256: `8f0a2db6bf2fabde6391761b8b98738f54980dee2486b27bb59267a7616036dc`.

This is a review of the finite Cantabria joint-method delta. It is neither an independent whole-country review nor professional attestation. No Guide edits, commits, pushes, authenticated return activity, filing or payment were performed. The root agent's tab 7 was not accessed or modified. No additional simulator trial was needed.

## Law and authority read independently

| Source | What it establishes | Read |
|---|---|---|
| [Current Cantabria DL 62/2008, art. 2.1](https://www.boe.es/buscar/act.php?id=BOCT-c-2008-90028#a2) | 10% rate; EUR 300 individual and EUR 600 joint ceilings; strict taxpayer rent-to-income comparison; at least one declarant meets the personal requirements; permitted documented bank payment | 2026-10-27 |
| [AEAT exact 2025 return instructions, 10.6.2](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-ayuda-presentacion/irpf-2025/10-cumplimentacion-irpf-deducciones-autonomicas/10_6-cantabria/10_6_2-arrendamiento-vivienda-habitual.html) | Personal eligibility and joint ceiling; named tenant inputs; a non-tenant spouse's payments excluded; sole named spouse can claim only 50% when community funds pay the rent | 2026-10-27 |
| [AEAT 2025 practical manual](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025-deducciones-autonomicas/comunidad-autonoma-cantabria/arrendamiento-vivienda-habitual-jovenes-mayores-discapacidad.html) | Confirms tenancy, joint qualification and the same-home incompatibility with the rural rental deduction | 2026-10-27 |
| [Ley 5/2026, art. 2.One](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-10431) | Alters art. 2.1(a)'s age alternative; leaves the income-comparison and joint paragraphs unchanged | 2026-10-27 |

An attempted BOE historical consolidation URL with `p=20251231` was unavailable through the web tool. The current law, operative 2026 amending provision, and AEAT's published 2025 wording supplied the necessary year comparison. No unavailable historical text was treated as read.

## Actual raw states checked

I read the raw profile, each spouse's interest state, household base summary, every valid rent input, and each individual/joint result. I also read the failed dot-decimal input/result and visually inspected both result screenshots. The observations manifest was cross-checked, not used as the sole evidence.

The profile shows married fictional spouses, both born 1 January 1990, both Cantabria, with disability blank. Both interest screens show EUR 30,000 taxable bank interest. The household summary shows joint savings BI EUR 60,000 and savings BL EUR 56,600, with EUR 30,000 individual bases. These were 2025 simulator inputs and 2025 age 35 facts.

| Attributed eligible rent: P / S | Actual individual result | Actual joint result | Meaning |
|---|---|---|---|
| 4,000 / 0 | P: 300 | 400; base 4,000 | Joint result exceeds the separate individual cap although joint BI/BL comparisons would fail |
| 3,000 / 0 | P: blank | Blank | Exact equality with 10% of personal R fails |
| 3,000.01 / 0 | P: 300 | 300; base 3,000.01 | A cent above the personal threshold qualifies, despite remaining below 10% of joint BI/BL |
| 3,000.01 / 3,000 | S: blank | 600; base 6,000.01 | Once P qualifies, S's eligible attributed payment enters the combined joint base even though S fails the personal burden test |

The valid cent input is visibly `3.000,01`; its accepted result retains that amount. The earlier dot-decimal attempt visibly retained `3000,00` and produced blank output. It is correctly excluded from the four valid observations. Blank means no generated credit in those UI fields, not a positive numeric observation of zero.

The evidence supports the specified personal qualification followed by the combined eligible contract-holder payment base and joint ceiling. It contradicts an aggregate joint BI/BL qualification and a sum of separately EUR 300-capped individual credits. The fourth configuration distinguishes inclusion of the other named tenant's eligible payment after one declarant qualifies.

## Scope and preservation

The new prose expressly labels the method a controlled inference from the 2025 implementation for the unchanged 2026 income-comparison wording. It does not claim a 2026 campaign observation or an express statutory BI definition. Its empirical joint controls use bank interest; positive employment and the individual BI method were previously committed and independently reviewed, and are not presented as newly simulated here. The limited inference is acceptable when read with that existing branch and the statutory personal qualification structure.

The method retains tenancy/payment attribution, including the sole-tenant community-funds 50% rule. It does not turn an unnamed spouse's payment into eligible rent. Other family/entitlement combinations and exempt-income/loss/offset cases remain expressly reserved. The unchanged surrounding paragraph preserves age/disability conditions and the same-home rural-rent incompatibility. The new age alternative in current 2026 law is not falsely presented as exercised in the 2025 trials.

The only paragraph differences from the exact baseline are: the existing limitation refinement plus the two new joint paragraphs, and the Cantabria refinement in the Not yet confirmed paragraph. Every other paragraph is byte-identical, including unrelated Cantabrian and other regional methods, all source-table rows, metadata, the previously reviewed individual method, both examples and the platform CTA. Controls retain SHA-256s and equal-paragraph spans. There are nine authored H2 sections in the prescribed order plus the unchanged platform CTA H2, ten H2 headings in the complete file. There are exactly two `oa-check` blocks. No content was lost.

## Arithmetic and validation

I recomputed the four new configurations with decimal arithmetic: personal threshold EUR 3,000; nominal joint results EUR 400, none at equality, EUR 300.001 rounded to EUR 300.00, and EUR 600.001 capped at EUR 600. The prior individual illustrations also reconcile: 30,000 minus 3,000 minus 2,000 equals R 25,000; 2,500 equality fails, 2,500.01 gives 250.00; adding 10,000 interest produces R 35,000, with 3,500 equality failing and 3,500.01 reaching the EUR 300 cap.

`python3 scripts/check-examples.py skills/international/spain/es-irpf-deductions.md` checked one file and two blocks, with zero failures and zero missing blocks. The unchanged Canarias example returns acquisition 180, medical 480, total regional credit 660, regional liquid 540 and final differential -850. The unchanged Asturias example uses 2,000, 700, 1,000 and 1,000, with 300 expiring and total use 4,700.

Targeted `validate-guides.py` `check_guides` validation of this Guide returned zero errors and zero warnings using the existing `/private/tmp/claude-502/fi/venv/bin/python`. Initial attempts with system and bundled Python lacked the `yaml` module; the existing environment resolved that dependency without installation. Full-repository validation and coverage reports were not run for this finite review.

Artifacts: `manifest.json`, `controls.json`, `raw-state-controls.txt`, and `example-check.txt`. The manifest hashes all supplied raw evidence, including excluded failed-input files. The frozen Guide hash was verified before and after the controls.
