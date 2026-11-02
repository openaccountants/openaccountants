---
name: ma-formation
description: Use this skill whenever asked about registering or forming a business in Morocco for tax year 2026, as a self-employed person or a company. Choosing a legal status, the identifiers every business needs (ICE, IF, RC, taxe professionnelle), the tax regime picked at registration, the declaration of existence, registration duties on capital, and VAT status at the start. Trigger on phrases like "register auto-entrepreneur Morocco", "créer auto-entrepreneur", "comment s'inscrire auto-entrepreneur Maroc", "ICE Maroc", "obtenir un IF", "Registre de Commerce Maroc", "start business Morocco", "créer une SARL Maroc", "patente / taxe professionnelle", "كيفاش نسجل مقاول ذاتي", "تسجيل شركة المغرب". Reply in the user's language (English, French, or Moroccan Arabic / Darija) and keep the native terms. Cross-reference ma-auto-entrepreneur, ma-cpu, morocco-professional-income-tax, ma-social-contributions and morocco-vat for the tax detail.
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

# Morocco business formation and registration, tax year 2026

## Who this applies to

An individual starting an activity in Morocco, or founders forming a company or other entity. This skill covers the choice of status and the registrations. Ongoing tax goes to `ma-auto-entrepreneur`, `ma-cpu`, `morocco-professional-income-tax`, `morocco-vat` and `ma-social-contributions`.

Authorities: the DGI (tax.gov.ma), OMPIC (ompic.ma), the regional CRI, the CNSS (cnss.ma), the RNAE (rn.ae.gov.ma, through banks partnered with Poste Maroc), and the Direct Entreprise platform (directentreprise.ma). Currency: MAD (dirham).

Forms available ([CRI Casablanca-Settat, read 2026-11-01](https://casainvest.ma/index.php/fr/d%C3%A9marches-de-cr%C3%A9ation)):

| Form | Key points |
|---|---|
| Entreprise individuelle | Run in the person's own name; no minimum funds; unlimited liability; income tax (IR) |
| Auto-entrepreneur | Simplified individual business; person resident in Morocco; no commercial register entry; filed through Poste Maroc partner banks |
| SNC | No minimum capital; all partners are merchants, with unlimited joint liability; IR by right, irrevocable option for company tax (IS) |
| Société en commandite simple | Managing partners liable without limit; sleeping partners liable up to their contribution |
| SARL (including one partner) | Corporate tax; legal personality once on the commercial register; liability limited to contributions; auditor required only from MAD 50 million turnover; not open to financial companies |
| SA | Minimum capital MAD 300,000 (MAD 3 million for a public offering); at least 5 shareholders; corporate tax |
| SAS / SASU | Law 19.20; one person can form it; organisation set by the articles |
| Société en commandite par actions | Managing partners unlimited, others up to their contributions |
| Société en participation | Not registered; no legal personality; at least two people |
| Succursale | Branch of a parent; no legal personality; company tax |
| GIE | Two or more persons, with or without capital; on the commercial register |

Do not pick the status or regime for the user. Lay out the routes and let them choose. If turnover is near a ceiling, treat the ceiling as breached and set out the consequences (regime exit, VAT). A company's IS is computed in `morocco-corporate-income-tax` when that skill is on the repo; otherwise refer to a Moroccan expert-comptable. This skill's output is not a filed registration.

## Rates, bands and thresholds

Every row: tax year 2026, read 2026-11-01. Rows marked unverified carry a figure from the earlier version that could not be opened at an official page.

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Auto-entrepreneur ceiling, commerce, industry, crafts | MAD 500,000 a year collected | Option; social security membership; excluded trades out | [CGI Art. 42 ter-II](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Auto-entrepreneur ceiling, services | MAD 200,000 a year collected | Same. Mixed activities: each within its own ceiling, or total within the main activity's (Art. 43-5°) | same |
| Auto-entrepreneur IR | 0.5% commerce, industry, crafts; 1% services | On turnover collected | [CGI Art. 73-III](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Auto-entrepreneur, one client | Above MAD 80,000 of services from one client, the excess is withheld by the client at 30% | Annual, per client | [CGI Art. 42 bis, 73-II-G-8°](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Auto-entrepreneur exit | Over the ceiling two consecutive years: real net result from 1 January after, unless RNS or CPU is opted; AE closed for good | | [CGI Art. 43-4°](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| CPU ceiling, commerce, industry, crafts | MAD 2,000,000 a year | AMO membership required. Corrects the MAD 500,000 of the earlier version | [CGI Art. 41-II](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| CPU ceiling, services | MAD 500,000 a year | Same. Corrects the MAD 200,000 of the earlier version | same |
| CPU tax | 10% of turnover x trade coefficient, plus droit complémentaire | Coefficients in `ma-cpu` | [CGI Art. 40-I, 73-II-B-6°](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| RNS ceiling, listed commercial activities | MAD 2,000,000 excluding VAT | Other bands in `morocco-professional-income-tax` | [CGI Art. 39](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| VAT exemption, small makers and providers | Annual turnover up to MAD 500,000 | Natural persons only; once taxable, three consecutive years at or under the figure to leave. Corrects the MAD 200,000 services figure | [CGI Art. 91-II-3°](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| VAT, traders | Wholesalers always; other traders from MAD 2,000,000 of prior-year taxable turnover | | [CGI Art. 89-I-2°](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Capital duty, cash, shareholder current-account debt, profits or reserves | Exempt | Constitution and increase of companies and GIEs, pure and simple contributions | [CGI Art. 129-IV-23°](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Capital duty, in-kind contribution valued by a contributions auditor | Exempt | Constitution only; liabilities attached stay under transfer duty | same |
| Capital duty, other pure and simple new contributions up to MAD 500,000 | MAD 1,000 fixed | Subject to Art. 129-IV-23° | [CGI Art. 135-I-1°](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Capital duty, other new contributions above that | 0.5%, minimum MAD 1,000 | Subject to Art. 129-IV-23°; liabilities at transfer rates | [CGI Art. 133-I-H, 133-II](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Minimum tax relief, company | 36 months from start of operations, ending at most 60 months after constitution | Not concession companies | [CGI Art. 144-I-C-1°](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Minimum tax relief, IR taxpayer | First 3 financial years from start | Not on resuming the same activity after cession | [CGI Art. 144-I-C-2°](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Cash payment, deduction limit | Charges paid other than by the listed traceable means are deductible only up to MAD 5,000 a day and MAD 50,000 a month per supplier | | [CGI Art. 11-II](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| ICE | 15 digits (9 entity, 4 establishment, 2 control) | unverified: ice.gov.ma refused the read | unverified |
| Taxe professionnelle exemption | 5 years from start | unverified: Law 47-06 not opened | unverified |
| Taxe professionnelle rates | 10% to 30% of rental value | unverified: Law 47-06 not opened | unverified |
| SARL minimum capital | None since Law 24-10 | unverified: law not opened | unverified |
| SARL capital blocking | Above MAD 100,000, at least a quarter blocked | unverified: law not opened | unverified |
| Name certificate fee | About MAD 230 | unverified: ompic.ma did not open | unverified |
| SARL cost and time | About MAD 5,000 to 15,000; 10 to 15 working days | unverified: varies by region and adviser | unverified |
| RNAE fee and time | Free; 24 to 72 hours | unverified: ae.gov.ma did not open | unverified |

## The base

**Identifiers.**
- ICE: the common business identifier, on invoices and used across administrations. A return carries a sales statement by client ICE ([CGI Art. 20-I](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1)).
- IF: the tax identifier from the DGI, needed for IR or IS, VAT and invoicing.
- RC: the commercial register, for merchants. An auto-entrepreneur is exempt ([CRI](https://casainvest.ma/index.php/fr/d%C3%A9marches-de-cr%C3%A9ation)). Ask whether the activity is commercial; if it is pure service or liberal, the RC depends on the activity.
- TP: taxe professionnelle, the local tax formerly called patente, charged with the taxe de services communaux. CPU taxpayers are exempt from both and still register, per `ma-cpu`.

**Excluded from auto-entrepreneur** ([Decree under CGI Art. 42 ter-III, CGI annex](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1)): architects, insurers, lawyers, money changers, surgeons, dentists, statutory auditors, goods commission agents, accountants, tobacconists, publishers, expert-comptables, driving-school operators, cinema operators, clinics, medical laboratories, private schools, surveyors, hotel keepers, bailiffs, printers, booksellers, developers, aircraft lessors, trading agents, property dealers, jewellery retailers and wholesalers, export and import merchants, quantity surveyors, doctors, notaries, event and reception providers, pharmacists, opticians, radiologists, study-office holders, customs agents, topographers and vets. Read the list; never infer it. Activity lists 1 and 2 of Decree 2-15-303 decide commerce against services.

**Regulated activity.** If the trade may need a licence or a professional order (health, legal, accounting, engineering, transport, food handling), treat it as needing one until shown otherwise. The status cannot be finalised before that licence.

**The routes.**

| Route | Who | Tax | Skill |
|---|---|---|---|
| Auto-entrepreneur | Individual within ceilings, trade not excluded | 0.5% or 1% of collected turnover, final | `ma-auto-entrepreneur` |
| CPU | Individual within ceilings, AMO member, trade not excluded (Art. 41-III) | 10% of turnover x coefficient, plus droit complémentaire | `ma-cpu` |
| RNS | Mid-size, by option | Simplified net profit, scale | `morocco-professional-income-tax` |
| RNR | Default and above ceilings | Net profit, scale | `morocco-professional-income-tax` |
| SARL or other company | Limited liability or scale | IS, VAT rules below | company tax skill |

If expenses are light and the trade is eligible, compare auto-entrepreneur and CPU first (example 2). If expenses are heavy or the trade is excluded, compare RNR or RNS.

**VAT at the start.** The Art. 91-II-3° exemption covers natural persons only. A company making goods or supplying services is therefore not within it and charges VAT from its first taxable operation. A company that only resells follows the Art. 89-I-2° trader test. Rates and returns: `morocco-vat`; new taxpayers file quarterly in the current year ([CGI Art. 108-II](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1)).

## Deadlines and filing

**Auto-entrepreneur** ([CRI](https://casainvest.ma/index.php/fr/d%C3%A9marches-de-cr%C3%A9ation)):
1. Check the activity is eligible.
2. Pre-register at rn.ae.gov.ma.
3. Build the dossier.
4. File it at a counter of a Poste Maroc partner bank. The AE option is made with this declaration of existence ([CGI Art. 44-II](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1)).
5. Track the dossier online.
6. Receive the auto-entrepreneur card.

CNSS affiliation follows (see `ma-social-contributions`; the automatic link from RNAE is unverified).

**Company.** Direct Entreprise (directentreprise.ma) is the official route for creation formalities, filing of deeds and certificates ([CRI](https://casainvest.ma/index.php/fr/d%C3%A9marches-de-cr%C3%A9ation)). Sequence from the earlier version, order unverified at OMPIC: name certificate (certificat négatif) from OMPIC, articles, capital deposit, RC, IF, TP and CNSS, legal publications. Individual enterprises are exempt from newspaper publication ([CRI](https://casainvest.ma/index.php/fr/d%C3%A9marches-de-cr%C3%A9ation)).

| Filing | Deadline | Source |
|---|---|---|
| Declaration of existence, company | 30 days from constitution, to the local tax office, on the DGI form, with RC, CNSS and TP numbers | [CGI Art. 148-I, II](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Declaration of existence, non-resident | 30 days from installation | same |
| Declaration of existence, individual | 30 days from start of activity | same |
| Registration of the deed | 30 days from its date | [CGI Art. 127, 128-I](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Option for RNS at start | Before 1 May of the year after start | [CGI Art. 44-I](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Option for CPU at start | Within the Art. 82 quater-I periods | same |
| Change of seat or fiscal domicile | 30 days | [CGI Art. 149](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| First IS return | 3 months after year end | [CGI Art. 20-I](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |

After submission keep the receipt or registered-post proof; it is the evidence of the date.

## Penalties and interest

| Default | Penalty | Source |
|---|---|---|
| Declaration of existence late, missing or inaccurate | MAD 1,000 fine, by assessment roll | [CGI Art. 188](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Late returns, deeds | Surcharges of 5%, 15% and 20% by case | [CGI Art. 184](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Late payment | 10% penalty (5% if paid within 30 days; 20% for VAT or tax withheld at source and not paid over), plus 5% for the first month and 0.50% each further month or part | [CGI Art. 208-I](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |

## Cross-border points

A non-resident company setting up files the declaration of existence within 30 days of installation (Art. 148-I). A branch has no legal personality and pays IS ([CRI](https://casainvest.ma/index.php/fr/d%C3%A9marches-de-cr%C3%A9ation)). Only a person resident in Morocco can be an auto-entrepreneur ([CRI](https://casainvest.ma/index.php/fr/d%C3%A9marches-de-cr%C3%A9ation)). Treaties and withholding belong to the cross-border skill.

## Two worked examples that recompute

**Example 1: capital duty on two SARL formations.** Founders contribute MAD 100,000 in cash: exempt under Art. 129-IV-23°. Another contributes MAD 800,000 of equipment with no contributions auditor: 0.5% applies, MAD 4,000, above the MAD 1,000 minimum. A MAD 300,000 such contribution pays the MAD 1,000 fixed duty.

```oa-check
name: Capital duty on in-kind contribution without an auditor
inputs:
  contribution: 800000
steps:
  - duty: max(contribution * 0.005, 1000)
expected:
  duty: 4000.00
```

**Example 2: decision, auto-entrepreneur or CPU.** A graphic designer collects MAD 120,000 of services, no client above MAD 80,000. Auto-entrepreneur: 1%, MAD 1,200. CPU under "Autres prestations" at 20%: 120,000 x 20% x 10% = MAD 2,400, plus the droit complémentaire. On IR, auto-entrepreneur wins by MAD 1,200, if design is confirmed eligible and social costs are compared in `ma-social-contributions`. Income tax scale regimes need the expenses figure.

```oa-check
name: Auto-entrepreneur against CPU, services MAD 120,000
inputs:
  turnover: 120000
steps:
  - ae: turnover * 0.01
  - cpu: turnover * 0.20 * 0.10
  - saving: cpu - ae
expected:
  ae: 1200.00
  cpu: 2400.00
  saving: 1200.00
```

A trader expecting MAD 1,200,000 is over the auto-entrepreneur ceiling but within the CPU ceiling if the trade is not excluded; a lawyer is excluded from auto-entrepreneur and goes to `morocco-professional-income-tax`.

## Ask the client first

- Individual or company, and resident in Morocco?
- The exact activity: commercial, industrial, craft or service, and does it need a licence or order?
- Expected turnover, and any one client above MAD 80,000?
- Expected expenses, and staff?
- Will liability limits or outside investors matter?
- Capital: cash or in kind, and how much?

## Sources

| Source | Used for | Read |
|---|---|---|
| [Code Général des Impôts 2026, DGI](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) | All CGI rows; articles named on each row; read in full-text search, the articles cited and neighbours | 2026-11-01 |
| [CRI Casablanca-Settat, Démarches de création](https://casainvest.ma/index.php/fr/d%C3%A9marches-de-cr%C3%A9ation) | Legal forms, AE steps, Direct Entreprise | 2026-11-01 |

Pages tried and not opened on 2026-11-01: ae.gov.ma, rn.ae.gov.ma, ompic.ma, directentreprise.ma, cnss.ma (no connection, also in a browser tab); ice.gov.ma (refused).

Not yet confirmed: Law 114-13 text and RNAE documents, fee and timing; automatic CNSS affiliation; Law 47-06 and 07-20 on TP and TSC, including the AE position; Laws 5-96 and 24-10 on SARL capital and blocking; ICE structure and who attributes it (OMPIC for companies, DGI for individuals, recovery at ice.gov.ma); two RC forms (analytique, central) under Law 15-95; name certificate fee; SARL cost, time and step order; which service trades need no RC.

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
