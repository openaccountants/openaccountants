---
name: no-income-tax
description: "Use this skill whenever asked about Norwegian income tax for self-employed individuals (enkeltpersonforetak), alone or alongside wages, for income years 2025 and 2026. Trigger on phrases like \"Norwegian tax\", \"trinnskatt\", \"alminnelig inntekt\", \"personfradrag\", \"skattemelding\", \"RF-1175\", \"naeringsoppgave\", \"enkeltpersonforetak\", \"self-employed tax Norway\", or any question about filing or computing income tax for a Norwegian self-employed client. Covers alminnelig inntekt (22%), trinnskatt (5 brackets), personinntekt, trygdeavgift, skjermingsfradrag, personfradrag, minstefradrag, naeringsinntekt computation, deductible expenses, depreciation, the naeringsspesifikasjon that replaced RF-1175, filing deadlines, and penalties. ALWAYS read this skill before touching any Norwegian income tax work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/no-income-tax"
  jurisdiction: "NO"
  tax_year: "2026"
  last_updated: "2026-11-05"
---

# Norway income tax for self-employed individuals (enkeltpersonforetak) v2.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Coverage: the label 2026 means the income year 1 January to 31 December 2026, for which the return falls due by 31 May 2027. The file also covers income year 2025, for which the return fell due by 31 May 2026. The prior version labelled itself 2025. The income year is the calendar year unless otherwise provided (skatteloven § 14-1(1)). A business with accounting duty that uses a different accounting year under § 14-1(3) is Needs Input. Rates come from the annual Stortinget resolutions. Figures in the budget for 2027 are not used anywhere in this file.

## Who this applies to

A natural person who is tax resident in Norway for the whole income year and owns an enkeltpersonforetak, with or without wages, pension, rent or capital income. Skatteetaten is the tax authority. The portal is skatteetaten.no, where the skattemelding and næringsspesifikasjon are opened and sent; an accounting or year-end system can send them instead. The prior version gave Altinn as a filing route. The Skatteetaten pages read for this file name skatteetaten.no and systems for filing, and name the Altinn inbox only for forskuddsskatt invoices.

A person is resident when they live in Norway, or stay for more than 183 days in any 12 month period or more than 270 days in any 36 month period (skatteloven § 2-1). The exit rules in § 2-1 are not expanded here. Part-year residents, non-residents and dual residents are refused (R-NO-5).

Filing unit: spouses are taxed separately on income (skatteloven § 2-11(1)). Income from a business owned by one or both spouses may, on documentation, be split by each spouse's work and participation (§ 2-11(2)). Joint taxation under § 2-10 covers wealth, and wealth tax is outside this file.

### What this file is

This file is a Tier 2 reference with review pending. Each statement has 1 of 3 standings:

- **Enacted.** Read in an Act, a regulation or a Stortinget resolution on Lovdata.
- **Practice.** Published by Skatteetaten on a rate page, a guidance page or in Skatte-ABC 2025. It shows how the authority applies the rule and is not itself the statute. Skatte-ABC 2025 still prints some 2024 amounts, so an amount in it is not used without a year check.
- **Held.** Not confirmed from a primary source. It is listed on the 'Not yet confirmed' line under Sources.

An amendment that has been enacted but has no effect for 2025 or 2026 is named as such and is not applied.

**Operational hold.** This file does not fill the complete country companion contract in `income-tax-workflow-base`, so it does not support unattended preparation:

- The pattern library and bank formats are carried from the prior version. Their narrations and file layouts were not tested against bank files.
- The skjermingsrente for 2026 is held, so a 2026 skjermingsfradrag cannot be computed.
- The rule for converting foreign currency was not read, so any foreign-currency item is Needs Input.
- Skattebegrensning and the pension credit are identified but not computed.
- The companions `no-social-contributions`, `no-capital-gains`, `norway-mva` and `no-tax-overview` have not been converted, and conflicts with them are listed under Source conflicts.

**Reviewer warning.** Any working paper produced under this file is a working paper only. It must show which inputs were confirmed and which are Needs Input, and it must carry the label 'estimated, not reviewed'. Do not present a calculation as definitive. A qualified professional, such as a statsautorisert revisor or registrert revisor, must review it before anything is filed or paid.

### Question threshold

Tier 2 question threshold: NOK 0. No row is filtered on amount: a material question goes to the client or the reviewer whatever its size, because no text read sets a floor.

### Refusals

A refusal is a full stop. When a trigger applies, output the message verbatim and end. Do not classify part of the file first. Where a trigger is only suspected, ask the client the question that resolves it.

- **R-NO-1, company.** Trigger: the income belongs to an aksjeselskap (AS) or allmennaksjeselskap (ASA). Message: 'This skill covers enkeltpersonforetak only. Aksjeselskap files separate return. Out of scope.'
- **R-NO-2, cross-border.** Trigger: the client has foreign-source income, a foreign permanent establishment, foreign tax paid, or a treaty question. Message: 'Cross-border income requires specialist analysis. Escalate.'
- **R-NO-3, restructuring.** Trigger: the business is being converted or restructured (omdanning). Message: 'Business restructuring (omdanning) requires specialist advice. Escalate.'
- **R-NO-4, petroleum.** Trigger: the income is subject to petroleum taxation. Message: 'Petroleum taxation is out of scope.'
- **R-NO-5, residence.** Trigger: the client was not tax resident in Norway for the whole income year, became or stopped being resident in the year, or is a dual resident. Message: 'Stop. This file covers full-year Norwegian tax residents only. Thresholds and allowances change for part-year residents, so this needs a reviewer.'
- **R-NO-6, outside coverage.** Trigger: the requested income year is not 2025 or 2026. Message: 'Stop. This file covers income years 2025 and 2026 only. Do not apply its figures to another year.'
- **R-NO-7, regime not covered.** Trigger: any of these 6 cases: a share of a selskap med deltakerfastsetting; farming or forestry; reindeer husbandry; fishing or catching; income taxed under the Svalbard tax Act; or a trade that pays a product levy under folketrygdloven § 23-5. Message: 'Stop. This regime has its own deductions, rates or return. This file does not compute it, so this needs a reviewer.'
- **R-NO-8, no bank statement.** Trigger: no bank statement for the full income year has been supplied. Message: 'Stop. I cannot prepare this without the bank statement for the full income year.'

### Required inputs

**Minimum viable:** the bank statement for the full income year, and confirmation that the business is an enkeltpersonforetak. A missing bank statement is a hard stop (R-NO-8). A missing recommended or ideal item is a warning in the reviewer brief, not a refusal.

**Recommended:** all invoices, the prior year skattemelding, an asset register and forskuddsskatt payment records.

**Ideal:** the prior year næringsspesifikasjon or, for 2022 or earlier, the RF-1175; a balance sheet (needed for skjermingsfradrag); and a documented mileage log if a vehicle is claimed.

### Prohibitions

- Never apply minstefradrag to næringsinntekt. The exception is care of children in the carer's own home under skatteloven § 6-31(1)(d), which is Needs Input.
- Never apply trinnskatt to alminnelig inntekt. It applies to personinntekt.
- Never blend the 2 bases. Personfradrag and carried-forward underskudd reduce alminnelig inntekt only. Skjermingsfradrag reduces personinntekt only.
- Never use the wage rate for næringsinntekt. The rates are 7.7% wage and 10.9% business for 2025, and 7.6% wage and 10.8% business for 2026. The exception is own-home childcare under folketrygdloven § 23-3(2) nr. 2, which is Needs Input.
- Never include MVA in taxable revenue of a registered person, and never strip MVA before verifying that the amount carried it and at which rate.
- Never expense an asset costing NOK 30,000 or more with a life of 3 years or more. It goes on saldo.
- Never claim income tax or trygdeavgift as a business expense. This is a conservative default: the direct authority is held.
- Never allow education for a new profession as a deduction.
- Never ignore personfradrag where the client is in class 1.
- Never use a figure from the wrong income year, a budget proposal, or the 2 prior version figures of NOK 15,000 and NOK 104,450.
- Never present calculations as definitive.

## Rates, bands and thresholds

The label 2026 means the income year 1 January to 31 December 2026; income year 2025 is also covered. All rows below are Enacted unless they say Practice or Held. Lovdata law was read from Lovdata's public data bundles; the source column names the instrument and section.

### Tax on alminnelig inntekt

The 22% in the prior version is a sum of 3 rates on the same base, and its parts changed between the years.

| Item | 2025 | 2026 | Official source |
| --- | --- | --- | --- |
| Fellesskatt, general | 6.6% | 8.25% | Stortingets skattevedtak 2025 and 2026 § 3-2 (FOR-2024-12-13-3203; FOR-2025-12-18-2747): https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| Fellesskatt, Finnmark county and Karlsøy, Kvænangen, Kåfjord, Lyngen, Nordreisa, Skjervøy and Storfjord municipalities | 3.1% | 4.75% | Skattevedtak 2025 and 2026 § 3-2: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| Municipal income tax, maximum | 12.75% | 11.35% | Skattevedtak 2025 and 2026 § 3-8: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| County income tax, maximum | 2.65% | 2.40% | Skattevedtak 2025 and 2026 § 3-8: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| Total at the maximum, general | 22.00% | 22.00% | Sum of the rows above: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| Total at the maximum, Finnmark and the named municipalities | 18.50% | 18.50% | Sum of the rows above: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |

The municipal and county rates are maxima, which Stortinget sets each year (skatteloven § 15-2). The rates that apply are those the municipality and county adopt under § 15-3, which may be changed by the end of April after the income year; confirm them where the result depends on them. The resolution excludes owner income that is scaled up under the listed sections from these rates, so dividends and share gains are outside this table and go to `no-capital-gains` and the reviewer.

### Trinnskatt on personinntekt

Trinnskatt applies to personinntekt under skatteloven chapter 12 for class 0 and class 1. Each rate applies to the part of the income between its threshold and the next. The resolutions read contain no lower rate for Finnmark.

| Trinn | Income year | Above (NOK) | Rate | Official source |
| --- | --- | --- | --- | --- |
| 1 | 2025 | 217,400 | 1.7% | Skattevedtak 2025 § 3-1: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| 2 | 2025 | 306,050 | 4.0% | Skattevedtak 2025 § 3-1: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| 3 | 2025 | 697,150 | 13.7% | Skattevedtak 2025 § 3-1: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| 4 | 2025 | 942,400 | 16.7% | Skattevedtak 2025 § 3-1: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| 5 | 2025 | 1,410,750 | 17.7% | Skattevedtak 2025 § 3-1: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| 1 | 2026 | 226,100 | 1.7% | Skattevedtak 2026 § 3-1 and Skatteetaten: https://www.skatteetaten.no/satser/trinnskatt/ |
| 2 | 2026 | 318,300 | 4.0% | Skattevedtak 2026 § 3-1 and Skatteetaten: https://www.skatteetaten.no/satser/trinnskatt/ |
| 3 | 2026 | 725,050 | 13.7% | Skattevedtak 2026 § 3-1 and Skatteetaten: https://www.skatteetaten.no/satser/trinnskatt/ |
| 4 | 2026 | 980,100 | 16.8% | Skattevedtak 2026 § 3-1 and Skatteetaten: https://www.skatteetaten.no/satser/trinnskatt/ |
| 5 | 2026 | 1,467,200 | 17.8% | Skattevedtak 2026 § 3-1 and Skatteetaten: https://www.skatteetaten.no/satser/trinnskatt/ |

### Allowances and fixed deductions

| Item | 2025 | 2026 | Official source |
| --- | --- | --- | --- |
| Personfradrag, class 1 | NOK 108,550 | NOK 114,540 | Skattevedtak 2025 and 2026 § 6-3, skatteloven § 15-4, and Skatteetaten: https://www.skatteetaten.no/satser/personfradrag/ |
| Class 0 | No personfradrag | No personfradrag | Skatteloven § 15-4(6): https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 |
| Minstefradrag, wages | 46%, maximum NOK 92,000 | 46%, maximum NOK 95,700 | Skatteloven § 6-32, skattevedtak § 6-1, and Skatteetaten: https://www.skatteetaten.no/satser/minstefradrag/ |
| Minstefradrag, pension | 40%, maximum NOK 73,150 | 40%, maximum NOK 75,400 | Skatteloven § 6-32, skattevedtak § 6-1: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| Wage and pension together | Sum, capped at NOK 92,000 | Sum, capped at NOK 95,700 | Skatteloven § 6-32(1): https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 |
| Finnmark and named municipalities deduction, on tax computation only | NOK 30,000 (Practice) | NOK 45,000 | 2026: skatteloven § 15-5(2) as amended by lov 22 Dec 2025 nr. 119, https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2. 2025: Skatte-ABC 2025 T-12-1, https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/t-12-tiltakssonen-i-finnmark-og-nord-troms/T-12.001/ |
| Skattebegrensning limits (single, each spouse, couple) | NOK 157,450, 145,550 and 291,100 | NOK 163,750, 151,350 and 302,700 | Skattevedtak 2025 and 2026 § 6-4: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| Pension credit (amount, trinn 1, trinn 2) | NOK 36,000, 276,400 and 422,950 | NOK 39,100, 294,200 and 437,100 | Skattevedtak 2025 and 2026 § 6-5: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| Trial work deduction | None | NOK 125,000, tapered 40% above NOK 345,000 | Skattevedtak 2026 § 6-6, skatteloven § 6-86: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |

The Finnmark deduction goes to a person tax resident in that area who has personfradrag, unless a child under 17 at the end of the year. It is given in the tax computation, does not change alminnelig inntekt as fixed, and has no effect on trygdeavgift or trinnskatt (§ 15-5(1) to (3)). Skattebegrensning and the pension credit are not computed in this file: where a client's income is near those limits, or the client has pension, mark Needs Input. The trial deduction applies only to the persons drawn at random: 8% of those born from 1991 to 2006 on the 31 October 2025 register, for 5 income years. It reaches beregnet personinntekt under § 12-2 g and cannot create a loss to carry forward.

### Trygdeavgift

The base is personinntekt under skatteloven § 12-2 (folketrygdloven § 23-3). Stortinget sets the rates each year.

| Income type | 2025 | 2026 | Official source |
| --- | --- | --- | --- |
| Høy sats: beregnet personinntekt from an enkeltpersonforetak (næringsinntekt) | 10.9% | 10.8% | Folketrygd resolutions 2025 §§ 6 to 8 (FOR-2024-12-13-3204): https://api.lovdata.no/v1/publicData/get/lovtidend-avd1-2001-2025.tar.bz2 and 2026 (FOR-2025-12-18-2748) with Skatteetaten: https://www.skatteetaten.no/satser/trygdeavgift/ |
| Mellomsats: lønnsinntekt (employment) | 7.7% | 7.6% | Same resolutions: https://www.skatteetaten.no/satser/trygdeavgift/ |
| Lav sats: pensjonsinntekt (pension), and personinntekt of a person under 17 or over 69 | 5.1% | 5.1% | Same resolutions, folketrygdloven § 23-3(2): https://www.skatteetaten.no/satser/trygdeavgift/ |
| Mellomsats on business income: care of a child in the carer's own home, where the child has not turned 12 before the end of the year or has a special need for care | 7.7% | 7.6% | Folketrygdloven § 23-3(2) nr. 2: https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 |
| No contribution | Income up to NOK 99,650 | Income up to NOK 99,650 | 2026: folketrygdloven § 23-3(4), https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2. 2025: Skatte-ABC 2025 P-16-4.3 (Practice), https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/p-16-personinntekt--trygdeavgiftpensjonspoengpensjonsbeholdning/P-16.027/P-16.035/ |
| Maximum | 25% of the income above NOK 99,650 | 25% of the income above NOK 99,650 | Same sources: https://www.skatteetaten.no/satser/trygdeavgift/ |

The age test runs by year: the middle and high rates apply from the year a person turns 17 to the year they turn 69 (Skatte-ABC 2025 P-16-4.2.2, Practice), so ask the year of birth. The floor and the cap apply to total personinntekt across the low, middle and high bases, not to each type (Skatte-ABC 2025 P-16-4.3). Mellomsats also applies to § 12-10 personinntekt in a trade paying product levy, which R-NO-7 refuses. The rows name only the limbs this file uses: folketrygdloven § 23-3(2) also lists benefits at the low and middle rates, including overgangsstønad, arbeidsavklaringspenger and uføretrygd, so any NAV benefit is Needs Input.

The cap only bites at low income. At the 2025 høy sats the cap and the rate meet at about NOK 176,684 of personinntekt, since 99,650 × 25% ÷ (25% − 10.9%) = 176,684.40.

### Skjermingsrente for an enkeltpersonforetak

| Income year | Maximum rate | Status | Official source |
| --- | --- | --- | --- |
| 2025 | 4.6% (3-month treasury bill mean 4.1480, plus 0.5 points, rounded to the nearest tenth) | Practice | Skatteetaten rate page, under FSFIN §§ 10-12-1 and 12-12-10: https://www.skatteetaten.no/en/rates/risk-free-interest-rate-for-shares-and-sole-proprietorships/ |
| 2026 | unverified: held. Do not use the 2025 rate. | Held | Same page, with FSFIN § 10-12-1(2): https://www.skatteetaten.no/en/rates/risk-free-interest-rate-for-shares-and-sole-proprietorships/ |

Skattedirektoratet announces the rate in January after the income year (FSFIN § 10-12-1(2)). A lower rate may be chosen only in whole percentage points, and by the time the return is filed on time. Where no clear choice is made, the maximum applies (FSFIN § 12-12-10(2)).

### Depreciation groups

The rates are maxima in skatteloven § 14-43(1), read in the current consolidated text. The threshold of NOK 30,000 has applied from income year 2024.

| Group | Assets | Maximum rate | Official source |
| --- | --- | --- | --- |
| a | Office machines | 30% | Skatteloven §§ 14-41 and 14-43: https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 |
| b | Acquired goodwill | 20% | Same: https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 |
| c | Trailers, lorries, buses, vans, taxis and vehicles for transporting disabled people | 24% | Same: https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 |
| d | Passenger cars, tractors, machinery, tools, instruments, fixtures and fittings | 20% | Same: https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 |
| e | Ships, vessels and rigs | 14% | Same: https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 |
| f | Aircraft and helicopters | 12% | Same: https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 |
| g | Electric power transmission and distribution installations and electrotechnical equipment in power undertakings, and such assets used in other business | 5% | Same: https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 |
| h | Buildings and structures, hotels, lodging houses and eating places | 4% | Same: https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 |
| i | Commercial buildings | 2% | Same: https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 |
| j | Fixed technical installations in buildings | 10% | Same: https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 |

Other limits in § 14-43: simple buildings up to 10%, livestock buildings 6%, fruit plantings 10%, and berry plantings 20%.

### Fixed amounts used in expense rules

| Item | 2025 | 2026 | Official source |
| --- | --- | --- | --- |
| Representation, outside service (uteservering) limit per person per occasion | NOK 579 | NOK 592 | Satsforskrift 2025 § 10 (FOR-2024-11-27-2889) and 2026 § 10 (FOR-2025-11-07-2216): https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| Branded gift item | NOK 317 | NOK 324 | Satsforskrift § 10: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| Attention to a business contact, per occasion | NOK 317 | NOK 324 | Satsforskrift § 10: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| Private car, per km of business driving | NOK 3.50 | unverified: deduction rate held (see note) | 2025 deduction: takseringsregler 2025 § 1-3-20 (FOR-2025-12-01-2404), https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2. 2026: satsforskrift 2026 § 4 |
| Home office standard deduction | NOK 2,192 | NOK 2,240 (Practice) | 2025: takseringsregler 2025 § 1-3-26. 2026: satsforskrift 2026 § 14 and Skatteetaten: https://www.skatteetaten.no/en/rates/home-office-standard-deduction/ |
| Private use of electronic communication | NOK 4,392 per year | NOK 4,392 per year | Skatteloven §§ 6-14 and 5-12(5), and FSFIN § 5-12-21 in the current text, unamended since income year 2014: https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2. Application to a sole trader: Skatte-ABC 2025 E-3-2.1 (Practice), https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/e-3-elektronisk-kommunikasjon-telefon-mv/E-3.019/E-3.020/ |
| Membership of a national trade body, sole trader | unverified: amount held | Up to NOK 8,700, or up to 2 per mille of total wages paid; see Expenses for the other limits | Skatteloven § 6-19(2) and (3), (2) as amended with effect from income year 2026: https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 |

No takseringsregler for 2026 appeared in the data read. The NOK 3.50 in satsforskrift 2026 § 4 is an allowance rate. It does not confirm a deduction rate, so a 2026 deduction per km is Needs Input and stays held under Sources.

### Thresholds outside income tax that this file uses

| Item | Figure | Official source |
| --- | --- | --- |
| MVA registration | Taxable turnover and withdrawals above NOK 50,000 in a 12 month period | Merverdiavgiftsloven § 2-1(1): https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 |
| MVA general rate, 2025 and 2026 | 25%, with reduced rates of 15%, 12% and 11.11% | Stortingsvedtak om merverdiavgift 2025 (FOR-2024-12-13-3208), https://api.lovdata.no/v1/publicData/get/lovtidend-avd1-2001-2025.tar.bz2, and 2026 (FOR-2025-12-18-2752), https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 |
| Bank payment rule | A cost is deductible only if paid through a bank or payment institution, unless the total payment is under NOK 10,000 | Skatteloven § 6-51: https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 |

## The base

### Two income bases

Norway taxes a sole trader on 2 separate bases. Compute both, and keep them apart through the whole ladder.

- **Alminnelig inntekt** is the net of all income and deductions, including capital income. The 22% (or 18.5%) applies to it after personfradrag.
- **Personinntekt** is a gross base with no personfradrag and no general deductions. It is the sum of wages, pension and beregnet personinntekt from the business. Trinnskatt and trygdeavgift apply to it (skatteloven § 12-1; folketrygdloven § 23-3).

The formulas, with every step the law read gives:

```text
naeringsinntekt = driftsinntekter (net of MVA where registered)
                  - driftskostnader - depreciation

alminnelig_inntekt_after_losses = max(naeringsinntekt + wages + pension
                                      - minstefradrag_on_wages_and_pension
                                      + other_income - other_deductions
                                      - underskudd_brought_forward, 0)
tax_on_alminnelig = max(alminnelig_inntekt_after_losses - personfradrag
                        - finnmark_deduction, 0) * 22%   (18.5% where it applies)

beregnet_personinntekt = naeringsinntekt            (before any carried underskudd)
                         + capital_costs_added_back
                         + losses_on_capital_objects
                         + 6_60_and_6_61_and_special_deductions
                         - capital_income
                         - gains_on_capital_objects
                         - skjermingsfradrag
                         - negative_personinntekt_brought_forward

personinntekt = wages + pension + max(beregnet_personinntekt, 0)
trinnskatt    = sum(rate * max(min(personinntekt, next_threshold) - threshold, 0))
trygdeavgift  = 0 if personinntekt <= 99,650
                else min(sum(rate * income_of_that_type),
                         25% * (personinntekt - 99,650))
total_tax     = tax_on_alminnelig + trinnskatt + trygdeavgift
balance       = total_tax - forskuddstrekk - forskuddsskatt_paid
```

The balance is restskatt when positive and an amount tilgode when negative. A beregnet personinntekt below zero is not set against wages or pension: see Losses.

### Næringsinntekt

Næringsinntekt is gross revenue minus cost of sales, operating expenses and depreciation. Income is taken in the year the taxpayer has an unconditional right to it, and a cost is deducted in the year an unconditional obligation to cover it arises, unless otherwise provided (skatteloven § 14-2). Treat deposits, part payments and receipts that straddle year end as timing items under that rule, not by averaging.

### Beregnet personinntekt

Personinntekt is computed for the owner only when the enkeltpersonforetak operates a business (skatteloven § 12-10). The computation starts from alminnelig inntekt from the business before carried-forward losses (§ 12-11(1)) and then adjusts:

- **Add** actual capital costs and capital losses (§ 12-11(2)). Two items are not added: losses on customer receivables; and interest on business debt to financial institutions or on bonds, to the extent that debt does not exceed the shield basis after deducting supplier credit and customer prepayments but before deducting debt. Interest on any other debt is added. Skatte-ABC 2025 E-5-5.5.1 confirms this reading.
- **Add** deductions under §§ 6-60 and 6-61, and the farming, reindeer and slate deductions.
- **Deduct** actual capital income, except on customer receivables, and gains on the same objects (§ 12-11(3)).
- **Deduct** skjermingsfradrag where it is chosen.
- **No personinntekt** arises on gains on ordinary farm property, milk quota or forestry (§ 12-11(4)).

Where only one spouse works in the calculation unit, that spouse takes the personinntekt, whoever owns the business. Where both work in it, personinntekt is split in proportion to each spouse's positive alminnelig inntekt from the unit (Skatte-ABC 2025 E-5-7.2).

There is no joint calculation across businesses with different trygdeavgift rates (FSFIN § 12-20-1), so more than 1 business is Needs Input.

### Skjermingsfradrag

Skjermingsfradrag shields a risk-free return on business capital from trinnskatt and trygdeavgift. It reduces personinntekt only, is chosen for each calculation unit, and has no effect on the 22% (skatteloven §§ 12-11(3)(c) and 12-12; Skatte-ABC 2025 E-5-6.1).

```text
skjermingsgrunnlag = mean of opening and closing value of:
    + operating assets within § 14-40(1), smaller assets in a saldo pool,
      stock, customer receivables, acquired goodwill and other acquired
      intangibles used in the business
    - debt to financial institutions and on bonds
    - supplier credit and customer prepayments
skjermingsfradrag = max(skjermingsgrunnlag, 0) * skjermingsrente
```

Assets count only if they have worked in the business. A physical asset must really have been taken into use: delivery and entry on saldo are not enough (Skatte-ABC 2025 E-5-6.2.10, Practice). An asset below either § 14-40(1) test is left out even if capitalised, unless it has gone into a pool (samlesaldo), so a pooled smaller asset counts (Skatte-ABC 2025 E-5-6.2.3, Practice). Assets used for welfare measures mainly outside working hours are excluded. Undeducted research and development costs may be added. Value is tax value, with 3 exceptions: a non-depreciable asset takes the higher of historic cost and the value at assessment; an asset valued at book value in the 1999 capital base may stay there; and an operating asset of disproportionately high value counts only at an amount usual for that type of business. The method used in the first year binds later years (§ 12-12(2)). A part-year business reduces the shield by whole months (FSFIN § 12-12-6(4)). FSFIN § 12-12-7 allows an alternative mean for stock, customer receivables and customer prepayments where documented stock values exceed the ordinary mean by at least 40%. Flag every shield for the reviewer: it needs an accurate balance sheet.

### Expenses

A cost is deductible when it is incurred to acquire, maintain or secure taxable income (skatteloven § 6-1(1)). Private costs for the taxpayer or family, including housing, food and upkeep, are not deductible (§ 6-1(2)). A mixed cost follows the rule for that cost below; a mixed cost with no rule here is Needs Input. A payment totalling NOK 10,000 or more must go through a bank or payment institution, with payments for the same delivery, service or contract counted as one and periodic payments deducted in the same year seen together (§ 6-51(1)).

| Item | Rule | Basis |
| --- | --- | --- |
| Representation | Not deductible, with limited exceptions (§ 6-21) | See below |
| Fines | Fines and charges of a mainly penal kind imposed under statute are not deductible, including tilleggsskatt and road traffic fines. Charges that are not mainly penal, such as tvangsmulkt and a parking-lot excess charge, may be deductible if tied to income | Skatte-ABC 2025 B-21-1 (Practice) |
| Income tax and trygdeavgift | Not claimed, as a conservative default. § 6-15(1) allows tax and charges on real property or a particular trade, and no text read gives a deduction for income tax or trygdeavgift. No text read states a prohibition either: the direct authority is held | Skatteloven § 6-15; Held |
| Capital items | Through saldo, see Depreciation | Skatteloven § 14-40 |
| Education for a new profession | Costs to reach a degree or competence are not deductible. Costs to maintain an education, or to keep up with a field, are deductible where the client uses it to earn income | Skatte-ABC 2025 U-3-1 and U-3-3 (Practice) |
| Minstefradrag on næringsinntekt | Blocked. It applies to wages, pension, board and similar fees, publisher payments other than royalties, and own-home childcare under § 6-31(1)(a) to (d) and (2). A spouse's income from the other spouse's business gets none (§ 6-32(3)) | Skatteloven §§ 6-31 and 6-32 |
| Membership dues | No deduction except under §§ 6-19 and 6-20 (§ 6-18). A sole trader can use § 6-19(2): a nationwide trade body whose main purpose is that group's economic interests, active trader, proof of payment by the filing deadline, excluding insurance and other non-association parts, and not where § 6-20 dues are claimed. § 6-19(3) caps the total under (1) and (2) at 2 per mille of total wages paid. Read literally, that sits awkwardly with the NOK amount in (2). Skatte-ABC 2025 K-3-5.2.1 (Practice) takes the higher of the amount and 2 per mille of wages paid in the year before the income year, across all memberships. Flag for the reviewer: held. § 6-20 union dues are for wage earners and active fishers only | Skatteloven §§ 6-18 to 6-20; Skatte-ABC 2025 K-3-5.2.1 |
| Legal costs on a tax dispute | Needs Input. Skatte-ABC 2025 K-4-5.2.1 records case law refusing deduction | Skatte-ABC 2025 K-4-5.2.1 (Practice) |

**Representation.** Modest hospitality of customers is deductible only in business hours or directly tied to negotiations or demonstrations, at the workplace or a nearby eating place if no reasonable service exists on site. Buying spirits or tobacco gets no deduction, and serving spirits with the meal loses the food deduction too. For outside service (uteservering), a cost over the limit per person per occasion is wholly non-deductible, not only the excess (FOR-1999-11-22-1160 § 6-21-2; satsforskrift § 10). Gifts get no deduction (§ 6-21-4). Branded items and attentions have their own limits above (§§ 6-21-5 and 6-21-6).

**Home office.** Rooms in the home used solely in the business give a deduction. Combined use of a room as work room and, for example, living room or bedroom gives no deduction at all (Skatte-ABC 2025 B-14-2.1). In an owner-occupied home outside accounts, where the owner uses at least half the property as a home by rental value, the owner takes the standard deduction above, or actual costs tied to the work part with shared costs split by rental value, or by area if the 2 parts are equivalent and rental value is hard to fix. The standard deduction is not cut for part-year use. In a rented home, actual costs are split by rental value or, alternatively, area. The owner's or spouse's own cleaning work is not deductible (B-14-2.2). Equipment in the home office needs at least half its use in the business (B-14-3.2). Flag a later sale of the home: use as a home office for more than 1 of the last 2 years can make part of a gain taxable (B-14-2.4). A home office in a home on the accounts follows the accounting rules for buildings.

**Vehicle.** The method follows from the car's status and is not a free choice:

- A car used only in business is a yrkesbil at any distance. So is a lorry of 7,500 kg or more, or a bus with more than 15 passenger seats, when used in the trade.
- Any other car is a yrkesbil if it does at least 6,000 km a year in business, over a 3 year view, or more than half its use is business.
- A yrkesbil deducts all actual costs, including depreciation in group c or d, less the private-use reversal under skatteloven §§ 6-12 and 5-13. The km rate is not available for it.
- Any other car is a private car: no actual costs. For 2025 it takes NOK 3.50 per km of documented business driving, normally up to 6,000 km (takseringsregler 2025 § 1-3-20). That rate covers depreciation, fuel or charging, road tax and insurance, so fuel is not claimed separately. For 2026 the deduction per km is Needs Input (see Fixed amounts used in expense rules).
- For 2025 the rate rises by NOK 1.00 per km for each passenger, on forest and construction roads, and for equipment that does not fit in a boot or on a roof rack. Other 2025 rates per km: motorboat NOK 7.50, snowmobile or ATV NOK 10.00, heavy motorcycle NOK 2.95, moped or light motorcycle NOK 2.00 (takseringsregler 2025 § 1-3-20). The 2026 figures are held.
- Parking, tolls and ferries on business trips are deductible on top, for either type. So are repair costs and excess from damage on a business trip.
- Driving between home and a fixed place of work is normally not business driving. A logbook is not mandatory but is usually the decisive evidence, and without adequate evidence the driving may be set by discretion (Skatte-ABC 2025 B-5-3 and B-5-4).
- Fines are not deductible.

**Phone and internet.** A sole trader deducts the cost in the business, and the deduction is reduced by the NOK 4,392 private-use amount (skatteloven § 6-14; Skatte-ABC 2025 E-3-2.1). A service in the home is deductible where its use is necessary for proper practice of the trade, and the reduction is limited to actual cost where that is lower (E-3-2.3). For a separate subscription at a workplace not tied to the home, there is no reduction where private use outside the ordinary work situation is not possible (E-3-2.2). Where the service has no confirmed business use, deduct nothing.

### Depreciation

An asset goes on saldo when it is both lasting, with a life of at least 3 years, and significant, costing NOK 30,000 or more including MVA where there is no right to deduct it (skatteloven § 14-40(1)). An asset below either test may be deducted in the year of acquisition or depreciated (§ 14-40(2)): depreciation is the client's choice, and the default is the deduction. An improvement to an asset on saldo always goes on saldo (§ 14-40(3)).

Both limbs matter:

- Cost under NOK 30,000, life 3 years or more: deduct or depreciate.
- Cost of NOK 30,000 or more, life under 3 years: deduct, or spread over the expected life (Skatte-ABC 2025 D-3-1.1.1).
- A physical asset that does not lose value through wear or age cannot be deducted at any cost (D-3-1.1.2).
- A new physical asset is taken to last 3 years or more unless a shorter life is probable. Intention to sell does not count (D-3-2).

Groups a to d are pooled by trade and municipality; groups e to i have an individual balance per asset; group j is per building (§ 14-41). The base is the opening balance plus cost of the year's additions (§ 14-42(2)), and depreciation is taken on that sum. On sale in groups a to d and j, the price reduces the balance so far as it is not taken to income (§ 14-44(2)). In groups e to i, gain or loss goes to the gain and loss account, and so does a negative balance in group b (§§ 14-44(3) and 14-45). A negative balance in groups a, c, d or j is taken to income at no less than the group's maximum rate (§ 14-46). On the gain and loss account, a positive balance is taken to income at no less than 20%, and a negative balance may be deducted at up to 20% (§ 14-45(4)). The NOK 30,000 tests in § 14-47 apply at the end of the income year, before that year's deduction or income entry. Under NOK 30,000, a depreciation base or a loss balance on the account may be deducted in full (§ 14-47(1)). Under NOK 30,000, a negative balance in groups a, c, d or j or a gain balance on the account must be taken to income in full (§ 14-47(2)).

### Losses

**Against alminnelig inntekt.** A loss of the year is set against the client's other income, then against a spouse's, and any rest is carried forward (skatteloven § 6-3). There is no time limit on carry-forward (Skatte-ABC 2025 U-2-5.1), except that losses lost under the 10 year rule up to 2005 stay lost. The carried loss must be used against the first positive income, oldest first; it cannot be deferred (§ 14-6(1); U-2-4.7). On ceasing a business, an uncovered loss of the final year may instead go back 1 and then 2 years on the taxpayer's claim, and a loss of the year before cessation goes back 1 year (§ 14-7; Skatte-ABC 2025 U-2-6.6). A composition with creditors or a bankruptcy limits carry-forward (§ 14-6(2) and (3)). Lov 19 June 2026 nr. 48 amends § 14-6 from a date the King decides, so it is not applied here.

**Against personinntekt.** A carried underskudd does not reduce personinntekt (§ 12-11(1)). A separate rule does. If the year's beregnet personinntekt is negative, it cannot be set against wages, pension or sick pay, and it carries forward against later positive personinntekt from the same calculation unit (§ 12-13; Skatte-ABC 2025 E-5-8.2.1). It must be claimed in the return (E-5-8.5), and it must be used in the first possible year down to zero: what is not used then is lost. There is no time limit (E-5-8.2.1). It cannot be carried back on ceasing a business (E-5-8.3, Practice). A person exempt from the næringsspesifikasjon who files no personinntekt message has personinntekt set equal to næringsinntekt, and cannot carry a negative amount (skatteforvaltningsforskriften § 8-2-1(3)).

A prior year loss can therefore carry in both bases, with different amounts. Ask for both.

### Computation order

Map the base's ladder as follows. Rung 3 uses the underskudd above. Rung 4 is minstefradrag, then personfradrag, and the Finnmark deduction in the tax computation only. Rung 5 is the 22% (with its 3 parts where a split is wanted) and trinnskatt on personinntekt. Rung 6 is the pension credit and skattebegrensning, which are not computed here. Rung 7 is trygdeavgift on personinntekt. Rung 8 is forskuddstrekk and forskuddsskatt, credited only when evidenced.

### Tiers and defaults

Tier 1 applies where the documents point to one treatment. The base's defaults apply only as this table allows, because the law read supports each result or the client's evidence decides it.

| Missing fact | Treatment | Why |
| --- | --- | --- |
| Business form | Needs Input | A company is R-NO-1, and the prior default of enkeltpersonforetak was a guess about legal form |
| Business-use proportion | 0% business use, flagged | § 6-1(2) and the taxpayer's duty to show the cost |
| Expense of uncertain character | Not deducted, flagged | § 6-1 |
| Receipt of uncertain character | Needs Input | It may be a gift, loan or benefit with a different treatment |
| Asset useful life | For a new physical asset, 3 years or more; use saldo rates where the cost is NOK 30,000 or more | Skatte-ABC 2025 D-3-2 |
| Minstefradrag claimed on næringsinntekt | Not applicable, unless § 6-31(1)(d) is shown | §§ 6-31 and 6-32 |
| Election under § 14-40(2) | Deduct in the year; depreciation needs a client choice | § 14-40(2) |
| Skjermingsrente choice | Maximum rate | FSFIN § 12-12-10(2) |
| Skjermingsgrunnlag or balance sheet missing | No shield in the computation, flagged with the alternative. Do not estimate it | §§ 12-11(3)(c) and 12-12 |
| Representation headcount or attendance | No deduction | The limit cannot be tested, and over the limit nothing is deductible |
| Withholding without a certificate | No credit | Base default |
| Prepayment without a receipt or authority statement | No credit | Base default |
| Tiltakssone residence or other allowance fact | Not claimed | Base default |
| Prior loss without a prior return | Not used | Base default |
| Childcare in own home, year of birth, or 2026 trial deduction selection | Needs Input | The fact decides the rate or deduction |
| 2026 deduction per km for a private car | Needs Input | No 2026 deduction rate was read. Satsforskrift 2026 § 4 sets an allowance rate |
| Trip with a mixed purpose | Needs Input | Skatte-ABC S-21 was not read |

Needs Input also covers: employee or self-employed status for a given engagement; whether an activity is a business or a hobby; any disposal of a significant asset; and which year a large item belongs to.

### MVA interaction

| Scenario | Income tax treatment |
| --- | --- |
| MVA collected (registered) | Not income: exclude from revenue |
| Input MVA recovered | Not an expense: exclude |
| Non-deductible MVA | Part of the cost, and counts in the NOK 30,000 test |
| Not registered | Gross equals net, and no MVA is extracted |

Being under NOK 50,000 does not settle registration on its own: the test is taxable turnover and withdrawals over any 12 month period (merverdiavgiftsloven § 2-1(1)). Before extracting MVA from a receipt, verify that the client was registered at that date and which rate the invoice charged. A sale may be at 25%, 15%, 12% or 11.11%, or may be exempt or outside the scope. Without the invoice, the net figure is Needs Input.

### Classifying a bank line

Each row is a starting point, not a result. Patterns are carried from the prior version and were not tested on bank files. Every 'deductible' below is subject to the Expenses section and § 6-1. If no row fits, use the tiers.

**Income patterns (credits)**

| Pattern | Tax line | Treatment | Notes |
| --- | --- | --- | --- |
| OVERF. [client], BETALING, HONORAR, FAKTURA | Driftsinntekter | Business income | If MVA-registered, extract net only after verifying the rate on the invoice |
| STRIPE PAYOUT, PAYPAL PAYOUT | Driftsinntekter | Business income | Where the payout is net of fees, record the gross amount and the fee separately |
| UPWORK, FIVERR, TOPTAL | Driftsinntekter | Business income | Freelance platform. Ask whether the income is foreign-source: R-NO-2 |
| LONN, ARBEIDSGIVER | Lønnsinntekt | Not self-employment | Employment income, personinntekt at mellomsats |
| LEIEINNTEKT, HUSLEIE MOTTATT | Eiendomsinntekt | Not self-employment | Rental income, alminnelig inntekt; treatment Needs Input |
| RENTER, UTBYTTE, AVKASTNING | Kapitalinntekt | Not self-employment | Alminnelig inntekt only. Dividends go to the reviewer |
| SKATT TILBAKEBETALING | Exclude | Not income | Tax refund |
| NAV UTBETALING | Needs Input | Check nature | Some NAV benefits are taxable, and rates differ by benefit |

**Expense patterns: deductible when the business link is shown**

| Pattern | Category | Notes |
| --- | --- | --- |
| KONTORLEIE, HUSLEIE KONTOR | Lokalekostnader | Dedicated premises. Home use follows Home office |
| YRKESSKADEFORSIKRING, ANSVARSFORSIKRING | Forsikring | Professional or business cover. Cover for the person is Needs Input |
| REVISOR, REGNSKAPSFORER, BOKHOLDER | Revisjonskostnader | Business accounts and returns |
| ADVOKAT (business) | Advokatkostnader | Business-related. A tax dispute is Needs Input |
| KONTORREKVISITA, KONTORMATERIELL | Kontorkostnader | |
| REKLAME, MARKEDSFORING, GOOGLE ADS | Markedsforingskostnader | Gifts and hospitality follow Representation |
| FAGLIG OPPDATERING, KURS, SEMINAR | Utdanningskostnader | Current profession only |
| BRANSJEFORENING | Kontingenter | Only under § 6-19, with its limits |
| FAGFORENING | Kontingenter | Not for a sole trader on business income: § 6-20 needs a wage earner or active fisher. A person with wages claims § 6-19(2) or § 6-20, not both |
| BANKGEBYR, KONTOGEBYR | Bankkostnader | Business account |
| STRIPE FEE, PAYPAL FEE | Transaksjonskostnader | |
| SOFTWARE, ABONNEMENT, LISENS | IT-kostnader | Test a purchased long-term licence under Depreciation |
| PORTO, POSTEN | Portokostnader | |

**Travel**

| Pattern | Category | Treatment |
| --- | --- | --- |
| FLY, SAS, NORWEGIAN, WIDEROE | Reisekostnader | Deductible for business travel. Commuting is normally not business travel (see Vehicle), and a private trip is not deductible (§ 6-1(2)) |
| HOTELL, BOOKING.COM | Reisekostnader | Deductible for business travel |
| NSB, VY, RUTER | Reisekostnader | Deductible for business travel |
| TAXI, UBER, BOLT | Reisekostnader | Deductible for a business purpose |
| BENSIN, DIESEL, CIRCLE K, ESSO, SHELL | Bilkostnader | Yrkesbil: actual cost, less private-use reversal. Private car, 2025: not separately deductible, because NOK 3.50 per km covers it. Private car, 2026: Needs Input. T2 until status is known |
| BOMPENGER, PARKERING | Bilkostnader | Deductible on business trips, in addition to the km rate. T2 |

A trip with a mixed purpose is Needs Input in every row above.

**Limited**

| Pattern | Limit | Notes |
| --- | --- | --- |
| REPRESENTASJON, KUNDEMIDDAG | Outside service: NOK 579 per person per occasion for 2025, NOK 592 for 2026 | Above the limit the whole bill is non-deductible. Document attendees and purpose |

**Not deductible or not claimed**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PRIVAT, DAGLIGVARER, KIWI, REMA, COOP | Not deductible | Personal living costs |
| BOT, FORELEGG, GEBYR (penalty) | Not deductible where mainly penal | A tvangsmulkt or a late or parking-lot charge is tested separately: see Expenses. A bank fee is not a fine |
| SKATT, FORSKUDDSSKATT, RESTSKATT | Not claimed | Income tax. Conservative default: the direct authority is held (see Expenses). Track prepayments as credits |
| TRYGDEAVGIFT | Not claimed | Conservative default: the direct authority is held (see Expenses) |
| PRIVATUTTAK | Not deductible | Drawings |
| UTDANNING NY PROFESJON | Not deductible | Education for a new profession |

**Capital items**

| Pattern | Group | Maximum rate | Notes |
| --- | --- | --- | --- |
| KONTORMASKIN, PC, LAPTOP, SKRIVER | a | 30% | Declining balance pool. Under NOK 30,000: client may deduct |
| BIL, PERSONBIL (business) | d | 20% | Yrkesbil only |
| VAREBIL, LASTEBIL | c | 24% | |
| INVENTAR, MOBLER | d | 20% | |
| BYGNING (commercial) | i | 2% | Commercial buildings |
| BYGNING (hotel, lodging, eating place, other structures) | h | 4% | The prior version's 'industrial' label is replaced by the Act's words |
| Low value, cost under NOK 30,000 | None | 100% or group rate | Deduct or depreciate, if the asset loses value |
| Short life, under 3 years | None | 100%, or spread over the life | Spreading needs a cost of NOK 30,000 or more |

**Exclusions and tracking**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERN OVERF., EGNE KONTI | Exclude | Own-account transfer |
| LAN, AVDRAG, NEDBETALING | Exclude | Loan principal |
| RENTER LAN (business) | Deductible | Business loan interest; see Beregnet personinntekt for add-back |
| MVA BETALING | Exclude from the profit and loss | MVA liability |
| FORSKUDDSSKATT | Track separately | Preliminary tax credit, when evidenced |

### Bank formats

Carried from the prior version and untested. Field names follow that version's Section 8.

| Bank | Format | Key fields | Notes |
| --- | --- | --- | --- |
| DNB | CSV, PDF | Dato, Forklaring or Tekst, Inn, Ut, Saldo | Most common; DNB Nettbank CSV export |
| Nordea NO | CSV, PDF | Bokføringsdato, Tekst, Beløp | |
| SpareBank 1 | CSV, PDF | Dato, Beskrivelse, Beløp | Regional banks (SR-Bank, SMN and others) |
| Handelsbanken NO | CSV, PDF | Datum, Text, Belopp | Swedish parent format |
| Sbanken | CSV | Dato, Tekst, Beløp | Clean CSV export |
| Revolut, Wise | CSV | Date, Counterparty, Amount | Multi-currency; a foreign-currency line is Needs Input |

| Term | English | Hint |
| --- | --- | --- |
| Innbetaling | Deposit or credit | Potential income |
| Utbetaling | Withdrawal or debit | Potential expense |
| Overføring | Transfer | Check direction |
| AvtaleGiro | Direct debit | Regular expense |
| Varekjøp / Kort | Card purchase | Expense |
| Kontantuttak | Cash withdrawal | Ask purpose |
| Gebyr | Fee or charge | Bank charge |
| Nettgiro | Online payment | Expense |

### Currency and rounding

Compute in NOK. Foreign amounts are Needs Input because the conversion rule was not read. Tax and contribution claims are rounded down to the nearest whole krone (skattebetalingsforskriften § 10-4-4), and interest likewise (§ 11-7-1). Examples show øre so the arithmetic can be checked. The whole-krone restskatt in Examples 1 and 2 is illustrative only: § 10-4-4 speaks of calculating claims, and no text read applies it to the net balance after credits. Example 3 stops at øre, because no text read rounds a refund. Which amount § 10-4-4 rounds, and whether it reaches a refund, is held.

### Excel working paper

```text
NORWAY INCOME TAX -- WORKING PAPER (estimated, not reviewed)
Income year: 2025 or 2026 (one year only)
Client: ___________________________
Business form: Enkeltpersonforetak (confirmed: yes / no)

A. DRIFTSINNTEKTER (net of MVA where registered)
  A1. Omsetning                                    ___________
  A2. Andre inntekter                              ___________
  A3. Total                                        ___________

B. DRIFTSKOSTNADER
  B1. Lokalekostnader                              ___________
  B2. Forsikring                                   ___________
  B3. Revisor / regnskapsfører                     ___________
  B4. IT / software                                ___________
  B5. Markedsføring                                ___________
  B6. Reisekostnader                               ___________
  B7. Bilkostnader (yrkesbil actual, or km rate)   ___________
  B8. Representasjon (per person limit for year)   ___________
  B9. Avskrivninger (saldogrupper)                 ___________
  B10. Bankkostnader                               ___________
  B11. Øvrige kostnader                            ___________
  B12. Total                                       ___________

C. NÆRINGSINNTEKT (A3 - B12)                       ___________

D. ALMINNELIG INNTEKT
  D1. Næringsinntekt (C)                           ___________
  D2. Wages and pension less minstefradrag         ___________
  D3. Other income less other deductions           ___________
  D4. Less underskudd brought forward              ___________
  D5. Less personfradrag for the year              ___________
  D6. Less Finnmark deduction, if any              ___________
  D7. Tax base (not below 0)                       ___________
  D8. D7 x 22% (or 18.5% where it applies)         ___________

E. PERSONINNTEKT
  E1. Næringsinntekt (C)                           ___________
  E2. Add capital costs and losses                 ___________
  E3. Add §§ 6-60, 6-61 and special deductions     ___________
  E4. Less capital income and gains                ___________
  E5. Less skjermingsfradrag                       ___________
  E6. Less negative personinntekt brought forward  ___________
  E7. Beregnet personinntekt                       ___________
  E8. Wages                                        ___________
  E9. Pension                                      ___________

F. TAX COMPUTATION
  F1. Trinnskatt (on E7, floor 0, + E8 + E9)       ___________
  F2. Trygdeavgift (type rates, floor, 25% cap)    ___________
  F3. Total tax (D8 + F1 + F2)                     ___________
  F4. Less forskuddstrekk                          ___________
  F5. Less forskuddsskatt paid                     ___________
  F6. Restskatt / tilgode                          ___________

G. NÆRINGSSPESIFIKASJON EXEMPTION TESTED?          Yes / No

REVIEWER FLAGS:
  [ ] Business form confirmed?
  [ ] Income year matches every figure used?
  [ ] Minstefradrag not applied to næringsinntekt?
  [ ] Trinnskatt on personinntekt (not alminnelig)?
  [ ] Trygdeavgift at the business rate for the year (not the wage rate, unless own-home childcare)?
  [ ] Vehicle status (yrkesbil or private car) confirmed?
  [ ] Home office arrangement confirmed?
  [ ] Items of NOK 30,000 or more on saldo?
  [ ] Loss carry-forward applied in both bases?
```

## Deadlines and filing

| Item | Date or rule | Source and standing |
| --- | --- | --- |
| Skattemelding, owner of enkeltpersonforetak | End of May after the income year: 31 May. The prior version's 30 April is wrong for this client | Skatteforvaltningsforskriften § 8-2-3(1)(a); Skatteetaten. Enacted. 31 May 2026 was a Sunday. Skatteetaten's page says that where the date to file and to apply for an extension falls on a Saturday or Sunday, it is not too late if you apply by the first working day (Practice). That wording ends on applying, and no statute or regulation read moves the filing date itself: held |
| Other persons | End of April | § 8-2-3(1)(b). Enacted |
| Spouses with different deadlines | May use the later one | § 8-2-3(2). Enacted |
| Extension | On application to the tax office, for special reasons causing significant difficulty, or to an accountant or auditor for a smaller share of named clients; not beyond 30 June. Skattedirektoratet may extend the date by up to 1 month for groups of taxpayers; no such decision was read. No application after the deadline has passed | § 8-2-5(1) and (2); Skatteetaten. Enacted and Practice |
| Filing route | Electronic | § 8-1-2(2), § 8-2-8. Enacted |
| Forskuddsskatt | 15 March, 15 June, 15 September, 15 December of the income year, in equal terms. Under NOK 2,000: all at 15 June. Earliest 3 weeks after notice. An unpaid term brings later terms forward. A payment date on a Saturday, Sunday or public holiday moves to the nearest working day | Skattebetalingsloven §§ 10-2 and 10-20. Enacted |
| Restskatt | 3 weeks after notice of the settlement, earliest 20 August. At NOK 1,000 or more, 2 equal terms, the second 5 weeks later | Skattebetalingsloven § 10-21. Enacted |
| Avoiding rentetillegg | Pay restskatt by 31 May in the year after the income year, as tilleggsforskudd. If the 31st is a weekend or public holiday, the date is the first working day after | Skattebetalingsloven § 11-5(1). Enacted. Weekend rule: Skatteetaten's tilleggsforskudd page. Practice |
| Records | 5 years for items under bokføringsloven § 13 nr. 1 to 4; 3 years 6 months for nr. 5 to 8. Changes by lov 19 June 2026 nr. 39 start on 1 January 2027 and are not applied here. The prior version's 'digital' was not checked against bokføringsforskriften and is held | Bokføringsloven § 13. Enacted |

**Næringsspesifikasjon.** RF-1175 Næringsoppgave 1 has been out of use since income year 2023. The information now goes in the skattemelding or the næringsspesifikasjon (Skatteetaten's RF-1175 page). The legacy threshold is replaced by an exemption: a person who runs a business with total operating income of NOK 50,000 or less need not file a næringsspesifikasjon (skatteforvaltningsforskriften § 8-2-1(1)(c)). The exemption does not apply to:

1. a company taxable under skatteloven § 2-2(1);
2. a company under § 2-2(2);
3. a taxpayer under § 2-3, § 14-81 or § 14-82;
4. a person splitting business income with a spouse under § 2-11;
5. a person who ran more than 1 business in the year, or a business taxable to more than 1 municipality;
6. a person who must file the 'Drosje og godstransportnæringen' message;
7. a person who must file the 'Utleie mv. av fast eiendom' message with the 'Avskrivning' message, for business and the let property;
8. a person with accounting duty under regnskapsloven § 1-2;
9. a person who is liable to register for MVA under merverdiavgiftsloven § 2-1;
10. a person taxable under the Svalbard tax Act.

An exempt person must still document transactions and keep records under the rules in § 8-2-1(3). Skatteetaten offers a simplified næringsspesifikasjon where operating income is under NOK 50,000. A person with accounting duty or audit duty must file the næringsspesifikasjon through an accounting or year-end system (Skatteetaten). A return is due even if there was no business activity in the year, and private and business items stay apart: a yrkesbil and assets costing over NOK 30,000 go in the næringsspesifikasjon.

**Forskuddsskatt.** It is set at the expected tax and trygdeavgift, less expected forskuddstrekk (skattebetalingsloven § 6-3). It may be changed when a restskatt or refund of at least one fifth of the amount is overwhelmingly likely (§ 6-3(5)), and is normally set by estimate for a person not previously assessed (§ 6-4(1)). The client registers expected profit in the skattekort on skatteetaten.no and may change it during the year. Skatteetaten sends the invoice about 3 weeks before each date: through eFaktura, or otherwise to the Altinn inbox.

A new self-employed person should estimate the profit and register it. The prior version said the authority sets NOK 0 where nothing is registered: no text read supports that, and it named the wrong authority. Late payment and rentetillegg still follow the rules here.

## Penalties and interest

| Item | Detail | Source and standing |
| --- | --- | --- |
| Tvangsmulkt, late filing | Half a rettsgebyr per day, cap 50 rettsgebyr. Special cases lower, or higher up to 3 rettsgebyr per day | Skatteforvaltningsloven § 14-1; forskrift § 14-1-1. Enacted |
| Rettsgebyr | NOK 1,314 from 1 January 2025; NOK 1,345 from 1 January 2026 | FOR-2024-12-20-3388; rettsgebyrforskriften § 2-1. Enacted |
| Tvangsmulkt in NOK | At the 2025 rettsgebyr: NOK 657 per day, cap NOK 65,700. At the 2026 rettsgebyr: NOK 672.50 per day, cap NOK 67,250. Which year's rettsgebyr applies to a given default was not read: held | Calculated from the 2 rows above |
| Tilleggsskatt | 20% of the tax advantage, or 10% where the data was also given by an employer or other third party under chapter 7 or by a company under § 8-9 | Skatteforvaltningsloven §§ 14-3 and 14-5. Enacted |
| Not imposed | Conduct is excusable (§ 14-3(2)); correct and complete pre-filled data; obvious calculation or writing errors; the seller's MVA case in § 14-4 c; voluntary correction not prompted by a control or third-party data; tilleggsskatt under NOK 1,000 for the matter; death | §§ 14-3(2) and 14-4. Enacted |
| Offset | Tvangsmulkt under § 14-1 comes off tilleggsskatt for non-delivery | § 14-5(5). Enacted |
| Timing errors | Tilleggsskatt is computed on the net benefit of the deferral | § 14-5(4). Enacted |
| Skjerpet tilleggsskatt | A further 20% or 40% of the tax evaded, for intent or gross negligence, and only in addition to tilleggsskatt. Arithmetically the totals are 40% or 60%, or 30% or 50% with a 10% base | §§ 14-5 and 14-6. Enacted |
| Prosecution | Skattesvik: fine or up to 2 years' prison. Grovt skattesvik: fine or up to 6 years | Straffeloven §§ 378 and 379. Enacted |
| Forsinkelsesrente | 12.5% from 1 January 2025; 12.25% from 1 July 2025; 12.00% from 1 January 2026; 12.25% from 1 July 2026 | Skattebetalingsloven §§ 11-1 and 11-6; FOR-2024-12-19-3279; FOR-2025-06-23-1321; FOR-2025-12-18-2658; FOR-2026-06-25-1372. Enacted |
| Rentetillegg | On restskatt, at Norges Bank's policy rate on 1 January less 22%, from 1 July in the income year until the first term falls due; none where paid by 31 May. The policy rate was not read, so the percentage is held | Skattebetalingsloven §§ 11-5(1) and 11-6(2). Enacted |
| Small amounts | Late-payment interest under NOK 50 is not charged | Skattebetalingsforskriften § 10-4-2. Enacted |

The prior version listed negligence at 20%, gross negligence at 40% and fraud at 60%. That is not how the Act is built: the ordinary rate has no separate negligence tier and the increase needs intent or gross negligence.

## Cross-border points

This file computes a full-year resident with Norwegian-source income. Everything else stops:

- Foreign income, a foreign permanent establishment, foreign tax paid or a treaty question: R-NO-2. Hand off to `cross-border-workflow-base` with a reviewer.
- Part-year residence, non-residence or dual residence: R-NO-5. For the reviewer's information, trinnskatt thresholds, personfradrag and the minstefradrag cap are reduced by whole or begun months of residence (skattevedtak § 3-1; skatteloven §§ 15-4(5) and 6-32(4)), and persons under § 2-3 have their own rules.
- Svalbard income: R-NO-7.
- Income received through a foreign platform or in foreign currency: flag it. It is Needs Input before classification.
- Costs abroad: a representation deduction applies to costs abroad too (FOR-1999-11-22-1160 § 6-21-1(4)).

## Two worked examples that recompute

These are invented fixtures. Each assumes a full-year resident who turns 17 to 69 in the income year, outside the Finnmark area, class 1, municipal and county rates at the maximum, and a confirmed profile. Each covers a client type in the base's slot 13. Results are estimated, not reviewed.

### Example 1: self-employed consultant, 2025

Income year 2025. An enkeltpersonforetak with a mean skjermingsgrunnlag of NOK 200,000 has næringsinntekt of NOK 660,000, no wages, no capital items and no losses. Forskuddsskatt paid was NOK 190,000 on Skatteetaten's statement. The client takes the maximum 2025 skjermingsrente of 4.6%.

```oa-check
name: NO 2025 self-employed, both bases, balance
inputs:
  naeringsinntekt: 660000
  shield_basis: 200000
  shield_rate: 0.046
  personfradrag: 108550
  forskuddsskatt: 190000
steps:
  - shield: max(shield_basis, 0) * shield_rate
  - personinntekt: naeringsinntekt - shield
  - general_tax: max(naeringsinntekt - personfradrag, 0) * 0.22
  - trinn_1: max(min(personinntekt, 306050) - 217400, 0) * 0.017
  - trinn_2: max(min(personinntekt, 697150) - 306050, 0) * 0.04
  - trinnskatt: trinn_1 + trinn_2
  - trygd_rate: personinntekt * 0.109
  - trygd_cap: max(personinntekt - 99650, 0) * 0.25
  - trygdeavgift: min(trygd_rate, trygd_cap)
  - total: general_tax + trinnskatt + trygdeavgift
  - balance: total - forskuddsskatt
  - illustrative_whole_krone: floor(balance)
expected:
  shield: 9200
  personinntekt: 650800
  general_tax: 121319
  trinnskatt: 15297.05
  trygdeavgift: 70937.20
  total: 207553.25
  balance: 17553.25
  illustrative_whole_krone: 17553
```

The 22% is on NOK 551,450, which is næringsinntekt less personfradrag. Trinnskatt and trygdeavgift are on NOK 650,800, which is næringsinntekt less the shield. Neither number replaces the other. Restskatt is NOK 17,553.25, or an illustrative NOK 17,553 if rounded down (see Currency and rounding). Paying it as tilleggsforskudd by 31 May 2026 or, as that was a Sunday, the first working day after avoids rentetillegg.

**Decision: deduct or depreciate.** Same client. Suppose the NOK 660,000 is before an office machine bought for NOK 25,000 with a 5 year life, and taken into use in the business in 2025. It is below NOK 30,000, so the client may deduct it or put it in group a. This is the client's election and the fixture does not make it.

```oa-check
name: NO 2025 under NOK 30,000 asset, deduct versus depreciate
inputs:
  profit_before_asset: 660000
  cost: 25000
  group_rate: 0.30
  shield_rate: 0.046
  base_shield: 9200
  personfradrag: 108550
steps:
  - profit_deduct: profit_before_asset - cost
  - person_deduct: profit_deduct - base_shield
  - tax_deduct: max(profit_deduct - personfradrag, 0) * 0.22 + (306050 - 217400) * 0.017 + (person_deduct - 306050) * 0.04 + person_deduct * 0.109
  - depreciation: cost * group_rate
  - closing_balance: cost - depreciation
  - extra_shield: closing_balance / 2 * shield_rate
  - profit_pool: profit_before_asset - depreciation
  - person_pool: profit_pool - base_shield - extra_shield
  - tax_pool: max(profit_pool - personfradrag, 0) * 0.22 + (306050 - 217400) * 0.017 + (person_pool - 306050) * 0.04 + person_pool * 0.109
  - first_year_gap: tax_pool - tax_deduct
expected:
  tax_deduct: 198328.25
  depreciation: 7500
  closing_balance: 17500
  extra_shield: 402.50
  tax_pool: 204725.78
  first_year_gap: 6397.53
```

The direct deduction costs NOK 198,328.25 of tax for 2025 against NOK 204,725.78 with the pool, so it is NOK 6,397.53 cheaper in year 1. The pool keeps NOK 17,500 for later years and adds a small shield, so the gap is mainly timing. The pool's extra shield rests on Skatte-ABC 2025 E-5-6.2.3, which keeps a pooled smaller asset in the basis. It assumes the machine really was taken into use in the business in 2025, because the asset must have worked there (skatteloven § 12-12(2) and Skatte-ABC 2025 E-5-6.2.10). A machine only delivered and put on saldo adds no shield. The figure also assumes the opening balance was 0 and uses the simple mean. The prior version's 18,000 and 25,000 laptop examples treated these assets as mandatory saldo items, which was wrong under the NOK 30,000 threshold.

### Example 2: wages and a sole trader, 2026

Income year 2026. A client has wages of NOK 400,000 and næringsinntekt of NOK 300,000. Beregnet personinntekt is NOK 300,000: the business has no assets or debt, so there is no shield, and the held 2026 skjermingsrente does not matter. The client was not drawn for the trial deduction. Forskuddstrekk on the wage certificate was NOK 100,000, and forskuddsskatt paid was NOK 70,000.

```oa-check
name: NO 2026 mixed wage and business income
inputs:
  wages: 400000
  business: 300000
  personfradrag: 114540
  forskuddstrekk: 100000
  forskuddsskatt: 70000
steps:
  - minstefradrag: min(wages * 0.46, 95700)
  - ordinary_income: wages - minstefradrag + business
  - general_tax: max(ordinary_income - personfradrag, 0) * 0.22
  - personinntekt: wages + business
  - trinn_1: max(min(personinntekt, 318300) - 226100, 0) * 0.017
  - trinn_2: max(min(personinntekt, 725050) - 318300, 0) * 0.04
  - trinnskatt: trinn_1 + trinn_2
  - trygd_rate: wages * 0.076 + business * 0.108
  - trygd_cap: max(personinntekt - 99650, 0) * 0.25
  - trygdeavgift: min(trygd_rate, trygd_cap)
  - total: general_tax + trinnskatt + trygdeavgift
  - balance: total - forskuddstrekk - forskuddsskatt
  - illustrative_whole_krone: floor(balance)
expected:
  minstefradrag: 95700
  ordinary_income: 604300
  general_tax: 107747.20
  trinnskatt: 16835.40
  trygdeavgift: 62800
  total: 187382.60
  balance: 17382.60
  illustrative_whole_krone: 17382
```

Minstefradrag is on the wages only. Trinnskatt is on all NOK 700,000 of personinntekt in one schedule, whilst trygdeavgift keeps each income type at its own rate. Restskatt is NOK 17,382.60, or an illustrative NOK 17,382 if rounded down (see Currency and rounding).

### Example 3: employee only, 2025

Income year 2025. An employee with wages of NOK 600,000 and no business, with forskuddstrekk of NOK 150,000 on the certificate.

```oa-check
name: NO 2025 employee only, refund
inputs:
  wages: 600000
  personfradrag: 108550
  forskuddstrekk: 150000
steps:
  - minstefradrag: min(wages * 0.46, 92000)
  - general_tax: max(wages - minstefradrag - personfradrag, 0) * 0.22
  - trinn_1: max(min(wages, 306050) - 217400, 0) * 0.017
  - trinn_2: max(min(wages, 697150) - 306050, 0) * 0.04
  - trinnskatt: trinn_1 + trinn_2
  - trygdeavgift: min(wages * 0.077, max(wages - 99650, 0) * 0.25)
  - total: general_tax + trinnskatt + trygdeavgift
  - refund: forskuddstrekk - total
expected:
  minstefradrag: 92000
  general_tax: 87879
  trinnskatt: 13265.05
  trygdeavgift: 46200
  total: 147344.05
  refund: 2655.95
```

### Fixtures and tests

```oa-check
name: NO trygdeavgift floor and cap, and loss in both bases
inputs:
  low_income: 120000
  floor_income: 99650
  mid_income: 200000
  current_year: 400000
  prior_loss: 150000
  prior_negative_personinntekt: 150000
steps:
  - at_floor: min(floor_income * 0.109, max(floor_income - 99650, 0) * 0.25)
  - low_rate_charge: low_income * 0.109
  - low_cap: max(low_income - 99650, 0) * 0.25
  - low_trygd: min(low_rate_charge, low_cap)
  - mid_trygd: min(mid_income * 0.109, max(mid_income - 99650, 0) * 0.25)
  - ordinary_base: max(current_year - prior_loss, 0)
  - personinntekt_no_negative: current_year
  - personinntekt_with_negative: max(current_year - prior_negative_personinntekt, 0)
expected:
  at_floor: 0
  low_trygd: 5087.50
  mid_trygd: 21800
  ordinary_base: 250000
  personinntekt_no_negative: 400000
  personinntekt_with_negative: 250000
```

```oa-check
name: NO gain and loss account at NOK 20,000, and a pooled asset used or unused
inputs:
  gain_balance: 20000
  loss_balance: 20000
  larger_balance: 30000
  limit: 30000
  annual_share: 0.20
  closing_balance: 17500
  shield_rate: 0.046
  used: 1
  unused: 0
steps:
  - gain_under_limit: 1 - min(floor(gain_balance / limit), 1)
  - gain_minimum_income: gain_balance * (gain_under_limit + (1 - gain_under_limit) * annual_share)
  - loss_under_limit: 1 - min(floor(loss_balance / limit), 1)
  - loss_maximum_deduction: loss_balance * (loss_under_limit + (1 - loss_under_limit) * annual_share)
  - loss_without_full_deduction: loss_balance * annual_share
  - larger_under_limit: 1 - min(floor(larger_balance / limit), 1)
  - larger_minimum_income: larger_balance * (larger_under_limit + (1 - larger_under_limit) * annual_share)
  - extra_shield_used: used * closing_balance / 2 * shield_rate
  - extra_shield_unused: unused * closing_balance / 2 * shield_rate
expected:
  gain_minimum_income: 20000
  loss_maximum_deduction: 20000
  loss_without_full_deduction: 4000
  larger_minimum_income: 6000
  extra_shield_used: 402.50
  extra_shield_unused: 0
```

| Fixture | Expected result |
| --- | --- |
| Payment 15/03/2025 ; DNB Innbetaling ; DESIGN STUDIO AS ; Faktura 2025-003 ; +125,000.00 ; NOK | Check the invoice. Registered client, invoice at 25%: driftsinntekt NOK 100,000, MVA NOK 25,000 excluded. Not registered: driftsinntekt NOK 125,000. Invoice not seen: Needs Input |
| Card 22/04/2025 ; SpareBank 1 Kort ; RESTAURANT MAAEMO ; Kundelunsj ; -2,500.00 ; NOK, 4 persons | NOK 625 per person is above NOK 579, so the whole NOK 2,500 is non-deductible. The prior version's NOK 2,236 was wrong. Headcount unknown: no deduction |
| Card 03/06/2025 ; DNB Kort ; ELKJOP ; LAPTOP ; -18,000.00 ; NOK | Under NOK 30,000: deduct NOK 18,000, or if the client chooses, group a at 30%, NOK 5,400 |
| Card 15/05/2025 ; Nordea Kort ; CLAS OHLSON ; KONTORSTOL ; -4,500.00 ; NOK | Driftskostnad, deductible in full if the client does not choose depreciation |
| Client claims minstefradrag of NOK 104,450 on næringsinntekt of NOK 500,000 | Reject. It does not apply to næringsinntekt outside § 6-31(1)(d). The figure is also not the cap for either year |
| Næringsinntekt NOK 600,000, 2025, no shield | Tax on alminnelig NOK 108,119.00 on (600,000 − 108,550) × 22%. Trinnskatt NOK 13,265.05, spanning trinn 1 and 2. Trygdeavgift NOK 65,400.00 at 10.9% |
| Næringsinntekt NOK 1,200,000, 2025, no shield | Trinnskatt NOK 93,769.50, through trinn 4 |
| Næringsinntekt NOK 200,000, 2025 | No trinnskatt. Alminnelig tax and trygdeavgift only |
| Laptop NOK 25,000, client chooses the pool | Group a, 30%, NOK 7,500. Without that choice, deduct NOK 25,000 |
| Gain and loss account, gain balance NOK 20,000 | Under NOK 30,000, so all NOK 20,000 goes to income. At NOK 30,000, at least NOK 6,000 |
| Gain and loss account, loss balance NOK 20,000 | Under NOK 30,000, so the client may deduct all NOK 20,000. Otherwise up to NOK 4,000 |
| Private car, 4,000 km of documented business driving | 2025: NOK 14,000. 2026: Needs Input, with no rate assumed |
| Group a machine delivered and put on saldo in 2025, with a closing balance of NOK 17,500 | Taken into use in the business: extra shield NOK 402.50. Not taken into use: NOK 0 |

## Ask the client first

Ask these as one message before classifying a line, and do not ask what the documents already answer.

1. **Form, residence and year.** Is the business an enkeltpersonforetak? Were you tax resident in Norway all year, and in which municipality? Which income year? What is your year of birth? Is any spouse working in or part-owner of the business? Any foreign income, platform or tax?
2. **Income and revenue.** What is gross revenue (to test the NOK 50,000 næringsspesifikasjon exemption)? Are you registered for MVA, and from when? Do you also have employment, capital or rental income? For 2026, were you notified of the trial deduction?
3. **Home office, vehicle, phone and internet.** Is the room dedicated or shared, and do you own or rent? Standard deduction or actual costs? How many business km on which car, and is there a logbook? What is the business use of phone and internet?
4. **Assets and balance sheet.** Were capital assets bought or sold in the year, with cost, type and life, and was each one bought taken into use in the business? For any item under NOK 30,000, do you want to deduct or depreciate? Do you have opening and closing values for the skjermingsgrunnlag, and which skjermingsrente do you want?
5. **Payments and losses.** What forskuddsskatt did you pay by term? Is there a certificate for forskuddstrekk? What underskudd and negative personinntekt carry in from earlier years?
6. **Prior return.** Is the prior year skattemelding and næringsspesifikasjon available?

### Completion checks

- The label on every figure matches the single income year computed.
- The 2 bases reconcile separately to the working paper.
- Every refusal was tested before any line was classified.
- The Finnmark area test, municipal and county rates, and class were confirmed.
- All 12 checks in `income-tax-workflow-base` Section 5 pass, and the reviewer brief lists each Tier 2 and Tier 3 item.

## Sources

Legal text was read from Lovdata's public data bundles. The Skatte-ABC 2025 rows are one Skatteetaten handbook, read on section pages. Each links the first section page of its chapter, and the other pages it names sit under the same chapter path. Each row states what was read. The budget for 2027 was not read, and no figure in this file comes from it.

| Source | URL | Read on | What was read |
| --- | --- | --- | --- |
| Skatteloven (LOV-1999-03-26-14) | https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 | 2026-11-05 | Member nl/nl-19990326-014.xml, current text, in part: §§ 2-1, 2-10, 2-11, 6-1, 6-3, 6-12, 6-14, 6-15, 6-18 to 6-21, 6-31, 6-32, 6-51, 6-86, 12-1, 12-2, 12-10 to 12-13, 14-1, 14-2, 14-6, 14-7, 14-40 to 14-47, 15-2 to 15-5 |
| Skatteforvaltningsloven (LOV-2016-05-27-14) | https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 | 2026-11-05 | Member nl/nl-20160527-014.xml, in part: §§ 8-1, 8-2, 14-1, 14-3 to 14-6 |
| Skattebetalingsloven (LOV-2005-06-17-67) | https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 | 2026-11-05 | Member nl/nl-20050617-067.xml, in part: §§ 6-1, 6-3, 6-4, 10-2, 10-20, 10-21, 11-1, 11-5, 11-6 |
| Folketrygdloven (LOV-1997-02-28-19) | https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 | 2026-11-05 | Member nl/nl-19970228-019.xml, in part: §§ 23-3 and 23-5 |
| Bokføringsloven (LOV-2004-11-19-73) and lov 19 June 2026 nr. 39 | https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 | 2026-11-05 | Members nl/nl-20041119-073.xml and nl/nl-20260619-039.xml, in part: §§ 13 and 13 b, and the commencement of the amendment |
| Merverdiavgiftsloven (LOV-2009-06-19-58) | https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 | 2026-11-05 | Member nl/nl-20090619-058.xml, in part: § 2-1 |
| Straffeloven (LOV-2005-05-20-28) | https://api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2 | 2026-11-05 | Member nl/nl-20050520-028.xml, in part: §§ 378 and 379 |
| Stortingets skattevedtak 2025 (FOR-2024-12-13-3203) | https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 | 2026-11-05 | Member stv/sf-20241213-3203.xml, in part: §§ 3-1, 3-2, 3-8 and 6-1 to 6-5, consolidated to the 18 December 2025 amendment |
| Stortingets skattevedtak 2026 (FOR-2025-12-18-2747) | https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 | 2026-11-05 | Member stv/sf-20251218-2747.xml, in part: §§ 3-1, 3-2, 3-8 and 6-1 to 6-6, consolidated to the 19 June 2026 amendment |
| Folketrygd resolution 2025 (FOR-2024-12-13-3204) | https://api.lovdata.no/v1/publicData/get/lovtidend-avd1-2001-2025.tar.bz2 | 2026-11-05 | Member lti/2024/sf-20241213-3204.xml, as gazetted: §§ 6 to 8. No consolidated copy, and Lovtidend 2025 lists no amending decision by title |
| Folketrygd resolution 2026 (FOR-2025-12-18-2748) | https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 | 2026-11-05 | Member stv/sf-20251218-2748.xml, in part: the trygdeavgift rates. The amendment of 2026 nr. 1244 concerns the employer section |
| Satsforskrift 2025 (FOR-2024-11-27-2889) | https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 | 2026-11-05 | Member sf/sf-20241127-2889.xml, in part: §§ 4, 10 and 14 |
| Satsforskrift 2026 (FOR-2025-11-07-2216) | https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 | 2026-11-05 | Member sf/sf-20251107-2216.xml, in part: §§ 4, 10 and 14 |
| Skatteforvaltningsforskriften (FOR-2016-11-23-1360) | https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 | 2026-11-05 | Member sf/sf-20161123-1360.xml, in part: §§ 8-1-2, 8-2-1, 8-2-3, 8-2-5, 8-2-8 and 14-1-1 |
| Skattebetalingsforskriften (FOR-2007-12-21-1766) | https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 | 2026-11-05 | Member sf/sf-20071221-1766.xml, in part: §§ 10-4-2, 10-4-4 and 11-7-1 |
| FSFIN (FOR-1999-11-19-1158) | https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 | 2026-11-05 | Member sf/sf-19991119-1158.xml, in part: §§ 5-12-20, 5-12-21, 10-12-1, 12-12-1 to 12-12-10 and 12-20-1 |
| Takseringsregler 2025 (FOR-2025-12-01-2404) | https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 | 2026-11-05 | Member sf/sf-20251201-2404.xml, in part: §§ 1-3-20 to 1-3-26 |
| Skattedirektoratets forskrift (FOR-1999-11-22-1160) | https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 | 2026-11-05 | Member sf/sf-19991122-1160.xml, in part: §§ 6-21-1 to 6-21-7 |
| Rettsgebyrforskriften (FOR-1983-02-15-86) | https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 | 2026-11-05 | Member sf/sf-19830215-0086.xml: § 2-1 for 2026 |
| Forsinkelsesrente regulation 2026 (FOR-2026-06-25-1372) | https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 | 2026-11-05 | Member sf/sf-20260625-1372.xml: § 1 |
| Stortingsvedtak om merverdiavgift 2026 (FOR-2025-12-18-2752) | https://api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2 | 2026-11-05 | Member stv/sf-20251218-2752.xml, in part: §§ 2 to 5 |
| Rettsgebyr 2025 (FOR-2024-12-20-3388) | https://api.lovdata.no/v1/publicData/get/lovtidend-avd1-2001-2025.tar.bz2 | 2026-11-05 | Member lti/2024/sf-20241220-3388.xml: the amendment of § 2-1 |
| Forsinkelsesrente regulations (FOR-2024-12-19-3279, FOR-2025-06-23-1321, FOR-2025-12-18-2658) | https://api.lovdata.no/v1/publicData/get/lovtidend-avd1-2001-2025.tar.bz2 | 2026-11-05 | The 3 members under lti/2024 and lti/2025: rate paragraph and commencement of each |
| Stortingsvedtak om merverdiavgift 2025 (FOR-2024-12-13-3208) | https://api.lovdata.no/v1/publicData/get/lovtidend-avd1-2001-2025.tar.bz2 | 2026-11-05 | Member lti/2024/sf-20241213-3208.xml, in part: §§ 2 to 5 |
| Skattevedtak amendment 2026 (FOR-2026-06-19-1243) | https://api.lovdata.no/v1/publicData/get/lovtidend-avd1-2026.tar.bz2 | 2026-11-05 | Member lti/2026/sf-20260619-1243.xml, in full: § 6-5 only |
| Skatteetaten rate page, trinnskatt | https://www.skatteetaten.no/satser/trinnskatt/ | 2026-11-05 | 2026 view, in full |
| Skatteetaten rate page, trygdeavgift | https://www.skatteetaten.no/satser/trygdeavgift/ | 2026-11-05 | 2026 view, in full |
| Skatteetaten rate page, personfradrag | https://www.skatteetaten.no/satser/personfradrag/ | 2026-11-05 | Latest-year view, in full |
| Skatteetaten rate page, minstefradrag | https://www.skatteetaten.no/satser/minstefradrag/ | 2026-11-05 | 2026 view, in full |
| Skatteetaten rate page, forsinkelsesrenter | https://www.skatteetaten.no/satser/forsinkelsesrenter/ | 2026-11-05 | 2026 view: § 11-1 rates only |
| Skatteetaten rate page, skjermingsrente | https://www.skatteetaten.no/en/rates/risk-free-interest-rate-for-shares-and-sole-proprietorships/ | 2026-11-05 | 2025 view, in full: the rate for an enkeltpersonforetak |
| Skatteetaten rate page, home office | https://www.skatteetaten.no/en/rates/home-office-standard-deduction/ | 2026-11-05 | 2026 view, part relied on: the amount and § 1-3-26 |
| Skatteetaten, return for an enkeltpersonforetak | https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/skattemelding-naringsdrivende/enk/ | 2026-11-05 | The page, in full: filing route, deadline, weekend notice, simplified specification, no activity case |
| Skatteetaten, return for business hub | https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/skattemelding-naringsdrivende/ | 2026-11-05 | Hub page: deadline and extension wording |
| Skatteetaten, RF-1175 page | https://www.skatteetaten.no/skjema/naringsoppgave-1/ | 2026-11-05 | The page, in full: form out of use from income year 2023 |
| Skatteetaten, forskuddsskatt for an enkeltpersonforetak | https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/forskuddsskatt/forskuddsskatt-for-enkeltpersonforetak/ | 2026-11-05 | The page, in full: registering profit, invoice timing, Altinn inbox |
| Skatteetaten, tilleggsforskudd | https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/forskuddsskatt/tilleggsforskudd/ | 2026-11-05 | The page, in full: 31 May payment and weekend rule |
| Skatteetaten, personinntekt in an enkeltpersonforetak | https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/income-in-business/personinntekt-i-enkeltpersonforetak | 2026-11-05 | The page, in full, as a summary behind § 12-11 |
| Skatte-ABC 2025, B-5 | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/b-5-bil--fradrag-for-bilkostnader/B-5.001/ | 2026-11-05 | Section pages B-5-1 to B-5-4 |
| Skatte-ABC 2025, B-14 | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/b-14-bolig--hjemmekontor-mv/B-14.001/ | 2026-11-05 | Section pages B-14-1 to B-14-3.2 |
| Skatte-ABC 2025, B-21 | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/b-21-bot-gebyr-mv/B-21.001/ | 2026-11-05 | All section pages |
| Skatte-ABC 2025, D-3 | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/d-3-driftsmiddel--direkte-fradragsforing/D-3.001/ | 2026-11-05 | Section pages D-3-1 and D-3-2 |
| Skatte-ABC 2025, E-3 | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/e-3-elektronisk-kommunikasjon-telefon-mv/E-3.001/ | 2026-11-05 | Section pages E-3-1.7 and E-3-2.1 to E-3-2.3 |
| Skatte-ABC 2025, E-5 | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/e-5-enkeltpersonforetak--beregnet-personinntekt-foretaksmodellen/E-5.001/ | 2026-11-05 | Section pages E-5-1, E-5-2, E-5-4.2, E-5-4.8, E-5-5.5, E-5-6.1, E-5-6.2, E-5-6.7, E-5-7.2 and E-5-8 |
| Skatte-ABC 2025, K-3 | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/k-3-kontingenter/K-3.001/ | 2026-11-05 | Searched, in part: K-3-5.2.1 read |
| Skatte-ABC 2025, K-4 | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/k-4-kostnader--allment-om-fradrag/K-4.001/ | 2026-11-05 | Searched, in part: K-4-5.2.1 read |
| Skatte-ABC 2025, M-6 | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/m-6-minstefradrag/M-6.001/ | 2026-11-05 | Searched, in part: no statement in this file rests on it |
| Skatte-ABC 2025, P-11 | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/p-11-personfradrag/P-11.001/ | 2026-11-05 | Searched, in part: no statement in this file rests on it |
| Skatte-ABC 2025, P-16 | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/p-16-personinntekt--trygdeavgiftpensjonspoengpensjonsbeholdning/P-16.001/ | 2026-11-05 | Searched, in part: P-16-4.2.2 and P-16-4.3 read |
| Skatte-ABC 2025, R-13 | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/r-13-representasjon/R-13.001/ | 2026-11-05 | Section pages R-13-1 to R-13-5, in part: no statement in this file rests on it |
| Skatte-ABC 2025, T-12 | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/t-12-tiltakssonen-i-finnmark-og-nord-troms/T-12.001/ | 2026-11-05 | Section T-12-1 |
| Skatte-ABC 2025, U-2 | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/u-2-underskudd/U-2.001/ | 2026-11-05 | Section pages U-2-1, U-2-4.7, U-2-5.1 and U-2-6 |
| Skatte-ABC 2025, U-3 | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/u-3-utdanning--tilskudd-og-kostnader/U-3.001/ | 2026-11-05 | Section pages U-3-1 to U-3-3 |

Not yet confirmed: (1) the January 2027 announcement by Skattedirektoratet of the maximum skjermingsrente for 2026; (2) the 2026 deduction rates for a private car, because takseringsregler for 2026 were not found in the data read; (3) the rule for converting foreign currency; (4) a text stating that income tax and trygdeavgift are not deductible; (5) the 2025 amount in skatteloven § 6-19(2), where Skatte-ABC 2025 prints NOK 8,250 and the section was amended with effect from income years 2025 and 2026; (6) the rate adopted by the client's municipality and county in each year; (7) whether the skattemelding date itself moves when it falls on a weekend, since Skatteetaten's notice ends on applying ('søker') and no statute or regulation read moves 31 May 2026, a Sunday; (8) which year's rettsgebyr applies to a given late filing default; (9) the deductibility of insurance for the person and of trips with a mixed purpose, because the Skatte-ABC chapters F-25 and S-21 were not read; (10) Norges Bank's policy rate on 1 January, which sets rentetillegg; (11) the start date of lov 19 June 2026 nr. 48 on § 14-6; (12) the 'digital' condition on records in the prior version; (13) bank patterns and formats, which are untested; (14) how § 6-19(3) fits with the NOK amount in § 6-19(2) for a trader with few or no wages; (15) which amount skattebetalingsforskriften § 10-4-4 rounds, and whether it reaches a refund.

### Source conflicts

| Target | Conflict | Status |
| --- | --- | --- |
| `no-tax-overview` | States the personal return is due 30 April, which is the date for persons without a business, and uses 7.9% national insurance in its top marginal rate, against 7.7% for 2025 and 7.6% for 2026 on wages | Reported, not edited |
| `no-social-contributions` | Agrees on the 10.9% and 10.8%, the NOK 99,650, 31 May and the low rate from age 70. Its 'Fishing / hunting / childminding' row at the middle rate omits the limits in folketrygdloven § 23-3(2) nr. 2: a child in the carer's own home, under 12 or with special care needs, and a trade paying product levy under § 23-5 | Reported, not edited |
| Skatte-ABC 2025 | Prints some amounts from an earlier year: home office NOK 2,128 and trade body dues NOK 8,250. This file uses the year's instrument | Handled per row |
| Skatteetaten personinntekt page | Shows business interest as a deduction line, where § 12-11(2)(a) adds capital costs back. E-5-5.5 resolves it: qualifying interest is not added back, other interest is | Resolved on Skatte-ABC 2025 |

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.2 | November 2026 | Converted to the reference template; income years 2025 and 2026 separated; filing date corrected to 31 May; RF-1175 replaced by the næringsspesifikasjon rules; asset threshold corrected to NOK 30,000; representation, minstefradrag, tvangsmulkt, tilleggsskatt and group g corrected; personinntekt, skjermingsfradrag and negative personinntekt rules added |
| 2.1 | November 2026 | Prior version |

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-05. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `no-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/no-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
