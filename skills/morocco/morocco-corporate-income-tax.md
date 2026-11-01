---
name: morocco-corporate-income-tax
description: >
  Use this skill whenever asked about Morocco company tax (impot sur les societes, IS) for tax year
  2026: who pays, the 20%, 35% and 40% rates for years opened from 1 January 2026, the MAD 100
  million test, the tax result, the cotisation minimale, four instalments, the three-month return,
  penalties and non-resident companies. Trigger on phrases like "impot sur les societes Maroc",
  "IS Maroc", "Morocco corporate tax", "acomptes provisionnels", "cotisation minimale societe".
  Replies in the user's language.
version: 1.0
jurisdiction: MA
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Morocco: company tax (IS), 2026

Built by Michael Cutajar and the OpenAccountants team. Articles are from the Code General des Impots 2026 (CGI).

> **General reference only.** This does not constitute tax, legal or financial advice. Verify figures against the cited sources or with a licensed professional before relying on them.

## Who this applies to

Companies of any form and purpose, except those in Art. 3, and public bodies and other legal persons carrying on profit-making operations (Art. 2-I). Companies are taxed on income tied to property, activity and profit-making operations in Morocco, even occasional, and on income a tax treaty gives Morocco to tax (Art. 5-I). Exemptions in Art. 6 are not covered here; refer them. Individuals: see `morocco-professional-income-tax`.

## Rates, bands and thresholds

| Item | Amount | Conditions | Tax year | Source |
|---|---|---|---|---|
| Normal rate | 20% | Years opened from 1 January 2026; end of the 2023 to 2026 transition | 2026 | CGI Art. 19-I-A, 247-XXXVII-A https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Higher rate | 35% | Net profit of MAD 100,000,000 or more. Excludes CFC service companies, industrial acceleration zone companies, and post-2023 companies with a State investment agreement of MAD 1.5 billion over five years | 2026 | CGI Art. 19-I-B https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Return to 20% | Three consecutive years below MAD 100,000,000 | Not where the MAD 100 million was reached through Art. 9 (I-C-1) non-current income | 2026 | same |
| Banks and insurers | 40% | Credit institutions, Bank Al Maghrib, CDG, insurers and reinsurers. Certain microfinance SAs excluded for five years | 2026 | CGI Art. 19-I-C https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Non-resident contractors, flat tax | 8% of contract value excl. VAT | Option under Art. 16; discharges Art. 4 withholding | 2026 | CGI Art. 19-III-A https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Non-resident gross income withholding | 10% | Art. 15 income excl. VAT | 2026 | CGI Art. 19-IV-B https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Dividends withholding | 10% | Art. 13; subject to Art. 247-XXXVII-C | 2026 | same |
| Fixed-income withholding | 20% | Art. 14 and 14 bis income | 2026 | CGI Art. 19-IV-C https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Withholding on Art. 15 bis and 15 ter payments to IS companies | 5% | Paid by the State, public bodies, banks, insurers, or businesses with MAD 200,000,000 turnover; see Art. 247-XXXXVI | 2026 | CGI Art. 19-IV-A https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Cotisation minimale | 0.25%, or 0.15% on listed sales | Art. 144-I-B base | 2026 | CGI Art. 144-I-D https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Cotisation minimale floor | MAD 3,000 | Even with no turnover | 2026 | same |

## The base

Income over charges of the year, for the taxable activity, under accounting law as adjusted by tax law; stock at the lower of cost and market (Art. 8-I). Non-deductible items and the cash limit are in Art. 11; losses carry to the fourth following year, with the exception in Art. 12. The tax cannot be below the cotisation minimale (Art. 144-I-A). New companies are exempt for the first 36 months of operation, ending at the latest 60 months after incorporation; concession companies are excluded (Art. 144-I-C-1).

## Deadlines and filing

1. Four instalments, each 25% of the last closed year's tax, before the end of the 3rd, 6th, 9th and 12th months from the year's opening (Art. 170-I).
2. If only the floor is due, pay it once, before the end of the 3rd month (Art. 170-I).
3. A company expecting that paid instalments cover the tax may stop, by signed declaration 15 days before the next due date. If the final tax exceeds instalments by more than 10%, Art. 208 applies to the skipped amounts (Art. 170-IV).
4. File the tax result return within three months of year end, including exempt companies, with payment references, annexes and the sales statement by client (Art. 20-I).
5. Settle any balance within the same period (Art. 170-IV).

## Penalties and interest

Late or missing return (Art. 184): 5% within 30 days, 15% after, 20% on assessment. Late payment (Art. 208-I): 10% penalty, 5% if paid within 30 days, plus 5% for the first month and 0.50% for each further month or part. The 20% penalty applies to withheld tax under Art. 156 to 160 ter.

## Cross-border points

Non-resident companies are also taxed on Art. 15 gross income for work or services for their Moroccan branches or independent persons in Morocco (Art. 5-II). Treaties and transfer pricing are not covered here.

## Two worked examples that recompute

**1. Profit MAD 5,000,000, turnover MAD 40,000,000.** Tax at 20% is 1,000,000; cotisation 100,000 is lower. Next year's instalments are 250,000 each.

```oa-check
name: Ordinary company 2026
inputs:
  profit: 5000000
  turnover: 40000000
steps:
  - tax: profit * 0.20
  - cm: max(turnover * 0.0025, 3000)
  - due: max(tax, cm)
  - instalment: due * 0.25
expected:
  due: 1000000.00
  instalment: 250000.00
```

**2. Decision: does a dip below MAD 100 million restore 20%? Profit was 120 million, now 90 million.** First year below: 35% applies, 31,500,000, because 20% needs three consecutive years below. At 20% it would be 18,000,000: a difference of 13,500,000.

```oa-check
name: Three year test
inputs:
  profit: 90000000
steps:
  - at_35: profit * 0.35
  - at_20: profit * 0.20
  - difference: at_35 - at_20
expected:
  at_35: 31500000.00
  difference: 13500000.00
```

## Ask the client first

1. Legal form and sector: bank or insurer?
2. Year end and date operations started and date of incorporation.
3. Net profit this year and the last three years; any non-current gains?
4. Turnover and Art. 144 base; any listed 0.15% sales?
5. Any Art. 6 status or State investment agreement?
6. Instalments paid; withholding suffered.
7. Non-resident payments or shareholders?

## Sources

| Source | URL | Read on |
|---|---|---|
| DGI, Code General des Impots 2026 (French); Art. 2, 5, 8, 19, 20, 144, 170, 184, 208, 247-XXXVII-A extracts read from the PDF | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 | 2026-11-01 |

Not yet confirmed: Art. 6 exemptions; Art. 247-XXXVII-C dividend transition and Art. 247-XXXXVI text; SIMPL-IS portal steps and form number; treaty rates.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network : accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
