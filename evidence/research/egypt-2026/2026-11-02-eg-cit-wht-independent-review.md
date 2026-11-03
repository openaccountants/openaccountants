# Independent review: eg-corporate-tax and eg-withholding-tax (tax year 2026)

Reviewer: independent AI review agent (Claude), no shared context with the writer. Review date: 2026-11-02. Rule: `docs/skill-template.md` line 12 (second reader) and line 5 (no lost rule).

Files reviewed (uncommitted, branch `pack/eg`): `skills/egypt/eg-corporate-tax.md` (v0.2), `skills/egypt/eg-withholding-tax.md` (v0.2). Old versions: `upstream/main`. The writer's notes (`2026-11-02-eg-cit-wht-source-notes.md`) were used only to find pages.

## Sources re-read by the reviewer

All downloaded fresh from eta.gov.eg on 2026-11-02 into the reviewer's own scratch folder (not the writer's cache). Scanned files were rendered with `pdftoppm` and read as page images; text-layer files were read after Unicode normalisation. No CAPTCHA or bot check was met.

| Source | URL | What the reviewer read |
|---|---|---|
| Law 91/2005, Gazette 23 cont., 9 Jun 2005 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf | PDF p. 15 to 20 (arts. 21 to 29), 29 to 36 (arts. 47 to 63) |
| Executive Regulations, decree 991/2005 | https://eta.gov.eg/sites/default/files/2024-03/law_no.991-2005.pdf | PDF p. 27, 28 (arts. 57 to 60), 30, 31 (arts. 63 to 69), 34 to 37 (arts. 74 to 84) |
| Law 53/2014 | https://eta.gov.eg/sites/default/files/2024-03/law_no.53-2014.pdf | PDF p. 1 (article list), 3 to 6 (arts. 50, 59 first para., 59 bis to 59 bis 2, 72, 73, 86, 135, 138) |
| Law 96/2015 | https://eta.gov.eg/sites/default/files/2024-03/law_no.96-2015.pdf | PDF p. 2 (art. 49 first para., 56 bis 2015 text) |
| Law 30/2023 | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf | Arts. 3, 4, 22, 50, 52, 56, 56 bis, 58, 72 bis; transitional arts. 3 to 12 |
| Law 151/2026, Gazette 30 bis (a), 28 Jul 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf | Whole text |
| Law 206/2020 | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | PDF p. 17 to 20 (arts. 31 to 34), 38 to 40 (arts. 67 to 75) |
| Law 7/2025 | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf | Whole text |
| ETA circular 1/2026 | https://eta.gov.eg/sites/default/files/2026-03/Dawry.no_.1.of_.2026.pdf | Whole page |
| ETA Services Guide, 2nd ed. | https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf | Service 5/1 (p. 97 to 100), 8/1 (p. 133 to 136), Law 6/2025 service (p. 246, 247) |
| ETA withholding forms page and form 41 xlsx | https://www.eta.gov.eg/ar/content/nmadhj-aqrarat-alkhsm-walthsyl | Link list; form 41 column headings |

## Items checked

Result key: M = matches; F = fixed; N = moved to or kept on "Not yet confirmed". CIT = eg-corporate-tax, WHT = eg-withholding-tax.

| # | Item | File | Source location | Result |
|---|---|---|---|---|
| 1 | Residents on worldwide profit, National Service Projects Organisation excluded; non-residents on PE profit | CIT | Law 91 art. 47, G. p. 30 | M |
| 2 | List of legal persons | CIT | Law 91 art. 48, G. p. 30 | M |
| 3 | Civil companies treated as partnerships | CIT, WHT | Law 151 art. 56 bis | M |
| 4 | Exempt bodies list, items 1 to 6, 11, 12, 14 to 18; exemption cannot create a loss | CIT | Law 30/2023 art. 50 | M |
| 5 | PE definition, 90 days in 12 months, services, dependent agent | CIT | Law 30/2023 art. 4 | M |
| 6 | 22.5%, base rounded down to EGP 10 | CIT | Law 96/2015 art. 49 first para. | M |
| 7 | 40% Suez Canal Authority, EGPC, Central Bank; 40.55% oil and gas | CIT | Law 91 art. 49 second para., G. p. 30 | M (whether later amended: N, kept) |
| 8 | Thin cap 2:1 statutory; exclusion for banks, insurers, designated finance companies | CIT | Law 30/2023 and Law 151 art. 52 item 1 | F: row dated "From 29 Jul 2026"; 2:1 has stood since Law 30/2023, Law 151 re-enacts it |
| 9 | Transitional 4:1 (2023), 3:1 (2024 to 2027), 2:1 (2028); not repealed by Law 151 | CIT | Law 30/2023 art. 5; Law 151 art. 6 | M |
| 10 | Infrastructure 4:1 with three conditions and end date | CIT | Law 151 art. 52 item 1 second para. | M |
| 11 | Participation exemption 25%, two years or undertaking, resident and non-resident subsidiaries, no 10% add-back | CIT | Law 151 art. 50 item 10; Law 30/2023 art. 50 item 10 | M |
| 12 | Resident-company dividends excluded from the CIT base with related cost | CIT | Law 151 art. 56 bis | M |
| 13 | Listed gains exempt, losses not deductible, delisting exception; art. 46 bis 5 repealed | CIT | Law 151 art. 50 item 7, art. 6 | M |
| 14 | Unlisted gains: Egypt or abroad; price less cost and brokerage; non-resident pays in 60 days; fair value uplift after three years; weighted average | CIT, WHT | Law 151 arts. 46 bis 3, 46 bis 4 | M |
| 15 | Non-resident T-bill gains outside the tax | WHT | Law 151 art. 46 bis 3 | M |
| 16 | Dividend tax 10%, 5% listed, no costs, not bonus shares | CIT, WHT | Law 151 art. 56 bis | M |
| 17 | PE profits deemed distributed within 60 days of year end | CIT, WHT | Law 151 art. 56 bis | M |
| 18 | Second resident-dividend exclusion (dividend tax base) | WHT | Law 151 art. 56 bis | M (reach: N, kept) |
| 19 | Dividend tax remittance, five working days, central department | WHT | Law 151 art. 56 bis | M |
| 20 | Listing incentive 15%, three years, EGP 50 bn, 20% or EGP 10 bn, once, no stacking | CIT | Law 151 art. 3 | F: "from listing" is "from the offering"; added FRA prospectus condition and ministerial extension |
| 21 | Law 151 in force day after publication (29 Jul 2026) | CIT, WHT | Law 151 art. 7 | M (whole-year question: N, kept; art. 5 waiver of unpaid listed-gains tax up to commencement noted) |
| 22 | Depreciation 5%, 10%, pools 50% and 25%, no depreciation on land and art | CIT | Law 91 art. 25, G. p. 19 | M |
| 23 | Pool basis, EGP 10,000 write-off | CIT | Law 91 art. 26 | M |
| 24 | 30% initial allowance, regular books | CIT | Law 91 art. 27, G. p. 20 | M |
| 25 | Bad debt conditions, 12 months, three serious steps, EGP 10,000 and 1% | CIT | Law 91 art. 28; Law 151 art. 28 item 4 | F: added the registered accountant's report required by art. 28 first para. |
| 26 | Loss carry-forward five years, no carry-back | CIT | Law 91 art. 29 | F: added art. 21 long-term contract loss carry-back exception |
| 27 | Arm's length | CIT | Law 91 art. 30 | M |
| 28 | Net profit per Book Two rules | CIT | Law 91 art. 51 | M |
| 29 | Add-backs: provisions, 80% bank loan provisions, insurers' technical provisions, dividends, attendance fees, board pay, employee share | CIT | Law 91 art. 52 items 2 to 6, G. p. 32, 33 | M |
| 30 | Art. 24 non-deductibles | CIT | Law 91 art. 24, G. p. 18 | F: writer had left unread; now listed (2005 text) |
| 31 | Donations, taxes and fees, health insurance contribution | CIT | Law 91 art. 23 items 3, 7, 8; Law 151 art. 23 item 10 | F: restored (lost content) |
| 32 | Costs need e-invoices (Jul 2023) and e-receipts (Jan 2025) | CIT | Law 30/2023 art. 22 item 2 | M |
| 33 | Interest and equity definitions, average formula | CIT | Exec. Regs arts. 58, 59 | F: exclusion of loans whose interest is not taxable added; "interest-free grace period" corrected to a grace period for paying interest |
| 34 | Change of legal form neutrality, list of changes | CIT | Law 91 art. 53; Exec. Regs art. 64 | M |
| 35 | Foreign tax credit, per country, losses abroad excluded | CIT | Law 91 art. 54; Exec. Regs arts. 66, 67 | M |
| 36 | Loss lapse needs all three conditions | CIT | Law 91 art. 55; Exec. Regs art. 68 | F: added three-year look-forward rule and art. 69 anti-avoidance; listing test scope |
| 37 | Long-term contracts, percentage of completion | CIT | Law 91 art. 21, G. p. 16, 17 | F: restored from old skill (was on Not yet confirmed) |
| 38 | Head office charges 7% cap, auditor's certificate, no royalties, interest, commissions | CIT, WHT | Exec. Regs art. 74 | M |
| 39 | Advance payments 60%, estimate if no return or a loss, three instalments 30 Jun, 30 Sep, 31 Dec, reduce or skip third | CIT, WHT | Law 91 arts. 61, 63 | M |
| 40 | Advance payment application 60 days before; ETA 60 days, silence is refusal | CIT, WHT | Law 91 art. 62; Exec. Regs arts. 83, 84 | M |
| 41 | Art. 60 exemption from deduction | CIT, WHT | Law 91 art. 60, G. p. 36 | F: added the regular-records condition |
| 42 | Yield on instalments at the Central Bank rate | CIT | Art. 63 fourth para.; circular 1/2026; Guide 8/1 | F: "first two instalments" sits in the Guide, not the circular; citation corrected |
| 43 | Guide: 6, 9, 12 months; renewal to period end; return to deduction after two losses, form change, 20% gap | CIT, WHT | Guide 8/1, p. 135 | F: losses must be two consecutive periods |
| 44 | Central Bank rate 20.50% on 1 Jan 2026; delay charge rate + 2% = 22.50%; part months and pounds dropped | CIT, WHT | Circular 1/2026; Law 91 art. 110 | M |
| 45 | Delay charge cap 100% | CIT, WHT | Law 7/2025, Law 206 art. 45 bis | M |
| 46 | Annual return before 1 May or four months after year end; due for exempt periods; tables complete | CIT | Law 206 art. 31(c), G. p. 18 | M |
| 47 | Accountant signature, turnover over EGP 2 million | CIT | Law 206 art. 31(d) last para., G. p. 19 | M |
| 48 | Cessation and transfer returns, 60 days | CIT | Law 206 art. 31(d) | M |
| 49 | E-filing; payment same day net of withholding, advance payments and yield | CIT | Law 206 art. 32 | M |
| 50 | Amended return within a year; 30 days counts as original; public sector 30 days | CIT | Law 206 art. 33 | F: added loss of the right on evasion or audit notice |
| 51 | Fine 3,000 to 50,000, trebled on repeat | CIT, WHT | Law 206 art. 69 | M |
| 52 | Fine 5,000 to 200,000 over 60 days, doubled within three years | CIT, WHT | Law 206 art. 70 | M |
| 53 | Fine 20,000 to 100,000; up to 50,000 for books | CIT | Law 206 art. 71 | M |
| 54 | Evasion prison one to three years, 50,000 to 250,000 | CIT | Law 206 art. 72 | M |
| 55 | Managers liable | CIT, WHT | Law 206 art. 73 | M |
| 56 | Settlement 100%, 150%, 175% | CIT | Law 206 art. 75 | M |
| 57 | Non-tax crimes settlement half to twice the minimum | CIT | Law 206 art. 75 bis (Law 7/2025) | M |
| 58 | Art. 135 settlement 12.5% plus amounts and delay charge | WHT | Law 206 art. 75 bis 1 (Law 7/2025) | M |
| 59 | Art. 56: 20% on interest, royalties (industry know-how exception), services (PE head office cost exception), athletes and artists; payers; 15 days | WHT | Law 91 art. 56, G. p. 34 | M |
| 60 | Government foreign loans exempt | WHT | Law 30/2023 art. 56 third para. | M |
| 61 | Infrastructure loan exemption, five years, unrelated lenders, 25% | WHT | Law 151 art. 56 fourth para. | M |
| 62 | Continued exemption for loans with interest paid before Law 30 | WHT | Law 30/2023 art. 6 | F: covers public sector, public business sector and private sector companies, not only private sector |
| 63 | Old exemption needed three years | WHT | Law 91 art. 56 (2005); Exec. Regs art. 75 | M |
| 64 | Commission to unconnected individuals, art. 56 rate, 15 days, form 14 | WHT | Law 91 art. 57; Exec. Regs art. 79 | M |
| 65 | T-bill interest 20%, next day | WHT | Law 30/2023 art. 58 second para. | M |
| 66 | Form 11 (art. 56), form 12 (free zone), form 13 | WHT | Exec. Regs arts. 76, 77 | M |
| 67 | Art. 59 payers list, partnerships over EGP 50,000 | WHT | Law 91 art. 59, G. p. 36 | F: citation (list is 2005 text; only the first para. was replaced in 2014) |
| 68 | Art. 59 over EGP 300, rate up to 5% by decree, insurance excepted, dividends of capital companies | WHT | Law 53/2014 art. 59 first para. | M (rate decree: N, kept) |
| 69 | Payer that fails to deduct owes amounts and delay charge | WHT | Law 91 art. 59 last para. | F: art. 72 removed from the citation (Law 53/2014 art. 72 is the salary-payer article) |
| 70 | Quarterly remittance end of April, July, October, January; records | WHT | Law 53/2014 art. 86; Exec. Regs art. 82 | M |
| 71 | No deduction in exemption period except arts. 59 to 59 bis 2 | WHT | Law 53/2014 art. 73 | M |
| 72 | Arts. 59 bis to 59 bis 2 | WHT | Law 53/2014, G. p. 5 | F: the Not-yet-confirmed line called them a collection system with rates; the text sets quarterly reporting duties; body now states them |
| 73 | 25% fine for failing to withhold or remit | WHT | Law 53/2014 art. 135 | M |
| 74 | Non-original employer 10% | WHT | Law 30/2023 art. 72 bis | M |
| 75 | Art. 3(ي) source rule | WHT | Law 30/2023 art. 3 | M |
| 76 | Treaty refund procedure, documents, 45 days, delay charge | WHT | Guide 5/1 | M |
| 77 | Form list and form 41 fields | WHT | Forms page; form 41 xlsx | M |
| 78 | Law 6/2025 regime: no deduction either way; threshold | CIT, WHT | Guide p. 246 | F: "under EGP 20 million" is "up to EGP 20 million" (لا يتجاوز) |
| 79 | Portal workspace.eta.gov.eg | CIT, WHT | HTTP 200 only, not read | M (link only) |

Totals: 79 items checked; 61 matched; 18 fixed (items 8, 20, 25, 26, 30, 31, 33, 36, 37, 41, 42, 43, 50, 62, 67, 69, 72, 78). Items that match but keep a Not-yet-confirmed note are counted as matched. Items newly moved to "Not yet confirmed": 0; existing entries kept after review: 5 (items 7, 18, 21, 68 and the post-2005 amendment question, which the reviewer narrowed).

Validation after fixes: `python3 scripts/check-examples.py --require` on both files: 4 oa-check blocks, 0 failures. `python3 scripts/validate-guides.py --no-index-check`: passed. `scripts/skill_checks.py` (a) to (o): all pass on both files.

## Content loss (line 5)

Old files: CIT 233 lines / 13,492 bytes, WHT 205 lines / 13,119 bytes. New files are larger (CIT 23 KB, WHT 22 KB), so the 25% shrink rule does not trigger, but old against new was compared item by item.

Restored from the old CIT skill, now checked against the law: (1) donations rule (old 5% cap corrected to 10%, art. 23 item 8, and unlimited to government, item 7); (2) fines add-back (narrowed to art. 24 item 2); (3) income tax not deductible (art. 24 item 3); (4) reserves not deductible (art. 24 item 1); (5) construction contracts by percentage of completion (art. 21, previously on Not yet confirmed). Old WHT items (rents to non-residents, timing of deduction, refund limits, software rule, record retention, annual reconciliation, treaty table, participation relief) are all carried on the WHT Not-yet-confirmed line or correctly dropped as contrary to the law; none lost. Old CIT "real estate tax not deductible" is contrary to art. 23 item 3 (taxes other than income tax are deductible) and now stated correctly.

Lost content restored: 5

## Example recomputations (by hand, Decimal)

CIT case 1: tax depreciation 2,400,000 x 25% = 600,000. Taxable 10,000,000 + 500,000 + 800,000 - 600,000 = 10,700,000 (already a multiple of 10). Tax 10,700,000 x 22.5% = 2,407,500. Payable 2,407,500 - 150,000 = 2,257,500. Matches.

CIT case 2: limit 20,000,000 x 3 = 60,000,000. Disallowed interest (80,000,000 - 60,000,000) x 15% = 3,000,000. Extra tax 3,000,000 x 22.5% = 675,000. At 2:1 (2028, Law 30/2023 art. 5): (80,000,000 - 40,000,000) x 15% = 6,000,000. Equity alternative: 40,000,000 x 3 = 120,000,000 limit against 60,000,000 of loans, all deductible. Matches; the decision is worked both ways.

WHT case 1: royalty 1,000,000 x 20% = 200,000; dividend 5,000,000 x 10% = 500,000; net 6,000,000 - 700,000 = 5,300,000; listed 5,000,000 x 5% = 250,000. Matches.

WHT case 2: delay 200,000 x 22.5% x 5/12 = 18,750. Settlement 200,000 + 18,750 + 25,000 = 243,750. Fine route 200,000 + 18,750 + 50,000 = 268,750. Saving 25,000. Matches.

## Still open

Whether ETA applies the Law 151/2026 base changes to all of 2026 or only from 29 July 2026; whether Law 30/2023 art. 5 (3:1) keeps running after Law 151 re-enacted art. 52 item 1; the art. 59 rate decree; post-2005 amendments to arts. 21 and 23 to 27 by laws not read; reach of the second resident-dividend exclusion; treaty relief at source.
