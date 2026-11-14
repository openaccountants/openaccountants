---
name: ca-fed-t1135
description: Determine and prepare Canada's T1135 foreign-property reporting for resident individuals, corporations, trusts and qualifying partnerships. Test the actual concurrent cost amount, exclusions, residence dates, Part A or Part B, seven property categories, country and currency fields, filing evidence, amendments and conditional penalties. Use for foreign accounts, securities, rental property, trusts, joint ownership and missed reporting; distinguish this information return from income-tax calculation and other foreign-information returns.
version: 2.1
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: filing-howto
---

# Canada T1135 foreign-property reporting, v2.1

## Scope

Determine whether T1135 is required, choose the permitted reporting method, build the complete property working paper and prepare the form and filing handoff. This is Canadian reporting, including Canadian obligations concerning assets abroad. It is not another country's tax return, a complete residency or foreign-affiliate analysis, or a filing/payment authorization. T1135 reports information; it neither calculates the tax on foreign income nor replaces reporting that income on the applicable income-tax return. Even below the T1135 threshold, report otherwise taxable foreign income. [P01][P12]

The figures and legislation below were read on 14 November 2026. The actual current catalogue links T1135 E (23), which says it is usable for 2015 and later taxation years. Its form revision is not its reporting year. Use the actual client's period and the software/form accepted for that period. Preserve valid 2025 filing/amendment work; do not invent a dedicated final 2026 form. The old form's reference to IC00-1R6 is superseded for new disclosure applications by IC00-1R7. [P13][P14][P19]

This substantial replacement has no renewed professional approval. Read the actual approval attached to this version; neither Nathan Wiebe's historical approval nor an accountant listed for Canada approves this changed method. An AI source check, a Git author or a prepared form is not accountant approval.

### Answer layer

For an ordinary Canadian-dollar filer, the filing trigger is a greatest **concurrent total cost amount over CAD100,000** during the relevant resident period. Exactly100,000 does not cross it. If filing is required and the total remained **below250,000 throughout the year**, choose Part A or Part B; reaching250,000 even once requires Part B. These are not independent thresholds per account, market-value tests, or the sum of every property's separate peak. Category7's fair-market-value fields are a reporting concession, not a replacement for the filing-threshold test. Confirm residence, entity exceptions, ownership and cost before concluding. [P01][P12][P14]

## Ask the client first

Ask only for missing facts, using existing records first. Six groups change the answer:

1. **Who and when:** individual/corporation/trust/partnership, identity and actual period, Canadian tax residence and changes, first-ever resident year for an individual, death or cessation. Resolve deemed residence and treaty/nominee issues before claiming an exemption.
2. **Whose property:** legal/beneficial owner and documented share, entity/partnership chain, foreign affiliates or trusts, registered-plan ownership, and personal/active-business use.
3. **Complete timeline:** every relevant foreign account/property held or disposed of during the period, transaction dates, concurrent balances/cost amounts, source currency, acquisition/gift/inheritance/immigration evidence and year-end records. Include transfers and closed accounts.
4. **Reporting data:** each asset's category, country under its category rule, income/capital receipts, dispositions and gains/losses; dealer/trust-company eligibility and monthly country aggregates if Category7 is chosen.
5. **Currency and method:** actual functional-currency election and effective year, otherwise CAD; exchange-rate records; Part A/B eligibility and choice; original/amended filing and prior submission evidence.
6. **Filing and gaps:** applicable income/partnership-return due date, intended certified software or paper channel, signer and preparer, missing records, prior missed years, CRA demand/audit/communications and any existing disclosure application.

Collect all fifteen legacy input purposes through these groups: taxpayer type; residency; first-year status; period dates; amendment; currency election; complete property list; each cost; maxima; year-end cost/FMV; income/gains; country/institution/description; plan; use; and ownership/dealer structure. A vague first question gets a useful partial working paper, not a guessed final conclusion or a blanket refusal.

## Rates, bands and thresholds

| Item | Rule and conditions | Official source |
|---|---|---|
| Filing | Specified Canadian entity with concurrent total cost amount **over CAD100,000** at any relevant time other than when non-resident; apply entity exclusions and first-year individual exception first | ITA233.3(1),(3),233.7: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.3.html and https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.7.html |
| Part A/B | If filing is required, total under250,000 throughout permits either Part A or B;250,000 or more at any time requires B. Complete one method, not both | Actual form instructions and CRA Q&A: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1135/t1135-23e.pdf and https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html |
| Partnership entity | Combined income/loss shares of non-residents and statutory excluded taxpayer classes must be **less than90%**; nil-period income/loss has the statutory1,000,000 deeming rule. Trace tiered memberships | ITA233.3(1),(2): https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.3.html |
| Ordinary late information return | Where162(7) applies, greater of100 and25 per day, days capped100, maximum2500. No tax owing does not itself remove liability; do not automatically charge an on-time return100 | ITA162(7): https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html |
| Knowing/grossly negligent failure | Section162(10):500 × A × B minus C. A is applicable months/parts capped24; B is2 after failure to comply with a section233 demand, otherwise1; C is162(7) liability for that return. Maximum pre-offset12000/24000, not an extra automatic flat amount | ITA162(10): https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html |
| Continuing failure | Requires162(10) liability and applicable clock **over24 months**. Additional162(10.1) T1135 amount is5% of greatest concurrent total cost in the reporting year, minus liabilities under162(7) and(10), not5% added without offsets | ITA162(10.1)(e) and B: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html |
| False statement/omission | Knowing/grossly negligent participation in a false statement or omission: greater of24000 and5% of greatest concurrent total cost of specified property **in respect of which** the statement/omission was made. Distinct from non-filing penalties | ITA163(2.4)(c),(3): https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-163.html |
| Negative statutory formula | Unless specifically otherwise provided, an algebraic formula's negative result is nil, not a credit | ITA257: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-257.html |
| Reassessment | An additional3-year window under152(4)(b.2) needs both the specified T1135 filing/information failure and an income-return omission of an amount required in income from specified foreign property; includes the stated partnership route. A T1135 error alone does not establish it | ITA152(4)(b.2): https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-152.html |
| Disclosure period | IC00-1R7 applies applications received on/after1October2025; R6 is historical for earlier applications | CRA R7 opening: https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic00-1/ic00-1r7-voluntary-disclosures-program.html |
| Disclosure relief | If eligible and granted, unprompted applications normally get75% interest/100% penalty relief; prompted normally25% interest/up to100% penalties. Tax remains payable. No promised acceptance/outcome | CRA R7 paras17-23: https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic00-1/ic00-1r7-voluntary-disclosures-program.html |

All amounts above are CAD in the ordinary workflow. A valid section261 election requires its own currency reconciliation; do not read CAD100,000 or250,000 as the same number of foreign-currency units. See Method3 before using the table for that filer. Figures for other filing regimes are not interchangeable with T1135 penalties.

## The method, step by step

### 1. Identify the reporting entity and period

Apply the **specified Canadian entity** definition, not just a Canadian address or business number. The excluded resident classes in233.3(1)(a) are a mutual fund corporation; non-resident-owned investment corporation; a non-trust person or trust all of whose taxable income is PartI-exempt; mutual fund trust; trust described in108(1) trust-definition paragraphs(a)-(e.1); registered investment; and a trust whose beneficially interested persons are all in those excluded classes. Do not turn a T3 filing concession into an automatic T1135 exclusion. For an unusual trust, identify the actual statutory class before excluding it. [P01]

For partnerships, do not substitute the ordinary phrase 'Canadian-resident partnership'. Test the combined excluded/non-resident shares under the exact definition, including tiered partnerships and the nil-income/loss deeming rule. An interest in a partnership that **is a specified Canadian entity** is excluded from the investor's specified foreign property by233.3(1)(o); that condition is not simply whether the partnership happened to file. An interest in a non-qualifying partnership that holds specified foreign property may itself be reportable in Category6. Do not mechanically report both underlying partnership assets and the same partner interest. A joint venture does not itself file T1135: test each specified Canadian entity party's own property. [P01][P12]

A person who was non-resident throughout the period does not become a T1135 filer just because Canadian employment income is taxable. An individual other than a trust who **first became resident in Canada in that year** has the233.7 exception; a return after an earlier Canadian-resident period is not necessarily the first-ever resident year. It is not a corporation/trust exemption. For a later year, retest the property and threshold; filing does not automatically begin regardless of holdings. CRA's emigration practice permits reporting as if the year ended on cessation of residence; retain statutory full-year wording versus that administrative concession. Do not treat physical departure alone as tax non-residence. [P01][P02][P12]

### 2. Classify every property before aggregation

Use an inventory with asset ID, legal/beneficial owner, ownership fraction and evidence, acquisition/disposal dates, account/custodian, country facts, original currency, cost basis, use, plan/entity, income and disposition records. Three outcomes remain **REPORTABLE**, **EXCLUDED**, or **REVIEWER FLAG**. A flag holds the affected conclusion; continue separable supported work and show whether the missing property could change the threshold or method. No asset is silently dropped because it closed before year-end. [P01][P12][P14]

| Existing pattern or extension | Treatment, subject to actual facts | Destination/source |
|---|---|---|
| Foreign bank account, deposits, foreign-held money/prepaid instruments | Normally reportable Category1; distinguish money from marketable debt securities | Form Category1 https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1135/t1135-23e.pdf |
| Non-resident company shares, directly or through a foreign broker | Category2 even if certificates/custody are in Canada, unless foreign-affiliate exclusion applies | ITA233.3(c),(k) https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.3.html |
| Foreign bonds, notes, loans, bills, mortgages and term-deposit/GIC debt | Category3 for non-resident debtor, unless applicable affiliate exclusion; physical custody does not remove it | Form Category3 https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1135/t1135-23e.pdf |
| Non-resident trust or foreign mutual-fund trust interest | Category4 if included under233.3 and acquired-for-consideration rules; apply related-person consideration and specific trust/affiliate exceptions | ITA233.3(d),(l)-(n) https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.3.html |
| Foreign rental/investment real estate | Category5 unless applicable personal-use/active-business exclusion; test whole property/use, not only net equity | CRA real-property Q&A https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html |
| Other foreign investment property | Category6 where not another category: Canadian shares held abroad, relevant insurance, foreign bullion, partnership interests, qualifying rights/options/derivatives | Form Category6 https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1135/t1135-23e.pdf |
| Property with eligible Canadian registered dealer/trust company | Still test specified-property status/cost; choose valid Category7 aggregation or normal category detail. A broker's Canadian branding alone is insufficient | CRA dealer Q&A https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html |
| Foreign investments actually inside RRSP/RRIF/TFSA/RESP/DPSP or another actually qualifying plan trust | Keep documented registered-plan exclusion, not exclusion from tax merely because of an account nickname. Actual owner/plan must qualify | CRA registered-plan Q&A; statutory entity classes https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html and https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.3.html |
| Vacation/personal-use property | Exclude only with actual primary personal/enjoyment use; listed personal property can also qualify | ITA54 and233.3(p) https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html and https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.3.html |
| Exclusively active-business property | Excluded; an investor/day-trader label alone does not prove an active business or exclusive use | ITA233.3(j),CRA Q&A https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.3.html and https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html |
| Canadian mutual-fund trust/corporation units | Investor normally holds Canadian property, not underlying foreign portfolio; confirm actual residence and custody. Canadian shares held by a foreign agent are a separate rule | CRA specified-property Q&A https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html |
| Mixed-use foreign real estate | REVIEWER FLAG until supported use/profit facts classify it. Do not automatically exclude or report only the rental percentage | CRA real-property Q&A https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html |
| Joint ownership/unclear contributions | REVIEWER FLAG for actual beneficial shares; no automatic50/50. Preserve total cost and each owner's evidence | ITA233.3 own-cost test and CRA joint-venture Q&A https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.3.html and https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html |
| Bare trust/nominee mismatch | REVIEWER FLAG for ownership/attribution/residence; do not infer beneficial owner from bank title | ITA233.3 entity/property definitions https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.3.html |
| Partnership interest/underlying foreign property | REVIEWER FLAG until entity test/ownership chain resolved, then Method1 and Category6/exclusion as appropriate | ITA233.3(1),(2) https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.3.html |
| Possible foreign affiliate | REVIEWER FLAG: separate excluded property and possible T1134 job; do not stop reporting unrelated included assets or assume all foreign-company shares are affiliates | ITA233.3(k),(l),233.4 https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.3.html and https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.4.html |
| Crypto, offshore exchange/wallet/token | REVIEWER FLAG for actual situs, legal claim and characterization; a generic foreign website or wallet label is not a concluded statutory location | ITA233.3(a)-(i) https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.3.html |
| Pre-construction foreign deposit | REVIEWER FLAG: read contract/title/acquisition date and any separate debt/right. CRA says no reporting of the future real property before title passed in its stated example; do not generalize to every contractual right | CRA purchase-contract Q&A https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html |

For real estate, CRA's 'primarily' personal use is more than50%, determined from facts. In its equal-size/value four-unit example, three profit-making rental units cause the **entire property cost** to be reported, not only75%. A six-week personal-use condo rented for the remainder is not automatically personal-use property. Document genuine cost-recovery/no-profit use separately. Financing does not reduce cost to down payment or net equity. For a foreign insurance policy, CRA accepts the policy's148(9) adjusted cost basis as a reasonable approximation; do not substitute cash surrender value without support. [P10][P12]

Additional statutory exclusions remain material: relevant exempt foreign trusts, interests not acquired for consideration by taxpayer or related person, the stated Australian/New Zealand pension-trust branch, eligible Canadian-branch foreign-bank debt/rights, and rights to excluded property under233.3(q). Test the actual paragraph and records; do not replace these with 'all foreign trusts reportable'. Full T1134/T1141/T1142 computations or trust-residence determinations are separate jobs. Registered-plan/trust exclusions must match the actual108(1)(a)-(e.1) list read with233.3; a plan nickname is not evidence. A property need not produce income to be reportable, and foreign-currency denomination alone does not make Canadian-held Canadian property foreign. [P01][P12][P14][P24]

### 3. Establish cost, currency and the actual timeline

'Cost amount' is defined in248(1), **not233.3(1)**. It is generally ACB for non-depreciable capital property; depreciable property uses the statutory class-UCC allocation, inventory its tax value, and loans/other rights their applicable statutory basis. It is not universally original purchase price, market value or mortgage equity. Keep source calculations for each property class. [P03]

For a new resident, the ordinary immigration FMV basis reflects128.1(1)'s deemed disposition/reacquisition, subject to its exceptions; CRA's T1135 guidance uses immigration FMV for future reporting. Gifts/inheritances generally use event-date FMV under the cited guidance. Thus a supported event-date FMV **can establish tax cost**; 'never use any FMV' is not the rule. Today's market value or missing historic records cannot be substituted without reconstructing the actual basis. [P04][P12][P14]

Retain the original foreign amounts, dates, rate source/type and converted amounts. The form instructs transaction-date conversion for purchases/income, with annual average acceptable for income throughout the year; maximum funds and maximum FMV use annual average, while year-end funds/FMV use year-end exchange rate. Keep tax cost conversions separate from these reporting-field conventions. Do not retranslate a historic share ACB using today's rate. [P14]

Ordinary reporting is CAD. If a valid section261 election applies, confirm the eligible corporation, actual election/effective year and currency (the current form lists AUD/USD/GBP/EUR/JPY), and state all form monetary amounts consistently. Keep separate CAD threshold evidence under233.3 and the actual form header. Section261(5)(b) translates applicable statutory amounts for its tax-results regime at the first-day relevant spot rate, subject to its exceptions; that alone is not proof of a literal100000 or250000 foreign-unit T1135 trigger. Keep T2-8 open until the actual election, CAD threshold proof, reporting-currency amounts and accepted software rules are reconciled. Do not silently assume CAD after receiving evidence of an election; unaffected CAD cases can proceed. [P09][P14]

Build totals **at the same times** throughout the relevant resident period. Purchases, sales, transfers, withdrawals and reinvestment can cause short-lived crossings. Compute the maximum of those concurrent totals. The form permits maximum month-end cost for its maximum-cost field; that does not excuse missing an actual intra-month statutory100,000 threshold crossing. Likewise do not add a bond's January peak to cash's December peak as though both existed together. Once the filing test is met, inventory all included property held during the reporting period, even sold before year-end. [P01][P12][P14]

### 4. Choose Part A or Part B and populate the actual fields

Record the greatest concurrent total and actual crossing dates. If no filing obligation, retain the completed exclusion/threshold analysis and separately complete income-tax obligations. If required and under250,000 throughout, document the choice A or B. If250,000 or more at any time, B is mandatory. Part A and B are alternatives, not simultaneous summaries. A current amendment may use A only if that historical period qualified; never apply today's holdings to a missed prior year. [P12][P14]

**Header:** reporting year from/to; amendment checkbox; elected functional-currency code if applicable; filer type; individual's first/last/initial/SIN or corporation's name/RC program account, trust's name/T account, partnership's name/RZ account; full address and country. Individual code1 if the individual or spouse/common-law partner is self-employed, otherwise2 if both are not. Partnership code1 for individual/trust end partners,2 for corporate end partners,3 for mixed; trace ultimate recipients through tiered partnerships. The form has separate type-specific identification blocks: do not copy an income-tax account number into a partnership field. [P14]

**Part A:** tick every applicable property-type box. Aggregate month-end cost by the country rules below, rank highest month-end country totals, and select up to the top three countries. Include gross income and gain/loss from all specified foreign property, not only those three countries. Retain a full underlying asset and income inventory even though A does not show every asset. [P12][P14]

**Part B:** complete the following exact fields and relevant category totals. These are unnumbered category columns on the form, not T1 line numbers. Use known nil0 as instructed, rounded to the nearest dollar, but never turn missing records into nil. For more space, use an attachment in the **identical table format**; a general spreadsheet alone is not the prescribed return. [P12][P14]

| Category | Description and required columns after the description | Country rule | Official source |
|---|---|---|---|
| 1 Funds outside Canada | Bank/other entity; maximum funds during year; year-end funds; **gross income**. No generic gain or capital-received column here | Where funds are located | Form pp2,4-5 https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1135/t1135-23e.pdf |
| 2 Non-resident company shares, excluding affiliates | Company name; maximum cost; year-end cost; gross income; gain/loss on disposition | Corporation's residence, not broker's location | Same actual form https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1135/t1135-23e.pdf |
| 3 Non-resident indebtedness | Debt description; maximum cost; year-end cost; gross income; gain/loss on disposition | Non-resident issuer's residence | Same actual form https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1135/t1135-23e.pdf |
| 4 Non-resident trust interests | Trust name; maximum cost; **year-end cost**; income received; capital received; gain/loss on disposition | Trust's residence; do not look through a foreign mutual-fund trust to every underlying issuer | Same actual form and Q&A https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1135/t1135-23e.pdf and https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html |
| 5 Foreign real property | Property description; maximum cost; year-end cost; gross income; gain/loss on disposition | Property's location | Same actual form https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1135/t1135-23e.pdf |
| 6 Other foreign property | Property description; maximum cost; year-end cost; gross income; gain/loss on disposition | Property's location; Canadian shares held by foreign agent use agent location per Q&A | Same form and Q&A https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1135/t1135-23e.pdf and https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html |
| 7 Eligible dealer/trust-company aggregation | Dealer/trust-company name; maximum aggregate FMV; year-end aggregate FMV; gross income; gain/loss, all on a country basis with consistent dealer/account grouping | Underlying property-type rules1-6; not automatically dealer residence or always issuer | Same form pp2,4-5 https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1135/t1135-23e.pdf |

For Category7, obtain confirmation that the custodian meets the Canadian registered securities-dealer/trust-company definitions. Aggregate by country **within the particular dealer/trust company**, or by country within each particular account as permitted; do not collapse unrelated dealers into an unidentified country row. Maximum country FMV may use the greatest total at a month-end. Sum values of that country's included securities at each month-end, then take the maximum; do not sum separate securities' maxima. Record year-end aggregate and actual total income/disposition results. Exclusions and cost-threshold testing still apply before these FMV fields. The concession is optional: valid ordinary Categories1-6 remain available. Remove the old unsourced story that T5008/T3/T5 infrastructure justifies a statutory test. [P12][P14][P15]

Use the form's country-specific rules. If genuinely uncertain, the form instructs **OTH**, with unresolved country facts in the working paper, rather than inventing a likely country. A known country needs its actual prescribed code; do not use OTH to hide absent research. [P14]

Report gross income rather than net rental profit; gain/loss on a property's disposition is not its taxable/allowable fraction. Do not offset unrelated Canadian-property losses against foreign gains. For a reportable partnership interest, the taxable portion of underlying partnership gains is reported as income under CRA guidance, while gain/loss on sale of the interest itself is the disposition field. T1135 is not the tax-return capital-gain computation. [P12]

### 5. Assemble, certify, file and retain confirmation

Use this workflow for a complete supported case, keeping actual filing authority separate from technical preparation:

1. Reconcile header/period/entity, inventory, exclusions, simultaneous threshold, A/B choice, currency and all category totals. Keep source records and evidence for unresolved items. Reconcile foreign income to the related T1/T2/T3/partnership work without assuming the form itself pays that tax.
2. Populate the actual accepted form or CRA-certified T1135 software. Check actual known0 versus blank, nearest-dollar presentation, attachments and full amendment data. Keep unrounded working calculations and currency/basis provenance.
3. Certification on the actual form includes printed signer name, signature, position/title, **telephone** and dateYYYYMMDD. Signer is the individual; authorized corporate officer; trustee/executor/administrator; or authorized partner, as applicable. Record role and real authorization; do not invent a signature or automatically impose a separate CPA signoff.
4. The adjacent preparer block applies if **someone other than the taxpayer or partnership prepared** it, whether paid or unpaid: name, address, postal/ZIP and telephone. The actual paper form has **no EFILE-number field**. Keep any software/service-provider EFILE identifier in separate operational records if applicable, not in a made-up form box. Do not claim the actual instructions say every individual must omit position/title; use the signer context without inventing a mandatory title.
5. Select the actual channel and period: individuals EFILE/NETFILE2017 onward; corporations EFILE2014 onward; partnerships EFILE/NETFILE2017 onward; trusts EFILE2021 onward, subject to actual supported software/eligibility. NETFILE/EFILE is tax-software transmission, not merely uploading a PDF to MyAccount. Check historical channel rules for earlier years.
6. For a permitted authorized electronic submission, keep the **separate T1135 confirmation number**, date, filer/year, accepted status and exact filed copy. A successful income-tax return receipt does not prove this information return was transmitted. Failed/rejected submission remains unfiled until actually accepted. A standard NOA reminder is not evidence that T1135 was missing or received.
7. Paper may accompany the paper income/partnership return to the applicable tax centre, or be mailed separately to the actual form's Winnipeg address: Winnipeg Taxation Centre, Data Assessment & Evaluation Programs, Validation & Verification Section, Foreign Reporting Returns,66StaponRoad,WinnipegMBR3C3M2. Keep the signed complete filed copy, correctly formatted extra sheets and mailing/delivery evidence; confirm address when actually filing. Do not send it to the VDP correspondence address instead.
8. For amendments tick the amended-return box and provide **all required data**, not only changes. CRA encourages current form revision and accepts original revision for an amendment; check applicable certified historical software/channel. Historical PartA eligibility is tested on that historical period. Keep original and amended receipts and reconciliation.
9. State actual status: NOT REQUIRED, INCOMPLETE, PREPARED FOR REVIEW, READY FOR AUTHORIZED FILING, SUBMITTED/ACCEPTED with evidence, or REJECTED. Under the shared preparation workflow, READY FOR AUTHORIZED FILING requires resolved material gaps, the case's actual required professional review recorded with reviewer, version, scope and date, and real filing authorization. This is a workflow safeguard, not a claim that T1135 universally requires a separate CPA signoff. Technical checks alone cannot establish that review. A prepared working paper is not a reviewed, approved or filed return. T1135 itself has no tax-payment amount; route any assessed penalties/tax and their actual notice/payment details separately. Do not execute filing, payment or disclosure merely because the preparation is complete.

These steps come from the actual form's certification/channel/paper instructions and CRA's filing/amendment/receipt Q&A. [P12][P14][P16]

### 6. Set the correct filing date

The legal rule is233.3(3), read with the248(1) filing-due-date definition,150(1) andReg229(5),(6). T1135 is due even if the linked income/partnership return is not itself required. A balance-payment deadline is not automatically its filing date. [P01][P03][P11][P21]

| Filer | Date rule and switch | Official source |
|---|---|---|
| Ordinary individual | Following April30; qualifying self-employed individual or qualifying spouse/common-law partner generally following June15. Preserve150(1)(d)(ii) tax-shelter expenditure exception | ITA150(1)(d) https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html |
| Deceased individual/affected spouse | Apply150(1)(b),(d)(iii), including actual death date/later-of-six-month conditions; do not automatically use April30 | Same statute https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html |
| Corporation | Within6months after actual year-end; not its income-tax payment due date | ITA150(1)(a) https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html |
| Trust/estate | Within90days after actual taxation-year end; determine that actual year-end, not a universal calendar assumption | ITA150(1)(c) https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html |
| Partnership all members corporate throughout period | Within5months after fiscal period end | Reg229(5)(a) https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-229.html |
| Partnership all members individuals throughout period | Last day ofMarch after calendar year in which period ended, including a period ending on that calendar-year end | Reg229(5)(b) https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-229.html |
| Other partnership | Earlier of5months after period end or following last day ofMarch | Reg229(5)(c) https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-229.html |
| Partnership discontinued activity | Earlier of90days after discontinuance or normal229(5) date for relevant unfiled period; retain actual cessation date | Reg229(6) https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-229.html |
| Dated2025 bridge | For ordinary living-individual2025 filing, CRA publishes30April2026 and qualifying self-employed15June2026;2025 income tax generally due30April2026 separately | CRA dates https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html |

Calculate the actual year/date and check any applicable weekend/public-holiday or special extension against the authority before finalizing that client's calendar. Do not treat this table as a certificate of every special extension or choose a later date from an unverified assumption.

### 7. Calculate and distinguish potential penalties

Keep a return-by-return schedule: year, actual due date, eventual filing date, elapsed days, relevant calendar months, knowing/gross-negligence facts, actual demand and service/noncompliance dates, concurrent cost history, prior liabilities/assessments and omitted-property/income facts. Do not mechanically apply every penalty to every missed form. The ordinary late information-return penalty can apply even without tax owing; no finding of gross negligence follows from arithmetic alone. [P06][P17][P18]

For162(7), if a penalized failure exists: max(100,25×min(days,100)). If on time, this failure's amount is0, not100. For162(10), establish paragraph(a)'s knowing/gross-negligent failure to file as required, or paragraph(b)'s knowing/gross-negligent failure to comply with a demand where(a) does not apply. **A** counts months during any part of which unfiled, capped24: from required-filing month for(a), or demand-served month for(b). **B=2** when a section233 demand was not complied with, even if(a) is the liability branch; otherwise1. **C** is162(7) liability, not merely an amount already paid or assessed. Calculate500×A×B−C, applying257 for a negative result. Do not add a second independent162(10)(b) fine to an(a) calculation. [P06][P22]

For162(10.1), establish162(10) liability and the applicable(a)/(b) clock exceeding24 months. For T1135, **A=5% of the greatest concurrent total cost amount** of specified foreign property in that **reporting year/period**, and **B=162(7)+162(10) liabilities** for that return. Additional amount is A−B, subject to257, not A plus those amounts again. It is imposed once for that return, not annually on the same delinquency; separate missed reporting years are separate returns/tests. [P06][P18][P22]

For163(2.4)(c), establish knowing/gross-negligent false-statement/omission involvement, then use the greater of24000 and5% of the greatest concurrent total cost of the specified property **to which that false statement/omission relates**. It is not automatically the cost of every disclosed asset, and does not automatically arise because no form was filed. Under163(3), in an appeal CRA bears the burden of establishing facts justifying its assessed penalty. Do not collapse possible non-filing and false-statement paths into a guaranteed total without the separate factual/legal findings. [P07]

The specific233.5 diligent-effort exception in CRA's foreign-reporting table does **not** cover T1135. Do not promise that statutory exception or say an automatic assessment defeats every possible legal defence. CRA's Q&A identifies discretionary taxpayer-relief requests, including RC4288, considered on individual merits; it is distinct from the current VDP. An existing assessed penalty is not automatically a new VDP-eligible item. [P12][P17][P19]

For152(4)(b.2), record both the specified T1135 failure (including the statutory partnership case) and the taxpayer's omitted income-return amount from specified foreign property. Only then record the additional3-year window under that paragraph, measured from the end of the taxpayer's actual normal reassessment period. It is not automatic indefinite reopening of every issue because a T1135 box was wrong. Other statutory reassessment provisions are separate. [P08]

### 8. Prepare a current disclosure handoff, if needed

Preserve the missed-year inventory and complete returns. Do not claim that 'CRA has not contacted me' alone guarantees eligibility or any stream. For applications **received on/after1October2025**, use IC00-1R7; the old R6 General/Limited process and the form's stale R6 cross-reference are not current instructions. Earlier applications retain their applicable historical process. [P19][P20]

Current eligibility needs a voluntary application concerning information at least one year past the filing due date; an error/omission with applicable interest, penalties or both; complete supporting information/all required years and comprehensive responses; and payment **or request for a payment arrangement** for estimated tax if applicable. Audit/investigation already initiated against taxpayer or related taxpayer concerning the disclosed information defeats voluntary status under the stated rule. An identified compliance communication/third-party information can make an application prompted without being the same as an audit disqualification. Preserve actual wording, dates and related-party facts. [P19]

Unprompted/general normally provides75% interest and100% applicable-penalty relief; prompted/partial normally25% interest and up to100% penalties. Eligible accepted information is protected from prosecution and gross-negligence penalties as stated by R7; do not promise acceptance,100% prompted penalty relief, tax forgiveness or no later audit. Current exclusions include already assessed penalties/interest requests, altering elections, insolvency and the other actual paragraph11 circumstances. Discuss these with the authorized adviser rather than disguising an ineligible case. [P19]

The handoff identifies RC199 application, all known errors, factual chronology, prior contacts/audits, estimated tax, actual payment/arrangement request and relevant documents. R7 generally requires records for the most recent6years, but **10years for errors/omissions concerning assets/income outside Canada**; a year with no error need not be included and CRA can request older records. Include advisers/promoters where required. R7 allows anonymous preliminary discussion, which is nonbinding. Actual authorized submission can use Submit documents online in MyAccount/MyBusinessAccount/Represent a Client, or current listed mail/fax; this method prepares the handoff and does not submit it. Keep CRA acknowledgment/effective date of disclosure and eventual written decision separate from filing receipts and any relief assumption. [P19]

### 9. Produce the complete working paper and controls

Retain these legacy templates with missing values explicitly MISSING, not false/zero. They are workpaper fields, not invented numbered form boxes:

```text
CANADA T1135 WORKING PAPER: actual reporting year and period ______
A HEADER
A1 original/amended and original receipt ______
A2 valid functional-currency election? confirmed / absent / MISSING
A3 currency/effective-year/evidence and conversion reconciliation ______
A4 filer type, identity/account, individual/partnership code ______
A5 full address/country; actual owner/beneficial shares/evidence ______
A6 actual period from ______ A7 actual period to ______
A8 residence/death/cessation/first-ever resident-year evidence ______
B THRESHOLD
B1 concurrent cost timeline/source and greatest included total ______
B2 exceeded100000 at any relevant time? supported yes/no/MISSING
B3 reached250000 at any relevant time? supported yes/no/MISSING
B4 result NONE / PART A / PART B / INCOMPLETE, legal reason ______
C INVENTORY, one asset row or documented valid Category7 group
ID; dates; owner/share; description; inclusion/exclusion/flag; category;
country/evidence; original currency/rates; tax-cost basis;
concurrent cost timeline; category-specific maximum and year-end amount;
gross income OR trust income/capital received; disposition gain/loss;
source document IDs; missing facts; downstream income-return reference
D EXCLUSIONS: asset; exact statutory/plan/use reason; evidence ______
E FLAGS: issue; affected conclusion; missing fact; safe partial work; owner ______
F CERTIFICATION: actual statement checked against current form;
printed signer name; role/position/title; actual signature; telephone;
actual dateYYYYMMDD; authority; status MISSING/PREPARED/SIGNED ______
G OTHER PREPARER if someone other than taxpayer/partnership prepared:
name; address; postal/ZIP; telephone; applicability/evidence ______
Separate operational record: EFILE provider/identifier if applicable ______
H RETURN: method/currency; header; PartA types/countries/income/gains OR
PartB exact category columns/totals; identical-format attachments ______
I DELIVERY: channel/year eligibility; due date/source; exact filed copy;
actual separate T1135 confirmation/status/date or paper evidence ______
J PRIOR YEARS: separate periods/penalty assumptions/contacts;
VDP or taxpayer-relief handoff and actual decision evidence ______
```

Final checks: all assets and supported exclusions present; no invented country/cost/residence/owner; actual concurrent threshold and A/B boundaries; every required field completed/known nil distinguished from missing; correct max-cost/funds/FMV and FX bases; no independent-peak double counting; correct category-country grouping and trust year-end cost; complete income/gain reconciliation; actual period due date/channel/certifier/preparer; whole amendment and separate receipt; prior-year/disclosure flags; source version/approval recorded. Hold the whole final conclusion if a missing asset could change it; unrelated completed work need not be repeated.

## Worked cases

The original eight test families remain below with clarified facts. These arithmetic components do not establish residence, beneficial ownership, gross negligence, a valid election or actual receipt of a filing. Cases use CAD, no functional-currency election and complete stated property inventories unless indicated. Each decision depends on the conditions in Methods1-8 and its cited source.

### Case 1. Original below-threshold case

A resident individual outside the first-year exception owns a foreign bank account with cost42000 and foreign-company shares with cost31000. Those are the only included properties, held concurrently, and the total never exceeded their stated73000. No T1135 is required. Foreign income still goes into the income-tax return. [P01][P12]

```oa-check
name: T1135 original below-threshold total
inputs:
  bank: 42000
  shares: 31000
steps:
  - total: bank + shares
  - below_by: 100000 - total
expected:
  total: 73000
  below_by: 27000
```

### Case 2. Original sold-before-year-end case and method decision

The same eligible type of filer concurrently held foreign cash18000 and shares108000, then sold the shares. Complete records show the total126000 never reached250000. Year-end included property is only18000, but the earlier crossing requires T1135 and the sold shares remain in that period's inventory. **Either A or B is allowed**: A uses all property-type boxes/top-country/income/gain totals; B requires actual category columns, or valid Category7 if elected for an eligible custodian. A lower year-end balance is not a no-filing election. [P01][P12][P14]

```oa-check
name: T1135 sold assets and method boundary
inputs:
  cash: 18000
  shares: 108000
steps:
  - concurrent_peak: cash + shares
  - above_trigger: concurrent_peak - 100000
  - year_end: cash
  - below_detailed_boundary: 250000 - concurrent_peak
expected:
  concurrent_peak: 126000
  above_trigger: 26000
  year_end: 18000
  below_detailed_boundary: 124000
```

### Case 3. Original corporation and exact boundaries

An ordinary resident corporation, not an excluded entity, had included securities cost310000 at a relevant time: T1135 and PartB are required. Separately, a complete eligible case that peaks **exactly100000** has no threshold crossing;100000.01 crosses it. Exactly250000 requires B;249999.99 may use A or B if no greater total occurred. Do not round cost to whole dollars before testing the legal boundaries. Form presentation rounding follows the underlying decision. [P01][P12][P14]

```oa-check
name: T1135 exact boundaries before presentation rounding
inputs:
  corporation_peak: 310000
  exact_trigger: 100000
  just_above: 100000.01
  just_below_b: 249999.99
steps:
  - corp_above_b: corporation_peak - 250000
  - exact_trigger_excess: exact_trigger - 100000
  - just_above_excess: just_above - 100000
  - gap_to_b: 250000 - just_below_b
expected:
  corp_above_b: 60000
  exact_trigger_excess: 0
  just_above_excess: 0.01
  gap_to_b: 0.01
```

### Case 4. Original registered-plan exclusion

Actual documents establish that foreign ETF150000 is inside the taxpayer's qualifying RRSP and foreign stock35000 inside a qualifying TFSA, with no other potentially included property. These holdings do not create a personal T1135 filing requirement. A generic label 'retirement' without confirmed plan/ownership would remain a flag. [P01][P12]

```oa-check
name: T1135 documented registered plans
inputs:
  rrsp: 150000
  tfsa: 35000
steps:
  - excluded_value: rrsp + tfsa
  - included_cost: excluded_value - rrsp - tfsa
expected:
  excluded_value: 185000
  included_cost: 0
```

### Case 5. Original mixed-use condo and financing distinction

A foreign condo used personally for6weeks and rented for the remainder of a365-day year is flagged until use, profit purpose and actual costs are established. The recorded42personal/323other days are evidence, not an automatic proportionate T1135 deduction. CRA's separate equal-size/value four-unit example with three profit-making rental units reports the **whole** property cost, not75%. A500000 included property bought with50000 down and450000 mortgage has cost500000, not50000. [P10][P12]

```oa-check
name: T1135 mixed use is not net-equity reporting
inputs:
  weeks_personal: 6
  days_year: 365
  property_cost: 500000
  down_payment: 50000
steps:
  - personal_days: weeks_personal * 7
  - other_days: days_year - personal_days
  - mortgage: property_cost - down_payment
  - financed_cost: down_payment + mortgage
  - wrong_rental_fraction_cost: property_cost * 0.75
expected:
  personal_days: 42
  other_days: 323
  mortgage: 450000
  financed_cost: 500000
  wrong_rental_fraction_cost: 375000
```

### Case 6. Original Category7, independently timed maxima

A confirmed eligible Canadian registered dealer holds included securities of the same underlying country in one account. The filer qualifies for A or B from a separately established greatest concurrent **cost120000**, and **chooses B with Category7**. CAD month-end FMVs: JanuaryA100000/B30000, FebruaryA70000/B80000; all other month-end totals at or below150000; year-endA60000/B50000. Report maximum country aggregate150000 and year-end110000. Summing each security's independent peak gives180000 and is wrong. Keep dealer/account/country scope, actual income and gains, and no duplication in Categories1-6. A second dealer requires its own supported grouping. [P12][P14][P15]

```oa-check
name: T1135 Category7 simultaneous country aggregates
inputs:
  jan_a: 100000
  jan_b: 30000
  feb_a: 70000
  feb_b: 80000
  year_end_a: 60000
  year_end_b: 50000
steps:
  - jan_total: jan_a + jan_b
  - feb_total: feb_a + feb_b
  - maximum_aggregate: max(jan_total, feb_total)
  - wrong_separate_peaks: max(jan_a, feb_a) + max(jan_b, feb_b)
  - year_end: year_end_a + year_end_b
  - overstatement: wrong_separate_peaks - maximum_aggregate
expected:
  jan_total: 130000
  feb_total: 150000
  maximum_aggregate: 150000
  wrong_separate_peaks: 180000
  year_end: 110000
  overstatement: 30000
```

### Case 7. Original first-ever Canadian resident

An individual other than a trust first became Canadian tax resident on14March2026. Foreign account cost180000 and rental property cost420000 were held throughout. Subject to confirming that this is truly the first resident year,233.7 removes this individual's2026 T1135 obligation;600000 does not override that exception. The following year is retested using the applicable property/cost/residence rules and actual immigration basis, not automatically declared reportable. A corporation/trust or someone returning after an earlier resident period does not get this individual first-ever-year answer. [P01][P02][P04][P12]

```oa-check
name: T1135 first-year exception does not depend on low value
inputs:
  bank: 180000
  rental: 420000
steps:
  - asset_cost_total: bank + rental
  - amount_above_ordinary_trigger: asset_cost_total - 100000
expected:
  asset_cost_total: 600000
  amount_above_ordinary_trigger: 500000
```

### Case 8. Original four missed years

A resident individual reports foreign brokerage cost310000 in each of four prior years, no filed T1135 and no reported CRA contact. Prepare each year's actual concurrent inventory/due date/filing history and test B separately. Ordinary maximum late-filing components could total4×2500=10000 **if each return has at least100penalized late days and162(7) applies**. This is not a guaranteed combined liability: knowing/gross negligence, demand, applicable month clock, greater-cost and false-statement facts need separate findings. Neither 'never filed' nor 'no contact' proves all higher penalties or disclosure eligibility. Assess unreported foreign income separately for152(4)(b.2). A new disclosure uses R7 even for old underlying years; no guaranteed relief or routine submission. [P06][P07][P08][P18][P19]

```oa-check
name: T1135 four separate ordinary late components only
inputs:
  affected_returns: 4
  penalized_days_each: 100
steps:
  - per_return: max(100, 25 * min(penalized_days_each, 100))
  - conditional_ordinary_total: affected_returns * per_return
expected:
  per_return: 2500
  conditional_ordinary_total: 10000
```

### Case 9. Transfers do not create simultaneous ownership twice

A resident's only specified property is60000 held in foreign bankA, then fully transferred to bankB with records showing no overlap and no larger balance, leaving at most60000 at any time. The separate maxima60000+60000=120000 do not establish a statutory crossing. Conversely, an actual simultaneous balance/asset purchase crossing within a month still matters even if every month-end is below100000. Preserve all transfer timestamps and bank FX/currency evidence. [P01][P12][P14]

```oa-check
name: T1135 transfer timeline versus independent account peaks
inputs:
  before_a: 60000
  before_b: 0
  after_a: 0
  after_b: 60000
steps:
  - before_total: before_a + before_b
  - after_total: after_a + after_b
  - actual_concurrent_peak: max(before_total, after_total)
  - wrong_separate_peaks: max(before_a, after_a) + max(before_b, after_b)
expected:
  before_total: 60000
  after_total: 60000
  actual_concurrent_peak: 60000
  wrong_separate_peaks: 120000
```

### Case 10. Penalty offsets, demand and nil floor

These are stipulated liability components for **one return**, not a factual finding of knowing/gross negligence. A30-day162(7) failure gives750. For a different return with162(7) liability2500,162(10) qualifying month count capped24, no failed demand(B1), and applicable raw clock over24months,162(10) is12000−2500=9500. Greatest concurrent cost500000 gives additional162(10.1)25000−(2500+9500)=13000, total25000. With a failed section233 demand(B2) under the same liability assumptions,162(10) becomes21500 and the additional amount1000, again total25000. Do not add25000 to the earlier12000/24000 without offsets. [P06][P22]

At smaller cost200000, the additional no-demand formula10000−12000 is negative and257 makes it0; the existing12000 liability is not refunded. Separately, a qualifying false statement about cost200000 yields24000, while cost800000 yields40000, under163(2.4)(c). Those are distinct conditional penalty paths, not automatically stacked onto the non-filing example. [P07][P22]

```oa-check
name: T1135 conditional penalty formula components
inputs:
  late_days: 30
  ordinary_liability: 2500
  capped_months: 24
  cost: 500000
  small_cost: 200000
steps:
  - ordinary_30_days: max(100, 25 * min(late_days, 100))
  - monthly_no_demand: max(0, 500 * capped_months - ordinary_liability)
  - earlier_no_demand: ordinary_liability + monthly_no_demand
  - additional_no_demand: max(0, cost * 0.05 - earlier_no_demand)
  - total_no_demand: earlier_no_demand + additional_no_demand
  - monthly_failed_demand: max(0, 500 * capped_months * 2 - ordinary_liability)
  - earlier_failed_demand: ordinary_liability + monthly_failed_demand
  - additional_failed_demand: max(0, cost * 0.05 - earlier_failed_demand)
  - total_failed_demand: earlier_failed_demand + additional_failed_demand
  - small_formula_raw: small_cost * 0.05 - earlier_no_demand
  - small_additional: max(0, small_formula_raw)
  - false_statement_small: max(24000, small_cost * 0.05)
  - false_statement_large: max(24000, 800000 * 0.05)
expected:
  ordinary_30_days: 750
  monthly_no_demand: 9500
  earlier_no_demand: 12000
  additional_no_demand: 13000
  total_no_demand: 25000
  monthly_failed_demand: 21500
  earlier_failed_demand: 24000
  additional_failed_demand: 1000
  total_failed_demand: 25000
  small_formula_raw: -2000
  small_additional: 0
  false_statement_small: 24000
  false_statement_large: 40000
```

### Decision regressions without invented client facts

| Situation | Correct action | Basis |
|---|---|---|
| Only current FMV supplied | Reconstruct actual cost; event-date gift/inheritance/immigration FMV may establish basis, today's value alone does not | P03/P04/P12/P14 |
| One missing account could cross100000 or250000 | Complete safe inventory work; hold final obligation/method conclusion | P01/P12 |
| Foreign-company shares with a Canadian broker | Not automatically excluded; prove eligibility for Category7 or report normal category | P01/P12/P14 |
| Foreign fund domiciled in one country invests elsewhere | Report the actual fund interest/country; do not substitute every portfolio country | P12/P14 |
| Country genuinely uncertain | Form permits OTH; preserve unresolved facts rather than guessed country | P14 |
| Known nil income versus absent statement | Known0 may be entered; unknown remains missing and cannot silently become0 | P14 |
| Demand after a knowing failure to file | B can be2 under10(a); do not force demand month as the10(a) Aclock or apply two monthly penalties | P06 |
| No omitted income but late T1135 | Penalties may apply;152(4)(b.2) additional3years needs both statutory predicates | P06/P08 |
| Identified compliance letter but no audit/investigation | Test current prompted disclosure rules; do not automatically deny all VDP or promise relief | P19 |
| Actual income-tax acceptance receipt only | T1135 remains unproven until separate confirmation/file evidence | P12/P14 |
| Historical amendment eligible for PartA | It may use A; provide complete amended data, not only changes; retain accepted channel/year and receipt | P12/P14 |

## When to refuse or refer

Keep the six existing refusal IDs as precise holds, not blanket claims that law requires a CPA for every routine action:

| ID | Trigger | Work to hold and useful handoff |
|---|---|---|
| R-CA-T1135-1 | Non-resident throughout period | Explain no ordinary Canadian T1135 residence trigger; hold any uncertain residence/deemed-residence conclusion, route other Canadian tax obligations separately |
| R-CA-T1135-2 | Immigration/emigration or first-ever resident-year unclear | Collect dates/ties/prior residence and documents; do not guess full-year obligation, first-year exception or immigration cost |
| R-CA-T1135-3 | Legal/beneficial ownership or attribution unclear | Retain inventory, contracts, shares and competing owners; hold attribution/threshold conclusion that depends on it |
| R-CA-T1135-4 | Actual cost unsupported | Reconstruct tax basis with acquisition/rollover/gift/immigration/class records; hold final threshold/field amount, not all unrelated work |
| R-CA-T1135-5 | Crypto/exchange/wallet situs or characterization unresolved | Identify actual legal claim/counterparty/custody, evidence and missing analysis before classification |
| R-CA-T1135-6 | Possible foreign affiliate | Separate excluded affiliate holdings and T1134 analysis from unrelated reportable assets; hold affected classification until established |

All ten original specialist-issue IDs remain:

| ID | Issue and actual control |
|---|---|
| T2-1 | Immigration/emigration: Method1/3 residence/basis and relevant-period evidence |
| T2-2 | Beneficial ownership/nominee: actual shares/attribution; no title-only guess |
| T2-3 | Foreign affiliate: exact statutory relationship and possible T1134 job |
| T2-4 | Partnership/trust attribution: statutory entity/inclusion/exclusions and chain, not automatic double reporting |
| T2-5 | Digital-asset situs/characterization: unresolved legal facts cannot be replaced with exchange branding |
| T2-6 | Mixed-use property: actual primary use/profit purpose and whole-property treatment |
| T2-7 | Pre-construction contract: real acquisition/title and separate rights/debt analysis |
| T2-8 | Functional election/amendment: actual effective period, basis/currency and historical method/channel; no automatic refusal of a straightforward supported amendment |
| T2-9 | Joint ownership: documented contributions/beneficial interests rather than50/50 default |
| T2-10 | Missed years: separate year inventory, precise penalties/reassessment and current VDP or taxpayer-relief handoff |

When handing off, provide taxpayer type, residence/period, actual known threshold computation, complete asset inventory/exclusions, proposed category/country/method, missing facts, applicable source and why the affected conclusion remains open. Do not label these issue IDs as the skill's accountant-approval tiers. Continue supported partial work, but do not claim whole-form readiness while material gaps remain.

Prohibitions retained: never replace required tax cost with unsupported market value; never assume a Canadian broker removes exposure; never infer no filing from low year-end balance; never omit sold property once filing required; never assume personal-use/active-business exclusions; never ignore the first-ever resident-year exception; never omit applicable amendment/currency/certification/preparer fields; never present speculation as definitive. Additionally, never invent an approval, signature, filing receipt, nil, country code or payment.

## Moved / Not moved

Rewritten in place, no slug moved/deleted. The full old-topic destination ledger preserves all11 numbered sections, seven category jobs,19 original property-pattern rows, fifteen required-input purposes, six refusal IDs, ten specialist issues, both workpaper/certifier-preparer template purposes, eight original test families and eight prohibitions. Exact destinations are in the accompanying preservation ledger.

Not retained as usable guidance: unsupported T5008/T3/T5 explanation for Category7; invented EFILE paper field/paid-only preparer limitation; generated verified-facts/Nathan credit wording for this changed version; obsolete current R6/General-Limited instructions; unconditional CPA signoff/liability boilerplate; guessed country, independent-peak aggregation, omitted trust year-end field and incomplete penalty conditions. Their legitimate workflow purposes are retained with the current sources. The historical signed version remains in Git; no renewed professional approval is implied.

## Sources

Each entry records the actual bounded portion read, not a whole-Act audit. Actual form pages1-3 were also rendered and visually inspected against the listed fields; all six pages of instructions/text were read. Copies are research evidence, not taxpayer records.

| Source and portion read | Official URL | Read on |
|---|---|---|
| P01: Read for ITA233.3(1)-(3), entity/property definitions, exclusions, tiered membership and filing date | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.3.html | 2026-11-14 |
| P02: Read for ITA233.7 full operative first-year exception | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.7.html | 2026-11-14 |
| P03: Read for ITA248(1), cost amount paragraphs(a)-(f), filing-due-date definition and relevant class distinction | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html | 2026-11-14 |
| P04: Read for ITA128.1(1)(a)-(c), immigration deemed disposition/acquisition and listed exceptions | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html | 2026-11-14 |
| P05: Read for ITA233.4(1)-(3), foreign-affiliate reporting-entity and relationship/look-through routing only | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.4.html | 2026-11-14 |
| P06: Read for ITA162(7),(10),(10.1), neighbouring penalty distinctions and all A/B/C definitions | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html | 2026-11-14 |
| P07: Read for ITA163(2.4)(c),(3), affected-property false-information basis and appeal burden | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-163.html | 2026-11-14 |
| P08: Read for ITA152(4)(b.2)(i),(ii), both predicates and additional window only | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-152.html | 2026-11-14 |
| P09: Read for ITA261(1)-(5), Canadian tax results, qualifying currency/election and conversion scope; no literal foreign-unit T1135 trigger certified | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-261.html | 2026-11-14 |
| P10: Read for ITA54 personal-use-property definition(a)-(c), partnership sentence and listed-personal-property distinction | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html | 2026-11-14 |
| P11: Read for ITR229(5),(6), all-corporate/individual/mixed periods and discontinuance dates | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-229.html | 2026-11-14 |
| P12: Read for CRA T1135 Q&A, all operative filing/amendment/residence/cost/method/property/income/ownership/use/penalty/dealer questions | https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html | 2026-11-14 |
| P13: Read for CRA actual current catalogue, E(23) normal/large/accessible versions and historical links | https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t1135.html | 2026-11-14 |
| P14: Read for Actual six-page T1135 E(23), header/A/B/certification/preparer, all instructions, countries/cost/FX/aggregation/channels/paper; old R6 reference superseded | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1135/t1135-23e.pdf | 2026-11-14 |
| P15: Read for CRA2015-later reporting, A/B boundaries, country/dealer month-end FMV aggregation, entity/year channels | https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/form-t1135-reporting-2015-later-tax-years.html | 2026-11-14 |
| P16: Read for CRA overview, reporting groups/property exceptions, complete filing-date table and channel/reassessment guidance | https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/foreign-income-verification-statement.html | 2026-11-14 |
| P17: Read for CRA penalty table, rows and operative failure/false-statement/due-diligence sections | https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/table-penalties.html | 2026-11-14 |
| P18: Read for CRA penalty Q&A, exact per-return 5% frequency, non-residence/ordinary/knowing/demand distinctions and cost basis | https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-penalties.html | 2026-11-14 |
| P19: Read for Current IC00-1R7 opening and paras7-43, eligibility/contact/audit/relief/document/payment/submission/decision conditions | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic00-1/ic00-1r7-voluntary-disclosures-program.html | 2026-11-14 |
| P20: Read for ARCHIVED IC00-1R6 opening/paras1-6 only, historical effective period and General/Limited distinction, not usable current process | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic00-1/ic00-1r6-voluntary-disclosures-program.html | 2026-11-14 |
| P21: Read for ITA150(1)(a)-(d), individual/corporate/trust/death dates and qualifying business/spouse exception only | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html | 2026-11-14 |
| P22: Read for ITA257 complete operative negative-formula rule | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-257.html | 2026-11-14 |
| P23: Read for CRA personal due dates, actual2025 filing/payment bridge and qualifying self-employed date | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html | 2026-11-14 |
| P24: Read for ITA108(1) trust-definition(a)-(e.1), actual qualifying plan/trust exclusions read with233.3 | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-108.html | 2026-11-14 |

Not yet confirmed: case-specific tax residence/beneficial ownership, crypto situs, complex trust/affiliate classification, valid functional-election threshold/presentation reconciliation, special filing extensions and actual filing/software/account status require the stated evidence before a real-case conclusion. No live registry, portal, spreadsheet, agent-schema, transmission or payment test was performed. No current professional approval of this replacement is supplied.

[P01]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.3.html
[P02]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.7.html
[P03]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html
[P04]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html
[P05]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.4.html
[P06]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html
[P07]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-163.html
[P08]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-152.html
[P09]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-261.html
[P10]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html
[P11]: https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-229.html
[P12]: https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html
[P13]: https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t1135.html
[P14]: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1135/t1135-23e.pdf
[P15]: https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/form-t1135-reporting-2015-later-tax-years.html
[P16]: https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/foreign-income-verification-statement.html
[P17]: https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/table-penalties.html
[P18]: https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-penalties.html
[P19]: https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic00-1/ic00-1r7-voluntary-disclosures-program.html
[P20]: https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic00-1/ic00-1r6-voluntary-disclosures-program.html
[P21]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html
[P22]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-257.html
[P23]: https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html
[P24]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-108.html
