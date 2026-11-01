# Independent Somalia review: initial three-Guide freeze

This report concerns candidate `49415f0ac633ca5eb547d0f2445fc99e6892b1ab`, compared with actual base `59c23acba2ad66dd2bb29ffc81ffbb9289769ef8`. It is initial evidence only. Sales-tax/formation additions and the eventual five-Guide freeze have not yet been accepted.

Read `AGENTS.md`, `CONTRIBUTING.md`, `docs/OWNERS.md`, `docs/skill-template.md`, all three changed Guides, every row of the 55-unique-row ledger and the rendered per-Guide ledgers. Checked the actual primary clauses and neighbours, using OCR as locator and the original page scans as authority. Cached files were reused as authorised; hashes were independently recomputed. No independent re-download claimed. Actual scope is in `frozen-three-read-scope.json`.

**Initial result: revise the payroll example assumptions and five ledger quotations.** All 55 substantive ledger rows are supported within the declared conditional statutory baseline, with the worked-case condition defect below. This is not operative-2026 approval, a filing-ready method, country completion or accountant attestation. Arithmetic does not settle implementation, the annual table conflict, real taxpayer facts or the live submission path.

## Findings requiring writer correction

**F1, condition completeness: specify primary employment in both payroll examples.** `so-payroll-social.md`, first worked case, assumes “ordinary resident employment” and computes USD84 on USD1,000. The following case imports the same assumptions. Regulation90-2(4), PDF27 (printed25), requires a secondary employer to “withhold tax at the highest rate” and expressly says “without any reduction under Regulation90-1(3)”. At that highest18% rate, the same USD1,000 gives USD180. The Guide explains the distinction correctly earlier, but each worked-case assumption should explicitly say primary employment. Keep the numerical examples unchanged on that assumption. [Official regulation](https://mof.gov.so/sites/default/files/Publications/Income%20Tax%20Regulation_%200141%2C%202025.pdf).

**F2, evidence transcription: fix OCR q/g errors in exact quotations.** The following five rows summarize the law correctly but do not quote the printed source exactly. Correct `rule-rows.json` and every rendered per-Guide ledger where the row appears. Declared whitespace/line-break and apostrophe normalization is accepted; it does not explain a letter substitution. [Official Act37](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).

| Ledger row | Primary clause / page | Current error | Visually verified wording |
|---|---|---|---|
| SO-022 | Art90(1), PDF109 | `loo shageeye` | `loo shaqeeye` |
| SO-034 | Schedule1 art1(2), PDF127 | `bogolkiiba labaatan (20%)` | `boqolkiiba labaatan (20%)` |
| SO-035 | Schedule1 art1(3), PDF127 | `bogolkiiba shan iyo toban (15%)` | `boqolkiiba shan iyo toban (15%)` |
| SO-036 | Schedule1 art1(4), PDF127 | `bogolkiiba siddeed iyo toban (18%)` | `boqolkiiba siddeed iyo toban (18%)` |
| SO-037 | Schedule1 art3, PDF128 | `bogolkiiba shan iyo toban (15%)` | `boqolkiiba shan iyo toban (15%)` |

No Guide, ledger, Git state or PR was edited by the reviewer. The writer must bind fixes to a new freeze; targeted recheck remains required. Findings were sent privately to the writer.

## Substantive conclusions checked

The annual statute visibly prints USD1,788 at the top-band entry. The lower-band computation gives USD1,728, and the Directorate monthly entry gives USD144. The Guide holds that USD60 conflict rather than silently amending the statute; both annual cases stay below that band. The minority exception requires the Ministry's written confirmation and satisfaction as to all included amounts, not an AI conclusion. Non-resident natural-person18% is distinct from ordinary corporation15% and PE/withholding charges. [Act37 Schedule1, PDF126–129](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).

The95% business-deduction ceiling is explicit in art16(t)(ii), PDF41, and art23 defines the statutory loss against95% of included amounts. The corporate examples correctly distinguish accounting profit and statutory income and do not assume an automatic carryforward. Capital expenses, inventory, loss order/rate matching, cash/accrual distinctions, reliefs, final withholding/credits,14-day remittance,30January/30day employee certificates and31March/noncalendar30thday returns were checked with neighbours. All relevant row outcomes are in `frozen-three-row-review.json`. [Act37 arts16–28,93–103](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).

Regulation9-1 is an individual-only presumptive regime. It is not the company turnover regime suggested by the Directorate summary. Eligibility, professional/property exclusions, election period, quarterly higher-of37.50/1.5%, defined cash turnover and the105-1 transition increases **by**250/200/150/100/50% all match the regulation. The actual implementation-year and circular gates remain unresolved. Regulations90,105-8 and106-1/107-1 support the employer-choice, postponement and territorial-allocation gates. The annual report describes delays/plans, not a precise public notice. [Official regulation](https://mof.gov.so/sites/default/files/Publications/Income%20Tax%20Regulation_%200141%2C%202025.pdf), [official Directorate monthly table](https://revenuedirectorate.gov.so/direct-tax), [Annual Report2025](https://revenuedirectorate.gov.so/sites/default/files/Annual%20Revenue%20Performance_2025_FINAL11.pdf).

## Recalculation, predecessor preservation and checks

Independently recomputed six cases: adultUSD1,008; minorUSD2,400 versusUSD1,008, differenceUSD1,392; companyUSD4,500; ceiling caseUSD750 versusUSD450, differenceUSD300; monthlyUSD84/netUSD916; reimbursementUSD84/netUSD1,116 versus allowanceUSD108/netUSD1,092, differenceUSD24. Source conditions are as above; F1 remains a correction to assumptions.

All37 nonempty pre-CTA body lines in the three predecessors have individual destination-map rows:13corporate,13income,11payroll. Every old text/line/blob/SHA matches immutable base, and the three baseline files are byte-identical. Manual review confirms old rates are held explicitly, rental/WHT/source/registration topics remain identified, and employer/social/rate/cap claims are held rather than erased or inferred zero. Complete platform CTA suffixes and platform-owned metadata are unchanged. The five other Guides, including prior TP/XB, and historical review evidence are unchanged at this initial freeze. **Lost content restored:0.** No Guide shrank or was deleted/merged.

All15skill checks pass for all3Guides; changed-only validation with `--no-index-check` passes3Guides with0warning groups;6required executable cases pass; strict metadata sync against actual base/head passes3Guides with0errors/warnings/notices; whole-base `git diff --check` passes. Exact outputs and hashes are in `frozen-three-mechanical.json`.

Probe limitation: `validate-guides.py --help` is unsupported and ran full-tree validation instead. It reported stale generated index/llms files and two legacy Guides' warning groups. No generator ran. The intended bounded checks above passed; this incidental full-tree result is not concealed or treated as acceptance evidence. Web PDF reads failed on source access/length, so the actual scan review used the authorised original cache. No access-control bypass occurred.

## Items not confirmed

Precise operative implementation/postponement dates and later inflation/allocation/employer notices; annual top-band correction and fractional-dollar boundaries; complete modified-cash, pension/charity, depreciation/interest/repair/loss, source/PE/treaty/foreign-credit/CFC and asset disposal methods; sanctions/interest/appeals; social/pension rates and coverage; complex payroll/benefits/arrears; live registration/FormTR1, workbook fields, upload/payment/acknowledgement. None is treated as zero, absent or complete. The two additional Guides and refreshed README/map await a second freeze and separate source review.
