---
name: gf-payroll
description: "French Guiana employer payroll and wage income tax withholding for calendar year 2026. Apply the DGFiP rate or the correct Guyane default withholding table, distinguish taxable net pay from cash net pay, process short contracts, and report and pay through DSN. Covers first-hire registration, actual DSN field identifiers, rate feedback, corrections, monthly and quarterly payment conditions, and ordinary withholding and declaration penalties. Trigger on Guyane payroll, French Guiana salary, prélèvement à la source, PAS, DSN, net imposable, net à payer, taux neutre Guyane and DPAE. Contribution rates, LODEOM and self-employed social security are owned by gf-social-contributions; annual personal tax and treaty residence are handled in the sibling Guides."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/gf-payroll"
  jurisdiction: "GF"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# French Guiana payroll and wage withholding 2026 v0.1

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.


## Who this applies to

This Guide handles an ordinary private employer paying salary for work in French Guiana, part of the French tax and social security system. Currency: EUR. The employer collects income tax by prélèvement à la source (PAS); the employee still files an annual income tax return. Withholding is an advance, not the annual tax calculation.

**Required inputs before computing:** payment date and usual pay frequency; employee's actual tax domicile; valid DGFiP CRM rate and identifier; taxable pay components and exempt items; contract term and start date; employer headcount, pay timing and payment elections. An employer's Cayenne address does not establish an employee's tax domicile. Use [gf-social-contributions](gf-social-contributions.md) for every employee/employer contribution rate and relief, [gf-income-tax](gf-income-tax.md) for the annual assessment, and [gf-cross-border-tax](gf-cross-border-tax.md) for residence, treaties and non-resident wage withholding.

| Situation | Rule and exception |
|---|---|
| Valid DGFiP rate transmitted | Use it, including a valid zero rate. Do not replace it with an estimated family tax rate or independently apply a DOM income tax reduction. |
| No valid rate, including a new hire or privacy choice | Use the default table for the employee's domicile and payment date. For monthly payments to a Guyane tax resident use the table below. |
| Qualifying short CDD or mission and no transmitted rate | Apply the short-contract base deduction below for the first two months; otherwise ordinary default method. |
| Non-resident or treaty-exempt income | Determine the special rule before payroll. Ordinary PAS is not interchangeable with CGI art. 182 A non-resident withholding. |
| Self-employed drawings or business income | Not salary PAS; tax authority instalments and personal social contributions apply. |

Sources: CGI arts. 204 A/B/F/H and DGFiP BOI-IR-PAS-20-10-10 §10, BOI-IR-PAS-20-20-30 §§10-70, 230-280.

## Rates, bands and thresholds

**Guyane monthly default PAS, not marginal income-tax bands.** Select one rate from the payment's base, then apply that rate to the whole PAS base. Lower bounds are inclusive; upper bounds exclusive. No additional annual DOM reduction is made by the employer. Each row cites the official table, §20. January-April uses the table effective from May 2025; May-December uses the table effective from May 2026. The July 2026 BOFiP update changes the short-contract deduction, not these bands.

| Monthly PAS base, January-April 2026 | Monthly PAS base, from 1 May 2026 | Rate on whole base | Official source |
|---|---|---|---|
| Below 1,990 | Below 2,008 | 0% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 1,990 to below 2,151 | 2,008 to below 2,170 | 0.5% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 2,151 to below 2,398 | 2,170 to below 2,420 | 1.3% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 2,398 to below 2,704 | 2,420 to below 2,728 | 2.1% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 2,704 to below 2,808 | 2,728 to below 2,833 | 2.9% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 2,808 to below 2,904 | 2,833 to below 2,930 | 3.5% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 2,904 to below 2,999 | 2,930 to below 3,026 | 4.1% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 2,999 to below 3,332 | 3,026 to below 3,362 | 5.3% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 3,332 to below 4,598 | 3,362 to below 4,639 | 7.5% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 4,598 to below 5,951 | 4,639 to below 6,005 | 9.9% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 5,951 to below 6,712 | 6,005 to below 6,772 | 11.9% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 6,712 to below 7,788 | 6,772 to below 7,858 | 13.8% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 7,788 to below 8,567 | 7,858 to below 8,644 | 15.8% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 8,567 to below 9,492 | 8,644 to below 9,577 | 17.9% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 9,492 to below 11,016 | 9,577 to below 11,115 | 20% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 11,016 to below 14,820 | 11,115 to below 14,953 | 24% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 14,820 to below 18,850 | 14,953 to below 19,020 | 28% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 18,850 to below 30,210 | 19,020 to below 30,482 | 33% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 30,210 to below 63,767 | 30,482 to below 64,341 | 38% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |
| 63,767 and above | 64,341 and above | 43% | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 (earlier); https://bofip.impots.gouv.fr/bofip/11255-PGP.html (May onward), §20 |

| Other payroll parameter | Rule / period / conditions | Official source |
|---|---|---|
| Transmitted rate validity | Last day of second month following availability; apply the received rate by that deadline, not indefinitely | CGI art. 1671(2), BOI-IR-PAS-20-20-30 §§60-70, https://bofip.impots.gouv.fr/bofip/11252-PGP.html |
| Qualifying short-contract deduction, 1 January-31 May 2026 | EUR 748 per month; half net taxable SMIC EUR 1,495.04, rounded; qualifying first two months absent transmitted rate | BOI-BAREME-000037 §30, https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20260407 |
| Qualifying short-contract deduction from 1 June 2026 | EUR 766 per month; half net taxable SMIC rounded, first two months only, absent transmitted rate | BOI-BAREME-000037 §30 (6 July 2026), https://bofip.impots.gouv.fr/bofip/11255-PGP.html; conditions https://bofip.impots.gouv.fr/bofip/11252-PGP.html §§230-280 |
| National minimum gross wage applying in Guyane | EUR 12.02/hour, EUR 1,823.03 monthly at statutory full time, 1 January-31 May 2026; EUR 12.31/hour and EUR 1,867.02 from 1 June | Ministry of Labour series published by INSEE, https://www.insee.fr/fr/statistiques/1375188 |

Use the half net taxable SMIC in force at payment; the BOFiP also permits the 1 January amount throughout that calendar year (§260). The hourly gross SMIC is not the net taxable SMIC used for this deduction. Do not carry forward the older November 2024 short-contract amount shown in the historical default-grid publication.

## The base

**Gross to net, in order.** Identify cash salary, bonuses, benefits in kind, overtime, expense reimbursements, statutory exemptions and the period. Compute contribution bases and employee/employer deductions under [gf-social-contributions](gf-social-contributions.md). Taxable net pay generally equals taxable gross less deductible employee contributions and deductible CSG, with taxable employer health contributions and other taxable reintegrations. Do not use cash paid, the net social amount, or gross pay as a substitute. The ordinary professional-expense deduction in the annual return is not deducted again from salary PAS (CGI art. 204 F; BOI-IR-PAS-20-10-10 §10).

Multiply the PAS base by the transmitted percentage, or by the single default percentage selected from the table, and round to cents. Cash paid is cash net before PAS less PAS. Benefits in kind affect the relevant bases but are not added to cash handed over. The annual result may produce a balance or refund; do not true up the household's annual tax in the employer's December payroll.

**Default-table timing and frequency.** The table in force on the payment date governs; the authority permits implementation of an updated table for payments from the following month. With ordinary monthly salary, do not prorate monthly bands for a part-time employee, midmonth start, midmonth departure or a short working month. Combine the taxable bonus and salary in the same payment before selecting the rate. For genuinely weekly customary pay, convert the monthly bands by 12/52; daily pay by 12/312; or equivalently convert pay to a monthly amount, select the rate, and apply it to actual pay. Round converted boundaries to cents. A one-off bonus does not by itself create a different usual pay frequency (BOI-IR-PAS-20-20-30 §§100-210).

**Short contracts.** A CDD or mission whose initial fixed term does not exceed two months, or such a CDD/mission without a precise end date (à terme imprécis) whose contractual minimum duration does not exceed two months, can use the deduction only while no valid individual rate is available. Count the first two months date to date; renewal does not restart them. A separate contract after an interruption is tested separately. Deduct the authorised monthly short-contract amount from taxable pay, floor at zero, select the ordinary monthly default rate on that reduced base and apply it to that reduced base. Never adjust these short-contract bands to weekly or daily frequency. Once an individual rate arrives, stop the special deduction. The deduction changes PAS only, not the reported taxable salary (same BOFiP §§230-280).

**Common exceptions.** Statutory apprentice/stage income exemption is tested cumulatively by each employer before PAS; ordinary student wages are included at payment even if the employee can claim an annual-return exemption. For subrogated sickness indemnities, the authority's first-60-days rule differs from taxable salary maintenance, maternity/paternity and occupational injury payments. Identify the payment category before selecting its base; use BOI-IR-PAS-20-10-10 §§20-30 and 80-110, rather than treating all sickness pay as exempt. Annual exemption amounts and special impatriate/expatriate calculations are outside this ordinary salary computation.

## Deadlines and filing

**Before first pay.** Complete the DPAE before the employee actually starts, no earlier than eight days before the expected hire. It registers a first employer and initiates the employee's social formalities; it does not replace the employment contract. Use Urssaf/CGSS electronic DPAE or Net-entreprises. Register the establishment SIRET, employee identity/NIR or temporary identifier, date/time of hire and contract information. Arrange DSN-compatible payroll and Net-entreprises DSN access; retrieve actual pension, health, accident and local mobility parameters. Source: Ministry of Labour, [employer hiring formalities](https://travail-emploi.gouv.fr/les-obligations-de-lemployeur-lors-de-lembauche).

| Return/payment | Deadline and conditions | Official source |
|---|---|---|
| Monthly DSN and ordinary contribution payment | 5th of following month for at least 50 employees paid in the employment month; 15th in other cases; non-working-day extension applies | CSS R243-6; DSN technical §1.4; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006186436/; https://entreprendre.service-public.gouv.fr/vosdroits/F34059 |
| PAS collection and remittance | Deduct at salary payment; remit by the applicable following DSN payment deadline to DGFiP via télérèglement | CGI art. 1671; https://entreprendre.service-public.gouv.fr/vosdroits/F34732 |
| Employer with fewer than 11 employees electing quarterly payment | Payment by 15th of first month after the quarter; monthly DSN remains compulsory. Elect with collecting body before 31 December or at first hire; absent renunciation election renews | CSS R243-6-1, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006186436/; https://entreprendre.service-public.gouv.fr/vosdroits/F34732 for PAS quarterly election |
| Event report | Normally five working days for a reportable stop, early return or contract end, subject to the event-specific exceptions in DSN rules | DSN technical §1.4 and https://entreprendre.service-public.gouv.fr/vosdroits/F34059 |
| Replace accepted monthly DSN | Annule et remplace before midnight Paris time on the day before the deadline; later correct through a subsequent DSN, including all affected fields | DSN technical §1.4.3.3, https://www.net-entreprises.fr/media/documentation/dsn-cahier-technique-2026.1.pdf |

**What is filed.** Prepare the 2026 P26V01 DSN from payroll; do not substitute the already-published 2027 specification. In block `S21.G00.50` use: `.001` date of payment; `.002` rémunération nette fiscale; `.004` montant net versé **before PAS** as defined by the technical standard; `.006` PAS rate; `.007` rate type (`01` transmitted, `33` Guyane/Mayotte monthly default); `.008` CRM rate identifier for a transmitted rate; enter `-1` for the qualifying short-CDD/mission default procedure described above, as the technical field requires; `.009` PAS amount; `.013` actual amount subjected to PAS, always populated even if equal to taxable net. Do not subtract PAS in `.004`. The short-contract base difference goes in `.013`, not by reducing `.002` (DSN 2026 technical pp. 243-245).

In Net-entreprises choose DSN régime général, submit the file or use approved machine-to-machine transmission, and retain the deposit receipt, conformity certificate and each body’s CRM. A deposit receipt alone does not prove acceptance or payment. Reconcile employee totals, aggregate contribution/payment blocks and DGFiP total with payroll and bank orders. Enable the bank account and SEPA business mandate in the impots.gouv.fr professional space for PAS; verify the bank has the mandate. Integrate DGFiP's new rate and identifier from its nominative CRM. Resolve identity anomalies before assuming that the missing rate is a zero rate. Ordinary employers do not file PASRAU merely because the establishment is in Guyane (DGFiP employer guidance; DSN technical).

## Penalties and interest

| Failure | Ordinary rule and conditions | Official source |
|---|---|---|
| PAS omission/inaccuracy | 5% of withholding that should have been made/declared | CGI art.1759-0 A(1), https://entreprendre.service-public.gouv.fr/vosdroits/F34732 |
| Late PAS declaration | 10%; 40% if still absent 30 days after formal notice; deliberate omissions/inaccuracies also 40% | CGI art.1759-0 A(2)-(3), https://entreprendre.service-public.gouv.fr/vosdroits/F34732 |
| Deliberately collected but neither declared nor remitted PAS | 80%; the foregoing alternatives are not added together; minimum EUR 250 per declaration | CGI art.1759-0 A(4), https://entreprendre.service-public.gouv.fr/vosdroits/F34732 |
| Late PAS payment | 5% surcharge on unpaid withholding; ordinary statutory late interest0.20% per month applies separately, with period calculated under CGI art.1727 IV | CGI arts.1731/1727 III-IV; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006133936/2026-02-21/; https://entreprendre.service-public.gouv.fr/vosdroits/F34732 |
| Late/missing DSN or omitted employee | 1.5% of monthly social ceiling per employee per month or part-month; delay no more than five days capped at 150% of monthly ceiling once per calendar year | CSS R243-12, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006186436/ |
| Understated remuneration reducing contributions | 1% of monthly social ceiling per employee; other covered inaccuracy/nomenclature failure one third of that penalty | CSS R243-13, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006186436/ |

Use the ceiling owned by [gf-social-contributions](gf-social-contributions.md), not a rounded euro summary on a portal. CSS R243-10 protects qualifying prompt corrections, with exceptions for omitted employees and repeated pay inaccuracies; it does not excuse every late filing. CSS R243-11 can protect a first short payment delay where declarations are current, payment or an honoured plan is arranged within 30 days, there was no delay in the prior 24 months, and penalties are below one monthly ceiling. Social late-payment surcharges and conditions are in the contribution Guide. Deliberate failure to declare and remit PAS for over a month also has penal consequences (CGI art.1771 A); it is not settled by paying an administrative late charge.

## Cross-border points

A transfer between metropolitan France and Guyane is not by itself international social security posting. Determine actual domicile for the neutral tax grid, French-source work and treaty status separately from social affiliation. A non-resident's salary can fall under CGI art.182 A rather than ordinary PAS. Foreign employers and foreign-source salaries can follow different DSN/PASRAU or instalment arrangements. Route those cases to [gf-cross-border-tax](gf-cross-border-tax.md) and obtain the applicable social security certificate before withholding French contributions; no general 183-day payroll exemption exists.

## Two worked examples that recompute

### Example 1: transmitted individual rate on an ordinary monthly salary

October 2026: the payroll working paper establishes cash gross EUR 3,000, all employee deductions EUR 620 and taxable net EUR 2,460 after its deductible/non-deductible analysis. These are case inputs, not statutory contribution rates. A valid DGFiP CRM gives a 3% rate. PAS is 2,460 × 3% = EUR 73.80. Cash net before PAS is 3,000 - 620 = EUR 2,380, then cash paid is EUR 2,306.20. Use the valid transmitted rate even if a default table would collect another amount. DSN `.002` and `.013` are 2,460, `.004` 2,380 and `.009` 73.80.

```oa-check
name: Guyane 2026 transmitted PAS rate and cash net
inputs:
  cash_gross: 3000
  all_employee_deductions: 620
  taxable_net: 2460
  transmitted_percent: 3
steps:
  - pas: round(taxable_net * transmitted_percent / 100, 2)
  - cash_net_before_pas: cash_gross - all_employee_deductions
  - paid: cash_net_before_pas - pas
expected:
  pas: 73.80
  cash_net_before_pas: 2380
  paid: 2306.20
```

### Example 2: decide whether the short-contract deduction applies

August 2026: a Guyane-resident new employee has EUR 2,500 taxable monthly pay and no transmitted rate. Under a qualifying one-month CDD the first-month deduction is EUR 766, so PAS base EUR 1,734 falls in the zero-rate band and PAS is zero. With identical pay but an ordinary CDI, the short-contract condition fails; EUR 2,500 falls in the 2.1% band and PAS is EUR 52.50 on the whole base. The decision is contract eligibility, not a choice to use whichever result is lower. On the CDD, taxable salary `.002` remains EUR 2,500 and PAS base `.013` is EUR 1,734; default type `.007` is `33` and short-contract rate identifier `.008` is `-1`.

```oa-check
name: Guyane 2026 August qualifying CDD versus CDI
inputs:
  taxable_net: 2500
  short_contract_deduction: 766
  cdd_percent: 0
  cdi_percent: 2.1
steps:
  - cdd_base: max(taxable_net - short_contract_deduction, 0)
  - cdd_pas: round(cdd_base * cdd_percent / 100, 2)
  - cdi_pas: round(taxable_net * cdi_percent / 100, 2)
  - difference: cdi_pas - cdd_pas
expected:
  cdd_base: 1734
  cdd_pas: 0
  cdi_pas: 52.50
  difference: 52.50
```

## Ask the client first

1. Payment date, customary pay frequency, full payroll components and contribution working paper, including benefits, health cover, overtime and sickness payments?
2. Employee's actual tax domicile and work locations, treaty status and social security certificate, if any?
3. Latest DGFiP CRM rate, identifier, delivery date and identity matches?
4. Contract type, original term/minimum duration, start date and interruptions/renewals?
5. Establishment SIRET, headcount, salary timing, quarterly-payment elections, accepted DSN/CRM history and payment mandate?

## Sources

| Source and portion actually read | URL | Read on |
|---|---|---|
| DGFiP BOI-BAREME-000037 current publication 6 July 2026, read §20 all Guyane monthly bands and §30 June short-contract deduction | https://bofip.impots.gouv.fr/bofip/11255-PGP.html | 2026-11-11 |
| DGFiP publication 7 April 2026, read §30 for the January 2026 net taxable SMIC and EUR 748 deduction | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20260407 | 2026-11-11 |
| DGFiP historical publication 10 April 2025, read §20 Guyane bands continuing through April 2026; its older short-contract amount was not used | https://bofip.impots.gouv.fr/bofip/11255-PGP.html/identifiant=BOI-BAREME-000037-20250410 | 2026-11-11 |
| DGFiP BOI-IR-PAS-20-10-10, read §10 and §§20-110 for taxable base, annual expenses, students/apprentices and subrogated indemnities | https://bofip.impots.gouv.fr/bofip/11249-PGP.html | 2026-11-11 |
| DGFiP BOI-IR-PAS-20-20-30, read §§10-280 for rate validity, usual frequency and short contracts | https://bofip.impots.gouv.fr/bofip/11252-PGP.html | 2026-11-11 |
| GIP-MDS DSN CT2026.1.2, read §1.4.3.3 and pp. 243-245, including every PAS field and rate-type code used here | https://www.net-entreprises.fr/media/documentation/dsn-cahier-technique-2026.1.pdf | 2026-11-11 |
| Ministry of Finance / Service Public employer PAS duties, read for payment, professional bank account and fiscal sanctions | https://entreprendre.service-public.gouv.fr/vosdroits/F34732 | 2026-11-11 |
| CGI arts.1727/1731, read for interest rate, statutory computation period and late PAS remittance surcharge | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006133936/2026-02-21/ | 2026-11-11 |
| CSS R243-6/6-1 and R243-10 to R243-16, read for collecting body, timing, corrections, declaration penalties and payment relief | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006186436/ | 2026-11-11 |
| Ministry of Labour hiring duties, read for DPAE timing and registration duties | https://travail-emploi.gouv.fr/les-obligations-de-lemployeur-lors-de-lembauche | 2026-11-11 |
| INSEE official SMIC series, read for both 2026 effective dates and Guyane-compatible national rates | https://www.insee.fr/fr/statistiques/1375188 | 2026-11-11 |

Not yet confirmed: none for the ordinary salary PAS computation covered here. Occupation-specific benefits, impatriate/expatriate exemptions and non-resident withholding are not computed here.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `gf-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/gf-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
