# Uganda TP and XB: independent review

- Date: 2026-11-02
- Reviewer: independent AI review agent (no shared context with the writer)
- Branch: pack/ug
- Files reviewed: `skills/uganda/ug-transfer-pricing.md`, `skills/uganda/ug-cross-border.md`
- Standard: `docs/skill-template.md` (line 12)

## Sources actually read

| Source | How read | Parts read |
|---|---|---|
| Income Tax Act, Chapter 338, as at 23 Dec 2024 (ULII PDF, generated 23 Oct 2026; and a browser print of the same ULII page), https://ulii.org/akn/ug/act/1997/11/eng@2024-12-23 | local copies saved by the user (ULII's Cloudflare check blocks automated fetch), extracted with `pdftotext -layout` | s2 (currency point), s3, s9, s10, s17 heading, Part IX ss77 to 88, Part XI ss116 to 117, ss137 to 142, s148, Sch. 1, Sch. 4 Parts III, IV, V, VI, VII |
| URA, Compendium for various Domestic Tax Laws (July 2021) | local copy, `pdftotext -layout` | Income Tax (Transfer Pricing) Regulations 2011 r1 to r10; ITA Cap. 340 Part IX ss78 to 88; old Sch. 4 Parts IV and VII; TPCA s48 to s50 |
| URA, Tax Amendments FY 2026-27 handbook | local scanned PDF, pages 6 to 11 rendered as images and read | p. 6 (status note, royalty, DST exclusion), p. 7, p. 8 (interest cap, debentures), p. 9 (arm's length duty), p. 10 (entertainers 6%), p. 11 (individual rates) |
| URA, File a Tax Return, https://ura.go.ug/en/domestic-taxes/returns/ | curl, 2026-11-02 | return deadlines, 15th-of-month rule, 90-day extension |
| URA notice, effective date of the Income Tax (Amendment) Act 2026 | curl, 2026-11-02 | assent and commencement 1 July 2026 (notice dated 23 Sep 2026) |

## Figures, rules and references checked

### ug-transfer-pricing.md

| # | Item | Skill value | Source value | Source | Result |
|---|---|---|---|---|---|
| 1 | TP power section | s116 Ch. 338 (old s90) | s116 "Transactions between associates", Part XI; old Cap. 340 s90 | ITA Ch. 338 s116; compendium | match |
| 2 | s116(1) scope incl. employment relationship | yes | yes | s116(1) | match |
| 3 | s116(2) intangibles commensurate with income | yes | yes | s116(2) | match |
| 4 | s116(3) source and revenue/capital nature | yes | yes | s116(3) | match |
| 5 | s117 re-characterisation | avoidance schemes, no substantial economic effect | also (c) form not reflecting substance | s117(1) | match (summary) |
| 6 | Associate general test | non-employee acting on directions | same | s3(1) | match |
| 7 | Relatives, partners unless CG satisfied | yes | yes | s3(2)(a), (b) | match |
| 8 | 50% control | "company or partnership ... voting power or rights to income or capital" | company: voting power (e), (h); partnership: rights to income or capital (c), (f); sister companies (h)(ii) | s3(2) | fixed (tests split, sister-company rule added) |
| 9 | Trusts | trustee and beneficiaries | same | s3(2)(d), (g) | match |
| 10 | Associate threshold row | 50% or more | fifty percent or more | s3(2) | match |
| 11 | TP Regs in force | 1 July 2011 | 1st July 2011, S.I. 2011 No. 30 | r1 | match |
| 12 | Application domestic and cross-border | yes | "located in or outside Uganda" | r2 | match |
| 13 | Controlled transaction = between associates | yes | yes; also 2026 Amendment | r3; handbook p. 9 | match |
| 14 | Branch definition in r3 | "s77 definition" | r3 cites s78 Cap. 340, which is s77 in Ch. 338 | r3; s77 | fixed (renumbering stated) |
| 15 | Branch/HQ separate persons and associates | yes | yes | r5 | match |
| 16 | "Transaction" incl. non-enforceable and branch dealings | yes | yes | r3 | match |
| 17 | CIT on adjustment | 30% | 30% | Sch. 4 Part III para 1 | match |
| 18 | WHT management charge/royalty to non-resident | 15% gross, final | 15%; final under s87(1) | ss82, 87; Sch. 4 Part V para 1 | match |
| 19 | Royalties incl. software, 15% WHT not DST, from 1 July 2026 | yes | yes | handbook p. 6; URA effective-date notice | match |
| 20 | Arm's length duty, 2026 Amendment | yes | "shall account ... consistent with the arm's length principle" | handbook p. 9 | match |
| 21 | Amendment commencement | 1 July 2026 | July 01, 2026 | URA notice | match |
| 22 | r7(1) to r7(5) duty, adjustment, MAM factors, person's method, other methods | yes | yes | r7 | match |
| 23 | Five methods | CUP, RPM, CPM, TNMM, profit split | same | r3 | match |
| 24 | Comparability factors (5) | yes | yes | r4 | match |
| 25 | OECD Art. 9 and Guidelines, Act prevails | yes | yes | r6 | match |
| 26 | Offence r7(6), r8(4) | 6 months, 25 currency points, or both | same | r7(6), r8(4) | match |
| 27 | Currency point | "not yet confirmed" | UGX 20 000 | ITA s2, Sch. 1 | fixed (added, row linked) |
| 28 | Documentation in place before return due | yes | "prior to the due date for filing" | r8(2) | match |
| 29 | Commissioner may specify items by notice | yes | yes | r8(3) | match |
| 30 | APA request contents and outcomes | yes | yes | r9(2) to (5) | match |
| 31 | APA timing | "before the transactions it covers" | applies to transactions entered into on or after the agreement date | r9(7) | fixed (reworded) |
| 32 | APA cancellation grounds | 4 grounds | 4 grounds (incl. mistake or omission) | r9(8) | match |
| 33 | Corresponding adjustment | on request, if arm's length | same, treaty country only | r10 | match |
| 34 | Return due date | 6 months; 31 Dec for 30 June | same | URA returns page | match |
| 35 | Extension | up to 90 days aggregate, payment date unchanged | same | URA returns page | match |
| 36 | Monthly WHT deadline | 15th, cited "s87" | 15 days after month end | ITA s140(1); URA | fixed (citation s140(1)) |
| 37 | Treaty override exceptions | Part XI and s88(7) | same | s88(2) | match |
| 38 | Interest on unpaid tax | "TPCA, not read" | 2% per month simple, cap | ITA s148 | fixed (added, row linked) |

### ug-cross-border.md

| # | Item | Skill value | Source value | Source | Result |
|---|---|---|---|---|---|
| 39 | Individual residence tests | home; 183 days in 12 months; avg > 122 days over 3 years; Govt posted abroad | same | s9(1) | match |
| 40 | Part-year rules | arrival / departure | same | s9(2), (3) | match |
| 41 | Company residence | incorporation; management and control at any time; majority of operations | same | s10 | match |
| 42 | Branch definition and 90-day tests | yes | same (Islamic finance carve-out not mentioned) | s77 | fixed (row wording: "90 days or more" vs "more than 90") |
| 43 | Non-residents taxed by "final withholding (ss82 to 87)" incl. digital services | yes | s87 final tax covers ss82, 83, 84, 85(1), 85(4) only; s137 withholding covers ss82, 84, 85; s86 is self-returned | ss86, 87, 137 | fixed (error) |
| 44 | Source rules list | 10 items | s78(a) to (t) | s78 | fixed (land-rich share condition "business asset"; change-of-ownership exclusions corrected to local governments) |
| 45 | 15% rate on ss81 to 84 | 15% | 15% excl. Govt securities | Sch. 4 Part V para 1 | match |
| 46 | Govt securities | 20% up to 10 yrs; 10% 10 yrs or more | 20% "does not exceed ten years"; 10% "at least ten years" | Sch. 4 Part V para 2 | match (overlap at exactly 10 years noted) |
| 47 | Digital services | 5% | 5% | s86(1); Sch. 4 Part V para 3 | match |
| 48 | Digital service list | 8 types + Minister | same | s86(3) | match |
| 49 | DST return | 15 days after tax period | same | s86(4) | match |
| 50 | Telecoms/internet/DTH | 5% gross | 5% gross, final | s85(4), s87 | match |
| 51 | Transport | 2%, "ship, air and road ... embarked" | road: cargo or mail only; trans-shipment excluded | s85(1), (3); Sch. 4 Part VI | fixed (conditions) |
| 52 | CIT on branch | 30% | 30% | Sch. 4 Part III | match |
| 53 | Royalties 15% not DST from 1 July 2026 | yes | yes | handbook p. 6 | match |
| 54 | Debenture interest 5% | "interest paid outside Uganda on widely issued debentures" | paid by a resident company to a bank or FI of a public character outside Uganda | handbook p. 8 | fixed (condition restored; reach to Not yet confirmed) |
| 55 | Branch profits tax formula A + (B - C) - D | yes | same | s81(3) | match |
| 56 | BPT in addition to tax on chargeable income | yes | yes | s81(5) | match |
| 57 | Dividend source, Ugandan profits first | yes | yes | s82(3), (4) | match |
| 58 | Branch carve-out | "taxed with the branch under s17" | s82(1) does not apply; subject to s17 (gross income) | s82(6) | fixed (wording) |
| 59 | s84 excludes royalties and management charges | yes | yes | s84(3) | match |
| 60 | Foreign tax credit cap, baskets, soak-up taxes | yes | yes | s80 | match |
| 61 | Foreign employment income exemption | yes | yes | s79 | match |
| 62 | Treaty override and s88(7) beneficial owner/substance, listed co exception | yes | yes | s88(2), (7) | match |
| 63 | AEOI | "URA facilitates" | where an agreement provides for it | s88(4) | fixed (condition) |
| 64 | WHT payment deadline | 15th, cited "s87" | within 15 days after month end | s140(1) | fixed (citation) |
| 65 | Entertainers group tax | before leaving | s83(4); agent: 5 days after performance or day before departure, earlier | s83(4), s140(2) | fixed (agent deadline added) |
| 66 | Non-resident services agreement notification | absent | 30 days; personal liability | s138(1), (4) | fixed (added, within the WHT job) |
| 67 | Withholding agent liability | "s137 onward and TPCA" | personally liable for tax not withheld | s142(1) | fixed |
| 68 | Interest | "TPCA, not read" | 2% per month, borne by agent | s148(1), (4) | fixed (added, row linked) |
| 69 | Old Cap. 340 cross-ref for entertainers | s84(4) | s84(4) | compendium | match |

Total: 69 items checked (38 TP, 31 XB); 51 match, 18 fixed (6 TP, 12 XB). Several items carry more than one figure or section reference.

## Where the 2024 text differs from the 2021 compendium

- Renumbering: Cap. 340 s78 to s88 became Ch. 338 s77 to s88 with s86 (digital services) new; s90 to s116; s91 to s117; tax avoidance Part X to Part XI; s88(5) to s88(7). TP Regulations r3 still cites "section 78" (the old branch definition).
- Sch. 4: the non-resident rate Part was Part IV (ss82 to 85), now Part V (ss81 to 84, 86). The 2% rate was "shipping and aircraft income" (old Part VII); the 2024 text adds road transport operators (Part VI).
- s87 withholding cross-references moved from ss120/123/115 to ss137/140/125.
- The 2024 text still holds the s82(5) debenture exemption; the handbook says the 2026 Act repeals it (not yet applied by ULII).

## Examples recomputed by hand

- TP 1: (0.05 - 0.01) x 8 000 000 000 = 320 000 000; x 30% = 96 000 000. Correct.
- TP 2: 15% x 500 000 000 = 75 000 000; excess 200 000 000 x 30% = 60 000 000; total 135 000 000. Correct.
- XB 1: 2 000 000 000 + (900 000 000 - 270 000 000) - 2 100 000 000 = 530 000 000; x 15% = 79 500 000; total 349 500 000. Correct.
- XB 2: 1 000 000 000 x 30% = 300 000 000; average rate 30%; cap 60 000 000; credit min(70 000 000, 60 000 000) = 60 000 000; net 240 000 000; unrelieved 10 000 000. Correct.
- `python3 scripts/check-examples.py --require`: 2 blocks each, 0 failures, before and after fixes.

## Checks run

- `skill_checks.run_all` on both files: all clean, before and after fixes.
- `python3 scripts/validate-guides.py --changed-only --no-index-check`: passed, 0 warnings.

## Reviewer notes not fixed (judgement for the writer/maintainer)

- Line 9 asks that one worked case be a decision where the topic invites one. Neither skill has a "which should I" case (for XB, branch versus subsidiary is the obvious one: 30% plus 15% branch profits tax against 30% plus 15% dividend withholding). Not added, to keep to the review's no-new-scope rule.
- XB description still lists "5% on digital services" beside the withholding rates; the body now says it is a self-returned tax, not withholding.

## Still not confirmed

- Enacted text of the Income Tax (Amendment) Act 2026 (Act 21 of 2026); only URA's handbook summary of the Bill and URA's commencement notice were read.
- Act 13 of 2025 and Act 18 of 2025 (ULII lists them as not yet applied), including any effect on rates, s148 or the currency point.
- Whether the TP Regulations 2011 were amended after the 2021 compendium.
- TPCA penal tax: the 2021 compendium prints TPCA s49A (UGX 50 million for TP records not provided within 30 days); current numbering and amount not checked.
- Reach of the debenture-interest change and whether the 5% is final.
- Whether the new 6% entertainer withholding (handbook p. 10) displaces the 15% for non-residents.
- Country-by-country, master and local file rules; URA TP practice note; list of treaties in force and rates.

## Unreachable sources

- ulii.org: Cloudflare check loops for automated browsers; not fetched by the reviewer. Local copies saved by the user from ULII were used instead.
- The enacted 2026 and 2025 amendment Acts: no official copy available to the reviewer.
