# San Marino independent full-pack source review

Date: 24 October 2026. Reviewer: fresh agent `/root/san_marino_pack_review`, independently assigned after Michael explicitly authorised one full-pack review and one country push. This is an advisory source review, not a named San Marino accountant's attestation or permission to file.

## Original review target and outcome

Exact checkpoint reviewed: `fc1a9b19591ebb8f163c4a1e8378694abb7c9c29`, all eight source Guides and the country README. The approval question named earlier `4d6678ca7cc9a0655f28ad9c2bf9d9371f0a193d`; the writer disclosed the later payroll/social 0.2 and README 0.4 contribution-procedure changes. I included those changes and all 28 controls. I read OWNERS.md and docs/skill-template.md before assessing the pack. No repository file, source Guide, commit or remote branch was edited by this reviewer.

**Original outcome: fix one P2 finding before country publication.** All 28 arithmetic scenarios independently recompute, with all stated expected outputs matching within 0.01. One exact-boundary legal assertion about permanent domestic electronic invoicing exceeds its cited text. Two additional clarity/routing observations and publication-status updates are set out below. No other blocking finding was identified within the selected source-method scope reviewed. This outcome does not establish comprehensive legal coverage or professional sign-off.

## Findings and observations at the original checkpoint

### F1 [P2] Separate the annual electronic-invoice boundary from indefinite continuation

File: `skills/international/san-marino/sm-vat-gst.md`, “Domestic invoices: dated transition”, paragraph beginning “Article 2 excludes operators”. The text states that reaching/exceeding 100,000 or opting brings continuing electronic use under article 2(3).

Authentic DD 133/2026 article 2(2) excludes revenues strictly below 100,000; exactly 100,000 therefore falls outside that annual exclusion. Article 2(3), however, uses “hanno superato l’importo” or an option as the continuing-use trigger. Treating equality as a permanently binding trigger silently resolves a distinct statutory boundary. A covered operator at exactly 100,000 in one year and below the threshold later is the affected case. State the current-year boundary separately, preserve the exceeded-threshold/option wording for continuation, and leave exact-equality persistence for official interpretation unless a primary instruction actually settles it. Source: [DD 133/2026, article 2](https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=4d7f1ffcf645b166ffc567d328d888e43fcdd538). The authentic four-page PDF was reopened independently and matched the retained SHA256.

Status: sent promptly to the writer. Writer reports a working-tree correction; **not closed by this original report**. Closure requires the exact corrected checkpoint and blob manifest.

### O1 [P3] State both limbs of the payroll remittance clock

File: `sm-payroll-social.md`, “Reporting and payment calendar”. The following-bimonth wording leaves its starting event unstated. IGR 125(1) expressly refers to the bimonth in which withholding was made **or monthly employment income accrued**. Add both statutory limbs so that a user does not infer that delayed cash payment always delays the payroll remittance clock. This is a clarification of a passage already cited; it does not complete the independently acknowledged ISS employee contribution calendar. Source: [official coordinated IGR archive, article 125(1)](https://www.consigliograndeegenerale.sm/on-line/documento17086436.html), no-notes edition dated 22 December 2025.

### O2 [P3] Route personal foreign relief to the prepared personal Guide

File: `sm-cross-border.md`, final paragraph of “Corporate foreign credit” and “Ask and refer”. It still says individual foreign relief remains to be reconciled and refers all personal-credit cases, although `sm-income-tax.md` now supplies a selected article 18 method. Link to that explicitly partial method while retaining its specialist, ordering, payment-year and filing limitations. This is cross-file routing consistency, not a claim that personal foreign-credit coverage is complete.

### Publication conditions, not additional tax findings

Before the one country push, replace stale prospective independent-review/unpublished wording with the dated advisory review record and accurate publication-stage wording; retain tier 2, pending professional review and every partial flag. README currently retains the older primary-Montenegro handover; the writer has independently fetched the newer published OWNERS handover (primary Armenia, Montenegro queued) and should reconcile country workflow prose. Status corrections must not become accountant attestation, comprehensive coverage, live portal or CI claims. Preserve all platform-owned fields and update substantive content versions/H1s and source hashes. Source/body changes outside the described corrections require review of their actual delta.

## Exact original country blob manifest

| Country file | Git blob at reviewed checkpoint | Version | Controls | SHA256 |
|---|---|---:|---:|---|
| README.md | `03d54169a4e9f1a33253a6222018b445ffa70882` | 0.4 | 0 | `2e442be9d0f833845bcecaa624980407caddcc2c2a5ea754d1c745340e8649d9` |
| sm-company-formation.md | `8643a27c461af18d28ce425388579b479f66fb1f` | 0.1 | 2 | `c4ef4205443419aa574c20f25651e4f65fbe183f9eb9a5226bb0718a045c9b09` |
| sm-corporate-income-tax.md | `fed7b0e9fc4ceb26a5ddd10f19d30c818cfcfddc` | 0.2 | 4 | `017b0ff00ab175e84e5aebd3960607a826fb3e02346e72674b7a5ab8d43b29a7` |
| sm-cross-border.md | `436a3e036cbf974ea4c9f0bcc4a581d206f878af` | 0.2 | 4 | `3db0b8f020c4939198fdc734784f796185fbb973cadf2bf99b6fc06f58808e36` |
| sm-income-tax.md | `f0c0c1feed7d8e9f0b0af0fefe00045e0e40cd07` | 0.1 | 6 | `81752dc4439d12f3415a949cd2b421aea8590d17ef1ec5b293584aca0d012a17` |
| sm-payroll-social.md | `087d9b47599e144a5c610709b29519fa5d501d6e` | 0.2 | 6 | `6c67424215f3d14d01f068b600ba067adc2da5dca4e144c5cfaed2ea34677117` |
| sm-tax-overview.md | `e9fd5cad4c432508ab20b94e38d2937f88f8bf70` | 0.3 | 0 | `0419796d37380242282e5537177c8c77e157d50e8182c48f841ef9f179887e9a` |
| sm-transfer-pricing.md | `c68cd6a35ae44d6dcb4716f9fc1a9f69ba7b6c43` | 0.2 | 3 | `4b52ec39c117c91d8b44c658e2d1173d9c79d06f01a7b17ebdcb696ce3e2e95b` |
| sm-vat-gst.md | `d94392cd5681d983a72ab8ee72635990d9ceabb1` | 0.1 | 3 | `655f762216062181b84933763dfd09890222ee0e134c5313cd6a6e5b37275958` |

The six inherited Guide paths retain their published-base `review_status`, `trust_label` and exact licence text unchanged from `532a156840646fa059f2cb96d6a75f3900cddcff`. New TP/XB Guides add no platform-owned attribution/review/licence fields. All eight Guides are SM, tax year 2026, tier 2; all seven README domains are explicitly partial. README is supplementary, not an additional computational tax Guide. All country links resolve to the intended source files, and the overview is a router with no independent liability formula.

## Independent arithmetic evidence

I used a separate Decimal calculation script with scenario-specific formulas. It does not evaluate the Guide `steps` strings or import the repository example checker. Every expected output key was compared with the independently derived value; all 28 scenarios match. These results test the stated assumptions, not taxpayer entitlement. The separate source exercise below corroborates the principal wage/SMaC example.

| Guide | Scenario | Independently derived outputs |
|---|---:|---|
| sm-company-formation.md | 1 | first_owner_subscription=15300.0; second_owner_subscription=10200.0; first_owner_initial=7650.0; second_owner_initial=5100.0; initial_total=12750; remaining_total=12750 |
| sm-company-formation.md | 2 | required_full_contribution=9000; amount_missing_if_only_half_contributed=4500 |
| sm-corporate-income-tax.md | 1 | pre_loss_taxable_income=102000; annual_loss_ceiling=71400.0; losses_used=71400.0; taxable_income_after_losses=30600.0; ordinary_igr=5508.000; losses_remaining=18600.0 |
| sm-corporate-income-tax.md | 2 | ordinary_igr=36000.00; conditional_effective_rate=0.09; conditional_igr=18000.00 |
| sm-corporate-income-tax.md | 3 | advance_basis=18000; first_advance=6300.00; second_advance=9900.00; paid_advances=16200.00; final_balance=6800.00 |
| sm-corporate-income-tax.md | 4 | isolated_current_deduction=10000 |
| sm-cross-border.md | 1 | withheld_igr=1300.00; recipient_cash=8700.00 |
| sm-cross-border.md | 2 | withheld_igr=1200.0; recipient_cash=10800.0 |
| sm-cross-border.md | 3 | self_assessed_igr=1800.00 |
| sm-cross-border.md | 4 | allocated_foreign_income=20000; domestic_credit_ceiling=3600; foreign_tax_credit=3600; foreign_tax_uncredited_in_example=1400 |
| sm-income-tax.md | 1 | wage_forfait=2100; deductible_contributions=2970.000; taxable_wage=24930.000; tariff_tax=3118.10000; maximum_credit=1444.62; required_eligible_spend=5455.14; stated_credit_percentage=26.48; annual_igr_after_full_credit=1673.48000 |
| sm-income-tax.md | 2 | tariff_tax=720.00; usable_credit=720.00; net_igr=0 |
| sm-income-tax.md | 3 | tariff_tax_before_credits=19340.00 |
| sm-income-tax.md | 4 | separate_igr=3600.00; eligible_credit=900.00; net_separate_igr=2700.00 |
| sm-income-tax.md | 5 | state_credit_limit=2500; allowed_foreign_credit=2500; uncredited_foreign_tax=500 |
| sm-income-tax.md | 6 | whole_child_credit=500; credit_for_each_parent=250 |
| sm-payroll-social.md | 1 | employee_iss=234.000; employee_fondiss=75.000; employee_stated_cash_components=309.000; employer_pension=528.000; employer_fondiss=75.000; employer_two_component_subtotal=603.000 |
| sm-payroll-social.md | 2 | capped_forfait=2800; deductible_contributions=4950.000; taxable_wage=42250.000 |
| sm-payroll-social.md | 3 | rounded_allocation=128.73; total_rounded_allocations=1673.49; final_adjustment=-0.01 |
| sm-payroll-social.md | 4 | applicable_income=40000; pension_component=9600.00; social_security_component=800.00; fondiss_component=1600.00; stated_component_subtotal=12000.00 |
| sm-payroll-social.md | 5 | ordinary_pension_slice=12070.6272; excess_pension_slice=194.1144; isolated_pension_component=12264.74 |
| sm-payroll-social.md | 6 | stated_plan_penalty=600.00; principal_and_penalty_before_interest=12600.00; equal_allocation_before_interest=1050.00 |
| sm-transfer-pricing.md | 1 | upward_income_adjustment=10000; isolated_additional_igr=1800.00 |
| sm-transfer-pricing.md | 2 | bilateral_multistate_fees=60000; separate_first_unilateral_fee=15000 |
| sm-transfer-pricing.md | 3 | gross_profit=8000.00; revenue=108000.00; profit_percentage_of_sales=7.407407407407407407407407407 |
| sm-vat-gst.md | 1 | import_tax=2040.00; base_plus_import_tax=14040.00 |
| sm-vat-gst.md | 2 | ordinary_tax=1700.00; table_a_tax=40.00; total_import_tax=1740.00 |
| sm-vat-gst.md | 3 | conditional_import_tax=500.00 |

Local independent calculation artifacts: `/private/tmp/oa-sm-independent-arithmetic.py` and `/private/tmp/oa-sm-independent-arithmetic.json`. They are review aids, not changes to the repository or new automated legal tests.

## Source identity and actual read scope

I independently re-fetched 17 material primary PDFs plus the two coordinated archives (19 sources total). Every response was HTTP 200 and every complete-body SHA256 matched the writer's retained source identity. Initial network attempts inside the default sandbox failed DNS resolution; the read-only public-source retrieval succeeded under approved network escalation. The web reader independently opened DD 156/2026, Law 141/2025, DD 133/2026 and the Italian Gazette page; it could not open DD 116 or the public calculator query. The successful direct retrievals below resolve transport only and are not represented as full substantive review of every page.

| Source | HTTP | Exact retained identity match | SHA256 |
|---|---:|---|---|
| law-141-2025 | 200 | True | `274ef75aa5da81c8c0e10be9a87bda3246a8eb3867de515ba2aba42a9154ba18` |
| crossborder-circular-1-2026 | 200 | True | `23997e3d5a51aa1d645205b90f783379d7b5fff87e24a5ec86b56d1f3c0b5d59` |
| dd-156-2026 | 200 | True | `5be329c273f1462c7b57a33e81d81050185182a61f76671d39255292f1638881` |
| dd-116-2026 | 200 | True | `3df5a20303498f924ee45a5cc0a21461eb26a91c5a89ecf13098a7297696d462` |
| dd-98-2026 | 200 | True | `5f66c378c1c86ef06207b32e8b08e1b0b14594b976f80582c4047430cd417743` |
| dd-133-2026 | 200 | True | `9198273eba5a15d18b86be252c8acdea2760176f76456a1632e5ef0638493d2d` |
| iss-general-revised-2026 | 200 | True | `7b6c1a321a75dd029aa19585b1f8745ac4c43ef0ec1832003634b21df4fc5ad3` |
| pension-law-157-2022 | 200 | True | `7eff5489f2d598750f2c2e5fee171f57b26d058f22c88d1d4e7a818eb1f54609` |
| import-law-40-1972 | 200 | True | `9e520020b95448dbc94d143c1ad929042513b2a556e7c90f6f50f4f55a4cb1a1` |
| import-d-50-1993 | 200 | True | `f8dea1e7b0130f07102c643d40dee29aad5818915754d4f853148dabbf4e99a6` |
| import-dd-183-2011 | 200 | True | `8e3ad9d943239739fe216ad13283469868efc214f34d0393233392e7f6a2e8b9` |
| import-d-108-1997 | 200 | True | `3552dce9dddfa06c71fe8433f9550a4f601fd7cf879eb611d486cfe89b037752` |
| import-d-135-2003 | 200 | True | `d6137ce89f82cc985e0c346be611f6b173fcba7e20a4ceb94efd376738df5ab7` |
| company-law-80-2022 | 200 | True | `4f032d3ba066d3ec1ab1106030165fc2b1fbba2b0b374ac3aa56136dfaedc444` |
| italy-gu-168-2021 | 200 | True | `18dcb791dec4ac7914b92f1e41afeb5a148616d7a9b83d781eb4a651e8957f0f` |
| reg-24-2026 | 200 | True | `1ad8dde05bfea7af439d94052e964802eadd7f973b1b1247fd582575887a7437` |
| iss-instalments-4295-2026 | 200 | True | `c6ec2a42df7194a33e48693942bf31576ea83d43dadc2228808ca2ac6249c740` |
| coordinated_archive | 200 | True | `0901777ac682f9d719ef5cd9b75a3409f52da085670c91e36ea79c91165ff86d` |
| company_coordinated_archive | 200 | True | `07e213846e9f5f88607dbacaef1b93d8860fe91521f8710191725315adab4047` |

Reviewer's retrieval record: `/private/tmp/oa-sm-review-primary/reviewer-source-retrieval.json`. Public primary material only; no credentials or client data. The country source-retrieval/transport records were inspected as provenance evidence, not treated as proof of legal completeness.

Actual material comparisons:

- **IGR chronology and corporate method:** distinguished the no-notes 22 December 2025 and with-notes 12 December 2025 editions in the official ZIP. Reopened Law 141/2025 and checked selected source, base, rate, losses, new-activity, advance and commencement provisions against the coordinated text. Its temporary covered 18% rate applies to 2026–2030, the ordinary loss cap is 70%, and half-rate relief is conditional rather than automatic on incorporation. Corporate foreign-credit allocation, equity-increase deduction and ordinary advances match the selected cited passages. Full cost, asset, incentive, restructuring, every amendment and operational filing scope remain open.
- **Current October correction:** read all twenty DD 156/2026 articles, including the from-2026 application rule and retained pre-2026 regime. Compared the identification/representative/no-automatic-PE rule, family/guardian allocation, mixed-income credit election, foreign residential rent, travel conditions, individual loss amendment, late-return charges, SMaC family allocation and selected specialist changes. The draft does not silently treat the December archive as the current consolidation.
- **Personal IGR:** checked the eight marginal tariff bands, gross-wage forfait/cap, pension deduction slices, family-credit conditions, ordinary SMaC endpoints/interpolation, separate business credit, election, personal foreign-credit ceiling and selected statutory procedure. The quoted low-income and high-band examples match those assumptions. Full categories, medical/rental relief ordering, every SMaC boundary/rounding combination and actual mixed-income execution remain expressly open.
- **Public synthetic calculator:** independently reran the public 30,000 gross annual wage case with employee type, 2026, thirteen periods and default components. HTTP 200; response SHA256 `cf6ed2b20334dd68db61b13f6dd5b0e1974f30c440f0118125d1ce1770a6efac`, exactly matching the writer's retained response. It states taxable wage 24,930.00, tariff tax 3,118.10, maximum credit 1,444.62, required SMaC spend 5,455.14 and final IGR 1,673.48. The live observed program output and source law support the worked scenario; they do not prove full-credit entitlement for a real person. I inspected the retained 11,000 and 50,000 observations, but did not independently rerun those two. Record: `/private/tmp/oa-sm-review-primary/public-calculator-30000-review.json`.
- **ISS rates/bases:** visually compared revised circular 2187/UC/2026 pages 1, 4, 5 and 10, including table-column alignment and footnote scope. It expressly supersedes the March circular. Pension, aggregate employee ISS, separate FONDISS, professional excess-income footnote and separate social-security ceiling match the draft's conditional statements. The 10.3% cash subtotal is not labelled an automatic 9.9% tax deduction or total employer cost. Selected enacted Law 157/2022 rate provisions and the record's special-scheme limits were checked. Full employee calendar, all employer funds, ceilings, coverage and every special case remain open.
- **Contribution debt:** read all fifteen Regulation 24/2026 articles and visually compared ISS circular 4295/UC/2026. The employee-specific notice count, separate ISS/FONDISS notice tests, October transitional state, distinct licence-count categories/exclusions, twelve-month plan, stated 5% penalty, one-instalment default and roll-stage restrictions match the cited route. A directed reform proposal is not enacted as a replacement sanctions schedule. Full underlying current penalty/licence chain and live notices are not certified.
- **TP/APA:** read all six DD 116/2026 articles against the draft. Checked international scope, group-turnover fee tiers, alternative unilateral/renewal reductions, no refund, nonanonymous pre-filing, signature-based five periods and conditional rollback. The two-State fee control expressly assumes accepted fee classification, and 8% cost-plus is expressly a hypothetical comparator, not a safe harbour. Domestic normal-value and limited downward-adjustment routes match selected IGR 2/6/30/46 passages. Actual comparables, circulars, MAP, CbCR and applications remain open.
- **Cross-border circular:** inspected the retained scanned circular's substantive text and visually compared page 2. The specific no-PE foreign-bank/rental scope, 13%/10% B2B and covered 18% B2C route, actual payment timing, documentation and anticipated 2027 systems are kept distinct. Checked domestic residence/source/PE and selected article 44 corporate-credit passages. No actual treaty outcome, general 183-day exemption or live future system is inferred.
- **Monofase and Italy:** checked selected original Law 40/1972 scope/base/liability/export wording, Decree 50/1993 base/document provisions, tariff framework and DD 183/2011 ordinary rate/commencement. Selected capital-goods Decree 135/2003 provisions support a conditional rather than universal 1% example. DD 98/2026 is a selected dated table amendment. Reopened authentic DD 133/2026 in full, finding F1; its optional 2026 route, 2027 obligation and 2028 sanctions are otherwise distinguished. Compared the Italian Gazette's DM 21 June 2021 material ordinary business-goods/electronic/validation provisions and dated transition. Full tariffs/amendments, claims, excise, special cases and technical/live execution remain partial.
- **Formation:** compared selected November 2024 coordinated company-law provisions and original Law 80/2022 capital/registration text. Ordinary 120-clear-day half-capital and three-year full contribution are separate from the conditional 9,000 SRL sixty-clear-day/full contribution route. No universal resident-director or automatically licensed profession assertion is retained. This is explicitly a dated baseline with later 2025–2026 company/activity amendments unverified, not a complete 2026 incorporation opinion.

## Limits and closure requirement

This advisory review covers the entire country pack's selected methods and internal consistency, not every law affecting San Marino. I did not research every unlisted amendment or actual treaty; determine a client's eligibility; test authenticated portals, filing, ingestion, production writes, payments or professional attestation; or independently rerun the writer's 129 repository unit tests. That writer evidence is separate and must be refreshed for the corrected checkpoint as appropriate. The presence of eight Guides, 28 passing arithmetic controls, current dates and successful source retrieval does not establish comprehensive coverage.

Before publication: fix F1; consider/apply O1/O2; reconcile workflow/review prose; provide the exact corrected checkpoint and changed-country blob manifest for focused closure. Preserve the complete original findings above when adding any closure. No push or closure is authorised by this report alone.

## Focused correction closure, 24 October 2026

Exact corrected source checkpoint: `b5e11396408884836a1d3b31dd10ba265628eae1`. I inspected the country diff from original reviewed `fc1a9b19591ebb8f163c4a1e8378694abb7c9c29` and independently verified every corrected country blob. Evidence-only checkpoint `c4f12b62` preserves all nine corrected blobs unchanged.

- **F1 closed:** monofase Guide 0.2 distinguishes the strictly-below annual exclusion, exact-equality current-year obligation, and article 2(3)'s exceeded-threshold/option continuation. Exact-equality persistence is left for official interpretation. It no longer asserts permanent entry from equality alone.
- **O1 addressed:** payroll/social 0.3 now states both article 125(1) starting events, withholding made or monthly employment income accrued, and expressly warns against using salary cash alone. This does not claim the missing ISS employee calendar is settled.
- **O2 addressed:** XB 0.3 links the personal Guide's expressly partial article 18 method and limits referrals to cases beyond it. Its specialist/timing/correction limitations remain open.
- **Workflow/review prose addressed:** all eight Guides refer to the dated source-review record while retaining named San Marino accountant review open. README 0.5 and overview 0.4 remove the stale unpublished assertion; README reflects primary Armenia/Montenegro queued. Publication/CI is tracked separately. The writer must include this complete original-plus-closure report at the linked repository path in the country batch.
- **Exact-content safeguards pass:** all 28 original `oa-check` blocks are byte-identical, so the independent scenario calculations above still apply. Every Guide's version advanced and H1 agrees. All other frontmatter apart from description/version is unchanged. Inherited platform fields are unchanged; no new platform fields are invented. The README's seven partial entries are unchanged. Both corrected source-hash records match all nine corrected country files, and the evidence-only commit preserves them.

**Closure outcome: no blocking source-review finding remains within the reviewed selected-method scope for publication as one partial, tier-2 country batch.** This is not a statement that the country is comprehensively covered, professionally attested, merged, live or ready for a particular filing. All source/read-scope and unverified legal/operational limitations in the original review remain. The writer reports refreshed schema, metadata, calculation, 129 repository-unit and 40 MCP-test results; I have not rerun those suites and do not substitute them for source review. Exact published-head CI remains a separate post-push check. I made no source edit, commit or push.

### Exact corrected country manifest

| Country file | Corrected Git blob | Version | Controls | SHA256 |
|---|---|---:|---:|---|
| README.md | `a1c902e9d35927cf80ae979f502aefd2b658d221` | 0.5 | 0 | `f06f21f141c5c5130cf2d12184923b18913e556734da4a9afc7d83398f5202d5` |
| sm-company-formation.md | `98d5dcd6d02240d20b99cfc9e3d56b0b1a2151eb` | 0.2 | 2 | `3213f2f7c3bb1bd07637f75cd1fdd5f979dff0a78922f45f9200448e0fc54e25` |
| sm-corporate-income-tax.md | `71a04d463b1846108c3b8a6712a560dffcea86ab` | 0.3 | 4 | `1581fbd03fc673d65d9e272ede646557ff45bf6b46a811ed5d33ad66daa011b8` |
| sm-cross-border.md | `cac543f4654692c8d89a82fd9bd07322a547c66c` | 0.3 | 4 | `4d09329515cad5079999890ad51f1c286bd6b1127ddfd322483a1a66a281593a` |
| sm-income-tax.md | `2bc86a804f371cf968015293c6080d7f0bd85a83` | 0.2 | 6 | `744e4e44d8b55ffcd8162432fd24ee1a3b4165d10226b5391b978225766ecfb6` |
| sm-payroll-social.md | `1dbae1890dfecd33abeb559b97eaffe1b6ba5ccf` | 0.3 | 6 | `ffb9144b818dffa6743bd9c80e06bfe12e7eb3f924b1d8eb64ab1770e3408afe` |
| sm-tax-overview.md | `ce3f1ceee7b963a8f57bafa14eee3ff306282ab6` | 0.4 | 0 | `b26e78811b5197e0da66839e7083b413c93eb5ecb14a8be9a5326ad33121c181` |
| sm-transfer-pricing.md | `b9121db2c07d1e2fac1ad3b3998ea98ac0e73630` | 0.3 | 3 | `ef783b5a2be4a92b95d39915bb89e1ba0ca31ddf50f14b1da338728a87db6c7d` |
| sm-vat-gst.md | `bfd456f9792f4557e834403cfa0415a22dbf3ed8` | 0.2 | 3 | `02f7b3d952ff36c2d2a0a65bc1ae8c5ad1a349a1fe951c65d990f4b46b497154` |

Closure audit artifact: `/private/tmp/oa-sm-review-closure.py`; final manifest: `/private/tmp/oa-sm-independent-final-manifest.json`. Original findings and manifests above are preserved as historical review evidence.
