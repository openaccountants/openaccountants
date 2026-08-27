---
name: us-state-payroll-matrix
description: Tier 2 US federal-level reference skill providing the 50-state at-a-glance payroll matrix covering income-tax withholding registration, quarterly return forms and due dates, SUTA wage base and rate ranges, new-hire reporting agencies and 20-day deadlines under §453A, state disability and paid family/medical leave mandates (CA SDI, NY/NJ DBL, CO FAMLI, MA PFML, WA PFML, OR Paid Leave, CT PFML, DC PFL), local payroll taxes (PA Act 32 EIT, OH RITA/CCA, NYC, CA SDI), and state-specific quirks (CalSavers mandate, OR TriMet transit tax, WA Cares Fund). Tax year 2025.
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US State Payroll Matrix

## US 50-State Payroll Reference Matrix (Tax Year 2025)

## 1. Scope

This reference covers payroll obligations for employers with W-2 employees in any combination of the 50 US states plus the District of Columbia. Coverage areas:

- State income tax (PIT) withholding: registration forms, employee certificates, quarterly returns, due dates
- State Unemployment Tax Act (SUTA) contributions: 2025 taxable wage base, new-employer rate, experience-rated range
- State new-hire reporting under 42 U.S.C. §653a (federal 20-day deadline; state-specific portals)
- State disability insurance (SDI) and short-term disability mandates (CA, NY, NJ, RI, HI, PR — not all flagged here)
- State paid family and medical leave (PFML) mandates: CA, NY, NJ, RI, MA, WA, OR, CT, CO, DC, MN (effective 2026), DE (effective 2026), MD (effective 2026)
- Local income / occupation / privilege taxes: PA Act 32 EIT, OH RITA/CCA, KY occupational license fees, NYC resident tax, AL/MO/MI/MD/IN/DE municipal income taxes
- State-specific retirement mandates: CalSavers, IL Secure Choice, OR OregonSaves, CT MyCTSavings, MD Saves, VA RetirePath, CO SecureSavings, NJ Secure Choice, NY Secure Choice
- Transit / special district payroll taxes: OR TriMet & Lane Transit, NY MCTMT, WA Cares Fund

**Out of scope:** federal Forms 941/940/W-2/W-3 (covered in `us-form-941-940-payroll.md`), federal §3401(c) statutory-employee classification, multi-state allocation methods (covered in `us-multi-state-allocation.md`), employer-sponsored retirement plans (covered in `us-self-employed-retirement.md`), workers' compensation insurance rates (a state-specific commercial-insurance matter, not a tax skill).

**Audience:** US CPAs, EAs, and payroll providers servicing multi-state employers. This skill is a quick-reference table; it is not a substitute for the state agency website on any given filing date.

## 2. How to use this matrix

- **Identify each state of employment** — Based on where the employee physically performs services, not where the employer is domiciled. The seven convenience-of-employer states (NY, NJ — limited, CT, PA, NE, AR, DE) may reach remote workers even outside the state.  _(unsure)_
- **For every employment state, check three things** — Income tax withholding registration (Column 3); SUTA registration in the state where wages are localized under the four-part FUTA test (26 USC §3306(j)); New-hire reporting within 20 days of hire (Column 6)  _(26 USC §3306(j))_
- **For PFML / SDI mandates** — If the state is in Column 7 or 8 as "Y," the employer must register with the state insurance agency and remit contributions (employer share, employee share, or both).  _(unsure)_
- **For local taxes** — If Column 9 flags "Y," consult the city/municipality directly. PA Act 32 employers must capture the employee's PSD code (political subdivision code) at hire.  _(unsure)_
- **Cross-reference Section 5** — Cross-reference Section 5 for the state-by-state quirks before finalizing the payroll setup.  _(unsure)_

## 3. Quick-reference tables

### 3.1 Multi-state employer essentials

- **Multi-state employer** — A "multi-state employer" for new-hire reporting purposes is one with employees in two or more states who elects to report all new hires to a single state. The election is filed with HHS Office of Child Support Services. All other employers must report to each state where the employee works.  _(42 U.S.C. §653a(b)(1)(B))_

### 3.2 No-PIT states (9)

**No-PIT states (9)**  _(3.2 No-PIT states (9))_

| State | SUTA Agency | Special Notes |
| --- | --- | --- |
| Alaska (AK) | AK DOL Employment Security | Employee SUI contribution 0.50% of wages (one of two states; NJ and PA are the others) |
| Florida (FL) | FL DOR — "Reemployment Tax" not "SUTA" | First $7,000 of wages |
| Nevada (NV) | NV DETR | Modified Business Tax (MBT) on payroll over $50K/quarter |
| New Hampshire (NH) | NH Employment Security | No PIT on wages; 4% tax on interest/dividends repealed for 2025 |
| South Dakota (SD) | SD DOL Reemployment Assistance | — |
| Tennessee (TN) | TN DOL Workforce Development | Hall Income Tax repealed 2021; unemployment-only |
| Texas (TX) | TX Workforce Commission (TWC) | Form C-3 quarterly |
| Washington (WA) | WA ESD | PFML + Cares Fund LTC mandate — see Section 5 |
| Wyoming (WY) | WY DWS | — |

These states have no personal income tax. Employers still owe SUTA, new-hire reporting, federal withholding, and (where applicable) workers' compensation and state-specific levies.

### 3.3 Paid-leave / SDI states (12 in 2025, expanding through 2026)

**Paid-leave / SDI states (12 in 2025, expanding through 2026)**  _(3.3 Paid-leave / SDI states (12 in 2025, expanding through 2026))_

| State | Program | 2025 Combined Rate | Funding Split |
| --- | --- | --- | --- |
| California | SDI + PFL | 1.20% (employee only) | Employee 100%; no wage cap (SB 951) |
| New York | DBL + PFL | DBL: employer-funded private carrier; PFL: 0.388% | DBL employer; PFL employee |
| New Jersey | TDI + FLI | TDI: 0.23% EE + employer-rated; FLI: 0.33% EE | EE-heavy; TDI taxable wage base $165,400 |
| Rhode Island | TDI + TCI | 1.30% (employee only) | Employee 100%; wage base $89,200 |
| Hawaii | TDI | 0.50% (employee max) | Employee up to 50%, employer balance |
| Massachusetts | PFML | 0.88% | Split employer/employee per MA DFML schedule |
| Washington | PFML + Cares Fund | PFML 0.92%; LTC 0.58% | PFML split; LTC employee-only |
| Oregon | Paid Leave Oregon | 1.00% | Employee 60% / Employer 40% (employers ≥25) |
| Connecticut | CT Paid Leave | 0.50% (employee only) | Employee 100%; wage base = SS base |
| Colorado | FAMLI | 0.90% | 50/50 employer/employee (employers ≥10) |
| District of Columbia | DC PFL | 0.75% | Employer-only |
| Minnesota | MN Paid Leave (eff. 1/1/2026) | 0.88% projected | Split per MN DEED |

### 3.4 Local income tax states (8)

**Local income tax states (8)**  _(3.4 Local income tax states (8))_

| State | Localities | Mechanism |
| --- | --- | --- |
| Pennsylvania | ~2,500 municipalities & school districts | Act 32 EIT — employee residence PSD code controls |
| Ohio | ~600 municipalities | RITA, CCA, or city-administered |
| Kentucky | ~210 counties/cities | Occupational license fees |
| Indiana | All 92 counties | County tax based on residence as of 1/1 |
| Michigan | 24 cities | Detroit, Grand Rapids, etc. |
| Maryland | 23 counties + Baltimore City | Piggybacked on state withholding |
| Missouri | Kansas City, St. Louis | 1% earnings tax |
| New York | NYC + Yonkers | NYC resident tax; Yonkers resident & non-resident |
| Alabama | Several municipalities | Birmingham, Bessemer, Gadsden, Macon County, etc. |
| Delaware | Wilmington | 1.25% city wage tax |
| West Virginia | 4 cities | "City service fee" — flat dollar |

## 4. THE BIG 50-STATE + DC TABLE

Column key:
1. State
2. PIT type: NoPIT / Flat / Graduated
3. Withholding registration form
4. Quarterly withholding return + due date
5. SUTA wage base 2025 + (new-employer rate / experience range)
6. New-hire reporting agency + portal
7. SDI? (rate)
8. PFML? (rate)
9. Local income tax?
10. Notable quirks

**THE BIG 50-STATE + DC TABLE**  _(4. THE BIG 50-STATE + DC TABLE)_

| # | State | PIT | WH Registration | Quarterly Return + Due | SUTA Base / Rates 2025 | New-Hire Agency | SDI | PFML | Local | Quirks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AL | Graduated 2-5% | Form COM:101 (My Alabama Taxes) | A-1 / A-6 monthly; A-3 annual recon. Quarterly liab <$1K | $8,000 / 2.7% new / 0.20-6.80% | AL DOL New Hire Unit | N | N | Y (municipal) | Birmingham 1% occupational; auto-renewal of WH ID annually |
| 2 | AK | NoPIT | N/A | N/A | $51,700 / 2.37% new / 1.00-5.40% (+ 0.50% employee SUI) | AK Child Support Services | N | N | N | Employee SUI contribution rare nationally; high SUTA base |
| 3 | AZ | Flat 2.5% | Form JT-1 (joint w/ SUTA) | A1-QRT quarterly, due last day of month after Q | $8,000 / 2.0% new / 0.04-9.72% | AZ New Hire Reporting Center | N | N | N | Employee chooses WH % on A-4 (0.5%-3.5%); flat tax effective 2023 |
| 4 | AR | Graduated up to 3.9% | AR-1R | AR941M monthly + AR941A annual recon; quarterly if <$1K | $7,000 / 1.9% new / 0.1-14.0% | AR New Hire Reporting Center | N | N | N | Convenience-of-employer state for remote workers post-2021 |
| 5 | CA | Graduated 1-13.3% (+1% MHST >$1M) | DE 1 (EDD registration) | DE 9 + DE 9C quarterly, due last day of month after Q-end | $7,000 (lowest in US) / 3.4% new / 1.5-6.2% | CA EDD New Employee Registry | **Y 1.20%** EE; no wage cap | Bundled w/ SDI (PFL) | N (except SF GRT) | **AUDIT FLASH POINT: SDI no-cap since 2024 (SB 951); CalSavers mandate for 1+ EE since 12/31/2023** |
| 6 | CO | Flat 4.40% | CR 0100 (MyBizColorado) | DR 1094 monthly/quarterly per filing tier | $27,200 / 3.05% new / 0.81-12.34% | CO Family Support Registry (CSE) | N | **Y FAMLI 0.90%** | N | FAMLI 50/50 split; SecureSavings retirement mandate (5+ EE) |
| 7 | CT | Graduated 2-6.99% | REG-1 | CT-941 quarterly, due last day of month after Q | $26,100 / 2.5% new / 1.1-7.8% | CT DOL New Hire Reporting | N | **Y CTPL 0.50%** EE | N | Convenience-of-employer state; CT MyCTSavings mandate (5+ EE) |
| 8 | DE | Graduated 2.2-6.6% | CRA (Combined Registration) | W1-Q quarterly or W1 monthly per liability | $12,500 / 1.2-1.8% new / 0.3-6.5% | DE DHSS Division of Child Support | N | Y (eff. 1/1/2026) DE Paid Leave | Y (Wilmington 1.25%) | Convenience-of-employer for remote workers; DE Paid Leave contributions begin 1/1/2025 with benefits 1/1/2026 |
| 9 | DC | Graduated 4-10.75% | FR-500 (MyTax.DC.gov) | FR-900Q quarterly, due last day of month after Q | $9,000 / 2.7% new / 1.9-7.4% | DC Directory of New Hires | N | **Y DC PFL 0.75%** ER-only | Y (residents only) | DC PFL is employer-funded entirely; residents working elsewhere taxed by DC |
| 10 | FL | NoPIT | N/A | N/A | $7,000 / 2.7% new / 0.1-5.4% (called "Reemployment Tax") | FL Dept Revenue Child Support | N | N | N | RT-6 quarterly reemployment return; no SUTA on first-year exempt orgs |
| 11 | GA | Graduated 1-5.39% (flattening to 5.19% in 2025) | Form CRF-002 | G-7 monthly or G-7Q quarterly | $9,500 / 2.7% new / 0.04-7.56% | GA New Hire Reporting Center | N | N | N | Atlanta city government has separate occupational tax but no local PIT |
| 12 | HI | Graduated 1.4-11% | BB-1 | HW-14 quarterly (now monthly for most >$5K/yr) | $62,000 (very high) / 4.0% new / 0.2-5.8% | HI Child Support Enforcement Agency | **Y HI TDI 0.50%** EE max | N (TDI only) | N | TDI premium split: EE up to 0.50%, ER balance; high SUTA base |
| 13 | ID | Graduated 1-5.695% (now flat 5.8% per HB 521) | Form IBR-1 | Form 910 monthly/quarterly per tier | $55,300 / 1.0% new / 0.207-5.4% | ID DOL Child Support | N | N | N | Flat 5.8% effective 2025; semi-monthly deposits over $300K/yr |
| 14 | IL | Flat 4.95% | REG-1 (MyTax Illinois) | IL-941 quarterly, due last day of month after Q | $13,916 / 3.95% new / 0.85-8.65% | IL Dept Employment Security | N | N (Chicago Paid Leave ordinance only) | N | **Secure Choice retirement mandate (5+ EE)**; Chicago Paid Leave & Paid Sick Leave 2024 |
| 15 | IN | Flat 3.0% (county +) | BT-1 (INBiz) | WH-1 monthly + WH-3 annual recon | $9,500 / 2.5% new / 0.50-7.4% | IN DOL New Hire | N | N | **Y (all 92 counties)** | County tax determined by residence 1/1; Form WH-4 lists county code |
| 16 | IA | Graduated 4.4-5.7% (flat 3.8% from 2025 per HF 2317) | Form 78-005 | IA W-1 quarterly | $39,500 / 1.0% new / 0.0-7.0% | IA DHHS Centralized Employee Registry | N | N | N | Flat 3.8% effective 2025; biweekly deposit tier >$120K/yr |
| 17 | KS | Graduated 3.1-5.7% | CR-16 | KW-5 monthly/quarterly per tier | $14,000 / 2.7% new / 0.17-6.40% | KS New Hire Directory | N | N | N | KS DOL UI portal separate from Dept Revenue; tiered deposit |
| 18 | KY | Flat 4.0% (down from 4.5%) | 10A100 | K-1 quarterly + K-3 annual recon | $11,700 / 2.7% new / 0.30-9.0% | KY New Hire Reporting Center | N | N | **Y (county occupational license)** | Louisville Metro 2.2%; Lexington-Fayette 2.25%; collected via Form OL-S |
| 19 | LA | Graduated 1.85-4.25% (flat 3% per HB 10 from 2025) | R-16019 | L-1 quarterly | $7,700 / 1.16% new / 0.09-6.20% | LA New Hires Directory | N | N | N | Flat 3% effective 2025 per Special Session bill |
| 20 | ME | Graduated 5.8-7.15% | Form 941ME | 941ME quarterly + W-3ME annual | $12,000 / 2.32% new / 0.28-6.03% | ME DHHS Division of Support Enforcement | N | **Y ME PFML 1.0% (eff. 1/1/2025)** | N | ME PFML contributions began 1/1/2025; benefits 5/1/2026; split 60 EE / 40 ER (15+ EE) |
| 21 | MD | Graduated 2-5.75% + county | Combined Registration App | MW506 monthly/quarterly per tier | $8,500 / 2.6% new / 0.3-7.5% | MD New Hire Registry | N | **Y MD FAMLI 0.90% (eff. 7/1/2025 contributions, 7/1/2026 benefits)** | **Y (all counties)** | County tax piggybacks on MW507; MD Saves retirement mandate (W-2 employer 2+ yr) |
| 22 | MA | Flat 5% (+ 4% surtax >$1M) | Form TA-1 | M-941 quarterly + monthly per tier | $15,000 / 2.42% new / 0.94-14.37% | MA Child Support Enforcement | N | **Y MA PFML 0.88%** | N | PFML split: ~60/40 EE/ER (medical); 100% EE (family) for ≥25 EE employers |
| 23 | MI | Flat 4.25% | Form 518 | Form 5080 monthly/quarterly | $9,500 / 2.7% new / 0.06-10.3% | MI New Hires Operations Center | N | N | **Y (24 cities)** | Detroit 2.4% resident/1.2% non; collected via Form CITY-W-4; rate dropped to 4.05% per Earned Income Tax Trigger but court reverted |
| 24 | MN | Graduated 5.35-9.85% | Business Tax Reg | MN Form W-3 quarterly | $43,000 / standard 1.6% new / 0.10-9.10% | MN DHS Office of Child Support | N | **Y MN Paid Leave (contributions begin 1/1/2026)** | N | Contribution rate 0.88% projected; ESST sick leave statewide since 2024 |
| 25 | MS | Graduated 0-5% (flat 4% 2025; 3% 2030) | Form 89-350 | 89-105 quarterly | $14,000 / 1.2% new / 0.20-5.40% | MS Dept Human Services Case Registry | N | N | N | Flat 4% effective 2025; full repeal trigger by 2040 per HB 1733 |
| 26 | MO | Graduated 2-4.7% | Form 2643 | MO-941 monthly/quarterly per tier | $9,500 / 2.376% new / 0.0-9.0% | MO Family Support Division | N | N | **Y (KC + St. Louis 1%)** | Kansas City/St. Louis 1% Earnings Tax (Form RD-110/E-234) |
| 27 | MT | Graduated 4.7-5.9% (flat 5.9% top from 2024) | Form GenReg | MW-1 monthly/quarterly per tier | $45,100 / 1.0-2.3% new (industry-based) / 0.0-6.12% | MT DPHHS Child Support Enforcement | N | N | N | MT new-employer rate varies by NAICS industry (only state with this) |
| 28 | NE | Graduated 2.46-5.84% (5.20% top from 2025) | Form 20 | Form 941N quarterly | $9,000 (cat 1) / $24,000 (cat 20) / 1.25% new / 0.0-5.4% | NE Workforce Development | N | N | N | Convenience-of-employer state; SUTA wage base varies by category |
| 29 | NV | NoPIT | N/A | N/A | $41,800 / 2.95% new / 0.25-5.4% | NV New Hire Reporting | N | N | N | Modified Business Tax 1.378% on wages >$50K/quarter (excise on payroll) |
| 30 | NH | NoPIT (I&D tax repealed 2025) | N/A (I&D 1040 individual only) | N/A | $14,000 / 1.7% new / 0.1-7.0% | NH DHHS Division of Child Support | N | N (Granite State Paid Family Leave Plan voluntary) | N | Voluntary state-administered PFL through MetLife; tax credit available |
| 31 | NJ | Graduated 1.4-10.75% | NJ-REG | NJ-927 quarterly | $43,300 / 2.8% new / 0.4-5.4% | NJ Child Support New Hire Reporting | **Y TDI EE 0.23% + ER rated** | **Y FLI EE 0.33%** | N | **AUDIT FLASH POINT: SDI + FLI separate line-item deductions on paycheck stub**; FLI base $165,400 (capped) |
| 32 | NM | Graduated 1.7-5.9% | ACD-31015 | TRD-41414 monthly + CRS-1 quarterly | $33,200 / 1.0% new / 0.33-6.4% | NM Children Youth & Families Dept | N | N | N | Workers' Compensation Fee $4.30/qtr; gross receipts overlay |
| 33 | NY | Graduated 4-10.9% (+ NYC) | NYS-100 | NYS-45 quarterly (combined WH + SUTA) | $12,800 / 4.025% new / 2.025-9.825% | NY New Hire Online | **Y DBL (private carrier)** | **Y NY PFL 0.388%** EE | **Y (NYC, Yonkers)** | **AUDIT FLASH POINT: Convenience-of-employer state**; MCTMT 0.34-0.60% for MCTD employers >$312,500/qtr; NYS-45 is the ONE quarterly form |
| 34 | NC | Flat 4.5% (4.25% from 2025; 3.99% 2026) | NC-BR | NC-5 monthly/quarterly per tier | $32,600 / 1.0% new / 0.06-5.76% | NC New Hire Directory | N | N | N | Semi-weekly deposit threshold $2K/month |
| 35 | ND | Graduated 1.95-2.5% | Form 301 | F-941 quarterly | $43,800 / new construction 9.83% / new non-const 1.05% / 0.08-9.97% | ND Dept Human Services | N | N | N | Two new-employer rates split by construction vs. non-construction NAICS |
| 36 | OH | Graduated 2.75-3.5% (flat 2.75% from 2026) | IT 1 (Ohio Business Gateway) | IT 941 / IT 942 per tier | $9,000 / 2.7% new (5.5% construction) / 0.4-10.1% | OH Centralized Employee Registry | N | N | **Y (~600 municipalities, RITA/CCA)** | **AUDIT FLASH POINT: RITA/CCA municipal withholding by work-location for ≤20 days, then resident**; school-district WH (SD-101) separate from city |
| 37 | OK | Graduated 0.25-4.75% | OW-11 (OkTAP) | WTH 10001 quarterly | $27,200 / 1.5% new / 0.3-9.2% | OK New Hire Reporting Center | N | N | N | New-employer rate higher than many states |
| 38 | OR | Graduated 4.75-9.9% | Form OR-WR-1 (Combined Payroll) | OR-OQ quarterly | $54,300 / 2.4% new / 0.9-5.4% | OR DOJ Division of Child Support | N | **Y Paid Leave Oregon 1.00%** | **Y TriMet 0.8237% / Lane Transit 0.79%** | **AUDIT FLASH POINT: TriMet/Lane Transit payroll tax; statewide transit tax 0.10% EE; OR Paid Leave employers ≥25 split 40 ER / 60 EE; OregonSaves mandate** |
| 39 | PA | Flat 3.07% | PA-100 | PA-W3 quarterly | $10,000 / 3.822% new (10.5924% construction) / 1.419-10.3734% | PA CareerLink | N | N | **Y (Act 32 EIT + LST $52/yr)** | **AUDIT FLASH POINT: Act 32 EIT — capture PSD code on Form Residency Certification at hire; LST $52 max (split if multiple jurisdictions)**; PA also has 0.07% EE UC contribution |
| 40 | RI | Graduated 3.75-5.99% | BAR (Business Application) | 941-Q quarterly | $29,200 (regular) / $30,700 (high-rate employers) / 0.98% new / 0.95-9.4% | RI DLT | **Y RI TDI 1.30%** EE | **Y RI TCI bundled w/ TDI** | N | TDI / TCI taxable wage base $89,200; second wage base for SUTA |
| 41 | SC | Graduated 3-6.4% (6.2% from 2025) | SCDOR-111 | WH-1605 quarterly | $14,000 / 0.41-5.4% (no fixed new-emp rate, year-1 = avg) | SC New Hire Reporting Program | N | N | N | New-employer rate set as the average rate of contributing employers |
| 42 | SD | NoPIT | N/A | N/A | $15,000 / 1.0% new (6% construction) / 0.0-9.5% | SD DOL Reemployment Assistance | N | N | N | Investment fee 0.02-0.55% on top of SUTA; no separate WH portal |
| 43 | TN | NoPIT | N/A | N/A | $7,000 / 2.7% new / 0.01-10.0% | TN Dept Human Services New Hire | N | N | N | Hall Income Tax repealed 2021; LLC/franchise tax obligations remain |
| 44 | TX | NoPIT | N/A | N/A | $9,000 / 2.7% new / 0.25-6.25% | TX Office of Attorney General Child Support | N | N | N | Form C-3 quarterly to TWC; no city-level PIT but franchise/sales overlay |
| 45 | UT | Flat 4.55% | TC-69 | TC-941E quarterly | $48,900 (high) / 1.4% new / 0.3-7.3% | UT Dept Workforce Services | N | N | N | One of highest SUTA bases nationally |
| 46 | VT | Graduated 3.35-8.75% | Form BR-400 | WHT-436 quarterly + WHT-434 annual | $14,800 / 1.0% new / 0.4-5.4% | VT DCF Office of Child Support | N | N (voluntary PFML through The Hartford) | N | VT Child Care Contribution 0.44% payroll tax (employer 0.33% / employee 0.11%) since 7/1/2024 |
| 47 | VA | Graduated 2-5.75% | R-1 | VA-5 monthly + VA-6 annual recon (most filers monthly) | $8,000 / 2.5% new / 0.1-6.2% | VA New Hire Reporting Center | N | N | N | VirginiaSaves (RetirePath) mandate for 25+ EE (eff. 7/1/2023) |
| 48 | WA | NoPIT | N/A | N/A | $72,800 (highest in US) / 1.0% new / 0.27-6.03% | WA DSHS Child Support | N | **Y WA PFML 0.92% + Cares Fund LTC 0.58%** | N | **AUDIT FLASH POINT: WA Cares Fund 0.58% employee-only payroll deduction (LTC trust); WA Paid Sick Leave statewide**; highest SUTA wage base in US |
| 49 | WV | Graduated 2.36-5.12% | WV/BUS-APP | IT-101 quarterly/monthly per tier | $9,500 / 2.7% new (8.5% construction) / 1.5-8.5% | WV BCSE New Hire | N | N | **Y (4 cities — service fee flat $$ ): Charleston, Huntington, Wheeling, Weirton** | City fees collected via local form, not withholding |
| 50 | WI | Graduated 3.5-7.65% | BTR-101 | WT-6 monthly + WT-7 annual | $14,000 / 3.05% new (3.25% construction) / 0.0-12.0% | WI DCF Trust Fund | N | N | N | WI new-construction rate higher; weekly deposit threshold $5K/month |
| 51 | WY | NoPIT | N/A | N/A | $32,400 / 0.07-8.5% (rate by NAICS) / no fixed new-emp | WY DWS | N | N | N | New-employer rate set by industry classification |

## 5. State-by-state notable quirks (selected high-risk states)

### 5.1 California — the heaviest state-level burden in the US

- **CA SDI rate** — 1.20% percent of wages (no wage cap since 2024 (SB 951 removed the cap))  _(CA-EDD Form DE 9 / DE 9C)_

A $500K/yr executive pays $6,000+ to SDI annually. AUDIT FLASH POINT: payroll providers from 2023 or earlier still capping at the old wage base.

- **CalSavers retirement mandate** — Any employer with 1+ employee that does not sponsor a qualified retirement plan must register and facilitate Roth IRA contributions. Deadline elapsed 12/31/2023 for all sizes.  _(CalSavers)_
- **CA PIT top marginal rate** — 12.3% + 1% Mental Health Services Tax on income >$1M = 13.3% top marginal percent  _(PIT brackets)_
- **DE 9 / DE 9C filing** — Filed quarterly through e-Services for Business; due last day of month after Q-end. DE 9C is the wage-detail return; DE 9 is the contribution return.  _(DE 9 / DE 9C)_
- **WTPA wage notice** — Must be furnished at hire.  _(Labor Code §2810.5)_

### 5.2 New York — the convenience-of-employer trap

- **NYS-45 combined quarterly return** — Combined quarterly return: state PIT WH + SUTA + MCTMT (where applicable). One form, four parts.  _(NYS-45)_
- **Convenience-of-employer rule** — If a NY employer permits remote work for the employee's convenience (not the employer's necessity), the wages are NY-sourced even if the employee never sets foot in NY. This rule cost out-of-state remote workers ~$1B+ in NY tax during 2020-2022. AUDIT FLASH POINT when onboarding a remote employee for a NY-based employer.  _(TSB-M-06(5)I)_
- **MCTMT rate and threshold** — 0.34-0.60% on payroll where total quarterly payroll within the MCTD (12 downstate counties) exceeds $312,500. Self-employed have a separate MCTMT regime. percent  _(MCTMT)_
- **NY PFL employee deduction** — 0.388% of wages capped at NYSAWW × 0.388%, remitted to the private DBL carrier percent  _(NY PFL)_
- **NYC resident-only city PIT** — 3.078-3.876% graduated; employer must withhold for NYC residents but not for non-residents percent  _(NYC)_
- **Yonkers earnings tax** — Resident (16.75% of NY state tax) and non-resident (0.5%) earnings tax percent  _(Yonkers)_

### 5.3 New Jersey — multi-deduction stub mandate

- **NJ paycheck line items requirement** — Employee paychecks must reflect separate line items for: NJ SIT; NJ UI/HC/WD (combined); NJ Workforce Development Partnership Fund; NJ SDI (TDI) — employee portion; NJ FLI — Family Leave Insurance
- **NJ wage bases** — SUI base ($43,300), TDI base ($165,400), and FLI base ($165,400) are different — payroll software must carry three wage bases. AUDIT FLASH POINT. USD
- **NJ-927 return** — NJ-927 is the quarterly combined return.  _(NJ-927)_

### 5.4 Pennsylvania — Act 32 EIT compliance

- **Residency Certification Form** — Every employee completes the Residency Certification Form at hire, declaring: Resident PSD code (6-digit political subdivision identifier); Work-location PSD code; Resident EIT rate; Non-resident EIT rate (for work location)  _(Act 32)_
- **PA EIT withholding rule** — Employer withholds the higher of the two rates and remits to the work-location's Tax Collection District (one of 69).
- **LST — Local Services Tax** — Flat $52/yr maximum, withheld in equal installments. If the employee works in multiple LST jurisdictions, the $52 cap is shared and the employee files for refund. USD/yr

PSD-code mismatches generate notices from any of the ~21 active TCDs (Berkheimer, Keystone, Capital Tax, etc.). A wrong PSD code on day one will compound for years.

### 5.5 Ohio — RITA/CCA municipal withholding

- **Ohio municipal income tax administration** — ~600 Ohio municipalities impose a local income tax (0.5-3.0%). Most are administered through one of: RITA (Regional Income Tax Agency) — ~330 municipalities; CCA (Central Collection Agency, Cleveland-based) — ~50 municipalities; Self-administered (Columbus, Cincinnati, Akron, Toledo, etc.) percent
- **20-day rule** — Withholding rules under HB 110 (2021) and the 20-day rule: employer withholds for the work-location city for the first 20 days an employee works there, then switches to the principal-place-of-work municipality.  _(HB 110 (2021))_
- **Courtesy withholding** — Employees who live in a city with a higher rate than their work city are entitled to a "courtesy withholding" of the difference, but it is voluntary for the employer.

Remote workers post-2021 sometimes get incorrectly withheld for the office-city when they actually never go there. HB 110 phased out the COVID-era principal-place-of-work emergency rule; the 20-day test now applies.

- **School-district income tax (SDIT)** — Separate school-district income tax (SDIT) withholding on Form SD-101 for ~190 school districts (paid by residents of those districts).  _(Form SD-101)_

### 5.6 Washington — Cares Fund LTC + PFML stack

- **WA Cares Fund** — 0.58% employee-only payroll tax (no wage cap) funding a state long-term-care trust. Opt-out window closed 12/31/2022 for existing LTCi holders; very few are exempt now. percent  _(WA Cares Fund)_
- **WA PFML** — 0.92% combined; employer share 28.57%, employee share 71.43% for 2025 (varies annually based on premium experience). percent  _(WA PFML)_
- **No PIT** — No PIT so employers register only with WA ESD for both unemployment and PFML.

Out-of-state employer with WA-resident remote employee must register for both PFML and Cares Fund — many miss this.

### 5.7 Oregon — TriMet & Statewide Transit

- **TriMet payroll tax** — 0.8237% 2025: employers pay on wages of services performed within the TriMet district (Portland metro 3-county area). Filed on Form OR-OQ. percent  _(Form OR-OQ)_
- **Lane Transit District (LTD)** — 0.79% on services performed in the LTD area (Eugene metro). percent
- **Statewide Transit Tax (STT)** — 0.10% employee deduction on all OR wages. percent
- **Paid Leave Oregon** — 1.00% on wages; employers with ≥25 employees split 40% employer / 60% employee. percent
- **OregonSaves retirement mandate** — Phased in 2020-2023 for all employers without a qualified plan.  _(OregonSaves)_

### 5.8 Colorado — FAMLI

- **FAMLI rate and split** — 0.90% on wages up to SS base; 50/50 employer/employee split for employers with ≥10 employees; employee-only for employers <10. percent  _(FAMLI)_
- **CO SecureSavings retirement mandate** — Retirement mandate for employers with 5+ employees since 12/31/2023.  _(CO SecureSavings)_

### 5.9 Illinois — Secure Choice + Chicago

- **IL Secure Choice mandate** — 5+ employees, no qualified plan → must register and facilitate Roth IRA contributions.  _(IL Secure Choice)_
- **Chicago Paid Leave & Paid Sick Leave ordinance** — Effective 7/1/2024, layers on top of IL state ESST.
- **IL flat PIT rate** — IL is flat 4.95% so withholding tables are simple, but local-equivalent obligations (transit fund, expense reimbursement under IL Wage Payment Act §9.5) are easy to miss. percent  _(IL Wage Payment Act §9.5)_

### 5.10 Massachusetts — PFML

- **MA PFML rate and split** — 0.88%: the only state-administered combined medical + family leave with employer/employee split that varies by employer size. Employers <25 EE pay 0.18% (employee-only for medical portion); ≥25 EE pay full 0.88% with employer covering 60% of medical / 0% of family. percent  _(MA PFML)_
- **Millionaires Tax surtax** — The 4% surtax on income >$1M (the "Millionaires Tax," Article 44) means high earners need additional withholding via Form M-4. percent  _(Article 44)_

## 6. AUDIT FLASH POINTS — multi-state remote workers

The convenience-of-employer rule (also called the "convenience of the employer" rule or COE rule) is the single largest audit flash point for multi-state employers in 2024-2025:

**Convenience-of-employer rule by state**  _(See table)_

| State | Authority | Effect |
| --- | --- | --- |
| New York | TSB-M-06(5)I | Wages of NY-based employer's remote employee sourced to NY unless employer requires the out-of-state location |
| New Jersey | Adopted 2023 (P.L. 2023, c.125) — limited reciprocal application against NY | Reverse convenience rule that sources to NJ in mirror situations |
| Connecticut | Conn. Gen. Stat. §12-711(b)(2)(C) | COE applies when nonresident works for CT employer |
| Pennsylvania | 61 Pa. Code §109.8 | COE rule for PA-employer non-resident remote workers |
| Nebraska | Nebraska Reg-22-003.01C | COE rule applies |
| Arkansas | Reg. §1.26-51-202 | COE rule applies |
| Delaware | 30 Del. C. §1124 (interpretation) | COE rule applies |

Practical guidance: when a client has a remote employee residing outside a COE-rule state but employed by a company headquartered in one of these seven states, withholding both states' PIT may be required, with the employee filing for credit. The default conservative position is to withhold for the COE state plus the residence state until the employee files for an exemption.

## 7. Practitioner self-check list

Before finalizing a multi-state payroll setup, verify each item:

- [ ] FEIN obtained for the entity
- [ ] State withholding registration in each state where employees physically perform services
- [ ] SUTA registration in each state where wages are localized under the 26 USC §3306(j) four-part test (services localized → services performed in the state → base of operations → direction & control → residence)
- [ ] SUTA new-employer rate confirmed against state agency; some states (SC, ND, MT) deviate from a single rate
- [ ] State new-hire reporting account created (multi-state employers may elect a single state under §653a(b)(1)(B) by filing election with HHS-OCSS)
- [ ] PFML registration in each state with a mandate (CA, NY, NJ, RI, MA, WA, OR, CT, CO, DC, ME from 2025; MN, DE, MD from 2026)
- [ ] SDI registration in CA, HI, NY, NJ, RI (mandated states)
- [ ] Local tax setup:
  - [ ] PA: Residency Certification Form completed; PSD codes verified; TCD identified
  - [ ] OH: RITA/CCA/self-administered city determined; SDIT verified
  - [ ] KY: County occupational license registration
  - [ ] NY: NYC vs Yonkers resident WH; MCTMT threshold checked
  - [ ] MD: county code verified
  - [ ] IN: county tax code per residence as of 1/1
- [ ] State retirement mandate registered or opted out:
  - [ ] CA CalSavers (1+ EE)
  - [ ] IL Secure Choice (5+ EE)
  - [ ] OR OregonSaves (all sizes)
  - [ ] CO SecureSavings (5+ EE)
  - [ ] CT MyCTSavings (5+ EE)
  - [ ] MD Saves (2+ yr W-2 employer)
  - [ ] VA RetirePath (25+ EE)
  - [ ] NY Secure Choice (10+ EE)
  - [ ] NJ Secure Choice (25+ EE)
- [ ] Transit district setup:
  - [ ] OR TriMet (Portland metro) / LTD (Eugene metro)
  - [ ] NY MCTMT (12 downstate counties; threshold $312,500/qtr)
- [ ] WA Cares Fund 0.58% if any WA-resident employee
- [ ] State paid-sick-leave compliance (separate from PFML): AZ, CA, CO, CT, IL, MD, MA, MI, MN, NV, NJ, NM, NY, OR, RI, VT, WA, DC + many municipalities
- [ ] Workers' compensation insurance procured in each state of employment (this matrix does not cover WC rates)
- [ ] Convenience-of-employer review for any remote employee of a NY/NJ/CT/PA/NE/AR/DE-based employer

## 8. Provenance

**Provenance table**  _(See table)_

| Data point | Source |
| --- | --- |
| SUTA wage bases & rates 2025 | State unemployment agency websites; APA Bulletin Q4 2024; cross-referenced with US DOL ETA-204 reports |
| State PIT brackets | State revenue agency 2025 withholding tables |
| Quarterly return form names | State revenue agency current forms list 2025 |
| PFML programs and rates | State PFML agency 2025 rate notices (CA EDD, NY DOL, NJ DOL, RI DLT, MA DFML, WA ESD, OR PLO, CT PFLI, CO FAMLI, DC OPFL) |
| New-hire reporting agencies | Federal Office of Child Support Services state-by-state directory under 42 U.S.C. §653a |
| Convenience-of-employer states | State tax department published rulings; Edward A. Zelinsky v. Tax Appeals Tribunal (NY 2003); Huckaby v. NY State Div. of Tax Appeals (2005) |
| Local tax inventory | Tax Foundation 2024 local income tax census; state Dept Revenue lists |
| Retirement mandate states | NAGDCA 2024 state retirement program tracker |

This matrix is a starting reference. Every state agency may revise rates, wage bases, and form names mid-year. Reviewer must verify the current rate at filing time. Last consolidated review: 2025-11-15.

## Cross-references

- `us-form-941-940-payroll.md` — Federal employer payroll obligations
- `us-multi-state-allocation.md` — W-2 wage allocation for multi-state employees
- `us-1099-nec-issuance.md` — Contractor reporting
- `ca-540-individual-return.md` — California state return (resident perspective)
- `tx-franchise-tax.md` — Texas state-level reporting
- `us-tax-workflow-base.md` — Workflow runbook (load alongside)

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
