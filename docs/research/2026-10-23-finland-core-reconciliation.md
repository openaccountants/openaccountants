# Finland core reconciliation and local country batch

23 October 2026. Michael directed the support chat to move from Iceland to Finland. The published allocation reserved Finland to ChatGPT. The handover was recorded on [issue #392](https://github.com/openaccountants/openaccountants/issues/392#issuecomment-6371115950) before writing. Local branch: `codex/finland-country-completion`, starting at shared published head `915c5118`. Reuse consolidated draft PR #514; no per-Guide publication.

## Existing work preserved

The baseline contains 12 source Guides plus README, rather than the issue body's original seven-Guide snapshot. Existing payroll, TP, residence, CbCR and property work and their research records were read and retained. VAT, YEL and prepayment operational drafts were extended with executable controls. The formation draft remains legacy 2025 work and is explicitly unresolved. The overview now routes to topic sources rather than repeating the earlier unverified summary figures. Earlier bodies remain in Git history.

## Individual-tax source work

- Act 1140/2025 section 1: indexed official Finlex statutory table, corroborated by directly opened Vero earned-income page. The direct Finlex open returned a navigation shell. This is not a direct full-statute retrieval or complete amendment audit.
- Dedicated Vero capital-income and entrepreneur-deduction pages: separate rate/base classification and deduction ordering.
- Vero Form 5 instructions: ordinary capital-allocation route and exceptions remain distinct from a universal percentage split.
- Vero YEL deduction page: the older personal-only prohibition contradicted the permitted business-return route. Replaced it with one-route/no-double-claim preparation.
- Current filing and individual timeline: distinguish the 2025 return cycle from 2026 income; do not invent the 2027 personal filing calendar.
- Individual sanctions and official interest calculator: distinguish filing charges, punitive increases and ordinary late-payment interest from reduced interest.

The relevant URLs and read date are in `fi-income-tax.md`. Most detailed administrative passages were read as indexed official text; no full current Income Tax Act/Business Income Tax Act audit is claimed.

## Corporate source work

Directly opened the Vero corporate rate/base, loss, return and corporate-sanction pages. Read indexed official Form 6B, instalment, residence, nonresident investment-income and future-change guidance. Replaced secondary-source-dependent shorthand with a tax bridge, conditional loss-use screen, filing/payment separation and scoped outbound-payment triage. Future rate/loss proposals are not used as 2026 law. URLs and unresolved specialist rules are in `fi-corporate-income-tax.md`.

The Vero corporate sanctions page abbreviates its filing deadline as four months after the accounting period. The dedicated return page and foreign-business worked example specify four months after the end of the calendar month in which the period ends; the Guide uses that more precise rule.

The loss page's first worked example has an apparent English labelling error after reducing the business-source profit to zero. This batch does not reproduce that example. It uses separately stated same-source loss and ownership principles with hypothetical amounts. The full statutory loss chain remains an open review item.

## Existing Guide controls

- YEL: ETK's self-employed page rechecked for the standard rate and eligible startup reduction; other earlier substantive content is not represented as newly audited.
- VAT: Vero rates and self-assessed-tax late-filing page opened directly. Added controls for separate food/wine rates, assumed mixed-use reverse charge and an original late return. Original/replacement filing routes are distinguished. Earlier September operational source work is preserved and still needs full review.
- Prepayments: current indexed Vero instalment table re-read for two ordinary individual schedule controls. Other earlier operational rules remain open to full review.
- CbCR: full-report MyTax instructions directly opened; added an equality-boundary control. Filer role, current legislation, exchange conditions and local filing remain separate gates.

## Verification and outstanding work

At this local preparation stage, 27 executable checks across ten source Guides pass. Seven changed source Guides pass strict metadata audit against `915c5118`. Every substantive edited Guide advances its version; platform-owned fields are preserved. The README and overview are scope records, not extra tax-computation engines.

`2026-10-23-finland-source-reachability.json` records the HTTP audit with source-file hashes. The first scan found 87 unique non-CTA URLs, all returning HTTP 200, with only Vero's homepage redirecting to its individual landing page. Reachability is not evidence that the full legal content was read, the rule is current, or a navigation shell contains the cited statute. Later source edits require a refreshed snapshot.

Still open: complete current statutory/amendment reconciliation, specialist domain gaps in README, independent review of the entire pack, fixes from that review, one combined content push and exact-head CI, and a named Finnish accountant's review. No independent review, country completeness, live filing or professional approval is claimed by this record. Issue #392 remains open and PR #514 remains draft.

Final link snapshot: 86 unique non-CTA URLs, all HTTP 200 without redirects. The earlier 87th URL was the homepage removed when the overview became a topic router. The content validator initially warned about VAT's `Official sources` heading; renamed it to the recognised `Sources` heading and advanced the VAT version to 2.2. The source URL set was unchanged by that metadata/heading correction.

Repository verification: `TMPDIR=/private/tmp .../python -m unittest discover -s tests -p test_*.py -q` completed 129 tests successfully. The strict metadata audit against `915c5118` passed seven edited source Guides with no errors, warnings or notices. Full contributor validation passed, initially with the corrected VAT heading warning and an inherited Gibraltar 2024 freshness warning. No generated trees were edited, and no Finland content was pushed.
