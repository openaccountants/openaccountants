# Montenegro individual income-tax source reconciliation

Read on 24 October 2026, issue #412, local branch `codex/montenegro-country-completion`, shared base `7775cf6a`. Previous goal turn was progress at payroll source `2f94130a` / validation `eb255509` and issue #412. This pass rebuilds retained individual v0.2, preserving the previous secondary-source summary at `eb255509:skills/international/montenegro/montenegro-income-tax.md`. Review/attribution/licence/CTA retained, no professional-review upgrade.

Fresh fetch confirms clean active worktree, no further shared advancement beyond `532a1568`; no Montenegro overlap previously found on the shared workstream. No new PR or country push.

## Actual primary reading

| Source | Reading and limits |
| --- | --- |
| [Ministry PIT consolidation through 160/25](https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0) | Actual previously retrieved PDF read further for Articles 16–37s, business expenses/assets/losses, rental, private capital and property/securities disposal, sport/royalties/other/internet categories, 42–50f settlement/filing/payment and sanctions. Prior payroll residence/exemption/status reading reused. PIT EUR 200 asset threshold and 3% qualifying-purpose cap deliberately distinguished from corporate EUR 300/3.5%. Does not establish actual taxpayer eligibility, valuation/indexation or current form boxes. |
| [Enacted 160/25 amendment](https://wapi.gov.me/download/47bea12c-f250-4cdc-b481-3afc30fba94f?version=1.0) | Prior operative reading reused and relevant principal/supplementary/occasional classifications, rate gates, annual filing/payer and advance provisions reconciled to consolidation. Application January 2026. No principal-business allowance extended to supplementary business. |
| [70/26 Gazette text](https://www.sluzbenilist.me/propisi/394390/download), [official record](https://www.sluzbenilist.me/propisi/394390) | Prior actual one-page Articles 1–3 reading reused: gambling 12% from 21 May 2026, distinct from the earlier scale still printed in the January consolidation. Full earlier-period transition/foreign gambling method remains open; no fabricated all-year current calculation. |
| [Annual-return rule, Ministry April publication](https://www.gov.me/en/documents/afb50b45-7e83-4dac-b69e-2a1e280d3ffc), [actual PDF](https://wapi.gov.me/download/afb50b45-7e83-4dac-b69e-2a1e280d3ffc?version=1.0) | Actual two-page PDF through 103/25 downloaded/read; page 1 rendered and visually inspected. Names GPP-FL and A/PPG/A1/B/B1/C/D/D1/E/E1/F/G/H; contains no actual attachments/instructions. Do not make up numbered form mapping or infer current supplementary-business schedule/IRMS acceptance. Current law's filing-population exceptions govern over older wording. |
| [Different official GPP-FL attachment](https://wapi.gov.me/download/6f6af511-ccf7-4fc1-bd5d-82243d9a91cd?version=1.0) | Actual 20-page PDF retrieved and inspected for identity, schedule names and tax computation. It uses obsolete flat 9% and fewer schedules; rejected as current mapping. Its survival on an official host does not make it current. No full current-tax implementation inferred. |
| [2025 proposed replacement](https://wapi.gov.me/download/b6aa4bd1-73e1-46ae-afaf-52d3b7d06686?version=1.0) | Search result explicitly labelled PREDLOG. Not substituted for the promulgated actual attachments or claimed as operative reading. Search preparation does not close the form gap. |
| [September salary proposal](https://wapi.gov.me/download/58f7f48c-33de-4ec0-a1f4-28fd16fc7fb6?version=1.0) | Prior full scanned one-page visual reading reused: application January 2027, final enactment not certified. Not used to change 2026 salary or annual principal-business rates. |

## Method and computation scope

Nine new controls: principal actual-income accounts-to-tax with PIT-specific expense caps, established depreciation/loss and paid advances; principal versus supplementary status rates; occasional independent withholding with standard expenses; rental 30/50/70% alternative evidence gates; property adjusted sale/indexed-cost and current capital loss; securities FIFO; residual internet versus video-game competition expense/base; capped qualifying foreign dividend credit; fine-art rights and qualifying amateur sport. Taxable bases and advance/foreign-credit registers stay separate. No corporate donation threshold, private dividend blanket exemption, general internet classification or business-loss carryforward for capital losses is imported.

The ordinary annual settlement example is a PIT-only established business case, not an integrated mixed-income form. Other controls explicitly exclude local surtax, insurance, incentives and other levies unless stated. Property indexed cost is an established hypothetical input, not a fetched inflation series or authority valuation. Foreign tax eligibility/treaty/refund proof and category classification are hypothetical cleared facts; no bilateral rate, automatic unused-credit carryforward or actual taxpayer clearance is claimed.

Removed old current-rate defaults, duplicate payroll calculations with wrong prirez allocation, unsourced shortcuts and unrelated VAT rate/registration summaries. Companion payroll/contribution/VAT methods own those computations; historic research preserved in Git.

## Remaining coverage and review

Actual current GPP-FL attachments/instructions, supplementary-business/new-activity forms and IRMS; full PIT depreciation/status/loss and specialist expense/relief/lump-sum procedures; real valuation/indexation and property/family exemption evidence; gambling transition; treaty/residence/foreign-credit implementation; local surtax/insurance/levy integration; exact amendments/refunds/interest/appeals/enforcement; independent full-country review and named accountant attestation. All seven domains remain partial, ten Guides and zero professionally reviewed. Complete applicable-domain arithmetic is not comprehensive coverage.

## Validation

Full-country required-example check now passes: 11 files, 39 controls, zero failures, zero missing. Final metadata/contributor/whitespace results will be recorded after source commit. No unit suite, generated-index/package validation, remote CI, new reviewer assignment, country push or publication claimed.

Final source checkpoint `1b10dfd1`, shared base `7775cf6a`: strict metadata checks seven source Guides with zero errors/warnings/notices. Contributor validator checks 104 Guides from 117 changed paths and passes with inherited Gibraltar 2024 freshness warning (two warning groups). Whitespace and full-country required-example checks pass: 11 files, 39 controls, zero failures/missing. Fresh in-memory coverage report confirms ME: ten Guides, reviewed 0, all seven domains partial/missing for complete coverage, complete:false. No unit suite, generated-index/package validation or remote CI claimed.
