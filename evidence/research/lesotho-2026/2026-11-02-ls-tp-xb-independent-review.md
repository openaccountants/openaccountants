# Lesotho TP and XB independent review (2026-11-02)

- Date: 2026-11-02
- Reviewer: independent AI review agent (no shared context with the writer)
- Files reviewed: `skills/lesotho/ls-transfer-pricing.md`, `skills/lesotho/ls-cross-border.md`, `skills/lesotho/README.md` (TP and XB rows only)
- Cross-checked against: `skills/lesotho/ls-corporate-income-tax.md`, `skills/lesotho/ls-income-tax.md`

## Sources opened by the reviewer (all fetched 2026-11-02 with curl, text layer extracted with pdftotext)

| Short name | URL | Date in or of the document |
|---|---|---|
| ITA | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf | consolidated to 1 April 2012 (PDF built October 2012) |
| WHT ruling | https://www.rsl.org.ls/sites/default/files/2026-09/Withholding%20Tax%20Public%20Ruling_2.pdf | text says "Date: April 2010"; PDF built June 2025, uploaded 2026-09 |
| WHT guide (older LRA brochure of the same ruling) | https://www.rsl.org.ls/sites/default/files/2024-05/Withholding%20Tax%20Guide_3.pdf | PDF built September 2015 |
| Automated WHT guide | https://www.rsl.org.ls/sites/default/files/2024-05/Automated%20Withholding%20Tax%20Guide_0.pdf | PDF built February 2023 |
| CIT guide | https://www.rsl.org.ls/sites/default/files/2024-07/Corporate%20Income%20Tax%20Guide.pdf | PDF built May 2017; mentions "LRA Banking Hall" |
| Provisional tax guide | https://www.rsl.org.ls/sites/default/files/2024-05/Tax%20Guide%20on%20Provisional%20Tax%20%281%29.pdf | PDF built November 2023 |
| Tech guide | https://www.rsl.org.ls/sites/default/files/2024-07/Guideline%20on%20Technical%20Services.pdf | PDF built 2018 |
| SA DTA (renegotiated) | https://www.rsl.org.ls/sites/default/files/2024-07/Agreement%20between%20Lesotho%20and%20Republic%20of%20South%20Africa.pdf | unsigned copy, PDF built 2016 |
| SA DTA (old, Order No 9 of 1993 era) | https://www.rsl.org.ls/sites/default/files/2024-07/Agreement%20between%20Lesotho%20and%20Republic%20of%20South%20Africa%201.pdf | checked only to identify it as the superseded text |
| FN note | https://www.rsl.org.ls/sites/default/files/2026-09/Taxation%20of%20Foreign%20Nationals.pdf | 27 January 2020 |
| Employment income guide 2026-27 | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Taxation%20of%20Employment%20Income%2026-27.pdf | April 2026 |
| RSL 2025-26 Integrated Annual Report | https://www.rsl.org.ls/sites/default/files/2026-10/2025%20-%202026%20Integrated%20Annual%20Report.pdf | 2026 |
| RSL pages: Withholding Tax, Tax Treaties, Income Tax, Tax Related Cases | https://www.rsl.org.ls/withholding-tax-0, https://www.rsl.org.ls/tax-treaties, https://www.rsl.org.ls/income-tax, https://www.rsl.org.ls/tax-related-cases | live 2026-11-02 |

## Figures and rules checked

| # | Item | Skill value (before review) | Source value | Source | Result |
|---|---|---|---|---|---|
| 1 | Associate definition | directions, requests, suggestions or wishes; no % test | same | ITA s.3(1) | match |
| 2 | Standard rate of tax | 25% | 25% | ITA s.3(1) | match |
| 3 | Year of assessment | 12 months to 31 March; company other period under s.49 | same (s.49 needs "compelling need") | ITA s.3(1), s.49 | match |
| 4 | Branch definition, incl. dependent agent, substantial equipment, construction project, no time limit | as stated | same | ITA s.3(1) | match |
| 5 | Individual residence tests (a) to (d) | as stated | same | ITA s.5(1) | match |
| 6 | Arrival year rule | days before first presence excluded | same | ITA s.5(2) | match |
| 7 | Departure year rule | ends if closer connection abroad | also requires non-residence in the following year | ITA s.5(3) | fixed (condition added) |
| 8 | Company residence (incorporation, management and control, majority of operations) | as stated | same | ITA s.6(1) | match |
| 9 | Branch treated as separate resident company | yes | yes | ITA s.6(2) | match |
| 10 | Partnership residence | any partner resident at any time | same | ITA s.7 | match |
| 11 | Manufacturing rate not for non-resident's branch | yes | yes | ITA s.10(2) | match |
| 12 | Third Schedule: 25% other income | 25% (item 4) | 25% | ITA Third Schedule | match |
| 13 | Third Schedule: manufacturing 10% | "item 3" | items 1 and 3 are 10%; item 2 0% (exports outside SACU, disputed by CIT guide) | ITA Third Schedule | fixed (items 1 and 3) |
| 14 | Non-resident assessed rate | 25% | standard rate | ITA s.12(1) | match |
| 15 | s.12(2) bands for non-resident full-time workers | "20% and 30%" cited to the 2012 Act | Act says Second Schedule rates; the 2012 copy shows 22%/35%; 20%/30% come from 2026 regulations (sibling ls-income-tax) | ITA s.12(2), Second Schedule; Employment guide 2026-27 | fixed (points to Second Schedule and ls-income-tax; notes the stale copy) |
| 16 | Non-resident gross income Lesotho-source only | yes | yes | ITA s.17(3) | match |
| 17 | Non-arm's length disposal at FMV; gift at greater of ACB and FMV | as stated | same | ITA s.61(2), (3) | match |
| 18 | Disguised dividends | as stated | same | ITA s.88 | match |
| 19 | Lesotho-source list | 12 bullets | s.103(1)(a) to (n); (c) and (m) omitted as "main categories" (acceptable) | ITA s.103 | match |
| 20 | Government contract services "wherever performed" | stated as law | the Act does not say "wherever performed"; RSL ruling Example 1 says no withholding where a Defence Force job was done outside Lesotho | ITA s.103(1)(b); WHT ruling Example 1 | fixed (removed; tension put on Not yet confirmed) |
| 21 | Foreign employment income exemption | if chargeable abroad | same | ITA s.104 | match |
| 22 | FTC cap and average rate definition; separate business and other baskets; soak-up excluded; FTC before ACT credit | as stated | same | ITA s.105(2), (3), (5), (6) | match |
| 23 | Tax havens; treaty partner never a tax haven | as stated | same | ITA s.106(1) to (3) | match |
| 24 | WHT on dividends, interest, royalties, natural resource payments, management charges to non-residents | 25% gross | 25% (standard rate); WHT ruling 25% | ITA s.107(1); WHT ruling s.107 table | match (2010/2026 ruling agrees with the Act) |
| 25 | Dividend out of concessional manufacturing income | 0% | no WHT | ITA s.107(2); WHT ruling | match |
| 26 | Manufacturing-use interest, royalty, management charge | 15% | 15% (Act); ruling names royalties only | ITA s.107(3); WHT ruling | match (difference in the ruling's wording noted in the skill) |
| 27 | Minister's Gazette exemption for interest | s.107(6) | same, with s.107(7) criteria | ITA s.107(6), (7) | match |
| 28 | Non-resident services contract | 10% gross, not management charges | 10%; s.108(2) excludes management charges; ruling 10% | ITA s.108; WHT ruling | match |
| 29 | WHT is final unless election; electing rate 40%; deduction limit | as stated | same; Fourth Schedule item 1 = 40% | ITA s.109; Fourth Schedule | match |
| 30 | Statement before other payments to non-residents | as stated | same | ITA s.110 | match |
| 31 | Branch profits tax 25% on repatriated income; formula; first out of branch income | as stated | same | ITA s.111 | match |
| 32 | Treaty powers and collection assistance | as stated | same | ITA s.112(1) to (3) | match |
| 33 | s.113(1) to (4) transfer pricing description | as stated | same wording; no "arm's length" in s.113 | ITA s.113 | match |
| 34 | GAAR s.114 (a) to (c) | as stated | same | ITA s.114 | match |
| 35 | Return due date | last day of third month; 30 June 2027 | same | ITA s.128(1) | match |
| 36 | Return of payments | 28 days after year end; company or partnership payer | same | ITA s.130 | match |
| 37 | Amendment window | 4 years; any time for fraud or gross or wilful neglect | same | ITA s.135(2) | match |
| 38 | Objection to amended assessment | later of 4 years from original and 60 days from amended; writing, detailed grounds | same | ITA s.137(2), (3) | match |
| 39 | Burden of proof on taxpayer | yes | yes | ITA s.141(1) | match |
| 40 | Tax due with return; 30 days after assessment notice; payable pending objection | as stated | same | ITA s.143(1) to (3) | match |
| 41 | Payer withholds s.107/108 payments | yes | yes | ITA s.161(1) | match |
| 42 | Certificate to non-employee payee on date of payment | yes | yes | ITA s.163(2)(b) | match |
| 43 | Agent personally liable, may recover from payee | yes | yes | ITA s.165(1) | match |
| 44 | Remittance time by regulations; RSL says monthly | yes | s.166(1); RSL WHT page "collected monthly or whenever there has been tax withheld"; Automated WHT guide: pay "immediately upon submission" | ITA s.166; RSL pages | match (filing steps added) |
| 45 | Records in Lesotho, Sesotho or English; deduction disallowed without records; keep while material | yes | yes | ITA s.169(1) to (3) | match |
| 46 | s.175(1) fine and imprisonment | M5,000 / 6 months | same | ITA s.175(1) | match |
| 47 | ss.178, 179, 180 fines | M10,000 / 2 years each | same | ITA ss.178 to 180 | match |
| 48 | Specified rate definition | CG publishes, from commercial lending rates | same | ITA s.192 | match |
| 49 | Late return, late payment, withholding additional tax | as stated | same | ITA ss.193, 194, 196 | match |
| 50 | Poor records: double the tax payable | yes | yes | ITA s.197 | match |
| 51 | False statements: double the excess | yes | yes | ITA s.198(1) | match |
| 52 | Remission; no s.197 additional tax after s.176 conviction | yes | yes | ITA s.199(2), (4) | match |
| 53 | Specified rate figure | 22% per twelve months (CIT guide, "undated") | CIT guide (PDF May 2017): 22% per twelve months; Provisional tax guide (PDF Nov 2023): 3% compounded monthly on unpaid instalments (s.194) | CIT guide 1.4; Provisional tax guide Q8 | fixed (newer RSL statement used, older noted; on Not yet confirmed) |
| 54 | SA DTA Art. 5(3)(a) construction PE | more than 6 months | same, incl. supervisory activity | SA DTA | match |
| 55 | SA DTA Art. 5(3)(b), (c) services PE | more than 90 days in any 12 months | 90 days aggregate in any twelve-month period commencing or ending in the fiscal year; (c) is an individual's independent services | SA DTA | match (wording completed) |
| 56 | SA DTA Art. 9(1), (2) | as stated | same | SA DTA | match |
| 57 | SA DTA Art. 10(2) dividends | 10% (company 10% of capital), 15% otherwise | same | SA DTA | match |
| 58 | SA DTA Art. 10(6) branch profits tax cap | 10% | 10% of repatriated income | SA DTA | match |
| 59 | SA DTA Art. 11(2) interest | 10% | 10% | SA DTA | match |
| 60 | SA DTA Art. 12(2) royalties | 10% | 10% | SA DTA | match |
| 61 | SA DTA Art. 13(2) technical fees; definition incl. managerial | 7.5% | 7.5%; Art. 13(3) technical, managerial or consultancy | SA DTA | match |
| 62 | SA DTA Arts. 11(6), 12(6), 13(6) special relationship | not stated | treaty rate only on the arm's length amount; excess taxable under domestic law | SA DTA | fixed (added; changes TP Example 2) |
| 63 | SA DTA Art. 4(3) dual-resident companies | "treaty tie-breakers" generally | no tie-breaker for non-individuals; MAP, otherwise no relief | SA DTA | fixed (added) |
| 64 | SA DTA Art. 29 entry into force | left to notifications | same: later notification; WHT from amounts paid 30 days after | SA DTA | match |
| 65 | 7.5% effective from 27 June 2016 | 27 June 2016 | "effective from the 27th June 2016" | Tech guide | match (EIF date itself not confirmable from the treaty text) |
| 66 | Treaty precedence | per FN note | "Where a treaty exists, provisions therein take precedence" | FN note, conclusion | match |
| 67 | Treaty list | SA, UK, Mauritius, Botswana, Eswatini; TIEAs Guernsey, Isle of Man | same (plus an SA VAT agreement) | RSL Tax Treaties page | match |
| 68 | WHT ruling DTA column | 5/10/12.5% dividends, 15% interest, 7.5% or 10% royalties and management fees | same in the 2026-09 upload; older 2015 brochure said 10%/15% dividends, 10% others (RSA and UK only) | WHT ruling; WHT guide 2015 | match (interest 15% vs SA 10% flagged in skill) |
| 69 | Gross amount before VAT | yes | Example 6 | WHT ruling | match |
| 70 | Services wholly outside Lesotho not Lesotho-source | yes | Example 1 | WHT ruling | match |
| 71 | Income Tax Amendment Bill for FY2026/27 | announced | "presentation of ... the Income Tax Amendment Bill ... in FY2026/27" | Annual Report 2025-26 | match |
| 72 | No TP regulations on RSL's list | none listed | none listed on Income Tax or Withholding pages; Tax Related Cases page has no TP case | RSL pages | match |
| 73 | README TP and XB rows | Ready, 2026, link to file | files exist, tax_year 2026 | README | match |

Figures and rules checked: 73 rows, plus 4 worked examples. Matches: 65. Fixed: 8 rows (7, 13, 15, 20, 53, 55, 62, 63) and 2 worked examples (TP 1, TP 2).

## Fixes made

1. Specified rate (both skills). The 22% rests on an RSL guide built in May 2017 (it still names the "LRA Banking Hall"). RSL's Provisional Tax guide (built November 2023) states additional tax on unpaid instalments at 3% a month compounded monthly; instalments fall under s.194 with the same specified rate. The more recent official text is used, the older one is quoted beside it, and the conflict sits on "Not yet confirmed". Row URL changed to the Provisional Tax guide.
2. TP Example 1 recomputed for 3% compounded monthly over 12 months: 375,000 x (1.03^12 - 1) = M159,660.33 (was M82,500 at 22%; the older figure kept in prose).
3. TP Example 2 rewritten for Article 13(6) of the South Africa agreement: the 7.5% cap covers only the arm's length M1,200,000; the M800,000 excess remains taxable under domestic law at the s.107 rate of 25%. Option A cost M490,000 (was M350,000); difference M400,000 (was M260,000).
4. TP rates row for 7.5% now carries the Article 13(6) condition; TP cross-border points mention Articles 11(6), 12(6), 13(6).
5. TP Third Schedule reference corrected to items 1 and 3; s.10(2) branch exclusion added.
6. TP branch bullet: s.113 needs both parties to be taxpayers and associates; condition added.
7. XB s.5(3) departure rule: added the "not resident in the following year" condition.
8. XB s.12(2): removed "20% and 30%" cited to the 2012 Act (which shows 22%/35%); now points to the Second Schedule and ls-income-tax for the 2026-27 bands.
9. XB s.103(1)(b): removed "wherever performed" (not in the Act; RSL's ruling Example 1 points the other way); conflict put on "Not yet confirmed".
10. XB company residence: added SA treaty Article 4(3) (no tie-breaker for companies).
11. XB SA rates rows: special-relationship limits (Arts. 11(6), 12(6), 13(6)); PE row wording completed.
12. XB ruling bullet: notes that the ruling's interest DTA rate (15%) exceeds the SA treaty's 10% and that the ruling names only royalties for the 15% domestic rate.
13. XB filing: added the RSL automated WHT steps (registration, emailed Excel schedule, WHTSubmission@rsl.org.ls, immediate payment, e-certificate) from the Automated WHT guide.
14. Sources tables: WHT ruling dated April 2010 in its own text; CIT guide dated May 2017; Provisional Tax guide and Automated WHT guide added; SA treaty articles read updated.

## Examples recomputed by hand

| Example | Recomputation | Result |
|---|---|---|
| TP 1 distributor | (0.04 - 0.01) x 50,000,000 = 1,500,000; x 25% = 375,000; x (1.03^12 - 1 = 0.4257609) = 159,660.33 | fixed (was 82,500 at 22%) |
| TP 2 management fee | A: 7.5% x 1,200,000 = 90,000 + 25% x 800,000 = 200,000 WHT = 290,000; CIT 25% x 800,000 = 200,000; total 490,000. B: 90,000. Difference 400,000 | fixed (was 350,000 / 260,000, which ignored Art. 13(6)) |
| XB 1 branch profits | 25% x 4,000,000 = 1,000,000; 4,000,000 - 1,000,000 - 600,000 = 2,400,000; x 25% = 600,000; x 10% = 240,000; totals 1,600,000 and 1,240,000; saving 360,000 | match |
| XB 2 FTC | 25% x 10,000,000 = 2,500,000; average rate 25%; cap 25% x 2,000,000 = 500,000; credit min(600,000, 500,000) = 500,000; net 2,000,000; unrelieved 100,000 | match |

`python3 scripts/check-examples.py --require` on both files: 2 blocks each, 0 failures. `skill_checks.run_all` on both files: `{}`.

## Sibling skill notes (not edited)

- `ls-corporate-income-tax.md` states the additional tax rate as 22% per twelve months from the 2017 CIT guide; RSL's November 2023 Provisional Tax guide states 3% a month compounded. It should be revisited in its own PR.
- `ls-corporate-income-tax.md` cites the WHT ruling for "Interest to residents 10%" etc.; fine, but that ruling's text is dated April 2010.

## Still not confirmed

- The currently published s.192 specified rate (two RSL guides disagree; no rate notice found).
- Amendments to the Income Tax Act after 1 April 2012 not in RSL's consolidated copy (proven to exist: the 2026 individual bands differ from the copy's Second Schedule), and whether the FY2026/27 Income Tax Amendment Bill changes s.107, s.108, s.111 or s.113.
- Entry-into-force date of the renegotiated SA agreement (only the RSL guide's 27 June 2016 effective date).
- Statutory basis for treaty precedence (practice note only).
- Remittance regulations under s.166.
- UK, Mauritius, Botswana and Eswatini treaty texts (not read by the writer or reviewer).
- Whether s.103(1)(b) reaches Government-contract services performed outside Lesotho.
- Revenue Appeals Tribunal decisions on s.113.

## Unreachable sources

- lesotholii.org judgment pages: HTTP 403 (Cloudflare check) on https://lesotholii.org/akn/ls/judgment/lsrat/2022/1/eng@2022-12-16; not bypassed. The RAT s.113 decisions and any amending Acts or Gazettes on LesLII were not read.
