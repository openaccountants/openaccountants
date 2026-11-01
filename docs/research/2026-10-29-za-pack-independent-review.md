# South Africa pack: independent review (rule 9)

- Date: 2026-10-29
- Reviewer: independent AI review agent (no shared context with the writer)
- Files reviewed: `skills/international/south-africa/za-corporate-income-tax.md`, `skills/international/south-africa/za-payroll-paye-uif-sdl.md`, `skills/international/south-africa/README.md`
- Writer's notes (`docs/research/2026-10-29-za-pack-source-notes.md`) were treated as claims, not evidence. Every source below was re-fetched or re-read by the reviewer on 2026-10-29.

## Sources re-read

| Source | How read |
|---|---|
| SARS, Companies, Trusts and SBC rates (page updated 28/10/2026) | curl, text extracted |
| SARS, Rates of Tax for Individuals (page updated 28/10/2026) | curl, text extracted |
| SARS, Budget 2026 FAQs | curl, text extracted |
| SARS FAQ, ITR14 submission | curl |
| SARS, Corporate Income Tax page (2 Feb 2026 enhancements) | curl |
| SARS, UIF page; SARS, SDL page; SARS, PAYE page | curl |
| SARS PAYE-GEN-01-G21 (2027), Revision 1, 42 pages | PDF downloaded, pdftotext |
| Income Tax Act 58 of 1962, SARS consolidation to GG 55220 of 19 Aug 2026: s1 ("company", "resident"), s5(2), s6, s6A, s7B, s10(1)(k)(i), s11F, s12E, s20, s64E, s64F, s89bis(2), s89quat(1)–(2); Fourth Schedule paras 1, 2(1)–(4), 6(1), 9, 13(2), 20, 23, 23A, 27 | sars.mylexisnexis.co.za in the built-in browser (iframe text via `redirectToDomainId`) |
| Tax Administration Act 28 of 2011, SARS consolidation to GG 54447 of 1 Apr 2026: ss29, 32, 210, 211, 213 | same |
| Skills Development Levies Act 9 of 1999, consolidation to GG 51828: ss3, 4, 6 | same |
| Unemployment Insurance Contributions Act 4 of 2002, consolidation to GG 51828: s1 "remuneration", ss4, 6, 7, 8, 13 | same |

## Figures checked

### za-corporate-income-tax

| Item | Skill value | Source value | Source | Result |
|---|---|---|---|---|
| Company rate YAs ending 1 Apr 2026–31 Mar 2027 | 27% | 27% | SARS rates page; Budget FAQ | match |
| Rate history (27% from YAs ending 31 Mar 2023; 28% before) | as stated | as stated | SARS rates page | match |
| SBC band 1 | 0% to R99 000 | 0% to R99 000 | SARS rates page; Budget FAQ | match |
| SBC band 2 | 7% above R99 000 to R365 000 | same | SARS rates page | match |
| SBC band 3 | R18 620 + 21% above R365 000 to R550 000 | same | SARS rates page | match |
| SBC band 4 | R57 470 + 27% above R550 000 | same | SARS rates page | match |
| SBC 2025/26 bands | R95 750 / R18 848 / R57 698 | same | SARS rates page | match |
| SBC fixed amounts derivation | 18 620; 57 470 | 266 000 x 7%; +185 000 x 21% | arithmetic | match |
| SBC gross income ceiling | R20m, pro rata, part month = full | same | ITA s12E(4)(a)(i) | match |
| SBC 20% investment/personal service test | not more than 20% | same | s12E(4)(a)(iii) | match |
| "Investment income" definition | dividends, royalties, rent, annuities | also foreign dividends, s24J interest, s24K, proceeds of trading in instruments/securities/immovable property | s12E(4)(c) | fixed |
| "Personal service" definition | not stated | listed professions, performed by holder/connected person, unless 3+ full-time unconnected employees | s12E(4)(d) | added for accuracy of test 4 |
| SBC shareholder tests, exceptions (listed, CIS, <5% co-ops, friendly societies, s12J, dormant R5 000, s41(4)) | as stated | same | s12E(4)(a)(ii) | match |
| PSP never an SBC | yes | yes | s12E(4)(a)(iv) | match |
| s12E(1) 100% manufacturing allowance | as stated | also excludes mining/farming trades | s12E(1) | fixed (wording) |
| s12E(1A) 50/30/20 election | as stated | same | s12E(1A) | match |
| s12E(2) cost cap | "capped at arm's-length cash price" | lesser of actual cost and arm's-length cash price incl. direct installation | s12E(2) | fixed (wording) |
| s12E(3B) no deduction where s12BA granted | as stated | same | s12E(3B) | match |
| Assessed loss cap | higher of R1m and 80% of TI before s20 | same | s20(1)(a)(i) | match |
| Cap lifted on s41(4) liquidation steps | as stated | same | proviso to s20(1)(a) | match |
| Foreign trade losses ring-fenced | as stated | same | s20(1) proviso (b) | match |
| Assessed loss definition | s11 deductions exceed income | same | s20(2) | match |
| "carries forward ... while the company keeps trading" | as stated | s20 has no time limit; set-off is against income from carrying on a trade; s20(2A)(b) only for non-companies | s20(1), (2A) | fixed (reworded to statute) |
| Residence test for companies; treaty exclusion; cessation | as stated | same | s1 "resident" (b) and proviso | match |
| CCs and co-operatives are companies | yes | "company" includes co-operatives (c) and close corporations (f) | s1 "company" | match |
| Dividends tax | 20%, Minister may change | same | s64E(1)(a) | match |
| Dividend exemption (normal tax) | body claim marked unread | exempt, with provisos (headquarter co., REITs etc.) | s10(1)(k)(i) | confirmed; citation added; removed from not-confirmed |
| Dividends tax exemption for resident company | body claim marked unread | exempt (non-in-specie) where beneficial owner is a resident company | s64F(1)(a) | confirmed; citation added; removed from not-confirmed |
| Late-payment interest | 10.25% from 2 Mar 2026 | same | Budget FAQ | match |
| Refund interest on overpaid provisional tax | 6.25% | same | Budget FAQ | match |
| Underestimation penalty, TI > R1m | 20% x (tax on 80% TI less paid) where estimate < 80% | same | Fourth Sch. para 20(1)(a) | match |
| Underestimation, TI <= R1m | "90% test, compared against basic amount" | estimate < 90% and < basic amount; 20% of (lesser of tax on 90% and tax on basic amount, less paid) | para 20(1)(b) | fixed (made precise) |
| Para 20 penalty reduced by para 27 penalty; remission | not stated | para 20(2B), 20(2) | para 20 | added |
| Late provisional tax penalty | 10% | 10% | para 27(1); TAA s213 | match |
| First payment | 6 months after start; half of estimate less PAYE and s6quat | same | para 23(1)(a) | match |
| Second payment | last day of YA | same | para 23(1)(b) | match |
| First payment skipped for YA <= 6 months | yes | yes | para 23(2) | match |
| Top-up payment | optional, to reduce s89quat interest | same | para 23A(1) | match |
| s89quat effective date | listed as not confirmed | 7 months after year end (Feb year-end company), 6 months otherwise; R20 000 company threshold | s89quat(1)–(2) | added; removed from not-confirmed |
| ITR14 deadline | 12 months after year end | same | SARS ITR14 FAQ | match |
| Worked dates (31 Aug 2026; 28 Feb 2027; 28 Feb 2028) | as stated | consistent | para 23; ITR14 FAQ | match (effective date 30 Sep 2027 added) |
| Record keeping | 5 years (cited to PAYE guide) | 5 years from submission; audit/objection extension | TAA ss29(3)(a), 32 | fixed (citation moved to statute; PAYE guide removed from CIT sources) |
| TAA s210 scope | public notice | also excludes percentage-penalty late payment, understatement and s212 cases | TAA s210(2) | wording added |
| TAA s211 table (8 rows, R250 to R16 000) | as stated | same | TAA s211(1) | match |
| s211(2) increments, 35/47 months | as stated | same | TAA s211(2) | match |
| s211(3) placement in item (vii) | "a level set in s211(3)" (threshold not confirmed) | listed cos; gross receipts > R500m; group members; except item (viii) or non-trading | TAA s211(3) | fixed; removed from not-confirmed |
| WHT royalties / interest / entertainers / immovable property (company) | 15% / 15% / 15% / 10% | same | Budget FAQ | match |
| SEZ 15% (SARS says may qualify) | as stated | same | Budget FAQ | match |
| s6quat carry-forward in ITR14 from 28 Feb 2026 | as stated | effective 28 Feb 2026 | SARS CIT page | match |
| PSPs taxed as company or trust | as stated | same | SARS rates page | match |
| Budget rate changes legal basis | not stated | 12 months subject to Parliament | ITA s5(2) | added |

### za-payroll-paye-uif-sdl

| Item | Skill value | Source value | Source | Result |
|---|---|---|---|---|
| 2027 tax table, 7 bands and fixed amounts | as stated | identical | SARS individuals page; G21 quick reference card; Budget FAQ | match (7 rows) |
| Primary / secondary / tertiary rebate 2027 | R17 820 / R9 765 / R3 249 | same | SARS page; G21 | match |
| Prior-year rebates | R17 235 / R9 444 / R3 145 | same | SARS page; also ITA s6(2) consolidation | match |
| Thresholds 2027 | R99 000 / R153 250 / R171 300 | same (and = rebates / 18%) | SARS page; G21 | match |
| 2026 threshold under 65 | R95 750 | same | SARS page | match |
| Medical credits | R376 / R376 / R254 | same | G21 | match; ITA s6A(2)(b) consolidation still shows R364/R728/R246, but s6A(5) gives the Budget announcement legal effect — noted in skill |
| Legal basis of 2027 bands/rebates/credits | not stated | Budget announcement for 12 months subject to Parliament | ITA ss5(2), 6(6), 6A(5) | added |
| Retirement fund cap | R430 000 | Act: R350 000 (s11F(2)(a), no announcement clause); SARS G21 and Budget FAQ: R430 000 | ITA s11F(2) | fixed to R350 000 per rule 2; R430 000 moved to not-confirmed; example updated (result unchanged) |
| 27.5% of higher of remuneration / taxable income, limited to TI | as stated | same | s11F(2)(b),(c); G21 | match (third limb added) |
| Medical credit deduction condition | "if paid through the payroll" | employer pays fees, or at employer's option on proof of payment | Fourth Sch. para 9(6) | fixed |
| Annual equivalent formula | as stated | same | G21; para 9(1)–(2) | match |
| PAYE balance of remuneration after retirement contributions | as stated | same | para 2(4)(a) | match |
| Who must deduct PAYE | "an employer" | resident employer, non-resident with PE, representative employer | para 2(1) | fixed |
| Directors as employees | "count as employees under para 1" | para 1 "employee" (a) covers any person receiving remuneration; G21 confirms directors | para 1; G21 | reworded |
| s7B variable remuneration accrues on payment | as stated | same | s7B(2); G21 | match |
| UIF employee / employer rate | 1% / 1% | same | UIC Act s6(1)(a)(i)–(ii) | match |
| UIF ceiling | R17 712 / R212 544 from 1 Jun 2021 | same | SARS UIF page; G21; s6(2) note names GN 475, GG 44641 of 28 May 2021 | match (notice reference added) |
| UIF max deduction | R177.12 | same | SARS UIF page | match |
| UIF exclusions | 4 groups | same | UIC Act s4(1)(a),(c),(e),(f) | match |
| UIF remuneration definition | "as defined for UIF" | para 1 remuneration excluding pensions, gross-income paras (a),(cA),(d),(e),(eA),(eD), and commission | UIC Act s1 | added |
| UIF deduction timing, arrears, liability, s7(4A) | as stated | same | UIC Act s7 | match |
| UIF registration rule | "registered for PAYE or SDL" | registered for employees' tax; UI Commissioner if not required/voluntary for employees' tax and not liable for SDL | SARS UIF page; G21 | fixed |
| UIF payment | 7 days | same | UIC Act s8(1) | match (citation corrected from ss7, 8) |
| UIF penalty 10% | yes | yes | UIC Act s13(1) | match |
| SDL rate 1% | yes | yes | SDL Act s3(1)(a)(ii) | match |
| SDL leviable amount | "total monthly remuneration"; example on gross pay | remuneration as determined under Fourth Schedule (s3(3)); G21: balance after retirement contributions and donations | SDL Act s3(3); G21 | fixed; example 2 edge R150 -> R135; statutory reading flagged in not-confirmed |
| SDL exclusions s3(4)(a)–(c) | as stated | same | SDL Act s3(4) | match |
| SDL exemptions incl. R500 000 | as stated | same | SDL Act s4(a)–(e) | match |
| SDL payment 7 days; return with payment | as stated | same | SDL Act s6(1), (2) | match |
| SDL return within 14 days on ceasing | as stated | same | SDL Act s6(2A)(b) | match (UIC Act s8(2A)(b) added) |
| Weekend/holiday rule | last business day before | same | G21; SARS UIF/SDL/PAYE pages | match |
| Electronic filing threshold | R10m in 12 months | same | SARS PAYE page | match |
| Certificate within 14 days on leaving | "when an employee dies" | any cessation while still an employer of others (death, resignation, retirement) | para 13(2)(b); SARS PAYE page | fixed |
| Record keeping 5 years | G21 | same | TAA ss29(3)(a), 32 | match (statute added) |
| Late-payment penalty 10% | yes | yes | Fourth Sch. para 6(1); UIC Act s13(1); TAA s213 | match |
| Intent to evade up to 2x | yes | yes | G21 | match |
| Payment allocation penalty, interest, tax | yes | yes | G21 | match |
| Estimated assessments | TAA ch. 8; UIC Act s9A | same | G21 | match |
| UIF offences, fine or up to 2 years | yes | yes | SARS UIF page | match |
| Company car 3.5% / 3.25% | yes | yes | G21 | match |
| Travel allowance 80% / 20% | yes | yes | G21 | match |
| Interest 10.25% from 2 Mar 2026 | yes | yes | Budget FAQ; s89bis(2) | match |
| Cross-border: PAYE on non-residents | "generally within PAYE, subject to treaty relief the employee proves" | para 2(1) employer scope; treaty not read | para 2(1) | fixed; unsourced treaty/directive claims removed |

Totals: 94 items (51 CIT, 43 payroll; the seven PAYE bands count as one row), plus 7 README claims. 70 matched as written (37 CIT, 33 payroll); 24 were fixed, made precise, added or newly sourced (14 CIT, 10 payroll).

### README

| Claim | Check | Result |
|---|---|---|
| IT-IND partial: za-income-tax tax_year 2025 | frontmatter `tax_year: 2025` | accurate |
| TP partial: south-africa-transfer-pricing tax_year 2025, no Sources | `tax_year: 2025`, no `## Sources` | accurate |
| XB partial: leaving-south-africa-tax-emigration tax_year 2025 | `tax_year: 2025` | accurate |
| covered_by SC/PR -> za-payroll-paye-uif-sdl; IT-CORP -> za-corporate-income-tax; XB -> leaving-... | slugs exist | accurate (IT-CORP and PR entries are redundant, since the slugs already carry "corporate" and "payroll" tokens, but harmless) |
| PR row status "checked against the law" | also listed za-emp501-..., which has no independent review record | fixed: za-emp501 marked "sourced from the law" in the row |
| Summary figures (27%, 18%–45%, UIF 1% + 1% to R17 712, SDL 1%) | sources above | match |
| VAT not partial | za-vat-return has tax_year 2026; south-africa-vat has tax_year 2025 and neither has a Sources section | left as is (current-year skill present); flagged for the pack owner |

`python3 scripts/coverage-report.py --json`: ZA present IT-CORP, VAT, SC, PR; missing IT-IND, TP, XB (the three partials); has_readme true.

## Fixes made (with sources)

CIT skill:
1. Description cut from 166 to 140 words (frontmatter rule, 80–150).
2. s12E(4)(c) investment income definition completed, and s12E(4)(d) personal service definition added.
3. s12E(1) mining/farming exclusion; s12E(2) "lesser of" cost rule.
4. s20 carry-forward sentence rewritten to the statute (s20(1), (2A)).
5. Dividend exemptions now cited to s10(1)(k)(i) and s64F(1)(a) and removed from not-confirmed.
6. Top-up payment row: s89quat effective date and R20 000 threshold added (s89quat(1)–(2)); s89quat effective date added to the worked dates and Example 2.
7. Record keeping cited to TAA ss29(3)(a), 32 instead of the PAYE guide; the PAYE guide row removed from CIT Sources.
8. Para 20(1)(b) made precise; para 20(2B) and 20(2) added.
9. Interest basis (s89bis(2), s89quat(2)) added.
10. TAA s210 exclusions and s211(3) R500 million rule added; threshold removed from not-confirmed.
11. s5(2) Budget-announcement basis noted; Sources rows updated with sections and consolidation dates.

Payroll skill:
1. Description cut from 172 to 148 words.
2. Legal basis of the 2027 tables (ITA ss5(2), 6(6), 6A(5)) noted; consolidation still shows 2026 amounts.
3. Retirement fund cap changed from R430 000 to R350 000 (ITA s11F(2)(a); rule 2), R430 000 flagged; example `rf_cap_annual` uses 350000 (value unchanged at 49 500).
4. Medical credit condition corrected to para 9(6).
5. PAYE employer scope (para 2(1)) and director wording corrected.
6. UIF registration rule corrected (SARS UIF page; G21).
7. UIF remuneration definition added (UIC Act s1), including the commission exclusion.
8. SDL base: G21 reading added; Example 2 edge corrected from R150 to R135 (`sdl_if_liable`), statutory question flagged.
9. Citation fixes: UIC Act s8(1)/(2)/(2A)(b), TAA ss29, 32, 213.
10. Para 13(2)(b) certificate row widened from death to any cessation.
11. Unsourced cross-border claims (treaty relief "the employee proves", directive requirement) removed.
12. ITA and TAA consolidation rows added to Sources; UIC Act row sections updated.

README: PR row status split so za-emp501 is not claimed as checked against the law.

## Examples recomputed by hand

- CIT Example 1: 266 000 x 7% = 18 620; 18 620 + 185 000 x 21% = 57 470; 18 620 + 55 000 x 21% = 30 170; 420 000 x 27% = 113 400; saving 83 230. Correct.
- CIT Example 2: cap max(1 000 000, 4 800 000) = 4 800 000; loss used 4 800 000, c/f 700 000; TI 1 200 000; tax 324 000; paid 243 000; tax on 960 000 = 259 200; penalty 20% x 16 200 = 3 240; balance 81 000. Correct. No para 27 penalty arises (payments matched the estimate).
- Payroll Example 1: 360 000; 44 118 + 114 900 x 26% = 73 992; less 17 820 = 56 172; /12 = 4 681; less 752 = 3 929; UIF 177.12 x 2; SDL 300; total 4 583.24. Correct.
- Payroll Example 2: cap min(350 000, 49 500) = 49 500; deduction 18 000; 162 000 x 18% = 29 160; less 27 585 = 1 575; /12 = 131.25; UIF 150 x 2; SDL nil; edge corrected to 135.
- `python3 scripts/check-examples.py`: both files, 2 blocks each, 0 failures (after fixes).
- `python3 scripts/validate-guides.py --no-index-check`: passed.

## Structure

Both skills: nine deep-tax sections in order; rates table with sources; exactly two worked examples with `oa-check` blocks; "Ask the client first"; `## Sources` last with read dates; "Not yet confirmed:" line present. Frontmatter: name, jurisdiction ZA, category (international / payroll), tax_year 2026 (bare integer), tier 2, last_updated 2026-10-29, version 0.1. No platform-written keys added.

## Still not confirmed

CIT: 2026 Rates and Monetary Amounts Act Gazette text; whether a late ITR14 is in the TAA s210 public notice; SEZ rules (s12R); the rest of s89quat.

Payroll: GN 475 text (UIF ceiling); the R430 000 retirement cap (SARS figure, not in the Act text read); whether the SDL leviable amount is reduced by retirement contributions (G21 reading); 2026 Rates Act Gazette text; 2027 EMP501 windows; ETI amounts; fringe-benefit determined value; treaty rules; how the s10(1)(o)(ii) exemption is applied in payroll.

## Could not reach

- Subordinate legislation (Gazette notices, including GN 475 of 2021 and the TAA s210 public notice) on sars.mylexisnexis.co.za needs a login; not read.
- SDL Act ss11–12 (penalty and interest) were not opened; the payroll skill cites them only through G21.
- Everything else listed under "Sources re-read" was reached and read directly.
