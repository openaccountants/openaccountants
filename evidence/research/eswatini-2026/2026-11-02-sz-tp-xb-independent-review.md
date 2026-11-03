# Eswatini TP and XB: independent review

- Date: 2026-11-02
- Reviewer: independent AI review agent (no shared context with the writer)
- Files reviewed: `skills/eswatini/sz-transfer-pricing.md`, `skills/eswatini/sz-cross-border.md`, `skills/eswatini/README.md` (generated TP and XB rows)
- Standard: `docs/skill-template.md` (read in full)

## How the sources were read

| Source | URL | How read |
|---|---|---|
| Income Tax (Amendment) Act 2023 (Act 20 of 2023), scanned | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf | curl; `pdftoppm -r 75`; pages S1, S2, S4, S5, S7, S11 to S15, S17 to S19, S22 to S30 viewed by eye |
| Income Tax Order 1975, ERS consolidated copy | https://www.ers.org.sz/documents/IncomeTaxOrder1975.pdf | curl; `pdftotext -layout`; s2 "associate", s7, s8, s11, s11bis, s12(1)(e), (u), ss21 to 32E, s35, s35bis, s40, s40bis, s41, s57, ss59 to 59C, s66, s68, s68bis, s68ter |
| ERS, Income Tax Order changes 2024 | https://ers.org.sz/whatsnew-file/1726738466004-Income_Tax_Order_Changes__2024.pdf | curl; `pdftotext`; whole document |
| ERS notice, returns for tax year end 2026 | https://ers.org.sz/whatsnew-file/1791462650754-1784270658474_Notice_for_Filing_Income_tax_Returns_Public_Notice_Final_Aligned.pdf | curl; `pdftotext` plus a rendered crop of the deadline table (two-column layout) |
| Eswatini and South Africa DTA with Protocol | https://www.ers.org.sz/documents/SouthAfrica.pdf | curl; `pdftotext`; Gazette notice, Articles 9, 10, Protocol |
| ERS Rates and Thresholds | https://www.ers.org.sz/IncomeTax/RatesandThres | curl; HTML stripped; non-resident table and additional tax note |
| ERS Withholding Taxes | https://www.ers.org.sz/IncomeTax/Withholding | curl; HTML stripped; interest wording |
| 2026-27 Budget Speech | https://ers.org.sz/whatsnew-file/1772201986460-2026_27_FY_Budget_Speech_2026.pdf | curl; `pdftotext`; paras 159 to 167 |

Not opened by the reviewer: the ERS Tax Legislations page and EswatiniLII (the treaty list and the absence of TP regulations rest on the writer's notes; no change depended on them).

## Figures and rules checked

| Item | Skill value | Source value | Source | Result |
|---|---|---|---|---|
| Act commencement | Gazette notice (s1(2)); ERS: 1 July 2024 | same | Act p. S1; ERS 2024 p. 1 | match |
| Assent date | 14 July 2023 | 14th July 2023 | Act p. S1 | match |
| Arm's length principle definition | price payable between independent enterprises | same | Act s2, p. S1 | match |
| Associate person (a) to (d), 50% test | relative; partner etc.; trustee; company 50%+ share capital or voting power, or acting on directions | same | Act s2, pp. S1 to S2 | match |
| Older s2 "associate" in the Order | not mentioned | separate definition still in the Order | Order s2 | fixed (added, plus Not yet confirmed) |
| Controlled / uncontrolled transaction | between associated / independent persons | same | Act s2, pp. S2, S7 | match |
| Financial indicators per method | price, resale margin, mark up, net profit margin, division of profit | same | Act s2, p. S2 | match |
| s65quat(1)(a), (b) and proviso | as stated | same | Act s31, p. S22 | match |
| s65quat(2) direction | "only adjusts in the direction that restores tax" | applies where effect is reducing or postponing tax | p. S22 | reworded to the statutory test |
| s65quat(3) | follows s65quin | "in accordance with section 65quin (1)" | p. S22 | match (subsection added) |
| s65quat(4) head office charges | royalties, management commission, interest except banking; actual expense reimbursement allowed | same | p. S22 | match |
| s65quin(1), (2) four criteria | as stated | same | p. S23 | match |
| s65quin(3) five methods, residual split proviso | as stated | same | pp. S23 to S24 | match |
| s65quin(4) one method enough | as stated | same | p. S24 | match |
| s65quin(5), (6) other method | as stated | same | p. S24 | match |
| s65quin(7), (8) beneficial tax regime | associated or not; Gazette limits | same | p. S24 | match |
| s65quin(9), (10) commodities | quoted price on shipment date; export proviso "agreed price" | export proviso refers to price agreed between the group and an independent person | pp. S24 to S25 | fixed |
| s65quin(11) documentation | s35bis plus TP Regulations | same | p. S25 | match |
| s65quin(12) intangibles cap | % of EBITDA | % of earnings before interest, taxes, depreciation, amortisation and royalties payable | p. S25 | fixed (2 places) |
| s65quin(13) domestic small-value exclusion | domestic pairs; Gazette threshold; Commissioner may direct before the year | same | p. S25 | match |
| s65sex(1) to (5) tested party | as stated | same | pp. S25 to S26 | match |
| s65sex(6), (7) OECD Guidelines, Order prevails | as stated | same | p. S26 | match |
| s65sep interest cap | 30% of tax EBITDA (linked only) | 30%, banking and insurance excluded, 3-year carry forward | p. S26 to S27 | match |
| s32I(3) cost base non-arm's length | market value | same (subject to (4)) | p. S14 | match |
| s32J(2) disposal to associate | greater of cost base and FMV | same, except transmission to trustee or beneficiary on death | p. S15 | fixed (exception added) |
| s11bis(6) trading stock | current market price in Commissioner's opinion | same | Order | match |
| s35(9) | E25 a day, max E10,000 | same, for failures under s35(1), (2), (4), (7) | Act s20, p. S18 | match; scope wording fixed |
| s35bis(3), (4), (5) | 5 years, in Eswatini, English or siSwati; longer during objection; disallowance | same | Order | match |
| s40(1)(b), (c) additional tax | "up to twice" | "an amount equal to twice", remissible under s40(3) | Order | fixed (TP 3 places, XB 1) |
| s40(5) non-permissible deduction | "includes an excessive related-party charge" | text covers non-permissible deductions; TP adjustment not named | Order | reworded as uncertain |
| s40(9) private ruling shield | as stated | same | Act s23, p. S19 | match |
| s40bis(1) | 20% of tax not withheld | same | Order; ERS rates page | match |
| s40bis(2) | 10% / 15% / 20% / 25% at under 30 / 30 / 90 / 180 days | same | Order; ERS rates page | match |
| s40bis(3) | borne personally | same | Order | match |
| s57(2) | 18% a year; Minister may vary | same | Order | match |
| s66(1)(b), (h), (j) | fine to E10,000, 1 year, or both | same | Order | match |
| s66(2) | fine to E50,000, 5 years, or both; withholding and s32E | same | Order | match |
| s66bis | public officer deemed; knowledge and diligence defence | "public officer or other similar officer"; "consent or knowledge" | Act s32, p. S27 | fixed |
| s68ter private ruling | as stated | same | Order | match |
| s33(1) proviso extension | as stated | same | Act s18, p. S17 | match |
| s33(16), (17) withholding return, E25 a day | as stated | same | Act s18, p. S17 | match |
| Company rate 25% | 25% | 25% (Third Schedule para 1(a)); 25% for 2026 declarations | Act s39, p. S29; 2026 notice para 5 | match |
| Third Schedule para 2 minimum | 10%; 3% on pension | same | Act p. S30 | match |
| 2026 return deadline, non-individual entities | 31 October 2026, TaxEase only | same | 2026 notice paras 3, 4 | match |
| Other approved year ends | within four months | same | 2026 notice para 4 | match |
| Individuals' deadline | 30 November 2026 "for individuals with employment and other income" | 30 November 2026 for all three individual segments; businesses (VAT and non-VAT) 31 October 2026 | 2026 notice para 4 | fixed (XB) |
| Draft financial statements | accepted | same | 2026 notice para 6 | match |
| Payment methods, no cash | as stated | same | 2026 notice para 7 | match |
| Non-resident must file | every person not ordinarily resident with Eswatini-source gross income | same | 2026 notice para 1.1(a) | match |
| Budget Speech | "latest income tax reform"; no new measures | listed among completed reforms (para 165); no tax increases except excise (para 166) | Budget paras 165, 166 | reworded (TP) |
| s7 source basis | as stated | same | Order | match |
| s11(1)(a) to (k) deemed source list | as stated | same | Order | match |
| s11(7) foreign government stock interest | as stated | same | Order | match |
| s11(9A)(a) to (c) foreign interest and credit | deemed source unless foreign branch; credit capped | same | Order | match |
| Only foreign tax credit is s11(9A) | as stated | no other credit found (s8 rebates are personal) | Order | match |
| Residence: s22(1)(c), s28(c), s27(c) | as stated | same | Order | match |
| PE fixed place list (i) to (xiii) | as stated | same | Act s2, p. S4 | match |
| PE services test (xiv) | more than 30 days in any 12-month period beginning or ending in the year | same | Act s2, p. S4 | match |
| PE dependent agent, stock of goods, independent agent, closely related, control | as stated | same | Act s2, p. S5 | match |
| Royalty definition amendment | industrial, commercial or scientific equipment | same | Act s2(d), p. S7 | match |
| NRST s21(2) | 15%; 12.5% proviso deleted | Order 15% with 12.5% proviso; Act s10 deletes proviso | Order; Act p. S11 | match |
| NRST ERS confirmation | 15%, increase from 12.5% | same | ERS 2024 summary | match |
| NRST s22(1) persons charged | three groups | four: deceased estates omitted | Order | fixed |
| NRST s22(2) exemptions, s24, s25 | as stated | same | Order | match |
| NRST s26(1) | 30 days with return | same | Order | match |
| s12(1)(e) dividends to non-residents exempt | as stated | same | Order | match |
| Non-resident interest s27 | 15% (ten replaced by fifteen) | Order "ten per centum"; Act s11 replaces with "fifteen" | Order; Act p. S12 | match |
| s29(c) E20 de minimis deleted | as stated | Act s12 deletes s29(c) | Act p. S12 | match |
| s28(a) address presumption, s29 remaining exemptions, s31, s32(1) 14 days, s32(3) credit | as stated | same | Order | match |
| s32A entertainers 15%, 15 days, group joint liability | as stated | same | Order | match |
| s32B royalties and management charges 15% final, 15 days, s12(1)(u) | as stated | same | Order | match |
| s32E BPT 15%, A minus B, normal tax | as stated | same; Act s14 deletes proviso to (1) and s32E(4) | Order; Act p. S13 | match |
| s32E deleted proviso countries | "southern African" / "SACU" | Botswana, Lesotho, Mozambique, Namibia, South Africa (s32E(4)) | Order | fixed (description and intro precision) |
| s32F, s32G 15th of next month | (notes only) | same | Act ss15, 16, p. S13 | match |
| s32H(4) to (7) entry and exit | as stated | same | Act s17, p. S14 | match |
| s59 construction 15% net of materials, 15 days, 30-day annual return, on account | as stated | same | Order | match |
| s59A services 15% gross, exclusions, on account, (8a) | as stated | same | Order | match |
| s59C notification 30 days, contents | as stated | same | Order | match |
| s68 treaties, reciprocity | as stated | same | Order | match |
| s69quin supremacy | as stated | same | Act s36, p. S28 | match |
| SA DTA Gazette notice 24 Nov 2004 | as stated (notes) | same | SA DTA p. 1 | match |
| SA DTA Article 9 | as stated | same | SA DTA | match |
| SA DTA Article 10(2) | 10% for company holding at least 25% capital; 15% otherwise | same | SA DTA | match |
| SA Protocol BPT | "capped at 10%" | not discrimination provided it does not exceed 10% of repatriated income | SA DTA Protocol | wording made precise |
| ERS rates page | 15th of following month; scale | same | ERS rates page | match |
| ERS Withholding page | still shows 10% non-resident interest | "ten per cent" | ERS Withholding page | match |

Figures and rules checked: 86 rows above (some rows group several sub-points).

## Fixes made

TP (`sz-transfer-pricing.md`):
1. s65quin(12) cap base: "EBITDA" to "earnings before interest, taxes, depreciation, amortisation and royalties payable" (rates row and base).
2. s40(1): "up to twice" to "twice", remissible under s40(3) (rates row, penalties, Example 1 wording).
3. s65quin(9) export proviso: the higher agreed price is the one agreed between the group and an independent person.
4. s32J(2): added the exception for transmission to a trustee or beneficiary on death.
5. s66bis: "public officer or other similar officer"; defence is "without consent or knowledge" plus reasonable diligence to prevent.
6. s35(9) row: scope stated as s35(1), (2), (4), (7) failures.
7. s65quat(2): direction sentence reworded to the statutory test.
8. s40(5): the claim that an excessive related-party charge is an omission marked as not spelled out; s65quat(4) case stated as clear.
9. Added the older Order s2 "associate" definition and a Not yet confirmed item on which definition governs.
10. Budget Speech sentence aligned to paras 165 and 166.

XB (`sz-cross-border.md`):
1. Description: "12.5% SACU rate" to the four named countries.
2. Intro: named the countries in each repealed 12.5% proviso (BPT also covered Mozambique).
3. NRST: added deceased non-resident estates (s22(1)(b)).
4. s40(1): "up to twice" to "twice", remissible.
5. Individuals' return deadline: all three individual segments 30 November 2026; VAT and non-VAT registered businesses 31 October 2026.
6. SA Protocol wording made precise (Article 23 non-discrimination condition).
7. Example 2: added the treaty conditions (SA resident beneficial owner, s68(2) reciprocity, s69quin open).

Both files staged with `git add`. `skill_checks.run_all` returns `{}` on both; `check-examples.py --require` passes 2 of 2 blocks on each; no em dash.

## Examples recomputed by hand

- TP Example 1: (0.04 - 0.01) x 20,000,000 = 600,000; x 25% = 150,000; x 2 = 300,000; x 18% = 27,000. Correct.
- TP Example 2: keep: 15% x 2,000,000 = 300,000; disallowed 800,000 x 25% = 200,000; total 500,000. Reprice: 15% x 1,200,000 = 180,000. Saving 320,000. Correct (taxable income is the same either way: 2,000,000 deducted less 800,000 added back equals 1,200,000 deducted).
- XB Example 1: 25% x 4,000,000 = 1,000,000; 3,000,000 x 15% = 450,000; total 1,450,000; 36.25%. Correct.
- XB Example 2: normal tax 1,000,000; branch 10% x 3,000,000 = 300,000; subsidiary 10% x 1,000,000 = 100,000; difference 200,000; full payout 300,000. Correct.

## Verdict on the conflict with the existing skills

Confirmed. Act 20 of 2023 s10 deletes the proviso to Order s21(2) (the 12.5% rate for Botswana, Lesotho, Namibia and South Africa companies), leaving 15%; s11 replaces "ten" with "fifteen" in s27; s14 deletes the proviso to s32E(1) (12.5% for neighbouring-country companies) and s32E(4). The ERS 2024 summary says the same and gives 1 July 2024 as the effective date. So for the year to 30 June 2026:

- `sz-corporate-income-tax.md` line 33 (NRST 12.5% for BLNS companies), line 35 (non-resident interest 10%) and line 40 (BPT 12.5% for neighbouring-country companies) are stale.
- `sz-tax-overview.md` line 49 ("interest 10%") and line 53 (worked dividend at 12.5% under s21) are stale.

Not edited here, as instructed; they need their own PR.

## README

The generated TP and XB rows are correct (slugs, tax year 2026, Ready). The regeneration did drop one hand-written line from "What still needs doing": "Settle the VAT registration threshold and return deadline, where official ERS sources conflict (see [VAT or GST](sz-vat-gst.md))." The generator only writes to-do lines from Missing, `partial:` and stale entries, and `partial:` is `{}`, so the line was lost and the section now says "Nothing is missing or out of date", which is not true while `sz-vat-gst.md` lists that conflict as unconfirmed. Not fixed here (outside the two skill files); the durable fix is a `partial:` entry for VAT in the README frontmatter so the generator keeps it.

## Tax year label

Both new skills use `tax_year: 2026` with the year of assessment 1 July 2025 to 30 June 2026, the same as every other Eswatini skill (`tax_year: 2026`, `tax_year_notes: "Year of assessment to 30 June 2026"`, body "1 July 2025 to 30 June 2026"). Consistent within the pack and with the template's "current year" rule; the template's "coverage start year" wording would read 2025 for a July to June year, so the pack follows the "current year" reading. No change made.

## Still not confirmed

- Which "associate" definition governs ss65quat to 65sex where the old and new ones differ (added).
- Transfer Pricing Regulations ("regulation 11"); Gazette notices for s65quin(8), (12), (13); the Act's s1(2) commencement notice.
- Whether remittance periods in ss26, 32, 32A, 32B, 59, 59A have been changed to the 15th of the following month shown on the ERS rates page (only ss32F, 32G seen amended).
- Whether s69quin limits treaty rates given effect under s68.
- Whether a s65quat(2) adjustment counts as a non-permissible deduction under s40(5) (now stated in the body as not spelled out).
- Other treaties' articles; any Tax Administration Act; TaxEase TP fields; CbCR, master/local file, APA.

## Unreachable sources

None. Every URL fetched answered with the document. Act pages S31 to S38 (Sixth and Seventh Schedules) were not read, as they hold nothing cited in these skills.
