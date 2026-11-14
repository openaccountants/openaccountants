---
version: 1.1
name: sn-company-formation
description: "Company and business formation in Senegal, tax year 2026. The tax registration steps from the DGID (NINEA, declaration of existence within 20 days, choice of regime, first monthly filings) and the CGU flat contribution for small individual businesses. Company law items (OHADA forms, capital, APIX one-stop shop) are listed as not yet confirmed."
jurisdiction: SN
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: filing-howto
---

# Senegal company formation

## Scope

Tax registration of a new business in Senegal in 2026, for an individual trader or service provider and for a company: getting the NINEA (tax identification number), filing the declaration of existence, choosing the tax regime and starting the monthly filings. It does not cover the company law steps (choice of OHADA form, minimum capital, statutes, the APIX one-stop shop, the trade register): those are not yet confirmed from an official text and are listed under Sources.

## Ask the client first

- Individual business or company, and which company form (SARL, SA, SAS).
- Expected annual turnover TTC (up to XOF 50 million may qualify for the CGU).
- Activity: services, trade or production, or renting property (CGF).
- Date the activity starts or the premises open (starts the 20-day clock).
- Whether staff will be hired (salary withholding, CFCE, social bodies).

## The method, step by step

### Rates, bands and thresholds

| Item | Figure | Tax year | Source |
|---|---|---|---|
| NINEA fee | Free apart from a fiscal stamp of XOF 2,000; issued in about 3 days | 2026 | https://www.dgid.sn/fiches/ninea |
| Declaration of existence | Within 20 days of opening the establishment or starting the business (CGI art. 633) | 2026 | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| CGU eligibility | Individuals with annual turnover TTC up to XOF 50 million | 2026 | https://www.dgid.sn/particuliers |
| CGU, service providers | 5% of turnover, minimum XOF 30,000 (art. 141) | 2026 | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| CGU, traders and producers | 2% of turnover, minimum XOF 25,000 (art. 141) | 2026 | same |
| Annual accounts | Filed with the profit return by 30 April (arts. 30, 31) | 2026 | same |
| VAT | Paid by the 15th of the month after the taxable event (art. 363) | 2026 | same |
| SARL capital | No national minimum: the statutes fix the capital (art. 1) and the nominal value of each share (art. 2), Loi n. 2015-07 of 9 April 2015 (JO n. 6844, 18 April 2015, p. 393), which repeals Loi n. 2014-20 | 2026 | https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Loi-n-2015-07-09-du-avril-2015-reglementation-capital-SARL-JO.pdf |
| Salary withholding | By the 15th of the next month; real simplified and CGU employers quarterly (art. 185) | 2026 | same |

### Steps

1. **Get the NINEA.** File at a DGID office or agency: a handwritten request, a copy of the national ID card (individuals), a XOF 2,000 fiscal stamp, a copy of the trade register certificate, a copy of the lease or title for the business premises, and a copy of the statutes (companies). Apart from the stamp the NINEA is free; it takes about three days.
2. **File the declaration of existence** within 20 days of opening the establishment or starting the business (art. 633), by registered letter in two copies to the head of the competent tax office. It gives the name or company name, address, profession and bank and postal account numbers.
3. **Choose the regime** by turnover: real regime, CGU (individuals up to XOF 50 million turnover TTC) or CGF (landlords). Formalisation can be done online on DGID-digitale (https://dgid-digitale.dgid.sn).
4. **Start the recurring filings**: VAT by the 15th of the next month (art. 363), salary withholding by the 15th (art. 185), annual profit return with the financial statements by 30 April (arts. 30, 31). Online filing runs through SENTAX; see [tax overview](sn-tax-overview.md).

### Boundary and exception table

| Situation | Treatment |
|---|---|
| Individual on the CGU | One flat contribution on the previous year's turnover; instalments of one third in the first 15 days of March and May (art. 144) |
| CGU employer | Salary withholding paid quarterly, by the 15th of January, April, July and October (art. 185) |
| Company | Not eligible for the CGU (individuals only); real regime, IS at 30% with the IMF floor: see [company tax](sn-corporate-income-tax.md) |

## Worked cases

Example 1: an individual provides services with turnover of XOF 400,000. CGU at 5% is 20,000, so the 30,000 minimum applies (art. 141).

```oa-check
name: CGU services at the minimum
inputs:
  turnover: 400000
steps:
  - cgu: max(turnover * 0.05, 30000)
expected:
  cgu: 30000.00
```

Example 2: an individual trader with turnover of XOF 10,000,000. CGU at 2% is 200,000, above the 25,000 minimum (art. 141).

```oa-check
name: CGU trader above the minimum
inputs:
  turnover: 10000000
steps:
  - cgu: max(turnover * 0.02, 25000)
expected:
  cgu: 200000.00
```

## When to refuse or refer

- Choice of company form, statutes and the trade register: refer to a Senegal notary or lawyer; the OHADA and APIX figures are not confirmed here. SARL capital itself is set freely in the statutes (Loi n. 2015-07, row above); pay-up and deposit rules are not covered here.
- Registration with the social bodies (CSS and IPRES): see [social contributions](senegal-social-contributions.md).
- Tax incentives under the investment code or special zones: refer.

## Filing and payment

The NINEA is applied for at the DGID; the declaration of existence goes to the competent tax office; recurring returns go through SENTAX. Payments go to the competent public accountant (Tresor).

## Sources

| Source | URL | Read on |
|---|---|---|
| Code general des impots, edition January 2025 (DGID): read arts. 30, 31, 141, 144, 185, 363 and 633 in the PDF text for the deadlines and CGU rates | https://www.dgid.sn/storage/docs/CGI-2025.pdf | 2026-11-14 |
| DGID, Lois et reglements: read the rates table and the Loi 2025-17 measures | https://www.dgid.sn/loi-reglement | 2026-11-14 |
| Loi n. 2025-19, finance law for 2026 (scan, read by OCR, all 64 pages searched): no CGI amendment found (not reopened) | https://budget.sec.gouv.sn/documents/public_download/69556841-a9d4-4658-8c1e-fe230a2a028a/telechargement | 2026-11-01 |
| DGID calendar of annual filings: read the table of annual filing dates | https://www.dgid.sn/storage/docs/calendrier-declarations-annuelles.pdf | 2026-11-14 |
| DGID SENTAX user guide v1.1, 2026: contents and steps read (not reopened) | https://www.dgid.sn/storage/uploads/guide-utilisateur-espace-connecte-1790609363.pdf | 2026-11-01 |
| DGID communique: SENTAX for CME1, CME2 and CPR from 1 October 2026, full text read (not reopened) | https://www.dgid.sn/storage/uploads/communique-ouverture-de-la-plateforme-sentax-aux-contribuables-du-cme1-cme2-et-du-cpr-1790699194.pdf | 2026-11-01 |
| DGID Entreprises page: read the portal descriptions | https://www.dgid.sn/entreprises | 2026-11-14 |
| DGID NINEA sheet: read the documents to file, the XOF 2,000 stamp, free issue and the three-day delay | https://www.dgid.sn/fiches/ninea | 2026-11-14 |
| Journal officiel n. 6844 (18 April 2015), Loi n. 2015-07 on SARL capital: read in full (arts. 1 to 3) | https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Loi-n-2015-07-09-du-avril-2015-reglementation-capital-SARL-JO.pdf | 2026-11-14 |
| DGID Particuliers page: read the three formalisation steps and the CGU and CGF eligibility lines | https://www.dgid.sn/particuliers | 2026-11-14 |

Not yet confirmed: OHADA forms (SARL, SA, SAS), SA capital of XOF 10,000,000, later amendments to Loi n. 2015-07, APIX one-stop steps and timing, and CSS and IPRES employer registration. The old citations were secondary, apix.sn and the social bodies did not open, and the OHADA Uniform Act was not read.
