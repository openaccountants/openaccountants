# Rwanda TP and XB: independent review (2026-11-02)

- Date: 2026-11-02
- Reviewer: independent AI review agent (no shared context with the writer)
- Files reviewed: `skills/rwanda/rw-transfer-pricing.md`, `skills/rwanda/rw-cross-border.md`, the generated TP and XB rows of `skills/rwanda/README.md`. Cross-read against `skills/rwanda/rw-corporate-income-tax.md`.
- Method: every source below was downloaded fresh with curl from the official host on 2026-11-02 and the English column of each trilingual Gazette text was extracted by column crop (pdftotext) and, for ITL art 60, also read as rendered page images (pp. 80 to 84). The writer's source notes were treated as claims only.

## Sources opened

| Key | Document | URL |
|---|---|---|
| ITL | Law 027/2022 establishing taxes on income, OG Special of 28/10/2022 | https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf |
| L051 | Law 051/2023 amending Law 027/2022 | https://www.rra.gov.rw/fileadmin/user_upload/Law_amending_Income_Tax_Ok.pdf |
| L014 | OG Special of 29/05/2025, Law 014/2025 amending Law 027/2022 | https://www.minijust.gov.rw/index.php?eID=dumpFile&f=130496&t=f&token=4b9d4de9658212b7aaeeb5c8a42c823a7b879d7b |
| TPL | Law 020/2023 on tax procedures, OG Special ter of 31/03/2023 | https://www.rra.gov.rw/fileadmin/user_upload/OG_n___Special_ter_of_31.03.2023_Uburyo_bw_isoresha_Tax_procedures_01.pdf |
| O003 | Ministerial Order 003/26/10/TC of 29/04/2026 (transfer pricing, simplified accounting, loss carry-forward) | https://www.rra.gov.rw/fileadmin/Folder_for_2025/Ministerial_Order_on_Simplified_Accounting_Method_April_2026.pdf |
| O009 | Ministerial Order 009/26/10/TC of 24/09/2026, OG Special of 25/09/2026 | https://www.rra.gov.rw/fileadmin/user_upload/Ministerial_orders-Financial_statements.pdf |
| HB | RRA Tax Handbook 2025 | https://www.rra.gov.rw/fileadmin/Folder_for_2025/RRA_Tax_Handbook_2025_Final.pdf |
| LPR | RRA laws, policies and rulings page | https://www.rra.gov.rw/en/laws-policies-and-rulings |
| CON | Constitution of Rwanda 2003 revised 2015, OG Special of 24/12/2015 (RwandaLII copy) | https://rwandalii.org/akn/rw/act/law/2003/nn/eng@2015-12-24/source.pdf |

## Figures checked

| # | Item | Skill value | Source value | Source | Result |
|---|---|---|---|---|---|
| 1 | Related persons test | no percentage; directives, management/control/capital, common control, family to 3rd degree | same, art 3(1) a to e | ITL art 3(1) | match |
| 2 | HB related person example | 50% of voting rights | "50% or more, by value or number, of the voting rights" | HB p. 138 | match |
| 3 | Controlled transaction incl. beneficial tax regime | as stated | same | ITL art 3(7) | match |
| 4 | Arm's length principle definition | as stated | same | ITL art 3(8) | match |
| 5 | Beneficial tax regime markers | max 15% income tax; tax break to non-residents; no substance; foreign income untaxed or max 15%; no ownership information | same (i) to (v) | O003 art 2(a) | match |
| 6 | Scope cases | 3(1)(a) to (d), 3(2) | same | O003 art 3 | match |
| 7 | Transactions covered | (a) to (h) | same | O003 art 5 | match |
| 8 | Comparability factors, risk control | art 6(1) to (3) | same | O003 art 6 | match |
| 9 | Disregard of non-rational arrangement | art 7 | same | O003 art 7 | match |
| 10 | Method selection criteria | four criteria, art 8(2) | same | O003 art 8 | match |
| 11 | Five methods and article numbers | CUP 9, RPM 10, CP 11, TNMM 12, PS 13 | same | O003 arts 9 to 13 | match |
| 12 | Alternative method | only if RRA satisfied | same | O003 art 14 | match |
| 13 | Tested party | compulsory for CP, RPM, TNMM; foreign tested party info | same | O003 art 15 | match |
| 14 | Interquartile range, no adjustment inside, median outside | art 16 | art 16(2) to (4) | O003 art 16 | match |
| 15 | Documentation: policy, local file, master file | art 17(1) | same | O003 art 17(1) | match |
| 16 | Local file contents incl. five largest products, 5% of group turnover | art 17(2) | same, items (a) to (c)(xvii) | O003 art 17(2) | match |
| 17 | Further documents incl. CbC report, agreements, Annex 1 schedule, allocation keys | art 17(3) | same | O003 art 17(3) | match |
| 18 | CbC report filing | 12 months after reporting fiscal year end | same | O003 art 17(3)(g) | match |
| 19 | Documentation prepared before declaration deadline | prepared before deadline | "prepared before the deadline ... and submitted"; TPL art 16 says declaration accompanied by TP documentation | O003 art 18(1); TPL art 16 | fixed (submission added, TPL art 16 cited) |
| 20 | Documentation on request | 7 days | seven days from receipt of written request | O003 art 18(2) | match |
| 21 | Group legal structure | first declaration; updates | same | O003 art 18(3), (4) | match |
| 22 | Waiver turnover | below FRW 600,000,000 | same | O003 art 19(1) | match |
| 23 | Waiver transaction limbs | below FRW 10,000,000 "or" aggregate below FRW 100,000,000 | same, "or" | O003 art 19(2) | match (ambiguity kept in Not yet confirmed) |
| 24 | Arm's length still applies when waived | yes | same | O003 art 19(3) | match |
| 25 | Foreign comparables, data-availability rules | art 20 | same | O003 art 20 | match |
| 26 | Services benefit test | "only if" all four | four tests, list ends "; or" before (d) | O003 art 21(1) | fixed (wording; doubt to Not yet confirmed) |
| 27 | Shareholder activities | as stated | same | O003 art 21(2) | match |
| 28 | Intangibles, hard-to-value | art 22 | same | O003 art 22 | match |
| 29 | Corresponding adjustments | domestic; foreign with treaty | same | O003 arts 23, 24 | match |
| 30 | APA before or after | art 26(1), (2) | same | O003 art 26 | match |
| 31 | APA rollback | at most 2 prior years | not exceeding two years | O003 art 26(3) | match |
| 32 | APA missing information | 30 days, "lapses" | 30 days, "considered withdrawn" | O003 art 26(4) | fixed (wording) |
| 33 | Bilateral/multilateral APA | treaty needed | same | O003 art 26(7) | match |
| 34 | Pre-application meeting | art 26(8) | same | O003 art 26(8) | match |
| 35 | APA portal | 3 months from publication | same | O003 arts 27, 35 | match |
| 36 | APA transaction threshold | at least FRW 100,000,000 | same | O003 art 28(1)(b) | match |
| 37 | APA turnover threshold | at least FRW 600,000,000 | same | O003 art 28(1)(c) | match |
| 38 | APA fee | FRW 6,000,000 non-refundable | same | O003 art 28(1)(d) | match |
| 39 | New CIT registrant turnover waiver | art 28(3) | same | O003 art 28(3) | match |
| 40 | RRA decision; draft in 45 days; sign in 30 days | art 28(4), (5), (7) | same | O003 art 28 | match |
| 41 | APA refusal grounds | art 29 | same | O003 art 29 | match |
| 42 | APA term | 3 years renewable once | same | O003 art 30(1) | match |
| 43 | Annual compliance report | on the date the return is filed | same | O003 art 30(2) | match |
| 44 | Cancellation grounds and 30-day effect | art 31 | same | O003 art 31 | match |
| 45 | Entry into force, no repeal clause | on publication 29/04/2026 | art 37; arts 35 to 37 only | O003 art 37 | match |
| 46 | Chapter II = arts 2 to 31 | as stated | Chapter III starts at art 32 | O003 | match |
| 47 | 2018-Law orders sunset | not more than 12 months | same | ITL art 70 | match |
| 48 | TP duty and adjustment; APA basis | art 32 | same | ITL art 32 | match |
| 49 | Deemed dividend after TP correction | art 40 | same | ITL art 40 | match |
| 50 | CIT rate | 28%, rounded down to FRW 1,000 | same | L051 art 2 | match |
| 51 | 2% fee cap; 4x paid-up equity; banks/insurers out of item 10 | as stated | same | ITL art 25 items 9 to 11 | match |
| 52 | TP audit type | art 46 | same | TPL art 46 | match |
| 53 | 5% fine on controlled transaction information | 5% of value | same | TPL art 86 | match |
| 54 | Controlled-transaction records fine doubled | art 81 | same | TPL art 81 | match |
| 55 | Information-request fines | FRW 500,000 / 2,000,000 / 3,000,000 / 5,000,000 by turnover band | same bands (<=20m; >20m <200m; 200m to <600m; >=600m) | TPL art 81 item 5 | match |
| 56 | Repeat-fault multiplier | x2 second in 2 years, x4 third | same | TPL art 81 | match |
| 57 | Evasion fine | equal to evaded tax | same | TPL art 81 | match |
| 58 | Late payment fines | 20/40/60%; 5/10/30% | same ("twenty percent (10%)" typo) | TPL art 82 | match |
| 59 | Understatement | 10% for 10% to 20%; doubled above 20%; none if rectified before notice | same | TPL art 83 | match |
| 60 | Interest | 0.5% / 1% / 1.5% a month; simple; started month counts; cap 100%; payable on appeal | same | TPL art 80 | match |
| 61 | Audit window | 5 years, 10 years concealment | same | TPL art 35 | match |
| 62 | Extension request | 15 days before; interest runs | same | TPL art 20 | match |
| 63 | Records of controlled transactions, 10 years | arts 14, 15, no condition | art 14 applies to turnover above FRW 20,000,000; 10 years from 1 January after the year | TPL arts 14, 15 | fixed (condition added) |
| 64 | Annual declaration date | 31 March 2027 "or 3 months after an approved year-end (ITL arts 9, 10)" | arts 9 (as amended) and 10 give only 31 March; 3-month rule appears only for exempt persons (art 45(2) as amended) | L051 art 1; ITL art 10; L014 art 3 | fixed (unsupported limb removed from TP; to Not yet confirmed) |
| 65 | E-Tax related party tab, "None" row, fields | as stated | same | HB pp. 138, 161 to 162 | match |
| 66 | Individual residence | 183 days; average more than 122 days in each of two prior periods | same | ITL art 4 | match |
| 67 | Entity residence | incorporation or effective management at any time | same | ITL art 4 | match |
| 68 | Permanent residence | home, house, apartment, hotel or quarters usually stayed in | same | O009 art 1 | match |
| 69 | Effective management tests | four, any one | same | O009 art 2 | match |
| 70 | O009 dates | 24/09/2026; OG 25/09/2026 | same | O009 | match |
| 71 | PE list and 90-day services test | more than 90 days in 12 months | same | ITL art 5 | match |
| 72 | Dependent agent | negotiates/concludes or principal role | same | ITL art 5 | match |
| 73 | PE exclusions | "storage, display stock, ..." | storage facilities; stock for storage; stock for processing; purchasing/information; preparatory. No "display" | ITL art 5 | fixed |
| 74 | Independent agent, subsidiary, insurer rules | as stated | same | ITL art 5 | match |
| 75 | Source rules incl. services abroad for residents | art 6, last paragraph | same | ITL art 6 | match |
| 76 | Foreign tax credit and cap | capped at Rwandan tax on foreign income | same | ITL art 7 | match |
| 77 | Withholding credit; refund in 30 days | art 10 | same | ITL art 10 | match |
| 78 | Non-resident PIT; KIFC 5 years | art 12 | same | ITL art 12 | match |
| 79 | Non-resident employee exemption | art 16 item 5 | same | ITL art 16 | match |
| 80 | Foreign income tax not deductible | art 25 item 5 | same | ITL art 25 | match |
| 81 | Capital gains on direct/indirect share transfer | art 35 | same | ITL art 35 | match |
| 82 | Capital gains rate | 10% | "The capital gain tax rate is 10%" (was 5%) | L014 art 1 | match |
| 83 | CGT withholding and 15-day deadline | resident company; seller or buyer for licences etc.; 15 days after the month | same | L014 art 2 (ITL art 37) | match |
| 84 | CGT exemption listed / CIS | art 38 | same | ITL art 38 | match |
| 85 | Non-resident CIT via PE | arts 44 item 7, 47 | same | ITL arts 44, 47 | match |
| 86 | Digital services tax | 1.5% of Rwanda-source gross revenue; Order needed | same; no such Order on LPR | L014 art 5 (ITL art 50 bis); LPR | match (pending) |
| 87 | Employee self-declaration under treaty | 15 days after month | same | ITL art 58 | match |
| 88 | Board allowance | 30% | same | ITL art 59 | match |
| 89 | Art 60 rate and base | 15% excl. VAT | same | ITL art 60 | match |
| 90 | Art 60 condition: payee unregistered or no recent declaration | stated as the trigger | in art 60 first paragraph itself (pp. 80 of the Gazette), not only art 63 | ITL art 60 | match (see note) |
| 91 | Art 60 item list | 8 of 10 items | 10 items; goods sold in Rwanda (6) and profits converted into shares (7) omitted; resident dividends under art 47 excluded from item 1 | ITL art 60 | fixed |
| 92 | Interest carve-outs | three | same | ITL art 60 item 2 | match |
| 93 | Reinsurance carve-out | Government agreements | same | ITL art 60 item 10 | match |
| 94 | Accrued liability rule | more than 6 months after period | same | ITL art 60 | match |
| 95 | PEs of non-residents withhold | yes | same | ITL art 60 | match |
| 96 | 5% rate | listed securities to Rwanda/EAC residents; treasury bonds of 3 years or more | same | ITL art 60 | match |
| 97 | Credit for registered payee that did not declare | deducted in declaration | same | ITL art 60 last paragraph | match |
| 98 | Withholding declaration | 15 days after month, arts 59, 60, 61, 63 | same | ITL art 64 | match |
| 99 | Withholding exemptions | exempt profit; tax clearance certificate; newly registered | same (arts 60, 62, 63) | ITL art 65 | match |
| 100 | Payer liability | personal liability | same | ITL art 66 | match |
| 101 | Withholding records | 10 years | same | ITL art 67 | match |
| 102 | Anti-abuse | four markers, four actions | same | ITL art 68 | match |
| 103 | Treaty residence certificate | with the withholding declaration | same | TPL art 22 | match |
| 104 | Recipient self-declaration | 15 days after month | same | TPL art 74 | match |
| 105 | Treaty disclosure and access | arts 96, 97 | same | TPL arts 96, 97 | match |
| 106 | Global Forum 2017; MAAC 11 August 2021 | as stated | same | HB p. 72 | match |
| 107 | FTC certificate | "a foreign taxpayer can request" | available to taxpayers to prove tax paid in Rwanda; requested at RRA offices, case by case | HB p. 54 | fixed (wording) |
| 108 | FTC declaration field | yes | same | HB p. 172 | match |
| 109 | DRC treaty ratification order listed | yes | listed | LPR | match |
| 110 | Treaty precedence | Not yet confirmed (Constitution not read) | ratified treaties rank above ordinary laws; a law may not contradict a higher one | CON art 95 | fixed (added to skill with source) |
| 111 | Law 014/2025 amends arts 36, 37, 45, 50, 50 bis, 61 only | as stated | same | L014 | match |
| 112 | L051 amends arts 9, 48 only | as stated | same | L051 | match |

Figures checked: 112.

## Fixes made

TP (`rw-transfer-pricing.md`):
1. Annual declaration row: removed "or 3 months after an approved year-end (ITL arts 9, 10)"; ITL art 9 (as amended by L051 art 1) and art 10 give only 31 March. Moved to Not yet confirmed.
2. Documentation timing row: added that the documentation is submitted (O003 art 18(1)) and that the declaration for related party transactions is accompanied by it (TPL art 16); the tension with O003 art 18(2) is in Not yet confirmed.
3. Records: added the FRW 20,000,000 turnover condition of TPL art 14 and the start of the 10-year period (art 15).
4. Services (O003 art 21): "only if" all four replaced by the Order's wording (list ends with "or"); doubt added to Not yet confirmed.
5. APA missing information: "lapses" corrected to "treated as withdrawn" (art 26(4)).
6. Art 60 conditions added wherever the TP skill applies 15% (secondary-rule row, payments abroad, secondary adjustment, example 1).
7. Sources: Order's full title; TPL read list includes arts 14 to 16.

XB (`rw-cross-border.md`):
1. Art 60 rates row: added items 6 (goods sold in Rwanda) and 7 (profits converted into shares), the art 47 resident-dividend exclusion and tax-exempt payers; item numbers cited.
2. PE exclusions: removed "display stock" (not in ITL art 5).
3. Added that a non-resident entity without a PE is outside CIT (ITL arts 44 item 7, 47), so the 15% is in practice its only Rwandan income tax; the finality question now narrowed to individuals.
4. Repatriated profits: flagged that the art 60 first-paragraph condition is not adapted for a head-office remittance.
5. Treaty precedence: added Constitution art 95 (ratified treaties above ordinary laws) with a Sources row.
6. FTC certificate wording corrected to the Handbook.

No change to the README rows: rendering `scripts/build-pack-readmes.py`'s `build()` for `skills/rwanda` gives text identical to the file.

## Note on the art 60 question raised for review

The concern was that "applies only where the payee is unregistered or has no recent declaration" confused art 60 with art 63. It does not. The English column of ITL art 60 (Gazette p. 80) reads: the 15% "is levied on payments made by resident persons including tax exempt persons if such payments are made to a person not registered in the Rwandan tax administration or to a registered person who does not have recent income tax declaration." Art 63 repeats the same condition for public tenders. The skill was right; the text now says where the condition sits.

## Examples recomputed by hand

- TP 1: (0.03 - 0.005) x 5,000,000,000 = 125,000,000; x 0.28 = 35,000,000; 125,000,000 - 35,000,000 = 90,000,000; x 0.15 = 13,500,000; total 48,500,000. Correct.
- TP 2: 600,000,000 - 550,000,000 = 50,000,000; 100,000,000 - 95,000,000 = 5,000,000; 120,000,000 - 100,000,000 = 20,000,000; 120,000,000 x 0.05 = 6,000,000. Correct. Company A passes both art 19(2) limbs; Company B fails both; B meets art 28(1)(b) but not (c). Correct.
- XB 1: 40,000,000 x 0.15 = 6,000,000; net 34,000,000; 40,000,000 - 25,000,000 = 15,000,000; x 0.28 = 4,200,000; 6,000,000 - 4,200,000 = 1,800,000. Correct.
- XB 2: 1,000,000,000 x 0.28 = 280,000,000; 200,000,000 x 0.28 = 56,000,000; min(70,000,000, 56,000,000) = 56,000,000; net 224,000,000; unrelieved 14,000,000. Correct.
- `python3 scripts/check-examples.py --require` on both files: 2 blocks each, 0 failures. `skill_checks.run_all` on both files: `{}`.

## Still not confirmed

- Whether the full local file and master file are filed with the return (TPL art 16, O003 art 18(1)) or only produced on request (O003 art 18(2)).
- O003 art 19(2): whether one limb or both must be met.
- O003 art 21(1): whether all four service tests or any one.
- Declaration date for a company with an approved non-calendar tax period.
- Collection of withholding on an art 40 deemed dividend.
- Base of the art 81 item 9 fine before doubling.
- Finality of the 15% for a non-resident individual; measurement of repatriated profits and how the art 60 payee condition applies to a head-office remittance.
- Whether a constitutional revision after 2015 changed art 95 (only the 2015 text was available on RwandaLII); interaction of ITL art 68 with treaties.
- Treaty list and rates; whether an art 50 bis Order has been issued (none on LPR on 2026-11-02); APA portal status; CbC threshold.

## Possible issue in rw-corporate-income-tax (not edited)

Its deadline table gives "31 March 2027 for 2026, or 3 months after an approved year-end". ITL art 9 as amended by L051 art 1 and art 10 state only 31 March; the 3-month rule found in the read texts is ITL art 45(2) as amended by L014 art 3, for exempt persons' statements. Worth a check in that skill's own PR.

## Unreachable sources

None blocked. RwandaLII's HTML page for the Constitution renders the text client-side; its source PDF (the Gazette copy) was read instead. No CAPTCHA was met.
