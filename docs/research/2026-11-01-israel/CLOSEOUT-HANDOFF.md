# Israel PR #1198: evidence checkpoint, not accepted for merge

Read date: 2026-11-01. Public repository: `openaccountants/openaccountants`.

- Live PR inspected as open on branch `refresh/il-2026`, initial head `10496024ad46c0fa45469fb4a4ec0c2746f0bc70`, base branch `main`.
- Full actual merge base: `46c01152da0fdd1b722f61190c88413d0a195d02`.
- Nine changed Guides. This checkpoint does not change any Guide, generated file, platform field, byline or CTA suffix.
- No GitHub reviews or comments were present when inspected. Earlier partial independent review checked eight insurance figures and arithmetic on eighteen examples, but did not accept the tax/VAT/immigration rules.
- **Status: HOLD. There is no completed repair or fresh independent acceptance. The initial PR still contains unsupported operative assertions. Do not infer acceptance from a current-year label or green CI.**

## Official material acquired

`source-register.json` records the six authentic source files, official URLs, SHA-256 hashes, actual selected read scopes and acquisition methods. Source bytes remain outside Git. The documents are:

1. Tax Authority salary deduction booklet for January 2026 onward, updated April 2026.
2. Tax Authority 2025 rights/duties guide, published July 2026; the VAT annex expressly states January 2026 figures.
3. Tax Authority Circular 5/2018 on distributed payment assets.
4. Tax Authority Circular 4/2026, Form 150, especially section 2.1.2.
5. National Insurance working-age self-employed rates page.
6. National Insurance employee rates page, including controlling-shareholder column 2.

Direct gov.il tool/curl fetches returned 403. An ordinary browser opened the official pages and downloaded the four linked PDFs successfully. No CAPTCHA, certificate bypass, disguised request or access-control bypass was used. Browser link `downloadMedia` worked for PDF links. The PDF viewer's displayed document title is stale (2025); the downloaded booklet cover and contents explicitly identify January 2026, updated April 2026. Do not mistake that stale viewer title for the source year.

A normal attempt to fetch a Knesset corporate-tax research PDF redirected to a geographic unavailability page. That response is not a PDF or tax evidence. No claim was accepted from its search extract. No archive fallback was completed for it.

## Concrete repair findings from opened primary material

These are findings for the next writer and reviewer, not a complete figure ledger:

| Guide | Finding | Opened official location |
|---|---|---|
| Income tax returns | The 2026 earned-income bands in the initial PR match the April booklet. Additional 3% on total taxable income and 2% on capital-source income have separate bases; a blanket 5% on every capital component above a total-income threshold is unsafe. Residential-property surtax inclusion also has its own sale-value/exemption conditions. | 2026 booklet pp.10-11, Income Tax Ordinance ss.121,121B |
| Employee refund | The initial estimate formula has the sign reversed: refund is tax paid minus final liability. Credit-point value does not establish entitlement or an automatic refund. Historical refund years need their own year's law. | Rights guide printed pp.5-6,118 / PDF pp.7-8,120; 2026 booklet p.12 |
| Freelancer operations | The old NIS1.5m periodic VAT threshold is not the 2026 amount: the current annex states NIS1,775,000. Its NI minimum-income assertion of NIS2,065 also conflicts with the opened page's NIS3,442. | Rights guide printed p.139 / PDF p.141; National Insurance self-employed page |
| VAT | Supplier-name classification tables do not establish legal treatment. The annex states 2026 allocation thresholds, lawful input documents, taxable-use conditions, six-month input window, and different private-car purchase/running-cost rules. Rebuild the examples, including the foreign-service example and the return that omits reverse-charge output while taking its input credit. | Rights guide printed pp.138-140 / PDF pp.140-142; VAT Law ss.38,41,47 and VAT Regulations regs.14,18 as cited there |
| Corporate tax | Opened NI totals confirm working-age shareholder payroll rates. A prescribed 6.53% interest rate is not a universal loan-principal tax or a safe harbour from withdrawal reclassification. The minimum-salary expectation and undistributed-profit simplification remain unaccepted. | NI employee column2; 2026 booklet p.15; rights guide printed p.56 / PDF p.58 |
| Crypto | Circular 5/2018 supports the asset/business/mining/barter distinction and its distinct VAT classifications. It does not establish mandatory FIFO, all DeFi/staking/airdrop rules, or a universal material-shareholder uplift for crypto. Ordinary asset-disposal reporting is distinct from listed securities. | Circular5/2018 pp.2-6; rights guide printed p.46 / PDF p.48 |
| New immigrant | The initial PR reverses ordinary/veteran returner categories and treats foreign employer/account location as sufficient source evidence. A blanket reporting exemption is unsafe for residence starting from 1January2026: Circular4/2026 s.2.1.2 specifically changes conditional Form150 reporting. A ten-year tax exemption must be separated from reporting duties. | Rights guide printed p.52 / PDF p.54; Circular4/2026 pp.2-3 |
| Withholding | Do not accept the initial universal 30% services default, its 20% dismissal, all listed payment rates, or its pre-VAT base without the governing orders. The authority states different payer/payment regimes and certificates. The NIS5,520 row alone does not prove all de minimis conditions. | Rights guide printed p.118 / PDF p.120; 2026 booklet p.15 |
| Customs | Neither the initial USD75 threshold/history, tariff ranges nor EUR.1 claims were confirmed in this checkpoint. The standard VAT rate alone does not establish an import exemption, valuation base, duty or origin preference. | No accepted current customs source in this checkpoint |

## Remaining mandatory gates

- Complete the actual nine-Guide diff/body review. A full diff was saved for continuation; this checkpoint does not claim that every line has been read or accepted.
- Produce one complete per-Guide figure/rule ledger: decisive exact Hebrew excerpts, article/page, official URL, read date, cached-byte hash and actual read scope. Forty-four private candidate rule notes exist; they are **not** a frozen ledger or accepted quote set.
- Produce every original old-topic destination from immutable merge-base blobs, including rates, exceptions, taxpayers, filing steps and examples. Base and initial-PR blobs were cached. No completed destination table exists yet.
- Repair unsupported operative text, retaining unresolved inherited topics as explicitly non-operative holds with destinations. Do not silently drop them or give failed pages read dates.
- Repair canonical headings, matching numeric H1/version, 80-150-word descriptions, row URLs, general notice and two meaningful executable examples per Guide; retain tier2 and all platform fields/CTA suffixes against the full merge base.
- Run the actual committed changed-only validator with `--no-index-check`, all fifteen semantic checks, eighteen executable cases, strict metadata sync integrity at the full merge base, and whitespace checks.
- Obtain fresh independent pack review after the repairs and ledger freeze, then exact-head CI and required separate-account approval. No auto-merge was enabled.

## README and validation status

The existing country README still says 2025/needs updating, and identifies social contributions and transfer pricing as missing. It makes no full-pack completion claim. It was inspected and left unchanged; no generator was run.

No changed-Guide validation was completed in this checkpoint. An attempted `python3 scripts/validate-guides.py --help` is not a supported help invocation in this script: it unexpectedly ran the broad local check and failed on pre-existing stale generated `index.json` and `llms-full.txt`, with structural warning groups. This was diagnostic output, not a valid PR check; no generated file was changed to suppress it. The handoff commit receives a whitespace check only. Original-head CI success does not validate this incomplete source review.
