---
name: ma-auto-entrepreneur
description: Use this skill whenever asked about Morocco's auto-entrepreneur regime for tax year 2026, the turnover-based income tax option for individuals running a small commercial, industrial, artisanal or service activity. Trigger on phrases like "auto-entrepreneur Maroc", "Morocco freelancer tax", "régime auto-entrepreneur", "micro business Morocco tax", "RNAE", "statut auto-entrepreneur", "تاجر ذاتي", "freelance Maroc impôt". Covers the MAD 500,000 and 200,000 ceilings, the 0.5% and 1% liberatory rates, the droit complémentaire bands, the 30% client withholding above MAD 80,000 from one client, excluded professions, monthly or quarterly declarations, penalties and exit after two years over a ceiling. Reply in the user's language (English, French, or Moroccan Arabic / Darija). Cross-reference ma-cpu and morocco-professional-income-tax for alternatives.
version: 1.1
jurisdiction: MA
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Morocco: auto-entrepreneur regime, tax year 2026

## Scope

This skill covers individuals taxed as auto-entrepreneurs (AE) in Morocco for 2026: income tax on turnover collected, the droit complémentaire, client withholding, registration, declarations, penalties and leaving the regime. The currency is the dirham (MAD, DH). The tax authority is the Direction Générale des Impôts (DGI).

The AE tax applies to collected turnover with no deduction of expenses (Art. 42 bis). It is liberatory (Art. 73, last paragraph), so a person with only liberatory income need not file the annual global income return unless they consider themselves overtaxed or claim the Art. 28 or Art. 74 deductions (Art. 86-3°).

Reply in the user's language. Moroccan users mix English, French and Darija, so keep the native terms (auto-entrepreneur, IR, DGI, CNSS, AMO, RNAE) and explain them.

Out of scope, route elsewhere: TVA detail to `morocco-vat`; employees to `morocco-payroll`; companies to `morocco-income-tax`; the CPU regime to `ma-cpu`; net-income regimes to `morocco-professional-income-tax`; CNSS and AMO detail to `ma-social-contributions`.

## Ask the client first

1. What exactly is the activity? Check it against the excluded list and the activity lists below.
2. Is it commercial, industrial or artisanal, service, or a mix? This sets the rate and ceiling.
3. How much turnover was actually collected in the year, per activity?
4. For services, how much was invoiced to each client in the year? Is any client above MAD 80,000, and is that client a company or an individual on the net real or simplified regime?
5. Was either ceiling exceeded last year as well as this year?
6. Is declaration monthly or quarterly, and were any periods missed?

If the activity mix is not given, work with services (1%, MAD 200,000) until the client confirms otherwise. If the activity could fall on the excluded list, treat it as excluded until confirmed. If turnover is near a ceiling, assume the ceiling is breached and warn about exit. If one services client is near MAD 80,000, assume the 30% withholding applies and confirm with the client.

## The method, step by step

1. Confirm eligibility: an individual, an activity not excluded, turnover within the limits, and membership of the social security scheme (Art. 42 ter-II).
2. Split collected turnover by activity and test each ceiling.
3. For services, find each client's annual total. Anything above MAD 80,000 for one client is the surplus, taken out of the AE rate.
4. Apply 0.5% or 1% to the remaining collected turnover.
5. Apply 30% to the surplus. The client withholds it where the client is a withholding payer.
6. Find the droit complémentaire band from the annual tax amount and add it.
7. Declare and pay by the deadline, and test the two-year exit rule.

### Rates, bands and thresholds ([CGI Art. 42 bis, 42 ter, 45 bis-II, 73](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

| Item | Figure | Who and when | Article | Official URL |
|---|---|---|---|---|
| Ceiling, commercial, industrial, artisanal | MAD 500,000 collected a year | Option condition, tested each year | Art. 42 ter-II-A | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Ceiling, services | MAD 200,000 collected a year | Option condition, tested each year | Art. 42 ter-II-A | same |
| IR rate, commercial, industrial, artisanal | 0.5% of collected turnover | Up to MAD 500,000 | Art. 73-III | same |
| IR rate, services | 1% of collected turnover | Up to MAD 200,000 | Art. 73-III | same |
| One-client limit, services only | MAD 80,000 a year | Surplus leaves the AE rate | Art. 42 bis, 45 bis-II | same |
| Withholding on the surplus | 30%, liberatory | Applied by a client that is a legal person or an individual on the net real or simplified regime | Art. 73-II-G-8°, 157-II | same |
| Gains on business assets | Art. 73-I scale | Net gains on sale or withdrawal of tangible and intangible assets, computed under Art. 40-II | Art. 42 bis | same |

The tax is increased by a droit complémentaire from the Art. 73-II-B-6° table, on terms set by regulation (Art. 73-III). Bands are by annual tax in dirhams:

| Annual tax (MAD) | Per quarter (MAD) | Per year (MAD) | Official URL |
|---|---|---|---|
| Under 500 | 300 | 1,200 | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| 500 to 1,000 | 390 | 1,560 | same |
| 1,001 to 2,500 | 570 | 2,280 | same |
| 2,501 to 5,000 | 720 | 2,880 | same |
| 5,001 to 10,000 | 1,050 | 4,200 | same |
| 10,001 to 25,000 | 1,500 | 6,000 | same |
| 25,001 to 50,000 | 2,250 | 9,000 | same |
| Over 50,000 | 3,600 | 14,400 | same |

The lowest band applies at any tax amount under MAD 500, so a nil year sits in that band on the table's wording. The implementing regulation was not read; see "Not yet confirmed".

### The base ([CGI Art. 42 bis, 43-5°](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

- The base is turnover collected in the year, not invoiced, with no expenses.
- Mixed activities: apply each rate to its own turnover. The option holds if turnover in each category stays within its own limit, or if total turnover stays within the limit for the main activity (Art. 43-5°).
- One client: first MAD 80,000 stays at the AE rate, the surplus goes to withholding. The rule covers services only. Goods sold to one client are not caught.
- A person mostly working for one company also has a labour-law risk of being treated as an employee. That is outside tax; refer it.

### Who can opt in ([CGI Art. 42 ter; Decree 2-15-263; Decree 2-15-303](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

Individuals carrying on a professional activity alone as auto-entrepreneurs under the applicable legislation (Art. 42 bis). The Art. 42 ter-II-B condition is joining the social security scheme. Loi 114-13 is the status law; Decree 2-15-303 lists the activities allowed.

Decree 2-15-263 excludes: architects, insurers, lawyers, money changers, surgeons, dental surgeons, statutory auditors, goods commission agents, accountants, tobacco retailers, publishers, chartered accountants, driving-school operators, cinema operators, clinic operators, medical laboratory operators, private school operators, surveyors (géomètres, topographes), hoteliers, bailiffs, printers, booksellers, land developers and property promoters, aircraft or helicopter lessors, mandataires négociants, property dealers, retail and wholesale jewellers, export and import merchants, quantity surveyors, doctors, notaries, event and reception service providers, pharmacists, opticians, radiologists, consultancy offices (bureau d'études), customs agents and veterinarians.

Decree 2-15-303 list 1 covers food, textile, wood, metal and similar manufacture, shop and market retail, mail order and internet sales, and handicrafts. List 2 covers services such as IT consulting and development, business and management consulting, design, photography, cleaning, transport, repairs, building finishing work, beauty and hairdressing, sport, tutoring support and artistic trades. "Conseil pour les affaires" is on list 2, but a "bureau d'études" is excluded, so a consultant's real set-up must be checked.

## Boundary and exception table

| Situation | Result | Source |
|---|---|---|
| Over a ceiling for one year only | Option stays valid | Art. 43-4° |
| Over a ceiling for two consecutive years | Net real regime from 1 January of the next year, unless RNS or CPU is elected; AE regime lost for good | Art. 43-4° |
| Services client above MAD 80,000, company payer | 30% on surplus withheld by client | Art. 42 bis, 157-II |
| Services client above MAD 80,000, payer is a private individual or CPU taxpayer | Surplus still leaves the AE rate; the client is not a named withholder. Refer | Art. 45 bis-II, 157-II |
| TVA, manufacturer or service provider, turnover up to MAD 500,000 | Exempt without deduction right | Art. 91-II-3° |
| TVA, trader | Not covered by Art. 91-II-3°; use `morocco-vat` | Art. 89, 91 |
| Bookkeeping duties of Art. 145 | Not applicable, except holding an email address | Art. 145-X, XI |
| Excluded profession | No AE option; use `ma-cpu` or `morocco-professional-income-tax` | Art. 42 ter-III |

## Worked cases

### Case 1: service freelancer, several clients

Sara is a freelance web developer. She collects MAD 150,000 in 2026 from 5 clients, the largest paying MAD 45,000. She is within the ceiling and no client is above 80,000.

```oa-check
name: Services AE, MAD 150,000 collected
inputs:
  turnover: 150000
  droit: 2280
steps:
  - ir: turnover * 0.01
  - total: ir + droit
expected:
  ir: 1500.00
  total: 3780.00
```

### Case 2: which should I choose, AE or CPU?

The same MAD 150,000 under CPU, "Autres prestations" coefficient 20% (Art. 40-I), rate 10% (Art. 73-II-B-6°): income 30,000, tax 3,000, droit band 2,501 to 5,000 at MAD 2,880, total MAD 5,880. AE costs MAD 3,780, so AE is MAD 2,100 cheaper. Past MAD 200,000 of services a year, AE stops being available in the long run and CPU comes back into play. Use `ma-cpu` for its conditions.

```oa-check
name: AE or CPU at MAD 150,000 services
inputs:
  turnover: 150000
  ae_droit: 2280
  cpu_droit: 2880
steps:
  - ae_total: turnover * 0.01 + ae_droit
  - cpu_tax: turnover * 0.20 * 0.10
  - cpu_total: cpu_tax + cpu_droit
  - saving: cpu_total - ae_total
expected:
  ae_total: 3780.00
  cpu_total: 5880.00
  saving: 2100.00
```

### Case 3: one dominant client

Youssef does design work and collects MAD 120,000: MAD 100,000 from one agency (a company) and MAD 20,000 from others. The surplus above 80,000 is MAD 20,000.

```oa-check
name: Services AE with one client above 80,000
inputs:
  one_client: 100000
  others: 20000
steps:
  - surplus: max(one_client - 80000, 0)
  - ir: (one_client - surplus + others) * 0.01
  - withheld: surplus * 0.30
  - total_tax: ir + withheld
expected:
  surplus: 20000.00
  ir: 1000.00
  withheld: 6000.00
  total_tax: 7000.00
```

Whether the droit band counts only the MAD 1,000 is not settled here; on that footing it is MAD 1,560. Flag the concentration as a disguised-employment risk.

### Case 4: commercial activity

Khadija resells handmade goods and collects MAD 400,000. Tax is 400,000 x 0.5% = MAD 2,000. Droit band 1,001 to 2,500: MAD 2,280.

```oa-check
name: Commercial AE, MAD 400,000 collected
inputs:
  turnover: 400000
  droit: 2280
steps:
  - ir: turnover * 0.005
  - total: ir + droit
expected:
  ir: 2000.00
  total: 4280.00
```

### Case 5: ceiling breach

Omar (services) collects MAD 230,000 in 2026. One year over does not end the option. If 2027 is also over, the net real regime applies from 1 January 2028 unless he elects RNS or CPU, and he can never return to AE. On the net real or simplified regime the ordinary Art. 73-I scale applies: the first MAD 40,000 is exempt and the top rate is 37%. Model the exit with `ma-cpu` and `morocco-professional-income-tax`, and check TVA.

## When to refuse or refer

Refer to a Moroccan expert-comptable when:

- one client's share suggests disguised employment;
- a ceiling is breached in the current or prior year, including the rate for the excess turnover;
- the activity is borderline for the excluded list;
- mixed activities straddle both ceilings;
- CNSS or AMO entitlement or arrears are disputed;
- TVA may apply;
- business assets are sold or withdrawn, because the Art. 73-I scale then applies.

Do not confirm eligibility for an excluded profession. Do not deduct expenses. Do not invent social contribution amounts. Do not present a return as filed without expert-comptable sign-off.

## Filing and payment ([CGI Art. 44-II, 82 bis, 148-V, 173-II, 184, 208](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

Registration: the option is made when filing the déclaration d'existence with the designated body (Art. 44-II, 148-V). That body sends a copy to the tax administration.

Steps each period:

1. Add up turnover collected in the period, per activity.
2. Complete the model form set by the designated body (Art. 82 bis-I), including a nil period if the portal asks for one.
3. Pay to the same body within the deadline (Art. 173-II).
4. Keep proof of filing and payment.

| Option | Period | Deadline |
|---|---|---|
| Monthly | Each month | Before the end of the following month |
| Quarterly, Q1 | Jan to Mar | Before 30 April |
| Quarterly, Q2 | Apr to Jun | Before 31 July |
| Quarterly, Q3 | Jul to Sep | Before 31 October |
| Quarterly, Q4 | Oct to Dec | Before 31 January of the next year |

Rules for control, sanctions, disputes and limitation are those of the CPU regime (Art. 82 bis-IV).

Late filing (Art. 184): 5% up to 30 days late; 15% after 30 days; 20% on assessment for no return or an incomplete one. The minimum is MAD 100 for an AE turnover return, and an incomplete return with no effect on the base costs MAD 100.

Late payment (Art. 208-I): penalty 10%, or 5% if within 30 days; surcharge 5% for the first month and 0.5% for each further month or part month.

Social cover: Art. 42 ter-II-B requires membership of the scheme. AMO health cover, base pension and daily allowances detail sits in `ma-social-contributions`.

## Completion checklist

- [ ] Activity checked against both decrees
- [ ] Turnover is collected, split by activity
- [ ] Each ceiling tested, this year and last
- [ ] Each services client tested against MAD 80,000
- [ ] Surplus withheld or referred
- [ ] Droit complémentaire band found
- [ ] Deadline and any Art. 184 or 208 cost stated
- [ ] TVA position routed

## Sources

| Source | URL | Read on |
|---|---|---|
| CGI 2026 (DGI), Art. 40, 42 bis to 44, 45 bis, 73, 82 bis, 86, 91, 145, 148, 157, 173, 184, 208 read in text extract | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 | 2026-11-01 |
| Decrees 2-15-263 and 2-15-303, as annexed to the CGI 2026 | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 | 2026-11-01 |

Not yet confirmed: cnss.ma and ae.gov.ma would not open in a browser on 2026-11-01 and have no 2026 archive copy, so these old-version items are unverified and kept out of the rules: social contribution rules and the "T1 to T8" brackets, whether they match the eight CGI bands; the old minimum of about MAD 300 a quarter for a nil period; the bases of 50% (services) and 20% (commercial) of turnover; Décret 2.21.477 as the AMO source; the RNAE portal address rn.ae.gov.ma, Poste Maroc or Al Barid Bank as designated body, free registration, the 7 to 15 day processing and card; online payment channels; duty to file nil returns and radiation for missed returns. Also unread: the regulation fixing droit complémentaire terms, including part years and whether the withheld surplus counts for the band; the rate on turnover above a ceiling in a year still within the option; the full text of Loi 114-13, including residence as a condition. The old list named engineers, adouls, regulated transport, alcohol and financial intermediaries as excluded; Decree 2-15-263 does not name them, so check any such case individually.

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
