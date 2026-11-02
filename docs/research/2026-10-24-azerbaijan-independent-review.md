# Azerbaijan independent source review, 24 October 2026

This is a separate AI source review, not an accountant attestation or a tier 1 sign-off. The reviewer did not receive the writer's research interpretation or conversation history. It read the eight Guides, README, repository `AGENTS.md`, `docs/skill-template.md` and relevant inventory before checking fresh primary sources. No Guide, commit, push, PR comment or external message was made by the reviewer.

## Reviewed revision and scope

Initial full-pack revision: **8c6a01eeb745a4a07013a297d48568061f975e54**, compared with **b1f4afab6bc0f5bc1f2d1930e992179bbcae2013**. The eight reviewed files are `az-tax-overview`, `az-corporate-income-tax`, `azerbaijan-income-tax`, `azerbaijan-vat`, `azerbaijan-payroll`, `azerbaijan-social-contributions`, `azerbaijan-transfer-pricing` and `azerbaijan-cross-border`, all under `skills/international/azerbaijan/`.

The writer subsequently supplied VAT electronic-seller and corporate expense-cap deltas for targeted review. These were read from the working-tree diff and checked against fresh downloads of Decision 387, Decision 492 and Decision 14. Corrections requested below also receive a final revision check. **Final targeted closure revision: 6321000977e7702ffe59ed084edee63c8b6f38a4.** This supersedes the writer's intermediate correction revision 88f51c485d948bd731acb4bcc24e2707ecce79b0; the final change only removes an extra EOF blank line in TP/XB. This receipt does not approve an unidentified later revision.

## Fresh source retrieval and reading

Ordinary HTTP requests used `User-Agent: Mozilla/5.0` and `Referer: https://e-qanun.az/`. No CAPTCHA was solved or bypassed. The first sandbox request failed DNS; approved read-only network execution retrieved the registered HTML. The `/framework/41048` shell was not treated as law: the actual registered `/41/f_41048.html` text was retrieved separately. Raw bytes and independently generated active-text extracts are under `work/reviewer/`; `retrieval.json`, `extra-retrieval.json` and `cit-retrieval.json` and `amendment-retrieval.json` record outcomes. Extraction removed `s`, `strike`, `del` and inline `line-through` text. The reviewer distinguished operative text, superseded passages and future commencement annotations; stripping crossed-out text alone does not resolve future commencement.

| Primary source independently retrieved/read | Fresh raw SHA-256 where available |
|---|---|
| [Current Tax Code](https://e-qanun.az/frameworks/46/f_46948.html), the cited ordinary income/profit, salary, VAT, TP, residence/PE, withholding and administration articles | `7ff76663c4ddfab65bf032f2f75394e8718cc6e209731ff588aad082fb0b08e7` |
| [Social Insurance Law](https://frameworks.e-qanun.az/3/f_3813.html), arts. 9-1–15, including 2027 annotation | `a86a4b7d2354357a0b4c97f6ee7c8fe01aeb53199d91f8030c3edd7463771faa` |
| [Medical Insurance Law](https://frameworks.e-qanun.az/0/f_80.html), arts. 15-2, 15-10–15-11, 15-24 and transition provisions | `681d82b0d7b240fae02e47e695e9c9f033d4edeadc5bfce3cd81bdcc0cffdcdf` |
| [Unemployment Insurance Law](https://frameworks.e-qanun.az/36/f_36310.html), scope and arts. 6–10 | `ab8e532d7132da455b1667c701aa330766a60d38d100318a2feb00440eabdf67` |
| [Current registered TP Rules](https://frameworks.e-qanun.az/35/f_35074.html), definitions, paras. 4–12 and Appendix Example 1 | `894310421350f8f86e7d7b110b3f5ef5bad87cc6b27efce8e6b6628af35eea20` |
| [Decision 556, current size criteria](https://frameworks.e-qanun.az/41/f_41048.html), table and notes, including higher-classification rule | `e8c6f79180432d43fd13e2a13e48dcbb08e1a526b7c801cf5624e613af4c1a77` |
| [Law 297-VIIQD](https://frameworks.e-qanun.az/61/f_61117.html), arts. 18.1 and 19.1–19.6, POS transition/commencement | `a775a81977abf3ec47bca643ad3938adc92b298dd204db0caf6479408901fa9b` |
| [Decision 387, foreign electronic sellers](https://frameworks.e-qanun.az/55/f_55514.html), current consolidated paras. 1–7 including September 2026 amendments | `dce48a0a667b180c793935a419352077d763442c9eccd1d22ac866bc9c501240` |
| [Decision 492, expense norms](https://nk.gov.az/uploads/doc/docs/674d98557ed68.pdf), all three pages, paras. 1.2–4.4 | `a38c1e1af3e50cdacf6d16d030b44dba2d48771c30bae62286c4a08d96bf3b1b` |
| [Decision 14, travel norms](https://frameworks.e-qanun.az/13/f_13154.html), domestic paragraphs, foreign Appendix 1 structure and current annotations | `45f62e3a73e9e219a971c90808bf0a8b6d8de3987776f91ed243ff4c34937371` |
| [Decision 56, employer-sector criteria](https://www.taxes.gov.az/az/post/321), paras. 2.1–2.2 | Read through fresh official-site web-search retrieval after direct TLS/timeout failures; raw hash unavailable |
| [Ministry 2026 social indicators](https://sosial.gov.az/az/faydali/sosial-odenisler), minimum wage | Read through web retrieval after direct TLS failure; raw hash unavailable |
| [STS CbCR page](https://www.taxes.gov.az/az/page/cbcr-auto-info-exchange), current implementing-rule summary | Read through web retrieval after direct timeout; raw hash unavailable |
| [DTA administration Rules](https://www.taxes.gov.az/az/page/ikiqat-vergitutmanin-aradan-qaldirilmasi-haqqinda-beynelxalq-muqavilelerin-inzibatciligi-qaydalari), sections 3–8 | Read through web retrieval after direct timeout; raw hash unavailable |
| [Official treaty register](https://taxes.gov.az/az/page/ikiqat-vergitutmanin-aradan-qaldirilmasina-dair-beynelxalq-sazisler), MLI notice and effective/application-date columns | Read through web retrieval; no individual treaty rate was asserted or reviewed |
| [STS 2026 amendment FAQ](https://www.taxes.gov.az/uploads/2026/faq/FAQ2026.pdf), POS transition discussion, pp. 12–16 | Read through web PDF retrieval after direct failure; raw hash unavailable |
| [STS 2026 wage booklet](https://www.taxes.gov.az/uploads/2026/buklet/1_16.pdf), printed p. 1 contract procedure | Read through web PDF retrieval after direct TLS failure; raw hash unavailable |

All listed sources were retrieved/read on **2026-10-24**. Browser retrieval is distinguished from a successful raw-file download; no hash is invented for it. The old 2017 `transfer.pdf` was not used to establish the current TP interval/documentation rules.

## Figure, base and deadline checks

The following checks apply to the actual assumptions and scope in each Guide, not to all possible taxpayer facts.

| Guide | Checks against freshly read law |
|---|---|
| Overview | Routing agrees with seven applicable domains. Entrepreneur/corporate 20%, VAT 18%, 200,000 rolling registration threshold, ordinary simplified 2%, 2026 private non-oil progressive salary schedule and ordinary service WHT 10% agree with the detailed articles. Annual, quarterly advance, monthly VAT/PIT and contribution cycles agree with their dedicated Guides. |
| Individual | Arts. 13, 95–102: >182-day limb, ordered residence factors, worldwide/source scope, business 20%, annual non-business 14%, foreign dividends 5%, domestic dividends 5%, interest 10%, rent/royalty 14% and specified residential rent 10%. Art. 102.1.6: 200/2,500 and 2,400/30,000 employment exemption tests. Arts. 102.1.30–.30-1 and 102.9: 75% relief, three employees/social debt, 45,000 listed-service limit, 50% mixed-activity condition and former-employer exclusion. Arts. 108, 121 and 130: expense allocation, three-year business-loss limit, no offset against other income and accounting method. Art. 152.3: 25% social-payment credit, tax cap and 2024–2026 period. Arts. 218–221: 2%, 200,000 threshold, exclusions, 30% invoiced-business test, POS threshold weighting and quarterly return/payment/election dates. |
| Corporate | Arts. 103–106, 108–121 and 130: 20%, five-year losses, depreciation 7/20/25/10% and known-life intangibles, residual method/write-off <500 or <5%, category repairs 2/5/3/8%, micro/small coefficients, 75% micro relief, 125% comparable-rate ceiling and twice-net-assets foreign-debt restriction. Arts. 109.8 and 119: 2% specified-document expense caps and tax sanctions/interest exclusion. Simplified 2%, catering 8%/qualifying POS 6% in 2026–2028, threshold weighting and regime exclusions agree. Corporate expense-cap delta agrees with Decisions 492/14 and Tax Code arts. 108.4/109.7/119.2. |
| Payroll | Arts. 98, 101–102: standard 14/25% at 2,500; private non-oil 2026 3/10/14% at 2,500/8,000 with cumulative 75/625; later 5% and 7% lower bands kept separate. Deductions 800/400/200/100/50 and largest-of-category rule checked. Technology-park 5% period checked. Article 102.2.9's new mine-clearer family category is distinguished from earlier 2026 months. Different workplaces, non-cash benefits and no automatic PIT deduction for contributions are correctly distinguished. Monthly PIT due 20th; unified quarterly report due 20th; insurance payments due 15th. Art. 58.10's 2,000/4,000/6,000 employee sanction is conditioned on the stated conduct. |
| Contributions | Social arts. 14.3–14.5: employee/employer 3/22%; private non-oil 200 and 8,000 bands and constants 6/44/786/1,214 with employer 11% above 8,000; entrepreneur 2% gross, 15–100% minimum-wage bounds; civil-contract 25%, author 15%, professional 15% net, notary/enforcement 25% of 10/5 minimum wages; fixed categories 8/5/6%, geographic 2/1.5/1 and agricultural 5/7.5/12.5% without geographic multiplier. Medical 2%/0.5% at 8,000 standard or 2,500 private; civil-contract 2%/1% at 8,000; registered self-insured 4% minimum wage. Minimum wage 400 gives floor 60/ceiling 400/medical 16. Unemployment is 0.5% each. Technology-park election four minimum wages, 2023–2032 and 15 January deadline checked without applying future 2027 amendments. |
| VAT | Arts. 153–179: 18%, zero-rate export/transport categories, 200,000 rolling/single-contract triggers, 0.5 POS weighting, 100,000/one-year deregistration conditions, payment tax point, input payment/deposit/invoice requirements, mixed-use share, 50% catering/medical turnover relief and their different periods. Monthly 20th return/payment, non-registered-agent seven-day payment, one-working-day deposit rule and 20-day/four-month refund provisions checked. Foreign-seller delta agrees with Decision 387: USD 10,000/30 days, 20-working-day review/change notification, two responsible persons, registration effective date, monthly return and separate end-of-next-month payment, selected currencies/payment-day FX, and registered versus unregistered agent collection. See VAT corrections below. |
| TP | Arts. 14-1, 16, 18: 20% ownership/votes is one relationship limb; >500,000 statement threshold only for first three classes; independent commodity class; >30 million/30% counterparty concentration. Current Rules: method preference, controlled-transaction checks below statement threshold, requested group/local/transaction information, 60 days/6,000 sanction, median correction subject to one-way tax protections. Current official CbCR page confirms prior-year >EUR 750 million, 12-month report and 30 June notification screens, with complete exceptions still partial. Advance-method agreement: three-month lead, 30 days plus two 30-day extensions, three-year letter and prior-transaction/audit restrictions. |
| Cross-border | Arts. 13/19: residence/departure condition, >=90-day domestic PE test, >30-day construction subcontractor aggregation and anti-fragmentation. Arts. 122–127: domestic WHT 5/10/14/4/6/10%, residential-rent exception, separate preferential payment 10%, PE remittance 5%, gross withholding and same-income foreign-credit cap. CFC >50% control, <=75% foreign tax comparison and >30% listed income are screens, not a completed inclusion. Art. 149.6's optional capped net-basis recomputation correctly retained. Arts. 150.3.2–.3 quarterly 20th differs from salary payment; annual 31 March and 30/15-day event notices checked. DTA consent-before-payment and five-year refund period supported. See procedure corrections below. |

Common penalties were independently checked once and compared across all eight files: art. 57.1 AZN 40 with scope conditions; art. 58.1 50% with desk-audit exclusion; art. 58.1-1 horizontal-monitoring 25%; art. 59.1 0.1% per overdue day and art. 59.2 one-year limit/field-audit assessment-date treatment. VAT art. 58.4/58.6 50% sanctions and TP/CFC 6,000/CbCR 10,000 sanctions also agree. Annual settlement by following 31 March, advances within 15 days after quarters and method notice by 15 April agree with arts. 149–152; the 75% process is correctly limited to new/no-prior-activity-or-taxable-profit cases.

## Independent recomputation

The reviewer calculated these separately using `Decimal` expressions written from the prose and law, before running the repository checker. `work/reviewer/independent-arithmetic.txt` records the results. No example formula was imported or evaluated to obtain these independent answers.

| File / example | Independently obtained result |
|---|---|
| Individual ordinary entrepreneur | 120,000 − 70,000 = 50,000 profit; 10,000 tax; 2,500 after advances |
| Individual former-employer exclusion | 30,000 profit; 6,000 tax before credit; 960 × 25% = 240 credit; 5,760 tax |
| Corporate annual settlement | 180,000 profit; 36,000 tax; 6,000 balance |
| Corporate machinery/loss | 24,000 depreciation; 46,000 taxable profit; 9,200 tax |
| Overview company | 100,000 profit; 20,000 tax |
| Overview inclusive VAT | 1,180 ÷ 1.18 = 1,000 net; VAT 180 |
| Payroll 1,000 | PIT 24; employee social 86; medical 20; unemployment 5; net 865; employer social 164; cost 1,189 |
| Payroll 10,000 | PIT 905; employee social 986; employer social 1,434; medical each 87.50; unemployment each 50; net 7,971.50; employer cost 11,571.50 |
| Contributions employee 1,000 | Employee total 111; employer total 189 |
| Contributions entrepreneur floor | Raw social 20 < floor 60; medical 16; total 76 |
| VAT ordinary | Output 9,000; input 3,600; payable 5,400 |
| VAT mixed use | 80% taxable share; credit 7,200; output 14,400; payable 7,200 |
| TP CUP export | Tax revenue 550,000; adjustment 50,000; extra tax 10,000 |
| TP purchase | Q1 105; median 115; Q3 125; deduction adjustment 25,000; extra tax 5,000 |
| Cross-border PE | Profit tax 20,000; remittance tax 4,000; combined 24,000; head-office net 76,000 |
| Cross-border net fee | Gross 100,000; tax 10,000; recipient net 90,000 |

All 16 agree with prose and expected outputs. Separately checked the official TP Appendix's unusual averaging method: 55,000/62,000/66,000/70,000 gives Q1 58,500, median 64,000 and Q3 68,000. The Guide correctly avoids replacing it with weighted interpolation. The later mechanical check reported `checked 8 files, 16 oa-check blocks, 0 failures, 0 missing`.

## Actionable findings and correction requirements

| Finding | Exact support and required change | Closure |
|---|---|---|
| P2: voluntary deregistration omitted POS weighting | Tax Code **158.2-1** applies 0.5 to qualifying POS turnover for the 100,000 test in **158.2**. Add it to the threshold row and computation paragraph. Otherwise 150,000 entirely qualifying POS receipts would be treated as 150,000 instead of 75,000. Verify commencement independently; the art. 18.1 receipt-date restriction names 155.1-1/218.1-1 and must not be copied silently. | Closed at `63210009`; threshold row and paragraph checked |
| P2: retained inventory stated without overriding credit-entitlement condition | Tax Code **159.7** overrides other art. 159 rules where acquisition in a VAT-taxed transaction carried no input-credit entitlement, and proportionately reduces the taxable amount where credit entitlement was partly denied. Qualify the VAT cancellation paragraph and corresponding XB reference. Actual entitlement, rather than whether a credit happened to be claimed, controls. | Closed at `63210009`; VAT and XB paragraphs checked |
| P2: treaty-relief application deadline absent | DTA Rules **5.3** requires DTA-03 by the end of the current income-payment quarter. Add alongside the separate **5.6–5.7** consent-before-payment requirement. | Closed at `63210009`; exact DTA paragraph checked |
| P2: foreign-credit consent attachment omitted | DTA Rules **4.2-2** requires the **4.2-1** consent letter to accompany the resident income/profit return. Add to the foreign-credit administration procedure. | Closed at `63210009`; exact DTA paragraph checked |

No wrong expected arithmetic, headline 2026 rate or false accountant approval was found. The initial draft's declared gaps were real gaps, not grounds to substitute zero tax. The electronic-seller and corporate-expense additions are source-supported targeted improvements, not a basis for changing unrelated domains to complete.

## README, metadata and publication limits

README mapping resolves IT-IND/IT-CORP/VAT/SC/PR/TP/XB to the correct existing slugs; no tax domain is marked not applicable. All eight Guides are 2026 tier 2 drafts. The two new files have no invented platform metadata or hand-added CTA. Comparing existing files with the base showed no change to platform-owned `review_status`, `license`, `authored_by`, `trust_label`, `drafted_by`, `approved_by`, `validation_status` or `validated`; existing CTA tails were identical byte for byte. Content versions and headings agree and advance where a prior version existed. No named reviewer or tier 1 attestation was introduced.

After the expense-cap delta, removing the IT-CORP partial flag is defensible for its stated ordinary-regime scope. After the electronic-seller delta, narrowing VAT's partial flag to the 25 December 2026 leasing transition is defensible. Keep IT-IND, VAT, SC, PR, TP and XB partial for the explicit unimplemented groups/calculations. CbCR exceptions, CFC attribution, preferential-jurisdiction payment interactions/list, relocation asset treatment, informal-worker medical implementation, non-employment director fees, property/fixed-receipt individual computation and the remaining deposit exemption work are not verified implementation. Specialist PSA/zone/investment/subsidy/margin regimes and treaty-rate tables remain explicit exclusions.

The unchanged formation/optimisation material is not approved by this review. The README correctly warns of its recorded conflicts and directs current computations to the tax Guides. Issue #380 should remain open because pack-wide completeness has not been achieved.

**Publication conclusion:** at **6321000977e7702ffe59ed084edee63c8b6f38a4**, publication as clearly marked **partial source-cited drafts** is defensible. All four findings are closed. No material publication-blocking issue remains within the stated scope. This review supplies no accountant sign-off and no claim that the entire Azerbaijan pack is complete.


## Final exact-revision closure

The reviewer read the complete source diff from `8c6a01eeb745a4a07013a297d48568061f975e54` to `6321000977e7702ffe59ed084edee63c8b6f38a4`. Only the declared VAT, corporate and XB content/README changes and TP/XB EOF cleanup were present in the Guides. The four requested corrections are present and accurate. Fresh Law 297-VIIQD art. 19.6 confirms 1 January 2026 commencement, while art. 18.1 expressly names only 155.1-1 and 218.1-1; the corrected deregistration treatment preserves that distinction. The electronic-seller and ordinary expense-cap additions agree with the independently retrieved primary texts. Existing platform metadata and CTA byte preservation were rechecked against the base at this final commit. The six partial-domain flags match the stated remaining gaps; IT-CORP has no ordinary-scope partial flag.

Final source Git blobs and raw-file SHA-256, obtained with `git show` from the named commit (not inferred from the working tree):

| Source file | Git blob | SHA-256 |
|---|---|---|
| `README.md` | `61ffcd989ca5532034d77a3ce6e9ed55d1183255` | `ced3b3482900c5ca8fe7204743f66028842da0add56e08debd362e661d7d21f9` |
| `az-corporate-income-tax.md` | `918203767a4abbd8e5fcbc1f71ff1a832499e37b` | `9b696863bb7cf2f01c710faf894417e8bbd887832d71c9138672f876fee2c996` |
| `az-tax-overview.md` | `6ccd19b23cf326818ad89093b44c8a31e1180d02` | `6a126054d3aadd5c821dd958eb0c08ba9b128c36dfd5e80ffc293e33539b2ede` |
| `azerbaijan-cross-border.md` | `0bec45fef693165460891b18128342951aaa465d` | `463a4a502fb3d7cf728b25a0f24d3e45efb232b5dcf3e8248c875f2cc7193a7c` |
| `azerbaijan-income-tax.md` | `1159775244d653aa90848d152cb91aadc3281f3e` | `11450a8755b753356949bb739559c9f7656997db3510a76546217bb74d6c4a8c` |
| `azerbaijan-payroll.md` | `73098e9cf9685cc44c63997362c526c7194f587a` | `fd5a8f86dc3ff3c876ad91d5df9a677035b5abfe3fd6c944289d52e559fc3218` |
| `azerbaijan-social-contributions.md` | `bcac2f4081e57343766aa88369fb71b4599bba57` | `d5df1e5f420c3aac04b373d7dd7005891ab6d25c7ec9c63ff4e6780467b58a69` |
| `azerbaijan-transfer-pricing.md` | `514d6e7b5307bd3c7e5097a96098e50f12f3bcbe` | `fe461aaf810910ff758b7091ef37b41cc738e1d77546686c057ea7ed750514a3` |
| `azerbaijan-vat.md` | `1a3d6ca5b50fe4e0bcd941d973b9e7599cfabc73` | `c2b23cefb9e77fc92c76d0cfec0ff1216121b4a3f1163760cfff8a58cb7e1248` |

This exact-revision closure covers content and source support, not an independent rerun of every software test. The reviewer independently ran the eight-file/16-block arithmetic checker in addition to the separate arithmetic above. The writer's wider test suite is outside this review receipt's attestation. No professional review metadata should be added on the strength of this receipt.
