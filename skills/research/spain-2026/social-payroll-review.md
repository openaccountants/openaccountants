# Independent national social/payroll review, 9784b7b4

Reviewed 27 October 2026. Frozen commit: `9784b7b45b9ed5bef2d618b2fe9786fe4faa6e9c`. Scope: `skills/international/spain/es-social-contributions.md` and `spain-payroll.md`. This reviewer did not write either Guide. No source Guide edits, commit, push or accountant attestation. **The two-file freeze is released.**

The four worked examples recompute, and the new household/agricultural/part-time methods agree with the checked primary rules. Three small corrections are needed: restore an explicit ordinary descendant-eligibility condition, adjust the historical May payment deadline for the preceding-business-day rule, and restore the original bar on later recovery of an employee contribution not deducted when salary was paid. The remaining December special-IT detail is mainly **enacted-law implementation**, not an external legal blocker.

## Findings and exact correction text

### SP-01 [P2] Restore the ordinary family-minimum eligibility method

`spain-payroll.md:83–85` retains amounts and says that other age/cohabitation conditions apply, but the original explicitly supplied the under-25 condition. A user cannot determine the ordinary child entitlement solely from the revised table. Add after the paragraph ending “ascendants/disability as well”:

> A descendant must be under 25, or disabled at any age, and live with the worker or meet the statutory economic-dependence rule, with annual income excluding exempt income no greater than 8,000. Apply the judicial child-support exception rather than counting the same child twice. For adoption or qualifying fostering, the 2,800 supplement applies in the registration/qualifying-resolution year and the following two years regardless of the child's age. For an ascendant, apply the over-65-or-disability and 8,000-income conditions and require cohabitation for at least half the tax period, or half the elapsed period if the ascendant dies. These withholding calculations continue to ignore the relative's own-return condition under RIRPF art. 84.

Sources freshly fetched/read: [LIRPF58](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a58), [59](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a59), [61.5](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a61), [RIRPF84](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a84). The first sentence restores an ordinary condition; the adoption/ascendant clauses close the same ordinary computation route.

### SP-02 [P2] Correct the operative historical catch-up payment date

`es-social-contributions.md:271` says the self-assessment window ran through31May2026. DT1 supplies the nominal calendar endpoint, but the Social Security collection regulation moves an endpoint on a nonbusiness day **backward**, not forward.31May2026 is Sunday. Replace its self-assessment sentence with:

> Self-assessment differences from 1 January had a nominal no-surcharge endpoint of 31 May 2026. Because that was a Sunday, RD 1415/2004 art. 8(b) moves the payment endpoint to the preceding business day, ordinarily Friday 29 May 2026, subject to the applicable holiday calendar. This historical window is closed.

Sources freshly fetched/read: [PJC297/2026 DT1.3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#dt), [RD1415/2004 art8(b)](https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836#a8). The April30 base-election window agrees with DT3. General notices retain their individual dates; the May29 example must not replace them.

### SP-03 [P2] Restore the employer's missed-deduction consequence

The original payroll Guide explicitly included LGSS142.2; the revision's gross-to-net method omits it. Add after the cash-net/employer-cost paragraph at `spain-payroll.md:140`:

> Deduct the employee contribution when remuneration is paid. If the employer fails to deduct it at that time, LGSS art. 142.2 bars recovering it from the employee later and requires the employer to pay the entire contribution at its own expense.

Source freshly fetched/read: [LGSS142.2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a142). This is a substantive original payroll safeguard, not an additional specialist topic.

## December special IT: implement the enacted branch

The Guide's existing December full-time BR and process-start distinction agree with [RDL31/2026 art1.4/1.6,DT1,DF4](https://www.boe.es/buscar/act.php?id=BOE-A-2026-21872). The legislation explicitly establishes the special situations and payment start. The unfinished list/day-rate treatment should be classified as **remaining implementation**, not awaiting an external clarification. Suggested replacement for the special-situation portion of line168:

> For special common-IT processes beginning from 1 December 2026, the employer pays full salary on the leave day and the common-IT entity/mutua bears the subsidy from the next day. The listed situations are secondary incapacitating menstruation, pregnancy interruption, gestation from the first day of week39, organ/tissue donation, the specified coded secondary menopausal disorder, and the specified injuries from gender violence with the statutory medical/documentary proof. Donation pays100% BR from day2. For the other listed special situations, apply the common-IT-equivalent amount:60% BR for days2–20 and75% from day21. No prior contribution minimum applies to art169.1.a situations1/3/4/5; the39th-week route uses the age-specific art178 contribution test. Apply the still-operative childbirth/risk-benefit termination rule in art173.2. DT1 confines these changes to processes beginning from entry into force; do not reset an earlier continuing special process.

Sources: freshly fetched [RDL31/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-21872), art1.3–1.6 (amended169/171/172/173),DT1,DF4; [Social Security ordinary percentage schedule](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/PrestacionesPensionesTrabajadores/10952/28362/28365/30791?changeLanguage=es). The60/75 mapping combines the expressly imported common-IT amount with amended173's special payment start; it is a statutory implementation inference, not a separately published new percentage table. Keep that provenance in the review evidence. The new menopause/gender-violence medical coding and qualifying documents remain factual eligibility gates, not uncertainty over the existence of the enacted route.

## FOGASA: published numbers pass; a matching reconstruction exists

The official FOGASA FAQ was re-read through web after direct urllib failed its certificate chain. It publishes94.78/day,11,373.60 wages and34,594.70 indemnity for2026 causes. Both multiplications pass. ET33's120-day/one-annuity limits,41.3 nine-month exception and50/56 thirty-day indemnity basis match the Guide.

A **derived reconstruction** matches the published daily module:

`round(2 × (40.70 + (2 × 1,221 /365)), 2) =94.78`.

This uses the published daily SMI plus two monthly extras allocated over365 days, then doubles and rounds the daily module before multiplying by120/365. It does not use `40.70×14/12`. [SMI art1/4](https://www.boe.es/buscar/act.php?id=BOE-A-2026-3815#a4) establishes the daily/monthly inputs and the two30-day extras; [ET31/33](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430#a33) establishes extras/FOGASA's capped module. No official source in this bounded pass explicitly printed that exact denominator formula. The numbers themselves are directly primary-sourced and executable; distinguish a matching reconstruction from a claim that the agency explicitly published the formula. No replacement monetary amount is required.

## Preservation result

**Lost content restored:17 topic families confirmed within this review's two-file scope**, using the writer's stated counting convention. The other13 of the writer's30 belong to VAT/rental and are not attested here.

- Social3:2025 solidarity comparative thresholds/splits;2026 catch-up/base-election windows; signed current-year RETA settlement expense/refund/excess-income booking. The deadline qualification above remains required.
- Payroll14: short-term SMI; external household hourly SMI; qualified nine-hour day; continuous-day break; public holidays; Christmas extra pay; employee IT amount/payer/BR; birth benefit; shared nursing-infant benefit; fixed-term expiry indemnity; employer death/retirement/incapacity; objective-termination notice; FOGASA framework/published limits; retirement-age retained common-IT contribution.

The original's errors are correctly replaced rather than preserved: using total accrued payslip items as taxable withholding cash, applying annual-return other-income restrictions to the withholding reduction, monthly-count instead of calendar-day RETA averaging, assumed combined-rate claims, and a territorial tax-administration refusal for statewide contributions. Original A1/non-EU coordination and historical individual severance/leave transitions remain explicitly bounded. SP01 andSP03 identify two separate original safeguards still needing restoration.

## Checked figures, source gates and tests

Fresh primary-source reading covers the RETA bands/component rates/floors, signed regularisation and deadlines; ordinary/group/daily/part-time bases; overtime/MEI/solidarity2025/2026; household all eight salary bands,20/80 relief and recognised45 replacement; agricultural all monthly/daily groups,22-day switch,2021→2026 reduction formula,monthly/daily CC floors/caps,55-day inactivity reduction,1.3636 factor and protected-period components;2026 SMI and restored labour/benefit/termination figures; and ordinary withholding inputs, scale,quota limit,rate truncation and recalculation examples. The3 formula images were independently viewed and agree with the written two-stage agricultural formula.

The automated source-linked table inventory has **503 numeric-token occurrences /263 distinct values**, including group/year identifiers. It is saved for triage and must not be represented as503 independent legal conclusions. The substantive review above checks context and gates as well as matching numbers.

- **4 oa-checks pass**,0 failures,0 missing; output `examples.txt`.
- **72 independent Decimal/date/boundary controls pass**, in `controls.json`; includes household every band edge,SMI actual base,agricultural floor/interior/cap/inactivity,2025/2026 solidarity boundaries,part-time floors,IT payer splits,FOGASA module/caps,RETA discrepancy and withholding results.
- **20 fresh source body hashes verified**, plus both frozen Guide hashes and nine authoredH2/two examples per file, in `sources.json` and `hashes-structure.json`.
-21 primary fetches attempted:20 succeeded;FOGASA raw fetch had an SSL-chain failure and was read from the official page through web instead (`fogasa-web-read.json`,no fabricated raw hash). Existing formula PNGs were independently viewed.
- `validate-guides.py --no-index-check` passes with the three repository-wide warning groups. An initial invocation with unsupported `--help` ran the full validator and reported the expected deferred **stale index.json** error; no source changes were made to hide it. The correctly scoped no-index run is saved in `validation-no-index.txt`.

## Ordinary partial coverage versus factual/specialist limits

**Real primary conflicts remain open:**2026 starting-fee monetary authority and TGSS80+MEI total88.64 against its stated950.98 base and0.9% (arithmetic gives88.56); TGSS31.40 combined figure versus its own listed components summing31.50; and the reduced-fee extension's equality-at-SMI interaction between art38ter's `<`/`>` wording and RD2064 art44.3.f's `≥`. The Guide correctly records these and follows the contribution order for ordinary full-rate computation. They cannot be closed by pretending the old2023–2025 monetary provision expressly fixes2026.

**Ordinary subsets still incomplete:** the uncertain new2026 reduced-fee amount/equality branch; the cessation-benefit monetary IPREM cap; the three small corrections above; and the straightforward December special-IT implementation described above. These are not all niche cases. Full-rate RETA,ordinary paid employee contributions,household ordinary20/80 and agricultural-employee computations are substantively supplied.

**Factual/specialist limits:** actual occupational tariff,qualifying family/benefit awards,collective-agreement top-ups,medically coded events,non-EU applicable-law determinations,case-specific ERTE exemptions,and sea/artist/training/SETA methods. These require their own facts or designated methods and do not invalidate an ordinary domestic computation. No live AEAT service parity result or accountant attestation is claimed.
