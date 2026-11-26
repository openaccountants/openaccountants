---
name: nl-payroll-tax
description: "Dutch payroll and WKR for 2026: select withholding tables, establish insurance coverage and employer premiums, classify benefits, calculate free space and final levy, and reconcile registration, returns, payments and corrections. Includes conditional worked cases and explicit referrals for specialist points."
version: 1.5
jurisdiction: NL
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - income-tax-workflow-base
  - payroll-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
authored_by: Michael Cutajar and the OpenAccountants team
tier: 2
domain: payroll
type: computation
---

# Netherlands: payroll (loonheffingen), work-cost scheme (WKR) and final levies 2026

Based on work by [John in 't Hout (@johnhout)](https://github.com/johnhout/knowledge-work-belastingzaken), licensed under MIT. Adapted for the OpenAccountants format.

## Who this applies to

Use this Guide for a Dutch withholding agent's 2026 payroll. Establish the wage-tax and insurance positions separately before calculating. Wage includes cash and noncash employment benefits; retain separate wage-tax, employee-insurance and Zvw bases. Use actual pension arrangements. Employer Zvw is an employer cost, not taxable wage or an employee net-pay deduction. [Wet LB arts. 6, 10–13](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002471/2026-10-08_0/xml/BWBR0002471_2026-10-08_0.xml); [Handbook ch. 1, 4–8](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).

Use the March 2026 handbook with the fourth rates appendix (25 June 2026) and the mileage policy below. A previous-year correction needs that year's rules. Annual reference calculations below do not establish period withholding. [Handbook ch. 9, 14](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf); [appendix](https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf).

## Rates, bands and thresholds

These premium figures apply only after coverage, classification and cumulative bases are established.

| Item | 2026 rate or amount | Source URL |
|---|---|---|
| AWf low / high | 2.74% / 7.74% | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf (table 9) |
| Aof low / high | 6.27% / 7.63% | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf (table 9) |
| Wko surcharge on the combined Aof base | 0.50% | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf (table 9); https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf §7.5 |
| Whk | Employer's actual notice; separate WGA and ZW components | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf (table 9) |
| Employer Zvw / withheld Zvw, according to status | 6.10% / 4.85% | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf (table 12) |
| Normal premium/contribution maximum | EUR 79,409 yearly; EUR 6,617.41 monthly; EUR 6,108.38 four-weekly | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf (table 11) |
| Aof ordinary small-employer boundary | 2024 premium wage sum at most EUR 1,082,500; use the actual classification, including startup/transfer rules | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf (table 9); https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf §7.5 |
| WKR free space | 2.00% through EUR 400,000 of eligible fiscal wage; 1.18% of the excess | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002471/2026-10-08_0/xml/BWBR0002471_2026-10-08_0.xml art. 31a(3) |
| WKR final levy | 80% of nonexempt designated wage above free space | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002471/2026-10-08_0/xml/BWBR0002471_2026-10-08_0.xml art. 31a(2) |
| Ordinary minimum hourly wage, age 21 and over | EUR 14.71 from 1 January; EUR 14.99 from 1 July; younger/BBL workers need their own category | https://www.rijksoverheid.nl/themas/werk/minimumloon/bedragen-minimumloon/bedragen-minimumloon-2026 |

## The taxable base

**Withholding tables.** Use white tables for current-employment wage and green tables for former-employment wage, subject to the handbook's payment-specific rules. Select the actual year, wage period, residence group, AOW status, insurance/tax coverage and credit election. Use the official table or its implemented calculation specification. Apply payroll credits at one employer/payer at a time on the employee's written request. Do not deduct a credit again after using a table that includes it. Net-pay agreements require grossing up. [Handbook §9.3–9.4, §24.1](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).

**Special remuneration.** A one-off or usually annual bonus/holiday payment uses the appropriate white or green special-remuneration table, including its credit-adjustment percentage. Annual salary paid once is ordinary period wage. Establish column-14 annual wage: previous full year's pay; annualise a partial previous year; for a new starter annualise expected current-year pay including foreseeable incidental amounts. Monthly holiday allowance joins monthly wage. [Handbook §9.3.6](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).

**Anonymous rate.** Missing required name/address/residence/BSN, failed required identity or permission checks, or known incorrect information can trigger 52% withholding without credits. The ordinary premium/Zvw ceilings then do not apply. A missing BSN outside both parties' control is not automatic exemption: send a written request to the Belastingdienst with evidence and obtain its agreement. Use a personnel number while no BSN is available. For later receipt of complete/correct data, current-year anonymous wage-tax withholding may be corrected; assess insurance/Zvw adjustments separately. [Wet LB art. 26b](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002471/2026-10-08_0/xml/BWBR0002471_2026-10-08_0.xml); [Handbook §2.6, §6.5, §29.2](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).

**AWf.** Low AWf normally requires a written indefinite contract that is not an on-call contract. Separately test the under-21 exception at the start of the return period: at most 48 paid hours per four weeks or 52 per month. Qualifying BBL needs a recognised training employer and a written, signed and dated practice agreement with the educational institution and learner kept in the records; an agency clause prevents this exception. Specified benefit payments have a separate low-AWf branch. Do not infer low-rate eligibility from a permanent-contract label alone. [Handbook §7.2, §29.13](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).

**AWf revision.** Review low AWf when employment ends within two months and when annual paid hours exceed contracted hours by more than 30%. The overtime test does not apply if average contracted hours across the relevant low-rate contracts exceed 30 weekly; exactly 30 does not meet that exception. Exactly 30% excess does not trigger that test. Qualifying BBL/young-worker exception contracts have exclusions from revision. Multiple contracts, transfers and benefit combinations: Check this point with one of our partner accountants. [Handbook §7.2.1–7.2.3](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).

**Aof.** Ordinary insured wages use low Aof for a small employer, high Aof otherwise. The notice and special startup/transfer rules matter. High Aof applies regardless of employer size to specified WAO/WIA/ZW/WW benefits through the employer or own-risk arrangements, WAZO, Toeslagenwet supplements, old-scheme wachtgeld, and WSW employment with relationship code 21/22; code 23 follows the employer rate. Use the Aof-uitkering boxes for the listed benefits, supplements and wachtgeld. Original boundary case J: a 2024 premium wage sum exactly EUR 1,082,500 meets the ordinary small-employer boundary; this does not turn a high-rate benefit into low-rate wage. [Handbook §7.5](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).

**Cumulative calculation.** For ordinary insured payroll, calculate the increase in the cumulative capped component base: cumulative wage capped at the cumulative maximum, less the component base already charged. Count wage periods in which component wage was enjoyed; a period without period wage creates no extra period maximum. Use published period maxima, never more than the annual maximum. Negative pay, changes of insurance/category, multiple income relationships and overlapping periods need the detailed VCR method. Check this point with one of our partner accountants. Up to 50% of the Whk WGA component may be recovered from net pay; the ZW component cannot be recovered this way. [Handbook ch. 6, §7.6.9–7.7, §8.2](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).

**Working substantial-interest shareholders.** Article 12a compares the most comparable employment, the highest-paid employee of the body/connected bodies, and EUR 58,000. If the employer substantiates that the highest is above the most comparable employment, that comparable wage applies. The EUR 5,000 exception concerns the combined statutory customary wage for all work in the body and connected bodies, not a separate allowance per company; actual pay remains taxable. Do not prorate automatically for part-time work. Uncertain comparators, startups/losses and insurance status: Check this point with one of our partner accountants. [Wet LB art. 12a](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002471/2026-10-08_0/xml/BWBR0002471_2026-10-08_0.xml).

**WKR classification and designation.** First decide whether an item is wage or reimbursement of an intermediary employer cost. Establish any targeted exemption or nil valuation and its conditions before using free space. Designation of eligible wage must occur no later than payment/provision; the records must show it. Genuine administrative errors differ from a later change of choice. Company cars/homes, fines, mortgage-interest benefits and former-employee payments have exclusions/exceptions: Check this point with one of our partner accountants. [Handbook §4.12, §10.1](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).

**Customary test.** Designation may not depart more than 30% from customary comparable arrangements. The authority accepts a total EUR 2,400 per person per year within reason; it is not per occasion or a hard prohibition on higher customary benefits. It cannot replace statutory minimum pay or be assumed for interns. Original decision case I, benefits above EUR 2,400: obtain comparables; splitting payments does not create extra annual room. [Handbook §4.2](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).

**Free space.** Use actual column-14 fiscal wage, combining subnumbers of the same employer. Exclude artists'/professional athletes' fees. Include former-employment wage if no more than 10% of the total; if above 10%, exclude it. Do not annualise a part-year employer's actual wage or carry unused space forward. Targeted exemptions and nil valuations do not consume free space. Apply 80% to the remaining designated excess. [Handbook §10.1.4–10.1.6](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf); [Wet LB art. 31a](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002471/2026-10-08_0/xml/BWBR0002471_2026-10-08_0.xml).

**Group election.** The 95% direct/indirect ownership condition must hold throughout the calendar year. Pool all qualifying concern members, with one first band for the combined payroll; the member with the highest fiscal wage reports/pays. Joining/leaving companies, foundations and former-employment wage in a group: Check this point with one of our partner accountants. Choose by the second-period return of the following year. [Wet LB art. 32](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002471/2026-10-08_0/xml/BWBR0002471_2026-10-08_0.xml); [Handbook §10.2](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).

**Valuation.** Ordinary noncash wage uses the purchase invoice including VAT; absent an invoice or with a connected-company invoice, use market value, subject to statutory special valuations. For designated provisions, aggregate relevant employee contributions may reduce the value, floored at nil. Own-product valuation and special meal/accommodation norms: Check this point with one of our partner accountants. [Handbook §4.5](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf); [Wet LB arts. 13, 31a(14)](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002471/2026-10-08_0/xml/BWBR0002471_2026-10-08_0.xml).

**Travel.** The approved mileage policy allows EUR 0.25 per eligible business/commuting kilometre from 1 January 2026. For prior reimbursement of EUR 0.23 or less, the EUR 0.02 top-up may accompany later pay. If the difference was taxed as wage, correct those returns; if final levy was already paid on it, offset that levy in a following return. Original case E: 1,000 eligible 2026 km previously reimbursed at EUR 0.23 gives a EUR 20 top-up. Netting and cafeteria arrangements: Check this point with one of our partner accountants. [Official mileage update](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/berichten/nieuws/verhoging-onbelaste-kilometervergoeding-hoe-verwerkt-u-dit-in-de-loonaangifte).

**Home working.** The targeted exemption is EUR 2.45 per full or partial home-working day. It cannot be combined on the same day with exempt travel to a fixed workplace, including relevant employer-provided transport. Fixed allowances and mixed travel arrangements: Check this point with one of our partner accountants. [Wet LB art. 31a(2)(k), (12)](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002471/2026-10-08_0/xml/BWBR0002471_2026-10-08_0.xml); [Handbook §22.1.12](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).

**Holiday allowance.** Normally at least 8% of qualifying earnings, including overtime and its supplement; profit/end-year distributions do not enter that statutory base. CAO and high-earner written agreements can alter entitlement: a CAO no-allowance arrangement requires at least 108% of minimum wage; an employee earning more than three times minimum wage can agree a lower amount or none in writing. Payment is at least annual under the actual agreement. Original case D: if all EUR 48,000 earnings qualify and 8% applies, gross holiday allowance is EUR 3,840; net pay needs the correct withholding table. [Official guidance](https://www.rijksoverheid.nl/vraag-en-antwoord/vakantiedagen-en-vakantiegeld/hoe-hoog-is-mijn-vakantiegeld).

## Deadlines and filing

- Register when first taking on an employee; use the authority's registration form and resulting loonheffingennummer/filing letter. [Handbook §2.1](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).
- Use the assigned period and official calendar. September 2026 monthly: due 31 October 2026; December: 31 January 2027. Four-week period 10, 7 September–4 October: due 4 November 2026; period 13: 31 January 2027. Payment must arrive by the filing-letter date; if that is a weekend/public holiday, the handbook requires earlier receipt. [Calendar](https://download.belastingdienst.nl/belastingdienst/docs/tijdvakcodes-aangiftedatums-betaaldatums-lh2101t62fd.pdf); [Handbook §13.4.2](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).
- File a **nihilaangifte** with no employees in the period; a **nulaangifte** with employees but no wage. Keep filing until the authority confirms withholding has ended. [Handbook §13.2.3, §13.2.10](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).
- File digitally through suitable software, an intermediary, or Mijn Belastingdienst Zakelijk (maximum 10 income relationships per loonheffingennummer). Keep acceptance/status evidence; repair rejected messages. [Handbook §13.2.1, §13.3](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).
- Before the deadline resend a complete corrected return; software may instead support an additional return. Afterwards normally attach a correction to a still-open return. Prior-year/specified cases require separate corrections; a self-discovered error requiring a separate correction must be sent within eight weeks. Correct dependent cumulative later periods too. [Handbook §14.1–14.4](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).
- For a disagreement with the applied law after correct calculation/payment, object within six weeks of payment. [Handbook §13.2.9](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).
- Give a payslip at first payment and whenever pay changes; digital delivery needs employee consent and a statement that can be saved for later. Give the jaaropgaaf after year-end, also without request. Reconcile it with corrected payroll. [Handbook ch. 12, 15](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).
- Settle 2026 WKR final levy no later than the second-period return of 2027 (February for monthly filers); earlier settlement/on-account payments are possible. If withholding ends during 2026, settle with that final period. [Wet LB art. 31a(16)](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002471/2026-10-08_0/xml/BWBR0002471_2026-10-08_0.xml); [Handbook §10.1.6](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).

## Penalties and interest

Ordinary filing default: seven-calendar-day leniency; after that EUR 83. Incorrect/incomplete filing can also attract EUR 83. Exceptional filing-default penalties can reach EUR 1,675. The grace period does not extend the filing deadline. [Handbook §13.5.2–13.5.5](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).

Ordinary payment default: seven-calendar-day leniency avoids the penalty only if the preceding return was paid timely and in full. Otherwise, or after that period, 3% of the late/unpaid amount, minimum EUR 50, maximum EUR 6,709. If payment is partly within and partly after leniency, the penalty uses the total. Filing and payment penalties can both arise. Exceptional payment defaults can reach 10%, capped at EUR 6,709. Intent/gross negligence and extra payment after corrections need separate assessment: Check this point with one of our partner accountants. [Handbook §13.5](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).

Refund interest on negative corrections, other interest and director/inability-to-pay liability and notification deadlines: Check this point with one of our partner accountants.

## Cross-border points

Dutch withholding and social-insurance coverage must be established separately; record work/residence countries, treaty facts and A1/coverage certificates. Foreign-employer voluntary registration, treaty/183-day allocation, foreign wage in the WKR base and cross-border credits: Check this point with one of our partner accountants. Routes: `nl-cross-border`, `nl-social-contributions`, `nl-income-tax`.

Expat decisions, salary norms, WNT caps, actual extraterritorial costs, scheme duration and 2027 transitions: Check this point with one of our partner accountants. Route: `nl-30-percent-ruling`. Original case F retains EUR 72,000 total remuneration, stipulated 30%, EUR 21,600 allowance and EUR 50,400 remainder; these are arithmetic only, with no tax-free entitlement inferred. The old EUR 48,013 salary-boundary outcome is held for specialist confirmation.

Other retained specialist topics: AOW transition and age-specific rates/credits, elderly credit; public-sector/Ufo payroll; competing exemptions/nil valuations and deemed designation; gifts to domestic/foreign business contacts, agency workers and freelancers (including recipient notice/records); vans used alternately; assessment gross-up and designation failures; excess-severance/RVU levies; relocation, own-product discounts, temporary stays, necessary tools/computers/phones, training, workplace/health-and-safety/clothing/bicycle exemptions; maternity/partner leave and UWV; working-time limits, sickness pay, leave expiry, transition-payment eligibility/cap; detailed payslip/annual-statement fields, third-party-payment reporting and pension reporting. Check this point with one of our partner accountants. Company-car route: `nl-company-car`. Do not use a figure from a neighbouring Guide without establishing that it applies.

## Worked examples

The four existing 2026 cases keep their original inputs. Calculate only under the stated conditions; otherwise obtain the missing facts or partner advice.

**Example 1. One employer, free space exceeded.** Column-14 fiscal wage EUR 1,250,000, including EUR 60,000 former-employment wage (4.8%, within 10%); customary eligible designated benefits EUR 30,000 (gifts, a staff party and a gym subscription), excluding separately exempt allowances. With those classifications confirmed, free space EUR 18,030; excess EUR 11,970; levy EUR 9,576, settled by the February 2027 return for monthly filing. [WKR method above](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002471/2026-10-08_0/xml/BWBR0002471_2026-10-08_0.xml).

```oa-check
name: WKR final levy, single employer, fiscal wage EUR 1,250,000 (2026)
inputs:
  wage: 1250000
  designated: 30000
steps:
  - space: min(wage, 400000) * 0.02 + max(wage - 400000, 0) * 0.0118
  - excess: max(designated - space, 0)
  - levy: excess * 0.8
expected:
  space: 18030
  excess: 11970
  levy: 9576
```

**Example 2. Group election.** A: wage EUR 300,000, designation EUR 9,000. B: wage EUR 500,000, designation EUR 6,000. Original shareholding: 100%. **If** that link held throughout 2026, all qualifying members are included and these are eligible bases/designations, separate levy is EUR 2,400; pooled space EUR 12,720 and levy EUR 1,824; saving EUR 576. B pays. Otherwise the group result is not established. [Wet LB art. 32](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002471/2026-10-08_0/xml/BWBR0002471_2026-10-08_0.xml).

```oa-check
name: WKR group election versus separate calculation (2026)
inputs:
  wage_a: 300000
  wage_b: 500000
  des_a: 9000
  des_b: 6000
steps:
  - space_a: min(wage_a, 400000) * 0.02 + max(wage_a - 400000, 0) * 0.0118
  - space_b: min(wage_b, 400000) * 0.02 + max(wage_b - 400000, 0) * 0.0118
  - separate_levy: max(des_a - space_a, 0) * 0.8 + max(des_b - space_b, 0) * 0.8
  - wage_group: wage_a + wage_b
  - space_group: min(wage_group, 400000) * 0.02 + max(wage_group - 400000, 0) * 0.0118
  - group_levy: max(des_a + des_b - space_group, 0) * 0.8
  - saving: separate_levy - group_levy
expected:
  space_a: 6000
  space_b: 9180
  separate_levy: 2400
  space_group: 12720
  group_levy: 1824
  saving: 576
```

**Example 3. Annual reference, not a payroll instruction.** Original inputs: EUR 48,000 in 2026, below AOW age, one employer, credits requested there, no other income. The following result is conditional on Dutch residence and full Dutch national-insurance coverage throughout the year, eligible current-employment wage and no other adjustments/credits; do not infer those facts. Tax EUR 6,573.35 plus premiums EUR 10,751.15, combined EUR 17,324.49 before rounding the components; credits EUR 1,946.47 and EUR 5,528.24; indicative balance EUR 9,849.79. Apply actual payroll-period tables and final assessment rules separately. [Wet LB arts. 20a, 22, 22a](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002471/2026-10-08_0/xml/BWBR0002471_2026-10-08_0.xml); [premium reference](https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf).

```oa-check
name: Employee EUR 48,000, under AOW age, credits with this employer (2026)
inputs:
  wage: 48000
steps:
  - wage_tax: 3149 + (wage - 38883) * 0.3756
  - premium: min(wage, 38883) * 0.2765
  - gross: wage_tax + premium
  - ahk: max(3115 - max(wage - 29736, 0) * 0.06398, 0)
  - ak: max(5685 - max(wage - 45592, 0) * 0.0651, 0)
  - withheld: max(gross - ahk - ak, 0)
expected:
  wage_tax: 6573.35
  premium: 10751.15
  gross: 17324.49
  ahk: 1946.47
  ak: 5528.24
  withheld: 9849.79
```

**Example 4. Employer premiums.** Original EUR 7,000 every month, small employer, written indefinite contract, assumed Whk decision 1.5%. **If** the contract is also non-on-call, normal low-AWf treatment remains valid, the employee is insured for all listed components and employer Zvw applies with identical bases, the ordinary full-month capped base is EUR 6,617.41. Five contributions total EUR 1,132.24. Prior-pay/cumulative adjustments and eligibility must be established; no employee net pay follows. [Appendix tables 9, 11–12](https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf).

```oa-check
name: Small employer, EUR 7,000 monthly wage, capped premiums (2026)
inputs:
  wage: 7000
  cap: 6617.41
  whk: 1.5
steps:
  - base: min(wage, cap)
  - awf: base * 0.0274
  - aof: base * 0.0627
  - wko: base * 0.005
  - whk_amt: base * whk / 100
  - zvw: base * 0.061
  - total: awf + aof + wko + whk_amt + zvw
expected:
  base: 6617.41
  awf: 181.32
  aof: 414.91
  wko: 33.09
  whk_amt: 99.26
  zvw: 403.66
  total: 1132.24
```

**Preserved earlier 2026 checks.** A: on the original EUR 4,000 full-month common insured base, conditional low AWf/small Aof and stipulated Whk 1.50%, contributions are EUR 109.60 + EUR 250.80 + EUR 20 + EUR 60 + EUR 244 = EUR 684.40; salary plus those costs EUR 4,684.40, excluding other costs. B: conditional high AWf on that same base is EUR 309.60, EUR 200 higher. C: eligible WKR wage EUR 800,000 and EUR 16,000 eligible designations, no group/former-wage exclusions: space EUR 12,720; excess EUR 3,280; levy EUR 2,624. Cases D/E/F/G/H/I/J retain their inputs and actions in the holiday/travel/expat/AWf/anonymous/customary/Aof paragraphs. H specifically retains municipal delay despite timely BSN application and otherwise satisfied identity requirements: obtain written authority agreement as above. [Rates](https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf); [WKR and conditions](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf).

**Original 2025 archive: non-usable tax results.** Preserve EUR 1,000,000 WKR wage; the monthly payroll case with a below-AOW employee, permanent employment, no special deductions and EUR 5,000 gross; and EUR 800,000 WKR wage with EUR 8,000 packages + EUR 5,000 party + EUR 3,000 bicycle. The old 1.92% first band and flat 35.82% monthly withholding shortcut do not establish correct liabilities. Arithmetic of the old premises is EUR 14,760 space on EUR 1,000,000; EUR 1,791 flat withholding and EUR 826.50 listed employer charges on EUR 5,000; EUR 12,400 space, EUR 3,600 excess and EUR 2,880 levy in the EUR 800,000 case. These are withdrawn historical outputs, **not** approved 2025 figures or 2026 inputs. Before using any 2025 outcome: Check this point with one of our partner accountants.

## Ask the client first

Obtain employer registration/period, Whk notice and size decision; per-worker identity/BSN, birth date, residence/work countries and insurance; contract, on-call status, contracted/paid hours and BBL evidence; start/end dates, previous pay/cumulative bases and special-pay annual wage; credit request, other jobs/benefits, pension/CAO, net-pay agreements, DGA/expat decisions; actual wage and benefit values/employee contributions/designation records; former-employment wage/artists' fees; group ownership dates/membership and election; gifts/recipient notices, vans and prior unrecorded items. Do not guess missing inputs. Reconcile the payroll journal, employee records, return, payment and annual statements; preserve acceptance/payment evidence and quantify corrections.

## Sources

| Official source and passages read | URL | Read on |
|---|---|---|
| Read for: Wet LB 1964, verified official XML edition effective 8 October 2026; arts. 6, 10–13, 20a, 22, 22a, 26b, 31a, 32; retained annual-rate/director/anonymous/group provisions also matched to the official January edition | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002471/2026-10-08_0/xml/BWBR0002471_2026-10-08_0.xml | 2026-11-26 |
| Read for: Handboek Loonheffingen, March 2026; cited payroll, WKR, valuation, identity, premium, filing/correction and penalty passages | https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf | 2026-11-26 |
| Read for: rates appendix 2026, edition 4; tables 1–2, 9, 11–13 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf | 2026-11-26 |
| Read for: September/December monthly and four-week periods 10/13 filing/payment dates | https://download.belastingdienst.nl/belastingdienst/docs/tijdvakcodes-aangiftedatums-betaaldatums-lh2101t62fd.pdf | 2026-11-26 |
| Read for: approved mileage policy implementation and correction routes | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/berichten/nieuws/verhoging-onbelaste-kilometervergoeding-hoe-verwerkt-u-dit-in-de-loonaangifte | 2026-11-26 |
| Read for: minimum wage, January/July 2026 age categories | https://www.rijksoverheid.nl/themas/werk/minimumloon/bedragen-minimumloon/bedragen-minimumloon-2026 | 2026-11-26 |
| Read for: holiday allowance basis, exceptions and payment | https://www.rijksoverheid.nl/vraag-en-antwoord/vakantiedagen-en-vakantiegeld/hoe-hoog-is-mijn-vakantiegeld | 2026-11-26 |

Not yet confirmed: all specialist topics expressly referred above, including 2025 archived tax outcomes, remain non-usable until resolved. No 2027 proposal is applied as enacted 2026 law. Check this point with one of our partner accountants.
