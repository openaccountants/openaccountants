# Croatia: finite correction review record

This record concerns the three Croatia Guides corrected after the first complete independent review of merged PR #2155 returned FIX. It is an AI source-review record, not professional accountant approval. The Guides remain tier 2.

The first review independently checked all 117 writer groups, all 230 original nonblank-line destinations and all 5 cases at source 655d627b44c7b60a3701c6f4be21cad941d2a883. It recorded 93 groups PASS and 24 changed groups requiring 15 bounded findings. Its exact manifest SHA-256 is 279355f114c5ac386b202319bbb8ae4cde3d18962fc357a8ce2bd0aa8c87aac0; report SHA-256 718a1dd3b1d09eefb4f3472ea5c4e84ba389ecb4654eb0b23b1628c36dcfc593. No earlier pending-review label was credited as PASS.

## Corrected source binding

Source correction commit: `bacb63c60ca8816767658415ce1a9fb16d95efbb`. Its parent is main `da3ae36ab6c44339ac18cb1f38101f978a163459`. Integration merge `81dcda014a1ff51b242c327b2bc309b8d2b7f21d` brings in fresh main `87697cff4635ce4bb03924d586c8dd74b93c5a31`; all three reviewed Guide hashes remain identical. This record is added without changing those bytes.

| Guide | Corrected SHA-256 |
|---|---|
| `skills/croatia/hr-tax-overview.md` | `f460ab7f03f53e33dcc5128b53c07d5a8dc4473fab6b51db6aafe0f8ef0874a6` |
| `skills/croatia/hr-company-formation.md` | `85ad1a1a55bb37134ad05dc5bc108675124ad6c3560d492894ec7c28f04bd7d4` |
| `skills/croatia/croatia-tax-optimization.md` | `57558795852ff562af715f175cd0a860be3f4f91b72463be48b2dfb0859e8fe3` |

## Finite changed claims

| Findings | Correction and operative authority |
|---|---|
| F01/F09 | Dependant counted receipts after ZPD 17(2) exclusions; local-decision November adoption distinct from NN publication. [Income Tax Act](https://porezna-uprava.gov.hr/Propisi/Propis/zakon-o-porezu-na-dohodak-redakcijski-procisceni-tekst/3), arts. 17, 19.a. |
| F02/F03 | Domestic/Union preceding/current-year SME tests, statutory supply turnover and asset-disposal exclusions, home-state notification/EX commencement; separate paušal receipt transition including December exception. [VAT Act](https://porezna-uprava.gov.hr/Propisi/Propis/zakon-o-porezu-na-dodanu-vrijednost/1651), arts. 89.a, 90, 90.f; Income Tax Act art. 82; Paušal Ordinance art. 4. |
| F04/F05/F06 | Actual professional and director insurance basis, art. 66(2) occupational exceptions, art. 30(2) journalist/artist/athlete election, annual-difference route for directors insured elsewhere, and statutory-month second-activity cap. [Contributions Act](https://porezna-uprava.gov.hr/Propisi/Propis/zakon-o-doprinosima-redakcijski-procisceni-tekst/3119), arts. 66, 90-92, 185-186, 187.c-g; [2026 Bases Order](https://porezna-uprava.gov.hr/Propisi/Propis/naredba-o-iznosima-osnovica-za-obracun-doprinosa-za-obvezna-osiguranja-za-2026-godinu/5778), arts. 6, 7, 12. |
| F07/F08/F15 | Nine-month employment/domicile/actual-residence company-relief gate; 36% confined to art. 66 capital-income withdrawals/hidden distributions; employee pension consent and registered domestic-fund conditions. [Profit Tax Act](https://porezna-uprava.gov.hr/Propisi/Propis/zakon-o-porezu-na-dobit-redakcijski-procisceni-tekst/1641), art. 28.a; Income Tax Act arts. 9(1)18, 32(11), 64-66, 70(2). |
| F10/F11 | Formal j.d.o.o. capital increase switches off only 390.a(3)-(6); sole-founder unpaid capital requires appropriate security and document before application. [NN 111/12](https://narodne-novine.nn.hr/clanci/sluzbeni/2012_10_111_2392.html),390.a(7); [baseline NN 152/11](https://narodne-novine.nn.hr/clanci/sluzbeni/2011_12_152_3144.html),394(2),(5)4; [NN 130/23 art. 50](https://narodne-novine.nn.hr/clanci/sluzbeni/2023_11_130_1794.html). |
| F12 | Substantive founder/member/director eligibility before proceeding, related-company debt/unpaid-wage/insolvency gates, narrow public-debt-below-EUR 30 exception and remote physical-check fallback. [NN 18/23](https://narodne-novine.nn.hr/clanci/sluzbeni/2023_02_18_305.html), [NN 130/23](https://narodne-novine.nn.hr/clanci/sluzbeni/2023_11_130_1794.html), [NN 136/24 art. 2](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_11_136_2248.html), Court Register [NN 34/22](https://narodne-novine.nn.hr/clanci/sluzbeni/2022_03_34_397.html) and [NN 123/23](https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_123_1697.html). The Companies Act fallback is 397.e(8). |
| F13/F14 | Combined FINA filing requires calendar business year and simultaneous additional statistical data; partial-year paušal needs annualised band and prorated deemed income with statutory months. [Accounting Act art. 50(2)](https://porezna-uprava.gov.hr/Propisi/Propis/zakon-o-racunovodstvu-redakcijski-procisceni-tekst/3223), [Paušal Ordinance art. 3(4)-(6)](https://porezna-uprava.gov.hr/Propisi/Propis/pravilnik-o-pausalnom-oporezivanju-samostalnih-djelatnosti-redakcijski-procisceni-tekst/5). |

The writer read the changed operative provisions and direct neighbors against retained native official text on 17 November 2026. The initial review's 93 unchanged groups and applicability evidence are reused. Proposals are not enacted authority. No full-pack legal rescan was repeated for a wrapper/hash change.

## Preservation and limits

All five original oa-check blocks are byte-identical. The original EUR 40,000 receipts/EUR 10,000 cost case and all displayed results remain; its full 12-month assumption is now explicit. The EUR 500/EUR 625/EUR 2,500/EUR 12,000 formation case remains, with the missing security/eligibility condition placed beside it. Exact-diff bridges preserve all 230 original destinations. Version advances 0.3 to 0.4; the current date remains 17 November 2026. Identity, licence, human names, tier, approval fields, CTA and calculator quotes are preserved; no professional approval is added.

Existing non-usable limits remain: unverified chosen 2026 municipal rates, home-office apportionment method, notary/bank/interpreter practice and FINA disclosure fee. Formation source scope now includes the Ministry's chain through NN 136/24 and the actual operative dependencies, without claiming a complete later-journal certification.

## Independent delta closure

**PASS for all 15 findings at exact source commit `bacb63c60ca8816767658415ce1a9fb16d95efbb`.** The same separate reviewer checked all changed claims and direct dependencies, closing all 24 affected groups while retaining the 93 unchanged PASS groups. Receipt SHA-256 `a890690e74cc1d20236885060986574598fdeca63c8daee3773aa82958d747cb`; Markdown receipt SHA-256 `d15b51f6c7d786407612150c0bd8fd5f5f5abd436ae2eedd6616f6cf17c6c1d4`. Additional dependencies read included VAT 89.b/90.h/90.i, the 2026 average wage, formal-capital-effect provisions 454(2), 457(1), 458/460 and director occupational-ban/eligibility amendments. Five prior Decimal case checks remain applicable because their blocks are byte-identical. This completes the full 117-group review plus finite closure; it is not a new whole-pack scan or accountant approval.

## Validation

Committed local standards: all 3 empty issue sets. Changed-only validation: 3 Guides, 0 warning groups. Calculator quotes retained. Five examples: 0 failures/missing. Strict sync: 0 errors/warnings/notices. Linked-row check: 42 rows, zero MISS and zero UNREADABLE. Hosted checks are pending. Sparse-checkout initially lacked docs/domains.yml; it was materialized before the clean standards result, without test/source changes.

Written by Codex. Not reviewed by an accountant.
