---
name: belgium-financial-statements
description: "Preparing and filing Belgian annual accounts (jaarrekening / comptes annuels) for financial years closing in 2026: the Companies and Associations Code (WVV / CSA) size criteria for micro, small and large companies (EUR 900,000 / 450,000 / 10 and EUR 11,250,000 / 6,000,000 / 50), the full, abbreviated and micro schemes of the Royal Decree of 29 April 2019, approval within six months, filing with the National Bank (NBB) within 30 days of approval and at the latest seven months after year-end, the 2026 NBB filing costs and late-filing surcharges, XBRL or PDF filing, language rules, the social balance sheet, the statutory auditor (commissaris) test, consolidation and groups of limited size, and the sanctions for not filing. Trigger on: jaarrekening, comptes annuels, NBB filing, Balanscentrale, Centrale des bilans, verkort schema, microschema, commissaris Belgium, Belgian GAAP accounts, late filing NBB. Out of scope: bookkeeping and the chart of accounts (belgium-bookkeeping), corporate tax (be-corporate-tax), VAT (be-vat-return)."
version: 1.1
jurisdiction: BE
category: financial-statements
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - financial-statements-workflow-base
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belgium Financial Statements

Rules below apply to annual accounts filed in 2026. Each line names its source; the full list is in Sources at the end. The WVV and the KB WVV were read in the consolidated Justel database, and the NBB pages on nbb.be, on 2026-10-30.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Belgium (Koninkrijk België / Royaume de Belgique) |
| Currency | EUR |
| Filing authority | Nationale Bank van België / Banque Nationale de Belgique (NBB / BNB), Balanscentrale / Centrale des bilans |
| Primary legislation | Wetboek van vennootschappen en verenigingen (WVV) / Code des sociétés et des associations (CSA), Book 3 |
| Supporting legislation | Royal Decree of 29 April 2019 executing the WVV (KB WVV / AR CSA): valuation rules, schemes, filing rules |
| Accounting standards | Belgian accounting law (KB WVV) with the guidance of the Commissie voor Boekhoudkundige Normen (CBN / CNC) |
| Financial year | Normally 12 months; an exceptional year may not exceed 24 months less one day (WVV art. 1:24 § 4) |
| Approval | Accounts put to the shareholders' meeting within 6 months after year-end (WVV art. 3:1 § 1) |
| Filing deadline | Within 30 days after approval and at the latest 7 months after year-end (WVV art. 3:12 § 1) |
| Filing cost 2026 (XBRL) | EUR 67.00 micro, EUR 89.40 abbreviated, EUR 379.50 full (NBB) |
| Late filing surcharge 2026 | From the 9th month after year-end: EUR 151 small / EUR 504 other; 10th to 12th month: EUR 227 / EUR 755; from the 13th month: EUR 453 / EUR 1,510 (NBB; WVV art. 3:13) |
| Digital filing | Electronic only, as an XBRL file (preferred) or a PDF file, through the NBB filing application; paper abolished since 1 January 2020 (NBB) |

## Section 2 -- Reporting Framework

**Reporting framework**

| Entity type | Applicable scheme | Source |
| --- | --- | --- |
| Large companies | Full scheme (volledig schema / schéma complet), KB WVV annex 3 | KB WVV art. 3:80 to 3:82 |
| Small companies | May use the abbreviated scheme (verkort schema / schéma abrégé), annex 4 | WVV art. 3:2; KB WVV art. 3:83 to 3:85 |
| Micro companies | May use the micro scheme (microschema / schéma micro), built on the abbreviated layout | WVV art. 3:3; KB WVV art. 3:86 to 3:88 |
| Groups (consolidated accounts) | A parent that controls one or more subsidiaries prepares consolidated accounts and a consolidated management report, unless exempt | WVV art. 3:23, 3:25, 3:26 |

- Unlisted small companies and micro companies may also publish in the abbreviated or micro form (WVV art. 3:11).
- Belgian accounting law differs from IFRS: for example "non-recurring" items are shown inside operating and financial results, revaluations go to a separate equity heading, and development costs and goodwill are written off over at most 10 years where the life cannot be estimated (KB WVV annex 3; art. 3:35, 3:39). See [belgium-bookkeeping](belgium-bookkeeping.md) for the valuation rules.

## Section 3 -- Size Thresholds

Criteria in force for financial years from 2024 (WVV art. 1:24 and 1:25, amounts set by the Law of 28 March 2024, in force 8 April 2024).

### Small company (art. 1:24)

- **Small company classification.** A company with legal personality is small if, on the balance sheet date of the last closed financial year, it exceeds no more than one of the criteria below (WVV art. 1:24 § 1). A company that exceeds more than one is large.

**Small company limits** (WVV art. 1:24 § 1)

| Criterion | Limit |
| --- | --- |
| Jaarlijkse netto-omzet / Chiffre d'affaires annuel (net turnover excl. VAT) | EUR 11,250,000 |
| Balanstotaal / Total du bilan (balance sheet total) | EUR 6,000,000 |
| Jaargemiddelde werknemers / Moyenne annuelle des travailleurs (FTE) | 50 |

### Micro company (art. 1:25)

- **Micro company classification.** A small company that is neither a parent nor a subsidiary is micro if it exceeds no more than one of the criteria below (WVV art. 1:25 § 1).

**Micro company limits** (WVV art. 1:25 § 1)

| Criterion | Limit |
| --- | --- |
| Net turnover excl. VAT | EUR 900,000 |
| Balance sheet total | EUR 450,000 |
| Average FTE | 10 |

### How the test works

- **Two-year rule.** Exceeding, or no longer exceeding, more than one criterion has effect only when it happens in two consecutive financial years; the change applies from the year after the second year (art. 1:24 § 2, applied to micro companies by art. 1:25 § 2).
- **Starters** estimate the figures in good faith at the start of the first year; if more than one criterion will be exceeded, that counts for the first year at once (art. 1:24 § 3).
- **Short or long year.** Turnover is multiplied by the number of months divided by 12, each started month counting as a full month (art. 1:24 § 4).
- **Staff** is the average of FTE registered in Dimona at the end of each month (art. 1:24 § 5).
- **Linked companies.** For a parent company, turnover and balance sheet total are measured on a consolidated basis and staff numbers are added; if intragroup items are not eliminated, the turnover and balance sheet limits rise by 20% (art. 1:24 § 6, § 7).

### Group of limited size (art. 1:26)

**Group of limited size** (WVV art. 1:26 § 1): exempt from consolidation (art. 3:25) if, on a consolidated basis, it exceeds no more than one of these:

| Criterion | Limit |
| --- | --- |
| Net turnover excl. VAT | EUR 42,500,000 |
| Balance sheet total | EUR 21,250,000 |
| Average FTE | 250 |

## Section 4 -- Required Financial Statements

**Required financial statements**

| Document | Micro | Small (verkort) | Large (volledig) | Source |
| --- | --- | --- | --- | --- |
| Balans (balance sheet) | Micro scheme | Abbreviated | Full | WVV art. 3:1 § 1; KB WVV art. 3:80, 3:83, 3:86 |
| Resultatenrekening (P&L) | Micro scheme | Abbreviated | Full | KB WVV art. 3:81, 3:84, 3:87 |
| Toelichting (notes) | Micro notes | Abbreviated notes | Full notes | KB WVV art. 3:82, 3:85, 3:88 |
| Sociale balans (social balance sheet) | Filed with the accounts | Filed with the accounts | Filed with the accounts | WVV art. 3:12 § 1, 8° |
| Jaarverslag (management report) | Not required if unlisted | Not required if unlisted | Required | WVV art. 3:4, 3:5 |
| Verslag commissaris (auditor's report) | Only if an auditor is appointed | Only if an auditor is appointed | Required | WVV art. 3:12 § 1, 4°; 3:72 |

- The accounts are the balance sheet, the profit and loss account and the notes, forming one whole (WVV art. 3:1 § 1).
- Unlisted small companies that do not file a management report must still give in the notes the justification required by art. 3:6 § 1, first paragraph, 6° (WVV art. 3:4, second paragraph).
- **Other documents filed with the accounts** (WVV art. 3:12 § 1): names of the directors and auditor and of any external accountant who checked or corrected the accounts, or a statement that none did; the appropriation of the result if not in the accounts; the date of filing of the deed or the updated articles; the auditor's report; amounts of debts guaranteed by the State, overdue tax and RSZ / ONSS debts, and public grants; the management report items where required; the list of participations; the social balance sheet; and other documents the code requires.
- The NBB filing form includes the shareholder structure and the reports on conflicts of interest (NBB, "Andere neer te leggen documenten").

## Section 5 -- Year-End Adjustments Checklist

**Year-end adjustments checklist**

| # | Adjustment | Belgian rule | Source |
| --- | --- | --- | --- |
| 1 | Afschrijvingen (depreciation) | Under a plan in the valuation rules; accelerated depreciation allowed under tax rules, with the excess disclosed; extra write-off where book value exceeds value in use | KB WVV art. 3:42 |
| 2 | Voorzieningen voor risico's en kosten (provisions) | For clearly defined losses or costs that are probable or certain at the balance sheet date but of uncertain amount; set up systematically under the valuation rules, not depending on the result | KB WVV art. 3:28, 3:31 |
| 3 | Overlopende rekeningen (accruals and deferrals) | Accounts 490 to 493 | MAR (see belgium-bookkeeping) |
| 4 | Waardeverminderingen op vorderingen (doubtful debts) | Write-downs where payment at maturity is uncertain in whole or in part | KB WVV art. 3:46 |
| 5 | Voorraden (stock) | Cost (specific, weighted average, FIFO or LIFO) or lower market value at the balance sheet date | KB WVV art. 3:21, 3:47 |
| 6 | Bestellingen in uitvoering (contracts in progress) | Percentage of completion where the margin is reasonably certain, or cost until completion | KB WVV art. 3:49 |
| 7 | Uitgestelde belastingen (deferred taxes) | On capital grants and realised gains that are taxed later, valued at the normal tax that would have been due | KB WVV art. 3:54 |
| 8 | Herwaarderingsmeerwaarden (revaluation) | Allowed for tangible and financial fixed assets whose value durably exceeds book value; surplus kept in equity until realised; never used to clear losses carried forward | KB WVV art. 3:35 |
| 9 | Geldbeleggingen (current investments) | Written down where realisable value at year-end is below cost | KB WVV art. 3:52 |
| 10 | Kapitaalsubsidies (capital grants) | Equity account 15, with deferred tax under item 7 | MAR; KB WVV art. 3:54 |
| 11 | Oprichtingskosten (formation expenses) | Written off by at least 20% a year if capitalised | KB WVV art. 3:37 |
| 12 | Goodwill and development costs | At most 10 years where the useful life cannot be estimated; goodwill write-offs never reversed | KB WVV art. 3:39 |

Holiday pay, the year-end bonus and foreign currency translation are on the "Not yet confirmed" line: no rule specific to them was read. The investment deduction is a tax item: see [be-corporate-tax](be-corporate-tax.md).

## Section 6 -- Resultatenrekening Format (P&L)

Belgian full scheme, by nature (KB WVV annex 3, art. 3:81):

```
I.    Bedrijfsopbrengsten (Operating income)
      A. Omzet (Turnover)
      B. Voorraad goederen in bewerking en gereed product en bestellingen in uitvoering:
         toename (afname)
      C. Geproduceerde vaste activa
      D. Andere bedrijfsopbrengsten
      E. Niet-recurrente bedrijfsopbrengsten

II.   Bedrijfskosten (Operating charges)
      A. Handelsgoederen, grond- en hulpstoffen (1. Aankopen 2. Voorraad: afname (toename))
      B. Diensten en diverse goederen
      C. Bezoldigingen, sociale lasten en pensioenen
      D. Afschrijvingen en waardeverminderingen op oprichtingskosten, op immateriële en
         materiële vaste activa
      E. Waardeverminderingen op voorraden, bestellingen in uitvoering en handelsvorderingen
      F. Voorzieningen voor risico's en kosten
      G. Andere bedrijfskosten
      H. Als herstructureringskosten geactiveerde bedrijfskosten (-)
      I. Niet-recurrente bedrijfskosten

III.  Bedrijfswinst / Bedrijfsverlies (Operating profit or loss)

IV.   Financiële opbrengsten (A. uit financiële vaste activa, B. uit vlottende activa,
      C. andere, D. niet-recurrente)
V.    Financiële kosten (A. kosten van schulden, B. waardeverminderingen op vlottende activa,
      C. andere, D. niet-recurrente)

VI.   Winst / Verlies van het boekjaar vóór belasting

VII.  A. Onttrekking aan de uitgestelde belastingen
      B. Overboeking naar de uitgestelde belastingen

VIII. Belastingen op het resultaat (A. Belastingen, B. Regulariseringen)

IX.   Winst / Verlies van het boekjaar

X.    A. Onttrekking aan de belastingvrije reserves
      B. Overboeking naar de belastingvrije reserves

XI.   Te bestemmen winst / verlies van het boekjaar
```

The abbreviated and micro schemes (annex 4) start with I.A.B Brutomarge (gross margin, with non-recurring operating income shown inside it), then C to I, II operating result, III financial income, IV financial charges, V result before tax, VI deferred taxes, VII taxes, VIII result, IX untaxed reserves, X profit to appropriate.

The 2025 version showed headings VI "result from ordinary activities", VII and VIII "exceptional" items and XII to XIV for untaxed reserves. The current annex has no separate exceptional section; non-recurring items sit inside operating and financial results.

## Section 7 -- Balans Format (Balance Sheet)

Belgian full scheme (KB WVV annex 3, art. 3:80):

```
ACTIVA (Assets)

  I.    Oprichtingskosten (Formation expenses)

VASTE ACTIVA (Fixed assets)
  II.   Immateriële vaste activa (Intangible assets)
  III.  Materiële vaste activa (Tangible assets)
        A. Terreinen en gebouwen
        B. Installaties, machines en uitrusting
        C. Meubilair en rollend materieel
        D. Leasing en soortgelijke rechten
        E. Overige materiële vaste activa
        F. Activa in aanbouw en vooruitbetalingen
  IV.   Financiële vaste activa (Financial fixed assets)

VLOTTENDE ACTIVA (Current assets)
  V.    Vorderingen op meer dan een jaar
  VI.   Voorraden en bestellingen in uitvoering
  VII.  Vorderingen op ten hoogste een jaar
  VIII. Geldbeleggingen
  IX.   Liquide middelen
  X.    Overlopende rekeningen

-------------------------------------

PASSIVA (Equity and liabilities)

EIGEN VERMOGEN (Equity)
  I.    Inbreng (NV: A. Kapitaal, B. Buiten kapitaal / BV and others: A. Beschikbaar,
        B. Onbeschikbaar)
  II.   Herwaarderingsmeerwaarden (Revaluation surplus)
  III.  Reserves
  IV.   Overgedragen winst / verlies (Retained earnings)
  V.    Kapitaalsubsidies (Capital grants)
  VI.   Voorschot aan de vennoten op de verdeling van het netto-actief (-)

VOORZIENINGEN EN UITGESTELDE BELASTINGEN (Provisions and deferred taxes)
  VII.  A. Voorzieningen voor risico's en kosten
        B. Uitgestelde belastingen

SCHULDEN (Liabilities)
  VIII. Schulden op meer dan een jaar
  IX.   Schulden op ten hoogste een jaar
  X.    Overlopende rekeningen
```

The 2025 version showed equity as capital and share premium (I, II) and liabilities as IX to XI. Since the WVV, equity heading I is the contribution (inbreng), and liabilities are VIII to X.

## Section 8 -- Toelichting (Notes to Accounts)

**Notes by scheme**

| Scheme | Content | Source |
| --- | --- | --- |
| Full | The items listed in KB WVV art. 3:82 (including fixed asset movements, participations, debts by remaining term, rights and commitments, results breakdown, related parties) | KB WVV art. 3:82 |
| Abbreviated | The items listed in KB WVV art. 3:85 | KB WVV art. 3:85 |
| Micro | I. Statement of fixed assets (cost, revaluations, depreciation and write-downs, uncalled amounts, net book value); II. A. Off-balance sheet rights and commitments (personal and real security given, mortgages, pledges), B. major pending disputes and other major commitments, C. supplementary pension schemes; III. Advances and loans to directors and managers; IV. Number of own shares held | KB WVV art. 3:88 |

- **Small companies** disclose the amount of capitalised development costs in the notes (KB WVV art. 3:38).
- **Accelerated depreciation** above the economic level is disclosed in the notes (KB WVV art. 3:39, 3:42).
- **Stock**: where the book value (for example under LIFO) differs much from market value, the difference is disclosed; small companies may give one total (KB WVV art. 3:21).
- The item-by-item table of the 2025 version (which notes apply to which size) is replaced by the article references above; the detailed lists are on the "Not yet confirmed" line for items not read one by one.

## Section 9 -- Filing Requirements

**Filing requirements**

| Item | Detail | Source |
| --- | --- | --- |
| Filing authority | NBB, Balanscentrale | WVV art. 3:10 |
| Who files | Most Belgian companies, including all with limited liability; VOF / SNC and CommV / SComm only where a partner is a legal person and the company is large, or in other listed cases | NBB, "Belgische vennootschappen" |
| Approval deadline | Within 6 months after year-end; late approval shifts the burden of proof for third-party damage | WVV art. 3:1 § 1 |
| Filing deadline | Within 30 days after approval and at the latest 7 months after year-end | WVV art. 3:12 § 1; NBB, "Wanneer neerleggen" |
| Filing method | Electronic only; paper abolished since 1 January 2020 | NBB, "Welk formaat" |
| Format | XBRL file under the April 2022 taxonomy (about 99% of filings) or PDF; PDF compulsory for credit institutions, investment firms, health insurers and immigrating companies; maximum file size 50 MB | NBB, "Welk formaat" |
| Language | The language (or one of the languages) of the language area of the registered office; one language per filing; an English translation may be filed in addition, never alone | NBB, "Welke taal" (WVV art. 2:33; KB WVV art. 3:67) |
| Filing cost 2026 | See table below | NBB, history of filing costs 2026 |
| Acceptance | Deemed accepted on the filing date unless the NBB objects within 8 working days | WVV art. 3:14 |
| Corrections | A corrected document is filed as a complete corrected set marked "aanpassing", in the same currency and language | KB WVV art. 3:73 |
| Liquidation | A company dissolved during the year files two sets of accounts for that year (former directors and liquidator), unless dissolution and closure fall in the same year | NBB, "Belgische vennootschappen" (WVV art. 2:70, 2:99, 3:10) |
| Public country-by-country report | Where required, filed within 12 months after year-end | WVV art. 3:12/1 |

**NBB filing costs 2026** (NBB, history of filing costs for companies)

| Filing | Full model | Abbreviated model | Micro model |
| --- | --- | --- | --- |
| XBRL | EUR 379.50 | EUR 89.40 | EUR 67.00 |
| PDF | EUR 449.70 | EUR 159.50 | EUR 137.30 |
| Improved (corrected) filing | EUR 86.00 | EUR 86.00 | EUR 54.70 |

The costs are indexed every 1 January to consumer prices (NBB, "Tarieven neerlegging", citing KB WVV art. 3:70).

### Late filing surcharge (tarieftoeslag)

A company that files more than one month after the 7-month deadline pays a contribution to the cost of detecting companies in difficulty, collected by the NBB with the filing cost (WVV art. 3:13). The base amounts in the law (EUR 400 / 600 / 1,200, or EUR 120 / 180 / 360 for small companies filing the abbreviated or micro model) are indexed every 1 January. The 2026 amounts:

**Late filing surcharge, filings from 1 January 2026** (NBB, "Tarieftoeslag en beroepsprocedure")

| Filing made | Small companies filing the abbreviated or micro model | Other companies |
| --- | --- | --- |
| From the 1st day of the 9th month after year-end | EUR 151 | EUR 504 |
| From the 1st day of the 10th month to the 12th month | EUR 227 | EUR 755 |
| From the 1st day of the 13th month | EUR 453 | EUR 1,510 |

The surcharge can be refunded in case of force majeure on request within 18 months after year-end (WVV art. 3:13), and the company can appeal against it (NBB). The 2025 version's table (EUR 120 rising to EUR 1,200, EUR 600 "each subsequent month") was wrong: the surcharge is a single amount fixed by the month of filing, not a monthly charge.

### Worked example: late filing by a small company

A small BV with a 31 December 2025 year-end approves its abbreviated accounts on 25 June 2026 but files the XBRL file only on 15 October 2026. The 7-month deadline was 31 July 2026. The surcharge starts on 1 September 2026 (first day of the 9th month); 15 October falls in the 10th month (October), so the small-company surcharge is EUR 227. The NBB collects EUR 89.40 + EUR 227 = EUR 316.40.

```oa-check
name: Belgium NBB late filing, small company, 10th month, 2026
inputs:
  filing_cost_abbreviated_xbrl: 89.40
  surcharge_small_month_10_to_12: 227
  year_end_month: 12
  filing_month_2026: 10
steps:
  - months_after_year_end: filing_month_2026 + 12 - year_end_month
  - total_paid: filing_cost_abbreviated_xbrl + surcharge_small_month_10_to_12
expected:
  months_after_year_end: 10
  total_paid: 316.40
```

### Other sanctions for not filing

- **Civil sanction.** Damage suffered by third parties is presumed to result from late approval or filing, unless the company proves otherwise (WVV art. 3:1 § 1, 3:12 § 3).
- **Striking off.** The KBO / BCE may strike off a company that has not filed for at least three consecutive financial years; filing the missing accounts reverses it (NBB, citing WER art. III.42 § 1, 4°).
- **Judicial dissolution.** The enterprise court may dissolve a company that has not filed its accounts, at the request of any interested party or the public prosecutor, unless the situation is put right during the proceedings (NBB, citing WVV art. 2:73).

## Section 10 -- Audit Requirements

### Mandatory appointment of a commissaris (statutory auditor)

- **Who needs one.** The audit chapter (WVV art. 3:72 and following) applies to every company except: general and limited partnerships and EEIGs whose unlimited partners are all natural persons; unlisted small companies (art. 1:24), each company judged separately, unless it belongs to a group that must prepare and publish consolidated accounts; and certain recognised agricultural partnerships (WVV art. 3:72). Listed companies, public-interest entities (art. 1:12, 5°) and credit institutions and insurers are always covered (same article, opening words).
- **In practice:** a large company (more than one small criterion exceeded, two years running) must appoint a commissaris.

**Large company test for audit** (WVV art. 1:24 § 1)

| Criterion | Limit (more than one exceeded = large) |
| --- | --- |
| Net turnover excl. VAT | EUR 11,250,000 |
| Balance sheet total | EUR 6,000,000 |
| Average FTE | 50 |

- **Two-year rule.** The size change applies from the year after it happens for the second consecutive year (art. 1:24 § 2).

### Companies with a works council

- In every company that must set up a works council (ondernemingsraad) under the Law of 20 September 1948, one or more bedrijfsrevisoren are appointed for the information tasks towards the works council (WVV art. 3:83). Where no commissaris is appointed, the shareholders' meeting appoints a bedrijfsrevisor for those tasks (art. 3:93). In such a company the auditor can only be dismissed on the proposal or with the agreement of the works council (art. 3:91).

### Auditor qualification

- **Bedrijfsrevisor / réviseur d'entreprises.** The commissaris is appointed by the shareholders' meeting from among the auditors in the public register of bedrijfsrevisoren or registered audit firms (WVV art. 3:58 § 1).

### Audit mandate

- **Term.** A renewable term of three years (WVV art. 3:61 § 1).
- **Dismissal.** During the mandate only for legal reasons, on pain of damages; a disagreement on an accounting treatment or audit procedure is not in itself a legal reason (WVV art. 3:66 § 1).
- **No auditor appointed.** Each shareholder then has the investigation powers of an auditor individually, and may be assisted by a certified accountant (WVV art. 3:101).

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Companies and Associations Code (WVV), art. 1:24 to 1:26, 3:1 to 3:17, 3:23 to 3:26, 3:58 to 3:101 (Justel, consolidated) | https://www.ejustice.just.fgov.be/eli/wet/2019/03/23/2019A40586/justel | 2026-10-30 |
| Royal Decree of 29 April 2019 executing the WVV (valuation rules art. 3:21 to 3:55, schemes art. 3:80 to 3:88, filing art. 3:66 to 3:75, annexes 3 and 4) (Justel, consolidated) | https://www.ejustice.just.fgov.be/eli/besluit/2019/04/29/2019011967/justel | 2026-10-30 |
| NBB, Tarieftoeslag en beroepsprocedure (surcharges from 1 January 2026, sanctions) | https://www.nbb.be/nl/balanscentrale/opmaken-en-neerleggen/hoeveel-betalen/tarieftoeslag-en-beroepsprocedure | 2026-10-30 |
| NBB, Tarieven neerlegging (indexation) | https://www.nbb.be/nl/balanscentrale/opmaken-en-neerleggen/hoeveel-betalen/tarieven-neerlegging | 2026-10-30 |
| NBB, history of filing costs for companies, 2026 (PDF) | https://www.nbb.be/doc/ba/tarif/2026/historiek%20van%20de%20neerleggingskosten%20van%20vennootschappen_2026_nl.pdf | 2026-10-30 |
| NBB, Wanneer neerleggen | https://www.nbb.be/nl/balanscentrale/opmaken-en-neerleggen/wanneer-en-hoe-neerleggen/wanneer-neerleggen | 2026-10-30 |
| NBB, Welk formaat | https://www.nbb.be/nl/balanscentrale/opmaken-en-neerleggen/wanneer-en-hoe-neerleggen/welk-formaat | 2026-10-30 |
| NBB, Welke taal | https://www.nbb.be/nl/balanscentrale/opmaken-en-neerleggen/wanneer-en-hoe-neerleggen/welke-taal | 2026-10-30 |
| NBB, Andere neer te leggen documenten | https://www.nbb.be/nl/balanscentrale/opmaken-en-neerleggen/wat-neerleggen/andere-neer-te-leggen-documenten | 2026-10-30 |
| NBB, Belgische vennootschappen (who files, liquidation) | https://www.nbb.be/nl/balanscentrale/opmaken-en-neerleggen/wie-moet-neerleggen/belgische-vennootschappen | 2026-10-30 |

Not yet confirmed: that listed groups must use IFRS for consolidated accounts and unlisted groups may choose (EU Regulation 1606/2002 and the Belgian consolidation rules were not read); the full item lists of the notes under KB WVV art. 3:82 and 3:85 (only the micro list in art. 3:88 was read in full); provisions for holiday pay and the year-end bonus, and the treatment of foreign-currency items (CBN guidance not read); the works-council threshold of 100 workers (the Law of 20 September 1948 was not read); whether the social balance sheet must be filed by companies with no staff; the 2025 version's statements that a correction can be filed within 2 months and that the accounts may be filed in German in the German-speaking area (the language rule was read only as "the language of the language area").

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
