# France VAT figure and rule ledger

Independent AI source/calculation review: completed31October2026. The writer-status sentence below records the earlier handover; the [pack review](../docs/research/2026-10-31-france-pack-review.md) records the final outcome. This is not accountant attestation.

Guide SHA256 `f540e90aec7dda55893edfe6fbd8d973e8812f5ea41305ebd8b41e185d1362d4`, version 2.17; writer repair FR-R100–R103, 31 October 2026. The completed whole-pack review and its findings remain preserved; different independent successor review pending.

Native coordinates below count LF characters only. Each unchanged quotation retains its actual original read attribution and source representation. Hashes and row rebinding establish identity, not independent legal acceptance. Source/history files remain private; this ledger is self-contained.

## Current rules and figures

| Unit / section / native LF | Wording | Source quotation anchors | Qualification |
|---|---|---|---|
| france-vat-return-0003 / # France: VAT and the VAT return (TVA, CA3 and CA12) / 35 | - **The VAT articles are still in the Code général des impôts (CGI) for all of 2026.** Ordonnance n° 2025-1247 of 17 December 2025 moves them into book II of the Code des impositions sur les biens et services (CIBS). Ordonnance n° 2026-671 of 27 July 2026 put that move back from 1 September 2026 to 1 January 2027, and the old CGI references can still be used until 30 June 2028 (BOFiP, actualité of 7 October 2026). This skill cites the CGI article in force in 2026. | [VAT-Q050](#vat-q050) |  |
| france-vat-return-0004 / # France: VAT and the VAT return (TVA, CA3 and CA12) / 36 | - **The 2026 finance law is loi n° 2026-103 of 19 February 2026.** For VAT it changed rate rules at the edges (waste services and cold networks to 5.5%, forestry work kept at 10%, among others), ended the exclusion of deduction for alcohol advertising from 21 February 2026, and amended the e-invoicing and e-reporting fines (CGI art. 1737 and 1788 D). It did not touch the franchise thresholds or the 20%, 10%, 5.5% and 2.1% rates. | [VAT-Q050](#vat-q050); [VAT-Q001](#vat-q001); [VAT-Q002](#vat-q002); [ROOT-VAT-R001](#root-vat-r001); [ROOT-VAT-R002](#root-vat-r002); [ROOT-VAT-R004](#root-vat-r004); [ROOT-VAT-R005](#root-vat-r005); [ROOT-VAT-R006](#root-vat-r006); [ROOT-VAT-R018](#root-vat-r018); [ROOT-VAT-S002](#root-vat-s002); [ROOT-VAT-C008](#root-vat-c008); [ROOT-VAT-D019](#root-vat-d019); [ROOT-VAT-D020](#root-vat-d020) |  |
| france-vat-return-0005 / ## Who this applies to / 40 | - **Taxable persons established in France** making supplies for consideration in the French VAT scope. Charge the applicable French VAT where the supplier is liable, subject to the actual franchise, exemption and recipient-liability rules; establish the supply and place first. | [ROOT-VAT-C002](#root-vat-c002); [VAT-Q018](#vat-q018); [VAT-Q035](#vat-q035) |  |
| france-vat-return-0006 / ## Who this applies to / 41 | - **The franchise en base (CGI art. 293 B).** An eligible business does not charge VAT on its franchised supplies and cannot deduct tax on costs used for those operations (art. 293 E). No ordinary CA3/CA12 output return is required for those franchised sales/services; separately test foreign purchases and other operations for which the business itself owes VAT. The franchise does not cancel those liabilities. Its domestic franchise invoices state "TVA non applicable, art. 293 B du code général des impôts"; art. 293 E gives the applicable alternative reference for art. 293 B bis claims. It may opt for VAT under art. 293 F. | [VAT-Q001](#vat-q001); [VAT-Q002](#vat-q002); [ROOT-VAT-C031](#root-vat-c031); [ROOT-VAT-C032](#root-vat-c032); [ROOT-VAT-C033](#root-vat-c033); [ROOT-VAT-C034](#root-vat-c034); [ROOT-VAT-C035](#root-vat-c035); [ROOT-VAT-C036](#root-vat-c036) |  |
| france-vat-return-0007 / ## Who this applies to / 42 | - **The single EUR 25,000 threshold never applied.** The 2025 finance law (loi n° 2025-127, art. 32) set one threshold of EUR 25,000 from 1 March 2025. Loi n° 2025-1044 of 3 November 2025, art. 1, restored the separate thresholds with effect from 1 March 2025 itself. So for 2025 and 2026 the thresholds are the ones in the table below. Any page or skill that prints EUR 25,000 as the French franchise threshold is wrong. | [VAT-Q002](#vat-q002); [ROOT-VAT-D001](#root-vat-d001) |  |
| france-vat-return-0008 / ## Who this applies to / 43 | - **Businesses established in another EU state** may use the French franchise only if they meet the French art. 293 B conditions as well as the cumulative art. 293 B bis requirements: EU-wide turnover at or below EUR 100,000 in BOTH the previous and current year and the prescribed home-state notification/identification process. A French business using another state's franchise notifies the French administration and reports quarterly under art. 293 B ter. | [VAT-Q001](#vat-q001); [VAT-Q002](#vat-q002); [ROOT-VAT-C025](#root-vat-c025); [ROOT-VAT-C026](#root-vat-c026); [ROOT-VAT-C027](#root-vat-c027); [ROOT-VAT-C028](#root-vat-c028) |  |
| france-vat-return-0009 / ## Who this applies to / 44 | - **Régime réel normal.** Monthly CA3, or quarterly where the VAT due each year is below EUR 4,000 (CGI art. 287-2). | [VAT-Q006](#vat-q006); [VAT-Q026](#vat-q026) |  |
| france-vat-return-0010 / ## Who this applies to / 45 | - **Régime simplifié (régime simplifié de déclaration).** One annual CA12 plus two instalments (CGI art. 287-3), for businesses inside the turnover band in the table and with VAT due of EUR 15,000 or less for the previous year (CIBS art. L. 162-4, L. 162-5, L. 162-7). | [VAT-Q006](#vat-q006); [VAT-Q007](#vat-q007); [VAT-Q045](#vat-q045); [VAT-Q049](#vat-q049) |  |
| france-vat-return-0011 / ## Who this applies to / 46 | - **Out of this skill:** the overseas departments (their own rates, listed for recognition only; VAT is provisionally not applicable in Guyane and Mayotte), Corsica's special rates beyond the CA3 lines, the margin scheme, property VAT (TVA immobilière), VAT groups (CGI art. 256 C), and non-residents registering through a fiscal representative. Refuse or refer these (see Ask the client first). | [ROOT-VAT-D002](#root-vat-d002); [ROOT-VAT-D003](#root-vat-d003); [ROOT-VAT-D004](#root-vat-d004); [ROOT-VAT-D005](#root-vat-d005); [ROOT-VAT-D006](#root-vat-d006); [ROOT-VAT-D007](#root-vat-d007); [VAT-Q018](#vat-q018) | Scope exclusions are house referral limits; DOM facts source-bound. No full margin/property/group method claimed. |
| france-vat-return-0013 / ## Rates, bands and thresholds / 52 | &#124; Standard rate (CGI art. 278) &#124; 20% &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191854/2026-10-24 &#124; | [ROOT-VAT-R001](#root-vat-r001) |  |
| france-vat-return-0014 / ## Rates, bands and thresholds / 53 | &#124; Intermediate reduced rate: qualifying hotel accommodation, on-site restaurant meals excluding alcohol, passenger transport and television subscriptions (CGI art. 279); qualifying works on dwellings completed more than two years ago (art. 279-0 bis; conditions below) &#124; 10% &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191654/2026-10-24 &#124; | [ROOT-VAT-R006](#root-vat-r006); [ROOT-VAT-R007](#root-vat-r007); [ROOT-VAT-R008](#root-vat-r008); [ROOT-VAT-R009](#root-vat-r009); [ROOT-VAT-R026](#root-vat-r026) |  |
| france-vat-return-0015 / ## Rates, bands and thresholds / 54 | &#124; Reduced rate: qualifying food with statutory exclusions and books on physical media, downloaded or audio (CGI art. 278-0 bis); potable water supplied by distribution networks; qualifying energy-renovation works (art. 278-0 bis A; conditions below); collection and treatment of household and similar municipal waste and supporting services from 1 March 2026 (art. 278-0 bis, M) &#124; 5.5% &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191654/2026-10-24 &#124; | [ROOT-VAT-R002](#root-vat-r002); [ROOT-VAT-R003](#root-vat-r003); [ROOT-VAT-R004](#root-vat-r004); [ROOT-VAT-R005](#root-vat-r005); [ROOT-VAT-R017](#root-vat-r017); [ROOT-VAT-R024](#root-vat-r024); [ROOT-VAT-R025](#root-vat-r025) |  |
| france-vat-return-0016 / ## Rates, bands and thresholds / 55 | &#124; Particular rate: medicines meeting CGI art. 281 octies conditions; defined human-blood products subject to the therapeutic exemption below; qualifying first performances (art. 281 quater and annexe III art. 89 ter); qualifying press including eligible digital press (art. 298 septies) &#124; 2.1% &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191656/2026-10-24 &#124; | [ROOT-VAT-R018](#root-vat-r018); [ROOT-VAT-R019](#root-vat-r019); [ROOT-VAT-R020](#root-vat-r020); [ROOT-VAT-R021](#root-vat-r021); [ROOT-VAT-R022](#root-vat-r022); [ROOT-VAT-R023](#root-vat-r023); [ROOT-VAT-R027](#root-vat-r027) |  |
| france-vat-return-0017 / ## Rates, bands and thresholds / 56 | &#124; Overseas departments (Guadeloupe, Martinique, Réunion): standard / reduced / particular &#124; 8.5% / 2.1% / 1.75% and 1.05% &#124; 2026 &#124; https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom &#124; | [ROOT-VAT-D002](#root-vat-d002); [ROOT-VAT-D003](#root-vat-d003); [ROOT-VAT-D004](#root-vat-d004); [ROOT-VAT-D005](#root-vat-d005); [ROOT-VAT-D006](#root-vat-d006); [ROOT-VAT-D007](#root-vat-d007) |  |
| france-vat-return-0018 / ## Rates, bands and thresholds / 57 | &#124; Corsica, CA3 lines TC, T3, T4, T5 &#124; 13%, 10%, 2.1%, 0.9% &#124; 2026 &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf &#124; | [VAT-Q068](#vat-q068); [VAT-Q069](#vat-q069); [VAT-Q070](#vat-q070); [VAT-Q071](#vat-q071) |  |
| france-vat-return-0019 / ## Rates, bands and thresholds / 58 | &#124; Franchise: total turnover, previous calendar year / current year (CGI art. 293 B, I) &#124; EUR 85,000 / EUR 93,500 &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-24 &#124; | [VAT-Q001](#vat-q001) |  |
| france-vat-return-0020 / ## Rates, bands and thresholds / 59 | &#124; Franchise: services other than on-site catering and accommodation, previous year / current year &#124; EUR 37,500 / EUR 41,250 &#124; 2026 &#124; same &#124; | [VAT-Q001](#vat-q001) |  |
| france-vat-return-0021 / ## Rates, bands and thresholds / 60 | &#124; Franchise: lawyers', authors' and performers' regulated work, previous / current year (art. 293 B, I bis) &#124; EUR 50,000 / EUR 55,000 &#124; 2026 &#124; same &#124; | [VAT-Q002](#vat-q002) |  |
| france-vat-return-0022 / ## Rates, bands and thresholds / 61 | &#124; Franchise: their other activities, previous / current year &#124; EUR 35,000 / EUR 38,500 &#124; 2026 &#124; same &#124; | [VAT-Q002](#vat-q002) |  |
| france-vat-return-0023 / ## Rates, bands and thresholds / 62 | &#124; Franchise for an EU-established business: EU-wide turnover, previous and current year (art. 293 B bis) &#124; EUR 100,000 &#124; 2026 &#124; same &#124; | [ROOT-VAT-C025](#root-vat-c025); [ROOT-VAT-C026](#root-vat-c026); [ROOT-VAT-C027](#root-vat-c027) |  |
| france-vat-return-0024 / ## Rates, bands and thresholds / 63 | &#124; Régime simplifié: previous year turnover, goods, on-site catering, accommodation (CIBS L. 162-4, 1°; amount fixed for 2026 by CIBS art. A. 162-7) &#124; EUR 85,000 to EUR 945,000 (below the lower end, the franchise; F23566: "compris entre : 85 000 € et 945 000 €") &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000049803748/2026-10-24 &#124; | [VAT-Q006](#vat-q006); [VAT-Q045](#vat-q045); [VAT-Q049](#vat-q049) |  |
| france-vat-return-0025 / ## Rates, bands and thresholds / 64 | &#124; Régime simplifié: current year ceiling, same activities (CIBS L. 162-5, 1°; A. 162-7) &#124; EUR 1,040,000 &#124; 2026 &#124; same &#124; | [VAT-Q006](#vat-q006); [VAT-Q045](#vat-q045); [VAT-Q049](#vat-q049) |  |
| france-vat-return-0026 / ## Rates, bands and thresholds / 65 | &#124; Régime simplifié: previous year turnover, other services incl. furnished lets (CIBS L. 162-4, 2°; A. 162-7) &#124; EUR 37,500 to EUR 286,000 (F23566) &#124; 2026 &#124; same &#124; | [VAT-Q006](#vat-q006); [VAT-Q045](#vat-q045); [VAT-Q049](#vat-q049) |  |
| france-vat-return-0027 / ## Rates, bands and thresholds / 66 | &#124; Régime simplifié: current year ceiling, other services (CIBS L. 162-5, 2°; A. 162-7) &#124; EUR 323,000 &#124; 2026 &#124; same &#124; | [VAT-Q006](#vat-q006); [VAT-Q045](#vat-q045); [VAT-Q049](#vat-q049) |  |
| france-vat-return-0028 / ## Rates, bands and thresholds / 67 | &#124; Régime simplifié: VAT due for the previous year must not exceed (CIBS L. 162-7) &#124; EUR 15,000 &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000044598127/2026-10-24 &#124; | [VAT-Q006](#vat-q006); [VAT-Q045](#vat-q045); [VAT-Q049](#vat-q049) |  |
| france-vat-return-0029 / ## Rates, bands and thresholds / 68 | &#124; Régime réel normal: quarterly CA3 where annual VAT due is below (CGI art. 287-2) &#124; EUR 4,000 &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191928/2026-10-24 &#124; | [VAT-Q006](#vat-q006) |  |
| france-vat-return-0030 / ## Rates, bands and thresholds / 69 | &#124; Régime simplifié instalments: July / December, share of previous year's tax before fixed-asset VAT (CGI art. 287-3) &#124; 55% / 40% &#124; 2026 &#124; same &#124; | [VAT-Q006](#vat-q006) |  |
| france-vat-return-0031 / ## Rates, bands and thresholds / 70 | &#124; No instalments where previous year's tax (before fixed-asset VAT) is below (CGI art. 287-3) &#124; EUR 1,000 &#124; 2026 &#124; same &#124; | [VAT-Q006](#vat-q006) |  |
| france-vat-return-0032 / ## Rates, bands and thresholds / 71 | &#124; Instalment change allowed where the real tax differs by at least (CGI art. 287-3) &#124; 10% &#124; 2026 &#124; same &#124; | [VAT-Q006](#vat-q006) |  |
| france-vat-return-0033 / ## Rates, bands and thresholds / 72 | &#124; First year of a new business: each self-set instalment at least (CGI art. 287-3) &#124; 80% of the half-year's real tax &#124; 2026 &#124; same &#124; | [VAT-Q006](#vat-q006) |  |
| france-vat-return-0034 / ## Rates, bands and thresholds / 73 | &#124; CA12 credit refundable at year end (frame VII) only where at least &#124; EUR 150 &#124; 2026 &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5291.pdf &#124; | [VAT-Q044](#vat-q044); [ROOT-VAT-C021](#root-vat-c021) |  |
| france-vat-return-0035 / ## Rates, bands and thresholds / 74 | &#124; Eligible distance goods sales from France and cross-border B2C digital services: the origin-tax exception requires sole-France establishment and aggregate turnover not exceeding this amount in BOTH current and previous calendar years, with no destination-tax option (see Cross-border points) &#124; EUR 10,000 excluding VAT in each year &#124; 2026 &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf &#124; | [VAT-Q024](#vat-q024); [VAT-Q025](#vat-q025) |  |
| france-vat-return-0036 / ## Rates, bands and thresholds / 75 | &#124; Intra-EU acquisitions by a business in the franchise: where the amount exceeds this in the previous or current calendar year, the French buyer self-assesses at the French rate and must ask its SIE for an intra-EU VAT number as soon as it knows the limit is crossed &#124; EUR 10,000 &#124; 2026 &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F21746 &#124; | [ROOT-VAT-C035](#root-vat-c035) |  |
| france-vat-return-0037 / ## Rates, bands and thresholds / 76 | &#124; Ordinary low-value invoices: the supplier VAT number and exemption reference can be omitted under CGI annexe II art. 242 nonies A, II, subject to its exclusions and independently required particulars; customer VAT numbers and reverse-charge wording are not generally waived &#124; EUR 150 excluding VAT, inclusive &#124; 2026 &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F31808 ; actual statute and BOFiP clarification below &#124; | [ROOT-VAT-Q001](#root-vat-q001); [ROOT-VAT-Q002](#root-vat-q002); [ROOT-VAT-Q003](#root-vat-q003); [ROOT-VAT-Q004](#root-vat-q004) |  |
| france-vat-return-0038 / ## Rates, bands and thresholds / 77 | &#124; Optional expense tolerance for qualifying small equipment, unit value excluding VAT up to; actual capitalisation or expensing determines line 19 or 20 &#124; EUR 500 &#124; 2026 &#124; https://bofip.impots.gouv.fr/bofip/2109-PGP.html &#124; | [VAT-Q015](#vat-q015) |  |
| france-vat-return-0039 / ## Rates, bands and thresholds / 78 | &#124; Fuel: petrol, diesel and E85 in a vehicle excluded from deduction, or a lease the lessee cannot deduct / in any other vehicle &#124; 80% / 100% deductible &#124; from 2022 &#124; https://bofip.impots.gouv.fr/bofip/1194-PGP.html &#124; | [ROOT-VAT-C022](#root-vat-c022) |  |
| france-vat-return-0040 / ## Rates, bands and thresholds / 79 | &#124; Fuel: petroleum gases/other gaseous hydrocarbons other than natural gas, and lamp oil used as fuel (liquefied products follow ordinary rules) in an excluded vehicle &#124; 50% deductible &#124; 2026 &#124; same &#124; | [ROOT-VAT-C023](#root-vat-c023); [ROOT-VAT-C024](#root-vat-c024) |  |
| france-vat-return-0041 / ## Rates, bands and thresholds / 80 | &#124; Late interest (CGI art. 1727, III) &#124; 0.20% a month &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006147309/2026-10-24 &#124; | [ROOT-VAT-P001](#root-vat-p001) |  |
| france-vat-return-0042 / ## Rates, bands and thresholds / 82 | **Apply the reduced-rate conditions to the actual supply.** Food at 5.5% excludes confectionery, the specified chocolate products, margarine/vegetable fats, caviar and alcohol; the statutory chocolate exceptions still matter. The title of a product or supplier does not decide the rate. For ordinary 10% dwelling works, verify improvement, conversion, fitting-out or maintenance, domestic use and completion more than two years ago; exclude the specified household/furniture and large-equipment supply components. Cleaning, green-space works and supply/installation of a fossil-fuel-capable boiler are at the standard rate. Works producing a new building or increasing floor area by more than 10% over the statutory two-year period also use the standard rate. Obtain the customer's certification on the quote or invoice and keep the supporting documents (CGI art. 279-0 bis). | [ROOT-VAT-R002](#root-vat-r002); [ROOT-VAT-R026](#root-vat-r026) |  |
| france-vat-return-0043 / ## Rates, bands and thresholds / 84 | For 5.5% energy renovation, CGI art. 278-0 bis A requires residential use and premises completed at least two years ago, specified insulation, heating/ventilation or hot-water energy-saving/renewable works, and the delegated technical/performance conditions. Apply its new-building/floor-increase and fossil-boiler exclusions and customer certification requirements. The customer keeps the supporting copy and invoices through 31 December of the fifth year after the invoice; these gates do not replace checking the delegated technical list for the actual work. | [ROOT-VAT-R024](#root-vat-r024); [ROOT-VAT-R025](#root-vat-r025) |  |
| france-vat-return-0044 / ## Rates, bands and thresholds / 86 | The 2.1% performance treatment is limited to the qualifying works and first 140 performances under CGI art. 281 quater and annexe III art. 89 ter, with the statutory exclusions; it is not a rate for every new show. Press must meet the annexed publication conditions or the recognised digital-press conditions. Human-blood treatment is also conditional: the defined labile products for human research and in-vitro diagnostic devices prepared from blood/components fall within CGI art. 281 octies; whole blood and derivatives intended for direct therapeutic use instead fall within the exemption in CGI art. 261, 4-2° (BOI-TVA-LIQ-40-10§350). | [ROOT-VAT-R018](#root-vat-r018); [ROOT-VAT-R019](#root-vat-r019); [ROOT-VAT-R020](#root-vat-r020); [ROOT-VAT-R021](#root-vat-r021); [ROOT-VAT-R022](#root-vat-r022); [ROOT-VAT-R023](#root-vat-r023); [ROOT-VAT-R027](#root-vat-r027) |  |
| france-vat-return-0045 / ## Rates, bands and thresholds / 88 | **Other retained rate examples.** Qualifying theatres, chansonniers, circuses, concerts and variety shows fall within CGI art. 278-0 bis, F at 5.5%, subject to its exclusion for establishments where consumption during performances is customary and the stated Centre national de la musique affiliation exception. Its separate F-2 ticket category requires an original musical performance, a physically present remunerated artist and the specified operator licence where refreshments are optional. Check those actual conditions and the distinct 2.1% first-performance rules above; a generic “live performance” label does not decide the rate. | [ROOT-VAT-W035](#root-vat-w035) |  |
| france-vat-return-0046 / ## Rates, bands and thresholds / 90 | **How the franchise thresholds bite.** The basic threshold is tested on the previous calendar year: crossing it brings VAT from 1 January of the next year. The higher threshold is tested on the current year: crossing it brings VAT from the day of the overrun itself (CGI art. 293 B, II), so invoices issued that day already carry VAT. For a start-up, service-public F21746 annualises turnover as actual turnover × calendar-year days / actual active days expressly to test the following year. It does not establish a universal annualised-turnover test for the current year. The conflicting first-year sources are set out below. | [VAT-Q002](#vat-q002); [VAT-Q003](#vat-q003); [VAT-Q004](#vat-q004); [VAT-Q005](#vat-q005) |  |
| france-vat-return-0047 / ## Rates, bands and thresholds / 92 | **Start-up franchise: literal law and administrative conflict.** CGI art. 293 D, III literally prorates the ceilings named in art. 293 B, I and I bis, by the fraction of the year remaining at the activity start. On that literal worksheet, a goods business starting on 1 July 2026 has 184/365 of the year: the EUR 93,500 current-year ceiling becomes EUR 47,134.246575... before any assessment rounding, and EUR 50,000 turnover exceeds it. The retained DGFiP regimes page instead expressly grants the first-year franchise up to the unscaled EUR 93,500 / EUR 41,250, so its worksheet does not find that overrun. It then prorates those higher ceilings to test the next year. Service-public F21746 expressly annualises for the following year; its printed example exceeds both the basic and higher limits and cannot distinguish them. With EUR 45,000 from that same start date, annualised turnover is EUR 89,266.304347..., above EUR 85,000 but below EUR 93,500. The statute and those administrative statements have not been reconciled here. Keep both calculations and the actual start date, qualifying turnover and dated sales; this Guide does not decide the first-year exemption, next-year basic-versus-higher test or exact VAT start date where those readings disagree. A year-end total alone cannot identify the overrun transaction. The turnover composition and capital-asset-disposal exclusion are in art. 293 D, I. | [VAT-Q003](#vat-q003); [VAT-Q004](#vat-q004); [VAT-Q005](#vat-q005) | Explicit unresolved statutory/administrative startup conflict; worksheet numbers are labelled conditional fixtures, not a selected filing ruling. |
| france-vat-return-0048 / ## Rates, bands and thresholds / 94 | **Where two official pages disagree.** The impots.gouv.fr page "Les régimes d'imposition à la TVA" (last modified 21 May 2026) still prints EUR 840,000 and EUR 254,000 as the régime simplifié limits. Those are the 2023-2025 values. The law settles it: CIBS art. L. 162-4 sets base amounts of EUR 818,000 and EUR 247,000 for 2020 to 2022 and indexes them on inflation every three years, rounded to the nearest thousand euros, and CIBS art. A. 162-7, as amended by the arrêté of 27 January 2026 (in force from 29 January 2026), fixes the 2026 amounts at EUR 945,000 / 1,040,000 and EUR 286,000 / 323,000. The BOFiP barème of 1 July 2026 and service-public F23566 give the same figures. Use the 2026 values. | [VAT-Q049](#vat-q049); [VAT-Q050](#vat-q050); [ROOT-VAT-D008](#root-vat-d008); [ROOT-VAT-D009](#root-vat-d009); [ROOT-VAT-D010](#root-vat-d010); [ROOT-VAT-D011](#root-vat-d011) |  |
| france-vat-return-0051 / ## The taxable base / 102 | &#124; A1 &#124; Taxable sales and services, net &#124; | [VAT-Q051](#vat-q051); [VAT-Q041](#vat-q041) |  |
| france-vat-return-0052 / ## The taxable base / 103 | &#124; A2 &#124; Other taxable operations: disposals of fixed assets, self-supplies, and purchases where the buyer is liable, including construction work received from a subcontractor (CGI art. 283-2 nonies) &#124; | [VAT-Q052](#vat-q052); [VAT-Q035](#vat-q035) |  |
| france-vat-return-0053 / ## The taxable base / 104 | &#124; A3 &#124; Services bought from a supplier not established in France (CGI art. 283-2), EU or non-EU alike &#124; | [VAT-Q053](#vat-q053); [VAT-Q035](#vat-q035) |  |
| france-vat-return-0054 / ## The taxable base / 105 | &#124; A4 &#124; Imports other than petroleum products, net &#124; | [VAT-Q054](#vat-q054); [VAT-Q035](#vat-q035) |  |
| france-vat-return-0055 / ## The taxable base / 106 | &#124; A5 &#124; Exits from a suspensive regime &#124; | [VAT-Q055](#vat-q055); [VAT-Q035](#vat-q035) |  |
| france-vat-return-0056 / ## The taxable base / 107 | &#124; B1 &#124; Petroleum products released for consumption &#124; | [VAT-Q056](#vat-q056); [VAT-Q036](#vat-q036) |  |
| france-vat-return-0057 / ## The taxable base / 108 | &#124; B2 &#124; Intra-EU acquisitions of goods, net &#124; | [VAT-Q057](#vat-q057); [VAT-Q036](#vat-q036) |  |
| france-vat-return-0058 / ## The taxable base / 109 | &#124; B3 &#124; Electricity, gas, heat or cold taxable in France &#124; | [VAT-Q058](#vat-q058); [VAT-Q036](#vat-q036) |  |
| france-vat-return-0059 / ## The taxable base / 110 | &#124; B4 &#124; Goods or services from a taxable person not established in France (CGI art. 283-1) &#124; | [VAT-Q059](#vat-q059); [VAT-Q036](#vat-q036) |  |
| france-vat-return-0060 / ## The taxable base / 111 | &#124; B5 &#124; Positive correction amounts on the taxed side, for example eligible customer credit notes; not negative taxable sales. See the correction method below &#124; | [VAT-Q060](#vat-q060); [VAT-Q029](#vat-q029) |  |
| france-vat-return-0061 / ## The taxable base / 112 | &#124; E1 &#124; Exports outside the EU &#124; | [VAT-Q037](#vat-q037); [VAT-Q033](#vat-q033); [VAT-Q024](#vat-q024); [VAT-Q025](#vat-q025) |  |
| france-vat-return-0062 / ## The taxable base / 113 | &#124; E2 &#124; Other non-taxable operations, including services to a customer established abroad and a subcontractor's construction work under art. 283-2 nonies &#124; | [VAT-Q037](#vat-q037); [VAT-Q033](#vat-q033); [VAT-Q024](#vat-q024); [VAT-Q025](#vat-q025) |  |
| france-vat-return-0063 / ## The taxable base / 114 | &#124; E3 &#124; Distance sales taxable in another EU state &#124; | [VAT-Q037](#vat-q037); [VAT-Q033](#vat-q033); [VAT-Q024](#vat-q024); [VAT-Q025](#vat-q025) |  |
| france-vat-return-0064 / ## The taxable base / 115 | &#124; E4 &#124; Imports, non-taxed side &#124; | [VAT-Q038](#vat-q038) |  |
| france-vat-return-0065 / ## The taxable base / 116 | &#124; F1 &#124; Intra-EU acquisitions not taxable in France (never the counterpart of B2) &#124; | [VAT-Q038](#vat-q038) |  |
| france-vat-return-0066 / ## The taxable base / 117 | &#124; F2 &#124; Zero-rated intra-EU supplies of goods to a taxable customer &#124; | [VAT-Q034](#vat-q034); [VAT-Q039](#vat-q039) |  |
| france-vat-return-0067 / ## The taxable base / 118 | &#124; F6 &#124; Purchases free of tax (achats en franchise) &#124; | [VAT-Q039](#vat-q039) |  |
| france-vat-return-0068 / ## The taxable base / 119 | &#124; F8 &#124; Positive correction amounts on the non-taxed side; do not change the other frame-A amounts for the same correction &#124; | [VAT-Q030](#vat-q030) |  |
| france-vat-return-0069 / ## The taxable base / 120 | &#124; 08 / 09 / 9B &#124; Base and tax, mainland: 20% / 5.5% / 10% &#124; | [VAT-Q061](#vat-q061); [VAT-Q062](#vat-q062); [VAT-Q063](#vat-q063) |  |
| france-vat-return-0070 / ## The taxable base / 121 | &#124; 10 / 11 &#124; Base and tax, overseas departments: 8.5% / 2.1% &#124; | [VAT-Q064](#vat-q064); [VAT-Q065](#vat-q065) |  |
| france-vat-return-0071 / ## The taxable base / 122 | &#124; T1, T2, TC, T3–T6 &#124; Overseas particular rates (1.75%, 1.05%), Corsica (13%, 10%, 2.1%, 0.9%), mainland particular rate 2.1% (T6) &#124; | [VAT-Q066](#vat-q066); [VAT-Q067](#vat-q067); [VAT-Q068](#vat-q068); [VAT-Q069](#vat-q069); [VAT-Q070](#vat-q070); [VAT-Q071](#vat-q071); [VAT-Q072](#vat-q072) |  |
| france-vat-return-0072 / ## The taxable base / 123 | &#124; P1, P2 &#124; Petroleum products, 20% and 13% &#124; | [VAT-Q073](#vat-q073); [VAT-Q074](#vat-q074) |  |
| france-vat-return-0073 / ## The taxable base / 124 | &#124; I1 to I6 &#124; Import VAT by rate: 20%, 10%, 8.5%, 5.5%, 2.1%, 1.05% &#124; | [VAT-Q075](#vat-q075); [VAT-Q076](#vat-q076); [VAT-Q077](#vat-q077); [VAT-Q078](#vat-q078); [VAT-Q079](#vat-q079); [VAT-Q080](#vat-q080) |  |
| france-vat-return-0074 / ## The taxable base / 125 | &#124; 15 &#124; VAT previously deducted to be paid back &#124; | [VAT-Q081](#vat-q081); [VAT-Q041](#vat-q041) |  |
| france-vat-return-0075 / ## The taxable base / 126 | &#124; 16 &#124; Total gross VAT due &#124; | [VAT-Q082](#vat-q082); [VAT-Q041](#vat-q041) |  |
| france-vat-return-0076 / ## The taxable base / 127 | &#124; 17 / 18 &#124; Memo lines: of which on intra-EU acquisitions / of which on operations to Monaco &#124; | [VAT-Q040](#vat-q040); [ROOT-VAT-W020](#root-vat-w020); [ROOT-VAT-W021](#root-vat-w021) |  |
| france-vat-return-0077 / ## The taxable base / 128 | &#124; 19 &#124; Deductible VAT on fixed assets &#124; | [VAT-Q083](#vat-q083); [VAT-Q027](#vat-q027) |  |
| france-vat-return-0078 / ## The taxable base / 129 | &#124; 20 &#124; Deductible VAT on other goods and services &#124; | [VAT-Q084](#vat-q084); [VAT-Q027](#vat-q027) |  |
| france-vat-return-0079 / ## The taxable base / 130 | &#124; 21 &#124; Other VAT to deduct &#124; | [VAT-Q085](#vat-q085); [VAT-Q041](#vat-q041) |  |
| france-vat-return-0080 / ## The taxable base / 131 | &#124; 22 &#124; Credit carried from line 27 of the previous return &#124; | [VAT-Q086](#vat-q086); [VAT-Q041](#vat-q041) |  |
| france-vat-return-0081 / ## The taxable base / 132 | &#124; 23 &#124; Total deductible VAT &#124; | [VAT-Q087](#vat-q087); [VAT-Q041](#vat-q041) |  |
| france-vat-return-0082 / ## The taxable base / 133 | &#124; 24 / 2E &#124; Memo: of which on imports / on petroleum products &#124; | [VAT-Q041](#vat-q041); [ROOT-VAT-W026](#root-vat-w026); [ROOT-VAT-W027](#root-vat-w027) |  |
| france-vat-return-0083 / ## The taxable base / 134 | &#124; 25 / TD &#124; Credit (line 23 less 16) / VAT due (line 16 less 23) &#124; | [VAT-Q088](#vat-q088); [VAT-Q041](#vat-q041) |  |
| france-vat-return-0084 / ## The taxable base / 135 | &#124; 26 &#124; Refund asked for on form 3519 &#124; | [VAT-Q089](#vat-q089); [VAT-Q041](#vat-q041) |  |
| france-vat-return-0085 / ## The taxable base / 136 | &#124; 27 &#124; Credit carried forward, to line 22 of the next return &#124; | [VAT-Q090](#vat-q090); [VAT-Q041](#vat-q041) |  |
| france-vat-return-0086 / ## The taxable base / 137 | &#124; 28 / 29 / 32 &#124; Net VAT due / assimilated taxes from annex 3310 A / total to pay &#124; | [VAT-Q041](#vat-q041); [VAT-Q091](#vat-q091); [VAT-Q092](#vat-q092); [VAT-Q093](#vat-q093) |  |
| france-vat-return-0087 / ## The taxable base / 139 | **Numeric identifiers on the retained 2026 CA3 form.** These identify printed form fields, not additional tax tests: A1 0979; A2 0981; A3 0044; A4 0056; A5 0051; B1 0048; B2 0031; B3 0030; B4 0040; B5 0036; E1 0032; E2 0033; E3 0047; E4 0052; F1 0055; F2 0034; F6 0037; F8 0039; 15 0600; 17 0035; 18 0038; 19 0703; 20 0702; 21 0059; 22 8001; 24 0710; 2E 0711; 25 0705; TD 8900; 26 8002; 27 8003; 28 8901; 29 9979; 32 9992. Use the visible line labels and the applicable current form when transferring data; the identifiers do not replace the ordinary line-selection and adjustment rules. | [ROOT-VAT-W001](#root-vat-w001); [ROOT-VAT-W002](#root-vat-w002); [ROOT-VAT-W003](#root-vat-w003); [ROOT-VAT-W004](#root-vat-w004); [ROOT-VAT-W005](#root-vat-w005); [ROOT-VAT-W006](#root-vat-w006); [ROOT-VAT-W007](#root-vat-w007); [ROOT-VAT-W008](#root-vat-w008); [ROOT-VAT-W009](#root-vat-w009); [ROOT-VAT-W010](#root-vat-w010); [ROOT-VAT-W011](#root-vat-w011); [ROOT-VAT-W012](#root-vat-w012); [ROOT-VAT-W013](#root-vat-w013); [ROOT-VAT-W014](#root-vat-w014); [ROOT-VAT-W015](#root-vat-w015); [ROOT-VAT-W016](#root-vat-w016); [ROOT-VAT-W017](#root-vat-w017); [ROOT-VAT-W018](#root-vat-w018); [ROOT-VAT-W019](#root-vat-w019); [ROOT-VAT-W020](#root-vat-w020); [ROOT-VAT-W021](#root-vat-w021); [ROOT-VAT-W022](#root-vat-w022); [ROOT-VAT-W023](#root-vat-w023); [ROOT-VAT-W024](#root-vat-w024); [ROOT-VAT-W025](#root-vat-w025); [ROOT-VAT-W026](#root-vat-w026); [ROOT-VAT-W027](#root-vat-w027); [ROOT-VAT-W028](#root-vat-w028); [ROOT-VAT-W029](#root-vat-w029); [ROOT-VAT-W030](#root-vat-w030); [ROOT-VAT-W031](#root-vat-w031); [ROOT-VAT-W032](#root-vat-w032); [ROOT-VAT-W033](#root-vat-w033); [ROOT-VAT-W034](#root-vat-w034) |  |
| france-vat-return-0088 / ## The taxable base / 141 | Line 18 is a Monaco memo line, not the line for self-assessed EU services. A credit at line 25 does not excuse paying the assimilated taxes at line 29. | [VAT-Q040](#vat-q040); [VAT-Q041](#vat-q041) |  |
| france-vat-return-0089 / ## The taxable base / 143 | **CA3 completion, rounding and refunds.** The 2026 notice requires one return for each reporting period, including a “Néant” return when there were no operations; do not combine several months or quarters on one return. Keep precise invoice values in the working paper. Round reported taxable bases, corresponding VAT and the deductible total for each of lines 19 and 20 to the nearest euro: below EUR 0.50 is discarded, EUR 0.50 or more becomes EUR 1. Thus EUR 101.49 becomes EUR 101 and EUR 101.50 becomes EUR 102; do not assume a per-invoice rounding method from that return-stage rule. For a requested line-26 refund, the notice gives a EUR 760 minimum for monthly or quarterly requests for January–November or the first three quarters, and EUR 150 for December or the fourth quarter. These are amount and period tests, not automatic approval of every claim: establish ordinary refund conditions and file the request on 3519. Carry only the unrequested credit to line 27 and the next line 22; do not both refund and carry the same amount. See the [2026 notice](https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf), sections I and IV. | [VAT-Q026](#vat-q026); [VAT-Q027](#vat-q027); [VAT-Q028](#vat-q028) |  |
| france-vat-return-0090 / ## The taxable base / 145 | **The CA12 (form 3517-S-SD, 2026)** has its own numbering. Lines 5A, 06, 6C and 07 carry the standard, reduced, intermediate and overseas standard rates; line 19 is total gross VAT; line 20 deductions on invoices, 21 the flat-rate deduction, 22 their total; line 23 VAT on fixed assets; line 24 the credit brought in; line 26 total deductible; line 28 VAT due; line 29 credit; line 30 instalments. Line 57 is next year's instalment base: line 16 less lines 11, 12 and 22, which is before VAT on fixed assets. Below EUR 150 a year-end credit is refundable only on a disposal, death or entry into a VAT group; otherwise carry it to next year (line 51) or set it against the next instalment (line 52). The selected 2026 completion notice is now accessible and was read for these ordinary entries. For line 30, distinguish instalments actually paid (column 1) from those still payable (column 2), using the instalments exigible within the covered VAT year. If the expected instalment was below EUR 550 for July or EUR 400 for December, show only what was actually paid in column 1; do not enter the unpaid balance in column 2. Keep credit used against instalments at AE separate from an unrefunded, unimputed opening credit at line 24; do not carry or refund the same amount twice. See the [selected 2026 CA12 notice](https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5424.pdf), lines 24, AE, 30 and 57 and frame VII. | [VAT-Q042](#vat-q042); [VAT-Q043](#vat-q043); [VAT-Q044](#vat-q044); [ROOT-VAT-C018](#root-vat-c018); [ROOT-VAT-C019](#root-vat-c019); [ROOT-VAT-C020](#root-vat-c020); [ROOT-VAT-C021](#root-vat-c021) |  |
| france-vat-return-0092 / ## The taxable base / 149 | - Ordinary general-rule B2B services taxable in France from a supplier not established there, with no participating French establishment: use A3, the actual output rate block and the eligible deduction at line 20 or 19 according to actual expensing/capitalisation (CGI arts. 259-1° and 283-2). First check the service and any special place rules. Net nil requires full ordinary deduction entitlement. VAT wrongly charged abroad is not French input tax; obtain the supplier correction and assess the lawful foreign-recovery route separately. | [VAT-Q018](#vat-q018); [VAT-Q021](#vat-q021); [VAT-Q022](#vat-q022); [VAT-Q027](#vat-q027); [VAT-Q033](#vat-q033); [VAT-Q035](#vat-q035) |  |
| france-vat-return-0093 / ## The taxable base / 150 | - Intra-EU acquisitions of goods: base on B2, tax in the rate block and again as a memo at line 17, deduction at line 20 or 19. | [VAT-Q034](#vat-q034); [VAT-Q036](#vat-q036) |  |
| france-vat-return-0094 / ## The taxable base / 151 | - Imports: import VAT is self-assessed on the CA3 (base on A4, tax at I1 to I6, deduction at line 20 or 19 and memo at line 24). The return is pre-filled with customs data: reconcile it with the client's import records. | [VAT-Q027](#vat-q027); [VAT-Q035](#vat-q035); [VAT-Q075](#vat-q075); [VAT-Q076](#vat-q076); [VAT-Q077](#vat-q077); [VAT-Q078](#vat-q078); [VAT-Q079](#vat-q079); [VAT-Q080](#vat-q080) |  |
| france-vat-return-0095 / ## The taxable base / 152 | - Domestic reverse charges: construction subcontracting (art. 283-2 nonies), scrap and waste (283-2 sexies), emission quotas (283-2 septies), electronic communications services (283-2 octies), gas and electricity (283-2 quinquies). Flag these for the reviewer. | [VAT-Q035](#vat-q035); [ROOT-VAT-D012](#root-vat-d012); [ROOT-VAT-D013](#root-vat-d013); [ROOT-VAT-D014](#root-vat-d014); [ROOT-VAT-D015](#root-vat-d015); [ROOT-VAT-D016](#root-vat-d016) | Named categories are referral flags; actual recipient/category conditions in clauses, no full specialist reverse-charge workflow claimed. |
| france-vat-return-0096 / ## The taxable base / 154 | **Exempt and zero-rated.** Exports go to E1 with export evidence. Intra-EU supplies of goods go to F2: check the customer's VAT number on VIES before invoicing without VAT, keep transport proof, and file the état récapitulatif. General-rule B2B services actually located abroad go to E2; first check supply classification and the special place rules, and apply the DES conditions below rather than treating every foreign business customer as enough. Where an exemption without input credit actually applies, charge no output VAT and exclude the related input tax to that extent. Establish the precise medical/education conditions under CGI art. 261, financial/insurance conditions and eligible options under arts. 261 C/260 B/260 C, and rental conditions/options under arts. 261 D/260; a profession or supplier label does not establish exemption. A mixed business applies the actual deduction-coefficient rules in CGI annexe II arts. 205–207. Before applying a proportional business-use deduction, test art. 206, IV-2-1°: use of the good or service more than 90% for purposes foreign to the business makes its admission coefficient zero, so none of its input VAT is deductible. Exactly 90% does not trigger that exclusion; the remaining coefficient and ordinary invoice/eligibility conditions still apply. Refer the detailed partial-exemption calculation to an expert-comptable. | [VAT-Q018](#vat-q018); [VAT-Q021](#vat-q021); [VAT-Q033](#vat-q033); [VAT-Q034](#vat-q034); [VAT-Q037](#vat-q037); [VAT-Q039](#vat-q039); [ROOT-VAT-R010](#root-vat-r010); [ROOT-VAT-R011](#root-vat-r011); [ROOT-VAT-R012](#root-vat-r012); [ROOT-VAT-R013](#root-vat-r013); [ROOT-VAT-R014](#root-vat-r014); [ROOT-VAT-R015](#root-vat-r015); [ROOT-VAT-C013](#root-vat-c013); [ROOT-VAT-C014](#root-vat-c014); [ROOT-VAT-C015](#root-vat-c015); [ROOT-VAT-C016](#root-vat-c016); [ROOT-VAT-C017](#root-vat-c017); [VAT-Q008](#vat-q008) |  |
| france-vat-return-0099 / ## The taxable base / 160 | &#124; Vehicles designed to carry people or for mixed use, their parts and upkeep &#124; Not deductible. The test is how the vehicle was designed, judged at purchase or lease, not how it is used. Leisure quads and cycles, electrically assisted or not, are caught unless specifically fitted for the exclusive carriage of goods (https://bofip.impots.gouv.fr/bofip/1192-PGP.html, § 45) &#124; https://bofip.impots.gouv.fr/bofip/1192-PGP.html &#124; | [VAT-Q008](#vat-q008); [VAT-Q012](#vat-q012); [VAT-Q013](#vat-q013) |  |
| france-vat-return-0100 / ## The taxable base / 161 | &#124; Exceptions to the vehicle exclusion &#124; Vehicles bought for resale new; taxis, VTC and public passenger transport used exclusively for it; driving schools; hearses used exclusively by undertakers; vehicle hire businesses; vehicles with more than eight seats besides the driver carrying staff; horse transport vehicles from 2024; ski-domain all-terrain vehicles; aircraft for paid air services; racing sailboats. Apply the conditions of the individual exception, rather than a universal exclusive-use test. CGI annexe II art. 206, IV-2-6° expressly imposes exclusive use for the driving-instruction, ski and public-transport limbs, with the separate BOFiP conditions and limited combined-use tolerances; it does not add that same condition to every resale, rental or staff-bus case. For public transport, the accessory-freight tolerance has its own limits (§130–150); paid aircraft services require the actual use and aviation records (§380–460) &#124; same &#124; | [VAT-Q008](#vat-q008); [VAT-Q014](#vat-q014); [VAT-Q019](#vat-q019); [VAT-Q020](#vat-q020) |  |
| france-vat-return-0101 / ## The taxable base / 162 | &#124; Fuel &#124; Shares in the rates table. The limit applies only to products used as fuel to propel vehicles and engines; petrol, diesel and E85 used in tests for manufacturing engines are outside it. Liquefied petroleum gases (butane, propane and similar) and natural gas in gaseous form follow the ordinary rules (https://bofip.impots.gouv.fr/bofip/1194-PGP.html, § 40 and 160). Electric charging is not on the fuel list: ordinary rules apply once the vehicle's own exclusion is settled &#124; https://bofip.impots.gouv.fr/bofip/1194-PGP.html &#124; | [ROOT-VAT-C022](#root-vat-c022); [ROOT-VAT-C023](#root-vat-c023); [ROOT-VAT-C024](#root-vat-c024); [VAT-Q016](#vat-q016) |  |
| france-vat-return-0102 / ## The taxable base / 163 | &#124; Passenger transport bought by the business &#124; No deduction for ordinary ad-hoc staff fares. CGI annexe II art. 206, IV-2-5° excludes passenger transport and accessories, except services for a public passenger-transport undertaking or under a permanent staff-transport contract bringing employees to work; establish ordinary deduction conditions too &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069569/LEGISCTA000006179225/2026-10-29 &#124; | [VAT-Q008](#vat-q008) |  |
| france-vat-return-0103 / ## The taxable base / 164 | &#124; Jet fuel &#124; Excluded for aircraft/engines without deduction rights, including hired aircraft where the hire VAT cannot be deducted. BOFiP §220–240 identifies exceptions for exclusive public passenger transport, freight aircraft, qualifying specialised helicopters and exclusive flying instruction; establish the actual aircraft/use and ordinary deduction conditions &#124; https://bofip.impots.gouv.fr/bofip/1194-PGP.html &#124; | [VAT-Q016](#vat-q016) |  |
| france-vat-return-0104 / ## The taxable base / 165 | &#124; Housing directors or staff free of charge &#124; Not deductible, including buying or renting the premises. The actual on-site guarding, security or surveillance exception requires lodging necessary for those functions on the worksite or business premises; ordinary function housing alone is insufficient. For mixed lodging of staff/directors and third parties whose costs open deduction rights, BOFiP allows the admission coefficient as eligible third-party headcount / total people on the invoice, with their identity and status recorded; ordinary deduction conditions still apply &#124; https://bofip.impots.gouv.fr/bofip/1190-PGP.html &#124; | [VAT-Q017](#vat-q017) |  |
| france-vat-return-0105 / ## The taxable base / 166 | &#124; Gifts and goods given away &#124; Excluded from deduction except qualifying very-low-value goods whose unit value does not exceed EUR 73 including all taxes, per object and per year for the same beneficiary (CGI annexe IV, art. 28-00 A; ordinary deduction conditions still apply). The actual published consolidated text was read on 29 October; its returned section is current at 9 October 2026, while the direct current-article route failed &#124; https://bofip.impots.gouv.fr/bofip/1196-PGP.html ; https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006179484/ &#124; | [VAT-Q008](#vat-q008); [ROOT-VAT-C007](#root-vat-c007) |  |
| france-vat-return-0106 / ## The taxable base / 167 | &#124; Private use by owners, directors or staff &#124; The personal portion is not deductible. If the good or service is used more than 90% for purposes foreign to the business, its admission coefficient is zero and the whole input claim is excluded (CGI annexe II art. 206, IV-2-1°). Otherwise apply the actual deduction coefficients and other ordinary conditions, not an assumed full entitlement &#124; https://bofip.impots.gouv.fr/bofip/1194-PGP.html ; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069569/LEGISCTA000006179225/2026-10-29 &#124; | [VAT-Q018](#vat-q018); [ROOT-VAT-C023](#root-vat-c023); [VAT-Q008](#vat-q008) |  |
| france-vat-return-0107 / ## The taxable base / 168 | &#124; Restaurant meals &#124; Not excluded by name. Deductible only where incurred for the business, with the purpose and guests documented &#124; CGI annexe II, art. 206 &#124; | [VAT-Q018](#vat-q018); [VAT-Q021](#vat-q021) |  |
| france-vat-return-0108 / ## The taxable base / 169 | &#124; Advertising for alcoholic drinks &#124; Deductible under the ordinary rules from 21 February 2026 (CGI art. 273 septies E, LF 2026 art. 91) &#124; https://bofip.impots.gouv.fr/bofip/15011-PGP.html &#124; | [ROOT-VAT-D019](#root-vat-d019); [ROOT-VAT-D020](#root-vat-d020) |  |
| france-vat-return-0109 / ## The taxable base / 170 | &#124; Fixed assets &#124; Line 19 for an actual capital asset, not line 20. For ordinary annual adjustments, CGI annexe II art. 207, II uses initial VAT × (current deduction coefficient − reference deduction coefficient) / 5 for movable assets or / 20 for immovable assets, over the statutory five-/twenty-year period including its starting year. The annual gate compares current versus reference products of the assujettissement and taxation coefficients: an absolute difference of exactly 0.10 does not trigger adjustment; it must exceed 0.10. Ordinary annual settlement is before 25 April of the following year. Reference assujettissement zero and the statutory pre-1996 immovable cases are excluded; disposal and the other global-adjustment events in art. 207, III have separate conditions. The EUR 500 small-equipment expense tolerance is optional and limited to qualifying categories: transport equipment is excluded, inseparable components are aggregated, and office furniture normally requires small-number routine replacement; initial or complete furniture equipment is excluded unless its total remains within EUR 500. Use line 20 only for qualifying costs actually expensed and line 19 for actual capitalisation, subject in either case to ordinary deduction eligibility (https://bofip.impots.gouv.fr/bofip/2109-PGP.html: "en considération du prix global de l'ensemble des éléments") &#124; https://bofip.impots.gouv.fr/bofip/2109-PGP.html &#124; | [VAT-Q009](#vat-q009); [VAT-Q010](#vat-q010); [VAT-Q011](#vat-q011); [VAT-Q015](#vat-q015); [VAT-Q027](#vat-q027) |  |
| france-vat-return-0110 / ## The taxable base / 172 | **When decision facts are missing.** Obtain the actual supply, billing entity and country, customer status and location, invoice tax, business-use share and any relevant exception. Keep the tax code unresolved and obtain the missing fact or document before selecting a rate, country, consumer treatment, self-assessment line or final deduction result. Do not choose 20%, France, consumer status or A3 solely because the corresponding fact is unknown. Hold unsupported input-tax claims until the ordinary eligibility and invoice evidence are established; a temporary hold is not a determination that the cost is permanently blocked. The supplier-name patterns below are only pre-classification aids and do not supply missing tax facts. | [VAT-Q018](#vat-q018); [VAT-Q021](#vat-q021); [VAT-Q022](#vat-q022); [VAT-Q024](#vat-q024); [VAT-Q025](#vat-q025) | House evidence-hold procedure applying actual eligibility; unknown facts do not create a statutory rate/country/tax result. |
| france-vat-return-0111 / ## The taxable base / 174 | **Supplier and bank-line patterns (pre-classifier).** Match the counterparty name only to choose the relevant checks, most specific first; if nothing matches, apply the rules above. Every treatment below is conditional on the proved supply, actual billing entity/establishment, tax regime, lawful invoice tax and business-use facts. The name, an IBAN or printed VAT alone cannot establish exemption, a rate, reverse charge or recovery. Record unresolved facts and obtain the evidence before final coding. | [VAT-Q018](#vat-q018); [VAT-Q021](#vat-q021); [VAT-Q022](#vat-q022) | House recognition workflow, conditional throughout; counterparty aliases are fixture patterns, not statutory categories. |
| france-vat-return-0113 / ## The taxable base / 178 | &#124; Bank fees and interest (BNP, Société Générale, Crédit Agricole, LCL, BPCE, Caisse d'Épargne, La Banque Postale, CIC, Crédit Mutuel; fee lines of Qonto, Revolut, Wise, N26); INTERETS, AGIOS; PRET, EMPRUNT &#124; Establish the actual financial operation and any applicable taxation option under CGI arts. 261 C, 260 B and 260 C. Exclude a proved exempt operation or principal movement, not every debit from a bank. Separate taxable subscriptions/other services and apply the ordinary lawful-tax/invoice/use tests; a printed tax amount alone cannot create a permitted option. &#124; | [ROOT-VAT-R010](#root-vat-r010); [ROOT-VAT-R012](#root-vat-r012); [ROOT-VAT-R013](#root-vat-r013); [ROOT-VAT-R014](#root-vat-r014); [ROOT-VAT-R015](#root-vat-r015); [VAT-Q018](#vat-q018); [VAT-Q021](#vat-q021) |  |
| france-vat-return-0114 / ## The taxable base / 179 | &#124; DGFIP, TRESOR PUBLIC, IMPOTS.GOUV, URSSAF, CPAM, SSI, France Travail, CIPAV, CNAV, GREFFE, CFE, CVAE, PREFECTURE, INPI, CCI, CMA &#124; Exclude proved tax settlements, statutory social contributions and other documented non-supply transfers. A public-body, registry or chamber name alone does not prove that the actual service or fee is outside VAT; inspect the document and classify any supply on its actual facts. &#124; | [ROOT-VAT-C002](#root-vat-c002) | Proved nonsupply transfer facts; labels only prompt questions. |
| france-vat-return-0115 / ## The taxable base / 180 | &#124; SALAIRE, PAIE, MUTUELLE (employee), DIVIDENDE, APPORT, VIREMENT INTERNE &#124; Exclude amounts actually proved to be wages, employee social contributions, dividend distributions, capital injections or own-account transfers. A label is a prompt to verify the transaction, not evidence that an unidentified customer receipt is outside VAT. &#124; | [ROOT-VAT-C002](#root-vat-c002) | Proved wages/capital/own transfers; labels alone insufficient. |
| france-vat-return-0116 / ## The taxable base / 181 | &#124; EDF, TotalEnergies, Orange, Free, SFR, Bouygues Telecom, OVHcloud &#124; Identify the actual product, billing entity and lawful rate. For an ordinary French supply actually subject to 20%, use that tax only to the deductible business extent at line 20, or line 19 if capitalised. Read the invoice's gas/water components and any applicable specific rate; the supplier brand does not fix them. &#124; | [ROOT-VAT-R001](#root-vat-r001); [ROOT-VAT-R017](#root-vat-r017); [VAT-Q018](#vat-q018); [VAT-Q021](#vat-q021) |  |
| france-vat-return-0117 / ## The taxable base / 182 | &#124; AXA, MAIF, MACIF, MATMUT, MAAF, Groupama, Generali, AG2R, Malakoff Humanis &#124; Exclude a proved insurance/reinsurance operation or qualifying related broker/intermediary service under CGI art. 261 C, 2°. Do not extend the exemption to every unrelated service merely because the provider is an insurer. &#124; | [ROOT-VAT-R011](#root-vat-r011) |  |
| france-vat-return-0118 / ## The taxable base / 183 | &#124; La Poste standard mail &#124; Check whether the actual operation falls within the qualifying universal-postal-service exemption under CGI art. 261, 4-11°. Do not classify every parcel or courier service from La Poste, Colissimo, Chronopost, DHL, Mondial Relay, UPS, TNT or FedEx by the brand alone. For a taxable service, establish the actual rate and billing establishment before selecting domestic or A3 treatment. &#124; | [ROOT-VAT-R016](#root-vat-r016) |  |
| france-vat-return-0119 / ## The taxable base / 184 | &#124; SNCF, Ouigo, RATP, taxis, G7, Bolt, Heetch, Uber rides, Air France domestic &#124; Where the domestic output rate is 10%, this does not itself allow input recovery. Ordinary ad-hoc employee passenger travel: no input VAT deduction under CGI annexe II art. 206, IV-2-5°. Exceptions require transport supplied for a public passenger-transport undertaking or under a permanent contract to bring staff to work, plus the ordinary deduction conditions. International flights: exclude &#124; | [ROOT-VAT-R007](#root-vat-r007); [VAT-Q008](#vat-q008) |  |
| france-vat-return-0120 / ## The taxable base / 185 | &#124; Motorway tolls (Vinci, Sanef, APRR) &#124; 20%; line 20 only where ordinary business-use and invoice deduction conditions are met &#124; | [ROOT-VAT-R001](#root-vat-r001); [VAT-Q018](#vat-q018); [VAT-Q021](#vat-q021) |  |
| france-vat-return-0121 / ## The taxable base / 186 | &#124; Supermarkets (Carrefour, Auchan, Leclerc, Lidl, Monoprix, etc.) and restaurants &#124; Obtain the actual goods/services, invoiceVAT, business purpose and users. Neither a supermarket nor restaurant name establishes personal use, a permanent block or a catering-only entitlement. Apply the ordinary deduction conditions and the actual product-specific exclusions; hold an unsupported claim pending evidence. &#124; | [ROOT-VAT-R002](#root-vat-r002); [ROOT-VAT-R009](#root-vat-r009); [VAT-Q018](#vat-q018); [VAT-Q021](#vat-q021) |  |
| france-vat-return-0122 / ## The taxable base / 187 | &#124; Google, Microsoft, Adobe, Meta, LinkedIn, Spotify, Dropbox, Slack, Atlassian, Zoom (EU billing entities); Notion, OpenAI, Anthropic, Figma, Canva, Twilio, GitHub, HubSpot (non-EU or check); AWS EMEA SARL &#124; A3 plus line 20 (self-assessment). Use the domestic route only if the French TVA was legally chargeable and the invoice and ordinary deduction conditions hold. A French VAT number or printed TVA alone does not displace reverse charge. For a qualifying French B2B service from a supplier without a participating French establishment, apply the legally required self-assessment, request correction/refund of wrongly invoiced VAT, and do not deduct that wrong tax (CGI art. 271, II-1-a and 283-2; BOFiP https://bofip.impots.gouv.fr/bofip/1111-PGP.html, §55–60 and https://bofip.impots.gouv.fr/bofip/1531-PGP.html, §80) &#124; | [VAT-Q021](#vat-q021); [VAT-Q022](#vat-q022); [VAT-Q027](#vat-q027); [VAT-Q035](#vat-q035) |  |
| france-vat-return-0123 / ## The taxable base / 188 | &#124; Amazon, Etsy, eBay marketplace fees &#124; A3 plus line 20 where billed from outside France (CA3 notice n° 3310 NOT-CA3-SD: line A3 is "prestations de services fournies par un prestataire non établi en France et imposables en France sur le fondement des articles 259-1° et 283-2 du CGI"); the sales themselves go to A1 at the applicable rate (or E3, distance sales taxable in the member state of arrival under the qualified current-and-previous-year EUR 10,000 selector below or by option; OSS is an available declaration route where its conditions are met: same notice, line E3) &#124; | [VAT-Q021](#vat-q021); [VAT-Q022](#vat-q022); [VAT-Q027](#vat-q027); [VAT-Q035](#vat-q035) |  |
| france-vat-return-0124 / ## The taxable base / 189 | &#124; Stripe, PayPal transaction fees &#124; Establish whether the actual item is a qualifying exempt payment/financial operation, an eligible operation under a valid taxation option, or a separate taxable subscription/technical service. Do not assume exemption from Stripe/PayPal or country from the brand. For SumUp, Square and Zettle too, identify the actual billing entity, service and invoice, then apply the ordinary place/liability/deduction method. &#124; | [ROOT-VAT-R010](#root-vat-r010); [ROOT-VAT-R012](#root-vat-r012); [ROOT-VAT-R013](#root-vat-r013); [ROOT-VAT-R014](#root-vat-r014); [ROOT-VAT-R015](#root-vat-r015); [VAT-Q035](#vat-q035) |  |
| france-vat-return-0125 / ## The taxable base / 190 | &#124; Expert-comptable, avocat, notaire (business), commissaire aux comptes, architecte &#124; Establish the actual supplier regime, service, billing establishment and lawful VAT. An ordinary French professional service actually taxed at 20% follows the general input route only to its deductible business extent, at line 20 or line 19 if capitalised. The profession label does not override franchise, exemption, place or invoice facts. &#124; | [ROOT-VAT-R001](#root-vat-r001); [VAT-Q018](#vat-q018); [VAT-Q021](#vat-q021) |  |
| france-vat-return-0126 / ## The taxable base / 191 | &#124; LOYER COMMERCIAL, SCI with TVA invoiced &#124; Establish whether the supply is bare premises, furnished accommodation or another property service, its residential/business use and actual regime. Qualifying bare-premises rent is ordinarily exempt under CGI art. 261 D, with its exceptions; an eligible business-premises letting can be taxed under a valid art. 260, 2° option. That option is unavailable for bare residential/agricultural premises. Furnished/hotel-type services have their own art. 261 D conditions, so residential or commercial wording alone does not decide exemption or rate. Refer the detailed property treatment. A proved TAXE FONCIERE settlement is not a purchase-VAT invoice. &#124; | [ROOT-VAT-C013](#root-vat-c013); [ROOT-VAT-C014](#root-vat-c014); [ROOT-VAT-C015](#root-vat-c015); [ROOT-VAT-C016](#root-vat-c016); [ROOT-VAT-C017](#root-vat-c017) |  |
| france-vat-return-0127 / ## The taxable base / 192 | &#124; RETRAIT DAB, cash &#124; Ask what the withdrawal funded and reconcile the cash account. A bank withdrawal alone is not a VAT purchase invoice or proof of personal drawings. Claim only actual eligible invoiced underlying purchases; do not invent a rate or permanent exclusion for unidentified cash. &#124; | [VAT-Q018](#vat-q018); [VAT-Q021](#vat-q021) | House question/reconciliation step; no withdrawal-as-drawing presumption. |
| france-vat-return-0128 / ## The taxable base / 194 | Bank-statement reading: French exports are usually semicolon-separated with DD/MM/YYYY dates (Qonto and Revolut use ISO dates). VIR is a transfer, CB a card payment, PRLV a direct debit, CHQ a cheque, REM a cheque deposit, TIP an interbank payment. Keep signed refund/credit-note reversals in the accounting reconciliation, but do not transfer negative amounts blindly to the original CA3 fields: the B5/F8 correction method below uses the return’s prescribed positive entries. For VAT currency conversion, use the latest ECB-published rate at the actual date the VAT becomes due (exigibilité), under CGI art. 266, 1 bis; keep the tax-point and rate evidence. Invoice, supply and receipt dates are not automatically the same tax point. BOFiP §410 also permits the customs conversion method for intra-EU acquisitions if used consistently for all such operations in the year; customs import conversion is separate. See https://bofip.impots.gouv.fr/bofip/140-PGP.html, §380–410. An IBAN prefix shows the bank's country, not the customer's VAT status: check VIES. | [VAT-Q023](#vat-q023); [VAT-Q029](#vat-q029); [VAT-Q030](#vat-q030); [VAT-Q031](#vat-q031); [VAT-Q032](#vat-q032) | CSV/glossary/IBAN recognisers are house aids; legalFX/return corrections source-bound. |
| france-vat-return-0129 / ## The taxable base / 196 | **Questions to raise when a line is ambiguous.** Fuel and vehicle costs (was the vehicle designed for people or goods, and which fuel?); restaurants (who was present and why?); SaaS (legal entity, country, any French TVA charged?); round transfers from the owner's name (sale, capital or loan?); incoming money from individuals or foreign accounts (sale? business or consumer? which country?); large one-off purchases near EUR 500 (asset or expense?); mixed-use phone or home costs (business share?); outgoing transfers to individuals (contractor with invoice, wages, refund or private?); foreign hotels (foreign VAT is not French input VAT; a refund may be claimed in that state); Airbnb income (furnished letting falls in the services band); construction subcontractors (domestic reverse charge?); platform sales on Amazon, Etsy or eBay (apply the qualified current-and-previous-year EUR 10,000 destination selector below, including establishment and goods-dispatch facts; use `eu-vat-directive` R-EU-5 for any applicable OSS route). | [VAT-Q008](#vat-q008); [VAT-Q015](#vat-q015); [VAT-Q018](#vat-q018); [VAT-Q021](#vat-q021); [VAT-Q022](#vat-q022); [VAT-Q024](#vat-q024); [VAT-Q025](#vat-q025); [ROOT-VAT-C013](#root-vat-c013); [ROOT-VAT-C014](#root-vat-c014); [ROOT-VAT-C015](#root-vat-c015) | Intake questions, with source-bound500/10k/actual eligibility facts. |
| france-vat-return-0130 / ## The taxable base / 198 | **Invoices.** At EUR 150 excluding VAT or less, the ordinary simplification in CGI annexe II art. 242 nonies A, II permits omission of the supplier's VAT identification number (I-2°) and the exemption reference (I-12°), subject to the actual exclusions and particulars independently imposed for the operation. It does not generally waive the customer's VAT number or the reverse-charge wording. The statutory distance-goods, exempt intra-EU/new-transport and specified cross-border branches have their own exclusions or simplifications: check the actual operation under II-a to c and BOFiP BOI-TVA-DECLA-30-20-20-20, §20–60, before omitting a particular. Reverse-charge invoices say "Autoliquidation". F31808's supplier/customer-number summary is not the selected statutory rule. From 1 September 2026 (large companies and ETI) and 1 September 2027 (SMEs and micro-enterprises), invoices add four new particulars: the customer's SIREN, the delivery address if different, whether the invoice is for goods, services or both, and "Option pour le paiement de la taxe d'après les débits" where that option was made (service-public F31808 and the actual article's commencement notes). | [ROOT-VAT-Q001](#root-vat-q001); [ROOT-VAT-Q002](#root-vat-q002); [ROOT-VAT-Q003](#root-vat-q003); [ROOT-VAT-Q004](#root-vat-q004); [VAT-Q048](#vat-q048); [ROOT-VAT-C001](#root-vat-c001); [ROOT-VAT-C003](#root-vat-c003) |  |
| france-vat-return-0131 / ## The taxable base / 200 | **Qualitative review checks (OpenAccountants working practice).** Flag unusually large transactions relative to the period, a classification uncertainty that materially changes tax, concentration in one counterparty, repeated unresolved facts, and a large payment/refund position. No statute-derived monetary trip point is asserted. Resolve the supporting facts; an internal review flag is not itself a VAT classification. |  | Qualitative flags without moneytrip points, pre-refresh nativeLF164–174. |
| france-vat-return-0132 / ## The taxable base / 202 | **Input pack (OpenAccountants working practice).** Obtain a bank statement covering the full reporting period, in CSV, PDF or readable text. Add sales and purchase invoices, the legal entity and trading name, written VAT identification, SIREN/SIRET, the prior CA3/CA12 and the invoice register/FEC-compatible export when available. Confirm the regime and full reporting period from the taxpayer record; the first and last bank transactions do not establish that period. Ask what the business does, whether it employs staff, whether it makes exempt supplies, whether sales are cross-border, and whether construction subcontracting is involved. Names, company suffixes, payroll-looking debits and IBANs suggest questions; they do not establish those facts or the VAT result. Reconcile the previous line27 credit to current line22. |  | House input pack and ten onboarding topics, old185–205/879–919. |
| france-vat-return-0133 / ## The taxable base / 204 | **Bank statement only (OpenAccountants working practice, not a legal rule).** If there is no bank statement at all, stop. With a bank statement but no invoices, prepare the return and tell the reviewer in writing that every input VAT claim must be checked against a compliant invoice before the return is approved. |  | House bankstatement reviewer-warning workflow, old185–205. |
| france-vat-return-0134 / ## The taxable base / 206 | **CA3 credit-note corrections.** For an ordinary supported credit note reducing a previously taxed customer sale, enter the positive correction base on B5; recover the previously paid output VAT through line 21, with the required credit note or corrected invoice and its separate collected-VAT-correction identification. Do not put negative VAT in the gross-tax block or also reduce the other frame-A amounts for that same correction. For example, a qualifying EUR 2,000 excluding-VAT reduction with EUR 400 VAT is B5 EUR 2,000 and line 21 EUR 400, not a second reduction of current A1 plus another EUR 400 deduction. A supplier credit note reverses the earlier input deduction through line 15 to its supported extent. Non-taxed customer corrections go as positive amounts on F8 without inventing output VAT. The 2026 notice expressly prohibits negative B5/F8 amounts and retains special rules for foreign customers already refunded incorrectly invoiced VAT; do not override those with this ordinary method. Keep the original invoice, its declared tax and the correction evidence together. See the [2026 notice](https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf), B5/F8 and lines 15/21. | [VAT-Q029](#vat-q029); [VAT-Q030](#vat-q030); [VAT-Q031](#vat-q031); [VAT-Q032](#vat-q032); [ROOT-VAT-R001](#root-vat-r001) | EUR2000/400 credit note is a labelled hypothetical application, not a statutory amount. |
| france-vat-return-0135 / ## The taxable base / 208 | **Working paper.** Follow `vat-workflow-base` Section 3. In the Transactions sheet the line-code column accepts only 2026 CA3 codes, blank for excluded lines, and "A3/20" style for self-assessed lines. The Line Summary sheet sums A1, E1, E2, E3, F2, A3, A4, B2, B4, then the rate block 08, 09, 9B, I1 to I6, line 16, memo 17, lines 19, 20, 22, 23, memo 24, then 25 or TD, 26, 27, 28 and 32. If line 23 exceeds line 16, line 25 is the credit and line 27 = 25 less 26 carries to the next return; otherwise TD = 16 less 23. This ordinary sheet assumes no energy-excise credit/levy or group-payment transfer. Where applicable, use the actual form’s X5/Z5/AB adjustments: line 28 = TD − X5 (X5 cannot exceed TD), and line 32 = 28 + 29 + Z5 − AB; do not silently set those actual liabilities or credits to zero. Keep the base Transactions columns and a separate Line Summary and Return Form. In the summary, use supported net amounts for operation bases and supported VAT for deductible lines; a self-assessed entry must feed both output and eligible input tax, rather than disappearing because its transaction code is A3/20. Include lines21 and2C where actually applicable in the line23 total, and all actual gross-tax rows in line16. Keep formulas separate from hardcoded facts and source links; mark unresolved rows for the reviewer without assigning a guessed tax result. The earlier template colour conventions were house formatting, not tax law. Use the available spreadsheet recalculation tool, inspect the recomputed outputs and reconcile the Return Form to the summary before handover; the old environment-specific /mnt helper path is not an assumed installation requirement. | [VAT-Q041](#vat-q041); [VAT-Q051](#vat-q051); [VAT-Q052](#vat-q052); [VAT-Q053](#vat-q053); [VAT-Q054](#vat-q054); [VAT-Q057](#vat-q057); [VAT-Q059](#vat-q059); [VAT-Q061](#vat-q061); [VAT-Q062](#vat-q062); [VAT-Q063](#vat-q063); [VAT-Q081](#vat-q081); [VAT-Q082](#vat-q082); [VAT-Q083](#vat-q083); [VAT-Q084](#vat-q084); [VAT-Q085](#vat-q085); [VAT-Q086](#vat-q086); [VAT-Q087](#vat-q087); [VAT-Q088](#vat-q088); [VAT-Q089](#vat-q089); [VAT-Q090](#vat-q090); [VAT-Q091](#vat-q091); [VAT-Q092](#vat-q092); [VAT-Q093](#vat-q093) | House workbook architecture; actual CA3 formula conditions source-bound, old environment-specific helper not required. |
| france-vat-return-0137 / ## Deadlines and filing / 214 | &#124; CA3, régime réel normal &#124; Monthly, between the 15th and the 24th of the following month. The exact day depends on the department (Paris, 92, 93 and 94 apart), the category of business and the SIREN or the first letter of the name, and is shown in the espace professionnel. Never state a single date &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F23566 ; https://www.impots.gouv.fr/le-regime-reel-normal-dates-limites-de-transmission-des-ca3 &#124; | [VAT-Q026](#vat-q026); [VAT-Q047](#vat-q047) |  |
| france-vat-return-0138 / ## Deadlines and filing / 215 | &#124; CA3, quarterly option &#124; Where annual VAT due is below EUR 4,000 (CGI art. 287-2) &#124; Légifrance art. 287 &#124; | [VAT-Q006](#vat-q006) |  |
| france-vat-return-0139 / ## Deadlines and filing / 216 | &#124; CA12, régime simplifié &#124; Annual, by the second working day after 1 May for a calendar year; within three months of the year end otherwise &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F23566 &#124; | [VAT-Q045](#vat-q045) |  |
| france-vat-return-0140 / ## Deadlines and filing / 217 | &#124; Régime simplifié instalments &#124; July (55%) and December (40%); balance with the CA12. Off-calendar years: return filed January to May of N gives instalments July and December N; June to October gives December N and July N+1; November or December gives July and December N+1 &#124; CGI art. 287-3 ; F23566 &#124; | [VAT-Q006](#vat-q006); [VAT-Q046](#vat-q046) |  |
| france-vat-return-0141 / ## Deadlines and filing / 218 | &#124; Régime simplifié moved to monthly CA3 &#124; VAT due for the previous year above EUR 15,000 (art. 287-3 bis); or the business makes intra-EU acquisitions, imports or exits from a suspensive regime (art. 287-3 ter, from 1 January 2025; quarterly if under EUR 4,000) &#124; Légifrance art. 287 &#124; | [VAT-Q006](#vat-q006); [VAT-Q007](#vat-q007) |  |
| france-vat-return-0142 / ## Deadlines and filing / 219 | &#124; Change of regime &#124; Failure of the previous-year L. 162-4 condition ends RSI on 1 January of the following year. Breaching a current-year L. 162-5 ceiling ends RSI with effect from 1 January of that year (D. 162-8, 1°–2°); see the ordinary calendar-year filing sequence below. The separate previous-year VAT-above-EUR-15,000 trigger remains governed by CGI art. 287-3 bis &#124; F23566 ; CIBS L. 162-4/L. 162-5 and D. 162-8 &#124; | [ROOT-VAT-Q005](#root-vat-q005); [ROOT-VAT-Q006](#root-vat-q006); [VAT-Q007](#vat-q007); [VAT-Q049](#vat-q049) |  |
| france-vat-return-0143 / ## Deadlines and filing / 220 | &#124; Cessation or sale of the business &#124; Final return within 30 days; 60 days under the régime simplifié (CGI art. 287-4) &#124; Légifrance art. 287 &#124; | [VAT-Q007](#vat-q007) |  |
| france-vat-return-0144 / ## Deadlines and filing / 221 | &#124; État récapitulatif des clients (eligible intra-EU supplies of goods) and déclaration européenne de services (DES) where the supplier/customer locations, general B2B place and recipient-liability/non-exemption conditions below apply &#124; Within ten working days after the month the VAT became due, filed with customs on pro.douane.gouv.fr (CGI art. 289 B). The notice permits franchise businesses to submit DES on paper &#124; CA3 notice 3310-NOT-CA3-SD, 2026 &#124; | [VAT-Q033](#vat-q033); [VAT-Q034](#vat-q034) |  |
| france-vat-return-0145 / ## Deadlines and filing / 222 | &#124; Payment &#124; With the return, online from the espace professionnel on impots.gouv.fr &#124; F23566 &#124; | [VAT-Q047](#vat-q047) |  |
| france-vat-return-0146 / ## Deadlines and filing / 223 | &#124; E-invoicing: receiving &#124; From 1 September 2026 every VAT taxable person (assujetti) established in France, including franchise businesses and those making only exempt supplies, must be able to receive e-invoices through an approved platform (plateforme agréée) &#124; CGI art. 289 bis ; LFR 2022 art. 26, III, as rewritten by LF 2024 art. 91 ; impots.gouv.fr FAQ &#124; | [ROOT-VAT-C001](#root-vat-c001); [ROOT-VAT-C002](#root-vat-c002); [ROOT-VAT-C003](#root-vat-c003); [ROOT-VAT-C006](#root-vat-c006) |  |
| france-vat-return-0147 / ## Deadlines and filing / 224 | &#124; E-invoicing and e-reporting: issuing &#124; From 1 September 2026 for large companies, ETI and VAT groups; from 1 September 2027 for SMEs and micro-enterprises (size under LME art. 51 and decree 2008-1354, art. 3) &#124; same ; BOFiP BOI-TVA-DECLA-20-30-50 (30 September 2026) &#124; | [ROOT-VAT-C003](#root-vat-c003); [ROOT-VAT-C004](#root-vat-c004); [ROOT-VAT-C008](#root-vat-c008); [ROOT-VAT-C009](#root-vat-c009); [ROOT-VAT-C011](#root-vat-c011); [ROOT-VAT-C012](#root-vat-c012) |  |
| france-vat-return-0149 / ## Deadlines and filing / 228 | **E-invoice scope and size reference.** The domestic electronic-invoice route applies to the actual qualifying operations between assujettis established in France, subject to CGI art. 289 bis and the French invoicing rules. Operations exempt under arts. 261–261 E and dispensed from invoicing are excluded from the issuing/e-reporting scope; an assujetti with only such sales still needs to receive qualifying supplier e-invoices. A non-assujetti is a different case. Under the actual consolidated LFR 2022 art. 26, III, SME/micro deferral excludes members of a VAT group. Assess the category for each legal person at 1 January 2025 using its last accounting year closed before that date, or its first accounting year closed on or after that date if none existed before it. The DGFiP September 2026 FAQ states the same reference; the unchanged size-category definitions remain under LME art. 51 and decree 2008-1354. | [ROOT-VAT-C001](#root-vat-c001); [ROOT-VAT-C002](#root-vat-c002); [ROOT-VAT-C003](#root-vat-c003); [ROOT-VAT-C004](#root-vat-c004); [ROOT-VAT-C005](#root-vat-c005); [ROOT-VAT-C006](#root-vat-c006); [ROOT-VAT-C008](#root-vat-c008); [ROOT-VAT-C009](#root-vat-c009); [ROOT-VAT-C010](#root-vat-c010); [ROOT-VAT-C011](#root-vat-c011); [ROOT-VAT-C012](#root-vat-c012) |  |
| france-vat-return-0150 / ## Deadlines and filing / 230 | **Current-year RSI ceiling: ordinary calendar-year business.** Monitor the applicable indexed L. 162-5 ceiling using the actual qualifying turnover method, with mixed-activity and startup conditions where relevant. Meeting the ceiling exactly does not breach it. If a calendar-year business first exceeds it in September 2026, the real-normal regime takes effect from 1 January 2026 under CIBS art. D. 162-8, 2°. File the recapitulative CA3 in October for January through September, crediting the RSI instalments required for that period under BOFiP §120; then file October's monthly CA3 in November and continue monthly returns. Use the exact personalised filing deadline above, not an assumed 21st. Retain the period reconciliation and instalment evidence. See BOI-TVA-DECLA-20-20-30-10, §60–130. For a non-calendar accounting year, do not silently reuse that doctrine's 2023 first-day-of-exercise examples as the 2025 decree's 1 January result: the precise transition-period/form reconciliation remains an identified source question. | [ROOT-VAT-Q005](#root-vat-q005); [ROOT-VAT-Q006](#root-vat-q006); [VAT-Q049](#vat-q049) | September/October2026 crossing sequence is a labelled ordinarycalendar fixture; noncalendar countertext remains unresolved. |
| france-vat-return-0152 / ## Penalties and interest / 236 | &#124; Late payment of tax &#124; Interest of 0.20% a month under CGI art. 1727, III. The ordinary IV-1 period starts on the first day of the month after the due month and runs to the last day of the payment month; where the late-filing majoration in art. 1728 applies, IV-3 instead stops the count at the last day of the return-filing month or rectification-proposal month, as applicable &#124; Légifrance art. 1727 &#124; | [ROOT-VAT-P001](#root-vat-p001); [ROOT-VAT-P002](#root-vat-p002) |  |
| france-vat-return-0153 / ## Penalties and interest / 237 | &#124; Late return, no formal notice, or filed within 30 days of a notice &#124; 10% of the tax due on the return (CGI art. 1728, 1, a) &#124; Légifrance art. 1728 &#124; | [ROOT-VAT-P003](#root-vat-p003) |  |
| france-vat-return-0154 / ## Penalties and interest / 238 | &#124; Return still missing 30 days after a formal notice &#124; 40% (art. 1728, 1, b) &#124; same &#124; | [ROOT-VAT-P003](#root-vat-p003) |  |
| france-vat-return-0155 / ## Penalties and interest / 239 | &#124; Hidden activity discovered &#124; 80% (art. 1728, 1, c) &#124; same &#124; | [ROOT-VAT-P003](#root-vat-p003) |  |
| france-vat-return-0156 / ## Penalties and interest / 240 | &#124; Errors or omissions: deliberate failure; L. 64 abuse of law; fraudulent schemes &#124; Deliberate failure: 40%. L. 64 abuse: 80%, reduced to 40% unless it is established that the taxpayer was the principal initiator or principal beneficiary of the abusive acts. Fraudulent schemes: 80% (CGI art. 1729, a–c) &#124; Légifrance art. 1729 &#124; | [ROOT-VAT-P004](#root-vat-p004) |  |
| france-vat-return-0157 / ## Penalties and interest / 241 | &#124; Late payment &#124; 5% surcharge (CGI art. 1731, 1). Under art. 1731, 2, it does not apply when the late declaration is accompanied by payment of all corresponding tax; application of art. 1728 alone does not establish this exception &#124; Légifrance art. 1731 &#124; | [ROOT-VAT-C030](#root-vat-c030) |  |
| france-vat-return-0158 / ## Penalties and interest / 242 | &#124; Ordinary self-assessed tax that would have been deductible but was left off the return &#124; Fine of 5% of the deductible amount (CGI art. 1788 A, 4). Its second paragraph provides a specific proportional adjustment for an art. 257 self-supply; do not apply this unadjusted ordinary amount to that special branch &#124; Légifrance art. 1788 A &#124; | [ROOT-VAT-S007](#root-vat-s007); [ROOT-VAT-S016](#root-vat-s016) |  |
| france-vat-return-0159 / ## Penalties and interest / 243 | &#124; État récapitulatif filed late &#124; EUR 750; EUR 1,500 if still missing 30 days after notice; EUR 15 per error, capped at EUR 1,500 (art. 1788 A, 1 and 2) &#124; same &#124; | [ROOT-VAT-S012](#root-vat-s012); [ROOT-VAT-S013](#root-vat-s013); [ROOT-VAT-S014](#root-vat-s014); [ROOT-VAT-S015](#root-vat-s015) |  |
| france-vat-return-0160 / ## Penalties and interest / 244 | &#124; Invoice errors or omissions &#124; EUR 15 per error, capped at a quarter of the invoice amount (CGI art. 1737, II) &#124; Légifrance art. 1737 &#124; | [ROOT-VAT-S001](#root-vat-s001) |  |
| france-vat-return-0161 / ## Penalties and interest / 245 | &#124; Invoice not issued electronically when required &#124; EUR 50 per invoice, capped at EUR 15,000 a year (art. 1737, III, as amended by LF 2026) &#124; same &#124; | [ROOT-VAT-S002](#root-vat-s002) |  |
| france-vat-return-0162 / ## Penalties and interest / 246 | &#124; No approved platform for receiving e-invoices &#124; Formal notice to comply within three months; EUR 500 if the failure persists at expiry, followed by a new three-month notice; EUR 1,000 if it remains unremedied at that expiry. Each further EUR 1,000 requires persistence after another three-month period and an unsuccessful formal notice (CGI art. 1737, IV bis) &#124; Légifrance art. 1737 &#124; | [ROOT-VAT-S008](#root-vat-s008); [ROOT-VAT-S009](#root-vat-s009); [ROOT-VAT-S010](#root-vat-s010); [ROOT-VAT-S011](#root-vat-s011) |  |
| france-vat-return-0163 / ## Penalties and interest / 247 | &#124; E-reporting not transmitted &#124; EUR 500 per transmission, capped at EUR 15,000 per calendar year for each applicable obligation under CGI art. 290 or 290 A (art. 1788 D, I and II, as amended by LF 2026); apply its V relief where the actual conditions hold &#124; Légifrance art. 1788 D &#124; | [ROOT-VAT-S004](#root-vat-s004); [ROOT-VAT-S005](#root-vat-s005); [ROOT-VAT-S006](#root-vat-s006) |  |
| france-vat-return-0164 / ## Penalties and interest / 248 | &#124; First-offence relief &#124; The stated art. 1737, II/III invoice fines and art. 1788 D e-reporting fines are not imposed for a first offence in the current calendar year and three previous years if corrected spontaneously or within 30 days of the administration's first request, under each article's V. Do not extend this relief to the art. 1737, IV bis receiving-platform procedure, which has its own notices &#124; Légifrance art. 1737, V and 1788 D, V &#124; | [ROOT-VAT-S003](#root-vat-s003); [ROOT-VAT-S006](#root-vat-s006) |  |
| france-vat-return-0165 / ## Penalties and interest / 250 | Example of the interest rule: a CA3 for March 2026 showing EUR 4,000 due, filed and paid in June without any notice, bears the 10% majoration (EUR 400) and interest for May and June, 2 × 0.20% × 4,000 = EUR 16. Audit procedure, the reductions for voluntary correction and the taxpayer's rights are in `fr-tax-audit`. | [ROOT-VAT-P001](#root-vat-p001); [ROOT-VAT-P002](#root-vat-p002); [ROOT-VAT-P003](#root-vat-p003) | Explicit4000/400/16 hypothetical interest illustration; legalrate/period/filing conditions source-bound, no invented penalty rule. |
| france-vat-return-0166 / ## Cross-border points / 254 | - **B2B services sold to EU customers:** establish the general CGI art. 259-1° place-of-supply rule first; a foreign customer alone does not displace the special place rules in art. 259 A–D. For the ordinary service supplied from the relevant French business establishment to an eligible business customer in another member state, invoice without French VAT, mark "Auto-liquidation", put the amount on E2 and check the customer's number on VIES. DES applies where the service is located there under directive art. 44 and the customer owes the tax under art. 196; a service exempt in that state is not included in DES. Keep the establishment, customer status, supply classification and destination-liability/exemption facts; apply the ten-working-day deadline above only to an operation actually requiring DES. | [VAT-Q022](#vat-q022); [VAT-Q033](#vat-q033); [VAT-Q037](#vat-q037) |  |
| france-vat-return-0167 / ## Cross-border points / 255 | - **Goods sold to EU businesses:** zero-rated on F2 with VIES check and transport proof; état récapitulatif within ten working days after the month. | [VAT-Q034](#vat-q034); [VAT-Q039](#vat-q039) |  |
| france-vat-return-0168 / ## Cross-border points / 256 | - **Distance sales and B2C digital services to other EU states:** the ordinary origin-tax exception applies to a seller established only in France, with qualifying goods dispatched from France, where the combined eligible intra-EU distance-goods sales and cross-border telecommunications, broadcasting and electronic services do not exceed EUR 10,000 excluding VAT in either the current or previous calendar year and no destination-tax option applies. Domestic digital sales are not part of that cross-border total. Destination tax applies from the transaction crossing the limit, where either year fails, or under the valid option. A prior-year EUR 11,000 / current-year EUR 1,000 seller fails the amount condition; EUR 10,000 in each year meets only the amount test, not all the other conditions. See CGI art. 259 D / 258 A and https://bofip.impots.gouv.fr/bofip/11964-PGP.html, §220 and 240–270. OSS can provide the declaration route where eligible, rather than being an unconditional duty created by this Guide. On the French CA3, destination-taxable distance goods go to E3; the stated cross-border B2C telecommunications, broadcasting and electronic services taxable in the consumption state go to E2 under the 2026 notice. Establish any applicable OSS declaration route separately. This is separate from the EUR 10,000 intra-EU acquisition threshold; detailed destination filing is in `eu-vat-directive`, R-EU-5. | [VAT-Q024](#vat-q024); [VAT-Q025](#vat-q025); [VAT-Q037](#vat-q037) |  |
| france-vat-return-0169 / ## Cross-border points / 257 | - **Purchases from abroad:** self-assess as set out in The taxable base (A3, B2, A4, B4). | [VAT-Q018](#vat-q018); [VAT-Q021](#vat-q021); [VAT-Q022](#vat-q022); [VAT-Q027](#vat-q027); [VAT-Q035](#vat-q035); [VAT-Q036](#vat-q036) |  |
| france-vat-return-0170 / ## Cross-border points / 258 | - **Non-established businesses selling in France:** where a French taxable customer buys, the customer is liable under art. 283-1 and 283-2 in the cases those articles name. A non-EU business that must register may need a fiscal representative: refer. | [VAT-Q022](#vat-q022); [VAT-Q035](#vat-q035); [VAT-Q036](#vat-q036); [ROOT-VAT-D017](#root-vat-d017); [ROOT-VAT-D018](#root-vat-d018) |  |
| france-vat-return-0171 / ## Cross-border points / 259 | - **The EU franchise:** an EU-established claimant must meet the French art. 293 B conditions and the cumulative art. 293 B bis EU-wide EUR 100,000 limit in BOTH years plus the prescribed home-state process. A French business using another state's franchise must tell the French administration within 15 working days after its EU-wide annual turnover exceeds EUR 100,000 and supply the required partial-quarter figures (art. 293 B ter). | [VAT-Q001](#vat-q001); [VAT-Q002](#vat-q002); [ROOT-VAT-C025](#root-vat-c025); [ROOT-VAT-C026](#root-vat-c026); [ROOT-VAT-C027](#root-vat-c027); [ROOT-VAT-C028](#root-vat-c028); [ROOT-VAT-C029](#root-vat-c029) |  |
| france-vat-return-0172 / ## Cross-border points / 260 | - **Monaco:** tax on operations to Monaco is shown at memo line 18 of the CA3. | [VAT-Q040](#vat-q040) |  |
| france-vat-return-0175 / ## Worked examples / 267 | - **3 April 2026, NOTION LABS INC, subscription EUR 14.68.** Stipulate that the actual invoice is for a general B2B service taxable in France from a non-established supplier without a participating French establishment, with no VAT charged and full ordinary deduction entitlement. Record EUR 14.68 at A3; EUR 14.68 × 20% = EUR 2.936, or EUR 2.94 in the decimal working paper, goes through the output rate block and the matching deductible amount at line 20. The two-sided self-assessment has nil net effect on those stipulated facts. A brand alone does not establish this branch. | [ROOT-VAT-R001](#root-vat-r001); [VAT-Q018](#vat-q018); [VAT-Q021](#vat-q021); [VAT-Q022](#vat-q022); [VAT-Q027](#vat-q027); [VAT-Q035](#vat-q035) | Retained Notion14.68 fixture; decimal arithmetic independently recorded in FR-L37 checks, not statutory threshold. |
| france-vat-return-0176 / ## Worked examples / 268 | - **10 April 2026, GOOGLE IRELAND LIMITED, Ads EUR 850.** On the same stipulated general-service and full-deduction facts, A3 is EUR 850 and the output and deductible tax are each EUR 170. Both sides are required; the first main example below retains the same purchase within an aggregate return. Verify the actual billing establishment and invoice rather than assuming them from the description. | [ROOT-VAT-R001](#root-vat-r001); [VAT-Q018](#vat-q018); [VAT-Q021](#vat-q021); [VAT-Q022](#vat-q022); [VAT-Q027](#vat-q027); [VAT-Q035](#vat-q035) | Retained Google850 fixture; own arithmetic controls in FR-L37. |
| france-vat-return-0177 / ## Worked examples / 269 | - **15 April 2026, BRASSERIE LIPP PARIS, meal EUR 220.** Obtain the invoice, actual VAT breakdown, attendees and business purpose. A restaurant name does not by itself block or establish recovery. If the ordinary use, lawful invoice and deduction conditions are met, put the supported deductible tax at line 20; if those facts are missing, hold the claim for evidence rather than inventing a permanent zero-tax invoice or denial. The EUR 220 debit alone does not prove the rate or deductible amount. | [VAT-Q018](#vat-q018); [VAT-Q021](#vat-q021) | Retained220mealquestioncase; no inventedVATsplit/permanentdenial. |
| france-vat-return-0178 / ## Worked examples / 270 | - **18 April 2026, DELL FRANCE SAS, laptop invoice DEL2026-0041, EUR 1,595 including 20% VAT.** On those stipulated invoice facts, EUR 1,595 ÷ 1.20 = EUR 1,329.166… net, or EUR 1,329.17, and the working-paper VAT is EUR 265.83. If the supported accounting treatment records this durable laptop as a fixed asset and the ordinary deduction conditions hold, claim the deductible tax at line 19. The optional EUR 500 equipment tolerance does not make every purchase above or below it automatically an asset or expense; retain the actual classification and linked-component facts. | [ROOT-VAT-R001](#root-vat-r001); [VAT-Q015](#vat-q015); [VAT-Q027](#vat-q027) | Retained1595gross/1329.17net/265.83tax conditional20%invoicefixture; FR-L37 arithmetic. |
| france-vat-return-0179 / ## Worked examples / 271 | - **22 April 2026, STUDIO KREBS GMBH, IT consultancy receipt EUR 3,500.** If the actual transaction is an ordinary general B2B service supplied from the relevant French establishment to an eligible German business customer, taxable there with recipient liability and no destination exemption, invoice without French VAT, state the required reverse charge, record EUR 3,500 at E2 and submit the required DES. Verify customer status/number and the supply/establishment facts; the German name or IBAN does not establish them. Apply the stated DES deadline only if its actual conditions hold. | [VAT-Q022](#vat-q022); [VAT-Q033](#vat-q033); [VAT-Q037](#vat-q037) | Retained3500servicefixture; customer/establishment/place/DES conditions stipulated. |
| france-vat-return-0180 / ## Worked examples / 272 | - **28 April 2026, ARVAL FRANCE, lease debit EUR 650.** If the actual leased vehicle is designed for passengers or mixed use and no qualifying exception applies, the vehicle-related input VAT is excluded under the admission rule. Retain the lease invoice and design/exception evidence. The bank debit alone does not establish its net price or VAT breakdown, so do not label all EUR 650 as net merely because nothing is claimed. Fuel and an independently qualifying vehicle exception follow their own stated rules. | [VAT-Q008](#vat-q008); [VAT-Q012](#vat-q012); [VAT-Q013](#vat-q013) | Retained650leasequestioncase; no inventednet/VATbreakdown. |
| france-vat-return-0181 / ## Worked examples / 274 | **Example 1: monthly CA3 for a Paris consultancy (régime réel normal).** In April 2026 the company sells EUR 50,000 of consulting at 20%, and its in-house café sells EUR 8,000 of food and soft drinks for consumption on the premises at 10% (CGI art. 279, m; alcoholic drinks would be 20%). It buys Google Ads from Google Ireland for EUR 850 (no VAT on the invoice), other French purchases of EUR 12,000 plus 20% VAT, and a server for EUR 1,500 plus 20% VAT that it records as a fixed asset. Sales: A1 is 58,000; line 08 base 50,000 and tax 10,000; line 9B base 8,000 and tax 800. Google Ads: A3 is 850, tax 170 joins line 08, and the same 170 is deducted at line 20. Deductions: line 20 is 2,400 plus 170, line 19 is 300. Line 16 is 10,970, line 23 is 2,870, so TD and line 28 are 8,100. | [ROOT-VAT-R001](#root-vat-r001); [ROOT-VAT-R009](#root-vat-r009); [VAT-Q006](#vat-q006); [VAT-Q021](#vat-q021); [VAT-Q022](#vat-q022); [VAT-Q026](#vat-q026); [VAT-Q027](#vat-q027); [VAT-Q035](#vat-q035); [VAT-Q041](#vat-q041) | Original aggregate CA3 fixture and executablecheck retained byteexact; actual tax/form rules separate from hypothetical inputs. |
| france-vat-return-0182 / ## Worked examples / 276 | ```oa-check | [ROOT-VAT-R001](#root-vat-r001); [ROOT-VAT-R009](#root-vat-r009); [VAT-Q006](#vat-q006); [VAT-Q021](#vat-q021); [VAT-Q022](#vat-q022); [VAT-Q026](#vat-q026); [VAT-Q027](#vat-q027); [VAT-Q035](#vat-q035); [VAT-Q041](#vat-q041) | Original aggregate CA3 fixture and executablecheck retained byteexact; actual tax/form rules separate from hypothetical inputs. |
| france-vat-return-0183 / ## Worked examples / 298 | **Example 2: régime simplifié, instalments and the fixed-asset edge.** A shop on the régime simplifié had tax of EUR 9,000 for 2025 before the VAT on fixed assets. Its 2026 instalments are 55% in July (4,950) and 40% in December (3,600). On the 2026 CA12 its gross VAT is EUR 18,000, deductions on other goods and services EUR 6,500, and VAT on fixed assets EUR 1,200. Net VAT for 2026 is 10,300, so the balance due with the CA12 by the second working day after 1 May 2027 is 10,300 less 8,550, or 1,750. The edge: next year's instalment base (line 57) is struck before the fixed-asset VAT, so it is 18,000 less 6,500, or 11,500, not 10,300. The 2027 instalments are 6,325 in July and 4,600 in December. | [VAT-Q006](#vat-q006); [VAT-Q042](#vat-q042); [VAT-Q043](#vat-q043); [VAT-Q044](#vat-q044); [ROOT-VAT-C020](#root-vat-c020); [ROOT-VAT-C021](#root-vat-c021) | Original CA12 fixture and executablecheck retained byteexact; current below550/400 branch does not affect its9000base instalments. |
| france-vat-return-0184 / ## Worked examples / 300 | ```oa-check | [VAT-Q006](#vat-q006); [VAT-Q042](#vat-q042); [VAT-Q043](#vat-q043); [VAT-Q044](#vat-q044); [ROOT-VAT-C020](#root-vat-c020); [ROOT-VAT-C021](#root-vat-c021) | Original CA12 fixture and executablecheck retained byteexact; current below550/400 branch does not affect its9000base instalments. |
| france-vat-return-0185 / ## Ask the client first / 325 | - For a start-up, what are the exact start date and dated qualifying sales? For the EUR 10,000 cross-border test, provide both calendar years, all establishments, goods-dispatch countries, combined eligible sales and any destination-tax option. For currency, identify the actual VAT tax point and conversion evidence; for assets and lodging, provide capitalisation/expense and beneficiary/use evidence. | [VAT-Q003](#vat-q003); [VAT-Q004](#vat-q004); [VAT-Q005](#vat-q005); [VAT-Q010](#vat-q010); [VAT-Q011](#vat-q011); [VAT-Q015](#vat-q015); [VAT-Q017](#vat-q017); [VAT-Q023](#vat-q023); [VAT-Q024](#vat-q024); [VAT-Q025](#vat-q025) | Intake routing; exact statutory versus administrative startup question stays explicit. |
| france-vat-return-0186 / ## Ask the client first / 327 | - Which regime are you in, and what were last year's turnover (by activity: goods and catering, or services) and last year's VAT due? Both numbers decide the regime. | [VAT-Q006](#vat-q006); [VAT-Q007](#vat-q007); [VAT-Q045](#vat-q045); [VAT-Q049](#vat-q049) |  |
| france-vat-return-0187 / ## Ask the client first / 328 | - What filing date does your espace professionnel show for the CA3? It depends on department, category and SIREN. | [VAT-Q047](#vat-q047) |  |
| france-vat-return-0188 / ## Ask the client first / 329 | - Do you sell outside France? For each customer: business or consumer, goods or services, which country. That decides E1, E2, E3, F2 and the EU statements. | [VAT-Q033](#vat-q033); [VAT-Q034](#vat-q034); [VAT-Q037](#vat-q037) |  |
| france-vat-return-0189 / ## Ask the client first / 330 | - Do you make intra-EU acquisitions, imports or exits from a suspensive regime? These trigger the CGI art. 287-3 ter CA3 route from 2025 even where the turnover remains within RSI limits; apply monthly filing or the statutory quarterly exception where annual VAT due is below EUR 4,000. | [VAT-Q006](#vat-q006); [VAT-Q007](#vat-q007) |  |
| france-vat-return-0190 / ## Ask the client first / 331 | - Any credit at line 27 of your last return, any exempt income, any construction subcontracting, any company cars (designed to carry people or goods)? | [VAT-Q008](#vat-q008); [VAT-Q018](#vat-q018); [VAT-Q035](#vat-q035); [VAT-Q041](#vat-q041) |  |
| france-vat-return-0191 / ## Ask the client first / 332 | - Refuse or refer: a business inside the franchise that has not opted; partial exemption above de minimis; margin scheme; property VAT; VAT groups; fiscal representatives; overseas departments; anyone wanting income tax (use `fr-income-tax` or `fr-personal-income-tax`); any refusal in `eu-vat-directive` R-EU-1 to R-EU-12. | [VAT-Q018](#vat-q018); [ROOT-VAT-D002](#root-vat-d002); [ROOT-VAT-D007](#root-vat-d007); [ROOT-VAT-D017](#root-vat-d017); [ROOT-VAT-D018](#root-vat-d018) | House referral policy and siblings; no assertion that specialist methods are complete. |

## Source quotations

### VAT-Q001

CGI293B/Bbis/Bter/D; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-29; actual original read 2026-10-29. Native LF [83, 102]; reader SHA256 `3fd741301235513b0890054c8d6568425c6a6d5e733a00ce453dba8135cb1814`. Inherited actual C selected reading, exact read-scope records preserved

```text
I. - Pour leurs livraisons de biens et leurs prestations de services, les assujettis établis en France bénéficient d'une franchise qui les dispense du paiement de la taxe sur la valeur ajoutée lorsqu'ils n'ont pas réalisé en France un chiffre d'affaires, évalué dans les conditions prévues à l'article 293 D, excédant les plafonds suivants :

(En euros.)


Année d'évaluation	
Chiffre d'affaires national total	
Chiffre d'affaires national afférent aux prestations de services autres que les ventes

à consommer sur place et les prestations d'hébergement



Année civile précédente	
85 000	
37 500

Année en cours	
93 500	
41 250
```

### VAT-Q002

CGI293B/Bbis/Bter/D; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-29; actual original read 2026-10-29. Native LF [104, 144]; reader SHA256 `3fd741301235513b0890054c8d6568425c6a6d5e733a00ce453dba8135cb1814`. Inherited actual C selected reading, exact read-scope records preserved

```text
I bis. - A. - Les avocats, les avocats au Conseil d'Etat et à la Cour de cassation, les auteurs d'œuvres de l'esprit et les artistes-interprètes assujettis et établis en France bénéficient d'une franchise qui les dispense du paiement de la taxe sur la valeur ajoutée lorsqu'ils n'ont pas réalisé en France un chiffre d'affaires, évalué dans les conditions prévues à l'article 293 D, excédant les plafonds suivants :

(En euros.)


Année d'évaluation	
Chiffre d'affaires national afférent aux opérations

mentionnées au B du présent I bis

	
Chiffre d'affaires national afférent aux opérations autres

que celles mentionnées au B du présent I bis



Année civile précédente	
50 000	
35 000

Année en cours	
55 000	
38 500

B. - Les opérations prises en compte pour les besoins des plafonds mentionnés à la deuxième colonne du tableau du second alinéa du A du présent I bis sont les suivantes :

1° Les opérations réalisées par les avocats et les avocats au Conseil d'Etat et à la Cour de cassation, dans le cadre de l'activité définie par la réglementation applicable à leur profession ;

2° Les livraisons par les auteurs d'œuvres de l'esprit, à l'exception des architectes, de leurs œuvres mentionnées aux 1° à 12° de l'article L. 112-2 du code de la propriété intellectuelle et la cession des droits patrimoniaux qui leur sont reconnus par la loi ;

3° Les opérations relatives à l'exploitation des droits patrimoniaux qui sont reconnus par la loi aux artistes-interprètes mentionnés à l'article L. 212-1 du même code.

II. - Lorsque l'un des plafonds de chiffre d'affaires prévus aux I ou I bis du présent article pour les opérations de l'année en cours est dépassé, la franchise cesse de s'appliquer pour les opérations intervenant à compter de la date du dépassement.




Conformément au II de l'article 32 de la loi n° 2025-127 du 14 février 2025, le I de l'article précité entre en vigueur le 1er mars 2025.

Conformément au A du III de l'article 1 de la loi n° 2025-1044 du 3 novembre 2025, ces dispositions s'appliquent à compter du 1er mars 2025.
```

### VAT-Q003

CGI293B/Bbis/Bter/D; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-29; actual original read 2026-10-29. Native LF [303, 323]; reader SHA256 `3fd741301235513b0890054c8d6568425c6a6d5e733a00ce453dba8135cb1814`. Inherited actual C selected reading, exact read-scope records preserved

```text
I.- A. - Le chiffre d'affaires réalisé en France qui sert de référence pour l'application de la franchise prévue aux articles 293 B et 293 B bis est le montant total annuel des livraisons de biens et des prestations de services, hors taxe sur la valeur ajoutée, réalisées en France.

B. - Le chiffre d'affaires mentionné au A du présent I est constitué des montants hors taxes suivants :

1° Le montant des livraisons de biens et des prestations de services, dans la mesure où elles seraient taxées si elles étaient effectuées par un assujetti ne bénéficiant pas de la franchise ;

2° Le montant des opérations exonérées avec droit à déduction en application des 8° à 10° du II de l'article 262 et de l'article 298 undecies ;

3° Le montant des opérations exonérées en application du I et des 1° à 7°, 12° et 14° du II de l'article 262 et des articles 262-00 bis et 263 ;

4° Le montant des opérations exonérées en application des 1° et 3° du I de l'article 262 ter ;

5° Le montant des opérations immobilières, ainsi que des opérations financières, d'assurance et de réassurance mentionnées aux 1° et 2° de l'article 261 C qui n'ont pas le caractère d'opérations accessoires.

Les cessions de biens d'investissement corporels ou incorporels de l'assujetti ne sont pas prises en considération pour la détermination du chiffre d'affaires.

II. - A. - Le chiffre d'affaires annuel réalisé dans l'Union européenne qui sert de référence pour l'application des articles 293 B bis et 293 B ter est le montant total annuel des livraisons de biens et des prestations de services, hors taxe sur la valeur ajoutée, réalisées sur le territoire de l'Union européenne.

B. - Les chiffres d'affaires réalisés dans les autres Etats membres de l'Union européenne entrant dans la composition du chiffre d'affaires annuel dans l'Union européenne sont déterminés en application des dispositions transposant dans ces Etats l'article 288 de la directive 2006/112/CE du Conseil du 28 novembre 2006 relative au système commun de taxe sur la valeur ajoutée.

III. - Pour l'assujetti débutant son activité en cours d'année, les plafonds mentionnés au I et au A du I bis de l'article 293 B et au 1° du I de l'article 293 B bis sont ajustés à proportion de la durée de l'année restant à courir à la date du début d'activité.
```

### VAT-Q004

OfficialServicePublicF21746 franchise/startup; https://entreprendre.service-public.gouv.fr/vosdroits/F21746; actual original read 2026-10-29. Native LF [119, 126]; reader SHA256 `d9a5db3b04694dd3bd888efed56a5450a3be8a6ef7514c38b57a72ef6c349896`. Inherited actual C selected reading, exact read-scope records preserved

```text
 Prorata en cas de démarrage de l'activité
 S'il s'agit de l'année de démarrage de l'activité de l'entreprise, son CA : titleContent doit être ajusté et calculé au prorata de son temps d'activité (entre la date de démarrage et le dernier jour de l'année) afin d'obtenir un CA sur une année complète (les seuils de TVA ne se calculent que sur une année complète).
 La formule est la suivante :
 (CA x nombre de jours dans une année ) / nombre de jours entre le démarrage et le dernier jour de l'année .
 Ce calcul permet de déterminer si l'entreprise peut continuer à bénéficier de la franchise en base de TVA l'année suivante.
 Exemple :
 Si l'entreprise démarre son activité le 14 mai 2025 et qu'elle avait réalisé un chiffre d'affaires de 82 000 € entre le 14 mai 2025 et le 31 décembre 2025, il aurait fallu calculer son chiffre d'affaires de l'année 2025 au prorata du temps d'activité. Ainsi, pour l'année 2025, le CA : titleContent calculé au prorata du temps d'exploitation est égal au CA de l'entreprise multiplié par le nombre de jours dans une année et divisé par le nombre de jours entre la date de création de l'entreprise et la fin de l'année : ( 82 000 € x 365)/232 = 129 009 € .
 Le chiffre d'affaires de l'entreprise calculé au prorata est supérieur à 93 500 € . L’entreprise ne peut donc plus bénéficier de la franchise en base de TVA en 2026.
```

### VAT-Q005

Retained DGFiP regimes page, archived29September2026; explicit startup countertext and stale RSI figures; https://www.impots.gouv.fr/professionnel/les-regimes-dimposition-la-tva; actual original read 2026-10-29. Native LF [59, 65]; reader SHA256 `7d16b3501529f33ed67596402ed6078933c72ddee683f2cd61efbe3d03cb72b3`. Inherited actual C selected reading, exact read-scope records preserved

```text
 Ce régime d'imposition s'applique, de plein droit, aux entreprises et aux sociétés dont le chiffre d'affaires au titre de l'exercice précédent n'excède pas :
 • 85 000 € pour les opérations de ventes de marchandises, objets, fournitures et denrées à emporter ou à consommer sur place, et la fourniture de logement.Les prestations d'hébergement à retenir sont celles qui ne sont pas exonérées de la TVA en application du 4° de l' article 261 D du Code général des impôts (CGI) (article L. 221-21 du Code des impositions des biens et des services (CIBS) 1 ). Il s'agit notamment des prestations fournies dans les hôtels et les résidences de tourisme classés ou dans les villages de vacances classés ainsi que celles fournies dans les établissements où l'exploitant offre, en plus de l'hébergement, des prestations para-hôtelières ;
 • 37 500€ pour les prestations de service.
 Pour les entreprises nouvelles, il n’y a pas lieu de proratiser sur la période d’exploitation le chiffre d’affaires de l’année de création. Par ailleurs, la franchise est de droit la première année d'activité dès lors que le chiffre d'affaires n’excède pas 93 500 € ou 41 250 €. Ces montants correspondent aux limites majorées de la franchise en base.
 Par contre, pour déterminer si la franchise est applicable l’année qui suit la création, les limites de 93 500 € et 41 250 € doivent être ajustées à proportion de la durée de l'année restant à courir à la date du début d'activité .
 En cours d'activité, la franchise en base cesse de s’appliquer au cours de l’exercice si le chiffre d’affaires de l’année en cours dépasse 93 500 € pour les ventes et 41 250 € pour les prestations de service (les assujettis deviennent redevables de la TVA à compter de la date de dépassement de l’un de ces seuils). 
 Ces seuils sont applicables à compter du 1er janvier 2025.
```

### VAT-Q006

CGI287; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191928/2026-10-29; actual original read 2026-10-29. Native LF [37, 76]; reader SHA256 `9527d21548840fe360b86cfe9076ab08c53b763fcbfddb8a4d2760fab5304236`. Inherited actual C selected reading, exact read-scope records preserved

```text
Article 287

EN VIGUEUR DEPUIS LE 01 JANVIER 2025

Modifié par LOI n°2023-1322 du 29 décembre 2023 - art. 82 (V)


1. Tout redevable de la taxe sur la valeur ajoutée identifié conformément aux dispositions combinées des articles 286 ter et 286 ter A est tenu de remettre au service des impôts dont il dépend et dans le délai fixé par arrêté une déclaration conforme au modèle prescrit par l'administration.

2. Les redevables soumis au régime réel normal d'imposition déposent mensuellement la déclaration visée au 1 indiquant, d'une part, le montant total des opérations réalisées, d'autre part, le détail des opérations taxables. La taxe exigible est acquittée tous les mois.

Ces redevables peuvent, sur leur demande, être autorisés, dans des conditions qui sont fixées par arrêté du ministre de l'économie et des finances, à disposer d'un délai supplémentaire d'un mois.

Lorsque la taxe exigible annuellement est inférieure à 4 000 €, ils sont admis à déposer leurs déclarations par trimestre civil.

3. Les redevables placés sous le régime simplifié d'imposition prévu à l'article 302 septies A, à l'exception de ceux mentionnés aux 3 bis et 3 ter, déposent au titre de chaque exercice une déclaration qui détermine la taxe due au titre de la période et le montant des acomptes semestriels pour la période ultérieure.

Des acomptes semestriels sont versés en juillet et en décembre. Ils sont égaux, respectivement, à 55 % et 40 % de la taxe due au titre de l'exercice précédent avant déduction de la taxe sur la valeur ajoutée relative aux biens constituant des immobilisations. Le complément d'impôt éventuellement exigible est versé lors du dépôt de la déclaration annuelle mentionnée au premier alinéa.

S'il estime que le montant des acomptes déjà versés au titre de l'exercice est égal ou supérieur au montant de la taxe qui sera finalement due, le redevable peut se dispenser de nouveaux versements en remettant au comptable chargé du recouvrement de ladite taxe, avant la date d'exigibilité du prochain versement à effectuer, une déclaration datée et signée.

S'il estime que la taxe due à raison des opérations réalisées au cours d'un semestre, après imputation de la taxe sur la valeur ajoutée relative aux biens constituant des immobilisations, est inférieure d'au moins 10 % au montant de l'acompte correspondant, calculé selon les modalités prévues au deuxième alinéa, le redevable peut diminuer à due concurrence le montant de cet acompte, en remettant au comptable chargé du recouvrement, au plus tard à la date d'exigibilité de l'acompte, une déclaration datée et signée. Si ces opérations ont été réalisées au cours d'une période inférieure à six mois, la modulation n'est admise que si la taxe réellement due est inférieure d'au moins 10 % à l'acompte réduit au prorata du temps.

S'il estime que la taxe sera supérieure d'au moins 10 % à celle qui a servi de base aux acomptes, il peut modifier le montant de ces derniers.

Les redevables sont dispensés du versement d'acomptes lorsque la taxe due au titre de l'exercice précédent, avant déduction de la taxe sur la valeur ajoutée relative aux biens constituant des immobilisations, est inférieure à 1 000 €. Dans ce cas, le montant total de l'impôt exigible est acquitté lors du dépôt de la déclaration annuelle mentionnée au premier alinéa.

Les nouveaux redevables sont autorisés, lors de leur première année d'imposition, à acquitter la taxe sur la valeur ajoutée par acomptes semestriels dont ils déterminent eux-mêmes le montant mais dont chacun doit représenter au moins 80 % de l'impôt réellement dû pour le semestre correspondant.

Les conditions d'application du présent 3, notamment les modalités de versement et de remboursement des acomptes, sont fixées par décret en Conseil d'Etat.

3 bis. Les redevables dont le chiffre d'affaires est inférieur aux seuils prévus aux 1° et 2° de l'article L. 162-4 du code des impositions sur les biens et services et dont le montant de la taxe exigible au titre de l'année précédente est supérieur à 15 000 € déposent mensuellement la déclaration mentionnée au 1 du présent article.

3 ter. Les redevables placés sous le régime simplifié d'imposition prévu à l'article 302 septies A déposent mensuellement la déclaration mentionnée au 1 du présent article dès lors qu'ils réalisent des acquisitions intracommunautaires, des importations ou des sorties des régimes suspensifs mentionnés au 2° du I de l'article 277 A. La première de ces déclarations récapitule l'ensemble des opérations pour lesquelles la taxe est devenue exigible depuis le début de l'exercice en cours.

Toutefois, lorsque la taxe exigible annuellement est inférieure à 4 000 €, ils sont admis à déposer leurs déclarations par trimestre civil.

4. En cas de cession ou de cessation d'une activité professionnelle, les redevables sont tenus de souscrire dans les trente jours la déclaration prévue au 1. Toutefois, ce délai est porté à soixante jours pour les entreprises placées sous le régime simplifié d'imposition.

5. Dans la déclaration prévue au 1, doivent notamment être identifiés :
```

### VAT-Q007

CGI287-3bis,3ter,4; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191928/2026-10-29; actual original read 2026-10-29. Native LF [68, 76]; reader SHA256 `9527d21548840fe360b86cfe9076ab08c53b763fcbfddb8a4d2760fab5304236`. Actual root targeted reread on29October2026; erroneous earlier selected range and inherited reading attribution are preserved in the sealed predecessor.

```text
3 bis. Les redevables dont le chiffre d'affaires est inférieur aux seuils prévus aux 1° et 2° de l'article L. 162-4 du code des impositions sur les biens et services et dont le montant de la taxe exigible au titre de l'année précédente est supérieur à 15 000 € déposent mensuellement la déclaration mentionnée au 1 du présent article.

3 ter. Les redevables placés sous le régime simplifié d'imposition prévu à l'article 302 septies A déposent mensuellement la déclaration mentionnée au 1 du présent article dès lors qu'ils réalisent des acquisitions intracommunautaires, des importations ou des sorties des régimes suspensifs mentionnés au 2° du I de l'article 277 A. La première de ces déclarations récapitule l'ensemble des opérations pour lesquelles la taxe est devenue exigible depuis le début de l'exercice en cours.

Toutefois, lorsque la taxe exigible annuellement est inférieure à 4 000 €, ils sont admis à déposer leurs déclarations par trimestre civil.

4. En cas de cession ou de cessation d'une activité professionnelle, les redevables sont tenus de souscrire dans les trente jours la déclaration prévue au 1. Toutefois, ce délai est porté à soixante jours pour les entreprises placées sous le régime simplifié d'imposition.

5. Dans la déclaration prévue au 1, doivent notamment être identifiés :
```

### VAT-Q008

CGIannexeII205–207; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069569/LEGISCTA000006179225/2026-10-29; actual original read 2026-10-29. Native LF [85, 132]; reader SHA256 `dd01aefa6fbc017e8487739d31f7b04486866c8769679f72d9225996a14594f1`. Inherited actual C selected reading, exact read-scope records preserved

```text
IV. – 1. Le coefficient d'admission d'un bien ou d'un service est égal à l'unité, sauf dans les cas décrits aux 2 à 4.

2. Le coefficient d'admission est nul dans les cas suivants :

1° Lorsque le bien ou le service est utilisé par l'assujetti à plus de 90 % à des fins étrangères à son entreprise ;

2° Lorsque le bien ou le service est relatif à la fourniture à titre gratuit du logement des dirigeants ou du personnel de l'entreprise, à l'exception de celui du personnel de gardiennage, de sécurité ou de surveillance sur les chantiers ou dans les locaux de l'entreprise ;

3° Lorsque le bien est cédé sans rémunération ou moyennant une rémunération très inférieure à son prix normal, notamment à titre de commission, salaire, gratification, rabais, bonification, cadeau, quelle que soit la qualité du bénéficiaire ou la forme de la distribution, sauf quand il s'agit de biens de très faible valeur. Un arrêté du ministre chargé du budget en fixe la valeur maximale ;

4° Lorsque le bien ou le service est utilisé pour des publicités prohibées par les articles L. 3323-2, L. 3323-4 et L. 3323-5 du code de la santé publique ;

5° Pour les prestations de transport de personnes et les prestations accessoires à ce transport, à l'exclusion de celles réalisées soit pour le compte d'une entreprise de transports publics de voyageurs, soit en vertu d'un contrat permanent de transport conclu par les entreprises pour amener leur personnel sur les lieux de travail ;

6° Pour les véhicules ou engins, quelle que soit leur nature, conçus pour transporter des personnes ou à usages mixtes, à l'exception de ceux :

a. Destinés à être revendus à l'état neuf ;

b. Donnés en location ;

c. Comportant, outre le siège du conducteur, plus de huit places assises et utilisés par des entreprises pour amener leur personnel sur les lieux du travail ;

d. Affectés de façon exclusive à l'enseignement de la conduite ;

e. De type tout terrain affectés exclusivement à l'exploitation des remontées mécaniques et des domaines skiables, dans des conditions fixées par décret ;

f. Acquis par les entreprises de transports publics de voyageurs et affectés de façon exclusive à la réalisation desdits transports ;

g. Aménagés pour le transport des équidés ;

7° Pour les éléments constitutifs, pièces détachées et accessoires des véhicules et engins mentionnés au premier alinéa du 6° ;

8° A l'exception des cas prévus au 1° bis du 4 de l'article 298 du code général des impôts :

a) Pour les carburéacteurs mentionnés au d du 1° du même 4 ;

b) Pour les produits pétroliers mentionnés au e du 1° du même 4 ;

9° Pour les biens acquis ou construits ainsi que les services acquis dont la valeur d'achat, de construction ou de livraison à soi-même est prise en compte pour l'application des dispositions du e du 1 de l'article 266 du code général des impôts ainsi que de l'article 297 A du code général des impôts ;

10° Pour les prestations de services de toute nature, notamment la location, afférentes aux biens dont le coefficient d'admission est nul en application des dispositions du 1° au 8°.

3. A l'exception des cas prévus au 1° bis du 4 de l'article 298 du code général des impôts, le coefficient d'admission est calculé en application des dispositions relatives à l'exclusion du droit à déduction fixées aux a, b et c du 1° du même 4 concernant, respectivement, les essences, les gazoles et le superéthanol E 85 et les gaz de pétrole et autres hydrocarbures présentés à l'état gazeux et le pétrole lampant.

4. (Abrogé).

V. – 1. L'assujetti peut, par année civile, retenir :

```

### VAT-Q009

CGIannexeII205–207; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069569/LEGISCTA000006179225/2026-10-29; actual original read 2026-10-29. Native LF [134, 153]; reader SHA256 `dd01aefa6fbc017e8487739d31f7b04486866c8769679f72d9225996a14594f1`. Inherited actual C selected reading, exact read-scope records preserved

```text

2° Pour l'ensemble de ses biens et services, un coefficient de taxation unique calculé dans les conditions du 3 du III.

Cette option est exercée séparément pour chacun des secteurs mentionnés au deuxième alinéa de l'article 209 et aux 1° à 5° du I du même article. Elle s'applique aux biens et services utilisés pour les besoins des opérations imposables de ce secteur.

2. Les quatre coefficients mentionnés au I sont arrondis par excès à la deuxième décimale. Ils sont définitivement arrêtés avant le 25 avril de l'année suivante ou le 31 décembre de l'année suivante pour ceux qui deviennent redevables de la taxe sur la valeur ajoutée en cours d'année.

Toutefois, lorsque l'option prévue au VI est exercée pour l'un des membres d'un assujetti unique, les coefficients mentionnés au I, compte tenu, le cas échéant, des arrondis prévus à l'alinéa ci-dessus, sont définitivement arrêtés avant le 25 mai de l'année suivante.

VI. – Lorsqu'il est recouru à l'option mentionnée au 2° du 1 du V pour l'un des membres d'un assujetti unique constitué en application de l'article 256 C du code général des impôts, cette option s'applique à l'ensemble des dépenses de ce membre. Dans ce cas, le rapport prévu au 1° du 3 du III pour la détermination du coefficient de taxation est ainsi établi :

a. Au numérateur, le montant total annuel du chiffre d'affaires afférent aux opérations ouvrant droit à déduction, y compris les subventions directement liées au prix de ces opérations, majoré du produit entre, d'une part, le montant total annuel du chiffre d'affaires afférent aux opérations effectuées par le membre à destination des autres membres de l'assujetti unique et qui auraient été imposables en l'absence de constitution de cet assujetti unique, en faisant abstraction du montant afférent aux opérations mentionnées au 3° du 3 du III, d'autre part, un coefficient de taxation de l'assujetti unique déterminé à partir de l'ensemble du chiffre d'affaires de ses opérations imposables ;

b. Au dénominateur, le montant total annuel du chiffre d'affaires afférent aux opérations imposables, y compris les subventions directement liées au prix de ces opérations, majoré du montant total annuel du chiffre d'affaires afférent aux opérations effectuées par le membre à destination des autres membres de l'assujetti unique et qui auraient été imposables en l'absence de constitution de cet assujetti unique, en faisant abstraction du montant afférent aux opérations mentionnées au 3° du 3 du III.




Conformément à l'article 3 du décret n° 2022-1033 du 20 juillet 2022, ces dispositions entrent en vigueur après consultation du comité consultatif de la taxe sur la valeur ajoutée mentionné à l'article 398 de la directive 2006/112/CE du Conseil du 28 novembre 2006 et, au plus tôt, le 1er janvier 2023.

```

### VAT-Q010

CGIannexeII205–207; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069569/LEGISCTA000006179225/2026-10-29; actual original read 2026-10-29. Native LF [168, 199]; reader SHA256 `dd01aefa6fbc017e8487739d31f7b04486866c8769679f72d9225996a14594f1`. Inherited actual C selected reading, exact read-scope records preserved

```text
I. – Sous réserve des dispositions qui suivent, la déduction opérée dans les conditions mentionnées aux articles 205 et 206 est définitivement acquise à l'entreprise.

II. – 1. Pour les biens immobilisés, une régularisation de la taxe initialement déduite est opérée chaque année pendant cinq ans, dont celle au cours de laquelle ils ont été acquis, importés, achevés, utilisés pour la première fois ou transférés entre secteurs d'activité constitués en application de l'article 209.

2. Chaque année, la régularisation est égale au cinquième du produit de la taxe initiale par la différence entre le coefficient de déduction de l'année et le coefficient de déduction de référence mentionné au 2 du V. Elle prend la forme d'une déduction complémentaire si cette différence est positive, d'un reversement dans le cas contraire.

3. Par dérogation à la durée mentionnée au 1 et à la fraction mentionnée au 2, cette régularisation s'opère pour les immeubles immobilisés par vingtième pendant vingt années.

Toutefois, pour les immeubles donnés en location dans les conditions prévues au 2 de l'article L. 313-7 du code monétaire et financier, cette durée est égale au nombre d'années qui courent jusqu'à l'échéance du contrat de bail, arrondi à l'entier supérieur, sans pouvoir excéder vingt années, et la régularisation s'opère par fractions égales à l'inverse de cette durée.

4. La régularisation doit être effectuée avant le 25 avril de l'année suivante. Aucune régularisation n'est effectuée si la différence entre le produit des coefficients d'assujettissement et de taxation de l'année, d'une part, et le produit des coefficients d'assujettissement et de taxation de référence mentionnés au 2 du V, d'autre part, n'est pas supérieure, en valeur absolue, à un dixième.

Lorsque l'option prévue au 2° du 1 du V de l'article 206 est exercée pour un membre d'un assujetti unique constitué en application de l'article 256 C du code général des impôts, la régularisation est effectuée avant le 25 mai de l'année suivante.

5. Les dispositions qui précèdent ne sont pas applicables :

1° Aux biens immobilisés dont le coefficient d'assujettissement de référence est nul ;

2° Aux immeubles livrés, acquis, apportés ou utilisés pour la première fois avant le 1er janvier 1996.

6. Pour la détermination des coefficients de référence mentionnés au 2 et au 4, il n'est pas tenu compte des dispositions du 1° et du 2° du 2 du V au titre de l'année où il est fait application de ces dispositions.

III. – 1. Une régularisation de la taxe initialement déduite et grevant un bien immobilisé est également opérée :

1° Lorsqu'il est cédé ou apporté, sans que cette opération soit soumise à la taxe sur le prix total, sur la valeur totale ou dans les conditions fixées à l'article 268 du code général des impôts, ou est transféré entre secteurs d'activité constitués en application de l'article 209 ;

2° Lorsqu'il est cédé ou apporté, et que cette opération est soumise à la taxe sur le prix total, sur la valeur totale ou dans les conditions fixées à l'article 268 du code général des impôts ;

3° Lorsque la réglementation modifie la valeur de son coefficient d'admission en cours d'utilisation ;

4° Lorsqu'il vient en cours d'utilisation à être utilisé à des opérations ouvrant droit à déduction ou, sous réserve du 5°, lorsqu'il cesse d'être utilisé à des opérations ouvrant droit à déduction ;

```

### VAT-Q011

CGIannexeII205–207; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069569/LEGISCTA000006179225/2026-10-29; actual original read 2026-10-29. Native LF [201, 250]; reader SHA256 `dd01aefa6fbc017e8487739d31f7b04486866c8769679f72d9225996a14594f1`. Inherited actual C selected reading, exact read-scope records preserved

```text

2. Cette régularisation est égale à la somme des régularisations qui auraient été effectuées jusqu'au terme de la période de régularisation en application des 1,2,3 et 5 du II, en considérant que pour chacune des années restantes de cette période :

1° Dans les cas visés au 1° du 1, le coefficient de taxation est égal à zéro ;

2° Dans les cas visés au 2° du 1, le coefficient de déduction est égal à l'unité ;

3° Dans le cas visé au 3° du 1, le coefficient d'admission est égal à sa nouvelle valeur ;

4° Dans les cas visés au 4° du 1, le coefficient de taxation est égal à sa nouvelle valeur ;

5° Dans le cas visé au 5° du 1, le coefficient d'assujettissement est égal à zéro.

3. Dans les cas visés au 1° du 1, sous réserve que le bien constitue également une immobilisation pour le bénéficiaire de la cession, de l'apport ou du transfert, celui-ci peut déduire une fraction du montant de taxe sur la valeur ajoutée ayant grevé initialement le bien, à proportion du rapport entre le nombre d'années restant à courir, pour le cédant ou l'apporteur, jusqu'au terme de la période de régularisation et le nombre d'années total de celle-ci. A cette fin, le cédant ou l'apporteur délivre au bénéficiaire une attestation mentionnant le montant de la taxe qu'il est en droit de déduire. Cette déduction est opérée dans les conditions prévues à l'article 206.

4. Les dispositions des 1 à 3 ne sont pas applicables :

1° Aux cessions ou apports dispensés de taxe sur la valeur ajoutée en application de l'article 257 bis du code général des impôts ;

2° Aux biens immobilisés :

a. Qui ont été volés ou détruits, dès lors qu'il est justifié du vol ou de la destruction ;

b. Dont le coefficient d'assujettissement de référence est nul.

IV. – 1. (alinéa abrogé)

2. Lorsqu'un bien en stock, ou un bien immobilisé non encore utilisé, vient à être utilisé à des opérations ouvrant droit à déduction, la taxe initiale peut être déduite à proportion du coefficient de déduction résultant de ce changement.

3. Pour l'application du II et des 1° et 2° du 1 du III, un immeuble ou une fraction d'immeuble en stock est considéré comme immobilisé lorsque, au 31 décembre de la deuxième année qui suit celle au cours de laquelle est intervenu l'achèvement de l'immeuble, il est utilisé pendant plus d'un an pour une opération relevant d'une activité économique mentionnée à l'article 256 A du code général des impôts.

V. – 1. La taxe initiale s'entend, selon le cas, de la taxe mentionnée au 1 du II de l'article 271 du code général des impôts ou de la fraction de taxe mentionnée sur les attestations prévues au 3 du III du présent article.

2. Les coefficients d'assujettissement, de taxation et d'admission de référence sont initialement égaux aux coefficients retenus pour le calcul de la déduction opérée en application de l'article 206 lors de l'acquisition, de l'importation ou de la livraison à soi-même du bien. Le cas échéant :

1° Après chaque déduction opérée en application des dispositions du 3 du III du présent article lors d'un transfert entre secteurs d'activité mentionné au 1° du 1 de ce même III, ils prennent la valeur des coefficients retenus pour la détermination du montant de cette déduction ;

2° Après chaque régularisation opérée en application des dispositions des 3° à 5° du 1 du III du présent article, ils prennent la valeur des coefficients mentionnés respectivement aux 3° à 5° du 2 de ce même III.

Le coefficient de déduction de référence est égal au produit des coefficients d'assujettissement, de taxation et d'admission de référence résultant des dispositions qui précèdent.

VI. – Le montant de la taxe dont la déduction a déjà été opérée doit être reversé dans les cas suivants :

1° Lorsque les marchandises ont disparu ;

2° Lorsque les biens ou services ayant fait l'objet d'une déduction de la taxe qui les avait grevés ont été utilisés pour une opération qui n'est pas effectivement soumise à l'impôt.

Ce reversement doit être opéré avant le 25 du mois qui suit celui au cours duquel l'événement qui motive le reversement est intervenu. Toutefois, ces reversements ne sont pas exigés lorsque les biens ont été détruits avant toute utilisation ou cession, ou volés, et qu'il est justifié de cette destruction ou de ce vol.


```

### VAT-Q012

BOI-TVA-DED-30-30-20 vehicle exclusions/exceptions; https://bofip.impots.gouv.fr/bofip/1192-PGP.html; actual original read 2026-10-29. Native LF [67, 82]; reader SHA256 `735a0a2286708f6bcb6468c6a31847d1acd513c83f9b303e114a84b01dd4d58d`. Inherited actual C selected reading, exact read-scope records preserved

```text
 1
 Aux termes du 6° du 2 du IV de l’ article 206 de l’annexe II au code général des impôts (CGI) , sont exclus du droit à déduction de la taxe sur la valeur ajoutée (TVA) les véhicules ou engins, quelle que soit leur nature, conçus pour transporter des personnes ou à usages mixtes, qui constituent une immobilisation ou, dans le cas contraire, qui ne sont pas destinés à être revendus à l’état neuf.
 Il en est de même des éléments constitutifs, des pièces détachées et accessoires de ces véhicules et engins (CGI, ann. II, art. 206, IV-2-7°).
 Les biens visés par cette exclusion doivent donc répondre simultanément à deux sortes de critères fondés sur :
 les caractéristiques du véhicule ;
 la destination du véhicule dans l’entreprise.
 A. Caractéristiques des véhicules exclus
 10
 Il s’agit de véhicules de toute nature conçus pour transporter des personnes ou à usages mixtes. Un véhicule conçu pour un usage mixte s’entend d’un véhicule conçu à la fois pour le transport de personnes et le transport de marchandises.
 L’exclusion est déterminé sur la base d’un critère de conception, indépendamment de l’usage effectif du véhicule. Ce critère est apprécié à la date de l’acquisition ou de la prise en location. Par conséquent, une éventuelle transformation des caractéristiques techniques du véhicule réalisée postérieurement à l’acquisition reste sans conséquence sur l’application du dispositif d’exclusion du droit à déduction de la taxe y afférente.
 Pour apprécier si un véhicule ou un engin a été conçu pour le transport des personnes ou pour un usage mixte, au sens des dispositions du 6° du 2 du IV de l’article 206 de l’annexe II au CGI, le Conseil d’État a jugé qu’il y a lieu non pas de se référer aux conditions d’utilisation du véhicule mais de rechercher, compte tenu de ses caractéristiques lors de l’acquisition, l’usage auquel il est normalement destiné.
 Aussi, ne sauraient être regardés comme conçus pour transporter des personnes, les véhicules ou engins, terrestres, maritimes ou aériens, qui, même s’ils ne peuvent se déplacer sans la présence à leur bord d’un conducteur, d’un pilote ou d’un équipage, ont, en raison des caractéristiques de leur conception, une autre fonction que celle de transporter des personnes et constituent, nécessairement, eu égard à cette fin, une immobilisation utile à l’exploitation d’une entreprise dont les opérations sont soumises à la TVA.
 Après avoir souverainement relevé les caractéristiques techniques spécifiques des scooters des neiges acquis par la société, tenant à l’importance de leur poids, de leurs dimensions, de leur puissance, de leur vitesse et de leur équipement, lesquelles n’étaient pas contestées par le ministre, et avoir estimé sans influence sur la qualification à apporter aux engins la circonstance qu’ils aient été munis d’un second siège permettant le transport d’un passager, la cour n’a ni inexactement qualifié les faits ni méconnu la portée des dispositions précitées en jugeant que ces véhicules n’avaient pas été conçus pour le transport des personnes ou à usages mixtes et ouvraient droit au bénéfice de la déduction de la TVA ( CE, décision du 25 novembre 2009, n° 319649 ).
 20
 Dans le secteur automobile, le critère de conception est d’abord apprécié sur la manière dont le véhicule est catégorisé au niveau européen et, le cas échéant, national pour les besoins de sa réception et de son immatriculation. Pour plus de précisions sur ces notions, il convient de se reporter aux I et II § 10 à 290 du BOI-AIS-MOB-10-10 .
 En particulier, la catégorie européenne (M, N, T, C, R, S et L) est une clef d’entrée déterminante de l’analyse.
```

### VAT-Q013

BOI-TVA-DED-30-30-20 vehicle exclusions/exceptions; https://bofip.impots.gouv.fr/bofip/1192-PGP.html; actual original read 2026-10-29. Native LF [108, 121]; reader SHA256 `735a0a2286708f6bcb6468c6a31847d1acd513c83f9b303e114a84b01dd4d58d`. Inherited actual C selected reading, exact read-scope records preserved

```text
 Les catégories de véhicules utilitaires qui ne sont pas concernées par l’exclusion du droit à déduction sont les catégories L2e-U (cyclomoteurs à trois roues conçus à des fins utilitaires), L5e-B (tricycles utilitaires), L6e-BU (quadrimobiles légers à fins utilitaires) et L7e-CU (quadrimobiles lourds à fins utilitaires).
 Les véhicules similaires aux véhicules de catégorie L mais qui ne sont pas homologués sont traités comme les véhicules homologués dont ils se rapprochent le plus. Ainsi, sont exclus du droit à déduction les « quads » de loisir ou les cycles, à assistance électriques ou non, sauf lorsqu’ils disposent d’aménagement spécifiques caractérisant une conception exclusive pour le transport de marchandises.
 Exemple : Les cycles dits « vélos cargo » caractérisés par un biporteur propre au transport de volumes importants de marchandises, pouvant disposer d’un plancher plat ou d’un benne basculante.
 50
 Les véhicules agricoles et forestiers, regroupés dans les catégories T, C, R et S ne sont pas concernés par l’exclusion du droit à déduction.
 Il en est de même des machines agricoles automotrices n’ayant pas fait l’objet d’une réception européenne. Il s’agit des véhicules faisant l’objet d’une réception nationale en application du l’ article 13 de l’arrêté du 19 décembre 2016 modifié relatif à la réception des véhicules agricoles et forestiers et de leurs systèmes, composants et entités techniques dont le genre national abrégé est « MAGA ».
 Remarque : Sont ainsi concernés notamment les quads agricoles.
 55
 Les mêmes principes s’appliquent pour les véhicules ne relevant pas des catégories européennes mentionnées au I-A § 20 à 50 , quels que soient les modes de transport (terrestre, y compris hors-route, aérien, maritime etc.), indépendamment du mode de propulsion (bicyclettes, trottinettes, etc.).
 57
 Les dépenses d’aménagement des véhicules exclus du droit à déduction suivent le même régime que ce dernier. La TVA qui les grèvent ne peut donc être déduite lorsque le véhicule est conçu pour le transport de personnes ou à usage mixte.
 58
 Compte tenu des précisions doctrinales exposées au I-A § 10 à 57 , les réponses ministérielles suivantes sont rapportées : RM Gouffier Valente n° 4630, JO AN du 18 avril 2023, p. 3619 ; RM Meslot n° 77620, JO AN du 1 er juin 2010, p. 6103 ; RM Remiller n° 74835, JO AN du 25 mai 2010, p. 5816 ; RM Meslot n° 58198, JO AN du 6 avril 2010, p. 3957 ; RM Jacque n° 26914, JO AN du 22 mars 2005, p. 2989 ; RM Martin n° 54973, JO AN du 8 mars 2005, p. 2431 .
 B. Destination des véhicules exclus
```

### VAT-Q014

BOI-TVA-DED-30-30-20 vehicle exclusions/exceptions; https://bofip.impots.gouv.fr/bofip/1192-PGP.html; actual original read 2026-10-29. Native LF [123, 160]; reader SHA256 `735a0a2286708f6bcb6468c6a31847d1acd513c83f9b303e114a84b01dd4d58d`. Inherited actual C selected reading, exact read-scope records preserved

```text
 Sont exclus du droit à déduction les véhicules dont les caractéristiques sont énumérées au I-A § 10 et 20 et qui constituent des immobilisations pour l’entreprise.
 Tel est le cas, par exemple, des voitures particulières utilisées par les entreprises industrielles ou commerciales pour assurer le transport de leur personnel.
 70
 En revanche, l’exclusion ne concerne pas les véhicules qui présentent le caractère d’éléments de stock. Les concessionnaires ainsi que tous les négociants opèrent donc dans les conditions normales la déduction de la taxe ayant grevé l’achat de tout véhicule qu’ils destinent à la revente à l’état neuf.
 II. Exceptions à la mesure d’exclusion
 (80-90)
 A. Voiliers exclusivement conçus pour la compétition
 100
 Certains voiliers sont exclusivement conçus pour les compétitions.
 Compte tenu des spécificités de leur construction, des autorisations de navigation particulières qu’ils requièrent et de l’impossibilité de leur délivrer l’homologation dans la catégorie des navires de plaisance, ces voiliers ne peuvent pas être regardés comme des véhicules ou engins de transport des personnes au sens du 6° du 2 du IV de l’article 206 de l’annexe II au CGI ( CE, décision du 21 décembre 1994, n° 134131 et 134137 et CE, décision du 21 décembre 1994, n° 134133 ).
 Si des voiliers de compétition sont utilisés pour les besoins d’opérations ouvrant droit à déduction, la TVA qui les grève peut donc être déduite dans les conditions de droit commun.
 B. Véhicules ou engins comportant, outre le siège du conducteur, plus de huit places assises et qui sont utilisés par les entreprises pour amener le personnel sur les lieux du travail
 110
 Bénéficient ainsi du droit à déduction les véhicules des catégories M2 ou M3 utilisés pour acheminer le personnel sur le lieu de travail, tant pour le trajet aller que pour le trajet retour.
 Remarque : Le versement d’une participation de quelque importance qu’elle soit de la part des travailleurs pour l’utilisation de ces transports ne fait pas obstacle à la déduction, mais le montant de cette participation est à inclure par l’entreprise dans les opérations imposables.
 C. Véhicules ou engins acquis par les entreprises de transports publics de voyageurs et affectés de façon exclusive à la réalisation desdits transports
 120
 Toute entreprise de transports publics peut opérer la déduction de la taxe ayant grevé les véhicules ou engins qu’elle utilise exclusivement pour ces transports, qu’il s’agisse de véhicules automobiles (quelle que soit la catégorie), de bateaux de plaisance, d’aéronefs, de remonte-pentes ou de téléphériques. La déduction est strictement limitée aux véhicules que ces entreprises utilisent effectivement pour assurer la réalisation de leurs services de transports et ne s’étend pas aux véhicules qu’elles utilisent pour leurs besoins propres.
 130
 La déduction est également subordonnée à l’affectation exclusive desdits véhicules à une activité de transport public de personnes.
 Ainsi, les agences de voyages qui utilisent des véhicules de transport de personnes leur appartenant ne peuvent opérer la déduction de la taxe afférente à ces véhicules que si elles les affectent exclusivement à une activité de transport de voyageurs distincte de leur activité d’agence de voyages et donnant lieu à une imposition portant sur le prix total du transport réclamé à leurs clients (sur le régime des transporteurs publics routiers de voyageurs qui organisent des voyages, il convient de se reporter au II § 400 à 430 du BOI-TVA-SECT-60 ).
 Toutefois, lorsque les entreprises de transport public de voyageurs utilisent des véhicules visés au 6° du 2 du IV de l’ article 206 de l’annexe II au CGI pour réaliser, à titre accessoire ou occasionnel, des prestations de transports de marchandises ou de messageries passibles de la TVA au taux normal, cette utilisation occasionnelle ou accessoire n’est pas de nature à remettre en cause le droit à déduction de la taxe afférente à l’acquisition des véhicules concernés.
 140
 La règle exposée au II-C § 130 est applicable aux transports publics particuliers de personnes régi par le titre II du livre Ier de la troisième partie du code des transports (taxis, voitures de transport avec chauffeur, véhicules à deux ou trois roues).
 Pour les intéressés, il y a lieu de considérer que les transports de marchandises ont un caractère accessoire ou occasionnel lorsque les recettes correspondantes sont inférieures à 7 630 € toutes taxes comprise (TTC) par an et n’excédant pas 30 % des recettes totales annuelles TTC.
 Pour l’appréciation du seuil de 7 630 €, le chiffre d’affaires annuel se rapportant à des transports de marchandises s’apprécie par véhicule. En cas d’exploitation de plusieurs véhicules par une même personne, le seuil est multiplié par le nombre de ces véhicules et apprécié globalement sur l’ensemble de la flotte.
 150
 Lorsqu’une entreprise exploite, d’une part, des véhicules destinés au transport de marchandises et, d’autre part, des véhicules utilisés accessoirement pour le transport de marchandises, il ne doit pas être tenu compte, aux deux termes du rapport servant à apprécier le seuil de 30 % mentionné au II-C § 130 et 140 , des recettes réalisées par les véhicules exclusivement destinés au transport de marchandises.
 160
 Le dépassement des limites prescrites a pour conséquence :
 d’exclure totalement du droit à déduction les véhicules acquis au cours de l’année civile correspondante ;
 d’exclure d’une fraction du droit à déduction pour les véhicules en cours d’utilisation dans les conditions prévues au 3° du 2 du III de l’ article 207 de l’annexe II au CGI .
 La diminution du chiffre d’affaires en deçà des limites autorise un droit à déduction dans les mêmes conditions.
 170
 Enfin, il est précisé que l’expression entreprise de « transports publics » ne saurait viser les entreprises (exploitants de supermarchés, hôteliers, etc.) qui affectent des véhicules conçus pour le transport de personnes ou à usage mixte, à l’usage de leur clientèle.
 180
 Les véhicules aménagés en corbillards, utilisés exclusivement à des transports funéraires par les entrepreneurs de pompes funèbres tant pour le transport des corps que pour le transport des familles, ouvrent droit à déduction de la taxe ayant grevé leur acquisition ( RM Durr n° 9821, JO AN du 26 avril 1982, p. 1712 [PDF - 10,4 Mo] ).
 Par ailleurs, l’exclusion du droit à déduction prévue au 6° du 2 du IV de l’article 206 de l’annexe II au CGI pour les véhicules de transports n’est pas applicable aux ambulances ou aux véhicules de transports sanitaires légers affectés exclusivement à l’activité taxable de transports de malades ou de blessés.
```

### VAT-Q015

BOI-BIC-CHG-20-30-10 optional low-value equipment expense tolerance; https://bofip.impots.gouv.fr/bofip/2109-PGP.html; actual original read 2026-10-29. Native LF [65, 116]; reader SHA256 `26d13731d12d38122666035ef4b37c4b0906702f22e4afd15e21fc05781211b1`. Inherited actual C selected reading, exact read-scope records preserved

```text
 Sur le plan comptable, l’article 212-6 du
 Plan comptable général prévoit que les éléments d’actif non significatifs peuvent ne pas être inscrits au bilan. Dans ce cas, ces
éléments sont comptabilisés en charges de l’exercice.
 I. Petit matériel et outillage
 A. Petit outillage à main
 10
 Il est admis que le petit outillage à main de faible valeur (marteaux, pinces, etc.) qui s'use
rapidement peut être entièrement amorti dès l'année de son acquisition, ce qui revient, en pratique, à le comptabiliser dans des comptes de charges.
 B. Petits matériels et outillages d'une valeur unitaire hors taxes n'excédant pas 500 euros
 20
 Les entreprises sont également autorisées à comprendre parmi leurs charges immédiatement
déductibles le prix d'acquisition des matériels et outillages d'une valeur unitaire hors taxes n'excédant pas 500 €.
 Les matériels et outillages pouvant bénéficier de cette tolérance sont ceux qui répondent à la
définition du matériel et de l'outillage à inscrire aux comptes 2154 et 2155 du Plan comptable général . Il s'agit en fait de
l'ensemble des objets, instruments et machines avec ou par lesquels :
 - on extrait, transforme ou façonne les matériels ou fournitures ;
 - on fournit les services qui sont l'objet même de la profession exercée.
 Il est précisé que cette seconde catégorie exclut le matériel de transport qui doit être
inscrit dans le compte d'actif approprié.
 C'est ainsi qu'un extincteur, dont le prix d'acquisition n'excède pas 500 € hors taxes peut,
en principe, être admis immédiatement en charge.
 Il en est de même en ce qui concerne les petits chariots à roulette utilisés par les clients
des magasins en libre service.
 Le dépassement du plafond de 500 € est apprécié le cas échéant en considération du prix global
de l'ensemble des éléments composant le matériel ou l'outillage.
 Par exemple, le prix à retenir pour l'achat d'un système antivol comprenant dans un magasin
des portiques de détection associés à des étiquettes attachées aux produits vendus et à des détacheurs est égal à la somme des prix d'acquisition de l'ensemble des étiquettes, des portiques et des
détacheurs, dès lors que les étiquettes participent indissociablement avec les portiques et les détacheurs au même système antivol.
 II. Matériels et mobiliers de bureau d'une valeur unitaire hors taxes n'excédant pas 500 euros
 30
 Les entreprises sont admises à comprendre dans leurs charges immédiatement déductibles les
matériels de bureau et mobiliers dont le prix d'achat unitaire hors taxes n'excède pas 500 €.
 Cette tolérance concerne, en pratique, les dépenses de menus équipements de bureau (tels que
corbeilles à papier, agrafeuses, pèse-lettres, timbres-dateurs, corbeilles à correspondance, boîtes à fiches, etc.) et, les dépenses d'acquisition de meubles « meublants » de bureau et de mobilier de
magasins commerciaux, dont les achats au cours d'un même exercice sont limités, pour un bien déterminé, à un petit nombre d'unités
( RM BUR n° 66314, JO AN du 10 décembre 2001 p. 7080 ).
 Les acquisitions en cause doivent donc résulter du renouvellement courant du mobilier
installé. La mesure n'est notamment pas applicable à l'équipement initial en mobilier d'un immeuble de bureaux, d'un restaurant ou d'un magasin commercial, ni au renouvellement complet de ce mobilier,
même si la valeur unitaire de chaque meuble est inférieure à 500 € hors taxes. Cette tolérance demeure cependant applicable lorsque l'équipement initial ou le renouvellement complet n'excède pas cette
limite.
 Si un bien déterminé se compose de plusieurs éléments qui peuvent être achetés séparément
(meubles de rangement modulables par exemple), il y a lieu de prendre en considération le prix global de ce bien, et non la valeur de chaque élément, pour apprécier la limite de 500 € prévue
ci-dessus.
 III. Logiciels d'une valeur unitaire hors taxes n'excédant pas 500 euros
 40
 Cette tolérance est aussi applicable aux dépenses d'acquisition de logiciels d'une valeur
unitaire hors taxes n'excédant pas 500 €.
 La comptabilisation en charge de ces dépenses est exclusive du régime de l'amortissement
exceptionnel sur douze mois prévu au II de l' article 236 du code général des impôts (CGI) .
 Le 6° du I de
l' article
32 de la loi n° 2016-1917 du 29 décembre 2016 de finances pour 2017 abroge le II de l' article 236 du CGI , de sorte que les
```

### VAT-Q016

BOI-TVA-DED-30-30-40 fuel/jetfuel; https://bofip.impots.gouv.fr/bofip/1194-PGP.html; actual original read 2026-10-29. Native LF [140, 164]; reader SHA256 `64020ec2492176fea413bffa44a120586b91e23c5530a9f0e5bec114b317911b`. Inherited actual C selected reading, exact read-scope records preserved

```text
 210
 Cette limite est fixée à 50 % du montant de la taxe pour les produits utilisés dans des véhicules ou engins exclus du droit à déduction, ou dans des véhicules ou engins pris en location quand le preneur ne peut pas déduire la taxe relative à cette location.
 C. Carburéacteurs
 220
 Le d du 1° du 4 de l' article 298 du CGI exclut du droit à déduction les carburéacteurs utilisés pour les aéronefs et engins qui n'ouvrent pas droit à déduction ou pour la location de ces aéronefs et engins.
 230
 Sont concernés les carburéacteurs, des types essence ou pétrole lampant, repris au tableau B de l' article 265 du C. douanes sous les indices d'identification 13 bis, 13 ter, 17 bis et 17 ter.
 L'exclusion du droit à déduction concerne les carburéacteurs utilisés pour les aéronefs et engins qui n'ouvrent pas droit à déduction de la taxe en application des dispositions de l' article 273 du CGI et du 6° et du 10° du 2 du IV de l' article 206 de l'annexe II au CGI . Il en est de même des carburéacteurs utilisés dans des aéronefs et engins pris en location quand le preneur ne peut pas déduire la taxe relative à cette location.
 Ainsi, aucune déduction ne peut être exercée pour les carburéacteurs consommés dans des avions de tourisme ou d'affaires, des hélicoptères, même s'ils sont utilisés pour des opérations de photographie, prises de vues, publicité, relevés topographiques ou géodésiques.
 240
 En revanche, les autres utilisations des carburéacteurs ouvrent droit à déduction de la taxe. Tel est le cas pour ceux consommés dans les aéronefs ou engins acquis par les entreprises de transports publics de voyageurs et affectés de façon exclusive à la réalisation de ces transports.
 En outre, ouvrent droit à déduction les carburéacteurs consommés :
 - dans les aéronefs conçus pour le transport du fret (avions-cargos, notamment) et les hélicoptères utilisés de façon constante par les entreprises spécialisées, soit pour la manutention de matériel, soit pour le transport du personnel de tierces entreprises ;
 - dans les aéronefs ou engins affectés de façon exclusive à l'enseignement de la conduite.
 D. Lubrifiants
 250
 Le e du 1° du 4 de l' article 298 du CGI prévoit que sont exclus du droit à déduction les produits pétroliers utilisés pour la lubrification des véhicules et engins exclus du droit à déduction, ainsi que des véhicules ou engins pris en location quand le preneur ne peut pas déduite la taxe y relative.
 260
 Sont concernées les huiles, préparations et graisses lubrifiantes mentionnées au tableau B de l' article 265 du C. douanes .
 270
 L'exclusion concerne les produits pétroliers utilisés pour la lubrification des véhicules ou engins qui n'ouvrent pas droit à déduction. Elle s'applique également si ces produits pétroliers sont utilisés dans des véhicules ou engins pris en location quand le preneur ne peut pas déduire la taxe relative à cette location ( CGI, art. 273 et CGI, ann. II, art. 206, IV-2- 6°et 10° ; se reporter également aux BOI-TVA-DED-30-30-20 et BOI-TVA-DED-30-30-70 ).
 280
 En revanche, la déduction de la TVA est autorisée pour les produits pétroliers utilisés pour la lubrification des véhicules et engins ouvrant droit à déduction de la taxe (camions, camionnettes, véhicules ou engins affectés de façon exclusive à l'enseignement de la conduite, engins de travaux publics, ainsi que pompes, moteurs fixes, compresseurs,etc. ), y compris lorsqu'ils sont pris en location ( CGI, ann. II, art. 206-IV-2- 6° ).
 Permalien du document : 
 Document précédent
```

### VAT-Q017

Current BOI-TVA-DED-30-30-10 paragraph1–50; https://bofip.impots.gouv.fr/bofip/1190-PGP.html/identifiant=BOI-TVA-DED-30-30-10-20130304; actual original read 2026-10-29. Native LF [57, 79]; reader SHA256 `665a1c14f371b6a98948c97a9688b42259cb8c074020b0c8c4097b7b246ec5df`. Inherited actual C selected reading, exact read-scope records preserved

```text
1
En application des dispositions du 2° du 2 du IV de l’【11†article 206 de l’annexe II au code général des impôts (CGI)†www.legifrance.gouv.fr】, un assujetti ne peut pas déduire la taxe ayant grevé les dépenses de bien ou de service supportées pour permettre d’assurer le logement à titre gratuit des dirigeants ou du personnel de l’entreprise. (Cette disposition n'est pas applicable aux dépenses supportées par un assujetti relatives à la fourniture à titre onéreux par cet assujetti de logements).
Remarque : Sont à ce titre exclus du droit à déduction les dépenses d'acquisition ou de location d'immeubles ou fraction d'immeubles affectés au logement à titre gratuit des dirigeants ou du personnel de l'entreprise.
Lorsque les dépenses de logement ou d'hébergement sont supportées concurremment au bénéfice de tiers -ouvrant droit à déduction- et au bénéfice de dirigeants et/ou de salariés -qui n'ouvrent pas droit à déduction- il est admis que le coefficient d'admission soit déterminé en proportion  du nombre de tiers par rapport  à l'ensemble des personnes ayant bénéficié des dépenses de cette nature portées sur la facture.
Afin de justifier que la taxe dont la déduction est opérée se rapporte effectivement à des dépenses de logement engagées au bénéfice de tiers, les entreprises devront porter sur les factures délivrées par les fournisseurs l'identité et la qualité des bénéficiaires.
10

Cette mesure d’exclusion n’est pas applicable aux dépenses relatives à la fourniture à titre gratuit du logement sur les chantiers ou dans les locaux d’une entreprise de personnel de sécurité, de gardiennage et de surveillance.

20

Cette disposition concerne les loges ou appartements de concierge ou de gardien compris dans les immeubles ou ensembles immobiliers à usage d'atelier ou de bureaux, etc.

30
La dérogation est limitée aux logements dont l'utilisation sur les lieux de travail est rendue nécessaire pour les fonctions de sécurité ou de surveillance incombant au bénéficiaire, même si ces fonctions ne sont pas exclusives et si les intéressés sont affectés à d'autres tâches au sein de l'entreprise.

40
L'expression « personnel salarié chargé de la sécurité ou de la surveillance » doit être interprétée strictement. En particulier, la déduction ne peut être accordée pour l'ensemble des dépenses des logements dits de fonction des personnels et de leur famille appartenant aux cadres, à la maîtrise ou aux autres catégories de personnel salarié de l'entreprise, même si le logement sur place de ce personnel répond aux nécessités d'une bonne marche de l'entreprise.

(41)

50
Lorsque l'option prévue au 2° de l'【12†article 260 du CGI†www.legifrance.gouv.fr】 a été valablement exercée par le bailleur et qu'elle couvre les locaux nus à usage professionnel et les logements de fonction, le preneur peut exercer la déduction de la taxe grevant les dépenses de logement dès lors que le personnel auxquels les locaux sont affectés est chargé de fonctions impliquant par nature et au regard et au regard de l'activité exercée une résidence permanente sur les lieux mêmes de son travail (RES N° 2010/73 au 【13†BOI-TVA-CHAMP-50-10 au II-D § 200】).
```

### VAT-Q018

CGIannexeII205–207; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069569/LEGISCTA000006179225/2026-10-29; actual original read 2026-10-29. Native LF [47, 84]; reader SHA256 `dd01aefa6fbc017e8487739d31f7b04486866c8769679f72d9225996a14594f1`. Inherited actual C selected reading, exact read-scope records preserved

```text
La taxe sur la valeur ajoutée grevant un bien ou un service qu'un assujetti à cette taxe acquiert, importe ou se livre à lui-même est déductible à proportion de son coefficient de déduction.

Voir les versions
Comparer les versions
Textes liés
Article 206

EN VIGUEUR DEPUIS LE 08 JUILLET 2024

Modifié par Décret n°2024-711 du 5 juillet 2024 - art. 1


I. – Le coefficient de déduction mentionné à l'article 205 est égal au produit des coefficients d'assujettissement, de taxation et d'admission.

II. – Le coefficient d'assujettissement d'un bien ou d'un service est égal à sa proportion d'utilisation pour la réalisation d'opérations imposables. Les opérations imposables s'entendent des opérations situées dans le champ d'application de la taxe sur la valeur ajoutée en vertu des articles 256 et suivants du code général des impôts, qu'elles soient imposées ou légalement exonérées.

III. – 1. Le coefficient de taxation d'un bien ou d'un service est égal à l'unité lorsque les opérations imposables auxquelles il est utilisé ouvrent droit à déduction.

2. Le coefficient de taxation d'un bien ou d'un service est nul lorsque les opérations auxquelles il est utilisé n'ouvrent pas droit à déduction.

3. Lorsque le bien ou le service est utilisé concurremment pour la réalisation d'opérations imposables ouvrant droit à déduction et d'opérations imposables n'ouvrant pas droit à déduction, le coefficient de taxation est calculé selon les modalités suivantes :

1° Ce coefficient est égal au rapport entre :

a. Au numérateur, le montant total annuel du chiffre d'affaires afférent aux opérations ouvrant droit à déduction, y compris les subventions directement liées au prix de ces opérations ;

b. Et, au dénominateur, le montant total annuel du chiffre d'affaires afférent aux opérations imposables, y compris les subventions directement liées au prix de ces opérations.

Les sommes mentionnées aux deux termes de ce rapport s'entendent tous frais et taxes compris, à l'exclusion de la taxe sur la valeur ajoutée ;

2° Lorsqu'un assujetti a constitué des secteurs distincts d'activité en application de l'article 209, le chiffre d'affaires à retenir pour le calcul du rapport défini au 1° est celui du ou des secteurs pour lesquels le bien ou le service est utilisé ou, lorsqu'un assujetti unique mentionné à l'article 256 C du code général des impôts le décide et que le bien ou service est utilisé par plusieurs de ses membres, celui de l'ensemble du chiffre d'affaires afférent aux opérations imposables de cet assujetti unique ;

3° Pour l'application des dispositions du 1°, il est fait abstraction du montant du chiffre d'affaires afférent :

a. Aux cessions des biens d'investissements corporels ou incorporels ;

b. Au produit des opérations immobilières et financières accessoires exonérées de la taxe sur la valeur ajoutée. Sont considérées comme accessoires les opérations qui présentent un lien avec l'activité principale de l'entreprise et dont la réalisation nécessite une utilisation limitée au maximum à 10 % des biens et des services grevés de taxe sur la valeur ajoutée qu'elle a acquis. Ce pourcentage est apprécié en fonction de la proportion d'utilisation pour ces opérations de chaque bien et service grevé de taxe sur la valeur ajoutée. Cette proportion est appliquée à la valeur d'acquisition par le redevable de chacun de ces biens et services pour déterminer leur valeur d'utilisation. Le pourcentage résulte du rapport entre, au numérateur, la somme des valeurs d'utilisation ainsi déterminées et, au dénominateur, le montant total de la valeur d'acquisition de ces biens et services.

```

### VAT-Q019

BOI-TVA-DED-30-30-20 vehicle exclusions/exceptions; https://bofip.impots.gouv.fr/bofip/1192-PGP.html; actual original read 2026-10-29. Native LF [185, 222]; reader SHA256 `735a0a2286708f6bcb6468c6a31847d1acd513c83f9b303e114a84b01dd4d58d`. Inherited actual C selected reading, exact read-scope records preserved

```text
 Les ventes de véhicules de démonstration sont soumises au régime des ventes de biens d’occasion par des assujettis-revendeurs ( II-B-1 § 170 du BOI-TVA-SECT-90-30 ).
 Ainsi, pour les voitures de tourisme de démonstration (voitures automobiles conçues pour le transport de personnes ou à usages mixtes et comportant, outre le siège du conducteur, huit places assises au maximum) les revendeurs peuvent choisir au moment de la vente entre deux possibilités ( II-D-2-a § 230 ) :
 acquitter la taxe sur la différence entre le prix de vente et le prix d’achat ( CGI, art. 297 A ). La taxe facturée par le fournisseur au moment de l’achat du véhicule est alors définitivement exclue du droit à déduction ;
 acquitter la taxe sur le prix de vente total ( CGI, art. 297 C ).
 250
 Dans le cas où le reversement a été effectué dès l’affectation du véhicule ( II-D-2-a § 220 ), le vendeur peut déduire au moment de la vente, la totalité de la TVA qu’il a supportée à raison de l’achat du véhicule.
 E. Véhicules ou engins utilisés par les entreprises ou établissements d’enseignement de la conduite
 260
 En application des dispositions de l’ article 273 septies A du CGI , un assujetti est autorisé à déduire la TVA ayant grevé les dépenses d’achat, d’importations, d’acquisitions intracommunautaires, de livraisons et de services afférentes aux véhicules ou engins qui sont affectés de façon exclusive à l’enseignement de la conduite.
 1. Principes
 a. Activité et redevables concernés
 270
 L’activité d’enseignement de la conduite a pour objet d’assurer la formation, sur un plan théorique et pratique, des personnes qui souhaitent apprendre la conduite des véhicules aptes à emprunter les voies de circulations terrestres, aériennes, maritimes et fluviales.
 Cette activité nécessite dans la plupart des cas la présence d’un moniteur chargé de fournir les éléments d’information utiles à la conduite du véhicule. D’une manière générale, l’aptitude de l’élève est sanctionnée, à la suite d’un examen, par la délivrance d’un permis ou d’un brevet reconnu par l’autorité publique.
 L’enseignement de la conduite peut constituer l’activité unique de l’entreprise ou peut être exercé concomitamment avec d’autres activités. Le cas échéant, ces établissements dispensent leur formation dans le cadre des textes législatifs ou réglementaires qui régissent la profession.
 Ainsi, à titre d’exemple dans le domaine terrestre, la formation est dispensée dans un établissement d’enseignement de la conduite des véhicules à moteur et de la sécurité routière agréé.
 b. Dépenses ouvrant droit à déduction
 280
 Il s’agit des dépenses qui se rapportent aux véhicules utilisés pour l’enseignement de la conduite tels que les véhicules routiers automobiles, les motocyclettes, les avions, les hélicoptères, les bateaux, etc.
 290
 À ce titre, sont concernés les achats, les importations, les livraisons et les acquisitions intracommunautaires portant sur des véhicules ou engins destinés à l’enseignement de la conduite.
 Il en va de même de ces dépenses lorsqu’elles concernent les éléments constitutifs, les pièces détachées et accessoires de ces véhicules.
 300
 Outre les prestations de services liées à l’entretien et à la réparation des véhicules, sont également concernées les opérations de crédit-bail et de location de courte ou longue durée concernant ces véhicules.
 310
 Les titulaires de revenus non commerciaux sont autorisés en matière d’impôts directs à déterminer leurs dépenses d’automobiles par application du barème forfaitaire publié chaque année par l’administration pour les salariés.
 Cette option n’est valable qu’en l’absence de comptabilisation des dépenses couvertes par le barème, notamment celles de carburant.
 Les redevables qui, sous réserve des exclusions en vigueur, souhaitent exercer le droit à déduction au titre de la TVA sur leurs dépenses afférentes à leurs véhicules de tourisme, doivent renoncer à utiliser le barème forfaitaire en matière d’impôts directs.
 En effet, l’utilisation de ce barème déterminé sur des bases TTC introduirait un double emploi s’il était utilisé concurremment avec l’exercice du droit à déduction de la TVA afférente aux dépenses concernées.
 2. Exercice du droit à déduction
 320
 En application des principes généraux du droit à déduction de la TVA, seuls les entreprises ou établissements qui sont redevables de la taxe au titre de leur activité d’enseignement de la conduite pourront effectuer la déduction de TVA ayant grevé les dépenses portant sur les véhicules qu’ils utilisent pour les besoins de cette activité.
 Ainsi, aucune déduction de la taxe afférente aux véhicules utilisés par des associations sportives ou de loisirs exonérées du paiement de la TVA (exemple : aéro-club, etc.) ou par des assujettis bénéficiant de la franchise en base ne peut être opérée.
 Pour ouvrir droit à déduction, le véhicule doit en principe être affecté de façon exclusive à l’enseignement de la conduite.
 Toutefois, il est admis que la condition d’affectation exclusive ne soit pas remise en cause lorsque le véhicule est affecté, en dehors de l’activité d’enseignement, à l’une ou à plusieurs des activités autorisant le droit à déduction sur les véhicules ou engins de transport de personnes ou à usages mixtes telles que :
 le transport public de voyageur ;
 la location de véhicules lorsque ces opérations de location sont soumises à la TVA.
 Ainsi, ouvre droit à déduction un véhicule utilisé simultanément pour :
```

### VAT-Q020

BOI-TVA-DED-30-30-20 vehicle exclusions/exceptions; https://bofip.impots.gouv.fr/bofip/1192-PGP.html; actual original read 2026-10-29. Native LF [223, 286]; reader SHA256 `735a0a2286708f6bcb6468c6a31847d1acd513c83f9b303e114a84b01dd4d58d`. Inherited actual C selected reading, exact read-scope records preserved

```text
 le transport public de voyageurs et l’enseignement de la conduite ;
 la location et l’enseignement de la conduite.
 En revanche, un tel véhicule utilisé simultanément, par exemple, pour le transport de marchandises et l’enseignement de la conduite reste exclu du droit à déduction.
 Il est précisé qu’en contrepartie de la déduction de TVA qui a pu, le cas échéant, être effectuée dans les conditions de droit commun lors de l’acquisition du véhicule, une PSASM doit être soumise à la TVA, conformément aux dispositions du 1° du 2 du II de l’ article 257 du CGI ( III § 180 et suivants du BOI-TVA-CHAMP-10-20-20 ), dans l’hypothèse où le véhicule ferait l’objet d’une utilisation privative (besoins privés du dirigeant, du personnel ou de tiers).
 F. Véhicules ou engins de type « tout terrain » affectés exclusivement à l’exploitation des remontées mécaniques et des domaines skiables
 330
 En application des dispositions du 1° de l’ article 273 septies C du CGI , un assujetti est autorisé à déduire la TVA afférente aux livraisons, aux importations, aux acquisitions intracommunautaires et aux prestations de services en ce qui concerne les véhicules tout terrain affectés exclusivement à l’exploitation des remontées mécaniques et des domaines skiables, dans les conditions fixées à l’ article 84 A de l’annexe III au CGI .
 Ainsi, il est prévu que l’assujetti certifie sur l’honneur que :
 le certificat d’immatriculation du véhicule, ou le cas échéant, le contrat de location du véhicule, est établi au nom d’un exploitant de remontées mécaniques ou de domaines skiables ;
 le véhicule comprend, d’origine ou à la suite de travaux, trois au moins des équipements techniques suivants : plateau de chargement, arceau de sécurité pour habitacle, portique de levage, crochet d’attelage, treuil frontal, bac de benne, blocage du différentiel, boîte de transfert, arceau porte-échelle arrière de cabine, plusieurs points d’arrimage sur les côtés des ridelles, pneus mixtes.
 Remarque : En pratique, sont essentiellement concernés les véhicules de la catégorie N1 de carrosserie européenne « camion pick-up ».
 G. Avions et hélicoptères
 1. Principes
 380
 Il est admis que les dépenses supportées pour l’acquisition d’avions ou d’hélicoptères par des assujettis qui les utilisent pour fournir à titre onéreux des prestations de services aériens soumis à la TVA ouvrent droit à déduction dans les conditions de droit commun prévues par l’ article 271 du CGI .
 390
 Les prestations de services aériens concernées peuvent être notamment le transport public de voyageurs, le transport de fret, l’enseignement du pilotage, la manutention de matériel, l’hélitreuillage et le levage, la publicité, la prise de vues, les vols panoramiques, les vols de démonstration, le largage de parachutistes, les opérations aériennes agricoles, etc.
 400
 La circonstance que l’avion ou l’hélicoptère soit utilisé de façon alternative pour la réalisation de plusieurs des prestations visées au II-G-1 § 390 est sans incidence pour l’exercice du droit à déduction.
 410
 Les dépenses de location, d’entretien, de réparation concernant des avions ou hélicoptères utilisés dans les conditions précisées au II-G-1 § 380 à 400 ouvrent également droit à déduction dans les conditions de droit commun.
 420
 Les carburants et autres produits pétroliers consommés pour le fonctionnement de ces mêmes engins ouvrent également droit à déduction à l’exception des essences visées au a du 1° du 4 de l’ article 298 du CGI .
 2. Modalités d’application
 430
 La TVA qui a grevé les dépenses visées au II-G-1 § 380 à 420 ne peut être déduite qu’à la condition que ces dépenses soient supportées pour les besoins d’opérations ouvrant droit à déduction et que la taxe correspondante figure distinctement sur une facture d’achat ( CGI, art. 271, II-1 ).
 440
 Les dépenses concernées doivent être supportées dans l’intérêt de l’entreprise.
 450
 Par ailleurs, les entreprises concernées doivent être en mesure de justifier strictement de l’utilisation effective qui est faite de ces aéronefs. Le respect de cette condition suppose que soient respectées les obligations résultant de la réglementation qui régit l’aéronautique civile.
 460
 À cet égard, il est rappelé que les entreprises qui effectuent, même partiellement, des opérations de transport aérien de voyageurs doivent :
 obtenir un certificat de transport aérien délivré par le Conseil supérieur de l’aviation marchande ou l’autorité d’aviation civile et faire approuver un manuel d’exploitation qui reprend l’ensemble de l’organigramme et des structures de l’entreprise ainsi que les procédures en vigueur et les performances des appareils exploités ;
 obtenir l’approbation par les services de la direction générale de l’aviation civile d’une liste de flotte inscrite dans le cadre de ce certificat de transport aérien et comprenant tous les appareils qui sont autorisés à effectuer du transport public de voyageurs ;
 se livrer à des contrôles périodiques de la navigabilité des aéronefs et des compétences des pilotes ;
 et tenir un suivi précis des heures de vol de l’appareil sur les documents définis par la réglementation en vigueur, à savoir : soit un compte rendu matériel (CRM) pour ceux des aéronefs qui sont inscrits en liste de flotte attachée à un certificat de transport aérien ;
 soit un carnet de route pour ceux des aéronefs non inscrits en liste de flotte. Ce dernier document (carnet de route) n’est pas obligatoire en transport aérien sur la base de la réglementation « OPS 3 ».
 C’est plus particulièrement la tenue de ces derniers documents qui conditionne l’application de la mesure de tempérament ( II-G-1 § 380 à 420 ) visant à ne pas appliquer l’exclusion prévue par les dispositions du 6° du 2 du IV de l’ article 206 de l’annexe II au CGI et les autres exclusions qui en sont corrélatives.
 L’utilisation effective de l’appareil est en effet justifiée par la présentation de ces documents et notamment par les informations résultant des mentions obligatoires (à savoir, la date, le nom des membres de l’équipage et leur fonction à bord, l’origine et la destination du vol, l’heure de départ et l’heure d’arrivée, le temps du vol, la nature du vol, le carburant embarqué lors de l’avitaillement, les anomalies constatées pendant le vol ou la mention explicite d’absence d’anomalie) figurant soit sur le carnet de route de l’avion ou de l’hélicoptère, soit sur le CRM.
 Remarque : Il est précisé que les entreprises qui ne réalisent que des travaux aériens sont soumises aux mêmes obligations hormis l’absence de certificat de transport aérien. Dans ce cas, le CRM n’est pas obligatoire.
 Pour les entreprises qui ne réaliseraient aucune prestation de transport aérien de voyageurs, cette justification est satisfaite par la tenue du carnet de route.
 3. Précisions
 470
 Lorsqu’une entreprise est autorisée à déduire, en application de la mesure de tempérament exposée au II-G-1 § 380 à 420 , la taxe grevant les dépenses afférentes à l’acquisition et l’entretien d’avions ou d’hélicoptères, l’utilisation de ces engins pour la réalisation d’opérations autres que des prestations aériennes rendues à titre onéreux donne lieu à la taxation d’une PSASM.
 Tel est le cas dans les situations suivantes :
 utilisation privative de l’appareil ou à des fins étrangères à l’entreprise. Lorsque l’appareil et les biens et services y afférents, qui a ouvert droit à déduction dans les conditions exposées au II-G § 380 à 460 , est utilisé pour les besoins privés de l’assujetti ou de son personnel, ou plus généralement à des fins étrangères à son entreprise, cette utilisation est assimilée à une prestation de services effectuée à titre onéreux ( CGI, art. 257, II ) ;
 utilisation de l’appareil pour le transport du personnel dans le cadre de la réalisation des activités de l’entreprise.
 480
 Cette mesure se justifie en raison de l’exclusion du droit à déduction applicable aux transports de personnes et les opérations accessoires auxdits transports ( CGI, ann. II, art. 206, IV-2-5° ).
 490
 La taxation d’une PSASM n’est toutefois pas exigée lorsque le transport du personnel est nécessaire à la réalisation matérielle des prestations de services aériens, ainsi que dans le cas de vols techniques consécutifs à des mises au point, réparations, ajustements ou révisions d’appareils, et de vols de mise en place à destination d’un site en vue de la réalisation d’une prestation.
 500
 La base d’imposition des PSASM visées au II-G-3 § 470 à 490 est constituée par les dépenses engagées pour leur exécution ( CGI, art. 266, 1-c ).
 510
 En outre, la taxe afférente à ces PSASM n’ouvre pas droit à déduction ( CGI, art. 271 et CGI, ann. II, art. 206, IV-2-5°).
 H. Véhicules dédiés au transport des équidés
 520
 En application des dispositions du 2° de l’ article 273 septies C du CGI , un assujetti est autorisé à déduire la TVA ayant grevé les livraisons, les importations, les acquisitions intracommunautaires et les prestations de services afférentes aux véhicules aménagés pour le transport des équidés dans les conditions de droit commun.
 Ces dispositions s’appliquent à compter du 1 er janvier 2024.
 Est ainsi déductible la taxe ayant grevé les véhicules dont les caractéristiques techniques les destinent à un usage mixte de transport d’équidés et de personnes.
 Exemple : Un véhicule aménagé pour transporter des équidés est également équipé d’une cabine-logement pour les besoins du chauffeur et des soigneurs (concept de « home car »). Ce type de véhicule permet de répondre aux obligations règlementaires induites par le transport d’équidés qui s’imposent aux professionnels de la filière équine ainsi qu’aux exigences du droit du travail. Bien qu’il soit conçu pour un usage mixte, le dispositif d’exclusion du droit à déduction ne s’applique plus à ce véhicule depuis le 1 er janvier 2024.
 Permalien du document : 
 Document précédent
 Document suivant
```

### VAT-Q021

CGI271II1a; currentBOI-TVA-DED-40-10-10 §§55–60; https://bofip.impots.gouv.fr/bofip/1111-PGP.html/identifiant=BOI-TVA-DED-40-10-10-20250108; actual original read 2026-10-29. Native LF [91, 114]; reader SHA256 `7d08d47109838f67dcb79b0a2d9ec1a114ecdfab9bd121ffb5139983c092ca93`. Inherited actual C selected reading, exact read-scope records preserved

```text
La facture constitue, pour l’exercice du droit à déduction, un document fondamental puisqu’il permet de justifier formellement de l’existence d’une créance de TVA sur le Trésor.
La taxe grevant les dépenses supportées par un assujetti ne peut être déduite qu’à la triple condition que :
  * ces dépenses soient exposées pour les besoins d’opérations ouvrant droit à déduction ;
  * le montant de la TVA correspondante figure distinctement sur une facture établie conformément aux dispositions de l’article 289 du CGI, de l’【21†article 242 nonies de l’annexe II au CGI†www.legifrance.gouv.fr】 et de l’article 242 nonies A de l’annexe II au CGI ;
  * la taxe ait pu légalement figurer sur ladite facture (CGI, art. 271, II-1).
Si l’une de ces conditions d’exercice du droit à déduction de la TVA n’est pas satisfaite, la déduction de la taxe est susceptible d’être remise en cause. Tel est notamment le cas lorsque l’importance ou la nature des manquements, inexactitudes ou omissions constatés ne permettent pas de considérer le document présenté comme une facture.
Cependant, il est précisé que la seule omission ou inexactitude de l’une des mentions obligatoires n’entraîne pas nécessairement la remise en cause de la validité d’une facture pour l’exercice des droits à déduction de la taxe dès lors que l’opération est justifiée dans sa réalité et qu’elle satisfait par ailleurs aux autres conditions posées pour l’exercice du droit à déduction. La facture doit en tout état de cause permettre de justifier la naissance et l’exercice du droit à déduction par le client.
Si la mention de certaines informations peut constituer une des conditions posées pour l’application d’un régime de TVA spécifique (livraisons intracommunautaires, franchise en base, etc.), une simple omission ou inexactitude en matière de mentions obligatoires n’a pas pour effet, dans la généralité des cas, d’entraîner une remise en cause du régime appliqué.
Dans tous les cas, l’administration s’attache à prendre en compte les circonstances dans lesquelles ces omissions et inexactitudes sont intervenues.

Par ailleurs, il est rappelé que les omissions ou inexactitudes dans les mentions que doivent comporter les factures sont sanctionnées (【22†II § 110 à 150 du BOI-CF-INF-10-40-40】).
## B. Facturation régulière de la TVA

60

L’existence de la facture mentionnant la TVA ne crée pas en soi le droit à déduction. Ce droit n’existe que dans la mesure où la taxe figurant sur la facture était légalement due par l’émetteur de ce document. Ce principe a d’ailleurs été confirmé par la Cour de justice des Communautés européennes (【23†CJCE, arrêt du 13 décembre 1989, aff. C-342/87, « Genius Holding BV c/ Staatssecretaris van Financiën », ECLI:EU:C:1989:635†eur-lex.europa.eu】).
La taxe illégalement facturée est due par celui qui l’a facturée, soit en application du 3 de l’【24†article 283 du CGI†www.legifrance.gouv.fr】 (taxe facturée à tort au titre d’une opération non imposable ou à un taux supérieur au taux légal), soit en application du 4 de l’article 283 du CGI (taxe facturée au titre d’une opération fictive).
Toutefois, elle n’est pas pour autant déductible par le destinataire, en application soit du a du 1 du II de l’【15†article 271 du CGI†www.legifrance.gouv.fr】 qui interdit la déduction de la taxe que le fournisseur n’était pas légalement autorisé à faire figurer sur la facture (cas visé au 3 de l’article 283 du CGI), soit du 2 de l’【25†article 272 du CGI†www.legifrance.gouv.fr】 (exclusion du droit à déduction de la taxe due en application des dispositions du 4 de l’article 283 du CGI).
Cependant, lorsque la taxe a été facturée par erreur au titre d’une opération exonérée ou à un taux supérieur à celui dont était passible l’opération, elle peut faire l’objet d’une régularisation dans les conditions décrites au 【26†IV-A § 370 et suivants du BOI-TVA-DECLA-30-20-20-30】.
Pour obtenir la restitution de la TVA qui lui a été facturée à tort, l’acquéreur doit prioritairement s’adresser, y compris le cas échéant par la voie juridictionnelle, à son fournisseur si celui-ci n’a pas pris l’initiative de lui rembourser l’indu correspondant, et, seulement à titre subsidiaire, à l’administration fiscale si l’obtention de la restitution de la taxe indue auprès du fournisseur est impossible ou excessivement difficile (【27†CE, décision du 29 novembre 2023, n° 469111, ECLI:FR:CECHR:2023:469111.20231129†www.legifrance.gouv.fr】).
À titre d’illustration, cette condition d’impossibilité ou d’excessive difficulté est établie dans les situations d’insolvabilité du fait de l’ouverture d’une procédure de faillite (【28†CJUE, arrêt du 11 avril 2019, aff. C-691/17, « PORR Épitesi Kft. c/ Nemzeti Adó- és Vámhivatal Fellebbviteli Igazgatósága », ECLI:EU:C:2019:327†eur-lex.europa.eu】), dans les cas de liquidation judiciaire (【29†CJUE, arrêt du 13 octobre 2022, aff. C-397/21, « HUMDA Magyar Autó-Motorsport Fejlesztési Ügynökség Zrt.
c/ Nemzeti Adó- és Vámhivatal Fellebbviteli Igazgatósága », ECLI:EU:C:2022:790†eur-lex.europa.eu】) ou en cas de prescription de toute action civile (【30†CJUE, arrêt du 7 septembre 2023, aff. C-453/22, « Michael Schütte c/ Finanzamt Brilon », ECLI:EU:C:2023:639†eur-lex.europa.eu】).
Remarque : En ce qui concerne les règles applicables aux assujettis étrangers non établis en France qui y ont supporté de la TVA facturée de façon erronée, il convient de se reporter au 【31†I-B-2 § 20 à 40 du BOI-TVA-DED-50-20-30-20】 s’agissant des assujettis établis dans un autre État membre de l’Union européenne et au 【32†IV-C § 400 à 420 du BOI-TVA-DED-50-20-30-40】 s’agissant des assujettis établis en dehors de l’Union européenne.
Enfin, il doit être fait une application stricte des dispositions du 4 de l’article 283 du CGI et du 2 de l’article 272 du CGI (taxe facturée au titre d’opérations fictives) dont l’objet est de prévenir et de réprimer des manœuvres frauduleuses portant sur la facturation de la TVA. Ces dispositions s’appliquent donc en tout état de cause.
```

### VAT-Q022

CGI2832/2830; currentBOI-TVA-DECLA-30-20-20-30 §§80–105; https://bofip.impots.gouv.fr/bofip/1531-PGP.html/identifiant=BOI-TVA-DECLA-30-20-20-30-20250108; actual original read 2026-10-29. Native LF [104, 119]; reader SHA256 `64ac045982f2bad27e2874769f7c886e33b014409e5eac2ed0b5bfac3db4fa24`. Inherited actual C selected reading, exact read-scope records preserved

```text
## C. Prestations de services pour lesquelles la taxe est due par le preneur

80
Les prestations de services qui se situent en France en application du 1° de l’【24†article 259 du CGI†www.legifrance.gouv.fr】 et de l’【25†article 259 A du CGI†www.legifrance.gouv.fr】 donnent lieu à autoliquidation (【26†CGI, art. 283, 2†www.legifrance.gouv.fr】 et CGI, art. 283, 1-al.
2), lorsqu’elles sont réalisées par un prestataire qui n’est pas établi en France ou n’y dispose que d’un établissement qui ne participe pas à l’opération conformément à l’【27†article 283-0 du CGI†www.legifrance.gouv.fr】 (【28†II § 10 et suivants du BOI-TVA-DECLA-10-10-20】).
90

La réalisation de ces prestations entraîne l’obligation de faire figurer sur les factures le numéro d’identification à la TVA du prestataire ainsi que celui fourni par le preneur (【19†CGI, ann. II, art. 242 nonies A, I-4°†www.legifrance.gouv.fr】).
Remarque 1 : En pratique, cette obligation s’impose surtout aux prestataires établis en dehors de l’Union européenne dès lors que, dans une situation similaire, les opérateurs qui fournissent des services depuis un autre État membre ont vocation à faire application, non pas des règles de facturation prévues par le code général des impôts, mais de celles prévues par la législation de cet État qui doit comprendre l’obligation de mentionner ce numéro dès lors que la directive ne prévoit aucun assouplissement à cet égard.
Remarque 2 : Dans l’hypothèse où la prestation est réalisée au bénéfice du membre d’un assujetti unique constitué sur le fondement de l’【22†article 256 C du CGI†www.legifrance.gouv.fr】, le numéro d’identification à la TVA du preneur devant être mentionné en application du 4° du I de l’article 242 nonies A de l’annexe II au CGI est celui de ce membre.

100
L’apposition de cette mention s’impose par ailleurs à l’assujetti qui réalise, depuis la France, une prestation de services réputée se situer sur le territoire d’un autre État membre au regard des règles de territorialité prévues par la 【29†directive 2006/112/CE du Conseil du 28 novembre 2006†eur-lex.europa.eu】, modifiée par la 【30†directive 2008/8/CE du Conseil du 12 février 2008 modifiant la directive 2006/112/CE en ce qui concerne le lieu des prestations de services†eur-lex.europa.eu】, et pour laquelle le preneur est redevable de la taxe.
105

Il est par ailleurs rappelé qu’en application des dispositions figurant au c du II de l’article 242 nonies A de l’annexe II au CGI (【31†II § 60 du BOI-TVA-DECLA-30-20-20-20】), la facture relative aux prestations pour lesquelles le preneur est redevable de la taxe peut ne pas faire mention de la TVA exigible. Elle doit cependant, afin de justifier que la taxe n’est pas collectée par le prestataire, comporter la mention « Autoliquidation » (CGI, ann. II, art. 242 nonies A, I-13°).
```

### VAT-Q023

CGI2661bis/289IV; current generic BOI-TVA-DECLA-30-20-20-10 §§380–410; https://bofip.impots.gouv.fr/bofip/140-PGP.html/identifiant=BOI-TVA-DECLA-30-20-20-10-20131018; actual original read 2026-10-29. Native LF [254, 279]; reader SHA256 `72b011783b24d01a4e975800dbb68f77a5b5d381922044935c04cd7e6a6dd04d`. Inherited actual C selected reading, exact read-scope records preserved

```text
370

Ces taxes étrangères ne peuvent donner lieu à déduction par les assujettis établis en France.
#### b. Facturation dans une monnaie autre que l'euro

380

En application des dispositions prévues au premier alinéa du IV de l'【22†article 289 du CGI†www.legifrance.gouv.fr】, les montants figurant sur la facture peuvent être exprimés dans toute monnaie, pour autant que le montant de la taxe à payer ou à régulariser soit déterminé en euros, en utilisant le mécanisme de conversion prévu au 1 bis de l'【27†article 266 du CGI†www.legifrance.gouv.fr】.

390
Lorsque les éléments servant à déterminer la base d'imposition à la TVA sont exprimés dans une monnaie autre que l’euro, le taux de change à appliquer est celui du dernier taux publié par la Banque centrale européenne, au jour de l'exigibilité de la taxe.

400

Pour éviter des litiges et assurer une bonne information de leurs clients, les entreprises qui établissent des factures en devises étrangères peuvent :
- lorsque l'exigibilité intervient lors de la délivrance ou du débit, indiquer sur les factures le taux de change applicable ;

- lorsque l'exigibilité intervient lors de l'encaissement, préciser que le montant de la TVA sera fonction du taux de change fixé lors de l'encaissement des acomptes ou du prix de l'opération.

410
De plus, les assujettis conservent la possibilité d’utiliser, pour déterminer la valeur fiscale de leurs acquisitions intracommunautaires, le taux de change déterminé pour calculer la valeur en douane des importations.

Remarque : Les taux de change retenus pour le calcul de la valeur en douane sont disponibles sur le site « 【29†https://pro.douane.gouv.fr/prodouane.asp†pro.douane.gouv.fr】».
A cet égard, il est rappelé que les articles 168 et suivants des 【30†Dispositions d'application du code des douanes communautaire†ec.europa.eu】 prévoient un système de taux de change périodique mensuel qui pourra être déterminé en application des instructions de la Direction générale des douanes et droits indirects (DGDDI).

L’assujetti qui choisit d’utiliser cette méthode de conversion devra le faire pour toutes les opérations intracommunautaires de l’année en cause.
```

### VAT-Q024

CGI259D/258A; current generic BOI-TVA-CHAMP-20-50-40-20 §220/240–270; https://bofip.impots.gouv.fr/bofip/11964-PGP.html/identifiant=BOI-TVA-CHAMP-20-50-40-20-20211222; actual original read 2026-10-29. Native LF [222, 256]; reader SHA256 `9a09a1a72252414a67f632092c864b85b2e83fc426df936a26881d862986dab4`. Inherited actual C selected reading, exact read-scope records preserved

```text
## B. Régime des petits opérateurs

220
Par exception au principe énoncé ci-dessus (II-A § 210), les prestations de télécommunications, les services de radiodiffusion et de télévision ainsi que les services fournis par voie électronique effectués par un prestataire établi en France auprès de personnes non assujetties sont imposées en France lorsque la valeur totale de ces prestations réalisées en faveur de personnes non assujetties cumulée à la valeur de ses ventes à distance intracommunautaires de biens (VAD-IC) qu’il réalise (concernant la définition des ventes à distance intracommunautaires de biens, se reporter au 【30†I § 20 à 60 du BOI-TVA-CHAMP-10-10-40-60】), est inférieure au seuil de 10 000 € hors TVA (【12†CGI, art.
259 D, I-2†www.legifrance.gouv.fr】).
Symétriquement, les prestations réalisées par un prestataire établi dans un autre État membre sont imposées dans cet autre État membre lorsque cette même condition est remplie (【18†directive 2006/112/CE du Conseil du 28 novembre 2006†eur-lex.europa.eu】, dans sa rédaction issue de la 【31†directive (UE) 2017/2455 du Conseil du 5 décembre 2017 modifiant la directive 2006/112/CE et la directive 2009/132/CE en ce qui concerne certaines obligations en matière de taxe sur la valeur ajoutée applicables aux prestations de services et aux ventes à distance de biens†eur-lex.europa.eu】, art.
59 quater).
Les conditions d’application du seuil appellent les précisions suivantes.

Eligibilité au seuil : L e bénéfice du seuil n’est ouvert qu’aux assujettis établis dans un seul État membre de l’Union européenne. Par conséquent, sont exclus du bénéfice du seuil les assujettis non établis dans l’Union ainsi que les assujettis établis dans plusieurs États membres de l’Union.
Appréciation du seuil : Le montant ne doit pas avoir été dépassé, ni au cours de l’année civile en cours, ni au cours de l’année civile précédente. Lorsque le montant d'une prestation a pour conséquence le franchissement de ce seuil, le lieu de cette prestation est situé dans l’État membre où réside la personne non assujettie. Il en est de même pour les prestations ultérieures, quel qu’en soit le montant.
Calcul du seuil : Le seuil de 10 000 € est déterminé en prenant en compte l'ensemble du chiffre d'affaires afférent à de telles prestations réalisées en faveur de personnes non assujetties dans les autres États membres de l'Union européenne, exception faite de celui réalisé dans le pays d'établissement du prestataire, auquel il convient d’ajouter l’ensemble du chiffre d’affaires des VAD-IC réalisées par ce même prestataire sur l'ensemble du territoire de l'Union.
Pour les opérations dont le fait générateur de la taxe intervient entre le 1^{er} juillet 2021 et le 31 décembre 2021, le chiffre d'affaires à en prendre en compte pour l'appréciation du seuil de 10 000 € hors TVA est :
- au titre de l'année précédente, le chiffre d'affaires réalisé durant l'année 2020 ; et
- au titre de l'année en cours, le chiffre d'affaires réalisé depuis le 1^{er} janvier 2021, non proratisé.

(230)

240
L'assujetti mentionné au II-B § 220 peut opter, auprès de l’administration fiscale française, pour que ces prestations soient imposables dans l’État membre où réside la personne non assujettie dès le premier euro (CGI, art. 259 D, II-2) et être ainsi au régime général mentionné au II-A § 210.

Les modalités de cette option sont les suivantes.

250
Durée de l'option, reconduction et dénonciation : L'option couvre obligatoirement une période de deux années civiles en plus de celle au cours de laquelle elle a été exercée.

Elle est renouvelable par tacite reconduction par période de deux années civiles, sauf dénonciation deux mois au moins avant l'expiration de chaque période.

260
Forme de l'option et de sa dénonciation : L'option prend effet le premier jour du mois au cours duquel elle est déclarée. Cette option doit être formulée par écrit. Elle peut être exercée à n'importe quel moment de l'année.

La dénonciation de l'option prend effet le 1^{er} janvier de l'année suivant celle au cours de laquelle elle est déclarée. Elle doit être formulée par écrit, au cours de l'année d'échéance de l'option, au plus tard le 31 octobre.
Le service des impôts des entreprises compétent pour recevoir la déclaration d'option ainsi que la dénonciation est celui dont relève le prestataire.

270
```

### VAT-Q025

CGI259D/258A; current generic BOI-TVA-CHAMP-20-50-40-20 §220/240–270; https://bofip.impots.gouv.fr/bofip/11964-PGP.html/identifiant=BOI-TVA-CHAMP-20-50-40-20-20211222; actual original read 2026-10-29. Native LF [268, 273]; reader SHA256 `9a09a1a72252414a67f632092c864b85b2e83fc426df936a26881d862986dab4`. Inherited actual C selected reading, exact read-scope records preserved

```text
État membre : désigne un État de l'Union européenne autre que la France.

Pays tiers : pays n'appartenant pas à l'Union européenne et territoire d'un État membre exclu du territoire de l'Union européenne (【33†CGI, art. 256-0†www.legifrance.gouv.fr】).

Preneur : client direct du prestataire.
Seuil : correspond à la valeur totale de 10 000 €, hors TVA, des prestations de services mentionnées aux 10°, 11°, 12° de l'article 259 B du CGI et des ventes à distance intracommunautaires de biens mentionnées au II bis de l’【34†article 256 du CGI†www.legifrance.gouv.fr】 réalisées à partir de l’Etat membre d’établissement du prestataire.
```

### VAT-Q026

Official2026notice3310-NOT-CA3-SD, ordinary period/form/legal conditions; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf; actual original read 2026-10-29. Native LF [58, 85]; reader SHA256 `23b05f9ed570dc9418217d987448baf202714f13d6ca49ea07d3641c972aef81`. Inherited actual C selected reading, exact read-scope records preserved

```text
La TVA et les taxes assimilées doivent être déclarées et acquittées selon une périodicité mensuelle. Seuls les redevables dont la taxe
exigible annuellement est inférieure à 4 000 € peuvent déposer des déclarations n° 3310-CA3 trimestrielles.

Dans tous les cas, ne cumulez jamais plusieurs mois (ou trimestres) sur une même déclaration. Lorsque aucune opération n’a été
réalisée au cours d’une période, souscrivez une déclaration, de manière électronique, en cochant la case correspondant à une
déclaration « Néant ».

DÉCLARATION ET PAIEMENT
La télétransmission des déclarations de TVA et de taxes assimilées, des paiements associés et des demandes de remboursement de
crédit de TVA est obligatoire pour tous les redevables.
Cette procédure peut être mise en œuvre selon une des modalités suivantes :
– l’échange de formulaires informatisé (EFI) est accessible à partir du site impots.gouv.fr, l’entreprise saisit sur un serveur sécurisé les
données à télétransmettre et signe avec un certificat numérique ;
– l’échange de données informatisé (EDI) par lequel un prestataire de l’entreprise transmet à l’administration un fichier obtenu avec un
logiciel de comptabilité. Cette modalité est particulièrement adaptée aux entreprises qui recourent aux services d’un cabinet
comptable.

Des informations supplémentaires sont disponibles sur le portail fiscal (impots.gouv.fr) rubrique « professionnels ».

Si vous disposez d’une créance sur le Trésor (crédit de TVA, excédent d’impôt sur les sociétés…), vous pouvez sous condition utiliser
tout ou partie de cette créance pour payer un impôt professionnel encaissé par le réseau comptable de la Direction générale des
finances publiques.
Pour obtenir des informations sur ce service et le formulaire n° 3516 à souscrire, vous pouvez contacter votre service des impôts ou
consulter le site impots.gouv.fr.

LES ARRONDIS FISCAUX
La base imposable et le montant de l’impôt sont arrondis à l’euro le plus proche. Les bases et cotisations inférieures à 0,50 euro sont
négligées et celles supérieures ou égales à 0,50 euro sont comptées pour 1.
```

### VAT-Q027

Official2026notice3310-NOT-CA3-SD, ordinary period/form/legal conditions; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf; actual original read 2026-10-29. Native LF [589, 599]; reader SHA256 `23b05f9ed570dc9418217d987448baf202714f13d6ca49ea07d3641c972aef81`. Inherited actual C selected reading, exact read-scope records preserved

```text
    ✔ Lignes 19 et 20 :
Déterminer les droits à déduction de la période en indiquant la taxe déductible correspondant aux biens et services ouvrant droit à
déduction. La TVA déduite au titre de chacune des catégories est arrondie à l’unité la plus proche.
Les fractions d’euro inférieures à 0,50 sont négligées, celles supérieures ou égales à 0,50 sont comptées pour 1.

La déduction est effectuée sur la déclaration déposée au titre du mois (ou du trimestre) au cours duquel est intervenue l’exigibilité
de la taxe. Par exemple, cette dernière intervient généralement lors du transfert de propriété lorsqu’il s’agit de l’acquisition sur le
marché intérieur d’un bien meuble corporel.
– les biens constituant des immobilisations sont les biens acquis ou créés, non pour être vendus, mais pour être utilisés d’une
manière durable comme instruments de travail ou moyens d’exploitation : terrains, constructions, matériels… ;
– les autres biens et services sont, d’une part, les biens qui constituent des valeurs d’exploitation comme les marchandises, les
```

### VAT-Q028

Official2026notice3310-NOT-CA3-SD, ordinary period/form/legal conditions; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf; actual original read 2026-10-29. Native LF [811, 818]; reader SHA256 `23b05f9ed570dc9418217d987448baf202714f13d6ca49ea07d3641c972aef81`. Inherited actual C selected reading, exact read-scope records preserved

```text

    ✔ Ligne 26 :
La demande de remboursement d’un crédit de TVA est autorisée dès lors que le crédit dégagé remplit les conditions de seuil
minimum suivantes :
- 760 euros : remboursement mensuel ou trimestriel formulé au titre de janvier à novembre ou des trois premiers trimestres.
- 150 euros : remboursement annuel formulé au titre de décembre ou du 4ème trimestre.

    ✔ Ligne AA :
```

### VAT-Q029

Official2026notice3310-NOT-CA3-SD, ordinary period/form/legal conditions; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf; actual original read 2026-10-29. Native LF [325, 335]; reader SHA256 `23b05f9ed570dc9418217d987448baf202714f13d6ca49ea07d3641c972aef81`. Inherited actual C selected reading, exact read-scope records preserved

```text
    ✔ Ligne B5 :
Indiquer les correctifs qui ont affecté le montant du chiffre d’affaires, notamment : les rabais, les factures d’avoir consentis à des
clients. Il est à noter que l’envoi de factures rectificatives à un client assujetti non établi en France, qui a obtenu le remboursement de
la taxe facturée à tort (CGI, ann. II, art. 242-0 M à 242-0 Z decies), n’est pas autorisé. Les notes d’avoir, éventuellement adressées à
ces clients, doivent être nettes de taxes.
Pour plus de précisions, il convient de se reporter aux paragraphes 20 à 40 du BOI-TVA-DED-50-20-30-20 et aux paragraphes 400 à
420 du BOI-TVA-DED-50-20-30-40.
Le montant qui figure ligne B5 est une régularisation qui ne doit pas conduire à modifier les montants figurant aux autres lignes du
cadre A. Le complément de TVA déductible sera compris dans le montant indiqué à la ligne 21 de l’imprimé et individualisé à la
rubrique « (dont régularisation de TVA collectée…) » qui figure sous la ligne 21.
Attention : ne pas mentionner de « montants négatifs » sur cette ligne.
```

### VAT-Q030

Official2026notice3310-NOT-CA3-SD, ordinary period/form/legal conditions; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf; actual original read 2026-10-29. Native LF [443, 454]; reader SHA256 `23b05f9ed570dc9418217d987448baf202714f13d6ca49ea07d3641c972aef81`. Inherited actual C selected reading, exact read-scope records preserved

```text
    ✔ Ligne F8 :
Indiquer les correctifs qui ont affecté des opérations non imposables, notamment : les rabais, les factures d’avoir consentis à des
clients.
Il est à noter que l’envoi de factures rectificatives à un client assujetti étranger non établi en France, qui a obtenu le remboursement
de la taxe facturée à tort (CGI, ann. II, art. 242-0 M à 242-0 Z decies), n’est pas autorisé. Les notes d’avoir, éventuellement adressées
à ces clients, doivent être nettes de taxes.
Pour plus de précisions, il convient de se reporter au BOFiP-Impôts : paragraphes 20 à 40 du BOI-TVA-DED-50-20-30-20 et aux
paragraphes 400 à 420 du BOI-TVA-DED-50-20-30-40.

Attention : ne pas mentionner de « montants négatifs » sur cette ligne.
Le montant qui figure ligne F8 est une régularisation qui ne doit pas conduire à modifier les montants figurant aux autres lignes du
cadre A.
```

### VAT-Q031

Official2026notice3310-NOT-CA3-SD, ordinary period/form/legal conditions; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf; actual original read 2026-10-29. Native LF [530, 545]; reader SHA256 `23b05f9ed570dc9418217d987448baf202714f13d6ca49ea07d3641c972aef81`. Inherited actual C selected reading, exact read-scope records preserved

```text
6) Lignes 15 à 18

    ✔ Ligne 15 :
Procéder, en respectant les règles des arrondis fiscaux énoncées au cadre I, au reversement de la TVA antérieurement déduite
lorsque des régularisations de déductions sont nécessaires, notamment :
– modification du pourcentage de déduction ;
– renonciation à une option ;
– réception de factures d’avoirs des fournisseurs ;
– reversement de la taxe déductible en application de l’article 207 de l’annexe II au CGI ;
– reversement de la taxe déductible résultant des variations du pourcentage de déduction ;
– régularisations de crédit de TVA à la suite de contrôles fiscaux ;
– déductions opérées à tort (y compris celles se rapportant aux produits pétroliers mentionnés aux articles L.312-2 du CIBS
(anciennement tableau B de l’article 265 du code des douanes) ou à des acquisitions intracommunautaires).
Dans ce dernier cas, il convient de préciser dans le cadre réservé à la correspondance la nature de l’erreur initialement commise, la
déclaration entachée de cette erreur et les modalités de calcul de la correction opérée.

```

### VAT-Q032

Official2026notice3310-NOT-CA3-SD, ordinary period/form/legal conditions; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf; actual original read 2026-10-29. Native LF [654, 688]; reader SHA256 `23b05f9ed570dc9418217d987448baf202714f13d6ca49ea07d3641c972aef81`. Inherited actual C selected reading, exact read-scope records preserved

```text
     ✔ Ligne 21 :
Doit être indiqué ici le complément de la taxe déductible, notamment :
– la taxe dont la déduction a été omise sur les déclarations déposées depuis le 1er janvier de la deuxième année précédant celle du
dépôt de la déclaration y compris pour les produits pétroliers ;
– le complément de déduction résultant des variations du pourcentage de déduction ;
– les transferts de droits à déduction reçus ;
– le complément de déduction qui résulte de l’application de l’article 207 de l’annexe II au CGI ;
– la taxe acquittée à tort au titre d’opérations non imposables ou d’opérations facturées à un taux supérieur au taux légalement
exigible (l’envoi d’une facture rectificative est également exigé) y compris pour la taxe due sur les produits pétroliers ;
– la taxe acquittée par les entreprises soumises au paiement de la TVA d’après les encaissements et correspondant à des chèques
non provisionnés ;
– la taxe acquittée à l’occasion de ventes ou services définitivement impayés, résiliés, annulés ;

La récupération de cette taxe est subordonnée à la justification de la rectification préalable de la facture initiale. En ce qui concerne
les opérations impayées (y compris en cas de liquidation judiciaire), l’entreprise doit adresser à son débiteur un duplicata de la facture
initiale surchargée de la mention « facture demeurée impayée pour la somme de ................................................ € (prix hors taxe) et
pour la somme de ................................................ € (TVA correspondante) qui ne peut faire l’objet d’une déduction (art. 272 du CGI) ».
L’entreprise est dispensée d’adresser ce duplicata pour chaque facture impayée à condition qu’elle délivre à chaque client défaillant
un état récapitulatif des factures impayées qui mentionne pour chacune d’entre elles :
– le numéro d’ordre, le libellé, la date et la référence du folio d’enregistrement de la facture initiale ;
– le montant hors taxe ;
– la mention « facture impayée pour la somme de ................................................ € (HT) et pour la somme
de ................................................ € (taxe correspondante) qui ne peut faire l’objet d’une déduction (art. 272 du CGI) ».
Une copie de l’état récapitulatif doit être conservée à l’appui de la comptabilité. Un exemplaire doit être produit au service des impôts
lorsque celui-ci en fait la demande.

– la taxe acquittée sur des opérations pour lesquelles une réduction de prix a été consentie après l’établissement de la facture (l’envoi
d’une note d’avoir ou l’émission d’une nouvelle facture annulant et remplaçant la précédente est également exigé).
La TVA, acquittée au titre des opérations énoncées aux deux derniers tirets, doit être individualisée à la rubrique « (dont régularisation
sur de la TVA collectée…) » qui figure sous la ligne 21.
Il est à noter que l’envoi de factures rectificatives à un client assujetti étranger non établi en France, qui a obtenu le remboursement
de la taxe (CGI, ann. II, art. 242-0 M à 242-0 Z ter), n’est pas autorisé. Les notes d’avoir, éventuellement adressées à ces clients,
doivent être nettes de taxes.Ligne 22 :
Le crédit dont le remboursement a été demandé ne peut plus donner lieu à imputation. (CGI, ann II, art 242-0-E)
Le montant du crédit dont le remboursement a été refusé pour des motifs d’irrecevabilité de la demande en la forme pourra être
```

### VAT-Q033

Official2026notice3310-NOT-CA3-SD, ordinary period/form/legal conditions; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf; actual original read 2026-10-29. Native LF [160, 190]; reader SHA256 `23b05f9ed570dc9418217d987448baf202714f13d6ca49ea07d3641c972aef81`. Inherited actual C selected reading, exact read-scope records preserved

```text
Conformément aux dispositions de l’article 1788-A-1 du CGI, le défaut de production dans les délais donne lieu à l’application d’une
amende de 750 €, qui peut être portée à 1 500 € si la défaillance persiste dans les trente jours d’une mise en demeure.

LIEU DE TAXATION DES PRESTATIONS DE SERVICES

1) PRINCIPES GÉNÉRAUX (article 259 du CGI)
Prestations entre assujettis : le lieu des prestations de services est situé en France lorsque le preneur est un assujetti établi en
France (article 259-1° du CGI). Par ailleurs, dans cette hypothèse, le preneur est le redevable de la taxe (article 283-2 du CGI).

Conformément à l’article 289 B-III du CGI, toute personne physique ou morale est tenue de souscrire une déclaration
européenne de services (DES) lorsque les conditions suivantes sont réunies :
– avoir en France le siège de son activité économique ou un établissement stable à partir duquel le service est rendu, ou à défaut, son
domicile ou sa résidence habituelle ;
– réaliser une prestation de services au profit d’un assujetti agissant en tant que tel qui a, dans un autre État membre de l’Union
européenne, son siège économique ou un établissement stable pour lequel le service est fourni, ou son domicile ou sa résidence
habituelle ;
– la prestation est située dans cet autre État membre en application de l’article 44 de la directive 2006/112/CE du 28 novembre 2006.
Toutefois, lorsque la prestation bénéficie d’une exonération dans l’État membre du preneur, le prestataire n’est pas tenu de
mentionner cette opération dans sa DES ;
– le redevable de la taxe due au titre de cette prestation est le preneur en application de l’article 196 de la directive 2006/112/CE déjà
citée.
La déclaration doit être produite dans les dix jours ouvrables qui suivent le mois au cours duquel la TVA est devenue exigible au titre
des prestations de services réalisées. Les assujettis sont dans l’obligation de transmettre leur déclaration en utilisant le téléservice
DES accessible via le portail « https://pro.douane.gouv.fr ». Toutefois, les entreprises bénéficiant du régime de la franchise en base en
matière de TVA ont la faculté de déposer une déclaration sur support papier.




                                                                                                                                      3/18
Prestations fournies à des personnes non assujetties : le lieu des prestations de services, autres que celles désignées aux
```

### VAT-Q034

Official2026notice3310-NOT-CA3-SD, ordinary period/form/legal conditions; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf; actual original read 2026-10-29. Native LF [125, 158]; reader SHA256 `23b05f9ed570dc9418217d987448baf202714f13d6ca49ea07d3641c972aef81`. Inherited actual C selected reading, exact read-scope records preserved

```text
à la taxe.

Les acquisitions intracommunautaires sont taxables chez l’acquéreur, au taux en vigueur dans le pays de destination (cf. ligne B2). Le
fournisseur est autorisé à délivrer une facture hors taxes à la condition qu’il y ait effectivement transfert physique des biens et que
l’acquéreur communique un numéro de TVA intracommunautaire valide dans la base des assujettis. À défaut la TVA lui sera facturée.

Si une anomalie dans la base des assujettis est signalée, seul le service des impôts dont relève l’entreprise est compétent pour en
opérer la rectification.

DÉFINITION DES LIVRAISONS INTRACOMMUNAUTAIRES
Les livraisons intracommunautaires sont constituées des livraisons de biens expédiés ou transportés sur le territoire d’un autre État
membre de l’Union européenne à destination d’un autre assujetti ou d’une personne morale non assujettie qui ne bénéficie pas, dans
son État membre, d’un régime dérogatoire l’autorisant à ne pas soumettre à la TVA ses acquisitions intracommunautaires.

Sont assimilés à des livraisons de biens, l’expédition ou le transport par un assujetti ou pour son compte, d’un bien meuble corporel
pour les besoins de son entreprise, à destination d’un autre État membre.

Les livraisons intracommunautaires sont exonérées de TVA dans le pays de départ (cf. ligne F2) à condition qu’il y ait effectivement
transfert physique des biens et que l’acquéreur communique un numéro de TVA intracommunautaire valide dans la base des
assujettis.

Avant toute facturation hors taxe, les entreprises doivent s’assurer de la validité du numéro de TVA intracommunautaire des clients
établis dans un autre État membre en consultant le site internet :« http://ec.europa.eu/taxation_customs/vies/ ». En cas de
difficulté, elles peuvent interroger le service des impôts dont elles relèvent.

Pour plus de précisions sur les moyens de preuve permettant d’établir le bien-fondé de l’exonération, il convient de se reporter au
BOFiP-Impôts : BOI-TVA-CHAMP-30-20-10.

Conformément à l’article 289 B du CGI, les entreprises qui réalisent des livraisons intracommunautaires doivent souscrire
auprès de l’administration des douanes un état récapitulatif des clients.

Cet état doit être souscrit dans les dix jours ouvrables qui suivent le mois au cours duquel la TVA est devenue exigible au titre des
livraisons intracommunautaires de biens ou le mois au cours duquel a eu lieu le mouvement de marchandises pour les autres
opérations.
```

### VAT-Q035

Official2026notice3310-NOT-CA3-SD, ordinary period/form/legal conditions; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf; actual original read 2026-10-29. Native LF [270, 300]; reader SHA256 `23b05f9ed570dc9418217d987448baf202714f13d6ca49ea07d3641c972aef81`. Inherited actual C selected reading, exact read-scope records preserved

```text
Indiquer le montant hors TVA des opérations taxables particulières qui ne constituent pas votre chiffre d’affaires courant,
notamment : les cessions d’immobilisations, livraisons à soi-même d’immobilisations, autres livraisons à soi-même ou prestations de
services à soi-même imposables en vertu des articles 257-I-3-1° et 257-II du CGI, les achats à des non-redevables de la TVA pour
lesquels la taxe doit être payée par l’acheteur, les droits d’auteur soumis à la retenue de TVA, l’acquisition d’or sous la forme de
matière première ou de produits semi-ouvrés d’une pureté égale ou supérieure à 325 millièmes, les acquisitions et prestations de
façon portant sur des déchets neufs d’industrie et des matières de récupération visées à l’article 283-2 sexies, les achats de quotas
d’émission de gaz à effet de serre et d’autres unités de réduction des émissions visés à l’article 283-2 septies, les achats de
communication électroniques visés à l’article 283-2 octies du CGI et les travaux de construction, y compris ceux de réparation, de
nettoyage, d’entretien, de transformation et de démolition effectués en relation avec un bien immobilier par une entreprise sous-
traitante, visés à l’article 283-2 nonies.

    ✔ Ligne A3 :
Indiquer le montant hors TVA des achats de prestations de services fournies par un prestataire non établi en France et imposables en
France sur le fondement des articles 259-1° et 283-2 du CGI.

    ✔ Ligne A4 :
Indiquer le montant hors TVA des importations taxables autres que celles portant sur les produits pétroliers. Pour l'application de la
taxe sur la valeur ajoutée, est considérée comme importation d'un bien :
- l'entrée en France métropolitaine d'un bien originaire ou en provenance des départements de la Guadeloupe, de la Guyane, de
Mayotte, de la Martinique ou de la Réunion ;
- l'entrée dans les départements de la Guadeloupe ou de la Martinique d'un bien originaire ou en provenance de la France
métropolitaine, d'un autre Etat membre de la Communauté européenne, des départements de la Guyane, de Mayotte, ou de la
Réunion ;
- l'entrée dans le département de la Réunion d'un bien originaire ou en provenance de la France métropolitaine, d'un autre Etat
membre de la Communauté européenne, des départements de la Guadeloupe, de la Guyane, de Mayotte, ou de la Martinique.

    ✔ Ligne A5 :
Indiquer le montant hors TVA des opérations taxables en sorties de régime fiscal suspensif et les sorties de régime particulier
douanier, uniquement lorsque des livraisons ont eu lieu en cours de régime (article 277 A du CGI).

Précision : la ligne A4 et les lignes I1 à I6 sont actuellement pré-remplies à tort des données relatives aux sorties de régime
```

### VAT-Q036

Official2026notice3310-NOT-CA3-SD, ordinary period/form/legal conditions; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf; actual original read 2026-10-29. Native LF [304, 323]; reader SHA256 `23b05f9ed570dc9418217d987448baf202714f13d6ca49ea07d3641c972aef81`. Inherited actual C selected reading, exact read-scope records preserved

```text
    ✔ Ligne B1 :
Seulement si vous êtes redevable de TICPE, c’est-à-dire que vous mettez à la consommation des produits pétroliers mentionnés aux
articles L.312-2 et suivants du CIBS (anciennement tableau B du 1 de l’article 265 du code des douanes dans sa rédaction en
vigueur au 31 décembre 2021) déclarés à la DGDDI dans l’application ISOPE, indiquer le montant des importations de produits
pétroliers non placées sous un régime suspensif et les sorties de produits pétroliers du régime suspensif.

    ✔    Ligne B2 : (pour les DOM, cf. III encadré)
Le montant total hors taxe sur la valeur ajoutée des acquisitions intracommunautaires taxables doit être mentionné sur cette ligne (cf.
BOI-TVA-CHAMP-10-10-40-20 et pour la définition de cette notion, paragraphe 10 du BOI-TVA-CHAMP-10-10-40).
NOTA : la taxe due sur les acquisitions intracommunautaires est exigible au plus tard le 15 du mois suivant le fait générateur (qui
correspond au transfert de propriété dans la majorité des cas). Toutefois, l’exigibilité intervient à la date de la facture lorsque celle-ci
est établie entre le fait générateur et le 15 du mois qui le suit.

    ✔ Ligne B3 :
cf. AIDE AU REMPLISSAGE en début de chapitre IV

    ✔ Ligne B4 :
Indiquer le montant total hors TVA des achats de biens ou de prestations de services mentionnés à l’article 259 A du CGI, réalisés
auprès d’un assujetti non établi en France et au titre desquels vous êtes redevable de la TVA en application du deuxième alinéa de
l’article 283-1 du CGI (cf. BOI-TVA-GEO et BOI-TVA-SECT).
```

### VAT-Q037

Official2026notice3310-NOT-CA3-SD, ordinary period/form/legal conditions; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf; actual original read 2026-10-29. Native LF [350, 395]; reader SHA256 `23b05f9ed570dc9418217d987448baf202714f13d6ca49ea07d3641c972aef81`. Inherited actual C selected reading, exact read-scope records preserved

```text
    ✔ Ligne E1 :
Indiquer les opérations constitutives de chiffre d’affaires (ventes à l’exportation hors de l’Union européenne ou dans un DOM,
livraisons de biens expédiés ou transportés hors de l’Union européenne, par l’acheteur établi hors de l’Union européenne ou pour son
compte, exonérées en application de l’article 262-I-2° du CGI) qui permettent d’effectuer en franchise des achats, des acquisitions
intracommunautaires ou des importations déclarées ligne F6.
En ce qui concerne les DOM, sont considérées comme exportations les ventes à destination de la métropole, des pays tiers
(membres de l’Union européenne ou non) ainsi que celles effectuées vers les autres DOM (à l’exception des ventes entre la
Guadeloupe et la Martinique).

    ✔ Ligne E2 :
Indiquer les autres opérations constitutives de votre chiffre d’affaires :
– les livraisons et prestations en suspension de taxe (art. 277 A et 298 du CGI) ou en franchise de taxe (art. 275 du CGI) ;
– les opérations intervenues dans le cadre des transmissions d’universalités totales ou partielles de biens dispensées de TVA en
application de l’article 257 bis du CGI ;
– les livraisons et prestations de façon portant sur des déchets neufs d’industrie et des matières de récupération visées à l’article 283-
2 sexies du CGI ;
– les ventes de gaz naturel ou d’électricité et les prestations directement liées non destinés à être consommés en France, à un
acquéreur établi et identifié à la TVA en France, visées au second alinéa de l’article 283-2 quinquies du CGI ;
– les transferts de quotas d’émission de gaz à effet de serre et d’autres unités de réduction des émissions visés à l’article 283-2
septies du CGI ;
– les ventes de services de communications électroniques visés à l’article 283-2 octies du CGI ;
– les travaux de construction, y compris ceux de réparation, de nettoyage, d’entretien et de démolition effectués en relation avec un
bien immobilier visés à l’article 283-2 nonies du CGI ;
– les ventes de services de télécommunication, de radiodiffusion et de télévision ainsi que les ventes de services délivrés par voie
électronique à des personnes non-assujetties ayant leur domicile ou leur résidence habituelle sur le territoire de l’UE et qui sont
déclarées dans l’État membre de consommation via le mini-guichet unique ;
– les autres opérations non imposables (affaires exonérées, fraction non imposable des opérations dont la TVA est calculée sur la
marge, prestations de services rendues à un preneur établi à l’étranger – même si elles sont taxées chez ce dernier).

    ✔ Ligne E3 :
Le montant total des ventes à distance taxables dans l’État membre d'arrivée (non imposables en France) constitutives de votre chiffre
d'affaires doit être mentionné sur cette ligne. Il s'agit des ventes à distance au profit d’une personne bénéficiant de la dérogation
prévue au 2° du 1 de l'article 256 bis ou à destination de toute autre personne non assujettie (ventes des entreprises aux particuliers
consommateurs finaux dénommées « BtoC », « Business to Consumer ») qui excèdent le seuil de 10 000 € mentionné au 2 de l’article
259 D du CGI ou pour lesquelles l’assujetti a opté pour que leur lieu d’imposition soit situé dans l’État membre de destination (et qui
sont déclarées dans l’État membre de consommation via le mini-guichet unique).

    ✔ Ligne E4 :
Indiquer le montant des importations autres que celles portant sur les produits pétroliers lorsque le montant de la TVA dû, avant prise
en compte des éventuels droits à déduction, est nul, quelle qu’en soit la raison (exonération ou suspension de la taxe sur la valeur
ajoutée), à l’exception toutefois des importations réalisées en franchise de la TVA sur le fondement de l’article 275 du CGI, à indiquer
en ligne F6.

    ✔ Ligne E5 :
Indiquer le montant des sorties de RFS lorsque le montant de TVA dû, avant prise en compte des éventuels droits à déduction, est nul,
quelle qu’en soit la raison (exonération ou suspension de la taxe sur la valeur ajoutée).
```

### VAT-Q038

Official2026notice3310-NOT-CA3-SD, ordinary period/form/legal conditions; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf; actual original read 2026-10-29. Native LF [395, 406]; reader SHA256 `23b05f9ed570dc9418217d987448baf202714f13d6ca49ea07d3641c972aef81`. Inherited actual C selected reading, exact read-scope records preserved

```text
quelle qu’en soit la raison (exonération ou suspension de la taxe sur la valeur ajoutée).

    ✔ Ligne E6 :
Indiquer le montant des importations de biens placées sous un régime fiscal suspensif (3° du I de l’article 277 A du CGI).

    ✔ Ligne F1 :
Indiquer le montant des acquisitions intracommunautaires non taxées, y compris celles relatives aux produits pétroliers.

    ✔    Ligne F2 : (pour les DOM, cf. III encadré)
Livraisons intracommunautaires à destination d’une personne assujettie : relations entre personnes assujetties dénommées « BtoB »
(« Business to Business »).

```

### VAT-Q039

Official2026notice3310-NOT-CA3-SD, ordinary period/form/legal conditions; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf; actual original read 2026-10-29. Native LF [409, 434]; reader SHA256 `23b05f9ed570dc9418217d987448baf202714f13d6ca49ea07d3641c972aef81`. Inherited actual C selected reading, exact read-scope records preserved

```text
Le montant total hors taxe des livraisons de biens intracommunautaires exonérées constituant du chiffre d’affaires (pour la
définition de cette notion, voir paragraphe III) doit être mentionné sur cette ligne.

Ces opérations sont susceptibles d’ouvrir droit à la procédure des achats, acquisitions intracommunautaires ou importations en
franchise de taxe.

    ✔ Ligne F3 :
cf. AIDE AU REMPLISSAGE en début de chapitre IV

    ✔ Ligne F4 :
Seulement si vous êtes redevable de TICPE, c’est-à-dire que vous mettez à la consommation des produits pétroliers mentionnés aux
articles L.312-2 et suivants du CIBS (anciennement tableau B du 1 de l’article 265 du code des douanes dans sa rédaction en
vigueur au 31 décembre 2021) déclarés à la DGDDI dans l’application ISOPE, indiquer les sorties de produits pétroliers du régime
suspensif non taxables :
- les produits pétroliers pour lesquels le redevable est dispensé du paiement de la taxe lorsque le bien fait l'objet d'une exportation ou
d'une livraison exonérée en vertu de l'article 262 ou du I de l'article 262 ter du CGI.
- les mises à la consommation de produits pétroliers exonérées qui ont lieu dans les départements de la Guyane, de la Guadeloupe,
de la Martinique et de la Réunion (art 295-1-6° du CGI).

    ✔ Ligne F5 :
Seulement si vous êtes redevable de TICPE, indiquer le montant des importations de produits pétroliers placés sous régime fiscal
suspensif (art 277 A I 3° du CGI).

    ✔ Ligne F6 :
Indiquer le montant total des achats, acquisitions intracommunautaires ou importations réalisés en franchise de taxe (art. 275 du
CGI).
```

### VAT-Q040

Official2026notice3310-NOT-CA3-SD, ordinary period/form/legal conditions; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf; actual original read 2026-10-29. Native LF [553, 575]; reader SHA256 `23b05f9ed570dc9418217d987448baf202714f13d6ca49ea07d3641c972aef81`. Inherited actual C selected reading, exact read-scope records preserved

```text
    ✔ Ligne 5B :
– Ajouter les insuffisances de déclaration commises par les entreprises.
– Reporter le montant de la ligne « g » calculé sur le bulletin n° 3515 qui doit obligatoirement être télédéclaré avec la déclaration
n° 3310-CA3 (entreprises autorisées à bénéficier du régime des acomptes provisionnels).

NOTA : l’entreprise qui corrige spontanément une erreur de déclaration à l’aide des lignes 2C et 5B doit mentionner dans le cadre
réservé à la correspondance, pour chaque période d’imposition :
– la nature de l’erreur ;
– la (ou les) déclaration(s) concernée(s) ;
– les modalités de détermination du complément d’impôt porté sur la ligne 5B.

     ✔ Ligne 17 : (pour les DOM, cf. III encadré)
Doit être impérativement mentionnée ici la taxe brute correspondant aux acquisitions taxables déclarées ligne B2.

    ✔   Ligne 18 : (ne concerne pas les DOM)
Doit être impérativement mentionnée ici la taxe correspondant aux opérations imposables réalisées à destination de Monaco,
c’est-à-dire la taxe qui devrait être acquittée à Monaco si les opérations réalisées en France métropolitaine et à Monaco étaient
déclarées dans chacun des deux États.

Remarque : les assujettis établis ou disposant d’un établissement stable en France, qui réalisent des opérations en France
métropolitaine et à Monaco déclarent l’ensemble des opérations réalisées dans chacun des États sur la déclaration de TVA déposée
en France métropolitaine. Les entrepreneurs de travaux immobiliers et les établissements bancaires ne sont pas concernés par cette
mesure.
```

### VAT-Q041

Official2026notice3310-NOT-CA3-SD, ordinary period/form/legal conditions; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf; actual original read 2026-10-29. Native LF [793, 837]; reader SHA256 `23b05f9ed570dc9418217d987448baf202714f13d6ca49ea07d3641c972aef81`. Inherited actual C selected reading, exact read-scope records preserved

```text
    ✔ Lignes X5 et Z5 : se reporter au chapitre consacré aux régularisations d’accise sur les énergies.
    ✔ Ligne 28 :
Indiquer le montant de TVA nette due après imputation d’un éventuel crédit d’accise sur les énergies (ligne TD – ligne X5). Attention,
ce montant ne peut pas être négatif. L’imputation du crédit d’accise sur les énergies s’effectue dans la limite de la TVA due ligne TD.

    ✔ Ligne 29 :
Reporter ici le montant total des taxes assimilées (calculées sur l'annexe 3310 A) dont l’entreprise est redevable (cf. paragraphe VI).

    ✔ Ligne AB :
Si vous êtes membre d’un groupe ayant opté pour le régime de consolidation du paiement de la TVA, vous devez indiquer le total à
payer (lignes 28 + 29 + Z5) qui est acquitté par la société tête de groupe sur la déclaration récapitulative n° 3310-CA3G (CGI, article
1693 ter).

    ✔ Ligne 32 :
Pour les redevables autres que les assujettis uniques, le total à payer tient compte, le cas échéant, des régularisations d ’accise sur
les énergies et des taxes assimilées dues.

CRÉDIT DE TVA ET RELIQUAT D‘ACCISE SUR LES ÉNERGIES À REMBOURSER

    ✔ Ligne 26 :
La demande de remboursement d’un crédit de TVA est autorisée dès lors que le crédit dégagé remplit les conditions de seuil
minimum suivantes :
- 760 euros : remboursement mensuel ou trimestriel formulé au titre de janvier à novembre ou des trois premiers trimestres.
- 150 euros : remboursement annuel formulé au titre de décembre ou du 4ème trimestre.

    ✔ Ligne AA :
Si vous êtes membre d’un groupe ayant opté pour le régime de consolidation du paiement de la TVA, vous devez indiquer le crédit de
TVA (report de la ligne 25) qui est transféré et déclaré par la société tête de groupe sur la déclaration récapitulative n° 3310-CA3G
(CGI, article 1693 ter). Le crédit de TVA constaté en ligne 25 ne peut faire l’objet d’aucun report sur une déclaration ultérieure (ligne
27). Il est définitivement transmis à la société tête de groupe.
     ✔ Ligne 27 :
Le crédit de TVA dont le remboursement n’est pas demandé (ligne 25 – ligne 26) est reporté ligne 22 de la prochaine déclaration.

    ✔ Ligne Y5 :


                                                                                                                                     12/18
Se reporter au chapitre consacré aux régularisations d’accise sur les énergies.

    ✔ Ligne Y6 :
Si vous êtes membre d’un groupe ayant opté pour le régime de consolidation du paiement de la TVA, vous devez indiquer le crédit
d’accise sur les énergies (ligne Y4) qui est transféré et déclaré par la société tête de groupe sur la déclaration récapitulative n° 3310-
CA3G (CGI, article 1693 ter).

Précision : les lignes Y5 et Y6 sont exclusives l’une de l’autre. Le report en ligne Y5 ou Y6 du reliquat de crédit d‘accise sur les
```

### VAT-Q042

OfficialCA12/CA12Eform3517-S-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5291.pdf; actual original read 2026-10-29. Native LF [109, 133]; reader SHA256 `ed1e2e8994d3f6d30976b0d500e78c97ca030bd70e2b105246399d657ad05c19`. Inherited actual C selected reading, exact read-scope records preserved

```text
   (article 283-2 du code général des impôts)
11   Cessions d’immobilisations                                                         0970    …………………………………. ………………………………….
12   Livraisons à soi-même                                                              0980    …………………………………. ………………………………….
13   Autres opérations imposables                                                       0981    …………………………………. ………………………………….
16                TOTAL DE LA TAXE DUE (ligne 5A à 13)                                                                           ………………………………...
     Autre TVA DUE
17   Remboursements provisionnels obtenus en cours d’année ou d’exercice                                                0983     ………………………………….
18   TVA antérieurement déduite à reverser dont TVA sur les produits pétroliers ………………..                                0600     ………………………………….
AD Sommes à ajouter                                                                                                     0602     ………………………………….
19                TOTAL DE LA TVA BRUTE DUE (lignes 16 + 17 + 18 + AD)                                                           …………………………………
         II – TVA DÉDUCTIBLE
     AUTRES BIENS ET SERVICES                                                                                                          Taxe déductible
20   Déductions sur factures (1)                                                                                        0702     ………………………………….
21   Déductions forfaitaires (1)                                                                                        0704     ………………………………….
22                TOTAL (lignes 20 + 21)                                                                                         …………………………………
     IMMOBILISATIONS
23   TVA déductible sur immobilisations (1)                                                                             0703    ………………………………….
     AUTRE TVA À DÉDUIRE
24   Crédit antérieur non imputé et non remboursé                                                                       0058     ………………………………….
25   Omissions ou compléments de déductions dont régularisations TVA déductible sur les produits pétroliers             0059     ………………………………….
25A (1) Compte-tenu, le cas échéant, du coefficient de déduction                ……..………… %
AE Sommes à imputer                                                                                                     0603     ………………………………….
26                TOTAL DE LA TVA DÉDUCTIBLE (lignes 22 + 23 + 24 + 25 + AE)                                                     …………………………………
2E   Dont TVA déductible sur les produits pétroliers                                                                    0711     ………………………………….

```

### VAT-Q043

OfficialCA12/CA12Eform3517-S-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5291.pdf; actual original read 2026-10-29. Native LF [140, 158]; reader SHA256 `ed1e2e8994d3f6d30976b0d500e78c97ca030bd70e2b105246399d657ad05c19`. Inherited actual C selected reading, exact read-scope records preserved

```text
           III – TVA NETTE
        RÉSULTAT DE LA LIQUIDATION                                                                                                                                       Taxe
28      TVA due : ( Ligne 19 – ligne 26 ) ou                                                                                                                 8900   ……………………………
29      CRÉDIT : ( Ligne 26 – ligne 19 )                                                                                                                     0705   ……………………………
        IMPUTATIONS/RÉGULARISATIONS DES ACOMPTES
                            Col. 1 : Montant                           Col. 2 : Montant                  30 Acomptes payés et / ou restant dus
                         effectivement payé                            restant à payer                                                                       0018   ……………………………
                                                                                                            (Tot. 1 + Tot. 2)
      Acompte 1        ....................................       ....................................

      Acompte 2        ....................................       ....................................

                       Tot. 1 .........................           Tot. 2 .........................

        RÉSULTAT NET
33      SOLDE DÛ si ligne 28 – (lignes 29 + 30) ≥ 0 ou                                                                                                              ……………………………
34      EXCÉDENT DE VERSEMENT : si ligne 30 – ligne 28 ≥ 0                                                                                                          ……………………………
35      SOLDE EXCÉDENTAIRE : (lignes 29 + 34)                                                                                                                0020   ……………………………
           IV – DÉCOMPTE DES TAXES ASSIMILÉES
```

### VAT-Q044

OfficialCA12/CA12Eform3517-S-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5291.pdf; actual original read 2026-10-29. Native LF [435, 451]; reader SHA256 `ed1e2e8994d3f6d30976b0d500e78c97ca030bd70e2b105246399d657ad05c19`. Inherited actual C selected reading, exact read-scope records preserved

```text
                                            BASE DE CALCUL DES ACOMPTES DUS AU TITRE DE L’EXERCICE SUIVANT
 57    TVA [ligne 16 – (lignes 11 + 12 + 22)]                                                                                                                                    …………………

           VII – DEMANDE DE REMBOURSEMENT


  Crédit remboursable dégagé à la clôture de l’année ou de l’exercice (≥ 150 €, ou, < à 150 € uniquement en cas de cession,                                    a
  décès, entrée dans un groupe TVA) (ligne 29)
  Excédent de versement dégagé (ligne 34)                                                                                                                      b
  Maximum remboursable (a + b)                                                                                                                                 c
  Remboursement demandé                                                                                                                                        d
  Crédit reportable (c – d)                                                                                                                                    e
Le soussigné (nom, prénom, qualité) :
demande le remboursement de la somme de (en chiffres)                                                    À …………………………………… ,                          Le ……………………………………..

– à créditer au compte désigné                                                              Cocher                                             Signature :
                                                                                            selon le
```

### VAT-Q045

OfficialF23566 TVAreturns/limits/periods; keep contradictory summary conditions explicit; https://entreprendre.service-public.gouv.fr/vosdroits/F23566; actual original read 2026-10-29. Native LF [125, 150]; reader SHA256 `14de3f97623ea9ffe4c3d4828684c75853de22275352fb7888bc75901e7af83a`. Inherited actual C selected reading, exact read-scope records preserved

```text
 Qu'est ce que le régime réel simplifié de TVA ? 
 Le régime réel simplifié de TVA s'applique à une entreprise à compter du 1 er janvier d’une année N lorsqu’elle respecte les seuils de chiffre d’affaires et de montant de TVA :
 Seuil concernant le chiffre d’affaires hors taxes
 Son chiffre d'affaires hors taxes en N-1 doit être compris entre :
 85 000 € et 945 000 € pour les activités de commerce, de restauration et de fourniture de logement (sauf location meublée) :
 37 500 € et 286 000 € pour les autres activités de prestation de services (dont la location meublée) :
 Son chiffre d'affaires hors taxes réalisé en N ne doit pas dépasser les seuils majorés suivants :
 Pour les activités de commerce, de restauration et de fourniture de logement (sauf location meublée) : 1 040 000 € 
 Pour les autres activités de prestation de services (dont la location meublée) : 323 000 € 
 À savoir 
 Ces seuils sont valables pour l’année 2026 (année N).
 Seuil concernant le montant de la TVA due
 Le montant de la TVA dû au titre de l’année N-1 doit être inférieur à 15 000 € 
 Conséquences en cas de dépassement
 En cas de dépassement, soit du seuil normal de chiffre d’affaires correspondant à l’activité exercée, soit du seuil de TVA due ( 15 000 € ) : l’entreprise bascule dans le régime réel normal de TVA à compter du 1 er janvier de l’année suivant celle du dépassement. 
 En cas de dépassement de l’un des seuils majorés de chiffre d’affaires, l’entreprise bascule dans le régime réel normal de TVA de manière rétroactive , c’est-à-dire que ce régime va s’appliquer à compter du 1 er janvier de l’année où le dépassement est survenu . L’entreprise doit alors souscrire une déclaration ( CA3 ) résumant l’ensemble des opérations réalisées sur l’ensemble du mois (ou du trimestre). Cette déclaration doit être effectuée le mois suivant le mois (ou le trimestre) du dépassement.
 Quand et comment faire sa déclaration de TVA ? 
 Les modalités de déclaration de la TVA diffèrent selon le montant de TVA déclaré par l'entreprise l'année précédente.
 Répondez aux questions successives et les réponses s’afficheront automatiquement
 Déclaration de moins de 15 000 €
 L'entreprise soumise à un régime simplifié de TVA doit faire une déclaration de TVA annuelle au plus tard le 2 e jour ouvré suivant le 1 er mai . Cette déclaration doit récapituler toutes les opérations imposables de l'année civile : titleContent précédente.
 La déclaration doit être faite en ligne sur le compte professionnel impot.gouv.fr de l'entreprise à l'aide du formulaire CA12 :
 Déclaration annuelle de régularisation de TVA - Régime simplifié (n° 3517-CA12) 
 Compte fiscal en ligne pour les professionnels (mode EFI) 
 Attention 
 Lorsque l'exercice comptable de l'entreprise ne coïncide pas avec une année civile (l'exercice n'est pas clos au 31 décembre), alors la déclaration de TVA doit être faite dans les 3 mois qui suivent la clôture de l'exercice comptable .
```

### VAT-Q046

OfficialF23566 TVAreturns/limits/periods; keep contradictory summary conditions explicit; https://entreprendre.service-public.gouv.fr/vosdroits/F23566; actual original read 2026-10-29. Native LF [160, 194]; reader SHA256 `14de3f97623ea9ffe4c3d4828684c75853de22275352fb7888bc75901e7af83a`. Inherited actual C selected reading, exact read-scope records preserved

```text
Clôture au 31 décembre
 L'entreprise doit payer la TVA en plusieurs fois :
 1 er acompte : en juillet , l'entreprise doit verser 55 % de la taxe due l'année précédente
 2 e acompte : en décembre , l'entreprise doit verser 40 % de la taxe due l'année précédente
 Solde : au moment du dépôt de la déclaration de TVA en mai de l'année suivante
 Si l'entreprise estime que les montants versés lors des acomptes sont égaux ou supérieurs au montant de la taxe due, alors elle peut se dispenser d'un nouveau versement. Elle doit alors remettre au service des impôts des entreprises (SIE) une déclaration datée et signée avant la date de recouvrement du prochain versement.
 Où s’adresser ? 
 Pivot Local
 Quelle est votre ville ou code postal ?
 Exemple : Sainte-Cécile-les-Vignes ou 95200
 Service des impôts des entreprises (SIE)
 L'entreprise peut également demander à ce que le montant de ses acomptes soit modifié si elle estime que la TVA dont elle est redevable est supérieur de plus de 10 % ou inférieur de plus de 10 % par rapport au montant de l'acompte correspondant. Par exemple, lors de son 2 nd acompte, l'entreprise doit verser 10 000 € de TVA, hors d'après ses estimations, elle est redevable de 15 000 € de TVA. Elle peut demander à ce que le montant de ce 2 nd acompte soit modifié pour ne pas avoir un trop gros rattrapage au moment du paiement du solde.
 À savoir 
 L'entreprise qui a versé un montant de TVA inférieur à 1 000 € l'année précédente est dispensée du versement des acomptes de TVA l'année suivante.
Clôture à une autre date que le 31 décembre
 L'entreprise doit payer la TVA en plusieurs fois. La date de versement des acomptes dépend de la date à laquelle l'entreprise a fait sa déclaration de TVA pour l'année précédente .
 Tableau - Date des acomptes en fonction des dates de déclaration de TVA Date déclaration de TVA au titre de l'année précédente
 Dates de versement des acomptes
 Janvier, février, mars, avril ou mai N
 1 er acompte : juillet N
 2 e acompte : décembre N
 Juin, juillet, août, septembre, octobre N
 1 er acompte : décembre N
 2 e acompte : juillet N+1
 Novembre ou décembre N
 1 er acompte : juillet N+1
 2 e acompte : décembre N+1
 L'entreprise doit verser 55 % de la taxe due l'année précédente au moment du 1 er acompte, puis 40 % lors du 2 e acompte. Pour finir, l'entreprise doit verser le solde restant au moment de sa déclaration de TVA .
 Si l'entreprise estime que les montants versés lors des acomptes sont égaux ou supérieurs au montant de la taxe due, alors elle peut se dispenser d'un nouveau versement. Elle doit alors remettre au service des impôts des entreprises une déclaration datée et signée avant la date de recouvrement du prochain versement.
 Où s’adresser ? 
 Pivot Local
 Quelle est votre ville ou code postal ?
 Exemple : Sainte-Cécile-les-Vignes ou 95200
 Service des impôts des entreprises (SIE)
 L'entreprise peut également demander à ce que le montant de ses acomptes soit modifié si elle estime que la TVA dont elle est redevable est supérieur de plus de 10 % ou inférieur de plus de 10 % par rapport au montant de l'acompte correspondant. Par exemple, lors de son 2 nd acompte, l'entreprise doit verser 10 000 € de TVA. Hors, d'après ses estimations, elle est redevable de 15 000 € de TVA. Elle peut alors demander à ce que le montant de ce 2 nd acompte soit modifié pour ne pas avoir un trop gros rattrapage au moment du paiement du solde.
```

### VAT-Q047

OfficialF23566 TVAreturns/limits/periods; keep contradictory summary conditions explicit; https://entreprendre.service-public.gouv.fr/vosdroits/F23566; actual original read 2026-10-29. Native LF [203, 222]; reader SHA256 `14de3f97623ea9ffe4c3d4828684c75853de22275352fb7888bc75901e7af83a`. Inherited actual C selected reading, exact read-scope records preserved

```text
 L'entreprise est soumise au régime réel normal de TVA lorsque son chiffre d'affaires est supérieur à 945 000 € .
 Fourniture de logement (hors location meublée)
 L'entreprise est soumise au régime réel normal de TVA lorsque son chiffre d'affaires est supérieur à 945 000 € .
 Prestation de services
 Une entreprise est soumise au régime réel normal de TVA lorsque son chiffre d'affaires est supérieur à 286 000 € .
 Quand et comment faire sa déclaration de TVA ? 
 L'entreprise soumise à un régime réel normal : titleContent de TVA doit faire une déclaration de TVA tous les mois . La date exacte de dépôt de la déclaration est indiquée dans l'espace professionnel impot.gouv.fr de chaque entreprise.
 À noter 
 Dans le régime réel normal de TVA, la déclaration doit être effectuée entre le 15 et le 24 du mois suivant le fait générateur. Celui-ci correspond par exemple au jour de l’encaissement pour une prestation de services, ou au jour de la remise matérielle pour une livraison de biens).
 La déclaration doit indiquer le montant total des ventes et prestations de services soumises à la TVA qui ont été réalisées dans le mois. Elle doit également préciser le détail des opérations taxables.
 La déclaration de TVA doit être faite en ligne sur l'espace professionnel impots.gouv.fr de l'entreprise :
 Compte fiscal en ligne pour les professionnels (mode EFI) 
 À savoir 
 Lorsque le montant de la TVA exigible chaque année est inférieur à 4 000 € , la déclaration doit être faite tous les 3 mois .
 Quand et comment payer la TVA ? 
 L'entreprise doit verser la TVA dont elle est redevable chaque mois ou chaque trimestre au moment de sa déclaration de TVA .
 Le versement est à effectuer sur le compte professionnel impots.gouv.fr de l'entreprise :
 Compte fiscal en ligne pour les professionnels (mode EFI) 
 À savoir 
 Lorsque le montant de la TVA exigible chaque année est inférieur à 4 000 € , la déclaration et le paiement doivent être fait tous les 3 mois .
```

### VAT-Q048

OfficialF31808 invoiceparticulars/timetable; actual150wording pending exact own-law scope check; https://entreprendre.service-public.gouv.fr/vosdroits/F31808; actual original read 2026-10-29. Native LF [125, 153]; reader SHA256 `426978b90f47de896b077a4bcb7fee3e3a118548b4a40936a35e012f422ff118`. Inherited actual C selected reading, exact read-scope records preserved

```text
 Lorsqu’il a préalablement été établi par l’acheteur
 Numéro individuel d’identification à la TVA : titleContent du vendeur (ainsi que celui du du client professionnel s’il est redevable de la TVA)
 Sauf pour les factures d’un montant total HT : titleContent inférieur ou égal à 150 € 
 Désignation du produit ou de la prestation
 Nature, marque, référence des produits
 Si prestation : matériaux fournis et main d’oeuvre
 Décompte détaillé de chaque prestation et produit fourni
 Quantité, dénomination précise, prix unitaire HT, taux de TVA applicable (ou mention du bénéfice d’exonération de TVA, le cas échéant)
 Somme totale HT : titleContent et TTC : titleContent à payer
 Préciser la majoration éventuelle de prix (frais de transport ou d’emballage par exemple)
 Réduction de prix
 Rabais, ristourne, ou remise acquise à la date de la vente ou de la prestation de service et directement liée à cette opération, à l'exclusion des escomptes non prévus sur la facture
 Date à laquelle le règlement doit intervenir
 Il faut également mentionner les conditions d' escompte : titleContent en cas de paiement anticipé. En cas d'absence d'escompte, mentionner sur la facture « Escompte pour paiement anticipé : néant »
 Taux de pénalités de retard 
 En cas de non-paiement à la date de règlement (les pénalités de retard sont exigibles sans qu’un rappel soit nécessaire)
 Mention de l’indemnité forfaitaire de 40 € 
 Pour frais de recouvrement, en cas de retard de paiement : ne peut être réclamée que par un client professionnel
 Lorsque la facture est adressée à un particulier , elle doit mentionner l’existence et la durée de la garantie légale de conformité d’au moins 2 ans.
 La mention concerne les biens vendus appartenant à l’une des catégories suivantes : appareils électroménagers, équipements informatiques, produits électroniques grand public, appareils de téléphonie, appareils photographiques, appareils dotés d’un moteur électrique ou thermique, destinés au bricolage ou au jardinage, jeux et jouets y compris consoles de jeux vidéos, articles de sport, montres et produits d’horlogerie, articles d’éclairage et luminaires, lunettes de protection solaire et éléments d’ameublement.
 Attention 
 Dans le cadre de la mise en place progressive de la facture électronique à compter du 1 er septembre 2026, de nouvelles mentions obligatoires doivent figurer sur les factures.
 Cette obligation concerne d’abord les grandes entreprises et les ETI : titleContent , puis s’étendra aux PME : titleContent et micro-entreprises à partir du 1 er septembre 2027.
 Les 4 nouvelles mentions obligatoires sont les suivantes :
 Numéro Siren : titleContent du client, lorsqu’il s’agit d’une entreprise
 Adresse de livraison des biens, si elle est différente de l’adresse du client
 Nature des opérations facturées, précisant s’il s’agit de livraisons de biens, de prestations de services, ou une combinaison des deux
 Mention « Option pour le paiement de la taxe d’après les débits » si le prestataire a opté pour le paiement de la taxe d’après les débits : titleContent 
 Généralisation de la facturation électronique Direction de l'information légale et administrative (Dila) - Premier ministre 
```

### VAT-Q049

CurrentBOI-BAREME-00003620260701; CIBS L1624/5 andA1627indexed2026table; https://bofip.impots.gouv.fr/bofip/9368-PGP.html/identifiant=BOI-BAREME-000036-20260701; actual original read 2026-10-29. Native LF [63, 89]; reader SHA256 `30bc31c7ffa5047b9dcd9f10220818af34cec37e3c39310f7be145831f5f2d59`. Inherited actual C selected reading, exact read-scope records preserved

```text
 Le régime simplifié d’imposition de déclaration de taxe sur la valeur ajoutée (TVA), mentionné à l’ article 302 septies A du code général des impôts (CGI) , est devenu le régime simplifié de déclaration (RSD) prévu de l’ article L. 162-1 code des impositions sur les biens et services (CIBS) à l’ article L. 162-9 du CIBS depuis le 1 er janvier 2022.
 Les seuils mentionnés à l’ article L. 162-4 du CIBS et à l’ article L. 162-5 du CIBS figurent à l’ article A. 162-7 du CIBS .
 10
 Les seuils du RSD sont établis comme présentés dans le tableau suivant.
 Seuils du RSD Opérations concernées
 Articles du CIBS (anciens I et II de l’article 302 septies A du CGI)
 Seuils 2023-2025
 Seuils pour l’année 2026 
 Livraisons de biens, ventes à consommer sur place et prestations d’hébergement
 CIBS, art. L. 162-4, 1°
 CIBS, art. L. 162-5, 1°
 840 000 €
 et
 925 000 €
 945 000 €
 et
 1 040 000 €
 Autres prestations de services
 CIBS, art. L. 162-4, 2°
 CIBS, art. L. 162-5, 2°
 254 000 €
 et
 287 000 €
 286 000 €
 et
 323 000 €
 Commentaire renvoyant à ce document : 
```

### VAT-Q050

OfficialBOFiP7October2026 recodification dates/actualLF2026VATsummary; https://bofip.impots.gouv.fr/bofip/15140-PGP.html; actual original read 2026-10-29. Native LF [55, 79]; reader SHA256 `1bdb8dbea8fff2c648bf34edef860f4a553f07b6a4316980d5b1e79700472011`. Inherited actual C selected reading, exact read-scope records preserved

```text
 L’entrée en vigueur du transfert des dispositions législatives recodifiées régissant la TVA au sein du code des impositions sur les biens et services est décalée du 1 er septembre 2026 au 1 er janvier 2027. En cohérence, la date jusqu’à laquelle les anciennes références au code général des impôts peuvent continuer à être utilisées est reportée du 31 décembre 2027 au 30 juin 2028. 
 2/ Par ailleurs, le BOI-RES-TVA-000253 est complété afin de prendre en compte des observations formulées dans le cadre de la consultation publique engagée le 18 février 2026.
 Il est réitéré de manière explicite dans le rescrit le caractère inchangé de la doctrine opposable et la garantie de son opposabilité pour l’interprétation par l’administration des dispositions de la TVA recodifiées au sein du code des impositions sur les biens et services. Cette continuité figure désormais expressément au III de l’ article 46 de l’ordonnance n° 2025-1247 du 17 décembre 2025 modifiée , telle qu’elle a été modifiée par l’ article 17 de l’ordonnance n° 2026-671 du 27 juillet 2026 .
 Par ailleurs, de nouvelles tables de concordance entre les anciennes et les nouvelles dispositions législatives ont été mises en ligne sur www.legifrance.gouv.fr à la rubrique Accueil > Autour de la loi > Codification > Tables de concordance > Code des impositions sur les biens et services . Elles sont complétées des références des jurisprudences de la Cour de justice de l’Union européenne dont les interprétations ont été reprises dans un certain nombre des dispositions du livre II de la partie législative du code des impositions sur les biens et services relatif aux règles de la TVA.
 3/ La présente publication intègre également dans le BOI-ANNX-000514 un glossaire destiné à faciliter la compréhension et l’appropriation par les usagers des expressions utilisées dans le code des impositions sur les biens et services, notamment en les liant aux concepts du code général des impôts qu’elles reprennent.
 4/ À titre informatif, l’ordonnance n° 2026-671 du 27 juillet 2026 apporte également des ajustements au code des impositions sur les biens et services. 
 4.1/ D’une part, pour améliorer la lisibilité et la qualité des dispositions du code des impositions sur les biens et services relatives à la TVA.
 Ainsi, l’ordonnance n° 2026-671 du 27 juillet 2026 procède d’abord au regroupement au sein du titre II du livre II de la partie législative du code des impositions sur les biens et services des dispositions relatives au droit à déduction de la TVA, jusqu’alors disséminées entre plusieurs subdivisions. 
 Cette subdivision relative aux droits à déduction sera par ailleurs complétée par des dispositions réglementaires, lesquelles reprendront les modalités de détermination du coefficient de déduction et des coefficients qui le composent.
 De plus, il est donné satisfaction aux souhaits exprimés de rapprocher certaines formulations de la jurisprudence.
 Enfin, l’ordonnance procède à diverses corrections d’erreurs matérielles décelées dans l’ordonnance n° 2025-1247 du 17 décembre 2025 modifiée, notamment dans le cadre de la consultation publique susmentionnée.
 4.2/ D’autre part, pour intégrer au sein du code des impositions sur les biens et services les dispositions suivantes de la loi n° 2026-103 du 19 février 2026 de finances pour 2026 :
 le renforcement des obligations s’imposant aux opérateurs de détaxe ( loi n° 2026-103 du 19 février 2026 de finances pour 2026, art. 69, II-1° ) ;
 l’uniformisation à 5,5 % du taux de TVA pour les services liés à la gestion des déchets ( loi n° 2026-103 du 19 février 2026 de finances pour 2026, art. 81, II ) ;
 l’application du taux de 5,5 % de TVA aux livraisons de froid par réseau ( loi n° 2026-103 du 19 février 2026 de finances pour 2026, art. 93 ) ;
 l’adjonction d’un critère de qualification professionnelle pour l’éligibilité au taux de 5,5 % de TVA dont relève l’installation de panneaux solaires ( loi n° 2026-103 du 19 février 2026 de finances pour 2026, art. 94 ) ;
 la prorogation du taux de 10 % de TVA pour les travaux forestiers ou de prévention des incendies ( loi n° 2026-103 du 19 février 2026 de finances pour 2026, art. 96 ) ;
 la simplification des taux nuls de TVA sur les transports outre-mer ( loi n° 2026-103 du 19 février 2026 de finances pour 2026, art. 100 ) ;
 l’harmonisation des plafonds de revenus pour l’éligibilité aux taux réduits de TVA propres à la politique sociale du logement ( loi n° 2026-103 du 19 février 2026 de finances pour 2026, art. 95 ) ;
 les dispositions permettant l’application du taux de TVA propre aux logements intermédiaires en cas de mise à disposition pendant les jeux Olympiques et Paralympiques d’hiver des Alpes françaises 2030 ( loi n° 2026-103 du 19 février 2026 de finances pour 2026, art. 97 ) ;
 l’application d’un régime suspensif d’octroi de mer en Guyane et au département de Mayotte ( loi n° 2026-103 du 19 février 2026 de finances pour 2026, art. 99, II ).
 L’ordonnance procède également à des coordinations de références rendues nécessaires par les travaux de recodification opérés par la loi n° 2026-103 du 19 février 2026 de finances pour 2026 en matière de fiscalité des déchets (loi n° 2026-103 du 19 février 2026 de finances pour 2026, art. 81) ainsi que par la recodification du code des douanes.
 En revanche, certaines dispositions de la loi n° 2026-103 du 19 février 2026 de finances pour 2026 relèvent de textes réglementaires ( loi n° 2026-103 du 19 février 2026 de finances pour 2026, art. 92 et loi n° 2026-103 du 19 février 2026 de finances pour 2026, art. 98 ) et ne figurent donc pas dans la partie législative du code des impositions sur les biens et services.
 Actualité liée :
 18/02/2026 : TVA - Consultation publique - Dispositions transitoires liées à l’entrée en vigueur de l’ordonnance codifiant la taxe sur la valeur ajoutée dans le code des impositions sur les biens et services - Rescrit 
```

### VAT-Q051

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [68, 70]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

A1   Ventes, prestations de services                             0979   …………………             E1   Exportations hors UE                                   0032   …………………

```

### VAT-Q052

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [70, 72]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

A2   Autres opérations imposables                                0981   …………………             E2   Autres opérations non imposables                       0033   …………………

```

### VAT-Q053

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [73, 75]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
     Achats de prestations de services réalisés auprès d’un                                      Ventes à distance taxables dans un autre État
A3   assujetti non établi en France                              0044   …………………             E3   membre au profit des personnes non assujetties –       0047   …………………
     (article 283-2 du code général des impôts)                                                  Ventes B to C
```

### VAT-Q054

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [75, 77]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
     (article 283-2 du code général des impôts)                                                  Ventes B to C
A4   Importations (autres que les produits pétroliers)           0056   …………………             E4   Importations (autres que les produits pétroliers)      0052   …………………
     Sorties de régime fiscal suspensif (autres que les
```

### VAT-Q055

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [78, 80]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
     produits pétroliers) et sorties de régime particulier                                       Sorties de régime fiscal suspensif (autres que les
A5                                                               0051   …………………             E5                                                          0053   …………………
     douanier uniquement lorsque des livraisons ont eu lieu                                      produits pétroliers)
```

### VAT-Q056

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [82, 84]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
                                                                                                 Importations placées sous régime fiscal suspensif
B1   Mises à la consommation de produits pétroliers              0048   …………………             E6                                                          0054   …………………
                                                                                                 (autres que les produits pétroliers)
```

### VAT-Q057

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [84, 86]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
                                                                                                 (autres que les produits pétroliers)
B2   Acquisitions intracommunautaires                            0031   …………………             F1   Acquisitions intracommunautaires                       0055   …………………
     Achats d’électricité, de gaz naturel, de chaleur ou de                                      Livraisons intracommunautaires à destination
```

### VAT-Q058

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [86, 88]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
     Achats d’électricité, de gaz naturel, de chaleur ou de                                      Livraisons intracommunautaires à destination
B3                                                               0030   …………………             F2                                                          0034   …………………
     froid imposables en France                                                                  d'une personne assujettie – Ventes B to B
```

### VAT-Q059

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [90, 92]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
                                                                                                 Livraisons d’électricité, de gaz naturel, de chaleur
B4   auprès d’un assujetti non établi en France (article 283-1   0040   …………………             F3                                                          0029   …………………
                                                                                                 ou de froid non imposables en France
```

### VAT-Q060

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [94, 96]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

B5   Régularisations (important : cf. notice)                    0036   …………………             F4   Mises à la consommation de produits pétroliers         0049   …………………

```

### VAT-Q061

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [113, 115]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

08   Taux normal 20 %                                                                                                          0207         …………………            …………………

```

### VAT-Q062

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [115, 117]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

09   Taux réduit 5,5 %                                                                                                         0105         …………………            …………………

```

### VAT-Q063

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [117, 119]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

9B   Taux réduit 10 %                                                                                                          0151         …………………            …………………

```

### VAT-Q064

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [121, 123]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

10   Taux normal 8,5 %                                                                                                         0201         …………………            …………………

```

### VAT-Q065

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [123, 125]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

11   Taux réduit 2,1 %                                                                                                         0100         …………………            …………………

```

### VAT-Q066

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [127, 129]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

T1   Opérations réalisées dans les DOM et imposables au taux de 1,75 %                                                         1120         …………………            …………………

```

### VAT-Q067

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [129, 131]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

T2   Opérations réalisées dans les DOM et imposables au taux de 1,05 %                                                         1110         …………………            …………………

```

### VAT-Q068

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [131, 133]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

TC   Opérations réalisées en Corse et imposables au taux de 13 %                                                               1090         …………………            …………………

```

### VAT-Q069

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [133, 135]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

T3   Opérations réalisées en Corse et imposables au taux de 10 %                                                               1081         …………………            …………………

```

### VAT-Q070

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [135, 137]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

T4   Opérations réalisées en Corse et imposables au taux de 2,1 %                                                              1050         …………………            …………………

```

### VAT-Q071

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [137, 139]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

T5   Opérations réalisées en Corse et imposables au taux de 0,9 %                                                              1040         …………………            …………………

```

### VAT-Q072

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [139, 141]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

T6   Opérations réalisées en France continentale au taux de 2,1 %                                                              1010         …………………            …………………

```

### VAT-Q073

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [147, 149]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

P1   Taux normal 20 %                                                                                                          0208         …………………            …………………

```

### VAT-Q074

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [149, 151]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

P2   Taux réduit 13 %                                                                                                          0152         …………………            …………………

```

### VAT-Q075

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [153, 155]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

I1   Taux normal 20 %                                                                                                          0210         …………………            …………………

```

### VAT-Q076

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [155, 157]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

I2   Taux réduit 10 %                                                                                                          0211         …………………            …………………

```

### VAT-Q077

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [157, 159]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

I3   Taux réduit 8,5 %                                                                                                         0212         …………………            …………………

```

### VAT-Q078

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [159, 161]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

I4   Taux réduit 5,5 %                                                                                                         0213         …………………            …………………

```

### VAT-Q079

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [161, 163]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

I5   Taux réduit 2,1 %                                                                                                         0214         …………………            …………………

```

### VAT-Q080

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [163, 165]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

I6   Taux réduit 1,05 %                                                                                                        0215         …………………            …………………
                                                  (dont TVA sur les produits pétroliers ………………..)
```

### VAT-Q081

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [165, 167]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
                                                  (dont TVA sur les produits pétroliers ………………..)
15   TVA antérieurement déduite à reverser                                                                                                              0600   …………………
                                                  (dont TVA sur les produits importés hors produits pétroliers ………………..)
```

### VAT-Q082

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [168, 170]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
5B   Sommes à ajouter, y compris acompte congés                                                                                                         0602   …………………
                                                                                                 16    Total de la TVA brute due (lignes 08 à 5B)                                 …………………
                                                                                                 17    Dont TVA sur acquisitions intracommunautaires                  0035        …………………
```

### VAT-Q083

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [172, 174]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
      TVA DÉDUCTIBLE
19    Biens constituant des immobilisations                                                                                                                           0703        …………………
20    Autres biens et services                                                                                                                                        0702        …………………
```

### VAT-Q084

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [173, 175]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
19    Biens constituant des immobilisations                                                                                                                           0703        …………………
20    Autres biens et services                                                                                                                                        0702        …………………
21    Autre TVA à déduire                                                                                                                                             0059        …………………
```

### VAT-Q085

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [174, 176]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
20    Autres biens et services                                                                                                                                        0702        …………………
21    Autre TVA à déduire                                                                                                                                             0059        …………………
      (dont régularisation de TVA sur les produits pétroliers :    )
```

### VAT-Q086

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [178, 180]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
      (dont régularisation de TVA collectée sur autres produits ou PS [cf. notice] ou de TVA déductible :       )
22    Report du crédit apparaissant ligne 27 de la précédente déclaration                                                                                             8001        …………………
2C    Sommes à imputer, y compris acompte congés                                                                                                                      0603        …………………
```

### VAT-Q087

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [180, 182]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
2C    Sommes à imputer, y compris acompte congés                                                                                                                      0603        …………………
                                                                                                 23    Total TVA déductible (ligne 19 à 2C)                                       |___________|
      Indiquer le coefficient de taxation unique applicable pour la période
```

### VAT-Q088

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [190, 192]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

25    Crédit de TVA (ligne 23 – ligne 16)                          0705     …………………              TD    TVA due (ligne 16 – ligne 23)                                  8900        …………………

```

### VAT-Q089

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [246, 248]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
      Remboursement de crédit de TVA demandé sur
26                                                                8002      …………………              X5    consommateurs imputé sur la TVA                                8103        …………………
      formulaire n°3519
```

### VAT-Q090

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [253, 255]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
      Crédit de TVA à reporter (ligne 25 – ligne 26) (Cette
27    somme est à reporter ligne 22 de la prochaine               8003      …………………              29    Taxes assimilées calculées sur l’annexe n° 3310 A              9979        …………………
      déclaration)
```

### VAT-Q091

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [250, 252]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
      Crédit de TVA transféré à la société tête de groupe
AA                                                                8005      …………………              28    TVA nette due (ligne TD – ligne X5)                            8901        …………………
      sur la déclaration récapitulative 3310 CA3G
```

### VAT-Q092

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [253, 255]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text
      Crédit de TVA à reporter (ligne 25 – ligne 26) (Cette
27    somme est à reporter ligne 22 de la prochaine               8003      …………………              29    Taxes assimilées calculées sur l’annexe n° 3310 A              9979        …………………
      déclaration)
```

### VAT-Q093

OfficialCA3form3310-CA3-SD2026; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [268, 270]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Inherited actual C selected reading, exact read-scope records preserved

```text

                                                                                                 32    Total à payer (lignes 28 + 29 + Z5 – AB)                       9992        …………………
                                                                                                       (N’oubliez pas d’effectuer le règlement correspondant)
```

### ROOT-VAT-Q001

CGI annexe II article242 noniesA I/II and commencement notes; https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006162005; actual original read 2026-10-29. Native LF [309, 309]; reader SHA256 `92af1d5d1daa6b83509409dff9a85747e41279e355e316773e994e0097e30cf1`. Root actual selected reading, returned source/version/access limits retained

```text
Les factures dont le montant est inférieur ou égal à 150 € hors taxe
```

### ROOT-VAT-Q002

CGI annexe II article242 noniesA I/II and commencement notes; https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006162005; actual original read 2026-10-29. Native LF [309, 309]; reader SHA256 `92af1d5d1daa6b83509409dff9a85747e41279e355e316773e994e0097e30cf1`. Root actual selected reading, returned source/version/access limits retained

```text
peuvent ne pas comporter les mentions énoncées aux 2° et 12° du I du présent article.
```

### ROOT-VAT-Q003

CGI annexe II article242 noniesA I/II and commencement notes; https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006162005; actual original read 2026-10-29. Native LF [300, 300]; reader SHA256 `92af1d5d1daa6b83509409dff9a85747e41279e355e316773e994e0097e30cf1`. Root actual selected reading, returned source/version/access limits retained

```text
13° Lorsque l'acquéreur ou le preneur est redevable de la taxe, la mention : " Autoliquidation " ;
```

### ROOT-VAT-Q004

BOI-TVA-DECLA-30-20-20-20 §§20–60; restaurant/toll conditions; https://bofip.impots.gouv.fr/bofip/142-PGP.html/identifiant=BOI-TVA-DECLA-30-20-20-20-20220119; actual original read 2026-10-29. Native LF [76, 76]; reader SHA256 `88d2e2c2d6ca0ef3cd5608819dd591f44689d15009e155450379a671f996ccf2`. Root actual selected reading, returned source/version/access limits retained

```text
Toutefois, ces mesures d’allégement ne sont pas applicables aux opérations pour lesquelles :
```

### ROOT-VAT-Q005

BOI-TVA-DECLA-20-20-30-10 §§60–130 and old noncalendar examples; retain doctrine/decree distinction; https://bofip.impots.gouv.fr/bofip/2418-PGP.html/identifiant=BOI-TVA-DECLA-20-20-30-10-20230118; actual original read 2026-10-29. Native LF [34, 34]; reader SHA256 `90853c68cc80094c6da084680b67681ea6339607e7ea7d77707e15924116503e`. Root actual selected reading, returned source/version/access limits retained

```text
Cette déclaration récapitule les opérations réalisées depuis le 1^{er} jour de l'exercice au cours duquel le dépassement est intervenu, en y incluant le mois de dépassement. Les acomptes de TVA exigibles au cours de l'exercice, qu'ils aient été antérieurement acquittés ou non, sont déduits sur cette déclaration.
```

### ROOT-VAT-Q006

CIBS D162-8, operative from1January2025; direct official indexed observation; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049803758; actual original read 2026-10-29. Native LF [18, 18]; reader SHA256 `46d257b1c3ad5e073eaf3d779540129715c323e5e88f1894d576eed347baaef3`. Root actual selected reading, returned source/version/access limits retained

```text
2° Au 1er janvier de l'année au cours de laquelle la condition mentionnée à l'article L. 162-5 n'est plus remplie ;
```

### ROOT-VAT-P001

CGI article 1727; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051213330/2026-10-29; actual original read 2026-10-29. Native LF [70, 72]; reader SHA256 `a2d62ccf5e0027530e7fe2a4aba840ff7f33c89ac696aa585bd08028a512d4e1`. Root actual selected reading, returned source/version/access limits retained

```text
III. – Le taux de l'intérêt de retard est de 0,20 % par mois. Il s'applique sur le montant des créances de nature fiscale mises à la charge du contribuable ou dont le versement a été différé.

IV. – 1. L'intérêt de retard est calculé à compter du premier jour du mois suivant celui au cours duquel l'impôt devait être acquitté jusqu'au dernier jour du mois du paiement.
```

### ROOT-VAT-P002

CGI article 1727; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051213330/2026-10-29; actual original read 2026-10-29. Native LF [82, 82]; reader SHA256 `a2d62ccf5e0027530e7fe2a4aba840ff7f33c89ac696aa585bd08028a512d4e1`. Root actual selected reading, returned source/version/access limits retained

```text
3. Lorsqu'il est fait application de l'article 1728, le décompte de l'intérêt de retard est arrêté au dernier jour du mois de la proposition de rectification ou du mois au cours duquel la déclaration ou l'acte a été déposé.
```

### ROOT-VAT-P003

CGI article 1728; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546784/2026-10-29; actual original read 2026-10-29. Native LF [42, 48]; reader SHA256 `fe34f8824d0c4c4991e2ae852ab4fb406337e7fb5441f06aca6028d14b9dabc3`. Root actual selected reading, returned source/version/access limits retained

```text
1. Le défaut de production dans les délais prescrits d'une déclaration ou d'un acte comportant l'indication d'éléments à retenir pour l'assiette ou la liquidation de l'impôt entraîne l'application, sur le montant des droits mis à la charge du contribuable ou résultant de la déclaration ou de l'acte déposé tardivement, d'une majoration de :

a. 10 % en l'absence de mise en demeure ou en cas de dépôt de la déclaration ou de l'acte dans les trente jours suivant la réception d'une mise en demeure d'avoir à le produire dans ce délai ;

b. 40 % lorsque la déclaration ou l'acte n'a pas été déposé dans les trente jours suivant la réception d'une mise en demeure d'avoir à le produire dans ce délai ;

c. 80 % en cas de découverte d'une activité occulte ou, s'agissant de la taxe d'aménagement prévue à l'article 1635 quater A, en cas de construction, d'aménagement ou d'opération de transformation de bâtiments à destination autre que d'habitation en bâtiments à destination d'habitation sans autorisation.
```

### ROOT-VAT-P004

CGI article 1729; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020051904/2026-10-29; actual original read 2026-10-29. Native LF [42, 48]; reader SHA256 `dea35e221ab627c15e187944d1d680b40860be3985a2d1be5c9eeb0db3a79004`. Root actual selected reading, returned source/version/access limits retained

```text
Les inexactitudes ou les omissions relevées dans une déclaration ou un acte comportant l'indication d'éléments à retenir pour l'assiette ou la liquidation de l'impôt ainsi que la restitution d'une créance de nature fiscale dont le versement a été indûment obtenu de l'Etat entraînent l'application d'une majoration de :

a. 40 % en cas de manquement délibéré ;

b. 80 % en cas d'abus de droit au sens de l'article L. 64 du livre des procédures fiscales ; elle est ramenée à 40 % lorsqu'il n'est pas établi que le contribuable a eu l'initiative principale du ou des actes constitutifs de l'abus de droit ou en a été le principal bénéficiaire ;

c. 80 % en cas de manœuvres frauduleuses ou de dissimulation d'une partie du prix stipulé dans un contrat ou en cas d'application de l'article 792 bis.
```

### ROOT-VAT-S001

CGI1737 II/III/IVbis/V; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053293950/2999-01-01; actual original read 2026-10-29. Native LF [40, 40]; reader SHA256 `4f3c9f83fc19e08804ca220283493aefc6f3b56fecf368d8477cc787fea6f6f2`. Root actual selected reading, returned source/version/access limits retained

```text
II. - Toute omission ou inexactitude constatée dans les factures ou documents en tenant lieu mentionnés aux articles 289 et 290 quinquies donne lieu à l'application d'une amende de 15 €. Toutefois, le montant total des amendes dues au titre de chaque facture ou document ne peut excéder le quart du montant qui y est ou aurait dû y être mentionné.
```

### ROOT-VAT-S002

CGI1737 II/III/IVbis/V; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053293950/2999-01-01; actual original read 2026-10-29. Native LF [42, 42]; reader SHA256 `4f3c9f83fc19e08804ca220283493aefc6f3b56fecf368d8477cc787fea6f6f2`. Root actual selected reading, returned source/version/access limits retained

```text
III. - Le non-respect par l'assujetti de l'obligation d'émission d'une facture sous une forme électronique dans les conditions prévues à l'article 289 bis donne lieu à l'application d'une amende de 50 € par facture, sans que le total des amendes appliquées au titre d'une même année civile puisse être supérieur à 15 000 €.
```

### ROOT-VAT-S003

CGI1737 II/III/IVbis/V; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053293950/2999-01-01; actual original read 2026-10-29. Native LF [54, 54]; reader SHA256 `4f3c9f83fc19e08804ca220283493aefc6f3b56fecf368d8477cc787fea6f6f2`. Root actual selected reading, returned source/version/access limits retained

```text
V. - Les amendes mentionnées au 3 du I et aux II, III et IV du présent article ne sont pas applicables en cas de première infraction commise au cours de l'année civile en cours et des trois années précédentes lorsque l'infraction a été réparée spontanément ou dans les trente jours suivant une première demande de l'administration.
```

### ROOT-VAT-S004

CGI1788D I/II/V; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044045593/2026-09-25; actual original read 2026-10-29. Native LF [14, 14]; reader SHA256 `00d4aed908a66116690f4e75306595a93f14a875eac4d60a06ee333dbc0254bc`. Root actual selected reading, returned source/version/access limits retained

```text
I. - Le non-respect par l'assujetti des obligations prévues à l'article 290 donne lieu à l'application d'une amende égale à 500 € par transmission, sans que le total des amendes appliquées au titre d'une même année civile puisse être supérieur à 15 000 €.
```

### ROOT-VAT-S005

CGI1788D I/II/V; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044045593/2026-09-25; actual original read 2026-10-29. Native LF [16, 16]; reader SHA256 `00d4aed908a66116690f4e75306595a93f14a875eac4d60a06ee333dbc0254bc`. Root actual selected reading, returned source/version/access limits retained

```text
II. - Le non-respect par l'assujetti des obligations prévues à l'article 290 A donne lieu à l'application d'une amende égale à 500 € par transmission, sans que le total des amendes appliquées au titre d'une même année civile puisse être supérieur à 15 000 €.
```

### ROOT-VAT-S006

CGI1788D I/II/V; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044045593/2026-09-25; actual original read 2026-10-29. Native LF [22, 22]; reader SHA256 `00d4aed908a66116690f4e75306595a93f14a875eac4d60a06ee333dbc0254bc`. Root actual selected reading, returned source/version/access limits retained

```text
V. - Les amendes mentionnées au présent article ne sont pas applicables en cas de première infraction commise au cours de l'année civile en cours et des trois années précédentes si l'infraction a été réparée spontanément ou dans les trente jours suivant une première demande de l'administration.
```

### ROOT-VAT-S007

CGI1788A1/2/4; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983701/2026-01-01; actual original read 2026-10-29. Native LF [30, 30]; reader SHA256 `d1fc3318caaa912e3a95abd6da0f1b584827d5e6cdb3088a72954c7a10ec4a89`. Root actual selected reading, returned source/version/access limits retained

```text
4. Lorsqu'au titre d'une opération donnée le redevable de la taxe sur la valeur ajoutée est autorisé à la déduire, le défaut de mention de la taxe exigible sur la déclaration prévue au 1 de l'article 287, qui doit être déposée au titre de la période concernée, entraîne l'application d'une amende égale à 5 % de la somme déductible.
```

### ROOT-VAT-S008

CGI1737 II/III/IVbis/V; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053293950/2999-01-01; actual original read 2026-10-29. Native LF [46, 46]; reader SHA256 `4f3c9f83fc19e08804ca220283493aefc6f3b56fecf368d8477cc787fea6f6f2`. Root actual selected reading, returned source/version/access limits retained

```text
IV bis. - Lorsque l'administration constate une omission ou un manquement par l'assujetti à l'obligation de recourir à une plateforme agréée pour la réception de factures électroniques prévue au I de l'article 289 bis du présent code, elle le met en demeure de s'y conformer dans un délai de trois mois.
```

### ROOT-VAT-S009

CGI1737 II/III/IVbis/V; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053293950/2999-01-01; actual original read 2026-10-29. Native LF [48, 48]; reader SHA256 `4f3c9f83fc19e08804ca220283493aefc6f3b56fecf368d8477cc787fea6f6f2`. Root actual selected reading, returned source/version/access limits retained

```text
La persistance de la méconnaissance par l'assujetti de l'obligation mentionnée au premier alinéa du présent IV bis à l'expiration du délai prévu au même premier alinéa donne lieu à l'application d'une amende de 500 €. L'administration met alors à nouveau l'assujetti en demeure de se conformer à cette obligation dans un même délai de trois mois.
```

### ROOT-VAT-S010

CGI1737 II/III/IVbis/V; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053293950/2999-01-01; actual original read 2026-10-29. Native LF [50, 50]; reader SHA256 `4f3c9f83fc19e08804ca220283493aefc6f3b56fecf368d8477cc787fea6f6f2`. Root actual selected reading, returned source/version/access limits retained

```text
La persistance de la méconnaissance de l'obligation mentionnée audit premier alinéa à l'expiration du délai prévu au deuxième alinéa donne lieu à l'application d'une amende de 1 000 €.
```

### ROOT-VAT-S011

CGI1737 II/III/IVbis/V; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053293950/2999-01-01; actual original read 2026-10-29. Native LF [52, 52]; reader SHA256 `4f3c9f83fc19e08804ca220283493aefc6f3b56fecf368d8477cc787fea6f6f2`. Root actual selected reading, returned source/version/access limits retained

```text
Une nouvelle amende de 1 000 € est encourue après chaque période de trois mois au terme de laquelle l'administration, après une mise en demeure infructueuse, constate la persistance de la méconnaissance de l'obligation prévue au premier alinéa.
```

### ROOT-VAT-S012

CGI1788A1/2/4; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983701/2026-01-01; actual original read 2026-10-29. Native LF [14, 14]; reader SHA256 `d1fc3318caaa912e3a95abd6da0f1b584827d5e6cdb3088a72954c7a10ec4a89`. Root actual selected reading, returned source/version/access limits retained

```text
1. Entraîne l'application d'une amende de 750 € :
```

### ROOT-VAT-S013

CGI1788A1/2/4; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983701/2026-01-01; actual original read 2026-10-29. Native LF [18, 18]; reader SHA256 `d1fc3318caaa912e3a95abd6da0f1b584827d5e6cdb3088a72954c7a10ec4a89`. Root actual selected reading, returned source/version/access limits retained

```text
L'amende est portée à 1 500 € à défaut de production de la déclaration dans les trente jours d'une mise en demeure ;
```

### ROOT-VAT-S014

CGI1788A1/2/4; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983701/2026-01-01; actual original read 2026-10-29. Native LF [22, 22]; reader SHA256 `d1fc3318caaa912e3a95abd6da0f1b584827d5e6cdb3088a72954c7a10ec4a89`. Root actual selected reading, returned source/version/access limits retained

```text
2. Entraîne l'application d'une amende de 15 € :
```

### ROOT-VAT-S015

CGI1788A1/2/4; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983701/2026-01-01; actual original read 2026-10-29. Native LF [24, 24]; reader SHA256 `d1fc3318caaa912e3a95abd6da0f1b584827d5e6cdb3088a72954c7a10ec4a89`. Root actual selected reading, returned source/version/access limits retained

```text
a. Chaque omission ou inexactitude relevée dans les états prévus à l'article 289 B ; cette amende est plafonnée à 1 500 € ;
```

### ROOT-VAT-S016

CGI1788A1/2/4; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983701/2026-01-01; actual original read 2026-10-29. Native LF [32, 32]; reader SHA256 `d1fc3318caaa912e3a95abd6da0f1b584827d5e6cdb3088a72954c7a10ec4a89`. Root actual selected reading, returned source/version/access limits retained

```text
Toutefois, lorsque l'opération mentionnée au premier alinéa est une livraison à soi-même de biens prévue par l'article 257, le montant de l'amende est multiplié par le rapport entre les coûts ou les dépenses non grevés de taxe sur la valeur ajoutée figurant dans la base d'imposition de la livraison à soi-même telle qu'elle résulte de l'article 266 et la totalité de cette base d'imposition.
```

### ROOT-VAT-R001

CGI278 standardrate; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000026950057/2021-05-01; actual original read 2026-10-29. Native LF [38, 38]; reader SHA256 `0159fa12ca3ecc48f84ebe21bf91a929314916d0274c40e6f13219837b9d96a4`. Root actual selected reading, returned source/version/access limits retained

```text
Le taux normal de la taxe sur la valeur ajoutée est fixé à 20 %.
```

### ROOT-VAT-R002

CGI278-0bis current1March2026; selected food/books/waste and commencement only; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053562844/2026-07-12; actual original read 2026-10-29. Native LF [14, 26]; reader SHA256 `24881ae025369ce1a99efd94093e6f0dc1bf912e97054630b80b9ce904638c48`. Root actual selected reading, returned source/version/access limits retained

```text
La taxe sur la valeur ajoutée est perçue au taux réduit de 5,5 % en ce qui concerne :

A. – Les livraisons portant sur :
1° Les denrées alimentaires destinées à la consommation humaine, les produits normalement destinés à être utilisés dans la préparation de ces denrées et les produits normalement utilisés pour compléter ou remplacer ces denrées, à l'exception des produits suivants auxquels s'applique le taux prévu à 【35†l'article 278】 :

a) Les produits de confiserie ;
b) Les chocolats et tous les produits composés contenant du chocolat ou du cacao. Toutefois le chocolat, le chocolat de ménage au lait, les bonbons de chocolat, les fèves de cacao et le beurre de cacao sont admis au taux réduit de 5,5 % ;

c) Les margarines et graisses végétales ;

d) Le caviar ;

e) Les boissons alcooliques ;
```

### ROOT-VAT-R003

CGI278-0bis current1March2026; selected food/books/waste and commencement only; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053562844/2026-07-12; actual original read 2026-10-29. Native LF [47, 47]; reader SHA256 `24881ae025369ce1a99efd94093e6f0dc1bf912e97054630b80b9ce904638c48`. Root actual selected reading, returned source/version/access limits retained

```text
3° Les livres, y compris leur location. Le présent 3° s'applique aux livres sur tout type de support physique et à ceux qui sont fournis par téléchargement, y compris les livres audio ;
```

### ROOT-VAT-R004

CGI278-0bis current1March2026; selected food/books/waste and commencement only; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053562844/2026-07-12; actual original read 2026-10-29. Native LF [71, 71]; reader SHA256 `24881ae025369ce1a99efd94093e6f0dc1bf912e97054630b80b9ce904638c48`. Root actual selected reading, returned source/version/access limits retained

```text
M. – Les prestations de collecte et de traitement des déchets des ménages et des autres déchets que les collectivités mentionnées à l'article 【54†L. 2224-13】 du code général des collectivités territoriales peuvent, eu égard à leurs caractéristiques et aux quantités produites, collecter et traiter sans sujétions techniques particulières, ainsi que les prestations de services qui concourent au bon déroulement de ces opérations ;
```

### ROOT-VAT-R005

CGI278-0bis current1March2026; selected food/books/waste and commencement only; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053562844/2026-07-12; actual original read 2026-10-29. Native LF [86, 86]; reader SHA256 `24881ae025369ce1a99efd94093e6f0dc1bf912e97054630b80b9ce904638c48`. Root actual selected reading, returned source/version/access limits retained

```text
Conformément au A du XII de l'article 81 de la loi n° 2026-103 du 19 février 2026, ces dispositions, dans leur rédaction résultant de l'article précité, entrent en vigueur le 1^{er} mars 2026.
```

### ROOT-VAT-R006

CGI279 actual1March2026–1January2027 hotels/passenger/TV/restaurant clauses; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053562872; actual original read 2026-10-29. Native LF [8, 17]; reader SHA256 `1fa17273cab17c2c02eacc222de01fba89b62d393c4aff60c28e88badfae8d49`. Root actual selected reading, returned source/version/access limits retained

```text
La taxe sur la valeur ajoutée est perçue au taux réduit de 10 % en ce qui concerne :

a. Les prestations relatives :
A la fourniture d'un hébergement dans le cadre du secteur hôtelier ou de secteurs ayant une fonction similaire et répondant aux conditions fixées au b du 4° de l'article 261 D ;
A la location de logements meublés répondant aux conditions fixées au b bis du même 4° ;

A la fourniture de logements dans les terrains de campings classés et à la location d'emplacement sur les terrains de campings classés ;

A la location d'aires d'accueil ou de terrains de passage des gens du voyage ;
a bis. Les recettes provenant de la fourniture des repas dans les cantines d'entreprises et répondant aux conditions qui sont fixées par décret, à l'exclusion de celles relatives aux boissons alcooliques qui relèvent du taux prévu à l'article 278 ;
```

### ROOT-VAT-R007

CGI279 actual1March2026–1January2027 hotels/passenger/TV/restaurant clauses; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053562872; actual original read 2026-10-29. Native LF [34, 34]; reader SHA256 `1fa17273cab17c2c02eacc222de01fba89b62d393c4aff60c28e88badfae8d49`. Root actual selected reading, returned source/version/access limits retained

```text
b quater. les transports de voyageurs ;
```

### ROOT-VAT-R008

CGI279 actual1March2026–1January2027 hotels/passenger/TV/restaurant clauses; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053562872; actual original read 2026-10-29. Native LF [40, 40]; reader SHA256 `1fa17273cab17c2c02eacc222de01fba89b62d393c4aff60c28e88badfae8d49`. Root actual selected reading, returned source/version/access limits retained

```text
b octies. Les abonnements souscrits par les clients afin de recevoir les services de télévision mentionnés à l'article 2 de la loi n【35†° 86-1067 du 30 septembre 1986】 relative à la liberté de communication.
```

### ROOT-VAT-R009

CGI279 actual1March2026–1January2027 hotels/passenger/TV/restaurant clauses; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053562872; actual original read 2026-10-29. Native LF [59, 59]; reader SHA256 `1fa17273cab17c2c02eacc222de01fba89b62d393c4aff60c28e88badfae8d49`. Root actual selected reading, returned source/version/access limits retained

```text
m. Les ventes à consommer sur place, à l'exclusion de celles relatives aux boissons alcooliques qui relèvent du taux prévu à 【39†l'article 278】 ;
```

### ROOT-VAT-R010

CGI261C1/2 financial and insurance exemptions; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041467574/2026-06-18; actual original read 2026-10-29. Native LF [23, 23]; reader SHA256 `5a8205bb61e2986b8dfe4d3481455a35bd85fd0aea733708b23780cc731d4b98`. Root actual selected reading, returned source/version/access limits retained

```text
c. Les opérations, y compris la négociation, concernant les dépôts de fonds, comptes courants, paiements, virements, créances, chèques et autres effets de commerce, à l'exception du recouvrement de créances ;
```

### ROOT-VAT-R011

CGI261C1/2 financial and insurance exemptions; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041467574/2026-06-18; actual original read 2026-10-29. Native LF [33, 33]; reader SHA256 `5a8205bb61e2986b8dfe4d3481455a35bd85fd0aea733708b23780cc731d4b98`. Root actual selected reading, returned source/version/access limits retained

```text
2° Les opérations d'assurance et de réassurance ainsi que les prestations de services afférentes à ces opérations effectuées par les courtiers et intermédiaires d'assurances ;
```

### ROOT-VAT-R012

CGI260B optionaltaxation operation selection; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983610/2026-03-21; actual original read 2026-10-29. Native LF [41, 41]; reader SHA256 `7afd14f3fcc4d3c32146862d3afb53876325aedf042bd7ac2f96c0489645658e`. Root actual selected reading, returned source/version/access limits retained

```text
Les opérations qui se rattachent aux activités bancaires, financières et, d'une manière générale, au commerce des valeurs et de l'argent, telles que ces activités sont définies par décret, peuvent, lorsqu'elles sont exonérées de taxe sur la valeur ajoutée, être soumises sur option à cette taxe.
```

### ROOT-VAT-R013

CGI260B optionaltaxation operation selection; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983610/2026-03-21; actual original read 2026-10-29. Native LF [43, 43]; reader SHA256 `7afd14f3fcc4d3c32146862d3afb53876325aedf042bd7ac2f96c0489645658e`. Root actual selected reading, returned source/version/access limits retained

```text
L'assujetti qui a exercé l'option l'applique aux seules opérations qu'il détermine. Cette option peut être dénoncée à partir du 1er janvier de la cinquième année qui suit celle au cours de laquelle elle a été exercée.
```

### ROOT-VAT-R014

CGI260C excluded option categories; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020763620/2026-07-23; actual original read 2026-10-29. Native LF [50, 50]; reader SHA256 `1de10006a6fae78ebdb45bb811e73141f636382c6e083fad638a62135f620145`. Root actual selected reading, returned source/version/access limits retained

```text
L'option mentionnée à l'article 260 B ne s'applique pas :
```

### ROOT-VAT-R015

CGI260C excluded option categories; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020763620/2026-07-23; actual original read 2026-10-29. Native LF [60, 60]; reader SHA256 `1de10006a6fae78ebdb45bb811e73141f636382c6e083fad638a62135f620145`. Root actual selected reading, returned source/version/access limits retained

```text
4° Aux intérêts, agios, rémunérations de prêts de titres effectués dans les conditions prévues aux articles L. 211-22 à L. 211-26 du code monétaire et financier, aux profits tirés des pensions réalisées dans les conditions prévues par les articles L. 211-27 à L. 211-34 du même code ;
```

### ROOT-VAT-R016

CGI2614(11) actual universalpostal exemption; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054374042/2026-07-01; actual original read 2026-10-29. Native LF [19, 19]; reader SHA256 `d37b850d91e1a1420565f8c3caac73ce0bdd70a10a5d4dd8e9cb6be7a40571af`. Root actual selected reading, returned source/version/access limits retained

```text
11° Les prestations de services et les livraisons de biens accessoires à ces prestations, à l'exception des transports de personnes et télécommunications, qui relèvent du service universel postal tel que défini par l'article L. 1 du code des postes et communications électroniques, effectuées par le prestataire en France du service universel postal tel que désigné à l'article L. 2 du même code.
```

### ROOT-VAT-R017

BOI-TVA-LIQ-30-10-10§100 ordinary potable-water network supply; https://bofip.impots.gouv.fr/bofip/2033-PGP.html/identifiant=BOI-TVA-LIQ-30-10-10-20251119; actual original read 2026-10-29. Native LF [10, 10]; reader SHA256 `f8de096f8828c9e1cfa1818bcb01d78c5246bd53af9ed0b1cbcf81f7b706d2fb`. Root actual selected reading, returned source/version/access limits retained

```text
L’eau potable fournie par les réseaux de distribution relève du taux réduit de 5,5 %.
```

### ROOT-VAT-R018

CGI281octies actual medication/blood-product2.10conditions; https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006191656; actual original read 2026-10-29. Native LF [29, 29]; reader SHA256 `aa18ad8b5a39d383352a989d905f4115c0d582928d91856a440d1854955ed6bc`. Root actual selected reading, returned source/version/access limits retained

```text
La taxe sur la valeur ajoutée est perçue au taux de 2,10 % pour les livraisons portant sur les préparations magistrales, médicaments officinaux, médicaments ou produits pharmaceutiques définis à l'article L. 5121-8 du code de la santé publique, qui remplissent les conditions de l'article L. 162-17 du code de la sécurité sociale ou qui sont agréés dans les conditions prévues par les articles L. 5123-2 et L. 5123-3 du code de la santé publique ainsi que, lorsqu'ils sont préparés à partir du sang ou de ses composants, les produits sanguins labiles destinés à des fins de recherche sur la personne humaine et les dispositifs médicaux de diagnostic in vitro.
```

### ROOT-VAT-R019

CGI298septies qualifyingpress/digital/territory rates; https://www.legifrance.gouv.fr/affichCode.do?cidTexte=LEGITEXT000006069577&idSectionTA=LEGISCTA000006179663; actual original read 2026-10-29. Native LF [15, 15]; reader SHA256 `ac7d1caa41cb4d858fd0697a520b731ca71fefef505a897c2c94dbfdd3ac1827`. Root actual selected reading, returned source/version/access limits retained

```text
Les livraisons et services d'intermédiation portant sur les publications qui remplissent les conditions prévues par les articles 72 et 73 de l'annexe III au présent code pris en application de l'article 52 de la loi du 28 février 1934, sont soumis à la taxe sur la valeur ajoutée au taux de 2,1 % dans les départements de la France métropolitaine et de 1,05 % dans les départements de la Guadeloupe, de la Martinique et de la Réunion.
```

### ROOT-VAT-R020

CGI298septies qualifyingpress/digital/territory rates; https://www.legifrance.gouv.fr/affichCode.do?cidTexte=LEGITEXT000006069577&idSectionTA=LEGISCTA000006179663; actual original read 2026-10-29. Native LF [17, 17]; reader SHA256 `ac7d1caa41cb4d858fd0697a520b731ca71fefef505a897c2c94dbfdd3ac1827`. Root actual selected reading, returned source/version/access limits retained

```text
Sont également soumis aux mêmes taux de la taxe sur la valeur ajoutée les livraisons et services d'intermédiation portant sur les versions numérisées d'une publication mentionnée au premier alinéa du présent article et sur les services de presse en ligne reconnus comme tels en application de l'article 1er de la loi n° 86-897 du 1er août 1986 portant réforme du régime juridique de la presse.
```

### ROOT-VAT-R021

CGI281quater actual qualifyingfirst-performances andexclusions; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000028416981/2026-07-09; actual original read 2026-10-29. Native LF [18, 18]; reader SHA256 `94070d14ea4068ef550826f33ad96f2e2f0cfb7f4c059149c1a7bc83a08077aa`. Root actual selected reading, returned source/version/access limits retained

```text
La taxe sur la valeur ajoutée est perçue au taux de 2,10 % en ce qui concerne les recettes réalisées aux entrées des premières représentations théâtrales d'oeuvres dramatiques, lyriques, musicales ou chorégraphiques nouvellement créées ou d'oeuvres classiques faisant l'objet d'une nouvelle mise en scène, ainsi que des spectacles de cirque comportant exclusivement des créations originales conçues et produites par l'entreprise et faisant appel aux services réguliers d'un groupe de musiciens.
```

### ROOT-VAT-R022

CGI281quater actual qualifyingfirst-performances andexclusions; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000028416981/2026-07-09; actual original read 2026-10-29. Native LF [20, 20]; reader SHA256 `94070d14ea4068ef550826f33ad96f2e2f0cfb7f4c059149c1a7bc83a08077aa`. Root actual selected reading, returned source/version/access limits retained

```text
Un décret définit la nature des œuvres et fixe le nombre de représentations auxquelles ces dispositions sont applicables.
```

### ROOT-VAT-R023

BOI-TVA-LIQ-40-20§10/20/30 andannexIII89ter140performances; https://bofip.impots.gouv.fr/export/pdf/1963; actual original read 2026-10-29. Native LF [20, 20]; reader SHA256 `5e1f9d462688d5f8738baf82cbbce2164853facf3ae857e36661f1ce8f8cdc05`. Root actual selected reading, returned source/version/access limits retained

```text
Aux termes de l'article 281 quater du CGI et de l'article 89 ter de l'annexe III au CGI, la TVA est perçue au taux particulier en ce qui concerne les recettes réalisées aux entrées des 140 premières représentations :
```

### ROOT-VAT-R024

CGI278-0bisA I/II/III/IIIbis/IV and279-0bis1/2/2bis/3 selected operative conditions; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191654/?anchor=LEGIARTI000053545600; actual original read 2026-10-29. Native LF [1, 7]; reader SHA256 `939c112646d2deaf0d047c9c1b419adf197f06e42d4147f4966ee970441cc856`. Root actual selected reading, returned source/version/access limits retained

```text
I. - Relèvent du taux réduit mentionné au premier alinéa de l'article 278-0 bis les prestations de rénovation énergétique qui répondent aux conditions suivantes :
1° Elles sont effectuées dans des locaux achevés depuis au moins deux ans ;
2° Les locaux mentionnés au 1° du présent I sont affectés ou destinés à être affectés, à l'issue des travaux, à un usage d'habitation ;
3° Ces prestations portent sur la pose, l'installation, l'adaptation ou l'entretien de matériaux, d'équipements, d'appareils ou de systèmes ayant pour objet d'économiser l'énergie ou de recourir à de l'énergie produite à partir de sources renouvelables par l'amélioration :
a) De l'isolation thermique ;
b) Du chauffage et de la ventilation ;
c) De la production d'eau chaude sanitaire.
```

### ROOT-VAT-R025

CGI278-0bisA I/II/III/IIIbis/IV and279-0bis1/2/2bis/3 selected operative conditions; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191654/?anchor=LEGIARTI000053545600; actual original read 2026-10-29. Native LF [8, 16]; reader SHA256 `939c112646d2deaf0d047c9c1b419adf197f06e42d4147f4966ee970441cc856`. Root actual selected reading, returned source/version/access limits retained

```text
II. - Un arrêté conjoint des ministres chargés du budget, du logement et de l'énergie précise la nature et le contenu des prestations mentionnées au 3° du I ainsi que les caractéristiques et les niveaux de performance des matériaux, équipements, appareils et systèmes concernés mentionnés au même 3°.
III. - Par dérogation au I du présent article, le taux prévu à l'article 278 s'applique aux prestations, réalisées sur une période de deux ans au plus :
1° Qui concourent à la production d'un immeuble neuf au sens du 2° du 2 du I de l'article 257 ;
2° A l'issue desquelles la surface de plancher des locaux existants est augmentée de plus de 10 %.
III bis. - Par dérogation au I du présent article, le taux prévu à l'article 278 s'applique aux prestations de rénovation énergétique comprenant la fourniture ou l'installation d'une chaudière susceptible d'utiliser des combustibles fossiles.
IV. - Pour l'application du I du présent article, le preneur de la prestation certifie sur le devis ou la facture que les conditions prévues au même I sont remplies.
Ces documents sont établis en double exemplaire, dont l'un est remis au redevable, qui le conserve à l'appui de sa comptabilité.
Le preneur conserve l'autre exemplaire ainsi que les factures ou notes relatives aux prestations, jusqu'au 31 décembre de la cinquième année qui suit l'émission des factures.
Le preneur est solidairement tenu au paiement du complément de taxe si les mentions portées sur le devis ou la facture s'avèrent inexactes de son fait.
```

### ROOT-VAT-R026

CGI278-0bisA I/II/III/IIIbis/IV and279-0bis1/2/2bis/3 selected operative conditions; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191654/?anchor=LEGIARTI000053545600; actual original read 2026-10-29. Native LF [17, 30]; reader SHA256 `939c112646d2deaf0d047c9c1b419adf197f06e42d4147f4966ee970441cc856`. Root actual selected reading, returned source/version/access limits retained

```text
La taxe sur la valeur ajoutée est perçue au taux réduit de 10 % sur les travaux d'amélioration, de transformation, d'aménagement et d'entretien autres que ceux mentionnés à 【92†l'article 278-0 bis A】 portant sur des locaux à usage d'habitation, achevés depuis plus de deux ans, à l'exception de la part correspondant à la fourniture d'équipements ménagers ou mobiliers ou à l'acquisition de gros équipements fournis dans le cadre de travaux d'installation ou de remplacement du système de chauffage, des ascenseurs, de l'installation sanitaire ou de système de climatisation dont la liste est fixée par arrêté du ministre chargé du budget.
2. Par dérogation au 1, le taux prévu à l'article 278 s'applique aux travaux, réalisés sur une période de deux ans au plus :

a) Qui concourent à la production d'un immeuble neuf au sens du 2° du 2 du I de 【93†l'article 257】 ;

b) A l'issue desquels la surface de plancher des locaux existants est augmentée de plus de 10 %.

2 bis. Par dérogation au 1 du présent article, le taux prévu à l'article 278 s'applique aux travaux suivants :

a) Les travaux de nettoyage ;
b) Les travaux d'aménagement ou d'entretien des espaces verts ;

c) Les travaux comprenant la fourniture ou l'installation d'une chaudière susceptible d'utiliser des combustibles fossiles.
3. Le taux réduit prévu au 1 est applicable aux travaux facturés au propriétaire ou, le cas échéant, au syndicat de copropriétaires, au locataire, à l'occupant des locaux ou à leur représentant à condition que le preneur certifie sur le devis ou la facture que ces travaux se rapportent à des locaux d'habitation achevés depuis plus de deux ans et ne répondent pas aux conditions mentionnées au 2.
```

### ROOT-VAT-R027

BOI-TVA-LIQ-40-10 current27November2024 medicine/bloodconditions; https://bofip.impots.gouv.fr/bofip/1449-PGP.html; actual original read 2026-10-29. Native LF [176, 177]; reader SHA256 `d49f2609c09b2aae8b59d7faeed335f6adcb2a1b4365fc34c95a8614b10bb3c3`. Root actual selected reading, returned source/version/access limits retained

```text
 Aux termes de l’ article 281 octies du CGI , lorsqu’ils sont préparés à partir du sang ou de ses composants, relèvent du taux particulier de 2,10 % de la TVA les produits sanguins labiles destinés à des fins de recherche sur la personne humaine ainsi que les dispositifs médicaux de diagnostic in vitro. 
 Remarque : Ce taux particulier s’applique sous réserve de l’exonération prévue au 2° du 4 de l’ article 261 du CGI ( BOI-TVA-CHAMP-30-10-20-30 ), portant sur le sang total ainsi que ses produits dérivés, lorsqu’ils sont destinés à un usage thérapeutique direct.
```

### ROOT-VAT-W001

Official2026CA3 form identifier A1; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [69, 69]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
A1   Ventes, prestations de services                             0979   …………………             E1   Exportations hors UE                                   0032   …………………
```

### ROOT-VAT-W002

Official2026CA3 form identifier A2; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [71, 71]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
A2   Autres opérations imposables                                0981   …………………             E2   Autres opérations non imposables                       0033   …………………
```

### ROOT-VAT-W003

Official2026CA3 form identifier A3; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [74, 74]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
A3   assujetti non établi en France                              0044   …………………             E3   membre au profit des personnes non assujetties –       0047   …………………
```

### ROOT-VAT-W004

Official2026CA3 form identifier A4; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [76, 76]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
A4   Importations (autres que les produits pétroliers)           0056   …………………             E4   Importations (autres que les produits pétroliers)      0052   …………………
```

### ROOT-VAT-W005

Official2026CA3 form identifier A5; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [79, 79]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
A5                                                               0051   …………………             E5                                                          0053   …………………
```

### ROOT-VAT-W006

Official2026CA3 form identifier B1; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [83, 83]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
B1   Mises à la consommation de produits pétroliers              0048   …………………             E6                                                          0054   …………………
```

### ROOT-VAT-W007

Official2026CA3 form identifier B2; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [85, 85]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
B2   Acquisitions intracommunautaires                            0031   …………………             F1   Acquisitions intracommunautaires                       0055   …………………
```

### ROOT-VAT-W008

Official2026CA3 form identifier B3; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [87, 87]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
B3                                                               0030   …………………             F2                                                          0034   …………………
```

### ROOT-VAT-W009

Official2026CA3 form identifier B4; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [91, 91]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
B4   auprès d’un assujetti non établi en France (article 283-1   0040   …………………             F3                                                          0029   …………………
```

### ROOT-VAT-W010

Official2026CA3 form identifier B5; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [95, 95]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
B5   Régularisations (important : cf. notice)                    0036   …………………             F4   Mises à la consommation de produits pétroliers         0049   …………………
```

### ROOT-VAT-W011

Official2026CA3 form identifier E1; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [69, 69]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
A1   Ventes, prestations de services                             0979   …………………             E1   Exportations hors UE                                   0032   …………………
```

### ROOT-VAT-W012

Official2026CA3 form identifier E2; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [71, 71]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
A2   Autres opérations imposables                                0981   …………………             E2   Autres opérations non imposables                       0033   …………………
```

### ROOT-VAT-W013

Official2026CA3 form identifier E3; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [74, 74]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
A3   assujetti non établi en France                              0044   …………………             E3   membre au profit des personnes non assujetties –       0047   …………………
```

### ROOT-VAT-W014

Official2026CA3 form identifier E4; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [76, 76]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
A4   Importations (autres que les produits pétroliers)           0056   …………………             E4   Importations (autres que les produits pétroliers)      0052   …………………
```

### ROOT-VAT-W015

Official2026CA3 form identifier F1; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [85, 85]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
B2   Acquisitions intracommunautaires                            0031   …………………             F1   Acquisitions intracommunautaires                       0055   …………………
```

### ROOT-VAT-W016

Official2026CA3 form identifier F2; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [87, 87]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
B3                                                               0030   …………………             F2                                                          0034   …………………
```

### ROOT-VAT-W017

Official2026CA3 form identifier F6; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [100, 100]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
                                                                                            F6   Achats en franchise                                    0037   …………………
```

### ROOT-VAT-W018

Official2026CA3 form identifier F8; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [104, 104]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
                                                                                            F8   Régularisations (important : cf. notice)               0039   …………………
```

### ROOT-VAT-W019

Official2026CA3 form identifier 15; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [166, 166]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
15   TVA antérieurement déduite à reverser                                                                                                              0600   …………………
```

### ROOT-VAT-W020

Official2026CA3 form identifier 17; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [170, 170]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
                                                                                                 17    Dont TVA sur acquisitions intracommunautaires                  0035        …………………
```

### ROOT-VAT-W021

Official2026CA3 form identifier 18; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [171, 171]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
                                                                                                 18    Dont TVA sur opérations à destination de Monaco                0038        …………………
```

### ROOT-VAT-W022

Official2026CA3 form identifier 19; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [173, 173]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
19    Biens constituant des immobilisations                                                                                                                           0703        …………………
```

### ROOT-VAT-W023

Official2026CA3 form identifier 20; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [174, 174]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
20    Autres biens et services                                                                                                                                        0702        …………………
```

### ROOT-VAT-W024

Official2026CA3 form identifier 21; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [175, 175]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
21    Autre TVA à déduire                                                                                                                                             0059        …………………
```

### ROOT-VAT-W025

Official2026CA3 form identifier 22; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [179, 179]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
22    Report du crédit apparaissant ligne 27 de la précédente déclaration                                                                                             8001        …………………
```

### ROOT-VAT-W026

Official2026CA3 form identifier 24; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [184, 184]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
      s'il est différent de 100 %                                                                24                                                                   0710        …………………
```

### ROOT-VAT-W027

Official2026CA3 form identifier 2E; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [187, 187]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
                                                                                                 2E    Dont TVA déductible sur les produits pétroliers                 0711       …………………
```

### ROOT-VAT-W028

Official2026CA3 form identifier 25; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [191, 191]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
25    Crédit de TVA (ligne 23 – ligne 16)                          0705     …………………              TD    TVA due (ligne 16 – ligne 23)                                  8900        …………………
```

### ROOT-VAT-W029

Official2026CA3 form identifier TD; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [191, 191]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
25    Crédit de TVA (ligne 23 – ligne 16)                          0705     …………………              TD    TVA due (ligne 16 – ligne 23)                                  8900        …………………
```

### ROOT-VAT-W030

Official2026CA3 form identifier 26; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [247, 247]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
26                                                                8002      …………………              X5    consommateurs imputé sur la TVA                                8103        …………………
```

### ROOT-VAT-W031

Official2026CA3 form identifier 27; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [254, 254]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
27    somme est à reporter ligne 22 de la prochaine               8003      …………………              29    Taxes assimilées calculées sur l’annexe n° 3310 A              9979        …………………
```

### ROOT-VAT-W032

Official2026CA3 form identifier 28; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [251, 251]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
AA                                                                8005      …………………              28    TVA nette due (ligne TD – ligne X5)                            8901        …………………
```

### ROOT-VAT-W033

Official2026CA3 form identifier 29; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [254, 254]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
27    somme est à reporter ligne 22 de la prochaine               8003      …………………              29    Taxes assimilées calculées sur l’annexe n° 3310 A              9979        …………………
```

### ROOT-VAT-W034

Official2026CA3 form identifier 32; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf; actual original read 2026-10-29. Native LF [269, 269]; reader SHA256 `3dc14bddaa81f35a73c3d8d6d47c381d3e9f624dcff2f43cee4dd8b106762f78`. Root actual selected reading, returned source/version/access limits retained

```text
                                                                                                 32    Total à payer (lignes 28 + 29 + Z5 – AB)                       9992        …………………
```

### ROOT-VAT-W035

CGI278-0bisF1/F2 liveperformanceconditions; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053562844/2026-07-12; actual original read 2026-10-29. Native LF [58, 59]; reader SHA256 `24881ae025369ce1a99efd94093e6f0dc1bf912e97054630b80b9ce904638c48`. Root actual selected reading, returned source/version/access limits retained

```text
F. – 1° Les spectacles suivants : théâtres, théâtres de chansonniers, cirques, concerts ; spectacles de variétés à l'exception de ceux qui sont donnés dans les établissements où il est d'usage de consommer pendant les séances. Cette exception n'est pas applicable aux établissements affiliés au Centre national de la musique ;
2° Le prix du billet d'entrée donnant accès à des interprétations originales d'œuvres musicales nécessitant la présence physique d'au moins un artiste du spectacle percevant une rémunération dans des établissements où il est servi facultativement des consommations pendant le spectacle et dont l'exploitant est titulaire de la licence de la catégorie mentionnée au 1° de 【50†l'article D. 7122-1】 du code du travail ;
```

### ROOT-VAT-C001

CGI289bis actual21February2026/current29October2026 returned body; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053576899; actual original read 2026-10-29. Native LF [133, 134]; reader SHA256 `eb1a576aca07bee3238a20cd0cbe462f97fd3a0499e4fde024a874fc09a189f4`. Root actual selected reading, returned source/version/access limits retained

```text
- Pour l'application de l'article 289 et par dérogation au VI du même article 289, l'émission, la transmission et la réception des factures relatives aux opérations mentionnées aux a et d du 1 du I dudit article 289 ainsi qu'aux acomptes s'y rapportant s'opèrent sous une forme électronique, selon des normes de facturation électronique définies par arrêté du ministre chargé du budget, lorsque l'émetteur de la facture et son destinataire sont des assujettis qui sont établis ou ont leur domicile ou leur résidence habituelle en France.
L'émission, la transmission et la réception des factures électroniques s'effectuent en recourant à une plateforme agréée.
```

### ROOT-VAT-C002

DGFiP FAQ Je découvre actual version1September2026 selectedscope/dates; https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq---fe_je-decouvre-la-facturation-electronique.pdf; actual original read 2026-10-29. Native LF [77, 91]; reader SHA256 `4ce0daea1c87e906ce10b6bf244c004a2dc788c37fdc74e81610c070eb247f07`. Root actual selected reading, returned source/version/access limits retained

```text
Seules les opérations imposables au sens de l’article 256 du CGI et qui entrent dans le champ
des articles 258 à 259 D du CGI sont soumises au dispositif de facturation électronique ou de
transmission de données à l’administration. Seules les opérations susmentionnées qui sont
dans le champ d’application de la TVA (livraisons de biens et prestations de services réalisées
à titre onéreux par un assujetti agissant en tant que tel) et qui ne sont pas exonérées en
application des articles 261 à 261 E du CGI relèvent de l’obligation de recours à la facturation
électronique ou de transmission des données à l’administration.
Par conséquent, les opérations hors du champ de la TVA qui ne sont pas imposables au sens
de l’article 256 du CGI, sont exclues de la facturation électronique et du e-reporting.
En revanche, même si un assujetti réalise exclusivement des opérations n’entrant pas dans le
champ du dispositif, il doit être en capacité de recevoir les factures électroniques qui lui
3 Version du 01/09/2026seront adressées par ses fournisseurs assujettis et de choisir une plateforme agréée à cet
effet. Cette obligation court depuis le 1er septembre 2026 (date à laquelle les grandes
entreprises et les entreprises de taille intermédiaire seront tenues d’émettre leurs factures au
format électronique).
```

### ROOT-VAT-C003

DGFiP FAQ Je découvre actual version1September2026 selectedscope/dates; https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq---fe_je-decouvre-la-facturation-electronique.pdf; actual original read 2026-10-29. Native LF [128, 137]; reader SHA256 `4ce0daea1c87e906ce10b6bf244c004a2dc788c37fdc74e81610c070eb247f07`. Root actual selected reading, returned source/version/access limits retained

```text
Depuis le 1er septembre 2026, toutes les entreprises, quelles que soient leur taille et leur
forme juridique, ont l’obligation de recevoir des factures sous format électronique, par
l’intermédiaire d’une plateforme agréée (cf. question 3.1).
Les grandes entreprises (GE) et les entreprises de taille intermédiaire (ETI) doivent également
émettre toutes leurs factures sous format électronique.
Les petites, moyennes et micro-entreprises seront, quant à elles tenues, d’émettre leurs
factures au format électronique au plus tard le 1er septembre 2027.
Pour apprécier le critère de la taille des entreprises (unité légale = SIREN) ainsi que la date à
laquelle il doit être pris en compte, vous pouvez vous référer à la question 1.1 de la foire aux
questions dans la rubrique « j’approfondis mes connaissances sur la réforme ».
```

### ROOT-VAT-C004

DGFiP FAQ Je découvre actual version1September2026 selectedscope/dates; https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq---fe_je-decouvre-la-facturation-electronique.pdf; actual original read 2026-10-29. Native LF [157, 163]; reader SHA256 `4ce0daea1c87e906ce10b6bf244c004a2dc788c37fdc74e81610c070eb247f07`. Root actual selected reading, returned source/version/access limits retained

```text
La mise en place de la transmission des données de transaction (e-reporting) suit celle de la
facturation électronique : depuis le 1er septembre 2026 pour les grandes entreprises et pour
les établissements de taille intermédiaire, et à partir du 1er septembre 2027 pour les micro,
petites et moyennes entreprises.
Pour apprécier le critère de la taille des entreprises (unité légale = SIREN) ainsi que la date à
laquelle il doit être pris en compte, vous pouvez vous référer à la question 1.1 de la foire aux
questions dans la rubrique « j’approfondis mes connaissances sur la réforme ».
```

### ROOT-VAT-C005

DGFiP FAQ J approfondis actual version1September2026 selected size reference/assujetti gates; https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq---fe_japprofondis-la-facturation-electronique.pdf; actual original read 2026-10-29. Native LF [19, 23]; reader SHA256 `98eca5c88b06f6428dfc7d4e7a359c12b5b4aa9a2c0fa6d98f9ddf341db25965`. Root actual selected reading, returned source/version/access limits retained

```text
sont supérieurs au seuil. La notion d’entreprise retenue est celle de l’unité légale, une unité
légale étant identifiée par son numéro SIREN.
La taille de l’entreprise s’apprécie au 1er janvier 2025, sur la base du dernier exercice clos
avant cette date ou, en l’absence d’un tel exercice, sur celle du premier exercice clos à
compter de cette date.
```

### ROOT-VAT-C006

DGFiP FAQ J approfondis actual version1September2026 selected size reference/assujetti gates; https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq---fe_japprofondis-la-facturation-electronique.pdf; actual original read 2026-10-29. Native LF [27, 37]; reader SHA256 `98eca5c88b06f6428dfc7d4e7a359c12b5b4aa9a2c0fa6d98f9ddf341db25965`. Root actual selected reading, returned source/version/access limits retained

```text
Si l’association est à but non lucratif et que sa gestion est désintéressée, que ses activités non
lucratives sont prépondérantes et que ses recettes annuelles lucratives sont inférieures à
81 051 € (pour 2026), alors elle est considérée comme une personne non assujettie à la TVA.
L’association à but non lucratif non assujettie à la TVA n’est pas soumise aux obligations
d’émission, transmission et réception des factures électroniques ni à la transmission des
données de transaction (e-reporting).
Néanmoins, les opérations réalisées à son profit (association = client) entrent dans le champ
du e-reporting de celui qui fournit la prestation ou réalise la vente. L’association n’a aucune
démarche à effectuer.
Si une association est assujettie à la TVA, les opérations réalisées à son profit par une
personne assujettie établie en France entrent dans le champ de la facturation électronique.
```

### ROOT-VAT-C007

CGIannexeIV28-00A actual73TTC perobject/year/beneficiary; https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006179484/; actual original read 2026-10-29. Native LF [14, 14]; reader SHA256 `e2d5d43500f82b04abb52e1ef9af61aa265dba9fba2f37b83199c2f5d8d63f2d`. Root actual selected reading, returned source/version/access limits retained

```text
Les biens de très faible valeur mentionnés au 3° du 2 du IV de l'article 206 de l'annexe II au code général des impôts s'entendent de ceux dont la valeur unitaire n'excède pas 73 € toutes taxes comprises par objet et par an pour un même bénéficiaire.
```

### ROOT-VAT-C008

LFR2022article26III consolidated21February2026 actualcurrentindexedtext; https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000053546715; actual original read 2026-10-29. Native LF [32, 32]; reader SHA256 `608144667ee17ebb3e284abacc70d16c0eb6bdab8bca4d7574bc2ff868c1d84b`. Root actual selected reading, returned source/version/access limits retained

```text
III. - A. - Les 2° et 4° du I et le II s'appliquent aux factures émises à compter du 1er septembre 2026. Un décret peut fixer une date ultérieure, qui ne peut être postérieure au 1er décembre 2026.
```

### ROOT-VAT-C009

LFR2022article26III consolidated21February2026 actualcurrentindexedtext; https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000053546715; actual original read 2026-10-29. Native LF [34, 34]; reader SHA256 `608144667ee17ebb3e284abacc70d16c0eb6bdab8bca4d7574bc2ff868c1d84b`. Root actual selected reading, returned source/version/access limits retained

```text
Toutefois, pour les factures émises par les assujettis relevant des catégories des microentreprises et des petites et moyennes entreprises qui ne sont pas membres d'un assujetti unique mentionné à l'article 256 C du code général des impôts, les 2° et 4° du I et le II du présent article s'appliquent à compter du 1er septembre 2027. Un décret peut fixer une date ultérieure, qui ne peut être postérieure au 1er décembre 2027.
```

### ROOT-VAT-C010

LFR2022article26III consolidated21February2026 actualcurrentindexedtext; https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000053546715; actual original read 2026-10-29. Native LF [36, 36]; reader SHA256 `608144667ee17ebb3e284abacc70d16c0eb6bdab8bca4d7574bc2ff868c1d84b`. Root actual selected reading, returned source/version/access limits retained

```text
Les catégories mentionnées au deuxième alinéa du présent A sont celles mentionnées à l'article 51 de la loi n° 2008-776 du 4 août 2008 de modernisation de l'économie. L'appartenance à une catégorie s'apprécie au niveau de chaque personne juridique au 1er janvier 2025, sur la base du dernier exercice clos avant cette date ou, en l'absence d'un tel exercice, sur celle du premier exercice clos à compter de cette date.
```

### ROOT-VAT-C011

LFR2022article26III consolidated21February2026 actualcurrentindexedtext; https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000053546715; actual original read 2026-10-29. Native LF [38, 38]; reader SHA256 `608144667ee17ebb3e284abacc70d16c0eb6bdab8bca4d7574bc2ff868c1d84b`. Root actual selected reading, returned source/version/access limits retained

```text
B. - A l'exception de l'article 290 B du code général des impôts, les 3° et 5° du I du présent article s'appliquent aux factures émises ou, à défaut, aux opérations réalisées à compter du 1er septembre 2026. Un décret peut fixer une date ultérieure, qui ne peut être postérieure au 1er décembre 2026.
```

### ROOT-VAT-C012

LFR2022article26III consolidated21February2026 actualcurrentindexedtext; https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000053546715; actual original read 2026-10-29. Native LF [40, 40]; reader SHA256 `608144667ee17ebb3e284abacc70d16c0eb6bdab8bca4d7574bc2ff868c1d84b`. Root actual selected reading, returned source/version/access limits retained

```text
Toutefois, les mêmes 3° et 5° ne s'appliquent qu'à compter du 1er septembre 2027 aux factures émises par les entreprises mentionnées au deuxième alinéa du A du présent III ou, à défaut, aux opérations réalisées par ces mêmes entreprises. Un décret peut fixer une date ultérieure, qui ne peut être postérieure au 1er décembre 2027.
```

### ROOT-VAT-C013

CGI261D ordinary rental exemption andactual exceptions; https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000048827285/2026-03-04; actual original read 2026-10-29. Native LF [25, 25]; reader SHA256 `65ec6a913c9313bd0f97320839e38773bc24434004b2f5446501446e975e4b34`. Root actual selected reading, returned source/version/access limits retained

```text
2° Les locations de terrains non aménagés et de locaux nus, à l'exception des emplacements pour le stationnement des véhicules ; toutefois, ces dispositions ne sont pas applicables lorsque les locations constituent pour le bailleur un moyen de poursuivre, sous une autre forme, l'exploitation d'un actif commercial ou d'accroître ses débouchés ou lorsque le bailleur participe aux résultats de l'entreprise locataire ;
```

### ROOT-VAT-C014

CGI261D ordinary rental exemption andactual exceptions; https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000048827285/2026-03-04; actual original read 2026-10-29. Native LF [29, 29]; reader SHA256 `65ec6a913c9313bd0f97320839e38773bc24434004b2f5446501446e975e4b34`. Root actual selected reading, returned source/version/access limits retained

```text
4° Les locations occasionnelles, permanentes ou saisonnières de logements meublés ou garnis à usage d'habitation.
```

### ROOT-VAT-C015

CGI261D ordinary rental exemption andactual exceptions; https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000048827285/2026-03-04; actual original read 2026-10-29. Native LF [40, 40]; reader SHA256 `65ec6a913c9313bd0f97320839e38773bc24434004b2f5446501446e975e4b34`. Root actual selected reading, returned source/version/access limits retained

```text
b bis. Aux locations de logements meublés à usage résidentiel dans le cadre de secteurs autres que ceux mentionnés au b qui sont assorties d'au moins trois des prestations suivantes : le petit déjeuner, le nettoyage régulier des locaux, la fourniture de linge de maison et la réception, même non personnalisée, de la clientèle ;
```

### ROOT-VAT-C016

CGI2602 actualbare-premises option andhousing/agricultural exclusions; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162559/2024-07-15; actual original read 2026-10-29. Native LF [19, 19]; reader SHA256 `cdae49b3d6006605d7425b2b2aecb205515f77be164d6ae001b692358cfc8dd5`. Root actual selected reading, returned source/version/access limits retained

```text
2° Les personnes qui donnent en location des locaux nus pour les besoins de l'activité d'un preneur assujetti à la taxe sur la valeur ajoutée ou, si le bail est conclu à compter du 1er janvier 1991, pour les besoins de l'activité d'un preneur non assujetti.
```

### ROOT-VAT-C017

CGI2602 actualbare-premises option andhousing/agricultural exclusions; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162559/2024-07-15; actual original read 2026-10-29. Native LF [23, 23]; reader SHA256 `cdae49b3d6006605d7425b2b2aecb205515f77be164d6ae001b692358cfc8dd5`. Root actual selected reading, returned source/version/access limits retained

```text
a. Si les locaux nus donnés en location sont destinés à l'habitation ou à un usage agricole ;
```

### ROOT-VAT-C018

Official2026CA12/CA12Enotice3517-S-NOT-SD selected deduction/instalment/refund clauses; https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5424.pdf; actual original read 2026-10-29. Native LF [35, 37]; reader SHA256 `ee12f3f7527b3944b5959730cef1207bcf8558d8f10312d53083b4b48fca8680`. Root actual selected reading, returned source/version/access limits retained

```text
✔ Ligne 24 :
Indiquez le crédit dont vous disposiez au début de l’exercice et qui n’a pas fait l’objet d’une demande de remboursement (report de la ligne 51 de la
précédente CA12/CA12E) ou d’une imputation sur acomptes. Les sommes imputées sur les acomptes sont indiquées ligne AE.
```

### ROOT-VAT-C019

Official2026CA12/CA12Enotice3517-S-NOT-SD selected deduction/instalment/refund clauses; https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5424.pdf; actual original read 2026-10-29. Native LF [64, 65]; reader SHA256 `ee12f3f7527b3944b5959730cef1207bcf8558d8f10312d53083b4b48fca8680`. Root actual selected reading, returned source/version/access limits retained

```text
✔ Ligne AE :
Indiquez le montant du crédit que vous avez imputé sur un ou des acomptes de l’exercice, ainsi que les excédents de déclaration constatés par vousmêmes.
```

### ROOT-VAT-C020

Official2026CA12/CA12Enotice3517-S-NOT-SD selected deduction/instalment/refund clauses; https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5424.pdf; actual original read 2026-10-29. Native LF [75, 84]; reader SHA256 `ee12f3f7527b3944b5959730cef1207bcf8558d8f10312d53083b4b48fca8680`. Root actual selected reading, returned source/version/access limits retained

```text
Le montant à porter sur cette ligne correspond à la somme des montants à porter aux colonnes 1 et 2 au titre des acomptes de votre exercice de TVA.
– Col. 1 : montant des acomptes effectivement payés quelle que soit la date à laquelle est intervenu ce paiement.
– Col. 2 : montant des acomptes restant à payer à la date du dépôt de la présente déclaration.
Les deux acomptes déductibles sont ceux exigibles au cours de l’exercice concerné par la présente déclaration (reportez les acomptes déduits à la
ligne 58). Ce principe s’applique à toutes les entreprises, quelle que soit leur date de clôture d’exercice.
Attention : si les acomptes attendus étaient inférieurs à :
– 550 euros pour l’acompte de juillet,
– 400 euros pour l’acompte de décembre,
vous devez mentionner uniquement le montant payé, en colonne 1.
En cas de non-paiement ou de paiement partiel, le montant non réglé ne doit pas être porté en colonne 2.
```

### ROOT-VAT-C021

Official2026CA12/CA12Enotice3517-S-NOT-SD selected deduction/instalment/refund clauses; https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5424.pdf; actual original read 2026-10-29. Native LF [152, 164]; reader SHA256 `ee12f3f7527b3944b5959730cef1207bcf8558d8f10312d53083b4b48fca8680`. Root actual selected reading, returned source/version/access limits retained

```text
9/10✔ Ligne 57 :
Les acomptes de TVA dus au cours du prochain exercice sont calculés à partir de la TVA nette exigible (ligne 16 – ligne 22) sous déduction de la TVA
due sur les cessions d’immobilisations (ligne 11) et sur les livraisons à soi-même (ligne 12). Les acomptes dus aux mois de juillet et décembre sont
respectivement égaux à 55 % et 40 % du résultat de cette opération.
Si vous ne demandez pas le remboursement du crédit éventuellement dégagé ligne 49, vous pouvez l’imputer sur votre prochain acompte en reportant
le montant sur la ligne 02 de l’avis d’acompte n° 3514.
CADRE VII : DEMANDE DE REMBOURSEMENT
Si le décompte effectué au cadre III (ligne 35) fait apparaître un solde excédentaire, celui-ci est imputable sur l’acompte suivant le dépôt de la présente
déclaration.
Le solde excédentaire ne peut être reporté ligne 24 de la prochaine déclaration CA 12/CA 12 E que si vous ne l’imputez pas sur cet acompte.
Vous avez également la possibilité de demander le remboursement total ou partiel des excédents de versement (ligne 34) et du crédit dégagé (ligne 29)
s’il est supérieur ou égal à 150 euros.
Si vous désirez bénéficier de ce remboursement, remplissez le cadre VII en reportant les montants figurant aux lignes 29 et 34 page 3.
```

### ROOT-VAT-C022

BOI-TVA-DED-30-30-40 fuel/jetfuel; https://bofip.impots.gouv.fr/bofip/1194-PGP.html; actual original read 2026-10-29. Native LF [98, 110]; reader SHA256 `64020ec2492176fea413bffa44a120586b91e23c5530a9f0e5bec114b317911b`. Root actual selected reading, returned source/version/access limits retained

```text
 Véhicules et engins pris en location sans droit à déduction du preneur
 Autres véhicules et engins
 1 er janvier 2021
 80 %
 80 %
 80 %
 1 er janvier 2022
 80 %
 80 %
 100 %
 2. Gazoles et superéthanol E85
 130
 Le b du 1° du 4 de l' article 298 du CGI prévoit que la TVA afférente aux importations, aux acquisitions intracommunautaires, aux livraisons et services portant sur les gazoles et le superéthanol E85 utilisés comme carburants pour les véhicules et engins exclus du droit à déduction ainsi que pour des véhicules et engins pris en location quand le preneur ne peut déduire la taxe relative à cette location n'est pas déductible dans la limite de 20 % de son montant.
```

### ROOT-VAT-C023

BOI-TVA-DED-30-30-40 fuel/jetfuel; https://bofip.impots.gouv.fr/bofip/1194-PGP.html; actual original read 2026-10-29. Native LF [68, 71]; reader SHA256 `64020ec2492176fea413bffa44a120586b91e23c5530a9f0e5bec114b317911b`. Root actual selected reading, returned source/version/access limits retained

```text
 À l'exception de ceux qui sont expressément cités au 1° du 4 de l' article 298 du CGI , l'ensemble des produits pétroliers et assimilés ouvre droit à déduction dans les conditions de droit commun.
 Exemple : les gaz de pétrole et autres hydrocarbures gazeux lorsqu'ils sont liquéfiés (butane, propane, éthylène, propylène, butylène, butadiène, gaz naturel etc.) ou le gaz naturel présenté à l'état gazeux. 
 60
 Les produits pétroliers et assimilés utilisés comme combustibles, c'est-à-dire pour produire de l'énergie thermique, ouvrent droit à déduction de la taxe, quelle que soit la nature de ces produits. Il en est de même des produits pétroliers et assimilés utilisés comme carburant pour activer un moteur qui n'a pas pour objet d'assurer la propulsion d'un véhicule ou d'un engin.
```

### ROOT-VAT-C024

BOI-TVA-DED-30-30-40 fuel/jetfuel; https://bofip.impots.gouv.fr/bofip/1194-PGP.html; actual original read 2026-10-29. Native LF [139, 141]; reader SHA256 `64020ec2492176fea413bffa44a120586b91e23c5530a9f0e5bec114b317911b`. Root actual selected reading, returned source/version/access limits retained

```text
 Le c du 1° du 4 de l' article 298 du CGI limite le droit à déduction de la TVA afférente aux achats, importations, acquisitions intracommunautaires, livraisons et services portant sur les gaz de pétrole et autres hydrocarbures présentés à l'état gazeux, autres que le gaz naturel (lorsque ces produits sont liquéfiés et pour le gaz naturel, le droit commun s'applique, I § 50 ) ou portant sur le pétrole lampant.
 210
 Cette limite est fixée à 50 % du montant de la taxe pour les produits utilisés dans des véhicules ou engins exclus du droit à déduction, ou dans des véhicules ou engins pris en location quand le preneur ne peut pas déduire la taxe relative à cette location.
```

### ROOT-VAT-C025

CGI293B/Bbis/Bter/D; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-29; actual original read 2026-10-29. Native LF [160, 160]; reader SHA256 `3fd741301235513b0890054c8d6568425c6a6d5e733a00ce453dba8135cb1814`. Root actual selected reading, returned source/version/access limits retained

```text
I.-L'article 293 B est applicable aux assujettis établis dans un Etat membre de l'Union européenne autre que la France pour leurs livraisons de biens et leurs prestations de services réalisées en France lorsque les conditions suivantes sont cumulativement remplies :
```

### ROOT-VAT-C026

CGI293B/Bbis/Bter/D; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-29; actual original read 2026-10-29. Native LF [162, 162]; reader SHA256 `3fd741301235513b0890054c8d6568425c6a6d5e733a00ce453dba8135cb1814`. Root actual selected reading, returned source/version/access limits retained

```text
1° Leur chiffre d'affaires sur le territoire de l'Union européenne n'excède pas 100 000 € lors de l'année précédente et lors de l'année en cours ;
```

### ROOT-VAT-C027

CGI293B/Bbis/Bter/D; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-29; actual original read 2026-10-29. Native LF [164, 164]; reader SHA256 `3fd741301235513b0890054c8d6568425c6a6d5e733a00ce453dba8135cb1814`. Root actual selected reading, returned source/version/access limits retained

```text
2° L'assujetti a adressé à l'Etat membre dans lequel il est établi une notification préalable ou une mise à jour de celle-ci indiquant qu'il entend faire usage de la franchise en France, selon les formalités prévues par les dispositions transposant, dans cet Etat, les 3 et 4 de l'article 284 de la directive 2006/112/ CE du Conseil du 28 novembre 2006 relative au système commun de taxe sur la valeur ajoutée.
```

### ROOT-VAT-C028

CGI293B/Bbis/Bter/D; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-29; actual original read 2026-10-29. Native LF [213, 213]; reader SHA256 `3fd741301235513b0890054c8d6568425c6a6d5e733a00ce453dba8135cb1814`. Root actual selected reading, returned source/version/access limits retained

```text
B.-L'assujetti communique les informations énoncées au A du présent III dans un délai d'un mois à compter de la fin du trimestre civil.
```

### ROOT-VAT-C029

CGI293B/Bbis/Bter/D; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-29; actual original read 2026-10-29. Native LF [215, 215]; reader SHA256 `3fd741301235513b0890054c8d6568425c6a6d5e733a00ce453dba8135cb1814`. Root actual selected reading, returned source/version/access limits retained

```text
IV.-L'assujetti mentionné au I informe l'administration française, dans un délai de quinze jours ouvrables, lorsque son chiffre d'affaires annuel dans l'Union européenne dépasse le montant mentionné au 1° du I de l'article 293 B bis.
```

### ROOT-VAT-C030

CGI1731 actual retained29Octoberbrowsermain35–55; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033812315/2026-10-29; actual original read 2026-10-29. Native LF [42, 44]; reader SHA256 `4f947bb80ff5c0898a575de179364fd5748ef839913401a9dee1cfe8f1c53210`. Root actual selected reading, returned source/version/access limits retained

```text
1. Donne lieu à l'application d'une majoration de 5 % tout retard dans le paiement des sommes qui doivent être versées aux comptables de l'administration fiscale au titre des impositions autres que celles mentionnées à l'article 1730.

2. La majoration prévue au 1 n'est pas applicable lorsque le dépôt tardif d'une déclaration ou d'un acte comportant l'indication d'éléments à retenir pour l'assiette ou la liquidation de l'impôt est accompagné du paiement de la totalité des droits correspondants.
```

### ROOT-VAT-C031

CGI293B/Bbis/Bter/D; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-29; actual original read 2026-10-29. Native LF [344, 344]; reader SHA256 `3fd741301235513b0890054c8d6568425c6a6d5e733a00ce453dba8135cb1814`. Root actual selected reading, returned source/version/access limits retained

```text
I.-Les assujettis bénéficiant d'une franchise de taxe mentionnée aux articles 293 B ou 293 B bis ou régie par les dispositions transposant, dans un autre Etat membre, la section 2 du chapitre 1 du titre XII de la directive 2006/112/ CE du Conseil du 28 novembre 2006 relative au système commun de taxe sur la valeur ajoutée ne peuvent opérer aucune déduction de la taxe sur la valeur ajoutée sur les biens et les services utilisés pour les besoins de ces opérations.
```

### ROOT-VAT-C032

CGI293B/Bbis/Bter/D; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-29; actual original read 2026-10-29. Native LF [348, 348]; reader SHA256 `3fd741301235513b0890054c8d6568425c6a6d5e733a00ce453dba8135cb1814`. Root actual selected reading, returned source/version/access limits retained

```text
En cas de délivrance d'une facture, d'une note d'honoraires ou de tout autre document en tenant lieu par ces assujettis pour leurs livraisons de biens et leurs prestations de services, la facture, la note d'honoraires ou le document doit comporter la mention correspondant à la base légale de la franchise : “ TVA non applicable, article 293 B du CGI ” ou “ TVA non applicable, article 293 B bis du CGI ” ou une référence à l'article 284 de la directive 2006/112/ CE du Conseil du 28 novembre 2006 précitée.
```

### ROOT-VAT-C033

CGI293B/Bbis/Bter/D; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-29; actual original read 2026-10-29. Native LF [371, 371]; reader SHA256 `3fd741301235513b0890054c8d6568425c6a6d5e733a00ce453dba8135cb1814`. Root actual selected reading, returned source/version/access limits retained

```text
I. - Les assujettis susceptibles de bénéficier de la franchise (1) mentionnée à l'article 293 B peuvent opter pour le paiement de la taxe sur la valeur ajoutée.
```

### ROOT-VAT-C034

OfficialServicePublicF21746 franchise/startup; https://entreprendre.service-public.gouv.fr/vosdroits/F21746; actual original read 2026-10-29. Native LF [97, 97]; reader SHA256 `d9a5db3b04694dd3bd888efed56a5450a3be8a6ef7514c38b57a72ef6c349896`. Root actual selected reading, returned source/version/access limits retained

```text
 La franchise en base de TVA est un régime qui exonère les entreprises de la déclaration et du paiement de la TVA sur les prestations ou ventes qu'elles réalisent. Ce régime fiscal s'applique à toutes les entreprises établies en France ou dans un autre État membre de l'Union européenne dont le chiffre d'affaires (CA) de l'année précédente ne dépasse pas certains seuils.
```

### ROOT-VAT-C035

OfficialServicePublicF21746 franchise/startup; https://entreprendre.service-public.gouv.fr/vosdroits/F21746; actual original read 2026-10-29. Native LF [264, 264]; reader SHA256 `d9a5db3b04694dd3bd888efed56a5450a3be8a6ef7514c38b57a72ef6c349896`. Root actual selected reading, returned source/version/access limits retained

```text
 Lorsque le montant total de ses acquisitions intracommunautaires a dépassé le seuil de 10 000 € HT : titleContent au cours de l'année précédente ou depuis le début de l'année en cours : le vendeur doit établir une facture sans TVA , c'est-à-dire en hors taxe (HT) . L’entreprise établie en France qui a réalisé cette acquisition intracommunautaire doit alors liquider elle-même la TVA en France au taux français .
```

### ROOT-VAT-C036

OfficialServicePublicF21746 franchise/startup; https://entreprendre.service-public.gouv.fr/vosdroits/F21746; actual original read 2026-10-29. Native LF [268, 268]; reader SHA256 `d9a5db3b04694dd3bd888efed56a5450a3be8a6ef7514c38b57a72ef6c349896`. Root actual selected reading, returned source/version/access limits retained

```text
 En revanche, lorsqu'une entreprise établie en France achète des prestations de services , elle doit payer la TVA , peu importe le montant de ces prestations.
```

### ROOT-VAT-D001

OfficialServicePublicF21746 franchise/startup; https://entreprendre.service-public.gouv.fr/vosdroits/F21746; actual original read 2026-10-29. Native LF [108, 108]; reader SHA256 `d9a5db3b04694dd3bd888efed56a5450a3be8a6ef7514c38b57a72ef6c349896`. Root actual selected reading, returned source/version/access limits retained

```text
 La proposition issue de la loi de finances pour 2025 visant à instaurer un seuil unique de franchise en base de TVA de 25 000 € a été abandonnée.
```

### ROOT-VAT-D002

DGFiP DOMrates/exclusions current13October2026; https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom; actual original read 2026-10-29. Native LF [8, 8]; reader SHA256 `4f2c2814b743c6801cd764a9a1b735334e04a4a0747c76b48c72428d970f97e6`. Root actual selected reading, returned source/version/access limits retained

```text
Quatre taux de TVA s’appliquent à La Réunion, la Guadeloupe et la Martinique (BOI-TVA-GEO-20-10). Ces taux sont répartis en trois catégories :
```

### ROOT-VAT-D003

DGFiP DOMrates/exclusions current13October2026; https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom; actual original read 2026-10-29. Native LF [10, 10]; reader SHA256 `4f2c2814b743c6801cd764a9a1b735334e04a4a0747c76b48c72428d970f97e6`. Root actual selected reading, returned source/version/access limits retained

```text
  * le taux normal : 8,5 % ;
```

### ROOT-VAT-D004

DGFiP DOMrates/exclusions current13October2026; https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom; actual original read 2026-10-29. Native LF [12, 12]; reader SHA256 `4f2c2814b743c6801cd764a9a1b735334e04a4a0747c76b48c72428d970f97e6`. Root actual selected reading, returned source/version/access limits retained

```text
  * le taux réduit : 2,1 % pour tous les produits et services relevant en métropole du taux réduit de 5,5 % ou du taux intermédiaire de 10 % ;
```

### ROOT-VAT-D005

DGFiP DOMrates/exclusions current13October2026; https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom; actual original read 2026-10-29. Native LF [16, 16]; reader SHA256 `4f2c2814b743c6801cd764a9a1b735334e04a4a0747c76b48c72428d970f97e6`. Root actual selected reading, returned source/version/access limits retained

```text
    * 1,75 % pour les ventes d'animaux vivants de boucherie et de charcuterie faites à des personnes non assujetties à la TVA jusqu'au 1er janvier 2027, puis uniquement à destination des petits agriculteurs franchisés à compter du 1er janvier 2027,
```

### ROOT-VAT-D006

DGFiP DOMrates/exclusions current13October2026; https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom; actual original read 2026-10-29. Native LF [18, 18]; reader SHA256 `4f2c2814b743c6801cd764a9a1b735334e04a4a0747c76b48c72428d970f97e6`. Root actual selected reading, returned source/version/access limits retained

```text
    * 1,05 % pour les 140 premières représentations de certains spectacles et certaines publications de presse.
```

### ROOT-VAT-D007

DGFiP DOMrates/exclusions current13October2026; https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom; actual original read 2026-10-29. Native LF [22, 22]; reader SHA256 `4f2c2814b743c6801cd764a9a1b735334e04a4a0747c76b48c72428d970f97e6`. Root actual selected reading, returned source/version/access limits retained

```text
À noter : la TVA n’est provisoirement pas applicable dans les départements de la Guyane et de Mayotte (article 294-1 du Code général des impôts (CGI) et article L211-7 du Code des impositions sur les biens et services (CIBS)).
```

### ROOT-VAT-D008

CIBSL1624 historical2020–22base andindexation; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051216656/2026-04-29; actual original read 2026-10-29. Native LF [12, 12]; reader SHA256 `4b2f3c51bfe8d7a97a21ad5442215ef3d9a89f312a923f8764b17d1050369875`. Root actual selected reading, returned source/version/access limits retained

```text
1° 818 000 € pour les activités de vente de biens corporels, de restauration ou de mise à disposition de logement ;
```

### ROOT-VAT-D009

CIBSL1624 historical2020–22base andindexation; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051216656/2026-04-29; actual original read 2026-10-29. Native LF [14, 14]; reader SHA256 `4b2f3c51bfe8d7a97a21ad5442215ef3d9a89f312a923f8764b17d1050369875`. Root actual selected reading, returned source/version/access limits retained

```text
2° 247 000 € pour les autres activités.
```

### ROOT-VAT-D010

CIBSL1624 historical2020–22base andindexation; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051216656/2026-04-29; actual original read 2026-10-29. Native LF [16, 16]; reader SHA256 `4b2f3c51bfe8d7a97a21ad5442215ef3d9a89f312a923f8764b17d1050369875`. Root actual selected reading, returned source/version/access limits retained

```text
Les valeurs mentionnées aux 1° et 2° sont celles applicables aux années 2020, 2021 et 2022. Pour les années suivantes, elles sont indexées sur l'inflation dans les conditions prévues par le chapitre II du titre III, avec une évolution tous les trois ans. Les valeurs révisées sont arrondies au millier d'euros.
```

### ROOT-VAT-D011

CIBSL1624 historical2020–22base andindexation; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051216656/2026-04-29; actual original read 2026-10-29. Native LF [18, 18]; reader SHA256 `4b2f3c51bfe8d7a97a21ad5442215ef3d9a89f312a923f8764b17d1050369875`. Root actual selected reading, returned source/version/access limits retained

```text
Les références aux seuils prévus au présent article s'entendent de références aux seuils prévus aux 1° et 2° après application de l'indexation prévue au quatrième alinéa.
```

### ROOT-VAT-D012

CGI2832quinquies/sexies/septies/octies selectedordinaryRCcategories; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051214570/2026-09-20; actual original read 2026-10-29. Native LF [3, 3]; reader SHA256 `fe6c98c533d8b4e2b4d85058d6278365cc93e472bf030fe1f522ae79a29c366c`. Root actual selected reading, returned source/version/access limits retained

```text
2 quinquies. Pour les livraisons mentionnées au III de l'article 258, la taxe est acquittée par l'acquéreur qui dispose d'un numéro d'identification à la taxe sur la valeur ajoutée en France lorsque son fournisseur est établi hors de France.
```

### ROOT-VAT-D013

CGI2832quinquies/sexies/septies/octies selectedordinaryRCcategories; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051214570/2026-09-20; actual original read 2026-10-29. Native LF [5, 5]; reader SHA256 `fe6c98c533d8b4e2b4d85058d6278365cc93e472bf030fe1f522ae79a29c366c`. Root actual selected reading, returned source/version/access limits retained

```text
Pour les livraisons de gaz naturel ou d'électricité mentionnées au b du même III, ainsi que pour les services définis au 13° de l'article 259 B qui leur sont directement liés, la taxe est acquittée par l'acquéreur qui dispose d'un numéro d'identification à la taxe sur la valeur ajoutée en France, y compris lorsque son fournisseur est établi en France.
```

### ROOT-VAT-D014

CGI2832quinquies/sexies/septies/octies selectedordinaryRCcategories; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051214570/2026-09-20; actual original read 2026-10-29. Native LF [7, 7]; reader SHA256 `fe6c98c533d8b4e2b4d85058d6278365cc93e472bf030fe1f522ae79a29c366c`. Root actual selected reading, returned source/version/access limits retained

```text
2 sexies. Pour les livraisons et les prestations de façon portant sur des déchets neufs d'industrie et des matières de récupération, la taxe est acquittée par le destinataire ou le preneur qui dispose d'un numéro d'identification à la taxe sur la valeur ajoutée en France.
```

### ROOT-VAT-D015

CGI2832quinquies/sexies/septies/octies selectedordinaryRCcategories; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051214570/2026-09-20; actual original read 2026-10-29. Native LF [9, 9]; reader SHA256 `fe6c98c533d8b4e2b4d85058d6278365cc93e472bf030fe1f522ae79a29c366c`. Root actual selected reading, returned source/version/access limits retained

```text
2 septies. Pour les transferts de quotas autorisant les exploitants à émettre des gaz à effet de serre, au sens de l'article 3 de la directive 2003/87/ CE du Parlement européen et du Conseil du 13 octobre 2003 établissant un système d'échange de quotas d'émission de gaz à effet de serre dans la Communauté et modifiant la directive 96/61/ CE du Conseil, et d'autres unités pouvant être utilisées par les opérateurs en vue de se conformer à cette directive, la taxe est acquittée par l'assujetti bénéficiaire du transfert.
```

### ROOT-VAT-D016

CGI2832quinquies/sexies/septies/octies selectedordinaryRCcategories; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051214570/2026-09-20; actual original read 2026-10-29. Native LF [13, 13]; reader SHA256 `fe6c98c533d8b4e2b4d85058d6278365cc93e472bf030fe1f522ae79a29c366c`. Root actual selected reading, returned source/version/access limits retained

```text
2 octies. Pour les services de communications électroniques, à l'exclusion de ceux soumis à la taxe mentionnée à l'article L. 453-1 du code des impositions sur les biens et services, la taxe est acquittée par l'acquéreur qui dispose d'un numéro d'identification à la taxe sur la valeur ajoutée en France.
```

### ROOT-VAT-D017

CGI289AI nonEUrepresentativeopening andmutualassistanceexception; https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000048838515/2026-03-10; actual original read 2026-10-29. Native LF [43, 43]; reader SHA256 `c21a9296a29406193e7f8600f08c9405887253f275c6dab431cce51532b6e194`. Root actual selected reading, returned source/version/access limits retained

```text
I. – Lorsqu'une personne non établie dans l'Union européenne est redevable de la taxe sur la valeur ajoutée ou doit accomplir des obligations déclaratives, elle est tenue de faire accréditer auprès du service des impôts un représentant assujetti établi en France qui s'engage à remplir les formalités incombant à cette personne et, en cas d'opérations imposables, à acquitter la taxe à sa place. A défaut, la taxe sur la valeur ajoutée et, le cas échéant, les pénalités qui s'y rapportent, sont dues par le destinataire de l'opération imposable.
```

### ROOT-VAT-D018

CGI289AI nonEUrepresentativeopening andmutualassistanceexception; https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000048838515/2026-03-10; actual original read 2026-10-29. Native LF [47, 47]; reader SHA256 `c21a9296a29406193e7f8600f08c9405887253f275c6dab431cce51532b6e194`. Root actual selected reading, returned source/version/access limits retained

```text
1° Aux personnes établies dans un Etat non membre de l'Union européenne avec lequel la France dispose d'un instrument juridique relatif à l'assistance mutuelle ayant une portée similaire à celle prévue par la directive 2010/24/UE du Conseil du 16 mars 2010 concernant l'assistance mutuelle en matière de recouvrement des créances relatives aux taxes, impôts, droits et autres mesures et par le règlement (UE) n° 904/2010 du Conseil du 7 octobre 2010 concernant la coopération administrative et la lutte contre la fraude dans le domaine de la taxe sur la valeur ajoutée. La liste de ces Etats est fixée par arrêté du ministre chargé du budget ;
```

### ROOT-VAT-D019

BOFiPactualite17June2026; CGI273septiesE; LF2026article91; https://bofip.impots.gouv.fr/bofip/15011-PGP.html; actual original read 2026-10-29. Native LF [51, 51]; reader SHA256 `14445da1562fdc5b31abacf31e35c4e8e0a1086bbd6550c70d86f6507c15f97f`. Root actual selected reading, returned source/version/access limits retained

```text
 L’ article 91 de la loi n° 2026-103 du 19 février 2026 de finances pour 2026 met fin à l’exclusion du droit à déduction de la taxe sur la valeur ajoutée (TVA) ayant grevé les biens et services utilisés pour des publicités en faveur des boissons alcooliques visées par les dispositions de l’ article L. 3323-2 du code de la santé publique (CSP) , de l’ article L. 3323-4 du CSP et de l’ article L. 3323-5 du CSP ( code général des impôts [CGI], ann. II, art. 206, IV-2-4° ).
```

### ROOT-VAT-D020

BOFiPactualite17June2026; CGI273septiesE; LF2026article91; https://bofip.impots.gouv.fr/bofip/15011-PGP.html; actual original read 2026-10-29. Native LF [52, 52]; reader SHA256 `14445da1562fdc5b31abacf31e35c4e8e0a1086bbd6550c70d86f6507c15f97f`. Root actual selected reading, returned source/version/access limits retained

```text
 À compter du 21 février 2026, aux termes de l’ article 273 septies E du CGI , issu de l’article 91 de la loi n° 2026-103 du 19 février 2026 de finances pour 2026, la TVA acquittée au titre de biens et de services utilisés pour des publicités, y compris celles en faveur des boissons alcooliques, est déductible dans les conditions de droit commun sans restriction, sous réserve que ces biens et services soient affectés à des opérations de l’assujetti qui ouvrent droit à déduction.
```

## Old topics carried

Every historical origin and wording is preserved. Destinations refer to this successor. R101 adds operative components within all three checked generic route groups; it does not delete the prior destinations.

| Origin / old native LF | Old topic | Current destination | Disposition / reason |
|---|---|---|---|
| current_main62b7639a / 31 | This skill covers French VAT for 2026: who is in and who is out, the rates, the two filing regimes and their limits, how to fill the CA3 and the CA12, self-assessment on cross-border purchases, the EU statements, the e-invoicing timetable, the deduction restrictions, and penalties and interest. Every figure was read on an official French page on 24 October 2026, unless the Sources table says otherwise. Load `vat-workflow-base` for the workflow architecture and `eu-vat-directive` for the EU directive content alongside it. | Current # France: VAT and the VAT return (TVA, CA3 and CA12), nativeLF31–31 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 33 | Two facts about the law itself in 2026: | Current # France: VAT and the VAT return (TVA, CA3 and CA12), nativeLF33–33 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 35 | - **The VAT articles are still in the Code général des impôts (CGI) for all of 2026.** Ordonnance n° 2025-1247 of 17 December 2025 moves them into book II of the Code des impositions sur les biens et services (CIBS). Ordonnance n° 2026-671 of 27 July 2026 put that move back from 1 September 2026 to 1 January 2027, and the old CGI references can still be used until 30 June 2028 (BOFiP, actualité of 7 October 2026). This skill cites the CGI article in force in 2026. | Current # France: VAT and the VAT return (TVA, CA3 and CA12), nativeLF35–35 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 36 | - **The 2026 finance law is loi n° 2026-103 of 19 February 2026.** For VAT it changed rate rules at the edges (waste services and cold networks to 5.5%, forestry work kept at 10%, among others), ended the exclusion of deduction for alcohol advertising from 21 February 2026, and amended the e-invoicing and e-reporting fines (CGI art. 1737 and 1788 D). It did not touch the franchise thresholds or the 20%, 10%, 5.5% and 2.1% rates. | Current # France: VAT and the VAT return (TVA, CA3 and CA12), nativeLF36–36 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 40 | - **Taxable persons established in France** who supply goods or services in France for consideration. They charge French VAT unless they sit inside the franchise en base or the supply is exempt. | Current ## Who this applies to, nativeLF40–40 | Retained / source-corrected: FR-L45: actualsupply/placeandsupplier-versusrecipientliability qualification. |
| current_main62b7639a / 41 | - **The franchise en base (CGI art. 293 B).** A business established in France does not charge VAT, and does not deduct it, while its French turnover stays at or below the thresholds in the rates table. It files no CA3 and no CA12. Its invoices carry the words "TVA non applicable, art. 293 B du code général des impôts". It may opt to charge VAT. | Current ## Who this applies to, nativeLF41–41 | Retained / source-corrected: FR-L45: ordinaryfranchisedsupplies/noinput with293E/F; foreignpurchaseliability notcancelled. |
| current_main62b7639a / 42 | - **The single EUR 25,000 threshold never applied.** The 2025 finance law (loi n° 2025-127, art. 32) set one threshold of EUR 25,000 from 1 March 2025. Loi n° 2025-1044 of 3 November 2025, art. 1, restored the separate thresholds with effect from 1 March 2025 itself. So for 2025 and 2026 the thresholds are the ones in the table below. Any page or skill that prints EUR 25,000 as the French franchise threshold is wrong. | Current ## Who this applies to, nativeLF42–42 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 43 | - **Businesses established in another EU state** may use the French franchise if their EU-wide turnover is at or below EUR 100,000 in the previous and the current year and they have notified their own state (CGI art. 293 B bis). A French business that wants to use another state's franchise notifies the French administration and reports quarterly (CGI art. 293 B ter). | Current ## Who this applies to, nativeLF43–43 | Retained / source-corrected: FR-L45: cumulativeFrench293BconditionsaswellEUcapandnotification. |
| current_main62b7639a / 44 | - **Régime réel normal.** Monthly CA3, or quarterly where the VAT due each year is below EUR 4,000 (CGI art. 287-2). | Current ## Who this applies to, nativeLF44–44 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 45 | - **Régime simplifié (régime simplifié de déclaration).** One annual CA12 plus two instalments (CGI art. 287-3), for businesses inside the turnover band in the table and with VAT due of EUR 15,000 or less for the previous year (CIBS art. L. 162-4, L. 162-5, L. 162-7). | Current ## Who this applies to, nativeLF45–45 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 46 | - **Out of this skill:** the overseas departments (their own rates, listed for recognition only; VAT is provisionally not applicable in Guyane and Mayotte), Corsica's special rates beyond the CA3 lines, the margin scheme, property VAT (TVA immobilière), VAT groups (CGI art. 256 C), and non-residents registering through a fiscal representative. Refuse or refer these (see Ask the client first). | Current ## Who this applies to, nativeLF46–46 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 52 | &#124; Standard rate (CGI art. 278) &#124; 20% &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191854/2026-10-24 &#124; | Current ## Rates, bands and thresholds, nativeLF52–52 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 53 | &#124; Intermediate reduced rate (CGI art. 279): hotels, restaurant meals, passenger transport, most work on dwellings over two years old &#124; 10% &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191654/2026-10-24 &#124; | Current ## Rates, bands and thresholds, nativeLF53–53 | Retained / source-corrected: FR-L42: rate conditions corrected; ordinary housing art279-0bis distinguished. |
| current_main62b7639a / 54 | &#124; Reduced rate (CGI art. 278-0 bis): most food, books, energy-efficiency work on dwellings, water; waste services from 1 March 2026 (LF 2026 art. 81) &#124; 5.5% &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191654/2026-10-24 &#124; | Current ## Rates, bands and thresholds, nativeLF54–54 | Retained / source-corrected: FR-L42: food/books/water/municipal waste and energy art278-0bisA conditions supplied. |
| current_main62b7639a / 55 | &#124; Particular rate: reimbursable medicines (CGI art. 281 octies), first performances (art. 281 quater), press (art. 298 septies) &#124; 2.1% &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191656/2026-10-24 &#124; | Current ## Rates, bands and thresholds, nativeLF55–55 | Retained / source-corrected: FR-L42: actual medicine/press/performance qualifications; blood topic restored with exemption distinction. |
| current_main62b7639a / 56 | &#124; Overseas departments (Guadeloupe, Martinique, Réunion): standard / reduced / particular &#124; 8.5% / 2.1% / 1.75% and 1.05% &#124; 2026 &#124; https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom &#124; | Current ## Rates, bands and thresholds, nativeLF56–56 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 57 | &#124; Corsica, CA3 lines TC, T3, T4, T5 &#124; 13%, 10%, 2.1%, 0.9% &#124; 2026 &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf &#124; | Current ## Rates, bands and thresholds, nativeLF57–57 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 58 | &#124; Franchise: total turnover, previous calendar year / current year (CGI art. 293 B, I) &#124; EUR 85,000 / EUR 93,500 &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-24 &#124; | Current ## Rates, bands and thresholds, nativeLF58–58 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 59 | &#124; Franchise: services other than on-site catering and accommodation, previous year / current year &#124; EUR 37,500 / EUR 41,250 &#124; 2026 &#124; same &#124; | Current ## Rates, bands and thresholds, nativeLF59–59 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 60 | &#124; Franchise: lawyers', authors' and performers' regulated work, previous / current year (art. 293 B, I bis) &#124; EUR 50,000 / EUR 55,000 &#124; 2026 &#124; same &#124; | Current ## Rates, bands and thresholds, nativeLF60–60 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 61 | &#124; Franchise: their other activities, previous / current year &#124; EUR 35,000 / EUR 38,500 &#124; 2026 &#124; same &#124; | Current ## Rates, bands and thresholds, nativeLF61–61 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 62 | &#124; Franchise for an EU-established business: EU-wide turnover, previous and current year (art. 293 B bis) &#124; EUR 100,000 &#124; 2026 &#124; same &#124; | Current ## Rates, bands and thresholds, nativeLF62–62 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 63 | &#124; Régime simplifié: previous year turnover, goods, on-site catering, accommodation (CIBS L. 162-4, 1°; amount fixed for 2026 by CIBS art. A. 162-7) &#124; EUR 85,000 to EUR 945,000 (below the lower end, the franchise; F23566: "compris entre : 85 000 € et 945 000 €") &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000049803748/2026-10-24 &#124; | Current ## Rates, bands and thresholds, nativeLF63–63 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 64 | &#124; Régime simplifié: current year ceiling, same activities (CIBS L. 162-5, 1°; A. 162-7) &#124; EUR 1,040,000 &#124; 2026 &#124; same &#124; | Current ## Rates, bands and thresholds, nativeLF64–64 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 65 | &#124; Régime simplifié: previous year turnover, other services incl. furnished lets (CIBS L. 162-4, 2°; A. 162-7) &#124; EUR 37,500 to EUR 286,000 (F23566) &#124; 2026 &#124; same &#124; | Current ## Rates, bands and thresholds, nativeLF65–65 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 66 | &#124; Régime simplifié: current year ceiling, other services (CIBS L. 162-5, 2°; A. 162-7) &#124; EUR 323,000 &#124; 2026 &#124; same &#124; | Current ## Rates, bands and thresholds, nativeLF66–66 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 67 | &#124; Régime simplifié: VAT due for the previous year must not exceed (CIBS L. 162-7) &#124; EUR 15,000 &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000044598127/2026-10-24 &#124; | Current ## Rates, bands and thresholds, nativeLF67–67 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 68 | &#124; Régime réel normal: quarterly CA3 where annual VAT due is below (CGI art. 287-2) &#124; EUR 4,000 &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191928/2026-10-24 &#124; | Current ## Rates, bands and thresholds, nativeLF68–68 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 69 | &#124; Régime simplifié instalments: July / December, share of previous year's tax before fixed-asset VAT (CGI art. 287-3) &#124; 55% / 40% &#124; 2026 &#124; same &#124; | Current ## Rates, bands and thresholds, nativeLF69–69 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 70 | &#124; No instalments where previous year's tax (before fixed-asset VAT) is below (CGI art. 287-3) &#124; EUR 1,000 &#124; 2026 &#124; same &#124; | Current ## Rates, bands and thresholds, nativeLF70–70 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 71 | &#124; Instalment change allowed where the real tax differs by at least (CGI art. 287-3) &#124; 10% &#124; 2026 &#124; same &#124; | Current ## Rates, bands and thresholds, nativeLF71–71 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 72 | &#124; First year of a new business: each self-set instalment at least (CGI art. 287-3) &#124; 80% of the half-year's real tax &#124; 2026 &#124; same &#124; | Current ## Rates, bands and thresholds, nativeLF72–72 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 73 | &#124; CA12 credit refundable at year end (frame VII) only where at least &#124; EUR 150 &#124; 2026 &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5291.pdf &#124; | Current ## Rates, bands and thresholds, nativeLF73–73 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 74 | &#124; Distance sales of goods and B2C digital services to other EU states stay French below (CA3 notice, line E3) &#124; EUR 10,000 a year &#124; 2026 &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf &#124; | Current ## Rates, bands and thresholds, nativeLF74–74 | Retained / source-corrected: Actual establishment, dispatch and BOTH-year conditions replace single-year shorthand. |
| current_main62b7639a / 75 | &#124; Intra-EU acquisitions by a business in the franchise: above this the French buyer self-assesses at the French rate and must ask its SIE for an intra-EU VAT number as soon as it knows the limit is crossed &#124; EUR 10,000 &#124; 2026 &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F21746 &#124; | Current ## Rates, bands and thresholds, nativeLF75–75 | Retained / source-corrected: FR-L45: actualpriorORcurrentyear10kacquisitionceiling. |
| current_main62b7639a / 76 | &#124; Invoices with total excluding VAT at or below this need not show the seller's VAT number (that particular only) &#124; EUR 150 &#124; 2026 &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F31808 &#124; | Current ## Rates, bands and thresholds, nativeLF76–76 | Retained / source-corrected: FR-L35: actual II simplification is I2/I12, inclusive150, with exclusions. |
| current_main62b7639a / 77 | &#124; Small equipment taken straight to expense, unit value excluding VAT up to (decides line 19 or line 20) &#124; EUR 500 &#124; 2026 &#124; https://bofip.impots.gouv.fr/bofip/2109-PGP.html &#124; | Current ## Rates, bands and thresholds, nativeLF77–77 | Retained / source-corrected: Actual optional accounting tolerance and equipment conditions; no universal asset threshold. |
| current_main62b7639a / 78 | &#124; Fuel: petrol, diesel and E85 in a vehicle excluded from deduction, or a lease the lessee cannot deduct / in any other vehicle &#124; 80% / 100% deductible &#124; from 2022 &#124; https://bofip.impots.gouv.fr/bofip/1194-PGP.html &#124; | Current ## Rates, bands and thresholds, nativeLF78–78 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 79 | &#124; Fuel: LPG and other gaseous petroleum products in an excluded vehicle &#124; 50% deductible &#124; 2026 &#124; same &#124; | Current ## Rates, bands and thresholds, nativeLF79–79 | Retained / source-corrected: FR-L45: actualgaseousproducts/lampoil50scope; liquefied/naturalgasordinaryrules. |
| current_main62b7639a / 80 | &#124; Late interest (CGI art. 1727, III) &#124; 0.20% a month &#124; 2026 &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006147309/2026-10-24 &#124; | Current ## Rates, bands and thresholds, nativeLF80–80 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 82 | **How the franchise thresholds bite.** The basic threshold is tested on the previous calendar year: crossing it brings VAT from 1 January of the next year. The higher threshold is tested on the current year: crossing it brings VAT from the day of the overrun itself (CGI art. 293 B, II), so invoices issued that day already carry VAT. In a start-up year, the turnover is scaled up to a full year before the test (service-public F21746). | Current ## Rates, bands and thresholds, nativeLF90–90 | Retained / source-corrected: Actual startup annualisation purpose separated from unresolved statutory/administrative conflict. |
| current_main62b7639a / 84 | **Where two official pages disagree.** The impots.gouv.fr page "Les régimes d'imposition à la TVA" (last modified 21 May 2026) still prints EUR 840,000 and EUR 254,000 as the régime simplifié limits. Those are the 2023-2025 values. The law settles it: CIBS art. L. 162-4 sets base amounts of EUR 818,000 and EUR 247,000 for 2020 to 2022 and indexes them on inflation every three years, rounded to the nearest thousand euros, and CIBS art. A. 162-7, as amended by the arrêté of 27 January 2026 (in force from 29 January 2026), fixes the 2026 amounts at EUR 945,000 / 1,040,000 and EUR 286,000 / 323,000. The BOFiP barème of 1 July 2026 and service-public F23566 give the same figures. Use the 2026 values. | Current ## Rates, bands and thresholds, nativeLF94–94 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 88 | **What goes on the CA3 (form 3310-CA3-SD, 2026).** Read the line codes off the 2026 form only. | Current ## The taxable base, nativeLF98–98 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 90 | &#124; CA3 line &#124; What goes on it &#124; | Current ## The taxable base, nativeLF100–100 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 92 | &#124; A1 &#124; Taxable sales and services, net &#124; | Current ## The taxable base, nativeLF102–102 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 93 | &#124; A2 &#124; Other taxable operations: disposals of fixed assets, self-supplies, and purchases where the buyer is liable, including construction work received from a subcontractor (CGI art. 283-2 nonies) &#124; | Current ## The taxable base, nativeLF103–103 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 94 | &#124; A3 &#124; Services bought from a supplier not established in France (CGI art. 283-2), EU or non-EU alike &#124; | Current ## The taxable base, nativeLF104–104 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 95 | &#124; A4 &#124; Imports other than petroleum products, net &#124; | Current ## The taxable base, nativeLF105–105 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 96 | &#124; A5 &#124; Exits from a suspensive regime &#124; | Current ## The taxable base, nativeLF106–106 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 97 | &#124; B1 &#124; Petroleum products released for consumption &#124; | Current ## The taxable base, nativeLF107–107 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 98 | &#124; B2 &#124; Intra-EU acquisitions of goods, net &#124; | Current ## The taxable base, nativeLF108–108 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 99 | &#124; B3 &#124; Electricity, gas, heat or cold taxable in France &#124; | Current ## The taxable base, nativeLF109–109 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 100 | &#124; B4 &#124; Goods or services from a taxable person not established in France (CGI art. 283-1) &#124; | Current ## The taxable base, nativeLF110–110 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 101 | &#124; B5 &#124; Corrections on the taxed side, for example credit notes to customers &#124; | Current ## The taxable base, nativeLF111–111 | Retained / source-corrected: Positive correction method and prohibition of duplicate/negative frameA correction supplied. |
| current_main62b7639a / 102 | &#124; E1 &#124; Exports outside the EU &#124; | Current ## The taxable base, nativeLF112–112 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 103 | &#124; E2 &#124; Other non-taxable operations, including services to a customer established abroad and a subcontractor's construction work under art. 283-2 nonies &#124; | Current ## The taxable base, nativeLF113–113 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 104 | &#124; E3 &#124; Distance sales taxable in another EU state &#124; | Current ## The taxable base, nativeLF114–114 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 105 | &#124; E4 &#124; Imports, non-taxed side &#124; | Current ## The taxable base, nativeLF115–115 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 106 | &#124; F1 &#124; Intra-EU acquisitions not taxable in France (never the counterpart of B2) &#124; | Current ## The taxable base, nativeLF116–116 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 107 | &#124; F2 &#124; Zero-rated intra-EU supplies of goods to a taxable customer &#124; | Current ## The taxable base, nativeLF117–117 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 108 | &#124; F6 &#124; Purchases free of tax (achats en franchise) &#124; | Current ## The taxable base, nativeLF118–118 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 109 | &#124; F8 &#124; Corrections on the non-taxed side &#124; | Current ## The taxable base, nativeLF119–119 | Retained / source-corrected: Positive non-taxed correction, not a negative original-field instruction. |
| current_main62b7639a / 110 | &#124; 08 / 09 / 9B &#124; Base and tax, mainland: 20% / 5.5% / 10% &#124; | Current ## The taxable base, nativeLF120–120 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 111 | &#124; 10 / 11 &#124; Base and tax, overseas departments: 8.5% / 2.1% &#124; | Current ## The taxable base, nativeLF121–121 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 112 | &#124; T1 to T6 &#124; Overseas particular rates (1.75%, 1.05%), Corsica (13%, 10%, 2.1%, 0.9%), mainland particular rate 2.1% (T6) &#124; | Current ## The taxable base, nativeLF122–122 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 113 | &#124; P1, P2 &#124; Petroleum products, 20% and 13% &#124; | Current ## The taxable base, nativeLF123–123 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 114 | &#124; I1 to I6 &#124; Import VAT by rate: 20%, 10%, 8.5%, 5.5%, 2.1%, 1.05% &#124; | Current ## The taxable base, nativeLF124–124 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 115 | &#124; 15 &#124; VAT previously deducted to be paid back &#124; | Current ## The taxable base, nativeLF125–125 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 116 | &#124; 16 &#124; Total gross VAT due &#124; | Current ## The taxable base, nativeLF126–126 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 117 | &#124; 17 / 18 &#124; Memo lines: of which on intra-EU acquisitions / of which on operations to Monaco &#124; | Current ## The taxable base, nativeLF127–127 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 118 | &#124; 19 &#124; Deductible VAT on fixed assets &#124; | Current ## The taxable base, nativeLF128–128 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 119 | &#124; 20 &#124; Deductible VAT on other goods and services &#124; | Current ## The taxable base, nativeLF129–129 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 120 | &#124; 21 &#124; Other VAT to deduct &#124; | Current ## The taxable base, nativeLF130–130 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 121 | &#124; 22 &#124; Credit carried from line 27 of the previous return &#124; | Current ## The taxable base, nativeLF131–131 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 122 | &#124; 23 &#124; Total deductible VAT &#124; | Current ## The taxable base, nativeLF132–132 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 123 | &#124; 24 / 2E &#124; Memo: of which on imports / on petroleum products &#124; | Current ## The taxable base, nativeLF133–133 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 124 | &#124; 25 / TD &#124; Credit (line 23 less 16) / VAT due (line 16 less 23) &#124; | Current ## The taxable base, nativeLF134–134 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 125 | &#124; 26 &#124; Refund asked for on form 3519 &#124; | Current ## The taxable base, nativeLF135–135 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 126 | &#124; 27 &#124; Credit carried forward, to line 22 of the next return &#124; | Current ## The taxable base, nativeLF136–136 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 127 | &#124; 28 / 29 / 32 &#124; Net VAT due / assimilated taxes from annex 3310 A / total to pay &#124; | Current ## The taxable base, nativeLF137–137 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 129 | Line 18 is a Monaco memo line, not the line for self-assessed EU services. A credit at line 25 does not excuse paying the assimilated taxes at line 29. | Current ## The taxable base, nativeLF141–141 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 131 | **The CA12 (form 3517-S-SD, 2026)** has its own numbering. Lines 5A, 06, 6C and 07 carry the standard, reduced, intermediate and overseas standard rates; line 19 is total gross VAT; line 20 deductions on invoices, 21 the flat-rate deduction, 22 their total; line 23 VAT on fixed assets; line 24 the credit brought in; line 26 total deductible; line 28 VAT due; line 29 credit; line 30 instalments. Line 57 is next year's instalment base: line 16 less lines 11, 12 and 22, which is before VAT on fixed assets. Below EUR 150 a year-end credit is refundable only on a disposal, death or entry into a VAT group; otherwise carry it to next year (line 51) or set it against the next instalment (line 52). | Current ## The taxable base, nativeLF145–145 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 133 | **Self-assessment (autoliquidation).** | Current ## The taxable base, nativeLF147–147 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 135 | - Services bought from a supplier not established in France, EU or not: base on A3, tax in the rate block (08, 09 or 9B), deduction at line 20 (CGI art. 283-2). Net nil for a fully taxable business. If an EU supplier wrongly charged its own VAT, that VAT is not French input VAT: reclaim it in that state. | Current ## The taxable base, nativeLF149–149 | Retained / source-corrected: FR-L45: actualplace/participatingestablishment/lawfulinvoiceanddeductioncapitalisationconditions. |
| current_main62b7639a / 136 | - Intra-EU acquisitions of goods: base on B2, tax in the rate block and again as a memo at line 17, deduction at line 20 or 19. | Current ## The taxable base, nativeLF150–150 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 137 | - Imports: import VAT is self-assessed on the CA3 (base on A4, tax at I1 to I6, deduction at line 20 or 19 and memo at line 24). The return is pre-filled with customs data: reconcile it with the client's import records. | Current ## The taxable base, nativeLF151–151 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 138 | - Domestic reverse charges: construction subcontracting (art. 283-2 nonies), scrap and waste (283-2 sexies), emission quotas (283-2 septies), electronic communications services (283-2 octies), gas and electricity (283-2 quinquies). Flag these for the reviewer. | Current ## The taxable base, nativeLF152–152 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 140 | **Exempt and zero-rated.** Exports go to E1 with export evidence. Intra-EU supplies of goods go to F2: check the customer's VAT number on VIES before invoicing without VAT, keep transport proof, and file the état récapitulatif. Services to a business customer abroad go to E2. Exempt without credit (CGI art. 261: medical, education, insurance, finance, residential rent): no output VAT and no deduction on the related costs. A mixed business uses the coefficient de déduction (CGI annexe II, art. 206 to 214); refer it to an expert-comptable. | Current ## The taxable base, nativeLF154–154 | Retained / source-corrected: Ordinary service place/recipient and DES conditions added; same export/goods/exempt/mixed-business topics retained. |
| current_main62b7639a / 142 | **Deduction restrictions.** | Current ## The taxable base, nativeLF156–156 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 146 | &#124; Vehicles designed to carry people or for mixed use, their parts and upkeep &#124; Not deductible. The test is how the vehicle was designed, judged at purchase or lease, not how it is used. Leisure quads and cycles, electrically assisted or not, are caught unless specifically fitted for the exclusive carriage of goods (https://bofip.impots.gouv.fr/bofip/1192-PGP.html, § 45) &#124; https://bofip.impots.gouv.fr/bofip/1192-PGP.html &#124; | Current ## The taxable base, nativeLF160–160 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 147 | &#124; Exceptions to the vehicle exclusion &#124; Vehicles bought for resale new; taxis, VTC and public passenger transport used exclusively for it; driving schools; hearses used exclusively by undertakers; vehicle hire businesses; vehicles with more than eight seats besides the driver carrying staff; horse transport vehicles from 2024; ski-domain all-terrain vehicles; aircraft for paid air services; racing sailboats. Each needs exclusive use &#124; same &#124; | Current ## The taxable base, nativeLF161–161 | Retained / source-corrected: Actual category-specific use conditions replace universal exclusive-use presumption. |
| current_main62b7639a / 148 | &#124; Fuel &#124; Shares in the rates table. The limit applies only to products used as fuel to propel vehicles and engines; petrol, diesel and E85 used in tests for manufacturing engines are outside it. Liquefied petroleum gases (butane, propane and similar) and natural gas in gaseous form follow the ordinary rules (https://bofip.impots.gouv.fr/bofip/1194-PGP.html, § 40 and 160). Electric charging is not on the fuel list: ordinary rules apply once the vehicle's own exclusion is settled &#124; https://bofip.impots.gouv.fr/bofip/1194-PGP.html &#124; | Current ## The taxable base, nativeLF162–162 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 149 | &#124; Housing directors or staff free of charge &#124; Not deductible, including buying or renting the premises; apportion by headcount where third parties are housed too &#124; https://bofip.impots.gouv.fr/bofip/1190-PGP.html &#124; | Current ## The taxable base, nativeLF165–165 | Retained / source-corrected: Actual guard/security and mixed-headcount gates supplied. |
| current_main62b7639a / 150 | &#124; Gifts and goods given away &#124; Not deductible, except goods of very low value (amount fixed by CGI annexe IV, art. 28-00 A, measured including all taxes, per object and per year for the same recipient; amount not printed here, see Sources) &#124; https://bofip.impots.gouv.fr/bofip/1196-PGP.html &#124; | Current ## The taxable base, nativeLF166–166 | Retained / source-corrected: FR-L44: actual published73TTC inclusive perobject/year/samebeneficiary closes unreadamount reservation; underlying deduction conditions still apply. |
| current_main62b7639a / 151 | &#124; Private use by owners, directors or staff &#124; Not deductible &#124; https://bofip.impots.gouv.fr/bofip/1194-PGP.html &#124; | Current ## The taxable base, nativeLF167–167 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 152 | &#124; Restaurant meals &#124; Not excluded by name. Deductible only where incurred for the business, with the purpose and guests documented &#124; CGI annexe II, art. 206 &#124; | Current ## The taxable base, nativeLF168–168 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 153 | &#124; Advertising for alcoholic drinks &#124; Deductible under the ordinary rules from 21 February 2026 (CGI art. 273 septies E, LF 2026 art. 91) &#124; https://bofip.impots.gouv.fr/bofip/15011-PGP.html &#124; | Current ## The taxable base, nativeLF169–169 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 154 | &#124; Fixed assets &#124; Line 19, not line 20. Adjusted over five years (movable) or twenty years (immovable) if use changes. The EUR 500 small-equipment tolerance decides asset or expense; where an item is made of several parts, the tolerance is tested on the global price of all the parts (https://bofip.impots.gouv.fr/bofip/2109-PGP.html: "en considération du prix global de l'ensemble des éléments") &#124; https://bofip.impots.gouv.fr/bofip/2109-PGP.html &#124; | Current ## The taxable base, nativeLF170–170 | Retained / source-corrected: Actual annual adjustment/coefficient gate, timing and optional500 conditions supplied. |
| current_main62b7639a / 156 | **Conservative defaults when facts are missing.** Unknown rate on a sale: 20%. Unknown VAT status of a purchase: not deductible. Unknown counterparty country: France. Unknown B2B or B2C status of an EU customer: consumer, charge French VAT. Unknown business-use share (car, phone, home office): no recovery. Unknown SaaS billing entity: line A3 self-assessment. Unknown whether a cost is blocked: blocked. Unknown whether in scope: in scope. | Current ## The taxable base, nativeLF172–172 | Retained / source-corrected: FR-L34: unsupported20/France/consumer/A3/permanent block defaults replaced with fact collection and temporary evidence hold. |
| current_main62b7639a / 158 | **Supplier and bank-line patterns (pre-classifier).** Match the counterparty name on the bank statement, most specific first; if nothing matches, apply the rules above. | Current ## The taxable base, nativeLF174–174 | Retained / source-corrected: FR-L41: every supplier row is fact-conditional, a question aid rather than tax proof. |
| current_main62b7639a / 160 | &#124; Pattern &#124; Treatment &#124; | Current ## The taxable base, nativeLF176–176 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 162 | &#124; Bank fees and interest (BNP, Société Générale, Crédit Agricole, LCL, BPCE, Caisse d'Épargne, La Banque Postale, CIC, Crédit Mutuel; fee lines of Qonto, Revolut, Wise, N26); INTERETS, AGIOS; PRET, EMPRUNT &#124; Exclude (exempt financial services or out of scope). Check for separate taxable subscription invoices from neobanks &#124; | Current ## The taxable base, nativeLF178–178 | Retained / source-corrected: FR-L41: operation-specific exemption/option, not automatic bank-brand exemption. |
| current_main62b7639a / 163 | &#124; DGFIP, TRESOR PUBLIC, IMPOTS.GOUV, URSSAF, CPAM, SSI, France Travail, CIPAV, CNAV, GREFFE, CFE, CVAE, PREFECTURE, INPI, CCI, CMA &#124; Exclude: taxes, social charges, sovereign or registry fees &#124; | Current ## The taxable base, nativeLF179–179 | Retained / source-corrected: FR-L41: proved non-supply payments only; public entity name alone is insufficient. |
| current_main62b7639a / 164 | &#124; SALAIRE, PAIE, MUTUELLE (employee), DIVIDENDE, APPORT, VIREMENT INTERNE &#124; Exclude: outside VAT &#124; | Current ## The taxable base, nativeLF180–180 | Retained / source-corrected: FR-L41: actual wages/capital/transfers only; label alone is insufficient. |
| current_main62b7639a / 165 | &#124; EDF, TotalEnergies, Orange, Free, SFR, Bouygues Telecom, OVHcloud &#124; Domestic 20%, line 20. Gas (Engie) and water (Veolia, Suez): read the invoice for the rate &#124; | Current ## The taxable base, nativeLF181–181 | Retained / source-corrected: FR-L41: actual product/entity/lawful rate and use, not a universal utility20 route. |
| current_main62b7639a / 166 | &#124; AXA, MAIF, MACIF, MATMUT, MAAF, Groupama, Generali, AG2R, Malakoff Humanis &#124; Exclude: insurance is exempt &#124; | Current ## The taxable base, nativeLF182–182 | Retained / source-corrected: FR-L41: actual insurance/broker operation, not every service by an insurer. |
| current_main62b7639a / 167 | &#124; La Poste standard mail &#124; Exclude (universal service). Colissimo, Chronopost, DHL Express France, Mondial Relay: 20%. UPS, TNT, FedEx: check whether billed from France or abroad (A3) &#124; | Current ## The taxable base, nativeLF183–183 | Retained / source-corrected: FR-L41: actual universal service gate and entity, not parcel-brand rate selection. |
| current_main62b7639a / 168 | &#124; SNCF, Ouigo, RATP, taxis, G7, Bolt, Heetch, Uber rides, Air France domestic &#124; 10%, line 20. International flights: exclude. Motorway tolls (Vinci, Sanef, APRR): 20% &#124; | Current ## The taxable base, nativeLF184–184 | Retained / source-corrected: Actual output passenger rate separated from purchaser deduction exclusion; tolls conditional. |
| current_main62b7639a / 169 | &#124; Supermarkets (Carrefour, Auchan, Leclerc, Lidl, Monoprix, etc.) and restaurants &#124; Default block unless a catering business or a documented business meal &#124; | Current ## The taxable base, nativeLF186–186 | Retained / source-corrected: FR-L41: actual goods/business use and exclusions; no catering-only or permanent name-based denial. |
| current_main62b7639a / 170 | &#124; Google, Microsoft, Adobe, Meta, LinkedIn, Spotify, Dropbox, Slack, Atlassian, Zoom (EU billing entities); Notion, OpenAI, Anthropic, Figma, Canva, Twilio, GitHub, HubSpot (non-EU or check); AWS EMEA SARL &#124; A3 plus line 20 (self-assessment). If the invoice shows French TVA actually charged, treat as a domestic 20% purchase &#124; | Current ## The taxable base, nativeLF187–187 | Retained / source-corrected: Actual participating establishment, lawful invoice tax and ordinary entitlement replace brand/printed-tax inference. |
| current_main62b7639a / 171 | &#124; Amazon, Etsy, eBay marketplace fees &#124; A3 plus line 20 where billed from outside France (CA3 notice n° 3310 NOT-CA3-SD: line A3 is "prestations de services fournies par un prestataire non établi en France et imposables en France sur le fondement des articles 259-1° et 283-2 du CGI"); the sales themselves go to A1 at the applicable rate (or E3, distance sales taxable in the member state of arrival above the EUR 10,000 limit of CGI art. 259 D or by option, declared through the OSS: same notice, line E3) &#124; | Current ## The taxable base, nativeLF188–188 | Retained / source-corrected: Actual invoice and supply place required; marketplace name alone does not prove A3. |
| current_main62b7639a / 172 | &#124; Stripe, PayPal transaction fees &#124; Exclude (exempt payment services). Stripe subscription: A3 plus 20. SumUp, Square, Zettle: by billing entity &#124; | Current ## The taxable base, nativeLF189–189 | Retained / source-corrected: FR-L41: actual payment operation/option versus technical subscription, not blanket brand exemption. |
| current_main62b7639a / 173 | &#124; Expert-comptable, avocat, notaire (business), commissaire aux comptes, architecte &#124; Domestic 20%, line 20 &#124; | Current ## The taxable base, nativeLF190–190 | Retained / source-corrected: FR-L41: actual regime/place/rate/use/capitalisation conditions replace profession-wide20. |
| current_main62b7639a / 174 | &#124; LOYER COMMERCIAL, SCI with TVA invoiced &#124; 20% only where the landlord opted for VAT. Residential rent and TAXE FONCIERE: exclude &#124; | Current ## The taxable base, nativeLF191–191 | Retained / source-corrected: FR-L44: actualbare/furnished/propertynature and261D/260option/exceptions, no blanketallcommercial/residentialoutcome. |
| current_main62b7639a / 175 | &#124; RETRAIT DAB, cash &#124; Ask; default exclude as drawings &#124; | Current ## The taxable base, nativeLF192–192 | Retained / source-corrected: FR-L41: actual use/reconciliation; bank withdrawal proves neither purchase invoice nor personal drawing. |
| current_main62b7639a / 177 | Bank-statement reading: French exports are usually semicolon-separated with DD/MM/YYYY dates (Qonto and Revolut use ISO dates). VIR is a transfer, CB a card payment, PRLV a direct debit, CHQ a cheque, REM a cheque deposit, TIP an interbank payment. Refunds (remboursement, annulation, avoir) go as negatives on the original line; a customer credit note is a B5 correction, a non-taxed correction F8. Convert foreign currency at the transaction-date rate and keep the evidence. An IBAN prefix shows the bank's country, not the customer's VAT status: check VIES. | Current ## The taxable base, nativeLF194–194 | Retained / source-corrected: Signed bookkeeping reversals distinguished from positive B5/F8 method; actual VAT tax-point FX replaces invoice-date default. |
| current_main62b7639a / 179 | **Questions to raise when a line is ambiguous.** Fuel and vehicle costs (was the vehicle designed for people or goods, and which fuel?); restaurants (who was present and why?); SaaS (legal entity, country, any French TVA charged?); round transfers from the owner's name (sale, capital or loan?); incoming money from individuals or foreign accounts (sale? business or consumer? which country?); large one-off purchases near EUR 500 (asset or expense?); mixed-use phone or home costs (business share?); outgoing transfers to individuals (contractor with invoice, wages, refund or private?); foreign hotels (foreign VAT is not French input VAT; a refund may be claimed in that state); Airbnb income (furnished letting falls in the services band); construction subcontractors (domestic reverse charge?); platform sales on Amazon, Etsy or eBay (cross-border consumer sales above EUR 10,000 go through the OSS, refuse here under `eu-vat-directive` R-EU-5). | Current ## The taxable base, nativeLF196–196 | Retained / source-corrected: Actual transaction questions retained; distance threshold qualified for BOTH years/establishment/dispatch. |
| current_main62b7639a / 181 | **Invoices.** Every mandatory particular applies at any amount; the EUR 150 rule only waives the seller's VAT number. Reverse-charge invoices say "Auto-liquidation". From 1 September 2026 (large companies and ETI) and 1 September 2027 (SMEs and micro-enterprises), invoices add four new particulars: the customer's SIREN, the delivery address if different, whether the invoice is for goods, services or both, and "Option pour le paiement de la taxe d'après les débits" where that option was made (service-public F31808). | Current ## The taxable base, nativeLF198–198 | Retained / source-corrected: FR-L35: actual invoice simplification/exclusions, actual wording and new-particular commencement retained. |
| current_main62b7639a / 183 | **Bank statement only (OpenAccountants working practice, not a legal rule).** If there is no bank statement at all, stop. With a bank statement but no invoices, prepare the return and tell the reviewer in writing that every input VAT claim must be checked against a compliant invoice before the return is approved. | Current ## The taxable base, nativeLF204–204 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 185 | **Working paper.** Follow `vat-workflow-base` Section 3. In the Transactions sheet the line-code column accepts only 2026 CA3 codes, blank for excluded lines, and "A3/20" style for self-assessed lines. The Line Summary sheet sums A1, E1, E2, E3, F2, A3, A4, B2, B4, then the rate block 08, 09, 9B, I1 to I6, line 16, memo 17, lines 19, 20, 22, 23, memo 24, then 25 or TD, 26, 27, 28 and 32. If line 23 exceeds line 16, line 25 is the credit and line 27 = 25 less 26 carries to the next return; otherwise TD = 16 less 23. Shade any row resting on a conservative default and recalculate the workbook before handing it over. | Current ## The taxable base, nativeLF208–208 | Retained / source-corrected: Actual X5/Z5/AB adjustments supplied instead of an unconditional ordinary net formula. |
| current_main62b7639a / 191 | &#124; CA3, régime réel normal &#124; Monthly, between the 15th and the 24th of the following month. The exact day depends on the department (Paris, 92, 93 and 94 apart), the category of business and the SIREN or the first letter of the name, and is shown in the espace professionnel. Never state a single date &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F23566 ; https://www.impots.gouv.fr/le-regime-reel-normal-dates-limites-de-transmission-des-ca3 &#124; | Current ## Deadlines and filing, nativeLF214–214 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 192 | &#124; CA3, quarterly option &#124; Where annual VAT due is below EUR 4,000 (CGI art. 287-2) &#124; Légifrance art. 287 &#124; | Current ## Deadlines and filing, nativeLF215–215 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 193 | &#124; CA12, régime simplifié &#124; Annual, by the second working day after 1 May for a calendar year; within three months of the year end otherwise &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F23566 &#124; | Current ## Deadlines and filing, nativeLF216–216 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 194 | &#124; Régime simplifié instalments &#124; July (55%) and December (40%); balance with the CA12. Off-calendar years: return filed January to May of N gives instalments July and December N; June to October gives December N and July N+1; November or December gives July and December N+1 &#124; CGI art. 287-3 ; F23566 &#124; | Current ## Deadlines and filing, nativeLF217–217 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 195 | &#124; Régime simplifié moved to monthly CA3 &#124; VAT due for the previous year above EUR 15,000 (art. 287-3 bis); or the business makes intra-EU acquisitions, imports or exits from a suspensive regime (art. 287-3 ter, from 1 January 2025; quarterly if under EUR 4,000) &#124; Légifrance art. 287 &#124; | Current ## Deadlines and filing, nativeLF218–218 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 196 | &#124; Change of regime &#124; Crossing the previous-year band or the EUR 15,000 limit: régime réel normal from 1 January of the following year (F23566). Crossing a current-year ceiling ends the régime simplifié during the year (CIBS L. 162-5); refer for the exact date and returns &#124; F23566 ; CIBS L. 162-5 &#124; | Current ## Deadlines and filing, nativeLF219–219 | Retained / source-corrected: FR-L36: actual D1628 ordinary calendar-year effective date; separate non-calendar question preserved. |
| current_main62b7639a / 197 | &#124; Cessation or sale of the business &#124; Final return within 30 days; 60 days under the régime simplifié (CGI art. 287-4) &#124; Légifrance art. 287 &#124; | Current ## Deadlines and filing, nativeLF220–220 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 198 | &#124; État récapitulatif des clients (intra-EU supplies of goods) and déclaration européenne de services (B2B services taxed in the customer's EU state) &#124; Within ten working days after the month the VAT became due, filed with customs on pro.douane.gouv.fr (CGI art. 289 B) &#124; CA3 notice 3310-NOT-CA3-SD, 2026 &#124; | Current ## Deadlines and filing, nativeLF221–221 | Retained / source-corrected: Actual eligible goods/DES conditions and paper-franchise route qualified. |
| current_main62b7639a / 199 | &#124; Payment &#124; With the return, online from the espace professionnel on impots.gouv.fr &#124; F23566 &#124; | Current ## Deadlines and filing, nativeLF222–222 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 200 | &#124; E-invoicing: receiving &#124; From 1 September 2026 every business established in France must be able to receive e-invoices through an approved platform (plateforme agréée) &#124; CGI art. 289 bis ; LFR 2022 art. 26, III, as rewritten by LF 2024 art. 91 ; impots.gouv.fr FAQ &#124; | Current ## Deadlines and filing, nativeLF223–223 | Retained / source-corrected: FR-L44: assujettistatus includesfranchise/exemptsupplies, not every nonassujettientity. |
| current_main62b7639a / 201 | &#124; E-invoicing and e-reporting: issuing &#124; From 1 September 2026 for large companies, ETI and VAT groups; from 1 September 2027 for SMEs and micro-enterprises (size under LME art. 51 and decree 2008-1354, art. 3) &#124; same ; BOFiP BOI-TVA-DECLA-20-30-50 (30 September 2026) &#124; | Current ## Deadlines and filing, nativeLF224–224 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 203 | Formats, platforms, e-reporting frequencies and the payment-data rules are in `france-einvoice`. | Current ## Deadlines and filing, nativeLF226–226 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 209 | &#124; Late payment of tax &#124; Interest of 0.20% a month, from the first day of the month after the due month to the last day of the month of payment (CGI art. 1727, III and IV) &#124; Légifrance art. 1727 &#124; | Current ## Penalties and interest, nativeLF236–236 | Retained / source-corrected: FR-L38: actual1727IV3 filing-majoration stop period distinguished. |
| current_main62b7639a / 210 | &#124; Late return, no formal notice, or filed within 30 days of a notice &#124; 10% of the tax due on the return (CGI art. 1728, 1, a) &#124; Légifrance art. 1728 &#124; | Current ## Penalties and interest, nativeLF237–237 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 211 | &#124; Return still missing 30 days after a formal notice &#124; 40% (art. 1728, 1, b) &#124; same &#124; | Current ## Penalties and interest, nativeLF238–238 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 212 | &#124; Hidden activity discovered &#124; 80% (art. 1728, 1, c) &#124; same &#124; | Current ## Penalties and interest, nativeLF239–239 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 213 | &#124; Errors or omissions: deliberate failure / abuse of law or fraudulent schemes &#124; 40% / 80% (CGI art. 1729) &#124; Légifrance art. 1729 &#124; | Current ## Penalties and interest, nativeLF240–240 | Retained / source-corrected: FR-L38: actual abuse80/40 principal-initiator/beneficiary condition restored. |
| current_main62b7639a / 214 | &#124; Late payment where art. 1728 does not apply &#124; 5% surcharge (CGI art. 1731) &#124; Légifrance art. 1731 &#124; | Current ## Penalties and interest, nativeLF241–241 | Retained / source-corrected: Actual1731full-payment-with-late-declaration exception, not absenceof1728alone. |
| current_main62b7639a / 215 | &#124; Self-assessed tax that would have been deductible but was left off the return &#124; Fine of 5% of the deductible amount (CGI art. 1788 A, 4) &#124; Légifrance art. 1788 A &#124; | Current ## Penalties and interest, nativeLF242–242 | Retained / source-corrected: FR-L39: ordinary1788A4 amount separated from special self-supply adjustment. |
| current_main62b7639a / 216 | &#124; État récapitulatif filed late &#124; EUR 750; EUR 1,500 if still missing 30 days after notice; EUR 15 per error, capped at EUR 1,500 (art. 1788 A, 1 and 2) &#124; same &#124; | Current ## Penalties and interest, nativeLF243–243 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 217 | &#124; Invoice errors or omissions &#124; EUR 15 per error, capped at a quarter of the invoice amount (CGI art. 1737, II) &#124; Légifrance art. 1737 &#124; | Current ## Penalties and interest, nativeLF244–244 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 218 | &#124; Invoice not issued electronically when required &#124; EUR 50 per invoice, capped at EUR 15,000 a year (art. 1737, III, as amended by LF 2026) &#124; same &#124; | Current ## Penalties and interest, nativeLF245–245 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 219 | &#124; No approved platform for receiving e-invoices &#124; Formal notice to comply within three months; then EUR 500; then EUR 1,000 after a second three-month notice, and EUR 1,000 again for each further three months the failure persists (CGI art. 1737, IV bis) &#124; Légifrance art. 1737 &#124; | Current ## Penalties and interest, nativeLF246–246 | Retained / source-corrected: FR-L40: each further1000 requires an unsuccessful formalnotice, not elapsedtime alone. |
| current_main62b7639a / 220 | &#124; E-reporting not transmitted &#124; EUR 500 per transmission, capped at EUR 15,000 a year (CGI art. 1788 D, I and II, as amended by LF 2026) &#124; Légifrance art. 1788 D &#124; | Current ## Penalties and interest, nativeLF247–247 | Retained / source-corrected: FR-L39: calendar-yearcap per290/290Aobligation and actualVrelief. |
| current_main62b7639a / 221 | &#124; First-offence relief &#124; The invoice fines in art. 1737, II and III do not apply to a first offence in the current year and the three previous years when it is put right spontaneously or within 30 days of the administration's first request (art. 1737, V) &#124; Légifrance art. 1737 &#124; | Current ## Penalties and interest, nativeLF248–248 | Retained / source-corrected: FR-L39: actual separate1737/1788DVrelief, no automaticIVbisextension. |
| current_main62b7639a / 223 | Example of the interest rule: a CA3 for March 2026 showing EUR 4,000 due, filed and paid in June without any notice, bears the 10% majoration (EUR 400) and interest for May and June, 2 × 0.20% × 4,000 = EUR 16. Audit procedure, the reductions for voluntary correction and the taxpayer's rights are in `fr-tax-audit`. | Current ## Penalties and interest, nativeLF250–250 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 227 | - **B2B services sold to EU customers:** place of supply is the customer's state (CGI art. 259-1°). Invoice without French VAT, mark "Auto-liquidation", put the amount on E2, check the customer's number on VIES, and file the déclaration européenne de services. | Current ## Cross-border points, nativeLF254–254 | Retained / source-corrected: General place versus specialrules; actual eligible DES destination liability/non-exemption gates. |
| current_main62b7639a / 228 | - **Goods sold to EU businesses:** zero-rated on F2 with VIES check and transport proof; état récapitulatif within ten working days after the month. | Current ## Cross-border points, nativeLF255–255 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 229 | - **Distance sales and B2C digital services to other EU states:** French VAT while the EU-wide total stays at or below EUR 10,000 a year; above it, or on option, the destination state's VAT applies and the OSS is used. That is outside this skill (`eu-vat-directive`, R-EU-5); such sales sit on E3. | Current ## Cross-border points, nativeLF256–256 | Retained / source-corrected: Actual BOTH-year/establishment/dispatch/option selector; OSS eligible route, not automatic duty. |
| current_main62b7639a / 230 | - **Purchases from abroad:** self-assess as set out in The taxable base (A3, B2, A4, B4). | Current ## Cross-border points, nativeLF257–257 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 231 | - **Non-established businesses selling in France:** where a French taxable customer buys, the customer is liable under art. 283-1 and 283-2 in the cases those articles name. A non-EU business that must register may need a fiscal representative: refer. | Current ## Cross-border points, nativeLF258–258 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 232 | - **The EU franchise:** an EU business with EU-wide turnover up to EUR 100,000 can use the French franchise after notifying its own state (art. 293 B bis); a French business crossing EUR 100,000 of EU-wide turnover while using another state's franchise must tell the French administration within 15 working days (art. 293 B ter). | Current ## Cross-border points, nativeLF259–259 | Retained / source-corrected: FR-L45: cumulativehostState/BOTHyear/process and15workingdayduties. |
| current_main62b7639a / 233 | - **Monaco:** tax on operations to Monaco is shown at memo line 18 of the CA3. | Current ## Cross-border points, nativeLF260–260 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 234 | - Income tax on cross-border activity is in `fr-cross-border` and `fr-corporate-tax`. | Current ## Cross-border points, nativeLF261–261 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 238 | **Example 1: monthly CA3 for a Paris consultancy (régime réel normal).** In April 2026 the company sells EUR 50,000 of consulting at 20%, and its in-house café sells EUR 8,000 of food and soft drinks for consumption on the premises at 10% (CGI art. 279, m; alcoholic drinks would be 20%). It buys Google Ads from Google Ireland for EUR 850 (no VAT on the invoice), other French purchases of EUR 12,000 plus 20% VAT, and a server for EUR 1,500 plus 20% VAT that it records as a fixed asset. Sales: A1 is 58,000; line 08 base 50,000 and tax 10,000; line 9B base 8,000 and tax 800. Google Ads: A3 is 850, tax 170 joins line 08, and the same 170 is deducted at line 20. Deductions: line 20 is 2,400 plus 170, line 19 is 300. Line 16 is 10,970, line 23 is 2,870, so TD and line 28 are 8,100. | Current ## Worked examples, nativeLF274–274 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 240 | ```oa-check<br>name: France CA3 April 2026, consultancy and café with an EU service self-assessed<br>inputs:<br>  sales_20: 50000<br>  sales_10: 8000<br>  eu_service_a3: 850<br>  domestic_purchases_net: 12000<br>  fixed_asset_net: 1500<br>steps:<br>  - tax_08: sales_20 * 0.20 + eu_service_a3 * 0.20<br>  - tax_9b: sales_10 * 0.10<br>  - line_16: tax_08 + tax_9b<br>  - line_19: fixed_asset_net * 0.20<br>  - line_20: domestic_purchases_net * 0.20 + eu_service_a3 * 0.20<br>  - line_23: line_19 + line_20<br>  - vat_due: line_16 - line_23<br>expected:<br>  line_16: 10970.00<br>  line_23: 2870.00<br>  vat_due: 8100.00<br>``` | Current ## Worked examples, nativeLF276–296 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 262 | **Example 2: régime simplifié, instalments and the fixed-asset edge.** A shop on the régime simplifié had tax of EUR 9,000 for 2025 before the VAT on fixed assets. Its 2026 instalments are 55% in July (4,950) and 40% in December (3,600). On the 2026 CA12 its gross VAT is EUR 18,000, deductions on other goods and services EUR 6,500, and VAT on fixed assets EUR 1,200. Net VAT for 2026 is 10,300, so the balance due with the CA12 by the second working day after 1 May 2027 is 10,300 less 8,550, or 1,750. The edge: next year's instalment base (line 57) is struck before the fixed-asset VAT, so it is 18,000 less 6,500, or 11,500, not 10,300. The 2027 instalments are 6,325 in July and 4,600 in December. | Current ## Worked examples, nativeLF298–298 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 264 | ```oa-check<br>name: France CA12 2026, instalments, balance and next year's base<br>inputs:<br>  prior_year_base: 9000<br>  gross_vat: 18000<br>  deduction_other: 6500<br>  deduction_fixed_assets: 1200<br>steps:<br>  - july_2026: prior_year_base * 0.55<br>  - december_2026: prior_year_base * 0.40<br>  - net_vat_2026: gross_vat - deduction_other - deduction_fixed_assets<br>  - balance_may_2027: net_vat_2026 - july_2026 - december_2026<br>  - base_2027: gross_vat - deduction_other<br>  - july_2027: base_2027 * 0.55<br>  - december_2027: base_2027 * 0.40<br>expected:<br>  july_2026: 4950.00<br>  december_2026: 3600.00<br>  balance_may_2027: 1750.00<br>  july_2027: 6325.00<br>  december_2027: 4600.00<br>``` | Current ## Worked examples, nativeLF300–321 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 289 | - Which regime are you in, and what were last year's turnover (by activity: goods and catering, or services) and last year's VAT due? Both numbers decide the regime. | Current ## Ask the client first, nativeLF327–327 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 290 | - What filing date does your espace professionnel show for the CA3? It depends on department, category and SIREN. | Current ## Ask the client first, nativeLF328–328 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 291 | - Do you sell outside France? For each customer: business or consumer, goods or services, which country. That decides E1, E2, E3, F2 and the EU statements. | Current ## Ask the client first, nativeLF329–329 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 292 | - Do you buy goods from other EU states or import? Under the régime simplifié that alone forces monthly CA3 returns from 2025. | Current ## Ask the client first, nativeLF330–330 | Retained / source-corrected: FR-L45: actualCA3triggerandstatutoryquarterlyexception retained. |
| current_main62b7639a / 293 | - Any credit at line 27 of your last return, any exempt income, any construction subcontracting, any company cars (designed to carry people or goods)? | Current ## Ask the client first, nativeLF331–331 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 294 | - Refuse or refer: a business inside the franchise that has not opted; partial exemption above de minimis; margin scheme; property VAT; VAT groups; fiscal representatives; overseas departments; anyone wanting income tax (use `fr-income-tax` or `fr-personal-income-tax`); any refusal in `eu-vat-directive` R-EU-1 to R-EU-12. | Current ## Ask the client first, nativeLF332–332 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 300 | &#124; CGI art. 293 B, 293 B bis, 293 B ter (franchise; LF 2025 art. 32 and loi n° 2025-1044 art. 1) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-24 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF338–338 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 301 | &#124; CGI art. 287 (returns, instalments, monthly triggers) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191928/2026-10-24 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF339–339 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 302 | &#124; CIBS art. L. 162-4 to L. 162-8 (régime simplifié conditions; L. 162-4 indexation rule) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000044598127/2026-10-24 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF340–340 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 303 | &#124; CIBS art. A. 162-7 (régime simplifié amounts for 2026, arrêté of 27 January 2026) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000049803748/2026-10-24 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF341–341 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 304 | &#124; BOFiP BOI-BAREME-000036-20260701 (régime simplifié limits for 2026) &#124; https://bofip.impots.gouv.fr/bofip/9368-PGP.html/identifiant=BOI-BAREME-000036-20260701 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF342–342 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 305 | &#124; CGI art. 278 (20%) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191854/2026-10-24 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF343–343 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 306 | &#124; CGI art. 278-0 bis (5.5%) and 279 (10%) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191654/2026-10-24 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF344–344 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 307 | &#124; CGI art. 281 quater and 281 octies (2.1%) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191656/2026-10-24 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF345–345 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 308 | &#124; CGI art. 298 septies (press, 2.1% and 1.05%) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179663/2026-10-24 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF346–346 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 309 | &#124; CGI art. 289 B (état récapitulatif) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191662/2026-10-24 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF347–347 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 310 | &#124; CGI art. 289 bis (e-invoicing, amended by LF 2026 art. 123) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191855/2026-10-24 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF348–348 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 311 | &#124; Loi n° 2023-1322 (LF 2024), art. 91, rewriting LFR 2022 art. 26, III (e-invoicing dates) &#124; https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048727345 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF349–349 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 312 | &#124; CGI art. 1727 (late interest) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006147309/2026-10-24 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF350–350 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 313 | &#124; CGI art. 1728 (late filing, amended by LF 2026 art. 126) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179995/2026-10-24 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF351–351 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 314 | &#124; CGI art. 1729 (inaccuracies) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179987/2026-10-24 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF352–352 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 315 | &#124; CGI art. 1731 (5% late payment) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006163002/2026-10-24 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF353–353 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 316 | &#124; CGI art. 1737 (invoice fines) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006163056/2026-10-24 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF354–354 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 317 | &#124; CGI art. 1788 A and 1788 D (statements, self-assessment, e-reporting fines) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162921/2026-10-24 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF355–355 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 318 | &#124; BOFiP actualité 7 October 2026: CIBS recodification moved to 1 January 2027; LF 2026 VAT measures &#124; https://bofip.impots.gouv.fr/bofip/15140-PGP.html &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF356–356 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 319 | &#124; BOFiP actualité 17 June 2026: alcohol advertising deduction (LF 2026 art. 91) &#124; https://bofip.impots.gouv.fr/bofip/15011-PGP.html &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF357–357 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 320 | &#124; BOFiP BOI-TVA-DECLA-20-30-50 (e-reporting dates) &#124; https://bofip.impots.gouv.fr/bofip/13897-PGP.html &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF358–358 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 321 | &#124; BOFiP: vehicles; fuel; accommodation; gifts; small equipment &#124; https://bofip.impots.gouv.fr/bofip/1192-PGP.html ; https://bofip.impots.gouv.fr/bofip/1194-PGP.html ; https://bofip.impots.gouv.fr/bofip/1190-PGP.html ; https://bofip.impots.gouv.fr/bofip/1196-PGP.html ; https://bofip.impots.gouv.fr/bofip/2109-PGP.html &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF359–359 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 322 | &#124; Service-public: franchise en base (checked 1 January 2026) &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F21746 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF360–360 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 323 | &#124; Service-public: déclarer et payer la TVA (checked 21 February 2026) &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F23566 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF362–362 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 324 | &#124; Service-public: invoice particulars (checked 11 August 2026) &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F31808 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF363–363 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 325 | &#124; CA3 form 3310-CA3-SD 2026 (impots.gouv.fr in maintenance; Internet Archive copy of 10 May 2026) &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF364–364 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 326 | &#124; CA3 notice 3310-NOT-CA3-SD 2026 (Internet Archive copy of 16 October 2026) &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF365–365 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 327 | &#124; CA12 form 3517-S-SD 2026 (Internet Archive copy of 12 January 2026) &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5291.pdf &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF372–372 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 328 | &#124; impots.gouv.fr: CA3 filing dates (Internet Archive copy of 29 September 2026) &#124; https://www.impots.gouv.fr/le-regime-reel-normal-dates-limites-de-transmission-des-ca3 &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF373–373 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 329 | &#124; impots.gouv.fr: e-invoicing start dates, modified 16 January 2026 (Internet Archive copy of 25 June 2026) &#124; https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF374–374 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 330 | &#124; impots.gouv.fr: overseas department rates (Internet Archive copy of 18 May 2026) &#124; https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF375–375 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 331 | &#124; impots.gouv.fr: VAT regimes, modified 21 May 2026, still showing 2023-2025 limits (Internet Archive copy of 29 September 2026) &#124; https://www.impots.gouv.fr/professionnel/les-regimes-dimposition-la-tva &#124; 2026-10-24 &#124; | Current ## Sources, nativeLF376–376 | Retained / source-corrected: Exact unchanged baseline topic, rebound to actual current coordinates. |
| current_main62b7639a / 333 | Not yet confirmed: the amount of the very-low-value gift exception (CGI annexe IV, art. 28-00 A, not re-read); the CA12 completion notice 3517-S-NOT-SD 2026 (no copy reachable; CA12 lines taken from the form and the earlier read of the notice); the reference date for measuring a business's size for the e-invoicing timetable (LFR 2022 art. 26, III and its decree, not re-read); the consolidated text of LFR 2022 art. 26, III after LF 2025 and LF 2026 (the dates were checked against the LF 2024 text, BOFiP of 30 September 2026 and service-public F31808); the exact date a business leaves the régime simplifié after crossing a current-year ceiling under CIBS L. 162-5 and its implementing decree; the full lists of goods and services under the 10% and 5.5% rates after LF 2026 (only the article headings and the BOFiP summary were read); Corsican rate rules beyond the CA3 lines; whether the franchise applies as of right in the first year of activity up to the higher limits (EUR 93,500 / EUR 41,250, as the impots.gouv.fr regimes page says) or only after scaling turnover to a full year (service-public F21746): the two pages differ and CGI art. 293 B was not re-read on this point; the exclusion of jet fuel used in aircraft without a right to deduct (older version of this skill, not found in the saved BOFiP text); the restaurant-meal treatment rests on CGI annexe II art. 206, not re-read today. | Current ## Sources, nativeLF378–378 | Retained / source-corrected: Source questions retained and narrowed only for clauses actually read; no universal tax completeness claim. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 15 | # France: the VAT return (déclaration de TVA, CA3 and CA12) | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 17 | This skill prepares, reviews and classifies transactions for a French VAT return: the monthly or quarterly CA3 under the régime réel normal, and the annual CA12 under the régime réel simplifié. Figures are for tax year 2026. The rules stated are those in force on 19 October 2026, read on official pages between 19 September and 19 October 2026; each page's own date stamp is given where it matters. Two pages carry different numbers for the same rule and both are official: `entreprendre.service-public.gouv.fr` was checked on 21 February 2026 and gives the simplified regime turnover band for 2026, while the `impots.gouv.fr` page "Les régimes d'imposition à la TVA", modified 21 May 2026, still prints the band it labels as applying from 1 January 2025. Both are set out below and the disagreement is named where it falls. | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210; ## Rates, bands and thresholds nativeLF92; ## Rates, bands and thresholds nativeLF94; ## Sources nativeLF378 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 19 | ## Section 1: Quick reference | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 21 | **Quick reference fields** | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 23 | &#124; Field &#124; Value &#124; | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 24 | &#124; --- &#124; --- &#124; | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 25 | &#124; Country &#124; France (République française) &#124; | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 26 | &#124; Return form, régime réel normal &#124; CA3, form number 3310-CA3-SD, monthly or quarterly &#124; | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210; ## Who this applies to nativeLF44; ## The taxable base nativeLF98 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 27 | &#124; Return form, régime réel simplifié &#124; CA12 or CA12E, form number 3517-S-SD, annual, with two instalments &#124; | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210; ## Who this applies to nativeLF45; ## Deadlines and filing nativeLF216; ## Deadlines and filing nativeLF217 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 28 | &#124; Filing portal &#124; https://www.impots.gouv.fr (espace professionnel, mode EFI) &#124; | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210; ## Deadlines and filing nativeLF222 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 29 | &#124; Intra-EU recapitulative statement and the services return &#124; pro.douane.gouv.fr &#124; | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210; ## Deadlines and filing nativeLF221 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 30 | &#124; Authority &#124; Direction Générale des Finances Publiques (DGFiP) &#124; | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210; ## Deadlines and filing nativeLF214; ## Sources nativeLF370; ## Deadlines and filing nativeLF222 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 31 | &#124; Currency &#124; euro only &#124; | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210; ## The taxable base nativeLF194; ## The taxable base nativeLF143 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 32 | &#124; Rates &#124; see the rate tables below; never assume a rate from the counterparty's name &#124; | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210; ## Rates, bands and thresholds nativeLF52; ## Rates, bands and thresholds nativeLF53; ## Rates, bands and thresholds nativeLF54; ## Rates, bands and thresholds nativeLF55; ## Rates, bands and thresholds nativeLF56; ## The taxable base nativeLF172; ## The taxable base nativeLF174 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 33 | &#124; Filing frequency &#124; see the regime table below &#124; | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210; ## Who this applies to nativeLF44; ## Who this applies to nativeLF45; ## Deadlines and filing nativeLF215; ## Deadlines and filing nativeLF218 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 34 | &#124; Deadline, CA3 &#124; no single date: see "Filing dates are a schedule, not a date" below &#124; | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210; ## Deadlines and filing nativeLF214 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 35 | &#124; Deadline, CA12 &#124; at the latest the second working day after 1 May; a business whose accounting year does not end on 31 December files within three months of its year end &#124; | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210; ## Deadlines and filing nativeLF216 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 36 | &#124; Companion skill (workflow) &#124; `vat-workflow-base`, load it alongside this one &#124; | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 37 | &#124; Companion skill (EU directive) &#124; `eu-vat-directive`, load it alongside this one &#124; | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 38 | &#124; Refresh date &#124; October 2026 &#124; | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 40 | **Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1. Follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.** | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Who this applies to nativeLF38; ## The taxable base nativeLF202; ## Deadlines and filing nativeLF210 | Retained / corrected in current Guide: Intro, jurisdiction/regime/portal/currency/date and companion-workflow topics retained; identity/period established from actual evidence, not transaction-name inference. Non-rule heading/table scaffolding maps to the same substantive section. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 42 | **VAT rates in mainland France** | ## Rates, bands and thresholds nativeLF52; ## Rates, bands and thresholds nativeLF53; ## Rates, bands and thresholds nativeLF54; ## Rates, bands and thresholds nativeLF55; ## Rates, bands and thresholds nativeLF82; ## Rates, bands and thresholds nativeLF86; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Actual selected rate conditions now supplied by FR-L42; blood/press source gaps narrowed only for actually read clauses. Unknown-rate default explicitly corrected, not retained as a legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 44 | &#124; What &#124; Value &#124; Note &#124; | ## Rates, bands and thresholds nativeLF52; ## Rates, bands and thresholds nativeLF53; ## Rates, bands and thresholds nativeLF54; ## Rates, bands and thresholds nativeLF55; ## Rates, bands and thresholds nativeLF82; ## Rates, bands and thresholds nativeLF86; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Actual selected rate conditions now supplied by FR-L42; blood/press source gaps narrowed only for actually read clauses. Unknown-rate default explicitly corrected, not retained as a legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 45 | &#124; --- &#124; --- &#124; --- &#124; | ## Rates, bands and thresholds nativeLF52; ## Rates, bands and thresholds nativeLF53; ## Rates, bands and thresholds nativeLF54; ## Rates, bands and thresholds nativeLF55; ## Rates, bands and thresholds nativeLF82; ## Rates, bands and thresholds nativeLF86; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Actual selected rate conditions now supplied by FR-L42; blood/press source gaps narrowed only for actually read clauses. Unknown-rate default explicitly corrected, not retained as a legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 46 | &#124; Source &#124; all figures below &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf &#124; | ## Rates, bands and thresholds nativeLF52; ## Rates, bands and thresholds nativeLF53; ## Rates, bands and thresholds nativeLF54; ## Rates, bands and thresholds nativeLF55; ## Rates, bands and thresholds nativeLF82; ## Rates, bands and thresholds nativeLF86; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Actual selected rate conditions now supplied by FR-L42; blood/press source gaps narrowed only for actually read clauses. Unknown-rate default explicitly corrected, not retained as a legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 47 | &#124; Standard rate, the rate whenever no other rate is provided (CGI art. 278), CA3 line 08 &#124; 20% &#124; "08 Taux normal 20 %" &#124; | ## Rates, bands and thresholds nativeLF52; ## Rates, bands and thresholds nativeLF53; ## Rates, bands and thresholds nativeLF54; ## Rates, bands and thresholds nativeLF55; ## Rates, bands and thresholds nativeLF82; ## Rates, bands and thresholds nativeLF86; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Actual selected rate conditions now supplied by FR-L42; blood/press source gaps narrowed only for actually read clauses. Unknown-rate default explicitly corrected, not retained as a legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 48 | &#124; Intermediate reduced rate (CGI art. 279), CA3 line 9B &#124; 10% &#124; "9B Taux réduit 10 %" &#124; | ## Rates, bands and thresholds nativeLF52; ## Rates, bands and thresholds nativeLF53; ## Rates, bands and thresholds nativeLF54; ## Rates, bands and thresholds nativeLF55; ## Rates, bands and thresholds nativeLF82; ## Rates, bands and thresholds nativeLF86; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Actual selected rate conditions now supplied by FR-L42; blood/press source gaps narrowed only for actually read clauses. Unknown-rate default explicitly corrected, not retained as a legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 49 | &#124; Reduced rate (CGI art. 278-0 bis), CA3 line 09 &#124; 5.5% &#124; "09 Taux réduit 5,5 %" &#124; | ## Rates, bands and thresholds nativeLF52; ## Rates, bands and thresholds nativeLF53; ## Rates, bands and thresholds nativeLF54; ## Rates, bands and thresholds nativeLF55; ## Rates, bands and thresholds nativeLF82; ## Rates, bands and thresholds nativeLF86; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Actual selected rate conditions now supplied by FR-L42; blood/press source gaps narrowed only for actually read clauses. Unknown-rate default explicitly corrected, not retained as a legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 50 | &#124; Particular rate in continental France (CGI art. 281 quater to 281 nonies), CA3 line T6 &#124; 2.1% &#124; "France continentale au taux de 2,1 %" &#124; | ## Rates, bands and thresholds nativeLF52; ## Rates, bands and thresholds nativeLF53; ## Rates, bands and thresholds nativeLF54; ## Rates, bands and thresholds nativeLF55; ## Rates, bands and thresholds nativeLF82; ## Rates, bands and thresholds nativeLF86; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Actual selected rate conditions now supplied by FR-L42; blood/press source gaps narrowed only for actually read clauses. Unknown-rate default explicitly corrected, not retained as a legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 52 | Which supplies carry which rate is not settled by the form. As a working summary, and subject to the accountant's check: the intermediate rate covers television subscriptions, restaurant meals, passenger transport and most work on dwellings finished more than two years ago, and BOFiP states the television case in terms, "soumet au taux de 10 % de la TVA les abonnements souscrits par les usagers afin de recevoir les services de télévision" (https://bofip.impots.gouv.fr/bofip/1013-PGP.html); the reduced rate covers most food, books including digital books, and energy-efficiency work on dwellings; the particular rate covers reimbursable medicines and human blood products (https://bofip.impots.gouv.fr/bofip/1449-PGP.html). Press publications also carry the particular rate, under CGI art. 298 septies, which is not on either page above: confirm it before relying on it. | ## Rates, bands and thresholds nativeLF52; ## Rates, bands and thresholds nativeLF53; ## Rates, bands and thresholds nativeLF54; ## Rates, bands and thresholds nativeLF55; ## Rates, bands and thresholds nativeLF82; ## Rates, bands and thresholds nativeLF86; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Actual selected rate conditions now supplied by FR-L42; blood/press source gaps narrowed only for actually read clauses. Unknown-rate default explicitly corrected, not retained as a legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 54 | The special rate is narrow. Where the rate is unknown, the conservative default in the table of defaults below applies. | ## Rates, bands and thresholds nativeLF52; ## Rates, bands and thresholds nativeLF53; ## Rates, bands and thresholds nativeLF54; ## Rates, bands and thresholds nativeLF55; ## Rates, bands and thresholds nativeLF82; ## Rates, bands and thresholds nativeLF86; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Actual selected rate conditions now supplied by FR-L42; blood/press source gaps narrowed only for actually read clauses. Unknown-rate default explicitly corrected, not retained as a legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 56 | **VAT rates in the overseas departments** | ## Rates, bands and thresholds nativeLF56; ## Who this applies to nativeLF46 | Retained / corrected in current Guide: Four DOM figures retained for recognition; actual DOMsource retains specific animal/first140/press scope. Own DOM filing remains excluded, including Guyane/Mayotte non-application. This map does not claim a full DOM method. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 58 | &#124; What &#124; Value &#124; Note &#124; | ## Rates, bands and thresholds nativeLF56; ## Who this applies to nativeLF46 | Retained / corrected in current Guide: Four DOM figures retained for recognition; actual DOMsource retains specific animal/first140/press scope. Own DOM filing remains excluded, including Guyane/Mayotte non-application. This map does not claim a full DOM method. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 59 | &#124; --- &#124; --- &#124; --- &#124; | ## Rates, bands and thresholds nativeLF56; ## Who this applies to nativeLF46 | Retained / corrected in current Guide: Four DOM figures retained for recognition; actual DOMsource retains specific animal/first140/press scope. Own DOM filing remains excluded, including Guyane/Mayotte non-application. This map does not claim a full DOM method. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 60 | &#124; Source &#124; all figures below &#124; https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom &#124; | ## Rates, bands and thresholds nativeLF56; ## Who this applies to nativeLF46 | Retained / corrected in current Guide: Four DOM figures retained for recognition; actual DOMsource retains specific animal/first140/press scope. Own DOM filing remains excluded, including Guyane/Mayotte non-application. This map does not claim a full DOM method. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 61 | &#124; Standard rate in Réunion, Guadeloupe and Martinique &#124; 8.5% &#124; "le taux normal : 8,5 %" &#124; | ## Rates, bands and thresholds nativeLF56; ## Who this applies to nativeLF46 | Retained / corrected in current Guide: Four DOM figures retained for recognition; actual DOMsource retains specific animal/first140/press scope. Own DOM filing remains excluded, including Guyane/Mayotte non-application. This map does not claim a full DOM method. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 62 | &#124; Reduced rate there, covering everything that carries the reduced or the intermediate rate in mainland France &#124; 2.1% &#124; "le taux réduit : 2,1 % pour tous les produits" &#124; | ## Rates, bands and thresholds nativeLF56; ## Who this applies to nativeLF46 | Retained / corrected in current Guide: Four DOM figures retained for recognition; actual DOMsource retains specific animal/first140/press scope. Own DOM filing remains excluded, including Guyane/Mayotte non-application. This map does not claim a full DOM method. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 63 | &#124; Particular rate on sales of live butchery and charcuterie animals to non-taxable persons &#124; 1.75% &#124; "1,75 % pour les ventes d'animaux vivants" &#124; | ## Rates, bands and thresholds nativeLF56; ## Who this applies to nativeLF46 | Retained / corrected in current Guide: Four DOM figures retained for recognition; actual DOMsource retains specific animal/first140/press scope. Own DOM filing remains excluded, including Guyane/Mayotte non-application. This map does not claim a full DOM method. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 64 | &#124; Particular rate on the first 140 performances of certain shows and on certain press publications &#124; 1.05% &#124; "1,05 % pour les 140 premières représentations" &#124; | ## Rates, bands and thresholds nativeLF56; ## Who this applies to nativeLF46 | Retained / corrected in current Guide: Four DOM figures retained for recognition; actual DOMsource retains specific animal/first140/press scope. Own DOM filing remains excluded, including Guyane/Mayotte non-application. This map does not claim a full DOM method. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 66 | VAT is provisionally not applicable in Guyane and in Mayotte. The same page says so in terms: "la TVA n'est provisoirement pas applicable dans les départements de la Guyane et de Mayotte". | ## Rates, bands and thresholds nativeLF56; ## Who this applies to nativeLF46 | Retained / corrected in current Guide: Four DOM figures retained for recognition; actual DOMsource retains specific animal/first140/press scope. Own DOM filing remains excluded, including Guyane/Mayotte non-application. This map does not claim a full DOM method. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 68 | **CA3 lines, from the 2026 form** | ## The taxable base nativeLF98; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Line-map preface/source/scaffolding retained with actually checked2026labels and numeric identifiers. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 70 | This replaces the line list carried by earlier versions of this skill, which used line numbers that are not on the form. Read the line codes below off the 2026 CA3 and nowhere else. | ## The taxable base nativeLF98; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Line-map preface/source/scaffolding retained with actually checked2026labels and numeric identifiers. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 72 | &#124; CA3 line &#124; What goes on it &#124; Rate or code &#124; | ## The taxable base nativeLF98; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Line-map preface/source/scaffolding retained with actually checked2026labels and numeric identifiers. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 73 | &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF98; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Line-map preface/source/scaffolding retained with actually checked2026labels and numeric identifiers. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 74 | &#124; Source &#124; all figures below &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf &#124; | ## The taxable base nativeLF98; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Line-map preface/source/scaffolding retained with actually checked2026labels and numeric identifiers. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 75 | &#124; A1 &#124; Ventes, prestations de services: taxable sales and services, net &#124; code 0979 &#124; | ## The taxable base nativeLF102; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 76 | &#124; A2 &#124; Autres opérations imposables: other taxable operations that are not ordinary turnover, for example disposals of fixed assets &#124; code 0981 &#124; | ## The taxable base nativeLF103; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 77 | &#124; A3 &#124; Achats de prestations de services réalisés auprès d'un assujetti non établi en France (CGI art. 283-2): services bought from a supplier not established in France, net &#124; code 0044 &#124; | ## The taxable base nativeLF104; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 78 | &#124; A4 &#124; Importations other than petroleum products, net &#124; code 0056 &#124; | ## The taxable base nativeLF105; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 79 | &#124; A5 &#124; Exits from a suspensive tax regime other than petroleum products &#124; code 0051 &#124; | ## The taxable base nativeLF106; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 80 | &#124; B1 &#124; Mises à la consommation de produits pétroliers &#124; code 0048 &#124; | ## The taxable base nativeLF107; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 81 | &#124; B2 &#124; Acquisitions intracommunautaires: intra-EU acquisitions of goods, net &#124; code 0031 &#124; | ## The taxable base nativeLF108; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 82 | &#124; B3 &#124; Purchases of electricity, natural gas, heat or cold taxable in France &#124; code 0030 &#124; | ## The taxable base nativeLF109; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 83 | &#124; B4 &#124; Goods or services bought from a taxable person not established in France (CGI art. 283-1) &#124; code 0040 &#124; | ## The taxable base nativeLF110; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 84 | &#124; B5 &#124; Régularisations on the taxed side, for example credit notes to customers &#124; code 0036 &#124; | ## The taxable base nativeLF111; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 85 | &#124; E1 &#124; Exportations hors UE: exports outside the European Union &#124; code 0032 &#124; | ## The taxable base nativeLF112; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 86 | &#124; E2 &#124; Autres opérations non imposables. This is where services supplied to a customer established abroad go, "même si elles sont taxées chez ce dernier" &#124; code 0033 &#124; | ## The taxable base nativeLF113; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 87 | &#124; E3 &#124; Distance sales taxable in another member state to non-taxable persons &#124; code 0047 &#124; | ## The taxable base nativeLF114; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 88 | &#124; E4 &#124; Importations other than petroleum products, non-taxed side &#124; code 0052 &#124; | ## The taxable base nativeLF115; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 89 | &#124; F1 &#124; Acquisitions intracommunautaires non taxées: intra-EU acquisitions that are not taxable in France. Not a counterpart of line B2 &#124; code 0055 &#124; | ## The taxable base nativeLF116; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 90 | &#124; F2 &#124; Livraisons intracommunautaires à destination d'une personne assujettie: zero-rated intra-EU supplies of goods, business to business &#124; code 0034 &#124; | ## The taxable base nativeLF117; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 91 | &#124; F6 &#124; Achats en franchise &#124; code 0037 &#124; | ## The taxable base nativeLF118; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 92 | &#124; F8 &#124; Régularisations on the non-taxed side &#124; code 0039 &#124; | ## The taxable base nativeLF119; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 93 | &#124; 08 &#124; Taxable base and tax, mainland, standard rate &#124; 20% &#124; | ## The taxable base nativeLF120; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 94 | &#124; 09 &#124; Taxable base and tax, mainland, reduced rate &#124; 5.5% &#124; | ## The taxable base nativeLF120; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 95 | &#124; 9B &#124; Taxable base and tax, mainland, intermediate rate &#124; 10% &#124; | ## The taxable base nativeLF120; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 96 | &#124; 10 &#124; Taxable base and tax, overseas departments, standard rate &#124; 8.5% &#124; | ## The taxable base nativeLF121; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 97 | &#124; 11 &#124; Taxable base and tax, overseas departments, reduced rate &#124; 2.1% &#124; | ## The taxable base nativeLF121; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 98 | &#124; 15 &#124; TVA antérieurement déduite à reverser: previously deducted VAT to be paid back &#124; code 0600 &#124; | ## The taxable base nativeLF125; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 99 | &#124; 16 &#124; Total de la TVA brute due, lines 08 to 5B &#124; total &#124; | ## The taxable base nativeLF126; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 100 | &#124; 17 &#124; Dont TVA sur acquisitions intracommunautaires: memo line, of which VAT on intra-EU acquisitions &#124; code 0035 &#124; | ## The taxable base nativeLF127; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 101 | &#124; 18 &#124; Dont TVA sur opérations à destination de Monaco: memo line, of which VAT on operations to Monaco &#124; code 0038 &#124; | ## The taxable base nativeLF127; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 102 | &#124; 19 &#124; Biens constituant des immobilisations: deductible VAT on capital goods &#124; code 0703 &#124; | ## The taxable base nativeLF128; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 103 | &#124; 20 &#124; Autres biens et services: deductible VAT on everything else &#124; code 0702 &#124; | ## The taxable base nativeLF129; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 104 | &#124; 21 &#124; Autre TVA à déduire &#124; code 0059 &#124; | ## The taxable base nativeLF130; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 105 | &#124; 22 &#124; Report du crédit apparaissant ligne 27 de la précédente déclaration &#124; code 8001 &#124; | ## The taxable base nativeLF131; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 106 | &#124; 23 &#124; Total TVA déductible, lines 19 to 2C &#124; total &#124; | ## The taxable base nativeLF132; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 107 | &#124; 24 &#124; Dont TVA déductible sur importations hors produits pétroliers &#124; code 0710 &#124; | ## The taxable base nativeLF133; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 108 | &#124; 2E &#124; Dont TVA déductible sur les produits pétroliers &#124; code 0711 &#124; | ## The taxable base nativeLF133; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 109 | &#124; 25 &#124; Crédit de TVA, line 23 less line 16 &#124; code 0705 &#124; | ## The taxable base nativeLF134; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 110 | &#124; TD &#124; TVA due, line 16 less line 23 &#124; code 8900 &#124; | ## The taxable base nativeLF134; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 111 | &#124; 26 &#124; Remboursement de crédit de TVA demandé sur formulaire n°3519 &#124; code 8002 &#124; | ## The taxable base nativeLF135; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 112 | &#124; 27 &#124; Crédit de TVA à reporter, line 25 less line 26, carried to line 22 of the next return &#124; code 8003 &#124; | ## The taxable base nativeLF136; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 113 | &#124; 28 &#124; TVA nette due &#124; code 8901 &#124; | ## The taxable base nativeLF137; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 114 | &#124; 29 &#124; Taxes assimilées calculées sur l'annexe n° 3310 A &#124; code 9979 &#124; | ## The taxable base nativeLF137; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 115 | &#124; 32 &#124; Total à payer &#124; code 9992 &#124; | ## The taxable base nativeLF137; ## The taxable base nativeLF139 | Retained / corrected in current Guide: Visible old line label and numeric identifier retained. B5/F8 correction is positive under the actual notice; memo lines are not duplicate deduction/output. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 117 | Line 18 is a Monaco memo line. It is not the line for VAT self-assessed on services received from the European Union: that tax is computed from the base on line A3 and appears in the rate block at lines 08, 09 or 9B, with the matching deduction at line 20 or line 19. | ## The taxable base nativeLF141; ## The taxable base nativeLF147 | Retained / corrected in current Guide: Monaco18 versus EU serviceA3/output/input distinction retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 119 | **Rates that only appear in the special blocks of the CA3, including the import block** | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 121 | &#124; CA3 line &#124; What it covers &#124; Rate &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 122 | &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 123 | &#124; Source &#124; all figures below &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 124 | &#124; T1 &#124; Operations in the overseas departments at the particular rate &#124; 1.75% &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 125 | &#124; T2 &#124; Operations in the overseas departments at the particular rate &#124; 1.05% &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 126 | &#124; TC &#124; Operations in Corsica &#124; 13% &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 127 | &#124; T3 &#124; Operations in Corsica &#124; 10% &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 128 | &#124; T4 &#124; Operations in Corsica &#124; 2.1% &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 129 | &#124; T5 &#124; Operations in Corsica &#124; 0.9% &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 130 | &#124; T6 &#124; Operations in continental France at the particular rate &#124; 2.1% &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 131 | &#124; P1 &#124; Petroleum products, standard rate &#124; 20% &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 132 | &#124; P2 &#124; Petroleum products, reduced rate &#124; 13% &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 133 | &#124; I1 &#124; Importations, standard rate: base and tax on imports other than petroleum products &#124; 20% &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 134 | &#124; I2 &#124; Importations, intermediate rate &#124; 10% &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 135 | &#124; I3 &#124; Importations, overseas standard rate &#124; 8.5% &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 136 | &#124; I4 &#124; Importations, reduced rate &#124; 5.5% &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 137 | &#124; I5 &#124; Importations, particular rate &#124; 2.1% &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 138 | &#124; I6 &#124; Importations, overseas particular rate &#124; 1.05% &#124; | ## The taxable base nativeLF122; ## The taxable base nativeLF123; ## The taxable base nativeLF124; ## Rates, bands and thresholds nativeLF57 | Retained / corrected in current Guide: Each old territorial/petroleum/import rate remains in the actual2026form-rate groups. Only recognition/form mapping is claimed; territorial eligibility stays outside scope. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 140 | **CA12 lines, from the 2026 return** | ## The taxable base nativeLF145; ## Rates, bands and thresholds nativeLF73 | Retained CA12 method; selected2026notice nowread, fullnotice audit notclaimed: CA12 numbering, instalment base57, refund150 and carry/offset exceptions retained; Selected2026CA12notice nowread underFR-L44 supplies actualline24/AE/30/57 andrefund150instructions. The old full intermediate AE/5B/25 breakdown remains in this origin record and actualformsource; no exhaustive specialbranch noticeauditclaimed. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 142 | The CA12 has its own numbering and it is not the CA3's. Frame A carries the operations, then: line 5A standard rate mainland, line 5B standard rate on petroleum products, line 06 reduced rate, line 6C intermediate rate, line 07 standard rate in the overseas departments. On the deduction side, line 20 carries deductions on invoices, line 21 the flat-rate deduction for general expenses, and line 22 is the total of lines 20 and 21 only. Line 23 is the VAT deductible on fixed assets, line 24 the credit carried in from the start of the year, and line 26 is the total deductible VAT, the sum of lines 22, 23, 24, 25 and AE. Line 19 is the total gross VAT due. Line 28 is the VAT due, line 19 less line 26; line 29 is the credit, line 26 less line 19; line 30 records the instalments paid and still owed. The base for next year's instalments is at line 57: line 16 less lines 11, 12 and 22, so it is struck before the VAT on fixed assets at line 23 and before any credit. The form and its completion notes are the authority for this: https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5291.pdf and https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5424.pdf | ## The taxable base nativeLF145; ## Rates, bands and thresholds nativeLF73 | Retained CA12 method; selected2026notice nowread, fullnotice audit notclaimed: CA12 numbering, instalment base57, refund150 and carry/offset exceptions retained; Selected2026CA12notice nowread underFR-L44 supplies actualline24/AE/30/57 andrefund150instructions. The old full intermediate AE/5B/25 breakdown remains in this origin record and actualformsource; no exhaustive specialbranch noticeauditclaimed. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 144 | &#124; What &#124; Value &#124; Note &#124; | ## The taxable base nativeLF145; ## Rates, bands and thresholds nativeLF73 | Retained CA12 method; selected2026notice nowread, fullnotice audit notclaimed: CA12 numbering, instalment base57, refund150 and carry/offset exceptions retained; Selected2026CA12notice nowread underFR-L44 supplies actualline24/AE/30/57 andrefund150instructions. The old full intermediate AE/5B/25 breakdown remains in this origin record and actualformsource; no exhaustive specialbranch noticeauditclaimed. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 145 | &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF145; ## Rates, bands and thresholds nativeLF73 | Retained CA12 method; selected2026notice nowread, fullnotice audit notclaimed: CA12 numbering, instalment base57, refund150 and carry/offset exceptions retained; Selected2026CA12notice nowread underFR-L44 supplies actualline24/AE/30/57 andrefund150instructions. The old full intermediate AE/5B/25 breakdown remains in this origin record and actualformsource; no exhaustive specialbranch noticeauditclaimed. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 146 | &#124; Source &#124; all figures below &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5424.pdf &#124; | ## The taxable base nativeLF145; ## Rates, bands and thresholds nativeLF73 | Retained CA12 method; selected2026notice nowread, fullnotice audit notclaimed: CA12 numbering, instalment base57, refund150 and carry/offset exceptions retained; Selected2026CA12notice nowread underFR-L44 supplies actualline24/AE/30/57 andrefund150instructions. The old full intermediate AE/5B/25 breakdown remains in this origin record and actualformsource; no exhaustive specialbranch noticeauditclaimed. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 147 | &#124; CA12: a refund of the overpaid instalments (line 34) and of the credit shown (line 29) may be asked for in frame VII where the amount is at least this &#124; EUR 150 &#124; "du crédit dégagé (ligne 29) s’il est supérieur ou égal à 150 euros" &#124; | ## The taxable base nativeLF145; ## Rates, bands and thresholds nativeLF73 | Retained CA12 method; selected2026notice nowread, fullnotice audit notclaimed: CA12 numbering, instalment base57, refund150 and carry/offset exceptions retained; Selected2026CA12notice nowread underFR-L44 supplies actualline24/AE/30/57 andrefund150instructions. The old full intermediate AE/5B/25 breakdown remains in this origin record and actualformsource; no exhaustive specialbranch noticeauditclaimed. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 149 | Below that amount the credit is refundable on the return only in the three cases frame VII of the form names, "uniquement en cas de cession", death, or entry into a VAT group, "entrée dans un groupe TVA". Otherwise it is carried to line 24 of the next return through line 51, which the form captions "Crédit à reporter", or set against the next instalment through line 52, "Crédit imputé sur les prochains acomptes"; the notes say you may "imputer sur votre prochain acompte". | ## The taxable base nativeLF145; ## Rates, bands and thresholds nativeLF73 | Retained CA12 method; selected2026notice nowread, fullnotice audit notclaimed: CA12 numbering, instalment base57, refund150 and carry/offset exceptions retained; Selected2026CA12notice nowread underFR-L44 supplies actualline24/AE/30/57 andrefund150instructions. The old full intermediate AE/5B/25 breakdown remains in this origin record and actualformsource; no exhaustive specialbranch noticeauditclaimed. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 151 | **Conservative defaults, France-specific values** | ## The taxable base nativeLF172 | Corrected unsafe default; actual question retained: All eight old unknown-fact branches explicitly superseded by FR-L34 fact gathering/evidence hold. No default20/France/consumer/A3/scope or permanent denial follows from missing facts alone. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 153 | &#124; Ambiguity &#124; Default &#124; | ## The taxable base nativeLF172 | Corrected unsafe default; actual question retained: All eight old unknown-fact branches explicitly superseded by FR-L34 fact gathering/evidence hold. No default20/France/consumer/A3/scope or permanent denial follows from missing facts alone. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 154 | &#124; --- &#124; --- &#124; | ## The taxable base nativeLF172 | Corrected unsafe default; actual question retained: All eight old unknown-fact branches explicitly superseded by FR-L34 fact gathering/evidence hold. No default20/France/consumer/A3/scope or permanent denial follows from missing facts alone. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 155 | &#124; Unknown rate on a sale &#124; The standard rate in the rate table above &#124; | ## The taxable base nativeLF172 | Corrected unsafe default; actual question retained: All eight old unknown-fact branches explicitly superseded by FR-L34 fact gathering/evidence hold. No default20/France/consumer/A3/scope or permanent denial follows from missing facts alone. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 156 | &#124; Unknown VAT status of a purchase &#124; Not deductible &#124; | ## The taxable base nativeLF172 | Corrected unsafe default; actual question retained: All eight old unknown-fact branches explicitly superseded by FR-L34 fact gathering/evidence hold. No default20/France/consumer/A3/scope or permanent denial follows from missing facts alone. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 157 | &#124; Unknown counterparty country &#124; Domestic France &#124; | ## The taxable base nativeLF172 | Corrected unsafe default; actual question retained: All eight old unknown-fact branches explicitly superseded by FR-L34 fact gathering/evidence hold. No default20/France/consumer/A3/scope or permanent denial follows from missing facts alone. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 158 | &#124; Unknown business or consumer status for an EU customer &#124; Consumer, charge French VAT at the applicable rate &#124; | ## The taxable base nativeLF172 | Corrected unsafe default; actual question retained: All eight old unknown-fact branches explicitly superseded by FR-L34 fact gathering/evidence hold. No default20/France/consumer/A3/scope or permanent denial follows from missing facts alone. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 159 | &#124; Unknown business-use proportion (vehicle, phone, home office) &#124; No recovery &#124; | ## The taxable base nativeLF172 | Corrected unsafe default; actual question retained: All eight old unknown-fact branches explicitly superseded by FR-L34 fact gathering/evidence hold. No default20/France/consumer/A3/scope or permanent denial follows from missing facts alone. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 160 | &#124; Unknown SaaS billing entity &#124; Self-assessment on a service bought from a supplier not established in France, line A3 &#124; | ## The taxable base nativeLF172 | Corrected unsafe default; actual question retained: All eight old unknown-fact branches explicitly superseded by FR-L34 fact gathering/evidence hold. No default20/France/consumer/A3/scope or permanent denial follows from missing facts alone. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 161 | &#124; Unknown blocked-input status (accommodation for staff, personal use) &#124; Blocked &#124; | ## The taxable base nativeLF172 | Corrected unsafe default; actual question retained: All eight old unknown-fact branches explicitly superseded by FR-L34 fact gathering/evidence hold. No default20/France/consumer/A3/scope or permanent denial follows from missing facts alone. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 162 | &#124; Unknown whether a transaction is in scope &#124; In scope &#124; | ## The taxable base nativeLF172 | Corrected unsafe default; actual question retained: All eight old unknown-fact branches explicitly superseded by FR-L34 fact gathering/evidence hold. No default20/France/consumer/A3/scope or permanent denial follows from missing facts alone. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 164 | **Red flags to raise with the reviewer** | ## The taxable base nativeLF200 | Retained / corrected in current Guide: All five qualitative flag concepts retained as internal review practice, with no invented monetary threshold or statutory tax result. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 166 | No official page sets money trip points for a review. The numeric thresholds carried by earlier versions of this skill were house values with no source, and they have been removed. Raise these as flags and let the reviewing accountant set the amounts for the client: | ## The taxable base nativeLF200 | Retained / corrected in current Guide: All five qualitative flag concepts retained as internal review practice, with no invented monetary threshold or statutory tax result. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 168 | &#124; Flag &#124; Trigger &#124; | ## The taxable base nativeLF200 | Retained / corrected in current Guide: All five qualitative flag concepts retained as internal review practice, with no invented monetary threshold or statutory tax result. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 169 | &#124; --- &#124; --- &#124; | ## The taxable base nativeLF200 | Retained / corrected in current Guide: All five qualitative flag concepts retained as internal review practice, with no invented monetary threshold or statutory tax result. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 170 | &#124; HIGH single-transaction size &#124; A transaction large against the period's turnover, or the largest few transactions of the period &#124; | ## The taxable base nativeLF200 | Retained / corrected in current Guide: All five qualitative flag concepts retained as internal review practice, with no invented monetary threshold or statutory tax result. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 171 | &#124; HIGH tax delta on a single conservative default &#124; A default that, if wrong, changes the VAT position materially &#124; | ## The taxable base nativeLF200 | Retained / corrected in current Guide: All five qualitative flag concepts retained as internal review practice, with no invented monetary threshold or statutory tax result. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 172 | &#124; MEDIUM counterparty concentration &#124; One counterparty dominating either the output or the input side &#124; | ## The taxable base nativeLF200 | Retained / corrected in current Guide: All five qualitative flag concepts retained as internal review practice, with no invented monetary threshold or statutory tax result. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 173 | &#124; MEDIUM conservative-default count &#124; Several defaults used across one return &#124; | ## The taxable base nativeLF200 | Retained / corrected in current Guide: All five qualitative flag concepts retained as internal review practice, with no invented monetary threshold or statutory tax result. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 174 | &#124; LOW absolute net VAT position &#124; A net position large enough that a repayment claim or a payment plan is in question &#124; | ## The taxable base nativeLF200 | Retained / corrected in current Guide: All five qualitative flag concepts retained as internal review practice, with no invented monetary threshold or statutory tax result. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 176 | ## The method, step by step | ## Who this applies to nativeLF38; ## Deadlines and filing nativeLF210; ## The taxable base nativeLF174; ## The taxable base nativeLF156; ## The taxable base nativeLF208; ## Who this applies to nativeLF41; ## Who this applies to nativeLF44; ## Who this applies to nativeLF45; ## Rates, bands and thresholds nativeLF90; ## The taxable base nativeLF98; ## The taxable base nativeLF154; ## The taxable base nativeLF159; ## The taxable base nativeLF160; ## The taxable base nativeLF161; ## The taxable base nativeLF162; ## The taxable base nativeLF163; ## The taxable base nativeLF164; ## The taxable base nativeLF165; ## The taxable base nativeLF166; ## The taxable base nativeLF167; ## The taxable base nativeLF168; ## The taxable base nativeLF169; ## The taxable base nativeLF170; ## Deadlines and filing nativeLF214; ## Deadlines and filing nativeLF216; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF221; ## Deadlines and filing nativeLF222 | Retained / corrected in current Guide: All six workflow steps retained across regime/date/classification/deduction/return-statements/payment sections; classifier is conditional, not authoritative tax proof. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 178 | 1. **Settle the regime and the frequency before anything else.** Compare the previous year's turnover and the previous year's VAT due against the limits in the regime table below, taken from https://entreprendre.service-public.gouv.fr/vosdroits/F23566 . A business inside the franchise en base files no VAT return at all. A business in the régime réel simplifié files one CA12 a year plus two instalments. A business in the régime réel normal files a CA3 every month, or every quarter where the VAT payable each year is below the quarterly limit in that table. | ## Who this applies to nativeLF38; ## Deadlines and filing nativeLF210; ## The taxable base nativeLF174; ## The taxable base nativeLF156; ## The taxable base nativeLF208; ## Who this applies to nativeLF41; ## Who this applies to nativeLF44; ## Who this applies to nativeLF45; ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF90; ## Deadlines and filing nativeLF215; ## Deadlines and filing nativeLF218; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All six workflow steps retained across regime/date/classification/deduction/return-statements/payment sections; classifier is conditional, not authoritative tax proof. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 179 | 2. **Find the filing date for this particular taxpayer.** There is no single national CA3 date. The DGFiP page https://www.impots.gouv.fr/le-regime-reel-normal-dates-limites-de-transmission-des-ca3 asks three questions in order: the department the business sits in (Paris, Hauts-de-Seine, Seine-Saint-Denis and Val-de-Marne on one side, all other departments on the other), the category of business (entreprise individuelle, any company other than a société anonyme, société anonyme, or other taxpayer such as a local authority or an association), and then, depending on that category, either the first letter of the operator's name or the range the SIREN number falls in. The taxpayer's own date is shown in their espace professionnel. The service-public page gives the outer window for the régime réel normal: "la déclaration doit être effectuée entre le 15 et le 24 du mois suivant le fait générateur" (https://entreprendre.service-public.gouv.fr/vosdroits/F23566). | ## Who this applies to nativeLF38; ## Deadlines and filing nativeLF210; ## The taxable base nativeLF174; ## The taxable base nativeLF156; ## The taxable base nativeLF208; ## Deadlines and filing nativeLF214 | Retained / corrected in current Guide: All six workflow steps retained across regime/date/classification/deduction/return-statements/payment sections; classifier is conditional, not authoritative tax proof. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 180 | 3. **Classify every line of the period.** Run the supplier pattern library in Section 3 first, then the Tier 1 rules in Section 5, then the Tier 2 questions in Section 6. Map each classified transaction to a line of the 2026 CA3 using the line table above, which is read off https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf . Purchases of services from a supplier not established in France go to line A3 under CGI art. 283-2; goods and services from a taxable person not established in France go to line B4 under CGI art. 283-1; intra-EU acquisitions of goods go to line B2. | ## Who this applies to nativeLF38; ## Deadlines and filing nativeLF210; ## The taxable base nativeLF174; ## The taxable base nativeLF156; ## The taxable base nativeLF208; ## The taxable base nativeLF105; ## The taxable base nativeLF106; ## The taxable base nativeLF107; ## The taxable base nativeLF108; ## The taxable base nativeLF109; ## The taxable base nativeLF110; ## The taxable base nativeLF111; ## The taxable base nativeLF149; ## The taxable base nativeLF150 | Retained / corrected in current Guide: All six workflow steps retained across regime/date/classification/deduction/return-statements/payment sections; classifier is conditional, not authoritative tax proof. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 181 | 4. **Check the deduction restrictions before claiming any input VAT.** Passenger vehicles (https://bofip.impots.gouv.fr/bofip/1192-PGP.html), fuel (https://bofip.impots.gouv.fr/bofip/1194-PGP.html), accommodation for directors and staff (https://bofip.impots.gouv.fr/bofip/1190-PGP.html) and goods given away (https://bofip.impots.gouv.fr/bofip/1196-PGP.html) each have their own rule, set out in Section 5.12. | ## Who this applies to nativeLF38; ## Deadlines and filing nativeLF210; ## The taxable base nativeLF174; ## The taxable base nativeLF156; ## The taxable base nativeLF208; ## The taxable base nativeLF159; ## The taxable base nativeLF160; ## The taxable base nativeLF161; ## The taxable base nativeLF162; ## The taxable base nativeLF163; ## The taxable base nativeLF164; ## The taxable base nativeLF165; ## The taxable base nativeLF166; ## The taxable base nativeLF167; ## The taxable base nativeLF168; ## The taxable base nativeLF169; ## The taxable base nativeLF170 | Retained / corrected in current Guide: All six workflow steps retained across regime/date/classification/deduction/return-statements/payment sections; classifier is conditional, not authoritative tax proof. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 182 | 5. **File the return and the companion statements.** The CA3 and the CA12 are filed online in the espace professionnel on https://www.impots.gouv.fr . Intra-EU supplies of goods also require an état récapitulatif des clients filed with the customs administration under CGI art. 289 B, and intra-EU services require a déclaration européenne de services under CGI art. 289 B-III, both "dans les dix jours ouvrables qui suivent le mois" in which the tax became due, through the customs portal (https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf). | ## Who this applies to nativeLF38; ## Deadlines and filing nativeLF210; ## The taxable base nativeLF174; ## The taxable base nativeLF156; ## The taxable base nativeLF208; ## Deadlines and filing nativeLF221; ## Deadlines and filing nativeLF222; ## Cross-border points nativeLF252; ## Cross-border points nativeLF253; ## Cross-border points nativeLF254 | Retained / corrected in current Guide: All six workflow steps retained across regime/date/classification/deduction/return-statements/payment sections; classifier is conditional, not authoritative tax proof. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 183 | 6. **Pay.** Under the régime réel normal, payment is made with the return, monthly or quarterly. Under the régime réel simplifié, the two instalments and the balance follow the percentages and dates in the regime table below (https://entreprendre.service-public.gouv.fr/vosdroits/F23566). | ## Who this applies to nativeLF38; ## Deadlines and filing nativeLF210; ## The taxable base nativeLF174; ## The taxable base nativeLF156; ## The taxable base nativeLF208; ## Deadlines and filing nativeLF216; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF222 | Retained / corrected in current Guide: All six workflow steps retained across regime/date/classification/deduction/return-statements/payment sections; classifier is conditional, not authoritative tax proof. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 185 | ## Section 2: Required inputs and refusal catalogue | ## The taxable base nativeLF202; ## The taxable base nativeLF204; ## The taxable base nativeLF198 | Retained / corrected in current Guide: Minimum/recommended/ideal bank/invoice/identity/prior-return input topics and reviewer warning retained. FR-L35 corrects150invoice omission scope using actual242noniesAII, rather than old seller-only claim. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 187 | ### Required inputs | ## The taxable base nativeLF202; ## The taxable base nativeLF204; ## The taxable base nativeLF198 | Retained / corrected in current Guide: Minimum/recommended/ideal bank/invoice/identity/prior-return input topics and reviewer warning retained. FR-L35 corrects150invoice omission scope using actual242noniesAII, rather than old seller-only claim. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 189 | **Minimum viable**: a bank statement for the period in CSV, PDF, or pasted text. It must cover the full period. Acceptable from any French or international business bank: BNP Paribas, Société Générale, Crédit Agricole, LCL, Banque Populaire, Caisse d'Épargne, La Banque Postale, CIC, Revolut Business, Wise Business, N26 Business, Qonto, or any other. | ## The taxable base nativeLF202; ## The taxable base nativeLF204; ## The taxable base nativeLF198 | Retained / corrected in current Guide: Minimum/recommended/ideal bank/invoice/identity/prior-return input topics and reviewer warning retained. FR-L35 corrects150invoice omission scope using actual242noniesAII, rather than old seller-only claim. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 191 | **Recommended**: sales invoices for the period (especially for intra-EU business-to-business services and zero-rated supplies), purchase invoices for input VAT claims, and the client's TVA number in writing (FR plus two check digits plus the nine-digit SIREN). | ## The taxable base nativeLF202; ## The taxable base nativeLF204; ## The taxable base nativeLF198 | Retained / corrected in current Guide: Minimum/recommended/ideal bank/invoice/identity/prior-return input topics and reviewer warning retained. FR-L35 corrects150invoice omission scope using actual242noniesAII, rather than old seller-only claim. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 193 | **Ideal**: a complete invoice register (compatible with the fichier des écritures comptables), the SIRET number, the prior period CA3, and a reconciliation of the credit carried forward at line 22. | ## The taxable base nativeLF202; ## The taxable base nativeLF204; ## The taxable base nativeLF198 | Retained / corrected in current Guide: Minimum/recommended/ideal bank/invoice/identity/prior-return input topics and reviewer warning retained. FR-L35 corrects150invoice omission scope using actual242noniesAII, rather than old seller-only claim. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 195 | **What an invoice must carry** | ## The taxable base nativeLF202; ## The taxable base nativeLF204; ## The taxable base nativeLF198 | Retained / corrected in current Guide: Minimum/recommended/ideal bank/invoice/identity/prior-return input topics and reviewer warning retained. FR-L35 corrects150invoice omission scope using actual242noniesAII, rather than old seller-only claim. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 197 | &#124; What &#124; Value &#124; Note &#124; | ## The taxable base nativeLF202; ## The taxable base nativeLF204; ## The taxable base nativeLF198 | Retained / corrected in current Guide: Minimum/recommended/ideal bank/invoice/identity/prior-return input topics and reviewer warning retained. FR-L35 corrects150invoice omission scope using actual242noniesAII, rather than old seller-only claim. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 198 | &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF202; ## The taxable base nativeLF204; ## The taxable base nativeLF198 | Retained / corrected in current Guide: Minimum/recommended/ideal bank/invoice/identity/prior-return input topics and reviewer warning retained. FR-L35 corrects150invoice omission scope using actual242noniesAII, rather than old seller-only claim. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 199 | &#124; Source &#124; all figures below &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F31808 &#124; | ## The taxable base nativeLF202; ## The taxable base nativeLF204; ## The taxable base nativeLF198 | Retained / corrected in current Guide: Minimum/recommended/ideal bank/invoice/identity/prior-return input topics and reviewer warning retained. FR-L35 corrects150invoice omission scope using actual242noniesAII, rather than old seller-only claim. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 200 | &#124; Total excluding VAT at or below this amount: the seller's VAT identification number is not a required particular &#124; EUR 150 &#124; "Sauf pour les factures d'un montant total HT inférieur ou égal à 150 €" &#124; | ## The taxable base nativeLF202; ## The taxable base nativeLF204; ## The taxable base nativeLF198 | Retained / corrected in current Guide: Minimum/recommended/ideal bank/invoice/identity/prior-return input topics and reviewer warning retained. FR-L35 corrects150invoice omission scope using actual242noniesAII, rather than old seller-only claim. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 202 | Earlier versions of this skill described that limit as a general "facture simplifiée" relief. It is not. The page makes it an exception to one particular only, the VAT identification number. Every other mandatory particular still applies below that amount. The same page gives the wording a seller inside the franchise must use, "TVA non applicable, art. 293 B du code général des impôts", and the wording where the customer is the person liable for the tax, "Auto-liquidation". | ## The taxable base nativeLF202; ## The taxable base nativeLF204; ## The taxable base nativeLF198 | Retained / corrected in current Guide: Minimum/recommended/ideal bank/invoice/identity/prior-return input topics and reviewer warning retained. FR-L35 corrects150invoice omission scope using actual242noniesAII, rather than old seller-only claim. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 204 | **Refusal policy if the minimum is missing: SOFT WARN.** If no bank statement is available at all, hard stop. If a bank statement only, with no invoices, proceed but record in the reviewer brief: "This return was produced from a bank statement alone. The reviewer must verify, before approval, that input VAT claims are supported by compliant tax invoices (factures), that the exception for the VAT identification number on small invoices has not been read as a wider relief, and that all reverse-charge classifications match the supplier's invoice." | ## The taxable base nativeLF202; ## The taxable base nativeLF204; ## The taxable base nativeLF198 | Retained / corrected in current Guide: Minimum/recommended/ideal bank/invoice/identity/prior-return input topics and reviewer warning retained. FR-L35 corrects150invoice omission scope using actual242noniesAII, rather than old seller-only claim. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 206 | ### France-specific refusal catalogue | ## Who this applies to nativeLF46; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: All eight French referral subjects retained: franchise withoutoption, mixedexemption, margin, property, VATgroup, fiscalrepresentative, DOM, income-tax sibling. Exact former message labels are operational wording, not a new professional legal gate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 208 | These refusals apply on top of the EU-wide refusals in `eu-vat-directive` Section 13 (R-EU-1 through R-EU-12). If any trigger fires, stop, output the refusal message verbatim, end the conversation. | ## Who this applies to nativeLF46; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: All eight French referral subjects retained: franchise withoutoption, mixedexemption, margin, property, VATgroup, fiscalrepresentative, DOM, income-tax sibling. Exact former message labels are operational wording, not a new professional legal gate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 210 | - **R-FR-1: Micro-entreprise and franchise en base de TVA.** Trigger: the client is under the franchise en base on the thresholds in the franchise table below and has not opted for VAT. Message: "A business inside the franchise en base de TVA does not charge VAT and does not deduct it. It files no CA3 and no CA12. This skill cannot prepare a return for a business inside the franchise. If you have opted for VAT (option pour la TVA), please confirm and provide your FR TVA number." _(R-FR-1)_ | ## Who this applies to nativeLF46; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: All eight French referral subjects retained: franchise withoutoption, mixedexemption, margin, property, VATgroup, fiscalrepresentative, DOM, income-tax sibling. Exact former message labels are operational wording, not a new professional legal gate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 211 | - **R-FR-2: Partial exemption (prorata de déduction).** Trigger: the client makes both taxable supplies and exempt-without-credit supplies (financial, medical, educational, insurance) and the exempt proportion is not de minimis. Message: "You make both taxable and exempt supplies. Your input VAT must be apportioned under the coefficient de déduction rules (Articles 206 to 214 of Annexe II to the CGI). Please use a qualified expert-comptable to determine the coefficient before input VAT is claimed." _(R-FR-2, Articles 206 to 214 of Annexe II to the CGI)_ | ## Who this applies to nativeLF46; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: All eight French referral subjects retained: franchise withoutoption, mixedexemption, margin, property, VATgroup, fiscalrepresentative, DOM, income-tax sibling. Exact former message labels are operational wording, not a new professional legal gate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 212 | - **R-FR-3: Margin scheme (régime de la marge).** Trigger: the client deals in second-hand goods, art, antiques, or collectables under the margin scheme. Message: "Margin scheme transactions (TVA sur la marge) require transaction-level margin computation. Out of scope for this skill." _(R-FR-3)_ | ## Who this applies to nativeLF46; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: All eight French referral subjects retained: franchise withoutoption, mixedexemption, margin, property, VATgroup, fiscalrepresentative, DOM, income-tax sibling. Exact former message labels are operational wording, not a new professional legal gate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 213 | - **R-FR-4: Real estate (TVA immobilière).** Trigger: the client deals in new construction, building land, or property transactions subject to TVA immobilière. Message: "Real estate VAT (TVA immobilière) is complex and fact-specific. Out of scope for this skill. Please consult an expert-comptable." _(R-FR-4)_ | ## Who this applies to nativeLF46; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: All eight French referral subjects retained: franchise withoutoption, mixedexemption, margin, property, VATgroup, fiscalrepresentative, DOM, income-tax sibling. Exact former message labels are operational wording, not a new professional legal gate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 214 | - **R-FR-5: VAT group (assujetti unique).** Trigger: the client is part of a VAT group under Article 256 C of the CGI. Message: "VAT groups require consolidation across the group, and internal operations between members go on their own CA3 line. Out of scope." _(R-FR-5, Article 256 C of the CGI)_ | ## Who this applies to nativeLF46; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: All eight French referral subjects retained: franchise withoutoption, mixedexemption, margin, property, VATgroup, fiscalrepresentative, DOM, income-tax sibling. Exact former message labels are operational wording, not a new professional legal gate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 215 | - **R-FR-6: Fiscal representative.** Trigger: a non-resident supplier or client with a fiscal representative in France. Message: "Non-resident registrations with fiscal representatives have specific obligations beyond this skill. Please use a qualified comptable." _(R-FR-6)_ | ## Who this applies to nativeLF46; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: All eight French referral subjects retained: franchise withoutoption, mixedexemption, margin, property, VATgroup, fiscalrepresentative, DOM, income-tax sibling. Exact former message labels are operational wording, not a new professional legal gate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 216 | - **R-FR-7: Overseas departments filing.** Trigger: the client is based in an overseas department or territory (Guadeloupe, Martinique, Réunion, Guyane, Mayotte). Message: "The overseas departments have their own rates, which are in the rate table in Section 1, and VAT is provisionally not applicable in Guyane and Mayotte. Classification, the local rate structure and the exchanges between the departments are outside this skill, which covers metropolitan France. Please use a local expert-comptable." _(R-FR-7)_ | ## Who this applies to nativeLF46; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: All eight French referral subjects retained: franchise withoutoption, mixedexemption, margin, property, VATgroup, fiscalrepresentative, DOM, income-tax sibling. Exact former message labels are operational wording, not a new professional legal gate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 217 | - **R-FR-8: Income tax instead of VAT.** Trigger: the user asks about annual income tax (impôt sur le revenu, impôt sur les sociétés, BNC, BIC) instead of TVA. Message: "This skill only handles French VAT returns. For income tax, use a dedicated French income tax skill such as `fr-income-tax` or `fr-personal-income-tax`." _(R-FR-8)_ | ## Who this applies to nativeLF46; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: All eight French referral subjects retained: franchise withoutoption, mixedexemption, margin, property, VATgroup, fiscalrepresentative, DOM, income-tax sibling. Exact former message labels are operational wording, not a new professional legal gate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 219 | ## Ask the client first | ## Ask the client first nativeLF323; ## The taxable base nativeLF196; ## The taxable base nativeLF202 | Retained / corrected in current Guide: Regime/turnover/VAT, exactdate, foreignsale status, landlord option, vehicle design and prior27credit questions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 221 | - Which regime are you in, and what was last year's turnover and last year's VAT due? Both numbers decide the regime, and the VAT figure alone can move a business to the régime réel normal whatever its turnover. | ## Ask the client first nativeLF323; ## The taxable base nativeLF196; ## The taxable base nativeLF202 | Retained / corrected in current Guide: Regime/turnover/VAT, exactdate, foreignsale status, landlord option, vehicle design and prior27credit questions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 222 | - What is the exact filing date shown in your espace professionnel this month? The date depends on the department, the category of business and the SIREN or the operator's name, so it cannot be guessed. | ## Ask the client first nativeLF323; ## The taxable base nativeLF196; ## The taxable base nativeLF202 | Retained / corrected in current Guide: Regime/turnover/VAT, exactdate, foreignsale status, landlord option, vehicle design and prior27credit questions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 223 | - Do you sell to customers outside France? For each: business or consumer, goods or services, and which country. That decides lines E1, E2, E3 and F2, and whether an état récapitulatif or a déclaration européenne de services is due. | ## Ask the client first nativeLF323; ## The taxable base nativeLF196; ## The taxable base nativeLF202 | Retained / corrected in current Guide: Regime/turnover/VAT, exactdate, foreignsale status, landlord option, vehicle design and prior27credit questions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 224 | - Has the landlord of any property you rent exercised the option for VAT? Commercial rent carries VAT only if the option was made. | ## Ask the client first nativeLF323; ## The taxable base nativeLF196; ## The taxable base nativeLF202 | Retained / corrected in current Guide: Regime/turnover/VAT, exactdate, foreignsale status, landlord option, vehicle design and prior27credit questions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 225 | - For any vehicle: was it designed to carry people or to carry goods? The exclusion turns on how the vehicle was designed, not on how it is used. | ## Ask the client first nativeLF323; ## The taxable base nativeLF196; ## The taxable base nativeLF202 | Retained / corrected in current Guide: Regime/turnover/VAT, exactdate, foreignsale status, landlord option, vehicle design and prior27credit questions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 226 | - Do you have a credit de TVA from the prior period, and what was the figure at line 27 of the last return? It has to be brought forward at line 22. | ## Ask the client first nativeLF323; ## The taxable base nativeLF196; ## The taxable base nativeLF202 | Retained / corrected in current Guide: Regime/turnover/VAT, exactdate, foreignsale status, landlord option, vehicle design and prior27credit questions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 228 | ## When to refuse or refer | ## Ask the client first nativeLF332; ## Deadlines and filing nativeLF219; ## Deadlines and filing nativeLF230; ## The taxable base nativeLF152; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: Referrals for every named domain and regime crossing retained. Old assertion that this Guide contains no penalty/interest method is superseded by the source-bound current table and example, with audit procedure delegated tofr-tax-audit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 230 | - Refuse when any of R-FR-1 through R-FR-8 fires, or any of R-EU-1 through R-EU-12 in `eu-vat-directive`. | ## Ask the client first nativeLF332; ## Deadlines and filing nativeLF219; ## Deadlines and filing nativeLF230; ## The taxable base nativeLF152; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: Referrals for every named domain and regime crossing retained. Old assertion that this Guide contains no penalty/interest method is superseded by the source-bound current table and example, with audit procedure delegated tofr-tax-audit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 231 | - Refer when the client makes exempt supplies that are not de minimis: the coefficient de déduction is an expert-comptable's job. | ## Ask the client first nativeLF332; ## Deadlines and filing nativeLF219; ## Deadlines and filing nativeLF230; ## The taxable base nativeLF152; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: Referrals for every named domain and regime crossing retained. Old assertion that this Guide contains no penalty/interest method is superseded by the source-bound current table and example, with audit procedure delegated tofr-tax-audit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 232 | - Refer when the business is in the régime réel simplifié and its VAT due for the previous year crossed the VAT limit in the regime table: it must file monthly CA3 returns instead, and the changeover needs checking against the tax office's own record. | ## Ask the client first nativeLF332; ## Deadlines and filing nativeLF219; ## Deadlines and filing nativeLF230; ## The taxable base nativeLF152; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: Referrals for every named domain and regime crossing retained. Old assertion that this Guide contains no penalty/interest method is superseded by the source-bound current table and example, with audit procedure delegated tofr-tax-audit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 233 | - Refer when a turnover ceiling was crossed during the year. Crossing a current-year ceiling throws the business into the régime réel normal retroactively from 1 January of the year of the overrun, and returns already filed have to be redone. | ## Ask the client first nativeLF332; ## Deadlines and filing nativeLF219; ## Deadlines and filing nativeLF230; ## The taxable base nativeLF152; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: Referrals for every named domain and regime crossing retained. Old assertion that this Guide contains no penalty/interest method is superseded by the source-bound current table and example, with audit procedure delegated tofr-tax-audit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 234 | - Refer when the client deals in petroleum products, energy, greenhouse gas quotas, electronic communications services or construction subcontracting: each has its own domestic reverse charge and its own CA3 line. | ## Ask the client first nativeLF332; ## Deadlines and filing nativeLF219; ## Deadlines and filing nativeLF230; ## The taxable base nativeLF152; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: Referrals for every named domain and regime crossing retained. Old assertion that this Guide contains no penalty/interest method is superseded by the source-bound current table and example, with audit procedure delegated tofr-tax-audit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 235 | - Do not answer a question about the overseas departments, about property VAT, about the margin scheme, or about a VAT group from this skill. | ## Ask the client first nativeLF332; ## Deadlines and filing nativeLF219; ## Deadlines and filing nativeLF230; ## The taxable base nativeLF152; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: Referrals for every named domain and regime crossing retained. Old assertion that this Guide contains no penalty/interest method is superseded by the source-bound current table and example, with audit procedure delegated tofr-tax-audit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 236 | - Do not compute a penalty or an interest figure from this skill. It carries none. | ## Ask the client first nativeLF332; ## Deadlines and filing nativeLF219; ## Deadlines and filing nativeLF230; ## The taxable base nativeLF152; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: Referrals for every named domain and regime crossing retained. Old assertion that this Guide contains no penalty/interest method is superseded by the source-bound current table and example, with audit procedure delegated tofr-tax-audit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 238 | **The franchise en base de TVA and its boundaries** | ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF75; ## Who this applies to nativeLF42; ## Cross-border points nativeLF259; ## Rates, bands and thresholds nativeLF90 | Retained / corrected in current Guide: All old franchise thresholds retained with actual current law. Old EU100k France-excluded wording corrected to EU-wide actualscope and15WORKINGdays; acquisition10k is a different gate. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 240 | The franchise page below is stamped "Vérifié le 01 janvier 2026" and was read again on 19 October 2026 with no change to its rules. It says in terms: "Pour l’année 2026 , les seuils de franchise en base de TVA française applicables restent inchangés". Each threshold is a test on turnover excluding VAT, "inférieur ou égal" to the amount, and each activity has two: a basic threshold on the previous calendar year and a higher tolerance threshold on the current year. | ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF75; ## Who this applies to nativeLF42; ## Cross-border points nativeLF259; ## Rates, bands and thresholds nativeLF90 | Retained / corrected in current Guide: All old franchise thresholds retained with actual current law. Old EU100k France-excluded wording corrected to EU-wide actualscope and15WORKINGdays; acquisition10k is a different gate. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 242 | &#124; Threshold &#124; Amount &#124; What crossing it does &#124; | ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF75; ## Who this applies to nativeLF42; ## Cross-border points nativeLF259; ## Rates, bands and thresholds nativeLF90 | Retained / corrected in current Guide: All old franchise thresholds retained with actual current law. Old EU100k France-excluded wording corrected to EU-wide actualscope and15WORKINGdays; acquisition10k is a different gate. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 243 | &#124; --- &#124; --- &#124; --- &#124; | ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF75; ## Who this applies to nativeLF42; ## Cross-border points nativeLF259 | Retained / corrected in current Guide: All old franchise thresholds retained with actual current law. Old EU100k France-excluded wording corrected to EU-wide actualscope and15WORKINGdays; acquisition10k is a different gate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 244 | &#124; Source &#124; all figures below &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F21746 &#124; | ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF75; ## Who this applies to nativeLF42; ## Cross-border points nativeLF259 | Retained / corrected in current Guide: All old franchise thresholds retained with actual current law. Old EU100k France-excluded wording corrected to EU-wide actualscope and15WORKINGdays; acquisition10k is a different gate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 245 | &#124; Goods and accommodation, turnover of the previous calendar year &#124; EUR 85,000 &#124; Above it: "elle est soumise à la TVA dès le 1 er janvier de l'année suivante" &#124; | ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF75; ## Who this applies to nativeLF42; ## Cross-border points nativeLF259; ## Rates, bands and thresholds nativeLF90 | Retained / corrected in current Guide: All old franchise thresholds retained with actual current law. Old EU100k France-excluded wording corrected to EU-wide actualscope and15WORKINGdays; acquisition10k is a different gate. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 246 | &#124; Goods and accommodation, turnover of the current year &#124; EUR 93,500 &#124; Above it: "elle est soumise à la TVA dès le 1 er jour de dépassement" &#124; | ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF75; ## Who this applies to nativeLF42; ## Cross-border points nativeLF259; ## Rates, bands and thresholds nativeLF90 | Retained / corrected in current Guide: All old franchise thresholds retained with actual current law. Old EU100k France-excluded wording corrected to EU-wide actualscope and15WORKINGdays; acquisition10k is a different gate. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 247 | &#124; Services and liberal professions other than lawyers, previous calendar year &#124; EUR 37,500 &#124; Above it, VAT from 1 January of the following year &#124; | ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF75; ## Who this applies to nativeLF42; ## Cross-border points nativeLF259; ## Rates, bands and thresholds nativeLF90 | Retained / corrected in current Guide: All old franchise thresholds retained with actual current law. Old EU100k France-excluded wording corrected to EU-wide actualscope and15WORKINGdays; acquisition10k is a different gate. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 248 | &#124; Services and liberal professions other than lawyers, current year &#124; EUR 41,250 &#124; Above it, VAT from the first day of the overrun &#124; | ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF75; ## Who this applies to nativeLF42; ## Cross-border points nativeLF259; ## Rates, bands and thresholds nativeLF90 | Retained / corrected in current Guide: All old franchise thresholds retained with actual current law. Old EU100k France-excluded wording corrected to EU-wide actualscope and15WORKINGdays; acquisition10k is a different gate. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 249 | &#124; A lawyer's regulated work, and authors' and performers' works and copyright, previous year &#124; EUR 50,000 &#124; Above it, VAT from 1 January of the following year &#124; | ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF75; ## Who this applies to nativeLF42; ## Cross-border points nativeLF259; ## Rates, bands and thresholds nativeLF90 | Retained / corrected in current Guide: All old franchise thresholds retained with actual current law. Old EU100k France-excluded wording corrected to EU-wide actualscope and15WORKINGdays; acquisition10k is a different gate. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 250 | &#124; The same activities, current year &#124; EUR 55,000 &#124; Above it, VAT from the first day of the overrun &#124; | ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF75; ## Who this applies to nativeLF42; ## Cross-border points nativeLF259; ## Rates, bands and thresholds nativeLF90 | Retained / corrected in current Guide: All old franchise thresholds retained with actual current law. Old EU100k France-excluded wording corrected to EU-wide actualscope and15WORKINGdays; acquisition10k is a different gate. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 251 | &#124; Their other activities, previous year &#124; EUR 35,000 &#124; Above it, VAT from 1 January of the following year &#124; | ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF75; ## Who this applies to nativeLF42; ## Cross-border points nativeLF259; ## Rates, bands and thresholds nativeLF90 | Retained / corrected in current Guide: All old franchise thresholds retained with actual current law. Old EU100k France-excluded wording corrected to EU-wide actualscope and15WORKINGdays; acquisition10k is a different gate. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 252 | &#124; Their other activities, current year &#124; EUR 38,500 &#124; Above it, VAT from the first day of the overrun &#124; | ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF75; ## Who this applies to nativeLF42; ## Cross-border points nativeLF259; ## Rates, bands and thresholds nativeLF90 | Retained / corrected in current Guide: All old franchise thresholds retained with actual current law. Old EU100k France-excluded wording corrected to EU-wide actualscope and15WORKINGdays; acquisition10k is a different gate. FR-R101 successor adds the actual operative components; previous maps preserved. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 253 | &#124; Annual turnover inside the European Union, France excluded &#124; EUR 100,000 &#124; Above it the franchise is lost for intra-EU trade and the tax office must be told within 15 days &#124; | ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF75; ## Who this applies to nativeLF42; ## Cross-border points nativeLF259 | Retained / corrected in current Guide: All old franchise thresholds retained with actual current law. Old EU100k France-excluded wording corrected to EU-wide actualscope and15WORKINGdays; acquisition10k is a different gate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 254 | &#124; Intra-EU acquisitions of goods by a business inside the franchise &#124; EUR 10,000 &#124; At or below it the seller may charge its own country's VAT. Above it the French buyer self-assesses French VAT at the French rate and must ask its tax office for an intra-EU VAT number &#124; | ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF75; ## Who this applies to nativeLF42; ## Cross-border points nativeLF259 | Retained / corrected in current Guide: All old franchise thresholds retained with actual current law. Old EU100k France-excluded wording corrected to EU-wide actualscope and15WORKINGdays; acquisition10k is a different gate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 255 | &#124; The single franchise threshold proposed by the 2025 finance law &#124; EUR 25,000 &#124; Abandoned: "La proposition issue de la loi de finances pour 2025 visant à instaurer un seuil unique de franchise en base de TVA de 25 000 € a été abandonnée" &#124; | ## Rates, bands and thresholds nativeLF58; ## Rates, bands and thresholds nativeLF59; ## Rates, bands and thresholds nativeLF60; ## Rates, bands and thresholds nativeLF61; ## Rates, bands and thresholds nativeLF62; ## Rates, bands and thresholds nativeLF75; ## Who this applies to nativeLF42; ## Cross-border points nativeLF259 | Retained / corrected in current Guide: All old franchise thresholds retained with actual current law. Old EU100k France-excluded wording corrected to EU-wide actualscope and15WORKINGdays; acquisition10k is a different gate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 257 | So the two thresholds bite differently, and the difference is the whole point. The basic threshold is tested on the previous calendar year and brings VAT from the first day of January of the following year. The tolerance threshold is tested on the current year and brings VAT from the first day of the overrun itself, which means invoices issued that same day already carry VAT. The sibling skill `france-bookkeeping` states the rule the same way, and the page above proves it in both directions. Any skill or note still printing a single French franchise threshold for 2026, at the abandoned amount in the last row of the table above, is wrong. | ## Rates, bands and thresholds nativeLF90 | Retained / corrected in current Guide: Prior-year versus same-day higher-threshold bite retained; startup conflict distinguished. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 259 | **The regimes, their limits and the instalments** | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 261 | &#124; Test &#124; Value &#124; Effect &#124; | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 262 | &#124; --- &#124; --- &#124; --- &#124; | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 263 | &#124; Source &#124; all figures below &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F23566 &#124; | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 264 | &#124; Régime réel simplifié, previous year turnover band for trade, catering and accommodation other than furnished lets: lower end &#124; EUR 85,000 &#124; "doit être compris entre : 85 000 € et 945 000 €" &#124; | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 265 | &#124; The same band: upper end &#124; EUR 945,000 &#124; Above it the business is in the régime réel normal &#124; | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 266 | &#124; Régime réel simplifié, previous year turnover band for other services including furnished lets: lower end &#124; EUR 37,500 &#124; "37 500 € et 286 000 €" &#124; | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 267 | &#124; The same band: upper end &#124; EUR 286,000 &#124; Above it the business is in the régime réel normal &#124; | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 268 | &#124; Current year ceiling for trade, catering and accommodation &#124; EUR 1,040,000 &#124; Crossing it puts the business in the régime réel normal retroactively from 1 January of the year of the overrun &#124; | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 269 | &#124; Current year ceiling for other services &#124; EUR 323,000 &#124; Same retroactive effect &#124; | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 270 | &#124; VAT due for the previous year, which must stay below this &#124; EUR 15,000 &#124; Crossing this alone moves the business to the régime réel normal from 1 January of the year after the overrun, whatever the turnover &#124; | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 271 | &#124; Régime réel normal, VAT payable each year below this &#124; EUR 4,000 &#124; Return and payment every three months instead of every month. The declaration page says the return "doit être faite tous les 3 mois"; the impots.gouv.fr regimes page says the business "peuvent opter pour le dépôt d'une déclaration de TVA chaque trimestre": treat quarterly filing as something to confirm with the tax office, not as automatic &#124; | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 272 | &#124; Régime réel simplifié, July instalment &#124; 55% &#124; "l'entreprise doit verser 55 % de la taxe due l'année précédente". The CA12 computes that base at line 57 as line 16 less lines 11, 12 and 22: the tax due less the tax on disposals of fixed assets and on self-supplies and less the deductions on other goods and services, before the VAT on fixed assets at line 23 &#124; | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 273 | &#124; Régime réel simplifié, December instalment &#124; 40% &#124; "l'entreprise doit verser 40 % de la taxe due l'année précédente". The CA12 computes that base at line 57 as line 16 less lines 11, 12 and 22: the tax due less the tax on disposals of fixed assets and on self-supplies and less the deductions on other goods and services, before the VAT on fixed assets at line 23 &#124; | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 274 | &#124; VAT paid in the previous year below this &#124; EUR 1,000 &#124; No instalments are due the following year, only the balance with the annual return &#124; | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 275 | &#124; Instalment revision &#124; 10% &#124; A business may ask for an instalment to be changed where its actual VAT is more than 10% above or below it &#124; | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 277 | The VAT-owed limit in that table is the condition most often dropped from a summary of the French regimes, and it is a limit in its own right: a business can sit comfortably inside the turnover band and still be moved to the régime réel normal because the VAT it owed last year was too large. Where a business in the régime réel simplifié declares more than that amount of VAT, the same page says it must file monthly instead of annually. | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 279 | Where the accounting year does not end on 31 December, the instalment dates follow the month in which the previous year's return was filed rather than a fixed calendar: a return filed between January and May of year N gives instalments in July and December of year N; a return filed between June and October of year N gives instalments in December of year N and July of year N plus one; a return filed in November or December of year N gives instalments in July and December of year N plus one. | ## Rates, bands and thresholds nativeLF63; ## Rates, bands and thresholds nativeLF64; ## Rates, bands and thresholds nativeLF65; ## Rates, bands and thresholds nativeLF66; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68; ## Rates, bands and thresholds nativeLF69; ## Rates, bands and thresholds nativeLF70; ## Rates, bands and thresholds nativeLF71; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF219 | Retained / corrected in current Guide: All four turnoverceilings, separate15000condition,4000quarterly,55/40,1000and10% and off-calendar instalment selector retained. Actual law corrects equality/atleast10% versus old below/morethan shorthand; FR-L36 supplies ordinary retroactive crossing procedure. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 281 | **Where two official pages disagree** | ## Rates, bands and thresholds nativeLF92; ## Rates, bands and thresholds nativeLF94; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68 | Retained / corrected in current Guide: Old840000/254000and current945000/286000countertexts remain in actual RSI explanation. Own indexed2026statute controls those figures rather than an invented conservative selector. Old taxpayer-size/startup contradictions remain expressly named. The old assertion that franchise also requires VAT<15000 is rejected by actual293B, not silently carried. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 283 | &#124; What impots.gouv.fr prints &#124; Value &#124; Note &#124; | ## Rates, bands and thresholds nativeLF92; ## Rates, bands and thresholds nativeLF94; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68 | Retained / corrected in current Guide: Old840000/254000and current945000/286000countertexts remain in actual RSI explanation. Own indexed2026statute controls those figures rather than an invented conservative selector. Old taxpayer-size/startup contradictions remain expressly named. The old assertion that franchise also requires VAT<15000 is rejected by actual293B, not silently carried. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 284 | &#124; --- &#124; --- &#124; --- &#124; | ## Rates, bands and thresholds nativeLF92; ## Rates, bands and thresholds nativeLF94; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68 | Retained / corrected in current Guide: Old840000/254000and current945000/286000countertexts remain in actual RSI explanation. Own indexed2026statute controls those figures rather than an invented conservative selector. Old taxpayer-size/startup contradictions remain expressly named. The old assertion that franchise also requires VAT<15000 is rejected by actual293B, not silently carried. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 285 | &#124; Source &#124; all figures below &#124; https://www.impots.gouv.fr/professionnel/les-regimes-dimposition-la-tva &#124; | ## Rates, bands and thresholds nativeLF92; ## Rates, bands and thresholds nativeLF94; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68 | Retained / corrected in current Guide: Old840000/254000and current945000/286000countertexts remain in actual RSI explanation. Own indexed2026statute controls those figures rather than an invented conservative selector. Old taxpayer-size/startup contradictions remain expressly named. The old assertion that franchise also requires VAT<15000 is rejected by actual293B, not silently carried. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 286 | &#124; Franchise, previous year, goods and accommodation &#124; EUR 85,000 &#124; Agrees with the franchise table above &#124; | ## Rates, bands and thresholds nativeLF92; ## Rates, bands and thresholds nativeLF94; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68 | Retained / corrected in current Guide: Old840000/254000and current945000/286000countertexts remain in actual RSI explanation. Own indexed2026statute controls those figures rather than an invented conservative selector. Old taxpayer-size/startup contradictions remain expressly named. The old assertion that franchise also requires VAT<15000 is rejected by actual293B, not silently carried. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 287 | &#124; Franchise, previous year, services &#124; EUR 37,500 &#124; Agrees with the franchise table above &#124; | ## Rates, bands and thresholds nativeLF92; ## Rates, bands and thresholds nativeLF94; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68 | Retained / corrected in current Guide: Old840000/254000and current945000/286000countertexts remain in actual RSI explanation. Own indexed2026statute controls those figures rather than an invented conservative selector. Old taxpayer-size/startup contradictions remain expressly named. The old assertion that franchise also requires VAT<15000 is rejected by actual293B, not silently carried. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 288 | &#124; Franchise in the first year of activity, goods and accommodation &#124; EUR 93,500 &#124; "n’excède pas 93 500 € ou 41 250 €". The full sentence: "la franchise est de droit la première année d'activité dès lors que le chiffre d'affaires n’excède pas 93 500 € ou 41 250 €" &#124; | ## Rates, bands and thresholds nativeLF92; ## Rates, bands and thresholds nativeLF94; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68 | Retained / corrected in current Guide: Old840000/254000and current945000/286000countertexts remain in actual RSI explanation. Own indexed2026statute controls those figures rather than an invented conservative selector. Old taxpayer-size/startup contradictions remain expressly named. The old assertion that franchise also requires VAT<15000 is rejected by actual293B, not silently carried. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 289 | &#124; Franchise in the first year of activity, services &#124; EUR 41,250 &#124; Same sentence. The page adds: "Ces montants correspondent aux limites majorées de la franchise en base" &#124; | ## Rates, bands and thresholds nativeLF92; ## Rates, bands and thresholds nativeLF94; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68 | Retained / corrected in current Guide: Old840000/254000and current945000/286000countertexts remain in actual RSI explanation. Own indexed2026statute controls those figures rather than an invented conservative selector. Old taxpayer-size/startup contradictions remain expressly named. The old assertion that franchise also requires VAT<15000 is rejected by actual293B, not silently carried. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 290 | &#124; Régime réel simplifié, turnover band for goods and accommodation: upper end &#124; EUR 840,000 &#124; The page says of these limits "sont applicables à compter du 1er janvier 2025" &#124; | ## Rates, bands and thresholds nativeLF92; ## Rates, bands and thresholds nativeLF94; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68 | Retained / corrected in current Guide: Old840000/254000and current945000/286000countertexts remain in actual RSI explanation. Own indexed2026statute controls those figures rather than an invented conservative selector. Old taxpayer-size/startup contradictions remain expressly named. The old assertion that franchise also requires VAT<15000 is rejected by actual293B, not silently carried. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 291 | &#124; Régime réel simplifié, turnover band for services: upper end &#124; EUR 254,000 &#124; Same note &#124; | ## Rates, bands and thresholds nativeLF92; ## Rates, bands and thresholds nativeLF94; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68 | Retained / corrected in current Guide: Old840000/254000and current945000/286000countertexts remain in actual RSI explanation. Own indexed2026statute controls those figures rather than an invented conservative selector. Old taxpayer-size/startup contradictions remain expressly named. The old assertion that franchise also requires VAT<15000 is rejected by actual293B, not silently carried. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 292 | &#124; VAT due limit for the régime réel simplifié &#124; EUR 15,000 &#124; Agrees with the regime table above &#124; | ## Rates, bands and thresholds nativeLF92; ## Rates, bands and thresholds nativeLF94; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68 | Retained / corrected in current Guide: Old840000/254000and current945000/286000countertexts remain in actual RSI explanation. Own indexed2026statute controls those figures rather than an invented conservative selector. Old taxpayer-size/startup contradictions remain expressly named. The old assertion that franchise also requires VAT<15000 is rejected by actual293B, not silently carried. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 293 | &#124; Quarterly returns where net VAT due in the year is below this &#124; EUR 4,000 &#124; "Lorsque le montant de la TVA nette due est inférieur annuellement à 4 000 €, les entreprises peuvent opter pour le dépôt d'une déclaration de TVA chaque trimestre" &#124; | ## Rates, bands and thresholds nativeLF92; ## Rates, bands and thresholds nativeLF94; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68 | Retained / corrected in current Guide: Old840000/254000and current945000/286000countertexts remain in actual RSI explanation. Own indexed2026statute controls those figures rather than an invented conservative selector. Old taxpayer-size/startup contradictions remain expressly named. The old assertion that franchise also requires VAT<15000 is rejected by actual293B, not silently carried. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 295 | The two official pages disagree on the upper ends of the simplified regime band. The service-public page, checked 21 February 2026, gives the figures it says are "valables pour l'année 2026". The impots.gouv.fr page, modified 21 May 2026, still prints the lower pair and labels them as applying from 1 January 2025. This skill works from the 2026 pair and prints the other pair here so that a reader who lands on the impots.gouv.fr page is not surprised. Where a client's turnover falls between the two pairs, the choice is not symmetric. If the lower pair is the live one, a business that stays on the annual CA12 has been in the régime réel normal since 1 January and has missed every monthly return since; if the higher pair is the live one, a business that files monthly CA3 returns has merely filed more often than it had to. So file on the régime réel normal footing and ask the tax office to confirm, rather than choosing the cheaper reading. | ## Rates, bands and thresholds nativeLF92; ## Rates, bands and thresholds nativeLF94; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68 | Retained / corrected in current Guide: Old840000/254000and current945000/286000countertexts remain in actual RSI explanation. Own indexed2026statute controls those figures rather than an invented conservative selector. Old taxpayer-size/startup contradictions remain expressly named. The old assertion that franchise also requires VAT<15000 is rejected by actual293B, not silently carried. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 297 | The same two pages also describe the franchise itself differently. The franchise page states it on turnover alone and uses "inférieur ou égal" against each threshold. The declaration page adds a second, cumulative condition, that the annual VAT the business owes is below the VAT limit in the regime table, and uses "inférieur à". Read both before telling a client they are inside the franchise. | ## Rates, bands and thresholds nativeLF92; ## Rates, bands and thresholds nativeLF94; ## Rates, bands and thresholds nativeLF67; ## Rates, bands and thresholds nativeLF68 | Retained / corrected in current Guide: Old840000/254000and current945000/286000countertexts remain in actual RSI explanation. Own indexed2026statute controls those figures rather than an invented conservative selector. Old taxpayer-size/startup contradictions remain expressly named. The old assertion that franchise also requires VAT<15000 is rejected by actual293B, not silently carried. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 299 | **Filing dates are a schedule, not a date** | ## Deadlines and filing nativeLF214; ## Deadlines and filing nativeLF216 | Retained / corrected in current Guide: Personalised15–24schedule and department/category/SIREN-or-name selector plus off-calendar annual deadline retained; exhaustive selector subranges remain at actual linked schedule, not a universal date. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 301 | There is no single French VAT filing date and this skill must never state one. Under the régime réel normal the return is due between the fifteenth and the twenty-fourth of the month following the chargeable event, and the taxpayer's own date inside that window is shown in the espace professionnel. The DGFiP publishes the schedule as a three-step selector (https://www.impots.gouv.fr/le-regime-reel-normal-dates-limites-de-transmission-des-ca3): first the department, with Paris, Hauts-de-Seine, Seine-Saint-Denis and Val-de-Marne treated apart from all other departments; then the category, which is entreprise individuelle, any company other than a société anonyme, société anonyme, or other taxpayer such as a local authority or an association; then, inside that category, either the first letter of the operator's name (A to H, or I to Z) or the range of the SIREN number (beginning 00 to 68, 69 to 78, 79 to 99 for one category, and 00 to 74 or 75 to 99 for another). The page renders the resulting day only for the combination chosen, so do not reproduce a day here: send the client to their espace professionnel. | ## Deadlines and filing nativeLF214; ## Deadlines and filing nativeLF216 | Retained / corrected in current Guide: Personalised15–24schedule and department/category/SIREN-or-name selector plus off-calendar annual deadline retained; exhaustive selector subranges remain at actual linked schedule, not a universal date. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 303 | Under the régime réel simplifié the annual return is due at the latest on the second working day following 1 May, and where the accounting year does not end on 31 December it is due within three months of the year end. | ## Deadlines and filing nativeLF214; ## Deadlines and filing nativeLF216 | Retained / corrected in current Guide: Personalised15–24schedule and department/category/SIREN-or-name selector plus off-calendar annual deadline retained; exhaustive selector subranges remain at actual linked schedule, not a universal date. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 305 | **Electronic invoicing arrives in two steps** | ## Deadlines and filing nativeLF223; ## Deadlines and filing nativeLF224; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Two receiving/issuing dates and company classes retained. Detailed platform/frequency/payment rules remain in siblingfrance-einvoice; consolidated commencement/size-reference questions explicitly remain. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 307 | &#124; Date &#124; Who &#124; What begins &#124; | ## Deadlines and filing nativeLF223; ## Deadlines and filing nativeLF224; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Two receiving/issuing dates and company classes retained. Detailed platform/frequency/payment rules remain in siblingfrance-einvoice; consolidated commencement/size-reference questions explicitly remain. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 308 | &#124; --- &#124; --- &#124; --- &#124; | ## Deadlines and filing nativeLF223; ## Deadlines and filing nativeLF224; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Two receiving/issuing dates and company classes retained. Detailed platform/frequency/payment rules remain in siblingfrance-einvoice; consolidated commencement/size-reference questions explicitly remain. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 309 | &#124; Source &#124; all rows below &#124; https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation &#124; | ## Deadlines and filing nativeLF223; ## Deadlines and filing nativeLF224; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Two receiving/issuing dates and company classes retained. Detailed platform/frequency/payment rules remain in siblingfrance-einvoice; consolidated commencement/size-reference questions explicitly remain. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 310 | &#124; 1 September 2026 &#124; Every business, whatever its size &#124; It must be able to receive invoices in electronic form, where its supplier is obliged to issue them that way: "devront recevoir leurs factures sous forme électronique, dès lors que leur fournisseur a l’obligation de les émettre sous ce format" &#124; | ## Deadlines and filing nativeLF223; ## Deadlines and filing nativeLF224; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Two receiving/issuing dates and company classes retained. Detailed platform/frequency/payment rules remain in siblingfrance-einvoice; consolidated commencement/size-reference questions explicitly remain. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 311 | &#124; 1 September 2026 &#124; Large companies and entreprises de taille intermédiaire &#124; They must issue electronic invoices and send transaction and payment data to the administration (e-reporting) &#124; | ## Deadlines and filing nativeLF223; ## Deadlines and filing nativeLF224; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Two receiving/issuing dates and company classes retained. Detailed platform/frequency/payment rules remain in siblingfrance-einvoice; consolidated commencement/size-reference questions explicitly remain. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 312 | &#124; 1 September 2027 &#124; Small and medium-sized companies and micro-enterprises &#124; They must issue electronic invoices and send transaction and payment data: "sera obligatoire pour les petites et moyennes entreprises ainsi que pour les micro-entreprises" &#124; | ## Deadlines and filing nativeLF223; ## Deadlines and filing nativeLF224; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Two receiving/issuing dates and company classes retained. Detailed platform/frequency/payment rules remain in siblingfrance-einvoice; consolidated commencement/size-reference questions explicitly remain. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 314 | The page is marked "Publié le 15/11/2024, modifié le 16/01/2026" and was read again on 19 October 2026. So on 19 October 2026 the first step is in force: every business must already be able to receive electronic invoices, and large and intermediate-sized companies already issue them and report. A small or medium-sized business or a micro-enterprise is not obliged to issue electronic invoices or to e-report before 1 September 2027. Receiving and issuing are separate duties. The sibling skill `france-einvoice` carries the formats, the platform model, the e-reporting frequencies and the penalties. Use it for anything beyond these dates. | ## Deadlines and filing nativeLF223; ## Deadlines and filing nativeLF224; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Two receiving/issuing dates and company classes retained. Detailed platform/frequency/payment rules remain in siblingfrance-einvoice; consolidated commencement/size-reference questions explicitly remain. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 316 | ## Section 3: Supplier pattern library (the lookup table) | ## The taxable base nativeLF174; ## The taxable base nativeLF172 | Corrected unsafe inference; workflow retained: Old do-not-question deterministic lookup replaced by conditional checks. Most-specific matching retained as a way to choose questions only. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 318 | This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment from the table directly. Do not second-guess. Do not consult Tier 1 rules: the table is authoritative for patterns it covers. Rates are not repeated here. Where a row says "standard rate" or "reduced rate", read the figure off the rate tables in Section 1. | ## The taxable base nativeLF174; ## The taxable base nativeLF172 | Corrected unsafe inference; workflow retained: Old do-not-question deterministic lookup replaced by conditional checks. Most-specific matching retained as a way to choose questions only. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 320 | **How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If several patterns match, use the most specific. If none match, fall through to the Tier 1 rules in Section 5. | ## The taxable base nativeLF174; ## The taxable base nativeLF172 | Corrected unsafe inference; workflow retained: Old do-not-question deterministic lookup replaced by conditional checks. Most-specific matching retained as a way to choose questions only. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 322 | ### 3.1 French banks (fees exempt, exclude) | ## The taxable base nativeLF178; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual operation and permitted financeoption, not automatic bankname exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 324 | **French banks pattern table** | ## The taxable base nativeLF178; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual operation and permitted financeoption, not automatic bankname exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 326 | &#124; Pattern &#124; Treatment &#124; Notes &#124; | ## The taxable base nativeLF178; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual operation and permitted financeoption, not automatic bankname exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 327 | &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF178; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual operation and permitted financeoption, not automatic bankname exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 328 | &#124; BNP PARIBAS, BNP &#124; EXCLUDE for bank charges and fees &#124; Financial service, exempt &#124; | ## The taxable base nativeLF178; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual operation and permitted financeoption, not automatic bankname exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 329 | &#124; SOCIETE GENERALE, SOC GEN, SG &#124; EXCLUDE for bank charges and fees &#124; Same &#124; | ## The taxable base nativeLF178; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual operation and permitted financeoption, not automatic bankname exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 330 | &#124; CREDIT AGRICOLE, CA, CRCAM &#124; EXCLUDE for bank charges and fees &#124; Same &#124; | ## The taxable base nativeLF178; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual operation and permitted financeoption, not automatic bankname exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 331 | &#124; LCL, CREDIT LYONNAIS &#124; EXCLUDE for bank charges and fees &#124; Same &#124; | ## The taxable base nativeLF178; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual operation and permitted financeoption, not automatic bankname exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 332 | &#124; BANQUE POPULAIRE, BPCE &#124; EXCLUDE for bank charges and fees &#124; Same &#124; | ## The taxable base nativeLF178; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual operation and permitted financeoption, not automatic bankname exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 333 | &#124; CAISSE D'EPARGNE, CE &#124; EXCLUDE for bank charges and fees &#124; Same &#124; | ## The taxable base nativeLF178; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual operation and permitted financeoption, not automatic bankname exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 334 | &#124; LA BANQUE POSTALE &#124; EXCLUDE for bank charges and fees &#124; Same &#124; | ## The taxable base nativeLF178; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual operation and permitted financeoption, not automatic bankname exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 335 | &#124; CIC, CREDIT MUTUEL &#124; EXCLUDE for bank charges and fees &#124; Same &#124; | ## The taxable base nativeLF178; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual operation and permitted financeoption, not automatic bankname exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 336 | &#124; QONTO &#124; EXCLUDE for bank charges and fees &#124; Check for separate taxable subscription invoices &#124; | ## The taxable base nativeLF178; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual operation and permitted financeoption, not automatic bankname exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 337 | &#124; REVOLUT, WISE, N26 (fee lines) &#124; EXCLUDE for transaction and maintenance fees &#124; Check for separate taxable subscription invoices &#124; | ## The taxable base nativeLF178; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual operation and permitted financeoption, not automatic bankname exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 338 | &#124; INTERETS, INTEREST, AGIOS &#124; EXCLUDE &#124; Interest income or expense, out of scope &#124; | ## The taxable base nativeLF178; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual operation and permitted financeoption, not automatic bankname exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 339 | &#124; PRET, EMPRUNT, LOAN &#124; EXCLUDE &#124; Loan principal movement, out of scope &#124; | ## The taxable base nativeLF178; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual operation and permitted financeoption, not automatic bankname exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 341 | ### 3.2 French government, regulators, and statutory bodies (exclude entirely) | ## The taxable base nativeLF179; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual tax/statutory/non-supply payment, not allpublicbody invoices. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 343 | **Government bodies pattern table** | ## The taxable base nativeLF179; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual tax/statutory/non-supply payment, not allpublicbody invoices. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 345 | &#124; Pattern &#124; Treatment &#124; Notes &#124; | ## The taxable base nativeLF179; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual tax/statutory/non-supply payment, not allpublicbody invoices. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 346 | &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF179; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual tax/statutory/non-supply payment, not allpublicbody invoices. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 347 | &#124; DGFIP, IMPOTS.GOUV, TRESOR PUBLIC &#124; EXCLUDE &#124; Tax payment, not a supply &#124; | ## The taxable base nativeLF179; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual tax/statutory/non-supply payment, not allpublicbody invoices. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 348 | &#124; DIRECTION GENERALE DES FINANCES &#124; EXCLUDE &#124; Tax payment &#124; | ## The taxable base nativeLF179; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual tax/statutory/non-supply payment, not allpublicbody invoices. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 349 | &#124; URSSAF &#124; EXCLUDE &#124; Social charges (cotisations sociales), not a VATable supply &#124; | ## The taxable base nativeLF179; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual tax/statutory/non-supply payment, not allpublicbody invoices. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 350 | &#124; CPAM, ASSURANCE MALADIE &#124; EXCLUDE &#124; Social security, not a supply &#124; | ## The taxable base nativeLF179; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual tax/statutory/non-supply payment, not allpublicbody invoices. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 351 | &#124; RSI, SSI &#124; EXCLUDE &#124; Social security for the self-employed &#124; | ## The taxable base nativeLF179; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual tax/statutory/non-supply payment, not allpublicbody invoices. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 352 | &#124; GREFFE, TRIBUNAL DE COMMERCE &#124; EXCLUDE &#124; Court and registry fees, sovereign acts &#124; | ## The taxable base nativeLF179; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual tax/statutory/non-supply payment, not allpublicbody invoices. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 353 | &#124; CFE, COTISATION FONCIERE &#124; EXCLUDE &#124; Local business tax, not a supply &#124; | ## The taxable base nativeLF179; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual tax/statutory/non-supply payment, not allpublicbody invoices. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 354 | &#124; CVAE &#124; EXCLUDE &#124; Contribution on added value, not a supply &#124; | ## The taxable base nativeLF179; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual tax/statutory/non-supply payment, not allpublicbody invoices. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 355 | &#124; PREFECTURE, SOUS-PREFECTURE &#124; EXCLUDE &#124; Government administrative fees &#124; | ## The taxable base nativeLF179; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual tax/statutory/non-supply payment, not allpublicbody invoices. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 356 | &#124; INPI &#124; EXCLUDE &#124; Trademark and patent office, government fee &#124; | ## The taxable base nativeLF179; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual tax/statutory/non-supply payment, not allpublicbody invoices. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 358 | ### 3.3 French utilities | ## The taxable base nativeLF181; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual product/invoice/entity/rate/use, not allutilities20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 360 | **Utilities pattern table** | ## The taxable base nativeLF181; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual product/invoice/entity/rate/use, not allutilities20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 362 | &#124; Pattern &#124; Treatment &#124; Line &#124; Notes &#124; | ## The taxable base nativeLF181; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual product/invoice/entity/rate/use, not allutilities20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 363 | &#124; --- &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF181; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual product/invoice/entity/rate/use, not allutilities20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 364 | &#124; EDF, ELECTRICITE DE FRANCE &#124; Domestic, standard rate &#124; 20 (input) &#124; Electricity, standard rate overhead &#124; | ## The taxable base nativeLF181; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual product/invoice/entity/rate/use, not allutilities20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 365 | &#124; ENGIE, GDF SUEZ &#124; Domestic, check the invoice &#124; 20 (input) &#124; Gas: the subscription and the energy can carry different rates. Read the invoice &#124; | ## The taxable base nativeLF181; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual product/invoice/entity/rate/use, not allutilities20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 366 | &#124; TOTAL ENERGIES, TOTALENERGIES &#124; Domestic, standard rate &#124; 20 (input) &#124; Energy and fuel supplier. Fuel is also caught by the fuel rule in Section 5.12 &#124; | ## The taxable base nativeLF181; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual product/invoice/entity/rate/use, not allutilities20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 367 | &#124; ORANGE, ORANGE BUSINESS &#124; Domestic, standard rate &#124; 20 (input) &#124; Telecoms and broadband, overhead &#124; | ## The taxable base nativeLF181; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual product/invoice/entity/rate/use, not allutilities20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 368 | &#124; FREE, FREE MOBILE, FREE SAS &#124; Domestic, standard rate &#124; 20 (input) &#124; Telecoms and broadband, overhead &#124; | ## The taxable base nativeLF181; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual product/invoice/entity/rate/use, not allutilities20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 369 | &#124; SFR, ALTICE &#124; Domestic, standard rate &#124; 20 (input) &#124; Telecoms and broadband &#124; | ## The taxable base nativeLF181; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual product/invoice/entity/rate/use, not allutilities20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 370 | &#124; BOUYGUES TELECOM &#124; Domestic, standard rate &#124; 20 (input) &#124; Telecoms and broadband &#124; | ## The taxable base nativeLF181; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual product/invoice/entity/rate/use, not allutilities20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 371 | &#124; OVH, OVH SAS, OVHCLOUD &#124; Domestic, standard rate &#124; 20 (input) &#124; Hosting, French entity &#124; | ## The taxable base nativeLF181; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual product/invoice/entity/rate/use, not allutilities20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 372 | &#124; VEOLIA, SUEZ EAU &#124; Domestic, reduced rate &#124; 20 (input) &#124; Water supply at the reduced rate &#124; | ## The taxable base nativeLF181; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual product/invoice/entity/rate/use, not allutilities20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 374 | ### 3.4 Insurance (exempt, exclude) | ## The taxable base nativeLF182; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual insurance/broker operation, not allinsurer services. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 376 | **Insurance pattern table** | ## The taxable base nativeLF182; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual insurance/broker operation, not allinsurer services. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 378 | &#124; Pattern &#124; Treatment &#124; Notes &#124; | ## The taxable base nativeLF182; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual insurance/broker operation, not allinsurer services. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 379 | &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF182; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual insurance/broker operation, not allinsurer services. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 380 | &#124; AXA, AXA FRANCE &#124; EXCLUDE &#124; Insurance, exempt &#124; | ## The taxable base nativeLF182; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual insurance/broker operation, not allinsurer services. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 381 | &#124; MAIF, MACIF, MATMUT, MAAF &#124; EXCLUDE &#124; Mutual insurance, exempt &#124; | ## The taxable base nativeLF182; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual insurance/broker operation, not allinsurer services. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 382 | &#124; GROUPAMA, GENERALI FRANCE &#124; EXCLUDE &#124; Insurance, exempt &#124; | ## The taxable base nativeLF182; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual insurance/broker operation, not allinsurer services. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 383 | &#124; AG2R, MALAKOFF HUMANIS &#124; EXCLUDE &#124; Complementary insurance and prévoyance, exempt &#124; | ## The taxable base nativeLF182; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual insurance/broker operation, not allinsurer services. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 384 | &#124; ASSURANCE, PRIME D'ASSURANCE &#124; EXCLUDE &#124; All insurance exempt &#124; | ## The taxable base nativeLF182; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual insurance/broker operation, not allinsurer services. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 386 | ### 3.5 Post and logistics | ## The taxable base nativeLF183; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual universalpostal condition and entity, not allparcelbrands sameVAT. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 388 | **Post and logistics pattern table** | ## The taxable base nativeLF183; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual universalpostal condition and entity, not allparcelbrands sameVAT. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 390 | &#124; Pattern &#124; Treatment &#124; Line &#124; Notes &#124; | ## The taxable base nativeLF183; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual universalpostal condition and entity, not allparcelbrands sameVAT. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 391 | &#124; --- &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF183; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual universalpostal condition and entity, not allparcelbrands sameVAT. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 392 | &#124; LA POSTE (standard mail) &#124; EXCLUDE for standard postage &#124; &#124; Universal postal service, exempt &#124; | ## The taxable base nativeLF183; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual universalpostal condition and entity, not allparcelbrands sameVAT. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 393 | &#124; LA POSTE (parcels, Colissimo) &#124; Domestic, standard rate &#124; 20 &#124; Non-universal services are taxable &#124; | ## The taxable base nativeLF183; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual universalpostal condition and entity, not allparcelbrands sameVAT. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 394 | &#124; CHRONOPOST &#124; Domestic, standard rate &#124; 20 &#124; Express courier, taxable &#124; | ## The taxable base nativeLF183; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual universalpostal condition and entity, not allparcelbrands sameVAT. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 395 | &#124; DHL EXPRESS FRANCE &#124; Domestic, standard rate &#124; 20 &#124; Express courier, taxable &#124; | ## The taxable base nativeLF183; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual universalpostal condition and entity, not allparcelbrands sameVAT. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 396 | &#124; UPS FRANCE, TNT FRANCE, FEDEX &#124; Domestic standard rate, or self-assessment if billed from outside France &#124; 20, or A3 plus 20 &#124; Check the billing entity &#124; | ## The taxable base nativeLF183; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual universalpostal condition and entity, not allparcelbrands sameVAT. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 397 | &#124; MONDIAL RELAY &#124; Domestic, standard rate &#124; 20 &#124; Parcel delivery, French entity &#124; | ## The taxable base nativeLF183; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual universalpostal condition and entity, not allparcelbrands sameVAT. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 399 | ### 3.6 Transport (France domestic) | ## The taxable base nativeLF184; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Output passenger rate distinguished from actual purchaser exclusion; tolls conditional. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 401 | **Transport pattern table** | ## The taxable base nativeLF184; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Output passenger rate distinguished from actual purchaser exclusion; tolls conditional. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 403 | &#124; Pattern &#124; Treatment &#124; Line &#124; Notes &#124; | ## The taxable base nativeLF184; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Output passenger rate distinguished from actual purchaser exclusion; tolls conditional. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 404 | &#124; --- &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF184; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Output passenger rate distinguished from actual purchaser exclusion; tolls conditional. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 405 | &#124; SNCF, OUIGO &#124; Domestic, intermediate rate &#124; 20 (input) &#124; Passenger transport at the intermediate rate &#124; | ## The taxable base nativeLF184; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Output passenger rate distinguished from actual purchaser exclusion; tolls conditional. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 406 | &#124; RATP, METRO, BUS RATP &#124; Domestic, intermediate rate &#124; 20 (input) &#124; Public transport, intermediate rate &#124; | ## The taxable base nativeLF184; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Output passenger rate distinguished from actual purchaser exclusion; tolls conditional. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 407 | &#124; UBER FR, UBER FRANCE &#124; Intermediate rate on the ride, standard rate on delivery &#124; 20 &#124; Separate rides from food delivery &#124; | ## The taxable base nativeLF184; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Output passenger rate distinguished from actual purchaser exclusion; tolls conditional. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 408 | &#124; BOLT FR, HEETCH &#124; Domestic, intermediate rate &#124; 20 &#124; Ride-hailing, passenger transport &#124; | ## The taxable base nativeLF184; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Output passenger rate distinguished from actual purchaser exclusion; tolls conditional. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 409 | &#124; AIR FRANCE (domestic) &#124; Domestic, intermediate rate &#124; 20 &#124; Domestic flights at the intermediate rate &#124; | ## The taxable base nativeLF184; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Output passenger rate distinguished from actual purchaser exclusion; tolls conditional. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 410 | &#124; AIR FRANCE, RYANAIR, EASYJET (international) &#124; EXCLUDE, exempt international transport &#124; &#124; International flights &#124; | ## The taxable base nativeLF184; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Output passenger rate distinguished from actual purchaser exclusion; tolls conditional. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 411 | &#124; TAXI, G7, TAXIS BLEUS &#124; Domestic, intermediate rate &#124; 20 &#124; Local taxi, passenger transport &#124; | ## The taxable base nativeLF184; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Output passenger rate distinguished from actual purchaser exclusion; tolls conditional. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 412 | &#124; AUTOROUTE, VINCI AUTOROUTES, SANEF, APRR &#124; Domestic, standard rate &#124; 20 &#124; Motorway tolls at the standard rate &#124; | ## The taxable base nativeLF184; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Output passenger rate distinguished from actual purchaser exclusion; tolls conditional. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 414 | ### 3.7 Food retail (blocked unless hospitality business) | ## The taxable base nativeLF186; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual goods/meal purpose and ordinary deduction; no supermarket/catering-only block. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 416 | **Food retail pattern table** | ## The taxable base nativeLF186; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual goods/meal purpose and ordinary deduction; no supermarket/catering-only block. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 418 | &#124; Pattern &#124; Treatment &#124; Notes &#124; | ## The taxable base nativeLF186; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual goods/meal purpose and ordinary deduction; no supermarket/catering-only block. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 419 | &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF186; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual goods/meal purpose and ordinary deduction; no supermarket/catering-only block. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 420 | &#124; CARREFOUR, AUCHAN, LECLERC, INTERMARCHE &#124; Default BLOCK input VAT &#124; Personal provisioning. Deductible only for a hospitality or catering business &#124; | ## The taxable base nativeLF186; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual goods/meal purpose and ordinary deduction; no supermarket/catering-only block. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 421 | &#124; LIDL, MONOPRIX, FRANPRIX, CASINO &#124; Default BLOCK &#124; Same &#124; | ## The taxable base nativeLF186; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual goods/meal purpose and ordinary deduction; no supermarket/catering-only block. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 422 | &#124; PICARD, LEADER PRICE, SUPER U &#124; Default BLOCK &#124; Same &#124; | ## The taxable base nativeLF186; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual goods/meal purpose and ordinary deduction; no supermarket/catering-only block. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 423 | &#124; RESTAURANT, BRASSERIE, CAFE, BISTRO &#124; Default BLOCK &#124; See Section 5.12 for what France does and does not block &#124; | ## The taxable base nativeLF186; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual goods/meal purpose and ordinary deduction; no supermarket/catering-only block. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 425 | ### 3.8 SaaS: EU suppliers (reverse charge, autoliquidation lines A3 and 20) | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 427 | These are billed from entities established in the European Union, typically Ireland or Luxembourg, and the French customer is the person liable for the tax under CGI art. 283-2. The base goes to line A3, the output tax into the rate block, and the deduction to line 20. | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 429 | **SaaS EU suppliers table** | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 431 | &#124; Pattern &#124; Billing entity &#124; Lines &#124; Notes &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 432 | &#124; --- &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 433 | &#124; GOOGLE (Ads, Workspace, Cloud) &#124; Google Ireland Ltd (IE) &#124; A3 plus 20 &#124; Self-assessment &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 434 | &#124; MICROSOFT (365, Azure) &#124; Microsoft Ireland Operations Ltd (IE) &#124; A3 plus 20 &#124; Self-assessment &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 435 | &#124; ADOBE &#124; Adobe Systems Software Ireland Ltd (IE) &#124; A3 plus 20 &#124; Self-assessment &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 436 | &#124; META, FACEBOOK ADS &#124; Meta Platforms Ireland Ltd (IE) &#124; A3 plus 20 &#124; Self-assessment &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 437 | &#124; LINKEDIN (paid) &#124; LinkedIn Ireland Unlimited (IE) &#124; A3 plus 20 &#124; Self-assessment &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 438 | &#124; SPOTIFY TECHNOLOGY &#124; Spotify AB (SE) &#124; A3 plus 20 &#124; Self-assessment &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 439 | &#124; DROPBOX &#124; Dropbox International Unlimited (IE) &#124; A3 plus 20 &#124; Self-assessment &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 440 | &#124; SLACK &#124; Slack Technologies Ireland Ltd (IE) &#124; A3 plus 20 &#124; Self-assessment &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 441 | &#124; ATLASSIAN (Jira, Confluence) &#124; Atlassian Network Services BV (NL) &#124; A3 plus 20 &#124; Self-assessment &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 442 | &#124; ZOOM &#124; Zoom Video Communications Ireland Ltd (IE) &#124; A3 plus 20 &#124; Self-assessment &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 443 | &#124; STRIPE (subscription fees) &#124; Stripe Technology Europe Ltd (IE) &#124; A3 plus 20 &#124; Transaction fees may be exempt, see 3.11 &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 445 | ### 3.9 SaaS: non-EU suppliers (autoliquidation, line A3 and line 20) | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 447 | The CA3 does not separate a service bought from an EU supplier from a service bought from a supplier outside the European Union. Both are purchases of services from a taxable person not established in France, the caption of line A3, and both go on line A3. Earlier versions of this skill sent non-EU services to a "line 05", which is not a line of the CA3. | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 449 | **SaaS non-EU suppliers table** | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 451 | &#124; Pattern &#124; Billing entity &#124; Lines &#124; Notes &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 452 | &#124; --- &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 453 | &#124; AWS (standard) &#124; AWS EMEA SARL (LU), check &#124; A3 plus 20 &#124; Luxembourg entity &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 454 | &#124; NOTION &#124; Notion Labs Inc (US) &#124; A3 plus 20 &#124; Service bought from a supplier not established in France &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 455 | &#124; ANTHROPIC, CLAUDE &#124; Anthropic PBC (US) &#124; A3 plus 20 &#124; Same &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 456 | &#124; OPENAI, CHATGPT &#124; OpenAI Inc (US) &#124; A3 plus 20 &#124; Same &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 457 | &#124; GITHUB (standard plans) &#124; GitHub Inc (US) &#124; A3 plus 20 &#124; Check whether billed by an Irish entity &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 458 | &#124; FIGMA &#124; Figma Inc (US) &#124; A3 plus 20 &#124; Same &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 459 | &#124; CANVA &#124; Canva Pty Ltd (AU) &#124; A3 plus 20 &#124; Same &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 460 | &#124; HUBSPOT &#124; HubSpot Inc (US) or HubSpot Ireland Ltd (IE), check the invoice &#124; A3 plus 20 &#124; Either way line A3 &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 461 | &#124; TWILIO &#124; Twilio Inc (US) &#124; A3 plus 20 &#124; Same &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 463 | ### 3.10 SaaS: the exception (reverse charge still applies) | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 465 | **SaaS exception table** | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 467 | &#124; Pattern &#124; Treatment &#124; Why &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 468 | &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 469 | &#124; AWS EMEA SARL &#124; Line A3 plus line 20 (Luxembourg entity) &#124; The customer is liable for the tax. If the invoice shows French TVA actually charged, treat it as a domestic purchase at the standard rate and deduct at line 20 &#124; | ## The taxable base nativeLF187; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: EU/nonEU/FRparticipatingestablishment and actual lawfulVAT; allbrands choosequestion, never legalresult. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 471 | ### 3.11 Payment processors | ## The taxable base nativeLF189; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual paymentoperation/option versus separate technical subscription; no brandwide exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 473 | **Payment processors table** | ## The taxable base nativeLF189; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual paymentoperation/option versus separate technical subscription; no brandwide exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 475 | &#124; Pattern &#124; Treatment &#124; Notes &#124; | ## The taxable base nativeLF189; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual paymentoperation/option versus separate technical subscription; no brandwide exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 476 | &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF189; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual paymentoperation/option versus separate technical subscription; no brandwide exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 477 | &#124; STRIPE (transaction fees) &#124; EXCLUDE (exempt) &#124; Payment processing fees are exempt financial services &#124; | ## The taxable base nativeLF189; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual paymentoperation/option versus separate technical subscription; no brandwide exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 478 | &#124; PAYPAL (transaction fees) &#124; EXCLUDE (exempt) &#124; Same &#124; | ## The taxable base nativeLF189; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual paymentoperation/option versus separate technical subscription; no brandwide exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 479 | &#124; STRIPE (monthly subscription) &#124; Line A3 plus line 20 &#124; Irish entity, separate line item from transaction fees &#124; | ## The taxable base nativeLF189; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual paymentoperation/option versus separate technical subscription; no brandwide exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 480 | &#124; SUMUP, SQUARE, ZETTLE &#124; Check the invoice &#124; French entity: domestic standard rate. Entity elsewhere: line A3 plus line 20 &#124; | ## The taxable base nativeLF189; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual paymentoperation/option versus separate technical subscription; no brandwide exemption. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 482 | ### 3.12 Professional services (France) | ## The taxable base nativeLF190; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual supplierregime/place/tax/use/capitalisation; no professionwide20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 484 | **Professional services table** | ## The taxable base nativeLF190; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual supplierregime/place/tax/use/capitalisation; no professionwide20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 486 | &#124; Pattern &#124; Treatment &#124; Line &#124; Notes &#124; | ## The taxable base nativeLF190; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual supplierregime/place/tax/use/capitalisation; no professionwide20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 487 | &#124; --- &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF190; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual supplierregime/place/tax/use/capitalisation; no professionwide20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 488 | &#124; EXPERT COMPTABLE, CABINET COMPTABLE &#124; Domestic, standard rate &#124; 20 &#124; Deductible &#124; | ## The taxable base nativeLF190; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual supplierregime/place/tax/use/capitalisation; no professionwide20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 489 | &#124; AVOCAT, CABINET D'AVOCATS &#124; Domestic, standard rate &#124; 20 &#124; Deductible if a business legal matter &#124; | ## The taxable base nativeLF190; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual supplierregime/place/tax/use/capitalisation; no professionwide20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 490 | &#124; NOTAIRE (business-related fees) &#124; Domestic, standard rate &#124; 20 &#124; Notarial fees on business transactions &#124; | ## The taxable base nativeLF190; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual supplierregime/place/tax/use/capitalisation; no professionwide20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 491 | &#124; COMMISSAIRE AUX COMPTES, CAC &#124; Domestic, standard rate &#124; 20 &#124; Audit fees, deductible &#124; | ## The taxable base nativeLF190; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual supplierregime/place/tax/use/capitalisation; no professionwide20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 492 | &#124; ARCHITECTE, GEOMETRE &#124; Domestic, standard rate &#124; 20 &#124; Professional services &#124; | ## The taxable base nativeLF190; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual supplierregime/place/tax/use/capitalisation; no professionwide20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 493 | &#124; CHAMBRE DE COMMERCE, CCI &#124; EXCLUDE &#124; Registration and membership fees, government body &#124; | ## The taxable base nativeLF190; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual supplierregime/place/tax/use/capitalisation; no professionwide20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 494 | &#124; CHAMBRE DES METIERS, CMA &#124; EXCLUDE &#124; Same &#124; | ## The taxable base nativeLF190; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual supplierregime/place/tax/use/capitalisation; no professionwide20. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 496 | ### 3.13 Payroll and social security (exclude entirely) | ## The taxable base nativeLF180; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Proved wage/socialamounts versus merely payrolllooking debit. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 498 | **Payroll and social security table** | ## The taxable base nativeLF180; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Proved wage/socialamounts versus merely payrolllooking debit. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 500 | &#124; Pattern &#124; Treatment &#124; Notes &#124; | ## The taxable base nativeLF180; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Proved wage/socialamounts versus merely payrolllooking debit. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 501 | &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF180; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Proved wage/socialamounts versus merely payrolllooking debit. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 502 | &#124; URSSAF &#124; EXCLUDE &#124; Social contributions &#124; | ## The taxable base nativeLF180; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Proved wage/socialamounts versus merely payrolllooking debit. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 503 | &#124; POLE EMPLOI, FRANCE TRAVAIL &#124; EXCLUDE &#124; Employment agency, social contribution &#124; | ## The taxable base nativeLF180; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Proved wage/socialamounts versus merely payrolllooking debit. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 504 | &#124; RETRAITE, CIPAV, CNAV &#124; EXCLUDE &#124; Pension and retirement contributions &#124; | ## The taxable base nativeLF180; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Proved wage/socialamounts versus merely payrolllooking debit. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 505 | &#124; SALAIRE, PAIE, VIREMENT SALAIRE &#124; EXCLUDE &#124; Wages, outside the scope of VAT &#124; | ## The taxable base nativeLF180; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Proved wage/socialamounts versus merely payrolllooking debit. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 506 | &#124; MUTUELLE (employee complementary) &#124; EXCLUDE &#124; Social benefit, not a VATable supply &#124; | ## The taxable base nativeLF180; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Proved wage/socialamounts versus merely payrolllooking debit. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 508 | ### 3.14 Property and rent | ## The taxable base nativeLF191; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual qualifying rent/option evidence, not landlordname inference. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 510 | **Property and rent table** | ## The taxable base nativeLF191; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual qualifying rent/option evidence, not landlordname inference. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 512 | &#124; Pattern &#124; Treatment &#124; Notes &#124; | ## The taxable base nativeLF191; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual qualifying rent/option evidence, not landlordname inference. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 513 | &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF191; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual qualifying rent/option evidence, not landlordname inference. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 514 | &#124; LOYER COMMERCIAL, BAIL COMMERCIAL &#124; Domestic, standard rate &#124; Only where the landlord opted to charge VAT (option à la TVA) &#124; | ## The taxable base nativeLF191; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual qualifying rent/option evidence, not landlordname inference. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 515 | &#124; LOYER, BAIL (residential, no VAT) &#124; EXCLUDE &#124; Residential lease exempt &#124; | ## The taxable base nativeLF191; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual qualifying rent/option evidence, not landlordname inference. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 516 | &#124; FONCIER, TAXE FONCIERE &#124; EXCLUDE &#124; Property tax, not a supply &#124; | ## The taxable base nativeLF191; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual qualifying rent/option evidence, not landlordname inference. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 517 | &#124; SCI (with TVA invoiced) &#124; Domestic, standard rate &#124; Commercial property through an SCI that opted for VAT &#124; | ## The taxable base nativeLF191; ## The taxable base nativeLF174 | Category retained; incorrect name-based rule corrected: Actual qualifying rent/option evidence, not landlordname inference. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 519 | ### 3.15 Internal transfers and exclusions | ## The taxable base nativeLF192; ## The taxable base nativeLF174; ## The taxable base nativeLF180 | Category retained; incorrect name-based rule corrected: Ownaccount/dividend/capital movements requirefacts; cashwithdrawal alone proves neither drawing nor VATpurchase. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 521 | **Internal transfers table** | ## The taxable base nativeLF192; ## The taxable base nativeLF174; ## The taxable base nativeLF180 | Category retained; incorrect name-based rule corrected: Ownaccount/dividend/capital movements requirefacts; cashwithdrawal alone proves neither drawing nor VATpurchase. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 523 | &#124; Pattern &#124; Treatment &#124; Notes &#124; | ## The taxable base nativeLF192; ## The taxable base nativeLF174; ## The taxable base nativeLF180 | Category retained; incorrect name-based rule corrected: Ownaccount/dividend/capital movements requirefacts; cashwithdrawal alone proves neither drawing nor VATpurchase. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 524 | &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF192; ## The taxable base nativeLF174; ## The taxable base nativeLF180 | Category retained; incorrect name-based rule corrected: Ownaccount/dividend/capital movements requirefacts; cashwithdrawal alone proves neither drawing nor VATpurchase. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 525 | &#124; VIREMENT INTERNE, VIR INTERNE &#124; EXCLUDE &#124; Internal movement &#124; | ## The taxable base nativeLF192; ## The taxable base nativeLF174; ## The taxable base nativeLF180 | Category retained; incorrect name-based rule corrected: Ownaccount/dividend/capital movements requirefacts; cashwithdrawal alone proves neither drawing nor VATpurchase. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 526 | &#124; VIREMENT ENTRE COMPTES &#124; EXCLUDE &#124; Own-account transfer &#124; | ## The taxable base nativeLF192; ## The taxable base nativeLF174; ## The taxable base nativeLF180 | Category retained; incorrect name-based rule corrected: Ownaccount/dividend/capital movements requirefacts; cashwithdrawal alone proves neither drawing nor VATpurchase. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 527 | &#124; DIVIDENDE &#124; EXCLUDE &#124; Dividend payment, out of scope &#124; | ## The taxable base nativeLF192; ## The taxable base nativeLF174; ## The taxable base nativeLF180 | Category retained; incorrect name-based rule corrected: Ownaccount/dividend/capital movements requirefacts; cashwithdrawal alone proves neither drawing nor VATpurchase. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 528 | &#124; REMBOURSEMENT PRET, ECHEANCE &#124; EXCLUDE &#124; Loan repayment, out of scope &#124; | ## The taxable base nativeLF192; ## The taxable base nativeLF174; ## The taxable base nativeLF180 | Category retained; incorrect name-based rule corrected: Ownaccount/dividend/capital movements requirefacts; cashwithdrawal alone proves neither drawing nor VATpurchase. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 529 | &#124; RETRAIT DAB, RETRAIT ESPECES &#124; TIER 2, ask &#124; Default exclude, ask what the cash was spent on &#124; | ## The taxable base nativeLF192; ## The taxable base nativeLF174; ## The taxable base nativeLF180 | Category retained; incorrect name-based rule corrected: Ownaccount/dividend/capital movements requirefacts; cashwithdrawal alone proves neither drawing nor VATpurchase. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 530 | &#124; APPORT, APPORT PERSONNEL &#124; EXCLUDE &#124; Owner injection &#124; | ## The taxable base nativeLF192; ## The taxable base nativeLF174; ## The taxable base nativeLF180 | Category retained; incorrect name-based rule corrected: Ownaccount/dividend/capital movements requirefacts; cashwithdrawal alone proves neither drawing nor VATpurchase. Each old alias and table scaffold remains in this origin record and is routed to the same substantive class; unmatched brands follow the general method, not an unsupported default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 532 | ## Section 4: Worked examples | ## Worked examples nativeLF265 | Retained / corrected in current Guide: All six hypothetical original cases restored and individually mapped below, with ordinary source gates and actual old dates/amounts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 534 | These are six fully worked classifications drawn from a hypothetical bank statement of a France-based self-employed IT consultant inside the régime réel normal. They illustrate the trickiest cases. All amounts in this section are in euro and are illustrative only. Rates are not repeated: read them off the rate tables in Section 1. | ## Worked examples nativeLF265 | Retained / corrected in current Guide: All six hypothetical original cases restored and individually mapped below, with ordinary source gates and actual old dates/amounts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 536 | ### Example 1: Non-EU SaaS autoliquidation (Notion) | ## Worked examples nativeLF267 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 538 | **Input line:** | ## Worked examples nativeLF267 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 539 | `03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; 14.68` | ## Worked examples nativeLF267 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 541 | **Reasoning:** | ## Worked examples nativeLF267 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 542 | Notion Labs Inc is a United States entity (Section 3.9). There is no VAT on the invoice. This is a service received from a supplier not established in France, so the French customer is the person liable for the tax under CGI art. 283-2. The net amount goes to line A3, the output tax into the standard-rate block at line 08, and the deduction to line 20. The net effect is nil for a fully taxable client. | ## Worked examples nativeLF267 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 544 | **Output table** | ## Worked examples nativeLF267 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 546 | &#124; Date &#124; Counterparty &#124; Gross &#124; Net &#124; VAT &#124; Rate &#124; Line (input) &#124; Line (output) &#124; Default? &#124; Question? &#124; Excluded? &#124; | ## Worked examples nativeLF267 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 547 | &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; | ## Worked examples nativeLF267 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 548 | &#124; 03.04.2026 &#124; NOTION LABS INC &#124; 14.68 &#124; 14.68 &#124; 2.94 &#124; standard &#124; 20 &#124; A3 and 08 &#124; N &#124; &#124; &#124; | ## Worked examples nativeLF267 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 550 | ### Example 2: EU service, autoliquidation (Google Ads) | ## Worked examples nativeLF268 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 552 | **Input line:** | ## Worked examples nativeLF268 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 553 | `10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; 850.00` | ## Worked examples nativeLF268 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 555 | **Reasoning:** | ## Worked examples nativeLF268 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 556 | Google Ireland Limited is an Irish entity. Google Ads is a service. The base goes to line A3, the output tax into the standard-rate block at line 08, and the deduction to line 20. Both sides must appear on the return. The net effect is nil for a fully taxable client. | ## Worked examples nativeLF268 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 558 | **Output table** | ## Worked examples nativeLF268 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 560 | &#124; Date &#124; Counterparty &#124; Gross &#124; Net &#124; VAT &#124; Rate &#124; Line (input) &#124; Line (output) &#124; Default? &#124; Question? &#124; Excluded? &#124; | ## Worked examples nativeLF268 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 561 | &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; | ## Worked examples nativeLF268 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 562 | &#124; 10.04.2026 &#124; GOOGLE IRELAND LIMITED &#124; 850.00 &#124; 850.00 &#124; 170.00 &#124; standard &#124; 20 &#124; A3 and 08 &#124; N &#124; &#124; &#124; | ## Worked examples nativeLF268 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 564 | ### Example 3: Entertainment and restaurant costs in France | ## Worked examples nativeLF269 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 566 | **Input line:** | ## Worked examples nativeLF269 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 567 | `15.04.2026 ; BRASSERIE LIPP PARIS ; DEBIT ; Business dinner ; 220.00` | ## Worked examples nativeLF269 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 569 | **Reasoning:** | ## Worked examples nativeLF269 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 570 | A restaurant transaction. France does not exclude restaurant and catering costs from deduction in the way it excludes accommodation for staff: the exclusions in Annexe II to the CGI are listed and restaurant costs are not among them. What controls the deduction is the ordinary condition that the expense is incurred for the needs of the business, so the file must show the business purpose and who was present. Personal meals are not deductible. Default: block and flag for the reviewer. If the reviewer confirms the business purpose with documentation, deduct at line 20. | ## Worked examples nativeLF269 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 572 | **Output table** | ## Worked examples nativeLF269 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 574 | &#124; Date &#124; Counterparty &#124; Gross &#124; Net &#124; VAT &#124; Rate &#124; Line &#124; Default? &#124; Question? &#124; Excluded? &#124; | ## Worked examples nativeLF269 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 575 | &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; | ## Worked examples nativeLF269 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 576 | &#124; 15.04.2026 &#124; BRASSERIE LIPP PARIS &#124; 220.00 &#124; 220.00 &#124; 0 &#124; &#124; &#124; Y &#124; Q1 &#124; "Restaurant: confirm business purpose and who was present" &#124; | ## Worked examples nativeLF269 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 578 | ### Example 4: capital goods (immobilisation) | ## Worked examples nativeLF270 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 580 | **Input line:** | ## Worked examples nativeLF270 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 581 | `18.04.2026 ; DELL FRANCE SAS ; DEBIT ; Invoice DEL2026-0041 Laptop ; 1,595.00` | ## Worked examples nativeLF270 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 583 | **Reasoning:** | ## Worked examples nativeLF270 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 584 | The gross amount is 1,595.00 including VAT. Dividing by 1.20 gives 1,329.17 excluding VAT, and the tax is 265.83. The amount excluding VAT is above the small-equipment tolerance in the capital goods table in Section 5.11, so the item is an immobilisation and its input VAT goes to line 19, not line 20. | ## Worked examples nativeLF270 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 586 | **Output table** | ## Worked examples nativeLF270 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 588 | &#124; Date &#124; Counterparty &#124; Gross &#124; Net &#124; VAT &#124; Rate &#124; Line &#124; Default? &#124; Question? &#124; Excluded? &#124; | ## Worked examples nativeLF270 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 589 | &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; | ## Worked examples nativeLF270 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 590 | &#124; 18.04.2026 &#124; DELL FRANCE SAS &#124; 1,595.00 &#124; 1,329.17 &#124; 265.83 &#124; standard &#124; 19 &#124; N &#124; &#124; &#124; | ## Worked examples nativeLF270 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 592 | ### Example 5: EU B2B service sale (inbound receipt) | ## Worked examples nativeLF271 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 594 | **Input line:** | ## Worked examples nativeLF271 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 595 | `22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice FR-2026-018 IT consultancy March ; 3,500.00` | ## Worked examples nativeLF271 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 597 | **Reasoning:** | ## Worked examples nativeLF271 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 598 | An incoming 3,500.00 from a German company with a German IBAN. The client supplies IT consultancy. For services between taxable persons the place of supply is the customer's country under CGI art. 259-1, and the customer is liable for the tax. The client invoices without French VAT and states "Auto-liquidation", the wording the invoice page gives for that case. On the CA3 the receipt goes to line E2, which covers "prestations de services rendues à un preneur établi à l'étranger". There is no output VAT. A déclaration européenne de services is due through the customs portal. Confirm two things: that the customer is VAT registered, by checking the German number on VIES, and that the invoice carries the reverse-charge wording. | ## Worked examples nativeLF271 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 600 | **Output table** | ## Worked examples nativeLF271 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 602 | &#124; Date &#124; Counterparty &#124; Gross &#124; Net &#124; VAT &#124; Rate &#124; Line &#124; Default? &#124; Question? &#124; Excluded? &#124; | ## Worked examples nativeLF271 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 603 | &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; | ## Worked examples nativeLF271 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 604 | &#124; 22.04.2026 &#124; STUDIO KREBS GMBH &#124; 3,500.00 &#124; 3,500.00 &#124; 0 &#124; none &#124; E2 &#124; Y &#124; Q2 (HIGH) &#124; "Verify the German VAT number on VIES" &#124; | ## Worked examples nativeLF271 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 606 | ### Example 6: Motor vehicle, blocked for VP | ## Worked examples nativeLF272 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 608 | **Input line:** | ## Worked examples nativeLF272 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 609 | `28.04.2026 ; ARVAL FRANCE ; DEBIT ; Lease payment ; 650.00` | ## Worked examples nativeLF272 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 611 | **Reasoning:** | ## Worked examples nativeLF272 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 612 | A car lease payment. Under the 6° of the 2 of the IV of article 206 of Annexe II to the CGI, vehicles designed to carry people or for mixed use are excluded from the right to deduct. The test is how the vehicle was designed, not how it is used, and the administration says so in terms: "L'exclusion est déterminé sur la base d'un critère de conception, indépendamment de l'usage effectif du véhicule", assessed at the date of acquisition or of taking on lease, so a later conversion does not change it. For an IT consultant leasing a passenger car the VAT is blocked. It would not be blocked for a taxi operator, a driving school, a vehicle hire business or an undertaker's hearse: see the exceptions in Section 5.12. Fuel follows its own rule, in Section 5.12. | ## Worked examples nativeLF272 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 614 | **Output table** | ## Worked examples nativeLF272 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 616 | &#124; Date &#124; Counterparty &#124; Gross &#124; Net &#124; VAT &#124; Rate &#124; Line &#124; Default? &#124; Question? &#124; Excluded? &#124; | ## Worked examples nativeLF272 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 617 | &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; --- &#124; | ## Worked examples nativeLF272 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 618 | &#124; 28.04.2026 &#124; ARVAL FRANCE &#124; 650.00 &#124; 650.00 &#124; 0 &#124; &#124; &#124; Y &#124; Q3 &#124; "Passenger vehicle: VAT blocked. Was this vehicle designed to carry goods?" &#124; | ## Worked examples nativeLF272 | Retained / source-corrected: Writer actually read old case and restored current destination with explicit source corrections; independent review pending |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 620 | ## Section 5: Tier 1 classification rules (compressed) | ## Rates, bands and thresholds nativeLF52; ## The taxable base nativeLF102; ## The taxable base nativeLF120; ## The taxable base nativeLF128; ## The taxable base nativeLF129 | Retained / corrected in current Guide: Standardrate and domestic output/input line topics retained; known transaction conditions, not an unknown-rate default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 622 | Each rule states the legal source and the line mapping. Apply silently if the data is unambiguous. Rates are in the rate tables in Section 1. | ## Rates, bands and thresholds nativeLF52; ## The taxable base nativeLF102; ## The taxable base nativeLF120; ## The taxable base nativeLF128; ## The taxable base nativeLF129 | Retained / corrected in current Guide: Standardrate and domestic output/input line topics retained; known transaction conditions, not an unknown-rate default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 624 | ### 5.1 Standard rate (Art. 278 CGI) | ## Rates, bands and thresholds nativeLF52; ## The taxable base nativeLF102; ## The taxable base nativeLF120; ## The taxable base nativeLF128; ## The taxable base nativeLF129 | Retained / corrected in current Guide: Standardrate and domestic output/input line topics retained; known transaction conditions, not an unknown-rate default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 626 | - **Standard rate**: the default for any taxable supply unless a reduced rate, an exemption or a self-assessment rule applies. Sales go to line A1 with the tax at line 08. Purchases go to line 20, or line 19 for capital goods. _(CGI art. 278)_ | ## Rates, bands and thresholds nativeLF52; ## The taxable base nativeLF102; ## The taxable base nativeLF120; ## The taxable base nativeLF128; ## The taxable base nativeLF129 | Retained / corrected in current Guide: Standardrate and domestic output/input line topics retained; known transaction conditions, not an unknown-rate default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 628 | ### 5.2 Reduced rate, intermediate (Art. 278 bis, 279 CGI) | ## Rates, bands and thresholds nativeLF53; ## Rates, bands and thresholds nativeLF82 | Retained selected categories; prepared take-away category not yet confirmed: Restaurant/passenger/hotel/TV/old-dwelling topics retained with actual conditions. Old immediate-consumption prepared-food category outside current selected279m clause remains to check in279n. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 630 | - **Intermediate reduced rate**: restaurant meals, passenger transport, work on dwellings finished more than two years ago other than construction, reconstruction and enlargement, hotel and holiday accommodation, prepared food for immediate consumption, television subscriptions. Sales go to line A1 with the tax at line 9B. Purchases go to line 20. _(CGI art. 278 bis, 279)_ | ## Rates, bands and thresholds nativeLF53; ## Rates, bands and thresholds nativeLF82 | Retained selected categories; prepared take-away category not yet confirmed: Restaurant/passenger/hotel/TV/old-dwelling topics retained with actual conditions. Old immediate-consumption prepared-food category outside current selected279m clause remains to check in279n. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 632 | ### 5.3 Reduced rate, the lower one (Art. 278-0 bis CGI) | ## Rates, bands and thresholds nativeLF54; ## Rates, bands and thresholds nativeLF82; ## Rates, bands and thresholds nativeLF88 | Retained / corrected in current Guide: Food/books/water/energy and live-performance topics retained with actual category conditions; ordinary input eligibility separate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 634 | - **Reduced rate**: food staples not prepared or consumed on the premises, books including digital books, live performances, energy-efficiency work on dwellings, water supply. Sales go to line A1 with the tax at line 09. Purchases go to line 20. _(CGI art. 278-0 bis)_ | ## Rates, bands and thresholds nativeLF54; ## Rates, bands and thresholds nativeLF82; ## Rates, bands and thresholds nativeLF88 | Retained / corrected in current Guide: Food/books/water/energy and live-performance topics retained with actual category conditions; ordinary input eligibility separate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 636 | ### 5.4 Super-reduced rate, the taux particulier (Art. 281 quater to 281 nonies CGI) | ## Rates, bands and thresholds nativeLF55; ## Rates, bands and thresholds nativeLF86; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Medicine/blood/press/T6 topic retained with actual qualifications and directtherapeuticexemption; unsupported default-to-standard-if-unknown removed. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 638 | - **Special rate**: reimbursable medicines and human blood products, and press publications under a separate article that this skill does not source. It is the only special rate in mainland France. On the CA3 the base and the tax go to line T6 for continental France. It is narrow: default to the standard rate if uncertain. _(CGI art. 281 quater to 281 nonies)_ | ## Rates, bands and thresholds nativeLF55; ## Rates, bands and thresholds nativeLF86; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Medicine/blood/press/T6 topic retained with actual qualifications and directtherapeuticexemption; unsupported default-to-standard-if-unknown removed. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 640 | ### 5.5 Zero rate and exempt with credit | ## The taxable base nativeLF154; ## Ask the client first nativeLF332 | Retained general method; specialist exemption scope not yet confirmed: Export/EUgoods/foreignservices/exemptwithoutcredit/mixedbusiness topics retained. Specific cultural/sporting and specialist education/medical exemption eligibility remains outside the selected method and must not be inferred from a label. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 642 | - **Zero rate and exempt with credit**: exports outside the European Union go to line E1 and need export evidence. Intra-EU supplies of goods to a taxable person go to line F2 and need the customer's VAT number checked on VIES, transport proof and a compliant invoice. Services supplied to a customer established abroad go to line E2, even where they are taxed in the customer's country. | ## The taxable base nativeLF154; ## Ask the client first nativeLF332 | Retained general method; specialist exemption scope not yet confirmed: Export/EUgoods/foreignservices/exemptwithoutcredit/mixedbusiness topics retained. Specific cultural/sporting and specialist education/medical exemption eligibility remains outside the selected method and must not be inferred from a label. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 644 | ### 5.6 Exempt without credit (Art. 261 CGI) | ## The taxable base nativeLF154; ## Ask the client first nativeLF332 | Retained general method; specialist exemption scope not yet confirmed: Export/EUgoods/foreignservices/exemptwithoutcredit/mixedbusiness topics retained. Specific cultural/sporting and specialist education/medical exemption eligibility remains outside the selected method and must not be inferred from a label. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 646 | - **Exempt without credit**: medical and paramedical services, education and training under conditions, insurance, financial services, residential rent, certain cultural and sporting activities. No output VAT and no deduction of input VAT on the related costs. If significant, the coefficient de déduction rules apply and **R-FR-2 refuses** where the exempt proportion is not de minimis. _(CGI art. 261)_ | ## The taxable base nativeLF154; ## Ask the client first nativeLF332 | Retained general method; specialist exemption scope not yet confirmed: Export/EUgoods/foreignservices/exemptwithoutcredit/mixedbusiness topics retained. Specific cultural/sporting and specialist education/medical exemption eligibility remains outside the selected method and must not be inferred from a label. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 648 | ### 5.7 Local standard purchases | ## The taxable base nativeLF128; ## The taxable base nativeLF129; ## The taxable base nativeLF156; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Compliant lawful domestic invoice, actual taxablebusiness use, restrictions and capitalisation/expense distinction retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 650 | - **Local standard purchases**: input VAT on a compliant facture from a French supplier is deductible for purchases used in a taxable business activity, subject to the deduction restrictions in 5.12 and the capital goods rule in 5.11. Overhead maps to line 20 and capital goods to line 19. | ## The taxable base nativeLF128; ## The taxable base nativeLF129; ## The taxable base nativeLF156; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Compliant lawful domestic invoice, actual taxablebusiness use, restrictions and capitalisation/expense distinction retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 652 | ### 5.8 Autoliquidation: EU services received (Art. 283-2 CGI) | ## The taxable base nativeLF149; ## The taxable base nativeLF187; ## The taxable base nativeLF172 | Retained / corrected in current Guide: EU/nonEUgeneralservice A3/output/input retained; actual billing/participatingestablishment and lawfulinvoice conditions apply. ForeignVAT is notFrenchinput; refund in sourcecountry distinct. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 654 | - **Services received**: the CA3 makes no distinction between a service bought from an EU supplier and one bought from a supplier outside the European Union. Where the client receives a service from a supplier not established in France and the supplier invoices without VAT, the base goes to line A3, the output tax into the rate block, and the input VAT to line 20. The net effect is nil for a fully taxable client. This applies whether the supplier is in the European Union or outside it. If an EU supplier actually charged its own local VAT, that is not self-assessment: treat it as an expense carrying irrecoverable foreign VAT and consider a refund claim in that country. _(CGI art. 283-2)_ | ## The taxable base nativeLF149; ## The taxable base nativeLF187; ## The taxable base nativeLF172 | Retained / corrected in current Guide: EU/nonEUgeneralservice A3/output/input retained; actual billing/participatingestablishment and lawfulinvoice conditions apply. ForeignVAT is notFrenchinput; refund in sourcecountry distinct. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 656 | ### 5.9 Autoliquidation: EU goods received (acquisitions intracommunautaires) | ## The taxable base nativeLF150; ## The taxable base nativeLF116 | Retained / corrected in current Guide: B2/output/memo17/19or20 distinction retained; F1isnotB2counterpart. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 658 | - **Intra-EU acquisitions**: physical goods from a supplier in another member state. The base goes to line B2, the output tax into the rate block, the same tax again as a memo at line 17, and the input VAT to line 20 or line 19. Line F1 is not a counterpart of line B2. It carries intra-EU acquisitions that are not taxed, and an acquisition already declared on line B2 must never also be put on line F1. | ## The taxable base nativeLF150; ## The taxable base nativeLF116 | Retained / corrected in current Guide: B2/output/memo17/19or20 distinction retained; F1isnotB2counterpart. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 660 | ### 5.10 Autoliquidation: non-EU services and imports | ## The taxable base nativeLF149; ## The taxable base nativeLF151 | Retained / corrected in current Guide: NonEUservices and goodsimports separate; A4/importIblock/deduction/memo24/customsreconciliation retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 662 | - **Non-EU services and imports**: a service bought from a supplier established outside the European Union follows 5.8 above and goes to line A3, not to a separate line. For goods, import VAT is declared and deducted on the CA3. The net amount goes to line A4 for goods other than petroleum products, the tax into the import block at lines I1 to I6, and the deductible part is shown at line 24 as well as being included in line 20 or line 19. The CA3 return is pre-filled with the customs data available to the administration, so reconcile it against the client's own import records before filing. | ## The taxable base nativeLF149; ## The taxable base nativeLF151 | Retained / corrected in current Guide: NonEUservices and goodsimports separate; A4/importIblock/deduction/memo24/customsreconciliation retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 664 | ### 5.11 Capital goods (immobilisations) | ## The taxable base nativeLF170 | Retained / corrected in current Guide: Optional500equipment accounting tolerance, aggregation and movable5/immovable20year actualadjustment conditions retained, not mandatory assetthreshold. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 666 | - **Capital goods**: input VAT on goods recorded as fixed assets goes to line 19 and everything else goes to line 20. What makes a small item a fixed asset rather than an expense is the tolerance below. Capital goods can be subject to a later adjustment of the deduction, over five years for movable property and twenty years for immovable property, if the use changes. | ## The taxable base nativeLF170 | Retained / corrected in current Guide: Optional500equipment accounting tolerance, aggregation and movable5/immovable20year actualadjustment conditions retained, not mandatory assetthreshold. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 668 | &#124; What &#124; Value &#124; Note &#124; | ## The taxable base nativeLF170 | Retained / corrected in current Guide: Optional500equipment accounting tolerance, aggregation and movable5/immovable20year actualadjustment conditions retained, not mandatory assetthreshold. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 669 | &#124; --- &#124; --- &#124; --- &#124; | ## The taxable base nativeLF170 | Retained / corrected in current Guide: Optional500equipment accounting tolerance, aggregation and movable5/immovable20year actualadjustment conditions retained, not mandatory assetthreshold. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 670 | &#124; Source &#124; all figures below &#124; https://bofip.impots.gouv.fr/bofip/2109-PGP.html &#124; | ## The taxable base nativeLF170 | Retained / corrected in current Guide: Optional500equipment accounting tolerance, aggregation and movable5/immovable20year actualadjustment conditions retained, not mandatory assetthreshold. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 671 | &#124; Small equipment and tooling, unit value excluding VAT at or below this amount, may be taken straight to expense &#124; EUR 500 &#124; "des matériels et outillages d'une valeur unitaire hors taxes n'excédant pas 500 €" &#124; | ## The taxable base nativeLF170 | Retained / corrected in current Guide: Optional500equipment accounting tolerance, aggregation and movable5/immovable20year actualadjustment conditions retained, not mandatory assetthreshold. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 673 | That tolerance is a business-profits rule, not a VAT rule: it decides whether the item is an asset in the accounts, and the CA3 line then follows the accounting treatment. Where several parts are bought separately but form one item, the page says the global price is what counts. | ## The taxable base nativeLF170 | Retained / corrected in current Guide: Optional500equipment accounting tolerance, aggregation and movable5/immovable20year actualadjustment conditions retained, not mandatory assetthreshold. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 675 | ### 5.12 Blocked input VAT (Art. 206 Annexe II CGI and related) | ## The taxable base nativeLF160; ## The taxable base nativeLF161 | Retained / corrected in current Guide: Designatpurchase/lease, cycle/quad and all named exceptions retained; individual exclusive-use gates replace old universalexclusiveassertion. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 677 | - **Passenger vehicles.** Vehicles and engines of any kind designed to carry people or for mixed use, which are a fixed asset or are not intended to be resold new, are excluded from the right to deduct, and so are their component parts, spares and accessories. The test is design, judged at acquisition or at taking on lease, not actual use. Cycles and leisure quads are caught unless they have fittings that make them exclusively goods carriers, and a cargo bike built to carry bulky goods is given as the example of one that is not caught. Source: https://bofip.impots.gouv.fr/bofip/1192-PGP.html | ## The taxable base nativeLF160; ## The taxable base nativeLF161 | Retained / corrected in current Guide: Designatpurchase/lease, cycle/quad and all named exceptions retained; individual exclusive-use gates replace old universalexclusiveassertion. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 678 | - **When a passenger vehicle is nevertheless deductible.** The same page carries a section headed "II. Exceptions à la mesure d’exclusion". A vehicle bought to be resold new is outside the exclusion, so dealers deduct. Beyond that the page allows deduction for: racing sailboats; vehicles with more than eight seats besides the driver used to bring staff to work; vehicles of a public passenger transport undertaking used exclusively for that transport, a rule the page extends in terms to "transports publics particuliers de personnes" (taxis, voitures de transport avec chauffeur, two- and three-wheel vehicles); vehicles used exclusively for teaching driving, where the page lets the business deduct the VAT on vehicles "qui sont affectés de façon exclusive à l’enseignement de la conduite"; hearses, where "Les véhicules aménagés en corbillards, utilisés exclusivement à des transports funéraires par les entrepreneurs de pompes funèbres" open a right to deduct; all-terrain vehicles used exclusively by a ski-lift or ski-domain operator; aeroplanes and helicopters used to supply air services for consideration; and, from 1 January 2024, vehicles fitted to transport horses. Renting vehicles out is itself an activity that authorises deduction, the page listing alongside public passenger transport "la location de véhicules lorsque ces opérations de location sont soumises à la TVA". Each exception turns on exclusive use for the qualifying activity, so check the actual use before claiming. Source: https://bofip.impots.gouv.fr/bofip/1192-PGP.html | ## The taxable base nativeLF160; ## The taxable base nativeLF161 | Retained / corrected in current Guide: Designatpurchase/lease, cycle/quad and all named exceptions retained; individual exclusive-use gates replace old universalexclusiveassertion. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 679 | - **Fuel.** The limitation applies only where the product is used by the buyer as fuel to propel vehicles and engines, with an exception for petrol, diesel and superéthanol E85 used as fuel in tests carried out to manufacture engines. Shares are in the table below. | ## Rates, bands and thresholds nativeLF78; ## Rates, bands and thresholds nativeLF79; ## The taxable base nativeLF162; ## The taxable base nativeLF164 | Retained / corrected in current Guide: 80/100/50shares, hiredvehicle, manufacturingtests, liquefied/naturalgas ordinaryrules and jetfuel exclusion/actualexceptions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 681 | &#124; Fuel and the vehicle it is used in &#124; Deductible share &#124; Note &#124; | ## Rates, bands and thresholds nativeLF78; ## Rates, bands and thresholds nativeLF79; ## The taxable base nativeLF162; ## The taxable base nativeLF164 | Retained / corrected in current Guide: 80/100/50shares, hiredvehicle, manufacturingtests, liquefied/naturalgas ordinaryrules and jetfuel exclusion/actualexceptions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 682 | &#124; --- &#124; --- &#124; --- &#124; | ## Rates, bands and thresholds nativeLF78; ## Rates, bands and thresholds nativeLF79; ## The taxable base nativeLF162; ## The taxable base nativeLF164 | Retained / corrected in current Guide: 80/100/50shares, hiredvehicle, manufacturingtests, liquefied/naturalgas ordinaryrules and jetfuel exclusion/actualexceptions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 683 | &#124; Source &#124; all figures below &#124; https://bofip.impots.gouv.fr/bofip/1194-PGP.html &#124; | ## Rates, bands and thresholds nativeLF78; ## Rates, bands and thresholds nativeLF79; ## The taxable base nativeLF162; ## The taxable base nativeLF164 | Retained / corrected in current Guide: 80/100/50shares, hiredvehicle, manufacturingtests, liquefied/naturalgas ordinaryrules and jetfuel exclusion/actualexceptions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 684 | &#124; Petrol, diesel and superéthanol E85 used in a vehicle or engine excluded from the right to deduct, from 1 January 2022 &#124; 80% &#124; "1 er janvier 2022 80 % 80 % 100 %": first column of the row dated 1 January 2022 in the page's own table, which is printed for essences &#124; | ## Rates, bands and thresholds nativeLF78; ## Rates, bands and thresholds nativeLF79; ## The taxable base nativeLF162; ## The taxable base nativeLF164 | Retained / corrected in current Guide: 80/100/50shares, hiredvehicle, manufacturingtests, liquefied/naturalgas ordinaryrules and jetfuel exclusion/actualexceptions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 685 | &#124; The same fuels in a vehicle taken on lease where the lessee cannot deduct the tax on the lease, from 1 January 2022 &#124; 80% &#124; Second column of the same row &#124; | ## Rates, bands and thresholds nativeLF78; ## Rates, bands and thresholds nativeLF79; ## The taxable base nativeLF162; ## The taxable base nativeLF164 | Retained / corrected in current Guide: 80/100/50shares, hiredvehicle, manufacturingtests, liquefied/naturalgas ordinaryrules and jetfuel exclusion/actualexceptions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 686 | &#124; The same fuels in any other vehicle or engine, from 1 January 2022 &#124; 100% &#124; Third column of the same row. That table is printed for essences; for gazoles and superéthanol E85 the same page reaches the same shares in words, "Les redevables peuvent porter en déduction 80 % du montant de la taxe grevant les dépenses de gazole utilisé comme carburant pour les véhicules exclus du droit à déduction" &#124; | ## Rates, bands and thresholds nativeLF78; ## Rates, bands and thresholds nativeLF79; ## The taxable base nativeLF162; ## The taxable base nativeLF164 | Retained / corrected in current Guide: 80/100/50shares, hiredvehicle, manufacturingtests, liquefied/naturalgas ordinaryrules and jetfuel exclusion/actualexceptions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 687 | &#124; Petroleum gases and other hydrocarbons in gaseous form other than natural gas, and lamp oil, used in a vehicle excluded from the right to deduct or in a lease the lessee cannot deduct &#124; 50% &#124; "Cette limite est fixée à 50 % du montant de la taxe pour les produits utilisés dans des véhicules ou engins exclus du droit à déduction" &#124; | ## Rates, bands and thresholds nativeLF78; ## Rates, bands and thresholds nativeLF79; ## The taxable base nativeLF162; ## The taxable base nativeLF164 | Retained / corrected in current Guide: 80/100/50shares, hiredvehicle, manufacturingtests, liquefied/naturalgas ordinaryrules and jetfuel exclusion/actualexceptions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 689 | Where those gaseous products are liquefied, and for natural gas, the same page says ordinary law applies rather than that limit. Jet fuel used in aircraft that do not give a right to deduct is excluded outright. | ## Rates, bands and thresholds nativeLF78; ## Rates, bands and thresholds nativeLF79; ## The taxable base nativeLF162; ## The taxable base nativeLF164 | Retained / corrected in current Guide: 80/100/50shares, hiredvehicle, manufacturingtests, liquefied/naturalgas ordinaryrules and jetfuel exclusion/actualexceptions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 691 | - **Accommodation.** VAT is not deductible on goods or services incurred to house directors or staff free of charge, and that includes buying or renting the premises. Where the same spending houses both third parties, which does give a right to deduct, and directors or employees, which does not, the administration allows the coefficient to be set in proportion to the number of people in each group. Source: https://bofip.impots.gouv.fr/bofip/1190-PGP.html | ## The taxable base nativeLF165 | Retained / corrected in current Guide: Free staff/director housing, actual onsiteguardexception and mixedheadcount conditions retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 692 | - **Goods given away.** VAT is not deductible on goods handed over without payment or for a price far below the normal one, whatever the recipient's status and whatever the form of the distribution, except where the goods are of very low value. The exception is defined by reference to the amount fixed by article 28-00 A of Annexe IV to the CGI, assessed inclusive of all taxes, per object and per year for the same beneficiary, and revalued every five years. Earlier versions of this skill printed a figure for that limit. No page on an allowed host prints it, so it is not printed here: read the current amount off the article before advising. Until that amount is confirmed, block the deduction: the conservative default for an unknown blocked-input status in Section 1 applies. Source: https://bofip.impots.gouv.fr/bofip/1196-PGP.html | ## The taxable base nativeLF166; ## Sources nativeLF378; ## The taxable base nativeLF172 | Retained exclusion; actual published73TTCexception now supplied: Gift exclusion and perbeneficiary/object/year scope retained. FR-L44 actuallyreadofficialconsolidated9October2026text: inclusive73TTC. The prior unreadamount reservation is superseded; ordinary eligibility and evidence remain. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 693 | - **Personal use.** VAT on goods and services used privately by third parties, directors or staff is not deductible. The fuel page gives the example of diesel bought for a director's private journeys. | ## The taxable base nativeLF167; ## The taxable base nativeLF168 | Retained / corrected in current Guide: Privateuse exclusion and conditional ordinarybusinessmeal recovery retained; business facts/invoice stillrequired. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 694 | - **Restaurant costs** are not on the exclusion list. See Example 3. | ## The taxable base nativeLF167; ## The taxable base nativeLF168 | Retained / corrected in current Guide: Privateuse exclusion and conditional ordinarybusinessmeal recovery retained; business facts/invoice stillrequired. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 696 | ### 5.13 Régime réel simplifié (CA12) | ## Deadlines and filing nativeLF216; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF218 | Retained / corrected in current Guide: Annual/calendar and offcalendar deadline, JulyDecemberinstalments, priorVATtrigger and annualdata aggregation retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 698 | - **Régime réel simplifié**: the business files one annual CA12 or CA12E covering the previous calendar year, due at the latest on the second working day following 1 May, and pays two instalments in July and December at the percentages in the regime table above. Where its accounting year does not end on 31 December, the return is due within three months of the year end and the instalment dates follow the month the previous return was filed. Where the VAT declared for the previous year is above the VAT limit in that table, the business files monthly CA3 returns instead. This skill can prepare the CA12 data: accumulate the monthly or quarterly totals into annual figures. | ## Deadlines and filing nativeLF216; ## Deadlines and filing nativeLF217; ## Deadlines and filing nativeLF218 | Retained / corrected in current Guide: Annual/calendar and offcalendar deadline, JulyDecemberinstalments, priorVATtrigger and annualdata aggregation retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 700 | ### 5.14 Sales: local domestic (any rate) | ## The taxable base nativeLF102; ## The taxable base nativeLF120; ## The taxable base nativeLF122 | Retained / corrected in current Guide: Domestic output base and actual rateblock includingT6 retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 702 | - **Sales local domestic**: charge the rate that fits the supply from the rate tables in Section 1, put the net on line A1, and the base and tax in the matching rate line, 08, 09, 9B or T6. | ## The taxable base nativeLF102; ## The taxable base nativeLF120; ## The taxable base nativeLF122 | Retained / corrected in current Guide: Domestic output base and actual rateblock includingT6 retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 704 | ### 5.15 Sales: cross-border B2C | ## Cross-border points nativeLF256; ## Rates, bands and thresholds nativeLF75 | Retained / corrected in current Guide: Qualified BOTH-year/soleestablishment/goodsdispatch/option10kselector replaces oldsingleyear shortcut. OSSisconditionalroute, not unconditionalduty. Buyeracquisition10k remainsseparate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 706 | - **Sales cross-border to consumers**: distance sales of goods to consumers in other member states, and cross-border digital services to consumers, are taxable in France while the annual total stays at or below the limit below, and taxable in the member state of destination above it or if the supplier opts. Above the limit, or on an option, **R-EU-5 (OSS refusal) from `eu-vat-directive` fires**. On the CA3, sales taxable in the destination state go on line E3. _(R-EU-5)_ | ## Cross-border points nativeLF256; ## Rates, bands and thresholds nativeLF75 | Retained / corrected in current Guide: Qualified BOTH-year/soleestablishment/goodsdispatch/option10kselector replaces oldsingleyear shortcut. OSSisconditionalroute, not unconditionalduty. Buyeracquisition10k remainsseparate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 708 | &#124; What &#124; Value &#124; Note &#124; | ## Cross-border points nativeLF256; ## Rates, bands and thresholds nativeLF75 | Retained / corrected in current Guide: Qualified BOTH-year/soleestablishment/goodsdispatch/option10kselector replaces oldsingleyear shortcut. OSSisconditionalroute, not unconditionalduty. Buyeracquisition10k remainsseparate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 709 | &#124; --- &#124; --- &#124; --- &#124; | ## Cross-border points nativeLF256; ## Rates, bands and thresholds nativeLF75 | Retained / corrected in current Guide: Qualified BOTH-year/soleestablishment/goodsdispatch/option10kselector replaces oldsingleyear shortcut. OSSisconditionalroute, not unconditionalduty. Buyeracquisition10k remainsseparate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 710 | &#124; Source &#124; all figures below &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf &#124; | ## Cross-border points nativeLF256; ## Rates, bands and thresholds nativeLF75 | Retained / corrected in current Guide: Qualified BOTH-year/soleestablishment/goodsdispatch/option10kselector replaces oldsingleyear shortcut. OSSisconditionalroute, not unconditionalduty. Buyeracquisition10k remainsseparate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 711 | &#124; Annual total of distance sales from France to other member states, at or below which they stay taxable in France &#124; EUR 10,000 &#124; "ventes de la France vers d'autres États membres si leur montant global annuel est inférieur ou égal à 10 000 €" &#124; | ## Cross-border points nativeLF256; ## Rates, bands and thresholds nativeLF75 | Retained / corrected in current Guide: Qualified BOTH-year/soleestablishment/goodsdispatch/option10kselector replaces oldsingleyear shortcut. OSSisconditionalroute, not unconditionalduty. Buyeracquisition10k remainsseparate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 713 | This is a different limit from the intra-EU acquisitions limit in the franchise table above, even though the amount is the same. One is about a franchised buyer's purchases of goods, the other about a seller's distance sales. Do not use one to prove the other. | ## Cross-border points nativeLF256; ## Rates, bands and thresholds nativeLF75 | Retained / corrected in current Guide: Qualified BOTH-year/soleestablishment/goodsdispatch/option10kselector replaces oldsingleyear shortcut. OSSisconditionalroute, not unconditionalduty. Buyeracquisition10k remainsseparate. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 715 | ## Section 6: Tier 2 catalogue (compressed) | ## The taxable base nativeLF196; ## The taxable base nativeLF162; ## Rates, bands and thresholds nativeLF78; ## Rates, bands and thresholds nativeLF79 | Retained / corrected in current Guide: Fueltype/vehicledesign questions, chargingordinaryrules and temporaryevidencehold retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 717 | ### 6.1 Fuel and vehicle costs | ## The taxable base nativeLF196; ## The taxable base nativeLF162; ## Rates, bands and thresholds nativeLF78; ## Rates, bands and thresholds nativeLF79 | Retained / corrected in current Guide: Fueltype/vehicledesign questions, chargingordinaryrules and temporaryevidencehold retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 719 | - **Fuel and vehicle costs**: pattern TOTAL, SHELL, BP, ESSO, AVIA, fuel receipts. Why insufficient: the deductible share turns on whether the vehicle is excluded from the right to deduct. Default: no recovery. Question: "Was this vehicle designed to carry people, or to carry goods? And what fuel was it, petrol, diesel, superéthanol E85, or a petroleum gas?" Then apply the fuel table in Section 5.12. Charging an electric vehicle is not one of the products the fuel restriction names, so it falls under the ordinary deduction rules rather than the table, and the vehicle's own exclusion still has to be settled first. | ## The taxable base nativeLF196; ## The taxable base nativeLF162; ## Rates, bands and thresholds nativeLF78; ## Rates, bands and thresholds nativeLF79 | Retained / corrected in current Guide: Fueltype/vehicledesign questions, chargingordinaryrules and temporaryevidencehold retained. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 721 | ### 6.2 Restaurants and entertainment | ## The taxable base nativeLF168; ## The taxable base nativeLF196 | Retained / corrected in current Guide: Purpose/attendees question and ordinaryeligibility; no automatic permanentrestaurantblock. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 723 | - **Restaurants and entertainment**: pattern any named restaurant, brasserie, café, traiteur. Why insufficient: France does not exclude restaurant costs by name, but the expense still has to be for the needs of the business and personal meals are blocked. Default: block. Question: "Was this a business meal with external guests? If yes, who was present and what was the business purpose?" | ## The taxable base nativeLF168; ## The taxable base nativeLF196 | Retained / corrected in current Guide: Purpose/attendees question and ordinaryeligibility; no automatic permanentrestaurantblock. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 725 | ### 6.3 Ambiguous SaaS billing entities | ## The taxable base nativeLF187; ## The taxable base nativeLF196; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Actual SaaS entity/country/lawfultax question, no guessedA3default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 727 | - **Ambiguous SaaS billing entities**: pattern Google, Microsoft, Adobe, Meta, Slack, Zoom, LinkedIn, Apple, Amazon, Dropbox, Atlassian, Stripe, PayPal. Why insufficient: the same brand can bill from Ireland, from the United States, or from France. Default: line A3 plus line 20. Question: "Could you check the invoice? I need the legal entity name, its country, and whether any French TVA was charged." | ## The taxable base nativeLF187; ## The taxable base nativeLF196; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Actual SaaS entity/country/lawfultax question, no guessedA3default. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 729 | ### 6.4 Round-number incoming transfers from owner-named counterparties | ## The taxable base nativeLF196; ## The taxable base nativeLF172; ## The taxable base nativeLF180 | Retained / corrected in current Guide: Ownerlooking/name/foreignreceipt topics retained as sale-versuscapital/loan, customerstatus/country questions, not inventedownerinjection/domesticconsumer20. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 731 | - **Round-number incoming transfers**: pattern a large round credit from a name matching the client's name. Default: exclude as an owner injection (apport personnel). Question: "That transfer from this name, is it a customer payment, your own money going in, or a loan?" | ## The taxable base nativeLF196; ## The taxable base nativeLF172; ## The taxable base nativeLF180 | Retained / corrected in current Guide: Ownerlooking/name/foreignreceipt topics retained as sale-versuscapital/loan, customerstatus/country questions, not inventedownerinjection/domesticconsumer20. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 733 | ### 6.5 Incoming transfers from individual names (not owner) | ## The taxable base nativeLF196; ## The taxable base nativeLF172; ## The taxable base nativeLF180 | Retained / corrected in current Guide: Ownerlooking/name/foreignreceipt topics retained as sale-versuscapital/loan, customerstatus/country questions, not inventedownerinjection/domesticconsumer20. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 735 | - **Incoming transfers from individual names**: pattern incoming from private-looking counterparties. Default: a domestic sale to a consumer at the standard rate, line A1 with the tax at line 08. Question: "For each: was it a sale? Business or consumer customer? Which country?" | ## The taxable base nativeLF196; ## The taxable base nativeLF172; ## The taxable base nativeLF180 | Retained / corrected in current Guide: Ownerlooking/name/foreignreceipt topics retained as sale-versuscapital/loan, customerstatus/country questions, not inventedownerinjection/domesticconsumer20. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 737 | ### 6.6 Incoming transfers from foreign counterparties | ## The taxable base nativeLF196; ## The taxable base nativeLF172; ## The taxable base nativeLF180 | Retained / corrected in current Guide: Ownerlooking/name/foreignreceipt topics retained as sale-versuscapital/loan, customerstatus/country questions, not inventedownerinjection/domesticconsumer20. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 739 | - **Incoming transfers from foreign counterparties**: pattern a foreign IBAN or a foreign currency. Default: domestic at the standard rate. Question: "What was this: business with a VAT number, or a consumer? Goods or services, and which country?" | ## The taxable base nativeLF196; ## The taxable base nativeLF172; ## The taxable base nativeLF180 | Retained / corrected in current Guide: Ownerlooking/name/foreignreceipt topics retained as sale-versuscapital/loan, customerstatus/country questions, not inventedownerinjection/domesticconsumer20. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 741 | ### 6.7 Large one-off purchases (potential immobilisations) | ## The taxable base nativeLF170; ## The taxable base nativeLF196 | Retained / corrected in current Guide: Oneoffequipmentinvoice, net/globalprice and actualcapitalisation questions retained; optional500isnotuniversalcutoff. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 743 | - **Large one-off purchases**: pattern a single invoice near the small-equipment tolerance in Section 5.11, or labelled laptop, equipment, machinery. Default: above the tolerance, line 19; at or below it, line 20. Question: "Could you confirm the total invoice amount and the amount excluding VAT?" | ## The taxable base nativeLF170; ## The taxable base nativeLF196 | Retained / corrected in current Guide: Oneoffequipmentinvoice, net/globalprice and actualcapitalisation questions retained; optional500isnotuniversalcutoff. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 745 | ### 6.8 Mixed-use phone, internet, home office | ## The taxable base nativeLF196; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Dedicatedversusmixedphone/homeuse and documentedbusinessshare retained; evidencehold not permanentdenial. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 747 | - **Mixed-use phone, internet, home office**: pattern Orange, Free, SFR personal lines, home electricity. Default: no recovery where the use is mixed and no percentage is declared. Question: "Is this a dedicated business line or mixed use? What business percentage?" | ## The taxable base nativeLF196; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Dedicatedversusmixedphone/homeuse and documentedbusinessshare retained; evidencehold not permanentdenial. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 749 | ### 6.9 Outgoing transfers to individuals | ## The taxable base nativeLF196; ## The taxable base nativeLF192 | Retained / corrected in current Guide: Contractor/wage/refund/privateoutgoing and cashuse questions retained; unknownindividualname/cashisnotproofdrawings. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 751 | - **Outgoing transfers to individuals**: pattern outgoing to private-looking names. Default: exclude as drawings. Question: "Was this a contractor payment with an invoice, wages, a refund, or a personal transfer?" | ## The taxable base nativeLF196; ## The taxable base nativeLF192 | Retained / corrected in current Guide: Contractor/wage/refund/privateoutgoing and cashuse questions retained; unknownindividualname/cashisnotproofdrawings. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 753 | ### 6.10 Cash withdrawals | ## The taxable base nativeLF196; ## The taxable base nativeLF192 | Retained / corrected in current Guide: Contractor/wage/refund/privateoutgoing and cashuse questions retained; unknownindividualname/cashisnotproofdrawings. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 755 | - **Cash withdrawals**: pattern DAB, retrait espèces, retrait guichet. Default: exclude as an owner drawing. Question: "What was the cash used for?" | ## The taxable base nativeLF196; ## The taxable base nativeLF192 | Retained / corrected in current Guide: Contractor/wage/refund/privateoutgoing and cashuse questions retained; unknownindividualname/cashisnotproofdrawings. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 757 | ### 6.11 Rent payments | ## The taxable base nativeLF191; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Commercial/residentialnature and actualVAToption evidence retained; no guessedresidentialdefault. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 759 | - **Rent payments**: pattern loyer, bail, a monthly payment to a landlord-sounding counterparty. Default: no VAT, the residential default. Question: "Is this a commercial property where the landlord has exercised the option for TVA?" | ## The taxable base nativeLF191; ## The taxable base nativeLF172 | Retained / corrected in current Guide: Commercial/residentialnature and actualVAToption evidence retained; no guessedresidentialdefault. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 761 | ### 6.12 Foreign hotel and accommodation | ## The taxable base nativeLF196; ## Rates, bands and thresholds nativeLF65 | Retained / corrected in current Guide: Foreignhotel nonFrenchinput/refundandbusinesspurpose; Airbnbfurnishednature/classification/serviceband questions retained. Detailed furnished-exemption/propertyrules remainreferred. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 763 | - **Foreign hotel and accommodation**: pattern a hotel or accommodation charged abroad. Default: exclude from input VAT on the CA3, because foreign VAT is not French input VAT. Question: "Was this a business trip?" A refund claim in the other country may be possible, and the cost is still an expense for income tax. | ## The taxable base nativeLF196; ## Rates, bands and thresholds nativeLF65 | Retained / corrected in current Guide: Foreignhotel nonFrenchinput/refundandbusinesspurpose; Airbnbfurnishednature/classification/serviceband questions retained. Detailed furnished-exemption/propertyrules remainreferred. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 765 | ### 6.13 Airbnb income | ## The taxable base nativeLF196; ## Rates, bands and thresholds nativeLF65 | Retained / corrected in current Guide: Foreignhotel nonFrenchinput/refundandbusinesspurpose; Airbnbfurnishednature/classification/serviceband questions retained. Detailed furnished-exemption/propertyrules remainreferred. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 767 | - **Airbnb income**: pattern Airbnb payouts. Default: flag for the reviewer. Question: "Is this furnished letting? What duration, and is it classified tourist accommodation?" Furnished letting sits in the services band of the regime table, which the page marks out expressly. | ## The taxable base nativeLF196; ## Rates, bands and thresholds nativeLF65 | Retained / corrected in current Guide: Foreignhotel nonFrenchinput/refundandbusinesspurpose; Airbnbfurnishednature/classification/serviceband questions retained. Detailed furnished-exemption/propertyrules remainreferred. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 769 | ### 6.14 Subcontractor reverse charge (construction) | ## The taxable base nativeLF152; ## The taxable base nativeLF103; ## The taxable base nativeLF113; ## The taxable base nativeLF188; ## Cross-border points nativeLF256 | Retained / corrected in current Guide: Constructionrecipient/subcontractor routing, platformgrosssalesversusfee distinction and qualifieddestinationsalesmethod retained; actualbillingfactsrequired. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 771 | - **Subcontractor reverse charge**: pattern payments to construction subcontractors. Why insufficient: construction work, including repair, cleaning, maintenance and demolition carried out in relation to immovable property, is subject to a domestic reverse charge under CGI art. 283-2 nonies. The subcontractor invoices without VAT and the main contractor accounts for it. The CA3 notes list those works among the operations to be shown at line E2 by the subcontractor. Default: flag for the reviewer. Question: "Is this a construction subcontractor inside the domestic reverse charge?" _(CGI art. 283-2 nonies)_ | ## The taxable base nativeLF152; ## The taxable base nativeLF103; ## The taxable base nativeLF113; ## The taxable base nativeLF188; ## Cross-border points nativeLF256 | Retained / corrected in current Guide: Constructionrecipient/subcontractor routing, platformgrosssalesversusfee distinction and qualifieddestinationsalesmethod retained; actualbillingfactsrequired. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 773 | ### 6.15 Platform sales (Amazon, eBay, Etsy) | ## The taxable base nativeLF152; ## The taxable base nativeLF103; ## The taxable base nativeLF113; ## The taxable base nativeLF188; ## Cross-border points nativeLF256 | Retained / corrected in current Guide: Constructionrecipient/subcontractor routing, platformgrosssalesversusfee distinction and qualifieddestinationsalesmethod retained; actualbillingfactsrequired. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 775 | - **Platform sales**: pattern incoming from Amazon Payments EU, Etsy Payments, PayPal, Stripe. Default: where the client sells to consumers across several member states above the distance-selling limit in Section 5.15, R-EU-5 fires. For France-only sales or sales below that limit, treat the gross as a domestic sale on line A1 at the applicable rate, and the platform fees as a service bought from a supplier not established in France on line A3. Question: "Do you sell to buyers outside France? What were your total cross-border sales to consumers for the year?" _(R-EU-5)_ | ## The taxable base nativeLF152; ## The taxable base nativeLF103; ## The taxable base nativeLF113; ## The taxable base nativeLF188; ## Cross-border points nativeLF256 | Retained / corrected in current Guide: Constructionrecipient/subcontractor routing, platformgrosssalesversusfee distinction and qualifieddestinationsalesmethod retained; actualbillingfactsrequired. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 777 | ## Section 7: Excel working paper template (France-specific) | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 779 | The base specification is in `vat-workflow-base` Section 3. This section gives the France-specific overlay. The line codes below are the 2026 CA3 codes from Section 1. | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 781 | ### Sheet "Transactions" | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 783 | Columns A to L per the base. Column H, the line code, accepts only valid CA3 line codes from Section 1 of this skill. Leave it blank for excluded transactions. For a transaction that is self-assessed, enter the base line and the deduction line separated by a slash in column H, for example A3/20. | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 785 | ### Sheet "Line Summary" | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 787 | One row per line. Column A is the line code, column B is the description, column C is the value computed by formula. Mandatory rows: | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 789 | ~~~ | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 790 | Operations, cadre A, taxed and non-taxed sides: | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 791 | &#124; A1 &#124; Taxable sales and services, net   &#124; =SUMIFS(Transactions!E:E, Transactions!H:H, "A1")  &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 792 | &#124; E1 &#124; Exports outside the EU            &#124; =SUMIFS(Transactions!E:E, Transactions!H:H, "E1")  &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 793 | &#124; E2 &#124; Other non-taxable operations      &#124; =SUMIFS(Transactions!E:E, Transactions!H:H, "E2")  &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 794 | &#124; E3 &#124; Distance sales taxed elsewhere    &#124; =SUMIFS(Transactions!E:E, Transactions!H:H, "E3")  &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 795 | &#124; F2 &#124; Intra-EU supplies of goods, B to B&#124; =SUMIFS(Transactions!E:E, Transactions!H:H, "F2")  &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 797 | Self-assessed bases: | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 798 | &#124; A3 &#124; Services from a supplier not established in France &#124; =SUMIFS(Transactions!E:E, Transactions!H:H, "A3") &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 799 | &#124; A4 &#124; Imports, net                                       &#124; =SUMIFS(Transactions!E:E, Transactions!H:H, "A4") &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 800 | &#124; B2 &#124; Intra-EU acquisitions of goods, net                &#124; =SUMIFS(Transactions!E:E, Transactions!H:H, "B2") &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 801 | &#124; B4 &#124; Goods or services, supplier not established        &#124; =SUMIFS(Transactions!E:E, Transactions!H:H, "B4") &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 803 | Gross tax block, base and tax: | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 804 | &#124; 08 &#124; Standard rate       &#124; base * standard rate     &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 805 | &#124; 09 &#124; Reduced rate        &#124; base * reduced rate      &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 806 | &#124; 9B &#124; Intermediate rate   &#124; base * intermediate rate &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 807 | &#124; I1 to I6 &#124; Import tax, one row per rate, base and tax &#124; =SUMIFS(Transactions!E:E, Transactions!H:H, "I1") and so on &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 808 | &#124; 16 &#124; Total gross tax due, every gross-tax line from 08 to 5B &#124; =SUM(08,09,9B,10,11,T1,T2,TC,T3,T4,T5,T6,T7,13,P1,P2,I1,I2,I3,I4,I5,I6,15,5B) &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 809 | &#124; 17 &#124; Memo: of which on intra-EU acquisitions &#124; manual &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 811 | Deductible tax: | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 812 | &#124; 19 &#124; Capital goods                     &#124; =SUMIFS(Transactions!F:F, Transactions!H:H, "19") &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 813 | &#124; 20 &#124; Other goods and services          &#124; =SUMIFS(Transactions!F:F, Transactions!H:H, "20") &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 814 | &#124; 22 &#124; Credit carried forward from line 27 of the previous return &#124; manual &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 815 | &#124; 23 &#124; Total deductible tax, lines 19 to 2C &#124; =SUM(19,20,21,22,2C)                          &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 816 | &#124; 24 &#124; Memo: of which on imports         &#124; manual                                            &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 818 | Bottom of the return: | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 819 | &#124; 25 &#124; Credit de TVA   &#124; =MAX(0, C[23]-C[16]) &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 820 | &#124; TD &#124; TVA due         &#124; =MAX(0, C[16]-C[23]) &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 821 | &#124; 26 &#124; Refund claimed on form 3519 &#124; manual   &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 822 | &#124; 27 &#124; Credit carried forward      &#124; =C[25]-C[26] &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 823 | &#124; 28 &#124; TVA nette due   &#124; =C[TD]               &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 824 | &#124; 32 &#124; Total to pay    &#124; =C[28]+C[29]         &#124; | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 825 | ~~~ | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 827 | ### Sheet "Return Form" | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 829 | Final CA3-ready figures. | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 831 | ~~~ | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 832 | IF line 23 > line 16: | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 833 |   Line 25 = credit de TVA | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 834 |   Line TD = 0 | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 835 |   Line 27 = line 25 less line 26, carried to line 22 of the next return | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 836 | ELSE: | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 837 |   Line 25 = 0 | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 838 |   Line TD = line 16 less line 23 | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 839 |   Line 28 = line TD less any energy excise credit | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 840 |   Line 32 = line 28 plus line 29 plus any energy excise due | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 841 | ~~~ | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 843 | A credit position at line 25 does not excuse paying the assimilated taxes at line 29 or the energy excise: the form says so on its face. | ## The taxable base nativeLF208; ## The taxable base nativeLF98; ## The taxable base nativeLF206 | Retained / corrected in current Guide: Transactions/summary/return sheets, base-versusVAT sums, selfassessmenttwo-sided flow, actualgross/deductiontotals and credit/refund/carry retained. Ordinary28/32 formulas corrected by actualX5/Z5/AB rather than silentlyzeroenergy/group adjustments. SUMIFSsyntax is an implementation example, not an independent legal rule. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 845 | ### Color and formatting conventions | ## The taxable base nativeLF208 | Workflow retained; historical tool path/colour convention explicitly superseded: House colours/uncertainrow marking and mandatoryrecalculation topic retained. Earlier specificcolour scheme and /mnt helperpath are historicaltool conventions, not tax rules or assumed currentinstallation. Current practice marks unresolvedfacts without a guessed taxresult. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 847 | Per the workbook conventions of the spreadsheet builder: blue for hardcoded values, black for formulas, green for cross-sheet references, yellow background for any row where Default? is "Y". (The recalculation helper named below is a tool convention of the workbook builder, not an official requirement.) | ## The taxable base nativeLF208 | Workflow retained; historical tool path/colour convention explicitly superseded: House colours/uncertainrow marking and mandatoryrecalculation topic retained. Earlier specificcolour scheme and /mnt helperpath are historicaltool conventions, not tax rules or assumed currentinstallation. Current practice marks unresolvedfacts without a guessed taxresult. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 849 | ### Mandatory recalc step | ## The taxable base nativeLF208 | Workflow retained; historical tool path/colour convention explicitly superseded: House colours/uncertainrow marking and mandatoryrecalculation topic retained. Earlier specificcolour scheme and /mnt helperpath are historicaltool conventions, not tax rules or assumed currentinstallation. Current practice marks unresolvedfacts without a guessed taxresult. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 851 | After building the workbook, run: | ## The taxable base nativeLF208 | Workflow retained; historical tool path/colour convention explicitly superseded: House colours/uncertainrow marking and mandatoryrecalculation topic retained. Earlier specificcolour scheme and /mnt helperpath are historicaltool conventions, not tax rules or assumed currentinstallation. Current practice marks unresolvedfacts without a guessed taxresult. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 853 | ~~~bash | ## The taxable base nativeLF208 | Workflow retained; historical tool path/colour convention explicitly superseded: House colours/uncertainrow marking and mandatoryrecalculation topic retained. Earlier specificcolour scheme and /mnt helperpath are historicaltool conventions, not tax rules or assumed currentinstallation. Current practice marks unresolvedfacts without a guessed taxresult. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 854 | python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/france-vat-period-working-paper.xlsx | ## The taxable base nativeLF208 | Workflow retained; historical tool path/colour convention explicitly superseded: House colours/uncertainrow marking and mandatoryrecalculation topic retained. Earlier specificcolour scheme and /mnt helperpath are historicaltool conventions, not tax rules or assumed currentinstallation. Current practice marks unresolvedfacts without a guessed taxresult. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 855 | ~~~ | ## The taxable base nativeLF208 | Workflow retained; historical tool path/colour convention explicitly superseded: House colours/uncertainrow marking and mandatoryrecalculation topic retained. Earlier specificcolour scheme and /mnt helperpath are historicaltool conventions, not tax rules or assumed currentinstallation. Current practice marks unresolvedfacts without a guessed taxresult. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 857 | ## Section 8: French bank statement reading guide | ## The taxable base nativeLF194; ## The taxable base nativeLF202 | Retained / corrected in current Guide: CSV/PDF/inputformat, Frenchglossary and transfer/card/directdebit/cheque prefixes retained as recognitionaids, not proof of taxclassification. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 859 | Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these France-specific patterns. | ## The taxable base nativeLF194; ## The taxable base nativeLF202 | Retained / corrected in current Guide: CSV/PDF/inputformat, Frenchglossary and transfer/card/directdebit/cheque prefixes retained as recognitionaids, not proof of taxclassification. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 861 | **CSV format conventions.** French banks typically export CSV with semicolon delimiters and DD/MM/YYYY dates. Common columns: Date, Libellé (description), Débit, Crédit, Solde. Qonto and Revolut use ISO dates. BNP and SG exports may include operation codes. | ## The taxable base nativeLF194; ## The taxable base nativeLF202 | Retained / corrected in current Guide: CSV/PDF/inputformat, Frenchglossary and transfer/card/directdebit/cheque prefixes retained as recognitionaids, not proof of taxclassification. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 863 | **French language variants.** Some descriptions appear in French: loyer (rent), salaire and paie (salary), intérêts (interest), virement (transfer), cotisations (contributions), facture (invoice), remboursement (refund). Treat as the English equivalent. | ## The taxable base nativeLF194; ## The taxable base nativeLF202 | Retained / corrected in current Guide: CSV/PDF/inputformat, Frenchglossary and transfer/card/directdebit/cheque prefixes retained as recognitionaids, not proof of taxclassification. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 865 | **Operation code prefixes.** VIR is a bank transfer, CB a card payment, PRLV a direct debit (prélèvement), CHQ a cheque, REM a cheque deposit, TIP an interbank payment title. The prefix helps classify: CB payments are typically purchases, and incoming VIR credits are typically sales. | ## The taxable base nativeLF194; ## The taxable base nativeLF202 | Retained / corrected in current Guide: CSV/PDF/inputformat, Frenchglossary and transfer/card/directdebit/cheque prefixes retained as recognitionaids, not proof of taxclassification. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 867 | **Internal transfers and exclusions.** Own-account transfers between the client's accounts, labelled "VIR INTERNE" or "virement entre comptes". Always exclude. | ## The taxable base nativeLF180; ## The taxable base nativeLF179; ## The taxable base nativeLF206; ## The taxable base nativeLF194 | Retained / corrected in current Guide: Owntransfer/social/taxpayment topics require actualtransactionproof. Signedbookkeepingrefunds distinct from positiveB5/F8/15/21 returncorrections. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 869 | **Refunds and reversals.** Identify by remboursement, annulation, avoir, storno. Book as a negative on the same line as the original transaction. On the CA3 a credit note to a customer belongs in the régularisations at line B5, and a correction on the non-taxed side at line F8. | ## The taxable base nativeLF180; ## The taxable base nativeLF179; ## The taxable base nativeLF206; ## The taxable base nativeLF194 | Retained / corrected in current Guide: Owntransfer/social/taxpayment topics require actualtransactionproof. Signedbookkeepingrefunds distinct from positiveB5/F8/15/21 returncorrections. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 871 | **URSSAF and social charges.** Monthly or quarterly URSSAF debits are social contributions, not a VATable supply. Always exclude. They can be large: do not confuse them with business purchases. | ## The taxable base nativeLF180; ## The taxable base nativeLF179; ## The taxable base nativeLF206; ## The taxable base nativeLF194 | Retained / corrected in current Guide: Owntransfer/social/taxpayment topics require actualtransactionproof. Signedbookkeepingrefunds distinct from positiveB5/F8/15/21 returncorrections. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 873 | **Tax payments.** Payments appearing as DGFIP, TRESOR PUBLIC or IMPOTS.GOUV are tax settlements, not supplies. Always exclude. | ## The taxable base nativeLF180; ## The taxable base nativeLF179; ## The taxable base nativeLF206; ## The taxable base nativeLF194 | Retained / corrected in current Guide: Owntransfer/social/taxpayment topics require actualtransactionproof. Signedbookkeepingrefunds distinct from positiveB5/F8/15/21 returncorrections. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 875 | **Foreign currency transactions.** Convert to euro at the transaction date rate. Use the rate shown on the bank statement, or the official reference rate the client's accounting policy names, and keep the evidence. | ## The taxable base nativeLF194; ## The taxable base nativeLF172 | Retained / corrected in current Guide: ActualVATexigibility/ECB or permitted consistentcustomsmethod replaces arbitrarytransaction/bankrate. IBANbankcountry doesnotprovecustomerstatus/supplyplace. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 877 | **IBAN country prefix.** FR is France. IE, LU, NL, DE and the other member state prefixes are in the European Union. US, GB, AU and CH are outside it. A French IBAN does not prove a French VAT registration: cross-check every time. | ## The taxable base nativeLF194; ## The taxable base nativeLF172 | Retained / corrected in current Guide: ActualVATexigibility/ECB or permitted consistentcustomsmethod replaces arbitrarytransaction/bankrate. IBANbankcountry doesnotprovecustomerstatus/supplyplace. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 879 | ## Section 9: Onboarding fallback (only when inference fails) | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 881 | ### 9.1 Entity type and trading name | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 883 | - **Entity type and trading name**: inference rule, a sole trader's name often matches the account holder, and company names end in SARL, SAS, EURL or SA. Fallback: "Are you a sole trader (entrepreneur individuel), EURL, SARL, SAS, or other?" | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 885 | ### 9.2 VAT regime | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 887 | - **VAT regime**: inference rule, a client filing a CA3 is in the régime réel normal, and a mention of annual filing points to the régime réel simplifié. Fallback: "Are you in the régime réel normal with a monthly or quarterly CA3, or the régime réel simplifié with an annual CA12?" | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 889 | ### 9.3 TVA number | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 891 | - **TVA number**: inference rule, an FR-format TVA number sometimes appears on invoices. Fallback: "What is your French TVA number? It is FR, two check digits, then the SIREN." | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 893 | ### 9.4 Filing period | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 895 | - **Filing period**: inference rule, the first and last transaction dates. Fallback: "Which month or quarter does this return cover?" | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 897 | ### 9.5 Industry and sector | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 899 | - **Industry and sector**: inference rule, the counterparty mix and the sales descriptions. Fallback: "In one sentence, what does the business do?" | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 901 | ### 9.6 Employees | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 903 | - **Employees**: inference rule, URSSAF and payroll outgoings. Fallback: "Do you have employees?" | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 905 | ### 9.7 Exempt supplies | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 907 | - **Exempt supplies**: inference rule, the presence of medical, financial, educational or residential rental income. Fallback: "Do you make any exempt sales?" If yes and not de minimis, R-FR-2 refuses.  _(R-FR-2)_ | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 909 | ### 9.8 Credit carried forward | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 911 | - **Credit carried forward**: inference rule, not inferable, always ask. Question: "Do you have a credit de TVA from the prior period? It is the figure at line 27 of the last return and it goes to line 22 of this one." | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 913 | ### 9.9 Cross-border customers | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 915 | - **Cross-border customers**: inference rule, foreign IBANs on incoming payments. Fallback: "Do you have customers outside France? In the European Union or outside it? Business or consumer?" | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 917 | ### 9.10 Construction subcontracting | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 919 | - **Construction subcontracting**: inference rule, construction-related counterparties in the payments. Conditional fallback: "Do you subcontract construction work? The domestic reverse charge may apply." | ## The taxable base nativeLF202; ## Ask the client first nativeLF323; ## The taxable base nativeLF196 | Retained / corrected in current Guide: All ten onboarding question subjects restored: identity, regime, VATnumber, actualperiod, activity, employees, exemptsupplies, priorcredit, foreigncustomers, subcontracting. Names/suffixes/bankdates/counterparties/IBANs only promptquestions; they cannot supply missingtaxfacts. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 921 | ## Section 10: Reference material | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 923 | ### Validation status | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 925 | This is the October 2026 refresh of the France VAT return skill, written by the OpenAccountants team. Every figure in it was read off a page on an official French host between 19 September and 19 October 2026, and each table names the page it came from. No accountant has attested it. The CA3 line map, the rates, the franchise thresholds, the regime limits, the instalment percentages and the fuel shares were all corrected in this pass: see the change log. | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 927 | ### Sources | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 929 | **Forms and their completion notes** | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 931 | 1. Form 3310-CA3-SD, the 2026 CA3: https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 932 | 2. Notice 3310-NOT-CA3-SD, how to fill in the CA3 and its annexes: https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 933 | 3. Notice 3517-S-NOT-SD, how to fill in the CA12 and CA12E: https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5424.pdf | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 934 | 3a. Form 3517-S-SD, the 2026 CA12 and CA12E: https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5291.pdf | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 935 | 4. The form's own landing page, which carries every year's version: https://www.impots.gouv.fr/formulaire/3310-ca3-sd/tva-et-taxes-assimilees-regime-du-reel-normal-mini-reel | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 937 | **Regimes, thresholds and dates** | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 939 | 5. Franchise en base de TVA: https://entreprendre.service-public.gouv.fr/vosdroits/F21746 | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 940 | 6. Déclarer et payer la TVA: https://entreprendre.service-public.gouv.fr/vosdroits/F23566 | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 941 | 7. Les régimes d'imposition à la TVA: https://www.impots.gouv.fr/professionnel/les-regimes-dimposition-la-tva | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 942 | 8. Le régime réel normal, dates limites de transmission des CA3: https://www.impots.gouv.fr/le-regime-reel-normal-dates-limites-de-transmission-des-ca3 | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 943 | 9. Mentions obligatoires sur une facture: https://entreprendre.service-public.gouv.fr/vosdroits/F31808 | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 944 | 10. À partir de quand suis-je concerné par la réforme de la facturation électronique: https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 946 | **Rates** | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 948 | 11. Reduced and intermediate rates on services, for the television example only: https://bofip.impots.gouv.fr/bofip/1013-PGP.html | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 949 | 12. The special rate: https://bofip.impots.gouv.fr/bofip/1449-PGP.html | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 950 | 13. Rates in the overseas departments: https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 952 | **Deduction restrictions** | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 954 | 14. Vehicles designed to carry people: https://bofip.impots.gouv.fr/bofip/1192-PGP.html | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 955 | 15. Petroleum products: https://bofip.impots.gouv.fr/bofip/1194-PGP.html | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 956 | 16. Accommodation: https://bofip.impots.gouv.fr/bofip/1190-PGP.html | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 957 | 17. Goods given away: https://bofip.impots.gouv.fr/bofip/1196-PGP.html | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 958 | 18. Small-value equipment taken to expense: https://bofip.impots.gouv.fr/bofip/2109-PGP.html | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 960 | **Companion skills** | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 962 | 19. `vat-workflow-base` for the workflow architecture and `eu-vat-directive` for the EU directive content. `france-einvoice` for electronic invoicing, `france-bookkeeping` for the books behind the return, `fr-business-accounting` for the wider accounting picture, `fr-tax-audit` if the return is already under audit. | ## Sources nativeLF334; # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31; ## Deadlines and filing nativeLF226 | Retained / corrected in current Guide: Sourcecatalogue/companion/validationmetadata preserved here as original historicalprovenance and routed to actual current source table/siblings. An oldlink/readclaim is not a freshsuccessfulfetch; unavailableCA12notice and selectedcurrentlimits remain explicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 964 | ### Known gaps | ## Sources nativeLF378; ## Who this applies to nativeLF46; ## The taxable base nativeLF200; ## Rates, bands and thresholds nativeLF94; ## Deadlines and filing nativeLF214; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: All nine oldlimits given disposition: patternlibrarynonexhaustive, DOM, constructionreferral, giftamount, qualitativeflags, RSIcountertext, personaliseddate, Corsica, audit/penalties. Actualcurrentpenaltymethod supersedes oldno-penaltiesassertion; unresolvedsourcequestionsstayexplicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 966 | 1. The supplier pattern library covers common French and international counterparties but not every local business. | ## Sources nativeLF378; ## Who this applies to nativeLF46; ## The taxable base nativeLF200; ## Rates, bands and thresholds nativeLF94; ## Deadlines and filing nativeLF214; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: All nine oldlimits given disposition: patternlibrarynonexhaustive, DOM, constructionreferral, giftamount, qualitativeflags, RSIcountertext, personaliseddate, Corsica, audit/penalties. Actualcurrentpenaltymethod supersedes oldno-penaltiesassertion; unresolvedsourcequestionsstayexplicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 967 | 2. The overseas departments are refused by R-FR-7. Their rates are listed for recognition only, and VAT is provisionally not applicable in Guyane and Mayotte. | ## Sources nativeLF378; ## Who this applies to nativeLF46; ## The taxable base nativeLF200; ## Rates, bands and thresholds nativeLF94; ## Deadlines and filing nativeLF214; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: All nine oldlimits given disposition: patternlibrarynonexhaustive, DOM, constructionreferral, giftamount, qualitativeflags, RSIcountertext, personaliseddate, Corsica, audit/penalties. Actualcurrentpenaltymethod supersedes oldno-penaltiesassertion; unresolvedsourcequestionsstayexplicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 968 | 3. Construction subcontracting under CGI art. 283-2 nonies is flagged at Tier 2 only. | ## Sources nativeLF378; ## Who this applies to nativeLF46; ## The taxable base nativeLF200; ## Rates, bands and thresholds nativeLF94; ## Deadlines and filing nativeLF214; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: All nine oldlimits given disposition: patternlibrarynonexhaustive, DOM, constructionreferral, giftamount, qualitativeflags, RSIcountertext, personaliseddate, Corsica, audit/penalties. Actualcurrentpenaltymethod supersedes oldno-penaltiesassertion; unresolvedsourcequestionsstayexplicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 969 | 4. The limit for the very-low-value gift exception is set by article 28-00 A of Annexe IV to the CGI. No allowed official page prints the amount, so this skill states the rule without a figure. | ## Sources nativeLF378; ## Who this applies to nativeLF46; ## The taxable base nativeLF200; ## Rates, bands and thresholds nativeLF94; ## Deadlines and filing nativeLF214; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: All nine oldlimits given disposition: patternlibrarynonexhaustive, DOM, constructionreferral, giftamount, qualitativeflags, RSIcountertext, personaliseddate, Corsica, audit/penalties. Actualcurrentpenaltymethod supersedes oldno-penaltiesassertion; unresolvedsourcequestionsstayexplicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 970 | 5. The red-flag trip points are qualitative. No official page sets money limits for a review, and the previous numeric values had no source. | ## Sources nativeLF378; ## Who this applies to nativeLF46; ## The taxable base nativeLF200; ## Rates, bands and thresholds nativeLF94; ## Deadlines and filing nativeLF214; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: All nine oldlimits given disposition: patternlibrarynonexhaustive, DOM, constructionreferral, giftamount, qualitativeflags, RSIcountertext, personaliseddate, Corsica, audit/penalties. Actualcurrentpenaltymethod supersedes oldno-penaltiesassertion; unresolvedsourcequestionsstayexplicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 971 | 6. Two official pages disagree on the upper ends of the simplified regime turnover band. Both are printed above. | ## Sources nativeLF378; ## Who this applies to nativeLF46; ## The taxable base nativeLF200; ## Rates, bands and thresholds nativeLF94; ## Deadlines and filing nativeLF214; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: All nine oldlimits given disposition: patternlibrarynonexhaustive, DOM, constructionreferral, giftamount, qualitativeflags, RSIcountertext, personaliseddate, Corsica, audit/penalties. Actualcurrentpenaltymethod supersedes oldno-penaltiesassertion; unresolvedsourcequestionsstayexplicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 972 | 7. The exact CA3 filing day cannot be stated here. It depends on the department, the category of business and the SIREN or the operator's name, and is shown in the taxpayer's espace professionnel. | ## Sources nativeLF378; ## Who this applies to nativeLF46; ## The taxable base nativeLF200; ## Rates, bands and thresholds nativeLF94; ## Deadlines and filing nativeLF214; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: All nine oldlimits given disposition: patternlibrarynonexhaustive, DOM, constructionreferral, giftamount, qualitativeflags, RSIcountertext, personaliseddate, Corsica, audit/penalties. Actualcurrentpenaltymethod supersedes oldno-penaltiesassertion; unresolvedsourcequestionsstayexplicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 973 | 8. Corsica has its own rates, shown on the CA3 in their own lines. This skill lists the lines but does not carry the Corsican rate rules. | ## Sources nativeLF378; ## Who this applies to nativeLF46; ## The taxable base nativeLF200; ## Rates, bands and thresholds nativeLF94; ## Deadlines and filing nativeLF214; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: All nine oldlimits given disposition: patternlibrarynonexhaustive, DOM, constructionreferral, giftamount, qualitativeflags, RSIcountertext, personaliseddate, Corsica, audit/penalties. Actualcurrentpenaltymethod supersedes oldno-penaltiesassertion; unresolvedsourcequestionsstayexplicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 974 | 9. Penalties and late interest are not in this skill. Use `fr-tax-audit`. | ## Sources nativeLF378; ## Who this applies to nativeLF46; ## The taxable base nativeLF200; ## Rates, bands and thresholds nativeLF94; ## Deadlines and filing nativeLF214; ## Penalties and interest nativeLF232 | Retained / corrected in current Guide: All nine oldlimits given disposition: patternlibrarynonexhaustive, DOM, constructionreferral, giftamount, qualitativeflags, RSIcountertext, personaliseddate, Corsica, audit/penalties. Actualcurrentpenaltymethod supersedes oldno-penaltiesassertion; unresolvedsourcequestionsstayexplicit. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 976 | ### Change log | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 978 | - **October 2026 refresh.** The CA3 line map was replaced with the 2026 form's own lines: the earlier map used line numbers such as 01, 02, 03, 04, 04B, 05, 06, 06A and 07 that do not exist on the form, described line 10 as the total output VAT when it is the overseas standard-rate line, and described line 18 as EU service self-assessment when it is the Monaco memo line. Franchise thresholds were corrected, the boundary rules were added, and the abandoned single threshold was recorded. The regime band, the current-year ceilings, the VAT-owed limit, the quarterly limit, the two instalment percentages and the instalment exemption were added from the official pages. The filing date was changed from one date to the published schedule. The fuel shares were corrected. The figure for the gift exception was removed as unprovable on an allowed host. The invoice figure was re-described as an exception to one particular. Electronic invoicing was added with its dates. The rate table is now read off the 2026 CA3 form. The intra-EU acquisition lines, the import block and the vehicle exceptions were corrected or restored. The CA12 refund floor was added. | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 979 | - **v2.0 (April 2026):** rewrite to the ten-section structure with the supplier pattern library, six worked examples, Tier 1 and Tier 2 catalogues, the Excel template, the bank statement reading guide and the onboarding fallback. | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 980 | - **v1.0:** initial version, a standalone monolithic document. | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 982 | ### Self-check (v2.0) | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 984 | 1. Quick reference at the top with the line table and the conservative defaults: yes (Section 1). | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 985 | 2. Supplier library as literal lookup tables: yes (Section 3, fifteen sub-tables). | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 986 | 3. Worked examples: yes (Section 4, six examples). | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 987 | 4. Tier 1 rules compressed: yes (Section 5, fifteen rules). | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 988 | 5. Tier 2 catalogue compressed: yes (Section 6, fifteen items). | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 989 | 6. Excel template specification: yes (Section 7). | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 990 | 7. Onboarding as fallback only: yes (Section 9, ten items). | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 991 | 8. All eight France-specific refusals present: yes (Section 2, R-FR-1 through R-FR-8). | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 992 | 9. Reference material at the bottom: yes (Section 10). | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 993 | 10. Restaurant costs treated as not excluded by name but still conditional: yes (Section 5.12 and Example 3). | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 994 | 11. Passenger vehicle exclusion stated on the design test: yes (Section 5.12 and Example 6). | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 995 | 12. Capital goods tolerance sourced: yes (Section 5.11 and Example 4). | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 996 | 13. Intra-EU business-to-business service sale on line E2 with the VIES check: yes (Example 5). | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 997 | 14. Services from a supplier not established in France on line A3: yes (Example 1 and Section 3.9). | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 998 | 15. Construction subcontracting reverse charge flagged: yes (Section 6.14). | ## Sources nativeLF334; ## The taxable base nativeLF98; ## The taxable base nativeLF174; ## Worked examples nativeLF265; ## The taxable base nativeLF208; ## The taxable base nativeLF202; ## Ask the client first nativeLF332 | Retained / corrected in current Guide: Historicalchangelog and all15selfchecksubjects preserved in originalwordinghere and actualcurrentsections. Oldversions/headings/counts are history, not currentlegalrules or unsupported verification claims. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1000 | ## End of France VAT Return Skill v2.0 | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31 | Retained / corrected in current Guide: Endmarker and bothmandatorycompanions retained in currentintro; versionhistory remains in exactoldorigin, not mislabelledcurrent. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1002 | This skill is incomplete without both companion files loaded alongside it: `vat-workflow-base` for the workflow architecture and `eu-vat-directive` for the EU directive content. Do not attempt to produce a CA3 without all three loaded. | # France: VAT and the VAT return (TVA, CA3 and CA12) nativeLF31 | Retained / corrected in current Guide: Endmarker and bothmandatorycompanions retained in currentintro; versionhistory remains in exactoldorigin, not mislabelledcurrent. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1004 | ## Sources | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1006 | - Form 3310-CA3-SD, 2026: https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1007 | - Notice 3310-NOT-CA3-SD, 2026: https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1008 | - Notice 3517-S-NOT-SD, 2026: https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5424.pdf | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1009 | - Form 3517-S-SD, 2026: https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5291.pdf | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1010 | - Formulaire n°3310-CA3-SD landing page: https://www.impots.gouv.fr/formulaire/3310-ca3-sd/tva-et-taxes-assimilees-regime-du-reel-normal-mini-reel | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1011 | - Franchise en base de TVA: https://entreprendre.service-public.gouv.fr/vosdroits/F21746 | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1012 | - Déclarer et payer la TVA: https://entreprendre.service-public.gouv.fr/vosdroits/F23566 | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1013 | - Les régimes d'imposition à la TVA: https://www.impots.gouv.fr/professionnel/les-regimes-dimposition-la-tva | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1014 | - Dates limites de transmission des CA3: https://www.impots.gouv.fr/le-regime-reel-normal-dates-limites-de-transmission-des-ca3 | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1015 | - Mentions obligatoires sur une facture: https://entreprendre.service-public.gouv.fr/vosdroits/F31808 | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1016 | - Facturation électronique, start dates: https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1017 | - VAT rates on services, reduced and intermediate: https://bofip.impots.gouv.fr/bofip/1013-PGP.html | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1018 | - The special rate: https://bofip.impots.gouv.fr/bofip/1449-PGP.html | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1019 | - Rates in the overseas departments: https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1020 | - Exclusion for vehicles designed to carry people: https://bofip.impots.gouv.fr/bofip/1192-PGP.html | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1021 | - Petroleum products and the deductible share: https://bofip.impots.gouv.fr/bofip/1194-PGP.html | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1022 | - Accommodation for directors and staff: https://bofip.impots.gouv.fr/bofip/1190-PGP.html | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1023 | - Goods given away: https://bofip.impots.gouv.fr/bofip/1196-PGP.html | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1024 | - Small-value equipment taken to expense: https://bofip.impots.gouv.fr/bofip/2109-PGP.html | ## Sources nativeLF334; ## Sources nativeLF378 | Retained / corrected in current Guide: Duplicate oldsourcecatalogue retained as exactorigin record, mapped to current source table/explicitlimits; sourceURLs and historicalreadmetadata not invented afresh. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1026 | ## Disclaimer | ## Talk to a verified accountant nativeLF394; ## Talk to a verified accountant nativeLF384 | Retained / corrected in current Guide: Professional-review/disclaimer and canonicalcurrentserviceCTA retained. Oldmarketingclaims aboutlogin/latestversion are historicalcopy, not newly verifiedproductfeatures. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1028 | This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional, such as an expert-comptable, a commissaire aux comptes, or an equivalent licensed practitioner in your jurisdiction, before filing or acting upon. | ## Talk to a verified accountant nativeLF394; ## Talk to a verified accountant nativeLF384 | Retained / corrected in current Guide: Professional-review/disclaimer and canonicalcurrentserviceCTA retained. Oldmarketingclaims aboutlogin/latestversion are historicalcopy, not newly verifiedproductfeatures. |
| b001836ffe270b1cde8ff908a3d7fac2d436bc8a^ / 1030 | The most up-to-date version of this skill is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes. | ## Talk to a verified accountant nativeLF394; ## Talk to a verified accountant nativeLF384 | Retained / corrected in current Guide: Professional-review/disclaimer and canonicalcurrentserviceCTA retained. Oldmarketingclaims aboutlogin/latestversion are historicalcopy, not newly verifiedproductfeatures. |

## Explicit non-rule units

| Unit / native LF | Wording | Classification |
|---|---|---|
| france-vat-return-0001 / 31 | This skill covers French VAT for 2026: who is in and who is out, the rates, the two filing regimes and their limits, how to fill the CA3 and the CA12, self-assessment on cross-border purchases, the EU statements, the e-invoicing timetable, the deduction restrictions, and penalties and interest. Every figure was read on an official French page on 24 October 2026, unless the Sources table says otherwise. Load `vat-workflow-base` for the workflow architecture and `eu-vat-directive` for the EU directive content alongside it. | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0002 / 33 | Two facts about the law itself in 2026: | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0012 / 50 | &#124; Item &#124; Rate or amount &#124; Year &#124; Source &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0049 / 98 | **What goes on the CA3 (form 3310-CA3-SD, 2026).** Read the line codes off the 2026 form only. | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0050 / 100 | &#124; CA3 line &#124; What goes on it &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0091 / 147 | **Self-assessment (autoliquidation).** | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0097 / 156 | **Deduction restrictions.** | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0098 / 158 | &#124; Cost &#124; Treatment &#124; Source &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0112 / 176 | &#124; Pattern &#124; Treatment &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0136 / 212 | &#124; What &#124; When &#124; Source &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0148 / 226 | Formats, platforms, e-reporting frequencies and the payment-data rules are in `france-einvoice`. | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0151 / 234 | &#124; Failure &#124; Charge &#124; Source &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0173 / 261 | - Income tax on cross-border activity is in `fr-cross-border` and `fr-corporate-tax`. | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0174 / 265 | **Earlier transaction illustrations, with their actual eligibility gates.** These retain the six hypothetical classification cases from the pre-refresh Guide. Counterparty labels and bank descriptions are fixture facts, not proof of the supplier, rate, place or deduction. The decimal amounts below are working-paper illustrations; apply the CA3 rounding rule to the supported period totals, not independently to each line. | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0192 / 336 | &#124; Source &#124; URL &#124; Read on &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0193 / 338 | &#124; CGI art. 293 B, 293 B bis, 293 B ter (franchise; LF 2025 art. 32 and loi n° 2025-1044 art. 1) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-24 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0194 / 339 | &#124; CGI art. 287 (returns, instalments, monthly triggers) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191928/2026-10-24 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0195 / 340 | &#124; CIBS art. L. 162-4 to L. 162-8 (régime simplifié conditions; L. 162-4 indexation rule) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000044598127/2026-10-24 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0196 / 341 | &#124; CIBS art. A. 162-7 (régime simplifié amounts for 2026, arrêté of 27 January 2026) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000049803748/2026-10-24 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0197 / 342 | &#124; BOFiP BOI-BAREME-000036-20260701 (régime simplifié limits for 2026) &#124; https://bofip.impots.gouv.fr/bofip/9368-PGP.html/identifiant=BOI-BAREME-000036-20260701 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0198 / 343 | &#124; CGI art. 278 (20%) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191854/2026-10-24 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0199 / 344 | &#124; CGI art. 278-0 bis (5.5%) and 279 (10%) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191654/2026-10-24 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0200 / 345 | &#124; CGI art. 281 quater and 281 octies (2.1%) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191656/2026-10-24 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0201 / 346 | &#124; CGI art. 298 septies (press, 2.1% and 1.05%) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179663/2026-10-24 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0202 / 347 | &#124; CGI art. 289 B (état récapitulatif) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191662/2026-10-24 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0203 / 348 | &#124; CGI art. 289 bis (e-invoicing, amended by LF 2026 art. 123) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191855/2026-10-24 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0204 / 349 | &#124; Loi n° 2023-1322 (LF 2024), art. 91, rewriting LFR 2022 art. 26, III (e-invoicing dates) &#124; https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048727345 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0205 / 350 | &#124; CGI art. 1727 (late interest) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006147309/2026-10-24 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0206 / 351 | &#124; CGI art. 1728 (late filing, amended by LF 2026 art. 126) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179995/2026-10-24 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0207 / 352 | &#124; CGI art. 1729 (inaccuracies) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179987/2026-10-24 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0208 / 353 | &#124; CGI art. 1731 (5% late payment) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006163002/2026-10-24 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0209 / 354 | &#124; CGI art. 1737 (invoice fines) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006163056/2026-10-24 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0210 / 355 | &#124; CGI art. 1788 A and 1788 D (statements, self-assessment, e-reporting fines) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162921/2026-10-24 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0211 / 356 | &#124; BOFiP actualité 7 October 2026: CIBS recodification moved to 1 January 2027; LF 2026 VAT measures &#124; https://bofip.impots.gouv.fr/bofip/15140-PGP.html &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0212 / 357 | &#124; BOFiP actualité 17 June 2026: alcohol advertising deduction (LF 2026 art. 91) &#124; https://bofip.impots.gouv.fr/bofip/15011-PGP.html &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0213 / 358 | &#124; BOFiP BOI-TVA-DECLA-20-30-50 (e-reporting dates) &#124; https://bofip.impots.gouv.fr/bofip/13897-PGP.html &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0214 / 359 | &#124; BOFiP: vehicles; fuel; accommodation; gifts; small equipment &#124; https://bofip.impots.gouv.fr/bofip/1192-PGP.html ; https://bofip.impots.gouv.fr/bofip/1194-PGP.html ; https://bofip.impots.gouv.fr/bofip/1190-PGP.html ; https://bofip.impots.gouv.fr/bofip/1196-PGP.html ; https://bofip.impots.gouv.fr/bofip/2109-PGP.html &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0215 / 360 | &#124; Service-public: franchise en base (checked 1 January 2026) &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F21746 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0216 / 361 | &#124; Scoped writer reread: CGI art. 293 D, III startup proration/countertext; annexe II art. 205–207 own deduction/adjustment conditions; BOFiP current invoice legal-chargeability, FX tax point and qualified EUR 10,000 selector; art. 206 IV-2-1° admission gate checked in the retained literal source on 31 October (fresh direct statute retrieval failed) &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-29 ; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069569/LEGISCTA000006179225/2026-10-29 ; https://bofip.impots.gouv.fr/bofip/1111-PGP.html ; https://bofip.impots.gouv.fr/bofip/1531-PGP.html ; https://bofip.impots.gouv.fr/bofip/140-PGP.html ; https://bofip.impots.gouv.fr/bofip/11964-PGP.html &#124; 2026-10-29; retained art. 206 gate 2026-10-31 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0217 / 362 | &#124; Service-public: déclarer et payer la TVA (checked 21 February 2026) &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F23566 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0218 / 363 | &#124; Service-public: invoice particulars (checked 11 August 2026) &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F31808 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0219 / 364 | &#124; CA3 form 3310-CA3-SD 2026 (impots.gouv.fr in maintenance; Internet Archive copy of 10 May 2026); historical acquisition retained, TC code checked in the retained literal form and fresh official PDF on 31 October &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf &#124; 2026-10-24; TC 2026-10-31 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0220 / 365 | &#124; CA3 notice 3310-NOT-CA3-SD 2026 (Internet Archive copy of 16 October 2026) &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0221 / 366 | &#124; Actual selected 2026 CA3 notice reread: period/Néant and rounding instructions, B5/F8 positive corrections and lines 15/21, line-26 refund amount/period tests and DES recipient-liability/non-exemption conditions; E2 destination-taxable TBE services versus E3 distance goods checked again on 31 October &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf &#124; 2026-10-29; E2/E3 2026-10-31 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0222 / 367 | &#124; Actual indexed sanction clauses: CGI 1737, II/III/IV bis/V and 1788 D, I/II/V (returned operative 21 February 2026–1 January 2027); CGI 1788 A, 1/2/4 (returned 1 January 2026 text; direct current fetch failures retained) &#124; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053293950/2999-01-01 ; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044045593/2026-09-25 ; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983701/2026-01-01 &#124; 2026-10-29 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0223 / 368 | &#124; Supplier classifier: actual financial/insurance exemption and option scope, disallowed option categories and universal-postal conditions; retained current-version observations and actual recodification-date countertext are separate &#124; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041467574/2026-06-18 ; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983610/2026-03-21 ; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020763620/2026-07-23 ; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054374042/2026-07-01 &#124; 2026-10-29 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0224 / 369 | &#124; Selected rates and eligibility: CGI 278-0 bis, 278-0 bis A, 279, 279-0 bis; BOFiP potable-water §100, medicines/blood §350 and qualifying first performances; current press and DOM observations. Selected clauses only, not the complete rate catalogue &#124; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191654/ ; https://bofip.impots.gouv.fr/bofip/2033-PGP.html/identifiant=BOI-TVA-LIQ-30-10-10-20251119 ; https://bofip.impots.gouv.fr/bofip/1449-PGP.html ; https://bofip.impots.gouv.fr/export/pdf/1963 ; https://www.legifrance.gouv.fr/affichCode.do?cidTexte=LEGITEXT000006069577&idSectionTA=LEGISCTA000006179663 &#124; 2026-10-29 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0225 / 370 | &#124; Finite source closures: actual published gift limit; consolidated21February2026 LFR2022article26III and current289bis; DGFiP September2026 scope/receiving/size-reference FAQs; selected actual2026CA12notice. Direct gift/currentLFR fetch failures retained separately from official indexed observations &#124; https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006179484/ ; https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000053546715 ; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053576899 ; https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq---fe_je-decouvre-la-facturation-electronique.pdf ; https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq---fe_japprofondis-la-facturation-electronique.pdf ; https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5424.pdf &#124; 2026-10-29 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0226 / 371 | &#124; Writer reread: actual article 242 nonies A, II and commencement notes; invoice simplifications and exclusions; official indexed CIBS D. 162-8 date rule and BOFiP calendar-year crossing procedure (direct decree fetch failures retained) &#124; https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006162005 ; https://bofip.impots.gouv.fr/bofip/142-PGP.html/identifiant=BOI-TVA-DECLA-30-20-20-20-20220119 ; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049803758 ; https://bofip.impots.gouv.fr/bofip/2418-PGP.html/identifiant=BOI-TVA-DECLA-20-20-30-10-20230118 &#124; 2026-10-29 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0227 / 372 | &#124; CA12 form 3517-S-SD 2026 (Internet Archive copy of 12 January 2026) &#124; https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5291.pdf &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0228 / 373 | &#124; impots.gouv.fr: CA3 filing dates (Internet Archive copy of 29 September 2026) &#124; https://www.impots.gouv.fr/le-regime-reel-normal-dates-limites-de-transmission-des-ca3 &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0229 / 374 | &#124; impots.gouv.fr: e-invoicing start dates, modified 16 January 2026 (Internet Archive copy of 25 June 2026) &#124; https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0230 / 375 | &#124; impots.gouv.fr: overseas department rates (Internet Archive copy of 18 May 2026) &#124; https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0231 / 376 | &#124; impots.gouv.fr: VAT regimes, modified 21 May 2026, still showing 2023-2025 limits (Internet Archive copy of 29 September 2026) &#124; https://www.impots.gouv.fr/professionnel/les-regimes-dimposition-la-tva &#124; 2026-10-24 &#124; | non-rule heading/sourcecatalogue/context/sibling |
| france-vat-return-0232 / 378 | Not yet confirmed: the non-calendar-year transition-period/form reconciliation where the 2023 BOFiP first-day-of-exercise examples differ from the 2025 CIBS D. 162-8, 2° wording (the ordinary calendar-year crossing date and CA3 sequence are now supplied); the unexamined remainder of the 10% and 5.5% rate catalogue after LF 2026, including the delegated technical/performance list for a particular energy-renovation project (the selected food/books/water/municipal-waste, hotel/meal/passenger/TV and dwelling-work statutory conditions above were actually read on 29 October); Corsican rate rules beyond the CA3 lines; the first-year franchise and next-year basic-versus-higher test where the literal CGI art. 293 D, III proration and the retained DGFiP first-year/no-proration guidance diverge: the actual own statute and F21746 following-year text have now been read, but no authoritative reconciliation is supplied. Ordinary restaurant-meal treatment rests on the actually read CGI annexe II art. 205–206 and documented business/invoice facts; specialist meal arrangements are not a blanket entitlement. | non-rule heading/sourcecatalogue/context/sibling |
