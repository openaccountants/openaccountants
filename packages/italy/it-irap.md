---
name: it-irap
description: Use this skill whenever asked about Italian IRAP (Imposta Regionale sulle Attività Produttive) for self-employed professionals. Trigger on phrases like "IRAP", "imposta regionale", "IRAP professionista", "IRAP autonomo", "valore della produzione", "regional production tax Italy", or any question about IRAP obligations for a self-employed client in Italy. Covers the standard 3.9% rate, valore della produzione netta, regional variations, and the landmark exemption for autonomous professionals without autonomous organisation. ALWAYS read this skill before touching any Italy IRAP work.
jurisdiction: IT
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Italian regional tax on productive activities (IRAP)

How IRAP (imposta regionale sulle attività produttive) works in Italy: who still pays it, who has been taken out, how the taxable base (valore della produzione netta) is worked out for each type of taxpayer, the standard and special rates, the regional variations, the deductions for employment costs, the return and the payments on account (acconti). Figures are for tax year 2026. Italy's tax year is the calendar year. Rates, deductions and payment rules come from the Agenzia delle Entrate instructions to the IRAP return filed in 2026, which covers tax year 2025; they are used here for 2026, with the 2026 surcharges in Step 2. The instructions for tax year 2026 are not yet published, so these rules are assumed unchanged for 2026 until they are. Statute text was read on Normattiva as in force on 30 June 2026.

**The big change since 2022.** Individuals who run a business (persone fisiche esercenti attività commerciali) and individuals who work as professionals (esercenti arti e professioni) do not owe IRAP from the tax year in progress when Law 234/2021 came into force, that is from 2022 (Law 234/2021, art. 1, comma 8, printed as note 70 to art. 3 of D.Lgs. 446/1997: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art3!vig=2026-06-30). A sole trader, a freelance professional and a forfettario are all individuals, so none of them pays IRAP for 2026. IRAP now falls on partnerships, professional associations, companies, other entities and public bodies.

## Guide Metadata

| Field | Value |
| --- | --- |
| Jurisdiction | Italy |
| Jurisdiction Code | IT |
| Primary Legislation | D.Lgs. 15 dicembre 1997, n. 446 (IRAP decree) |
| Supporting Legislation | Law 234/2021 art. 1 comma 8 (individuals taken out); D.L. 73/2022 art. 10 (deductions); Law 199/2025 art. 1 comma 74 (banks and insurers); D.L. 21/2026 art. 3 (sector surcharge); D.L. 185/2008 art. 6 and D.L. 201/2011 art. 2 (IRAP deducted for income tax) |
| Tax Authority | Agenzia delle Entrate (return and collection); the regions receive the tax and may vary the rate |
| Contributor | Open Accountants |
| Validated By | Pending. Requires validation by an Italian commercialista |
| Validation Date | Pending |
| Tax Year | 2026 |

## Confidence Tier Definitions

- **[T1] Tier 1: Deterministic.** Apply exactly as written.
- **[T2] Tier 2: Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3: Out of Scope, Escalate.** Do not guess.

## Step 0: Client Onboarding Questions

Before computing, you MUST know:

1. **Legal form** [T1]. Individual (sole trader, professional, forfettario), partnership (s.n.c., s.a.s., società semplice), professional association (studio associato), company (s.r.l., s.p.a.), non-commercial entity or public body? Individuals stop here: no IRAP since 2022.
2. **Main activity and its ATECO code** [T1]. Some sectors pay a surcharge in 2026 and 2027 (Step 2).
3. **Region or regions of activity** [T1]. Each region may vary the rate; activity in several regions for at least three months means the base is split (EC5).
4. **Is it a bank, financial intermediary, insurer or concession holder?** [T1]. Special rates apply.
5. **Staff** [T1]. Permanent, fixed-term, seasonal, apprentices. It decides the employment deductions (Step 4.3).
6. **Last year's IRAP and last year's return** [T1]. They drive the acconti (Step 5).

**If the client is an individual (persona fisica) running a business or a profession, STOP. IRAP is not due for 2026.**

## Step 1: Who Is Subject to IRAP? [T1]

- **Legislation.** D.Lgs. 446/1997, art. 2 and 3: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art3!vig=2026-06-30

The tax falls on the habitual exercise, in the regions, of an autonomously organised activity. For companies and entities the activity is always taxable (2026 IRAP instructions, chapter 1).

### Subject to IRAP

**Subject to IRAP**

| Category | IRAP Applies? |
| --- | --- |
| Imprese individuali (individuals with a business) | **NO** since 2022 (Law 234/2021 art. 1 comma 8) |
| Lavoratori autonomi (individual professionals), with or without an organisation | **NO** since 2022 (same rule) |
| Regime forfettario taxpayers | **NO**. They are individuals, so the same rule takes them out |
| Contribuenti minimi | **NO**. Individuals |
| Società in nome collettivo, in accomandita semplice and those treated like them (art. 3(1)(b)) | YES |
| Società semplici and associations that practise arts and professions (studi associati) (art. 3(1)(c)) | YES |
| Companies and commercial entities (s.r.l., s.p.a., cooperatives) (art. 3(1)(a)) | YES, always |
| Non-commercial private entities (art. 3(1)(e)) and public bodies (art. 3(1)(e-bis)) | YES |
| Farming within art. 32 TUIR, farm cooperatives (art. 3(2)(c-bis)) | NO |
| Collective investment funds other than SICAVs, pension funds, EEIGs (GEIE) (art. 3(2)) | NO. An EEIG's value of production is attributed to its members |

### The "Autonomous Organisation" Test (Autonoma Organizzazione) [T1/T2]

- **Landmark case.** Corte di Cassazione, Sezioni Unite, sent. 9451/2016 held that an individual professional owed IRAP only if the work used an autonomous organisation (staff, significant capital goods). This case is not on an allowed official page and was not read for this Guide.

Since 2022 an individual does not owe IRAP whatever the organisation, so the test no longer decides 2026. It still matters for tax years up to 2021 (refund claims and open disputes) and it is argued for small partnerships and professional associations. Both are [T3]: refer.

**Autonomous Organisation Indicators (years before 2022 only)**

| Indicator | Points Toward IRAP Liability |
| --- | --- |
| Employs staff (dipendenti or collaboratori) | YES, strong indicator |
| Uses significant capital goods (beni strumentali) beyond minimal personal tools | YES |
| Has a dedicated office or studio | Weak indicator alone |
| Works purely with personal skills, no employees, minimal equipment | NO, likely not liable |

**[T2]. Fact-specific. Flag any pre-2022 case for a reviewer.**

## Step 2: Standard Rate [T1]

The rates below are printed in the Agenzia's instructions. **Do not take IRAP rates from the Normattiva current view of art. 16.** It still prints a 2014 cut that was later repealed back to its start date. The instructions print the rates that apply.

| Item | Rate | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414 |
| Standard rate (art. 16(1)) | 3.9% | "l’aliquota del 3,9 per cento" |
| Concession holders other than motorway and tunnel concessions (art. 16(1-bis)(a)) | 4.2% | "si applica l’aliquota del 4,20 per cento" |
| Banks and other financial entities (art. 6) | 4.65% | "si applica l’aliquota del 4,65 per cento" |
| Insurance companies (art. 7) | 5.9% | "si applica l’aliquota del 5,90 per cento" |
| Public bodies, on the salary-based base (art. 10-bis) | 8.5% | "l’aliquota d’imposta dell’8,5 per cento" |
| Detrazione from tax for banks and insurers paying the surcharge, 2027 and 2028, only up to the extra tax the surcharge causes (Law 199/2025 comma 74) | EUR 90,000 | "spetta una detrazione pari a euro 90.000" |

- **Regional rate adjustment limits.** Each region may raise or lower the rates of art. 16(1) and (1-bis) by at most 0.92 percentage points, and may set different rates by sector and by category of taxpayer. Since 2013 an ordinary-statute region may also cut the rate to zero. Regions under a health-deficit recovery plan may have automatic increases (2026 IRAP instructions, quadro IR).
- **Sector surcharge 2026 and 2027.** D.L. 21/2026 art. 3(1) raises the rates of art. 16(1) and (1-bis) by two percentage points ("due punti percentuali") for taxpayers whose main activity falls under the ATECO codes in Table 1 attached to that decree, for the tax year after the one in progress at 31 December 2025 and the next one: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2026-02-20;21~art3!vig=2026-06-30 . The article is headed "imprese del comparto energetico" (energy sector). Table 1 was not read for this Guide: check the code against the table before applying the surcharge.
- **Banks and insurers 2026 to 2028.** Law 199/2025 art. 1 comma 74 raises the bank and insurer rates of art. 16(1-bis)(b) and (c) by two percentage points for the tax year after the one in progress at 31 December 2025 and the two after it, except the entities of art. 6(2), (3), (4) and (9). See the instructions linked in the table above. For 2027 and 2028 a detrazione from tax (amount in the table above) is allowed, but only up to the difference between the tax with the surcharge and the tax without it.

### Regional Rate Variations (2025, Selected Regions)

The legacy Guide listed rates for eight regions. No allowed official page prints them, so they are removed. The Agenzia's instructions say the applicable rate code and any regional deductions, detrazioni and credits are published by the Dipartimento delle Finanze of the Ministry of Economy and Finance, in the area "Fiscalità regionale e locale, IRAP". Read the rate for the region, the tax year and the sector there. **[T2]. Never assume the standard rate applies in a given region.**

## Step 3: Tax Base (Valore della Produzione Netta) [T1]

- **Legislation.** D.Lgs. 446/1997, art. 5 (companies), 5-bis (partnerships and sole traders in the income-statement method), 6 (banks), 7 (insurers), 8 (professional partnerships and associations), 10 and 10-bis (entities and public bodies). The 2026 IRAP instructions set out the rows for each quadro: IP (partnerships and others under art. 5-bis), IC (companies), IE (professionals and entities), IK (public bodies).

**Key difference from the income tax base.** The IRAP base is not taxable income. Staff costs and interest are generally not deductible in computing it, and employment deductions are then taken separately (Step 4.3).

### For Imprese Individuali (Sole Proprietors, Business)

Individuals no longer pay IRAP. The same method (art. 5-bis) applies to s.n.c., s.a.s. and similar partnerships: value of production = revenue (art. 85(1)(a), (b), (f), (g) TUIR) plus stock changes, less production costs, without deducting staff costs (other than the deductions in Step 4.3), interest, and losses on receivables. The 2026 IRAP instructions list the add-backs in rows IP29 to IP37 (for example leasing interest in IP30, losses on receivables in IP31, IMU in IP32). A partnership may instead opt for the company method of art. 5 (art. 5-bis(2)).

### For Lavoratori Autonomi (Professionals)

Individual professionals no longer pay IRAP. For società semplici and associations of professionals (art. 3(1)(c)), art. 8 sets the base as fees received less costs of the activity, including depreciation, but excluding interest and staff costs; fees and costs are taken as they count for the income tax return: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art8!vig=2026-06-30

### Simplified Computation for Small Businesses (Art. 5-bis)

- **Simplified computation option.** Businesses taxed on a flat-rate income basis for income tax may opt to compute the value of production under art. 17(2) (section III of quadri IP and IE, section V of quadro IC). [T2]: check the option rules in the instructions.

### Step 4.1: Verify IRAP liability

~~~
IF client is an individual (persona fisica) with a business or a profession, forfettario included:
    IRAP = 0. No IRAP return. (Law 234/2021 art. 1 comma 8)
ELIF farming within art. 32 TUIR, fund other than SICAV, pension fund, EEIG:
    not a taxpayer (art. 3(2))
ELSE:
    proceed to calculation
~~~

### Step 4.2: Compute valore della produzione netta

~~~
partnership (art. 5-bis):  value of production = revenue + stock changes + other income
                           less production costs, WITHOUT staff costs, interest, losses on receivables
company (art. 5):          same components as classified in the income statement
professional partnership or association (art. 8):
                           fees received less costs of the activity, WITHOUT interest and staff costs
~~~

### Step 4.3: Apply deductions

Employment deductions of art. 11 D.Lgs. 446/1997, as the 2026 IRAP instructions set them out (section I of quadro IS):

| Item | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414 |
| Permanent staff (art. 11(4-octies)) | the whole cost | "deduzione del costo complessivo per il personale dipendente con contratto a tempo indeterminato" |
| Seasonal workers employed at least 120 days in each of two tax years, from the second contract with the same employer within two years of the end of the previous one (INAIL contributions stay fully deductible) | 70% | "nei limiti del 70 per cento del costo complessivamente sostenuto" |
| Fixed-term staff, per worker, up to five workers (art. 11(4-bis.1)) | EUR 1,850 | "in misura pari a euro 1.850, su base annua" |
| Revenue cap for that deduction (positive components of the value of production) | EUR 400,000 | "non superiori nel periodo d’imposta a euro 400.000" |
| Also deductible | INAIL accident insurance contributions; apprentices, disabled staff, training contracts, research and development staff (art. 11(1)(a)) | see quadro IS rows IS1 and IS4 |

The permanent-staff deduction is for taxpayers computing the base under art. 5 to 9.

Per employee, the deductions of art. 11(1) and (4-bis.1) may not exceed the pay and other employer costs (art. 11(4-septies)). For activity partly abroad, the deductions cover only staff employed in Italy.

**Flat deduction for small bases (art. 11(4-bis)).** It depends on the value of production, and steps down in four bands. It is a deduction from the base, not a threshold of exemption.

| Base (value of production after the other art. 11 staff deductions) up to | Deduction, companies and others | Deduction, partnerships and professional associations (art. 3(1)(b) and (c)) |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414 |
| EUR 180,759.91 | EUR 8,000 | EUR 13,000 |
| EUR 180,839.91 | EUR 6,000 | EUR 9,750 |
| EUR 180,919.91 | EUR 4,000 | EUR 6,500 |
| EUR 180,999.91 | EUR 2,000 | EUR 3,250 |

Above the last band there is none. For a tax year shorter or longer than twelve months, or starting or ending during the year, the amounts are scaled to the calendar year (art. 11(4-bis.2)).

### Step 4.4: Apply regional rate

~~~
IRAP for each region = (net value of production attributed to that region) x (rate for that region, sector and year)
~~~

Take the rate from the regional rate list described in Step 2. Add the two-point surcharge only if the sector or bank and insurer rule applies. If the amount due to a region is not more than the minimum in the Step 5 table, no tax is due to that region.

### Step 4.5: Deductions from IRAP itself

Regional laws may grant detrazioni and tax credits against the IRAP due to that region (quadro IR, columns 9 and 10), listed with the regional rates. For IRAP in the income tax return, see Step 7.

## Step 5: Payment Schedule [T1]

- **Legislation.** D.Lgs. 446/1997, art. 30; D.P.R. 435/2001, art. 17; chapter 5 of the 2026 IRAP instructions.

**Payment Schedule**

| Item | Rule | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414 |
| Balance (saldo) and first acconto, partnerships and associations (art. 5 TUIR) | 30 June of the year the return is filed | "entro il 30 giugno dell’anno di presentazione" |
| Balance and first acconto, companies and other taxpayers | last day of the sixth month after the end of the tax year | "entro l’ultimo giorno del sesto mese successivo" |
| Paying 30 days later: interest added to balance and first acconto | 0.40% | "dello 0,40 per cento a titolo di interesse corrispettivo" |
| Minimum: no tax due to (and no refund from) a region if its amount is not more than | EUR 10.33 | "non superano 10,33 euro" |

Pay with form F24, electronically for VAT number holders.

### Advance Payment (Acconti)

**Advance Payment (Acconti)**

| Item | Rule | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414 |
| Total acconto (historical method) | 100% of last year's tax (row IR21) | "nella misura pari al 100 per cento" |
| Partnerships and associations: acconto due only if last year's tax is above | EUR 51.65 | "sempreché tale importo sia superiore a euro 51,65" |
| Companies and other taxpayers: acconto due only if last year's tax is above | EUR 20.66 | "sempreché tale importo sia superiore a euro 20,66" |
| First instalment, with the balance | 40% | "la prima, pari al 40 per cento" |
| First instalment not due if it is not more than | EUR 103 | "se d’importo non superiore a euro 103" |
| Second instalment, by 30 November 2026 (partnerships) or the last day of the eleventh month of the tax year (others) | 60% | "la seconda, pari al residuo 60 per cento, entro il 30 novembre 2026" |
| Taxpayers under the ISA reliability indices with revenue within the ISA limit | two instalments of 50% | "in due rate ciascuna nella misura del 50 per cento" |

- **Forecast method (metodo previsionale).** The acconti may be based on the tax expected for the current year instead. If they turn out too low, penalties apply.
- **2026 acconto adjustments.** For the 2026 acconto, last year's tax is recomputed as if certain listed provisions did not apply (Law 207/2024 art. 1 comma 19). Energy-sector taxpayers under D.L. 21/2026 compute the 2026 acconto as if the surcharge had applied last year (D.L. 21/2026 art. 3(2), linked in Step 2). Banks and insurers do the same for the Law 199/2025 surcharge (Law 199/2025 art. 1 comma 75). [T2].

~~~
1st acconto = last year's IRAP x first-instalment share (table above), with the balance
2nd acconto = last year's IRAP x second-instalment share, by the second date
~~~

## Step 6: IRAP Declaration [T1]

- **Legislation.** D.Lgs. 446/1997, art. 19; D.P.R. 322/1998. Chapter 3 of the 2026 IRAP instructions linked in the tables above.

**IRAP Declaration obligations**

| Obligation | Detail |
| --- | --- |
| Form | Dichiarazione IRAP (Modello IRAP), a separate return |
| Deadline, partnerships and associations | Between 15 April and 31 October of the year after the tax year |
| Deadline, companies (IRES taxpayers) | By the last day of the tenth month after the end of the tax year. For tax year 2025 the instructions give 2 November 2026, because 31 October 2026 was a Saturday |
| Filing | Electronic, through Entratel or Fisconline, directly or through an authorised intermediary |

The legacy Guide said 30 November; that is wrong.

## Step 7: Tax Deductibility of IRAP [T1]

- **Legislation.** D.L. 185/2008, art. 6(1): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2008-11-29;185~art6!vig=2026-06-30 and D.L. 201/2011, art. 2(1): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-12-06;201~art2!vig=2026-06-30

**Deductions from IRAP**

| Deduction | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2008-11-29;185~art6!vig=2026-06-30 |
| IRAP linked to interest (deductible for IRES and IRPEF) | 10% of IRAP | "un importo pari al 10 per cento dell'imposta regionale sulle attività produttive" |
| IRAP on staff costs, net of the art. 11 deductions (D.L. 201/2011 art. 2) | the IRAP on that share | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-12-06;201~art2!vig=2026-06-30 : "relativa alla quota imponibile delle spese per il personale dipendente e assimilato" |

Both deductions apply only to IRAP computed under art. 5, 5-bis, 6, 7 and 8 of D.Lgs. 446/1997, so not to non-commercial entities (art. 10) or public bodies (art. 10-bis). The 10% share is referred, as a flat amount, to the tax on net interest expense ("al netto degli interessi attivi"). [T2]: whether it is available when there is no net interest expense is a practice point; confirm. With permanent staff now fully deductible for IRAP, the staff-cost share is often small.

## Step 8: Edge Case Registry

### EC1: Freelance professional, no employees, minimal equipment [T1]

**Situation:** Avvocato (lawyer) working alone from home.
**Resolution:** No IRAP and no IRAP return: an individual professional is outside IRAP since 2022.

### EC2: Professional with one employee [T2]

**Situation:** Architect, as an individual, with one part-time employee.
**Resolution:** Still no IRAP for 2026: the individual rule does not depend on staff. If the architect works through a studio associato or a società semplice, the association pays IRAP on the art. 8 base. Whether a small association escapes for lack of organisation is [T3]: refer.

### EC3: Regime forfettario [T1]

**Situation:** Client uses the regime forfettario.
**Resolution:** No IRAP, no return. Forfettari are individuals, so the 2022 rule covers them.

### EC4: Sole proprietor with a shop [T1]

**Situation:** Impresa individuale running a retail shop with two employees.
**Resolution:** No IRAP for 2026. The legacy Guide said IRAP applies; since 2022 it does not for individuals. If the shop is run by an s.n.c. or s.a.s., IRAP applies under art. 5-bis.

### EC5: Multiple regions [T2]

**Situation:** A partnership or company works in Lombardia and Campania.
**Resolution:** If activity in another region lasts at least three months, the base is split by region in proportion to the pay of staff and collaborators working at premises in each region (quadro IS section II and quadro IR). Each region's rate applies to its share. [T2]: confirm the split.

### EC6: IRAP and IRPEF interaction [T1]

**Situation:** A partner asks whether IRAP reduces income tax.
**Resolution:** Yes, by the shares in Step 7, deducted in the partnership's income computation.

### EC7: First year of activity [T1]

**Situation:** New s.r.l. started in April 2026.
**Resolution:** IRAP applies from the first year. No acconti are due for the first year (there is no prior-year tax on the historical method). The flat deduction of Step 4.3 is scaled to the calendar year. The balance is due by the date in the Step 5 table.

### EC8: Cessation mid-year [T1]

**Situation:** A partnership closes in August 2026.
**Resolution:** IRAP applies to the value of production of the period of activity. The flat deduction is scaled. [T2]: return and payment dates for a winding-up follow art. 5 and 5-bis D.P.R. 322/1998; confirm.

### EC9: Contribuente minimo switching to ordinary [T2]

**Situation:** An individual leaves the forfettario or minimi regime for the ordinary regime.
**Resolution:** Still no IRAP: the individual rule does not depend on the income tax regime. IRAP starts only if the business moves into a partnership or company.

## Step 9: Test Suite

### Test 1: Professional exempt (no autonomous organisation)

**Input:** Freelance consultant, individual, works alone.
**Expected output:** IRAP nil.

### Test 2: Professional with organisation

**Input:** Dentist, individual, two employees and a rented studio.
**Expected output:** IRAP nil for 2026 (the legacy Guide computed a charge). If the same dentist practises through a studio associato: base under art. 8, less the permanent-staff deduction and the flat deduction in the right column of the Step 4.3 table, times the regional rate.

### Test 3: Sole proprietor (impresa), standard rate

**Input:** Retail s.n.c. in Lombardia with permanent staff.
**Expected output:** Base under art. 5-bis without staff costs and interest; deduct the whole cost of permanent staff and the flat deduction for partnerships from the Step 4.3 table if the base is in a band; apply the Lombardia rate for 2026 from the regional list.

### Test 4: Regime forfettario

**Input:** Forfettario individual.
**Expected output:** IRAP nil, no return.

### Test 5: High-rate region (Campania)

**Input:** Company in Campania.
**Expected output:** Read the Campania rate for the sector and year from the regional list. Never use a remembered rate.

### Test 6: Advance payments

**Input:** Partnership whose last-year IRAP is above the partnership minimum in the Step 5 table.
**Expected output:** Acconto equal to the whole of last year's tax, in two instalments of the shares shown in the Acconti table (or two equal instalments for ISA taxpayers), the first with the balance, the second by 30 November 2026.

### Test 7: Low IRAP, no advances

**Input:** Partnership whose last-year IRAP is not above the partnership minimum in the Step 5 table.
**Expected output:** No acconti. Only the balance is due.

## The method, step by step

1. Check who the taxpayer is: art. 3 D.Lgs. 446/1997 and note 70 (Law 234/2021 art. 1 comma 8). An individual with a business or profession stops here. https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art3!vig=2026-06-30
2. Choose the quadro and base: IP (art. 5-bis), IC (art. 5, 6, 7), IE (art. 8, 10), IK (art. 10-bis), as the 2026 IRAP instructions set out. For professional associations, art. 8: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art8!vig=2026-06-30
3. Take the employment deductions and the flat deduction of art. 11 in quadro IS section I, following the instructions: https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414
4. Split the base by region if activity in another region lasted at least three months (quadro IS section II), then apply each region's rate from the Dipartimento delle Finanze list. Rates and limits in Step 2 come from the same instructions: https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414
5. Check the surcharges: sector (D.L. 21/2026 art. 3, Table 1) and banks and insurers (Law 199/2025 comma 74). https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2026-02-20;21~art3!vig=2026-06-30
6. File the IRAP return electronically by the deadline in Step 6, and pay the balance and acconti with form F24 on the dates in Step 5 (chapters 3 and 5 of the instructions): https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414
7. In the income tax return, deduct the IRAP shares of D.L. 185/2008 art. 6 and D.L. 201/2011 art. 2. https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-12-06;201~art2!vig=2026-06-30

## Ask the client first

- Do you work as an individual, or through a partnership, association or company?
- What is the main activity and its ATECO code? Is it in the energy sector, banking, insurance or a concession?
- In which regions do you have premises or staff, and for how long in the year?
- How many staff do you have, on which contracts (permanent, fixed-term, seasonal, apprentices)?
- What IRAP did you declare last year, and do you apply the ISA reliability indices?
- Are you claiming back IRAP paid as an individual professional for a year before 2022?

## When to refuse or refer

- The IRAP rate of a named region for a named sector: not on an allowed page. Send the client to the Dipartimento delle Finanze regional list.
- Whether an ATECO code is in Table 1 of D.L. 21/2026 (not read for this Guide).
- Autonomous-organisation disputes and refund claims for years up to 2021, and any claim that a small partnership or association lacks organisation.
- Banks, financial intermediaries, insurers, holding companies (art. 6 and 7) and public bodies (art. 10-bis).
- Multi-region and foreign-activity splits beyond the basic pay-based rule.
- Group reorganisations, the concordato preventivo biennale, dormant companies (società di comodo) and farming mixed with other activity.
- Any combined or effective rate: no official page prints one.

## PROHIBITIONS

- NEVER charge IRAP to an individual (sole trader, professional, forfettario, minimo) for 2022 or later
- NEVER take IRAP rates from the Normattiva current view of art. 16; use the Agenzia instructions
- NEVER use the income tax base as the IRAP base; staff costs and interest are not deducted in computing it
- NEVER apply the standard rate without checking the region, the sector surcharge and the bank and insurer surcharge
- NEVER forget the IRAP deduction in the income tax return (Step 7)
- NEVER present acconti as optional when last year's tax is above the minimum in the Step 5 table
- NEVER advise on multi-region apportionment without flagging for reviewer

## Sources

- 2026 IRAP instructions (tax year 2025), Agenzia delle Entrate: https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414
- D.Lgs. 446/1997 art. 3, with note 70 (Law 234/2021): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art3!vig=2026-06-30
- D.Lgs. 446/1997 art. 8: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art8!vig=2026-06-30
- D.L. 21/2026 art. 3: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2026-02-20;21~art3!vig=2026-06-30
- D.L. 185/2008 art. 6: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2008-11-29;185~art6!vig=2026-06-30
- D.L. 201/2011 art. 2: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-12-06;201~art2!vig=2026-06-30

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by OpenAccountants.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
