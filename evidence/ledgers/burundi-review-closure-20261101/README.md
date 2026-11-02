# Burundi independent delta closure, 1 November 2026

**Accepted as source-faithful drafts within the stated partial scope at repair candidate `e42a4f145ce4393878310853027150dfaec193af`.** All five findings from the initial review, and its opening-notice observation, are closed by the inspected repair. This is a bounded independent delta closure, not accountant attestation, country-complete approval, authenticated filing validation, or a claim of currentness beyond the source chain previously verified and the actual repair clauses re-read here.

Pinned base: `8935b6fc3a7ff0f773334a45a67448f1efe37b19`. Original reviewed candidate: `124f6a7a00cbf173ddcd91a4c0ee81e5aa0f25bf`. The initial review's 114-row work carries forward except for the 15 changed existing rows checked again here; the two additional EBMS rows were also checked, giving 116 physical ledger rows. This closure did not repeat the full country review or broaden the residual scope.

## Finding closure

| Finding | Delta checked | Result |
|---|---|---|
| F1: ordinary income-tax EBMS condition | Corporate base now states the issue-time EBMS disallowance for both periods, with dated source links; corporate ledger 7 and new 17–18 checked. Individual base and row 6 explicitly import and state the condition. Actual modified budget art. 243 p. 58 and July art. 268 p. 65 independently re-read as images. | Closed. The income-tax condition is separated from VAT recovery. |
| F2: payroll form routing | Payroll filing paragraph and row 12 checked against the actual monthly form section III p. 4 and IR art. 117 p. 39. Historical lines 9–11 are now correctly identified as early-retirement/complementary-pension rows; political/public office and end-of-mandate treatment is distinguished, with actual current placement held for confirmation. | Closed. No historical pension line is presented as independent current-law authority. |
| F3: separate stock-inventory filing | Corporate filing and row 12, plus the conditional annual-individual route in row 6, checked against actual procedure art. 29 p. 11 and neighboring arts. 28–30. The detailed and valued stock inventory is now separately due within thirty days after accounting year-end rather than deferred to the annual return. | Closed. |
| F4: unsupported VAT monthly convention | VAT penalty row/body and ledger 20 checked against actual art. 59 continuation p. 22. The repair uses the statutory monthly wording and expressly withholds a starting-month/part-month calculation pending an applicable basis. | Closed by removing the unsupported operational convention and keeping the unresolved point explicit. |
| F5: quotations and locators | Changed formation rows 2/6/7/8/9, individual 5, overview 8, TP 8, VAT 1/13/20 checked against the actual relevant source passages. Formation general-articles and ADB headings, VAT art. 9/20 phrases, and the specified physical-page references are corrected. | Closed, with the reviewer correction below. |
| Opening notice observation | All eight opening notices, title versions and metadata inspected. Six legacy versions are 1.2; TP/XB are 1.1; every title matches. The general-reference notice is in writer-owned opening text. | Closed. |

Repair sources: [modified 2025/26 enacted budget](https://www.obr.bi/images/PDF/Loi%20de%20Finances%202025-2026%20Modifi%C3%A9e.pdf), [July 2026/27 enacted budget](https://www.obr.bi/images/LOI_DE_FINANCES_2026-2027_PROMULGUEE_compressed.pdf), [procedure law](https://www.obr.bi/images/LOI_RELATIVE_AUX_PROCEDURES_FISCALES_ET_NON_FISCALES_2020.pdf), [income law](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf), [monthly joint return](https://www.obr.bi/images/DECLARATION_TVA-_IRE-_PF_ET_AUTRES_RETENUES_A_LA_SOURCE-2021-VF-juillet-2022-vf-1.pdf), [VAT law](https://www.obr.bi/images/LOI_N1_10_DU_16_NOVEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_12_DU_29_JUILLET_2013_PORTANT_REVISION_DE_LA_LOI_N1_02_DU_17_FEVRIER_2009_PORTANT_INSTITUTION_DE_LA_TAXE_SUR_LA_VALEUR_AJOUTEE_TVA_.pdf), [company code](https://www.obr.bi/images/stories/download/CODE_DES_SOCIETES_PRIVEES_ET_A_PARTICIPATION_PUBLIQUE_Verrs_Fin1.pdf), [ADB procedure](https://investburundi.bi/procedure-de-la-creation/). Cached actual PDF/HTML and page images were used; no repeated general currentness sweep is claimed.

## Correction to the initial independent review

The initial review incorrectly proposed physical PDF page **12** for procedure art. 32. The correct physical and printed page is **13**. I independently viewed the p. 13 image: it contains arts. 31–32 and the ten-year retention text. Page 12 contains the continuation of art. 30. The repaired overview and TP locators correctly use p. 13, and TP's short quotation now matches the actual words. This corrects my earlier locator error; it does not alter the retention rule. The original review files have been preserved unchanged as historical evidence.

## Preservation and validation

The independent `check-closure.py` run, recorded in `closure-checks.json`, confirms:

- All eight repaired Guide SHA-256 values match the repair freeze. All 15 mechanical shape checks per Guide pass; description text is unchanged and remains 98–107 words, tier stays 2, titles match numeric versions and opening notices are present.
- All sixteen `oa-check` blocks are byte-identical to those independently recomputed in the initial review. The example checker also passes all sixteen again. Their legal case assumptions remain unchanged.
- All six existing platform field sets and complete CTA suffixes are exact. TP/XB contain neither platform-written fields nor copied CTA. No named review or attestation was added.
- The exact 65-topic legacy destination map, four introductory destinations, pack README, original writer checkpoint and all six original review evidence files are unchanged. All seven domain partial declarations remain in force.
- The pinned-base changed-only validator passes with zero warning groups; the strict-metadata sync audit on the exact repaired HEAD checks eight source Guides with zero errors, warnings or notices; the repair diff passes whitespace validation.
- Capture-manifest SHA-256 remains `1441f65ac42f1c00ddeb4807aaa2ee087b4fabbd1ad044c114a85c12119a85d5`. The closure's hash manifest also retains exact original-review evidence hashes.

The originally declared gaps remain: complete quarterly individual due days, July VAT transition/refund execution, annual financing cutover, operative TP implementation, treaty effectiveness/relief, diplomatic scan condition, health/training applicability, current interest, specialised sectors/incentives and authenticated filing screens. The repair does not claim to close them.

## Exact repaired Guide hashes

| Guide | SHA-256 |
|---|---|
| bi-company-formation | `d030c03c6f952fe891f66a3dc14fa6194b489a820d97649dd184ded64b4ba787` |
| bi-corporate-income-tax | `11cf094be1dd0b7245eed225873ac4b97d36a36252cc0d930284e4aff6f2b1f0` |
| bi-cross-border-tax | `c219a5198c226f825cf919795e32d8f9b3fe24f5bcce16bf44d85dc84a417920` |
| bi-income-tax | `2ae41a26836661a435206964e7a09f910eb94555bba38a7adf8dfa19cdaf074b` |
| bi-payroll-social | `13ba76e6e8950477863113c13af4210061a405c24367ea47e72ace38f97ac383` |
| bi-tax-overview | `11f8f4d8a10b12f534e09d3e7a8b7f1d7787c0c879e3fe2175632c6dc21059b4` |
| bi-transfer-pricing | `a0248c77314fc08d69ce49604b6b355340a12fdc8ec529b0692989448bca246a` |
| bi-vat-gst | `34ac483c645876a82b7083b6fe17ba3d3dc78dfe42118caa036ee2306a6f7036` |

Reviewer mutations: only new files under `evidence/ledgers/burundi-review-closure-20261101/`. No Guide, writer ledger, original review, reference, generated inventory or validator was edited. No commit, push or external filing was made.
