# Independent narrow sibling-method delta review

Date: 27 October 2026. Reviewer: the separate independent foral-IRNR reviewer. **PASS for these narrow additions and administrative review-status edits. No new actionable finding.** This is not a new whole-Guide attestation or approval of the unresolved extraordinary-profit charge.

## Frozen files

| File | Reviewed SHA-256 |
|---|---|
| es-foral-corporate-tax.md | `dcbfeb3202511f58c5d5ca416e8e09bf55379d4d8dfc1c413abc1f0cc99c6e5f` |
| es-foral-income-tax.md | `e018cb60cfd56edf69e547e7e254b6b08c5bdd182cbcad3a442a5aa5f8dd6d19` |
| es-foral-non-resident-tax.md | `588be27752c59716b15e5580d58d5a0973f29b4ce958232c89cc2255a7381152` |

Snapshots are in this directory. The resident-PIT and CIT pre-addition `HEAD` snapshots are retained as `*-before.md`.

## Law re-read and findings

The reviewer rehashed and re-read the actual nine official PDF bodies previously fetched independently in this same review session: the three current PIT laws, three current CIT laws and three2026coefficient decrees. `source-receipts.json` preserves complete official URLs, raw-file paths, independent retrieval times and verified hashes. These are the reviewer's own independently retrieved sources, not writer caches. The previously independently checked231coefficient entries are unchanged.

**Corporate disposal correction:** the added method agrees with [Bizkaia NF11/2013 art40.9](https://www.bizkaia.eus/documents/880307/15187815/ca_11_2013.pdf/5a463c1d-a59b-7e48-6429-80fd22f30bc6?t=1768908575887), [Álava NF37/2013 art40.9](https://web.araba.eus/documents/d/araba/norma-foral-del-impuesto-sobre-sociedades_cas-3-pdf) and [Gipuzkoa NF2/2014 art40.9](https://www.gipuzkoa.eus/documents/2456431/8.0761374E7/NF%202-2014%20%282026%29.pdf/f1231a01-1f83-ee15-e569-7b9b84d44d54):

- The asset population is tangible/intangible fixed assets and investment property, including those subsequently held for sale. Ordinary trading inventory is outside that population.
- The selected2026CIT coefficient table applies to tax periods beginning during2026. It is not the PIT table. Cost and improvements use their own years; accumulated **accounted depreciation** uses each corresponding year.
- Indexed net cost is an intermediate calculation. The monetary-depreciation deduction is indexed net minus the asset's **carrying value**, with the statutory last-legal-revaluation/acquisition starting point preserved.
- The positive monetary deduction is limited to positive reconciled disposal income; it cannot create or enlarge a disposal loss. Separate fiscal-depreciation reversals remain in the accounting-to-tax reconciliation. Indexed net must not replace that reconciliation or erase a reversal.
- The numeric illustration recomputes: indexed cost107,100; indexed depreciation6,180; carrying value94,000; indexed net100,920; correction6,920; taxable disposal income49,080. A5,000positive-income case permits only5,000deduction; a loss permits none. Independent control with an additional6,000fiscal-depreciation reversal produces55,080taxable income, preserving the reversal.

The coefficient timing matches [Bizkaia DF115/2025 art2](https://www.bizkaia.eus/lehendakaritza/Bao_bob/2025/12/15/I-1336_cas.pdf?hash=7bb6a27105d5d87568e6537aa6283dc3), [Álava DF41/2025 art2](https://www.araba.eus/botha/Boletines/2025/146/2025_146_03735_C.pdf) and [Gipuzkoa DF27/2025 DA2](https://egoitza.gipuzkoa.eus/gao-bog/castell/bog/2025/12/30/c2508991.pdf). No PIT31December1994exception has been imported into the CIT table.

**Resident PIT gain measurement:** the added paragraph agrees with the three actual PIT44–45texts: acquisition expenses/taxes and improvements, interest exclusion, required/minimum depreciation, separate payment/depreciation years, seller-paid disposal expenses/taxes, market-value floor and44.2component allocation. It correctly routes an ordinary non-business resident disposal into63(c), the savings-disposal sub-basket under66 and the resident76scale. Business-asset gains retain the separate business-income route. This matches [Bizkaia NF13/2013](https://www.bizkaia.eus/documents/880307/15187815/ca_13_2013.pdf/ce52e403-4fca-9ef7-bf85-2505ba29f921?t=1784098584068), [Álava NF33/2013](https://web.araba.eus/documents/d/araba/indice_norma-foral_irpf_cas-4-pdf) and [Gipuzkoa NF3/2014](https://www.gipuzkoa.eus/documents/2456431/8.0759126E7/NF%203-2014%20(2026-0).pdf/8ab5c95c-3f89-8fdf-5cb8-01950e3983cc), read at25/44–45/63/66/76.

The resident measurement can equal the IRNR-measured gain while tax differs: gain144,953 produces resident savings-scale gross quota35,637.545 before cent rounding, offsets and credits, versus the separate IRNR19%result27,541.07. The paragraph routes that distinction correctly. The PIT date exception and33rowtable were already independently checked against art1/DA1of the same three decrees.

## Byte preservation and administrative-only verification

`controls.json` records39passing independent source-hash, arithmetic, branch, anchor, preservation and execution checks, with zero failures.

Removing only the newly added method section and its three decree Sources rows from each resident-PIT/CIT sibling restores the corresponding pre-addition `HEAD` file **byte for byte**. Their existing two `oa-check` blocks are separately compared and remain byte-identical.

The new IRNR Guide differs from the approved73ddf9b snapshot only in two review-status statements: the introduction now states the bounded ordinary-scope pass, and the final unconfirmed line states the same scope and exclusions. Replacing exactly those two statements restores the full prior file byte for byte. Every intervening method, table, source and example byte is unchanged. The unchanged methods/source/examples region has SHA-256 `252a6d38675dcef6239618502d223e3b4dc3e7bcad701b65af12f7e82ad03598`.

Both coefficient link anchors resolve to the exact new Guide headings. The three files were rerun together with the repository example checker: `checked 3 files, 6 oa-check blocks, 0 failures, 0 missing`. Output is retained in `repository-example-check.txt`.

No Guide edits, commits or pushes were made by this reviewer. The prior bounded ordinary-scope review remains valid at the new administrative-only IRNR hash above. Positive provincial extraordinary-profit PE applicability, the resident-CIT positive-surcharge calculation and the other expressly unresolved branches remain outside this pass.
