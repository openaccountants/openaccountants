# Independent North Macedonia country-pack review

Reviewed immutable commit: `39ab9ebefcb5fb54b924372568a70c83faca613a`. Read date: 24 October 2026. Reviewer: a fresh independent Codex agent. This is a source/arithmetic review of a **tier 2 source-cited draft**, with no accountant sign-off.

**Result: closure required.** Five material source/computation or procedure omissions need correction. One accessible parameter improvement is recommended. All 14 examples and all 61 expected values independently recompute exactly. The country remains partial in IT-IND, SC, PR and XB.

## Source and review method

Independently retrieved 27 official URLs with separate receipts (13 PDFs, 14 HTML pages). Independent pdftotext for digital PDFs; independently rendered/OCRd all 39 PIT pages in Macedonian and visually inspected 7, 38, 39. Writer OCR used only as secondary navigation/cross-check to identical independently fetched statutory bytes. No unsupported secondary source used for law.

All 27 official URLs returned HTTP 200. Actual law PDFs independently match the writer-held statutory hashes. Monetary content on the dynamically rendered allowance page was re-read, rather than assuming HTML hash equality. Detailed URLs, hashes, retrieval times and local evidence paths are embedded in `independent-review.json` and in `reviewer-sources/manifest.json`.

The review read AGENTS.md, both canonical templates, GOAL.md, all seven computational Guides, the README, actual cited laws/implementing instruments, and the three supporting files for scoped contradictions. Source retrieval is evidence, not legal/professional attestation.

## Findings

### MK-R 1 [P 1] Apply the 2023 securities acquisition boundary and FIFO before calculating gains

Location:`skills/international/north-macedonia/north-macedonia-income-tax.md:59`.

The ordinary capital-gains instructions include securities/fund units without the statutory acquisition-date boundary and do not specify FIFO. Applying the paragraph to a 2026 sale of pre-2023 acquired securities can tax an excluded acquisition; using a chosen/average lot instead of FIFO changes the taxable gain. The acquisition date of the predecessor also matters for gifts/inheritances.

**Fix:** Add the 1 January 2023 acquisition boundary, including predecessor acquisitions, and chronological oldest-to-newest FIFO for the covered securities/fund calculation. Make the lot-acquisition history an intake fact. Route the cross-border guide to the same rule.

**Source:** [Gazette 274/2022 amending Act, transitional arts.21-22, consolidated PDF pp.38-39](https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf).

### MK-R 2 [P 2] Separate the domestic securities annual assessment route from ordinary monthly e-PDD

Location:`skills/international/north-macedonia/north-macedonia-income-tax.md:68`.

The filing section gives only the general monthly self-assessment timetable and does not explain the specific domestic securities/fund assessment machinery for the gains already covered in the base. This leaves a reader without the correct filer, annual assessment date or payment trigger.

**Fix:** State that the Central Securities Depository/fund managers report by 15 January next year, UJP assesses using the statutory reports by 15 February, and assessed tax is due within 15 days of service. Distinguish foreign receipts requiring self-reporting under arts.87-88 from this domestic reporting route. Do not imply that every security sale is a monthly domestic self-assessed sale.

**Source:** [PIT arts.85-a, 87(1)(2), 91-a, 93(4), PDF pp.25-29](https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf).

### MK-R 3 [P 2] Give the statutory fallback for unsupported sole-trader loan interest

Location:`skills/international/north-macedonia/north-macedonia-income-tax.md:49`.

The base says to add back excessive loan interest but omits the expressly prescribed fallback when the taxpayer cannot document the bank-comparable rate. The TP sole-trader paragraph does not supply it either. A preparer otherwise cannot determine the deductible ceiling in an ordinary undocumented-comparator case.

**Fix:** Explain the matching-maturity EURIBOR (foreign-currency loan) / SKIBOR (denar loan) plus one percentage point fallback, with evidence and correct period. Keep vehicle-loan exclusions separate. Corporate Profit Rulebook art.4 also contains its own corresponding related-party interest fallback; review and state that applicable rule in the corporate/TP financing route rather than silently importing PIT into CIT.

**Source:** [PIT art.27(7), PDF p.11](https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf).

### MK-R 4 [P 2] Date the 2026 change in who calculates lump-sum self-employed contributions

Location:`skills/international/north-macedonia/north-macedonia-social-contributions.md:23`.

The undated statement assigns calculation to UJP for assessed lump-sum taxpayers across a guide covering all 2026. UJP explicitly describes this as a July amendment changing the previous self-calculation administration. The correctly dated contribution-rate tables do not date this separate administrative change.

**Fix:** Tie UJP calculation to the July 2026 amendment/current-law period and preserve the pre-amendment self-calculation route for earlier periods/corrections. Obtain the amendment/operative instruction for an exact operational cutover rather than assuming every January-June original or correction falls under the current administration. Payment remains with the taxpayer.

**Source:** [Contributions Law art.13(1)(2), Gazette 148/2026; UJP notice 13 July 2026; official law landing shows validity 6 July 2026](https://ujp.gov.mk/en/javnost/soopstenija/pogledni/1266?print=1).

### MK-R 5 [P 2] Make the own-agricultural-products refund and registration tests usable

Location:`skills/international/north-macedonia/north-macedonia-income-tax.md:57`.

The covered category is reduced to 80% costs and an unspecified conditional refund. It omits the 1, 000, 000 threshold, the activity-registration trigger and deadline, the other-income test and the distinct refund process/deadline. Those are ordinary rules directly available in the cited law.

**Fix:** Add art.45 total annual income exceeding 1, 000, 000 registration by 15 January next year. Add art.46 own-product income not exceeding 1, 000, 000 refund test, other taxable income disqualification with the stated free-input exceptions, treatment of exempt income/art.13, confirmed annual-return/ministry verification and refund by end of the following year. Keep registered business farmers and market-stall regimes separate.

**Source:** [PIT arts.43-46, PDF pp.15-16](https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf).

### MK-R 6 [P 3] Fill the accessible 2026 first-year advance parameter

Location:`skills/international/north-macedonia/north-macedonia-income-tax.md:69`.

The first-year advance formula is correct, but the published January net-wage parameter is readily available and is absent from a 2026 computational guide.

**Fix:** Add the January-published net wage 45, 961, derived half-wage base 22, 980.50 and 10% analytical monthly advance 2, 298.05. Cite both the official release and art.94(2), and preserve the guide's operational-rounding qualification. Do not substitute the 69, 141 gross contribution reference.

**Source:** [PIT art.94(2); State Statistical Office release 23.3.2025.1/11 published 21 January 2026](https://www.stat.mk/en/stat/population-and-living-conditions/labour-market/average-monthly-net-wage-paid-per-employee/average-monthly-net-wage-paid-per-employee-november-2025/).

## Figures and ordinary coverage examined

| Domain | Verified scope and result |
|---|---|
|IT-IND|10%/15% rates; 183 days/12 months; 10, 932 monthly/131, 184 published annual reduction and actual-used restriction; rent 10%/15%; industrial rights 10%; copyright 50/40/30/20%; agriculture 80%; 90% entertainment/50% vehicle add-backs; investment 30%, 50% cap, 5-year retention; EUR 500/>1-year depreciation, 50% permitted rate uplift, 31 January unusable-asset request; capital gain 10% deemed costs, 3-/5-year property conditions and separate securities exemptions; lump-sum one employee/two annual gross-wage eligibility/form deadlines; advances 1/12, first-year 50% net wage, 10 th/15 th reporting/payment, 31 March foreign taxed salary/pension; 15 March business filing, 15-day balance;30 April/31 May/30 June annual route;15-day assessment difference/60-day refund; art.107100-250/50-250 and art.108 remitter-size fines; 0.03% daily interest. Existing printed numerical parameters supported; material ordinary securities/agricultural/interest omissions in findings; business-loss partial remains.|
|IT-CORP|10% profit and gross WHT; 3 m/6 m revenue bands, 1% entire revenue, 3-year election; nonprofit 1% excess over 1 m; 90% entertainment;5%/3% donation/sponsorship caps; 3-year loss window from loss year, oldest first, 31 March application/60-day approval; 20% nonresident holding/3-times equity/first 3 operating years exclusions; 5-year reinvestment/5 fold consequence/30-day DD-DO; EUR 500/>1-year assets/50% depreciation uplift/31 January writeoff consent; February/electronic 15 March annual-account rule, 30-day payment, 1/12 price-adjusted advances, 15 days monthly; 60-day refund decision; company fine ranges 600-2000, 1200-4000, 3600-12000, 6000-20000 and 300-1000, 600-2000, 1800-6000, 3000-10000; 0.03% interest. No incorrect printed amount identified; related-party interest fallback should be supplied under MK-R 3; current-year specialist exclusions explicit.|
|VAT|18%/5%/10% statutory rates; 2 m turnover threshold inclusive of relevant VAT, 25 m quarterly boundary; 3 calendar-year registration/2 preceding-year early removal; 5-/10-year capital-input correction and 1/5, 1/10 annual fractions; 6, 000 fiscal-receipt input limit; 15 January, 15 days commencement, 15 th following crossing month registration; 25-day returns/payment/cessation, 15-day assessment payment, 30-day refund; fine ranges and responsible-person ranges; 0.03% current interest;0.05% historical art.44 inoperative since 1 April 2006. Supported. Read operative post-2024 art.14, foreign-person threshold exception/reverse charge, taxable/exempt bases, blocked input and final annual allocation. Product/special schemes explicitly routed out.|
|SC|January-June 18.8/7.5/0.5/1.2%;July-December 19.9/7.5/0.5/0.1%; employee 28% both periods;self-employed 26.8/27.9%;uninsured director 26.3/27.4% by statutory group; 69, 141 reference;published 34, 570 minimum;professional 69, 141;16-times 1, 106, 256;12-times 829, 692;farmer 20%=13, 828.20 before operational rounding; extended-service 12: 18/17/16/15/14/13 rates 9.4/7.83/6.27/4.7/3.13/1.57% then 9.95/8.29/6.63/4.98/3.32/1.66%; MPIN 10 th;contribution maturity on payment or 15 th for unpaid ordinary wages;director exception; 15-day employee statement/15 February annual summary; fine ranges, 3-30-day restriction, 0.03% interest. Supported fund eligibility/rates, including both 2026 periods. Administration needs date under MK-R 4. Professional first-year interaction and ordinary reduced-hours bases remain unresolved and correctly flagged.|
|PR|10% PIT;10, 932/131, 184 reduction;1% private vehicle valuation; both 2026 fund splits;34, 570 floor/1, 106, 256 cap; MPIN 10 th;PIT at payment;contributions unpaid-wage 15 th distinct; 15-day statement/15 February annual summary;30 April/31 May/30 June PIT and 15-day assessment; company/responsible-person fines and 0.03% interest. Supported full-month formulas, benefits category distinction, no allowance on standalone director fees and no cap on PIT. Partial remains for unresolved reduced-hours contribution bases.|
|TP|300 m revenue exclusion applies to arts.12 and 12-a;domestic resident transactions excluded; 10 m shortened-report boundary; 20% ownership/vote/profit/loan definitions;25%-lower foreign rate relationship; 25 th-75 th percentile range/median outside; 10-year retention/15-day request response/30-day earliest request following DB deadline; 10% tax effect, fine ranges, 0.03% interest. Supported corporate scope/methods/documentation and no automatic downward adjustment. Add PIT/corporate unsupported-interest fallback under MK-R 3.|
|XB|10% PIT/CIT/listed gross corporate WHT; 183 days/12 months residence; construction>6 months;services>90 continuous days/12 months with<=7-day interruptions; 10% corporate foreign-credit cap;individual domestic-tax cap; 30-day relief/certificate decisions; DD-I 15 February;foreign salary/pension 31 March;ordinary 10 th/15 th;annual 30 April/31 May/30 June; fine ranges, 0.03% interest. Supported income categories, PE, gross-up, credit, certified corporate/individual relief/refund forms and registration/cessation. Securities route must inherit corrected PIT rule. No nil exit-tax inference; standalone departure issue remains partial.|

Ordinary bases, deductions, exemptions/blocks, loss treatment, registration/cessation, returns, payment/advance maturity, penalties, treaty-relief paperwork and credit/WHT mechanics were read across the corresponding provisions. No numerical defect was found in the printed headline rates, dated fund splits, ceilings/floors, fine scales or example amounts. The findings identify missing ordinary rules rather than arithmetic failures.

## Independent numerical controls

| Example | Independently checked outcome |
|---|---|
|MK 2026 nonresident royalty gross up|gross=1.0000 E+5; withholding=10000; recipient_cash=90000; exact match|
|MK 2026 foreign profit credit cap|local_tax=10000.0; credit=10000.0; residual=0; excess_foreign=8000.0; exact match|
|MK 2026 CUP expense adjustment|actual_cost=120000; allowable_cost=100000; adjustment=20000; extra_tax=2000.0; exact match|
|MK 2026 outside range median adjustment|actual_markup=0.02; benchmark_revenue=856000.00; adjustment=40000.00; extra_tax=4000.000; exact match|
|MK 2026 corporate reconciliation|base=2110000.0; tax=211000.00; balance=31000.00; exact match|
|MK 2026 turnover election whole revenue|tax=50000.00; balance=20000.00; exact match|
|MK June 2026 self-employed fund split|base=50000; pension=9400.000; health=3750.000; injury_health=250.000; total=13400.000; exact match|
|MK July 2026 professional minimum base|base=69141; pension=13759.06; health=5185.58; injury_health=345.71; total=19290.35; exact match|
|MK 2026 ordinary VAT period|output_tax=180000.00; input_tax=72000.00; payable=108000.00; exact match|
|MK 2026 reverse charge restricted deduction|reverse_output=18000.00; deductible_input=10800.000; payable=7200.000; exact match|
|MK June 2026 ordinary salary|pension=9400.000; health=3750.000; injury_health=250.000; unemployment=600.000; contributions=14000.000; base=25068.000; pit_tax=2506.8000; net=33493.2000; exact match|
|MK July 2026 salary above insurance cap|insurance_base=1106256; pension=220144.94; health=82969.20; injury_health=5531.28; unemployment=1106.26; contributions=309751.68; base=1179316.32; pit_tax=117931.63; net=1072316.69; exact match|
|MK 2026 unfurnished rent|costs=24000.0; base=216000.0; tax=21600.00; exact match|
|MK 2026 business investment cap|adjusted=920000.0; relief=460000.00; base=460000.00; tax=46000.000; balance=6000.000; exact match|

Separately checked derived first-year parameter: 45, 961×50%=22, 980.50;×10%=2, 298.05. This is an analytical value and does not settle operational filing/payment rounding. Published 34, 570 social floor was retained even though raw half of 69, 141 is 34, 570.50; no silent substitution was made.

## Remaining core gaps and closure attempts

- **IT-IND: Business-loss carryforward/cross-category relief beyond negative DLD-DB reporting.** Read PIT business base/assessment provisions and 2026 self-employment brochure/form field 22. Negative reporting is confirmed; no verified affirmative broader relief basis. Do not infer no relief or copy CIT.
- **SC: First-calendar-year professional minimum interaction.** Read Contributions Law 14(1)(14) half-reference starting base and 15(2) professional floor, plus UJP current base/rate/calculation pages. Current text supplies both rules; an explicit current authoritative resolution of the interaction was not established.
- **SC/PR: Ordinary part-time/partial-month contribution floors/ceilings outside the specific mixed work/sickness guidance.** Read arts.14-16 and current UJP steps 2-4. Hours-based gross/allowance and mixed work/sickness top-up confirmed. Search surfaced 2016 MPIN brochure with hour-sensitive wording, but that does not prove 2026 operational formula. No arbitrary calendar-day factor inferred.
- **XB: Standalone migration/deemed-disposal/exit charge and procedure.** Read PIT residence/realisation, CIT PE/status-change/liquidation, procedural tax scope, and official-source searches. None establishes a universal nil departure charge; no exclusion from absence of text was inferred.

The README partial declarations are honest and must remain. Specialist exclusions (specific VAT schemes/product decisions, top-up tax, treaty-specific rate/MAP tables, special insurance classes and regulated-sector/state-aid rules) do not create zero liability.

## Preservation and repository checks

- Five existing computational files: every protected platform field and marker-to-EOF CTA tail matches main byte-for-byte. No professional-review fields were added.
- TP/XB are new files without copied platform-owned fields or hand-stamped CTA blocks.
- All three supporting files are byte-for-byte unchanged. Their contradictions remain a separate scoped follow-up; README correctly prevents their 2025 figures overriding 2026 computations.
- Changed schema validation: 7 Guides, 0 warnings, pass. Independent Decimal controls: 14 examples, 61 exact expected values, 0 failures. Repository example runner: 14 blocks, 0 failures. Coverage report independently generated; four declared partial domains remain.
- The reviewer made no tracked repository edit and no commit. Default python lacked PyYAML; the existing support venv supplied it for scoped validation.

## Required closure

Fix MK-R 1 through MK-R 5; preferably fill MK-R 6. Re-review exact closure commit, including applicable shared PIT/XB/TP routes and protected tails. Retain genuine partial flags until primary support closes them. Do not grant tier 1 or close issue 413 as complete.

This review can be faithfully reported on the PR only with these findings and remaining uncertainties. A passing schema or example test does not clear them.
