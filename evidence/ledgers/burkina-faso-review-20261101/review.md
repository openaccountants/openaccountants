# Independent review: Burkina Faso two-job local draft, 1 November 2026

Decision: **REJECT the frozen TP preparation draft pending R1.** The non-resident-services Guide passes the source, condition and arithmetic review for its expressly limited domestic-law preparation scope. This is a local review, not country-pack approval, publication permission or accountant attestation.

Frozen input: `dd6be766e414d399098b29ae15c0355c63cba286`, branch `codex/burkina-faso-tax-2026`. Initial worktree was clean. Baseline `origin/main` and the frozen commit's parent both equal `db5bf4ff7d4b078421b4fedd483d9b9b91cd71a6`. The reviewer read CLAUDE.md, docs/skill-template.md and the pack README template. No separate AGENTS.md exists inside this public repository. Applicable user/parent instructions were also followed.

## Figures and rules checked

**41 ledger rows checked: TP 24; non-resident services 17.** These are ledger-row counts, not 41 unique numerical figures: they include broad rules and two duplicate navigation checks. Every stated rate, threshold, deadline, penalty and legal rule in those rows matches its cited source. TP rows 11, 13 and 14 need the preparation-completeness repair below. The ledger quotations match the source wording with typographic apostrophe/whitespace normalisation; no incorrect amount or translated quotation was found.

The accompanying `input-and-check-manifest.json` records each row's outcome, exact SHA-256/git blob inputs, all eight preserved Guide hashes, source PDF/text/image/manifest hashes and arithmetic outputs. The manifest binds this conclusion to the frozen inputs only.

## R1: complete the claimed master/local-file preparation checklist

Location: `skills/burkina-faso/bf-transfer-pricing.md`, **The base**, the two bullets introduced by “Prepare two files under articles 1–3 of that order”. Ledger rows 11, 13 and 14.

The Guide presents these bullets as the preparation contents but collapses mandatory items into labels such as “intangibles and agreements” and “financing”. A preparer following them can omit required information. This is a completeness failure under skill-template line 4, not a rate error. Expand the existing bullets or add a compact checklist to cover the following exact missing details; no new tax job is requested.

| File | Required detail to restore | Signed 2026 order provision |
|---|---|---|
| Master | Supply-chain goods/services ranked by turnover; important intragroup service arrangements exclude R&D services and must describe the main service sites' capabilities and cost-allocation/pricing policies. | Art. 2(2)(b)–(c), page 2 |
| Master | Significant reorganisations **and acquisitions/disposals of assets during the fiscal year**. | Art. 2(2)(f), page 2 |
| Master | Intangible development/ownership/exploitation strategy, including main R&D installations and R&D management locations; important intangibles and their legal owners; cost-sharing, principal research-service and licence agreements; R&D/intangible pricing policies; significant intangible-interest transfers during the year, including entities, countries and consideration. | Art. 2(3)(a)–(e), page 2 |
| Master | Group financing structure including important independent-lender financing; each central financing entity's incorporation-law country and effective-management location; intragroup-financing pricing policies. | Art. 2(4)(a)–(c), pages 2–3 |
| Local | Management structure/reporting lines, persons to whom local management reports and their principal-office countries; restructurings or intangible transfers affecting the enterprise **during the current or preceding year**, explaining their impact. | Art. 3(1)(a)–(b), page 3 |
| Local | Controlled transaction context and the nature of each linked-enterprise relationship; functional/comparability changes from earlier years; reasons for tested-party choice and any multi-year analysis; say whether comparability adjustments affect the tested party, comparables or both. | Art. 3(2)(a), (c), (e), (g), (i), (k), pages 3–4 |
| Local | A summary of financial information used to apply the method, and summary tables of financial data for the comparables **and the sources from which the data are drawn**. Existing annual-account reconciliation wording covers art. 3(3)(b), but does not cover these separate requirements. | Art. 3(2)(m), 3(3)(c), page 4 |

Source: [signed Arrêté 2026-000287/MEF/SG/DGI](https://dgi.bf/wp-content/uploads/2026/09/ARRETE-N%C2%B02026-00287_MEF_SG_DGI-PORTANT-FIXATION-DU-CONTENU-DE-LA-DOCUMENTATION-DES-PRIX-DE-TRANSFERT.pdf), all five rendered pages independently read. The reviewer did not alter Guide bytes. Writer repairs must update the relevant ledger detail and receive a check of the new frozen inputs. This initial record must be preserved.

## Effective dates, scope and sources

- The official CGI explicitly identifies the 2026 edition, including 2025 rectifying-budget and 2026 budget changes. The read was limited to the edition statement and CGI arts. 65–66, 95, 98-1, 98-2, 99, 210–214, 671, 757 and 768, including adjacent paragraphs and the reproduced declaration order 2022-101. No claim is made to have read all 566 pages.
- TP annual declaration **above** XOF 1 billion versus audit documentation **at least** XOF 1 billion is correct. Majority ownership alternatives, domestic controlled transactions, actual control, common-person control, privileged-tax counterparties, notice timing and the affected-transaction penalty base were checked.
- The five-page signed order is dated **14 July 2026**. Arts. 7–8 repeal the 2022-102 documentation order and take effect on signature. Its distinction from the 2022-101 annual-declaration order is correct. The separately signed order wins over the superseded documentation text reproduced in the CGI. Pre-signature documentation practice is explicitly unresolved.
- The order URL failed through the web tool. A normal direct fetch first failed under sandbox DNS, then succeeded with narrowly scoped network escalation. The newly downloaded official PDF's SHA-256 exactly matches the supplied PDF: `564208d953f8c50c8d5ec104b4ee266f9c06d7caa9ffe7a68fd83fa1f3d807d2`. The CGI opened independently from its official URL through the web tool. The DGI index was opened and its actual 2026 CGI and eSINTAX navigation links read. No authenticated session was accessed.
- Withholding scope, all payer categories, the 20% and exclusive-road-freight 10% rates, incidental-expense base, prohibition on debtor bearing tax, declaration/certificate data, the 15th remittance date and three sanction branches agree with arts. 210–214, 671 and 768. No treaty relief, gross-up entitlement or sanction cumulation was inferred.
- No research beyond the cited official sources was needed: the failed completeness check is resolved by the signed order already cited.

## Four independent recomputations

| Case | Recomputed outputs | Result |
|---|---|---|
| TP price adjustment | 1,000 × 10,000 = 10,000,000; 1,000 × 12,000 = 12,000,000; difference 2,000,000 | Pass |
| TP exact threshold and penalty | max(1,000,000,000; 800,000,000) minus threshold = 0; 100,000,000 × 0.005 = 500,000; statutory floor 10,000,000 | Pass; own-size declaration test fails and documentation test passes on stated ownership facts |
| Withholding, travel | 5,000,000 + 500,000 = 5,500,000; × 20% = 1,100,000; cash = 3,900,000; payer outlay = 5,500,000 | Pass |
| Road versus mixed services | 10,000,000 × 10% = 1,000,000; cash 9,000,000; × 20% = 2,000,000; cash 8,000,000 | Pass on the stated exclusive/mixed and no-treaty assumptions |

Both Guides pass all 15 `skill_checks.py` checks. `check-examples.py --require` checked two files/four blocks with zero failures and zero missing. Full `validate-guides.py` could not start because PyYAML is absent from both system and bundled Python (`ModuleNotFoundError: No module named 'yaml'`). Full-repository validation and coverage-report execution are not claimed; parent/writer should run them in the working dependency environment before a publication decision. Logs are retained alongside this report.

## Preservation and README

All **eight** legacy Guide files were byte-compared to `origin/main`; all remain identical, including their platform metadata and CTA. The input manifest records their hashes. Lost content restored: **0**; no content was removed. The old-topic table represents all eight files. Spot checks covered formation beneficial owners, corporate distributions, income-tax head-office deductions, payroll family reductions, social-contribution ceiling, optimisation election deadline, overview identity and VAT e-commerce; destinations remain the original files. Retention is not validation of their old tax claims.

All seven domains are listed as applicable and all seven are explicitly partial. TP and XB correctly identify the new drafts' incomplete workflows and specialist scope. The five core legacy domains identify stale 2025 coverage; the three additional legacy Guides are explicitly retained without recertification. No inapplicability, full-country coverage or accountant sign-off is claimed. The frozen README's statement that independent review is pending remains historically accurate for this rejected TP candidate; any eventual changed status must match the follow-up review.

## Still not confirmed

Current declaration/certificate form identifiers and boxes; authenticated portal and submission-confirmation workflows; CbCR implementation/forms/exchange and local/substitute exemptions; APA procedure; pre-14-July documentation practice; ordinary IS consequences/sanction interaction; particular treaties' continued force, entitlement and claim procedure; PE profit taxation; VAT interaction; expense deductibility; sanction cumulation; existing net-of-tax contracts. These are already excluded or listed on the Guides' unresolved lines. No new specialist work was undertaken.

No push, PR, public comment, merge, source deletion or accountant attestation was performed. Follow-up acceptance requires R1 repair and review of the repaired bytes.
