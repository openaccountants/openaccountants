---
name: ma-cross-border
description: >
  Use this skill for Morocco cross-border tax for tax year 2026: withholding on payments to
  non-residents under Art. 15, dividends, the Art. 16 flat tax for foreign contractors,
  territoriality under Art. 5, branches, foreign tax credits under Art. 19 bis and 77, who pays
  and when. Covers Moroccan payers and non-resident companies. Trigger on phrases like "retenue a
  la source non resident Maroc", "Morocco withholding tax", "produits bruts article 15", "royalties
  Morocco", "societe non residente", "imposition forfaitaire 8%", "convention fiscale Maroc",
  "credit d'impot etranger", "الاقتطاع من المنبع المغرب". Replies in the user's language.
version: 0.1
jurisdiction: MA
tax_year: 2026
tier: 2
last_updated: 2026-11-01
category: cross-border
---

# Morocco cross-border tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing position or professional obligations. Verify figures against the cited primary sources or with a licensed professional before relying on them.

## Who this applies to

Moroccan businesses paying non-residents, non-resident companies with Moroccan income, and Moroccan companies or individuals with foreign tax to credit. Companies are taxed on income from property held, activity carried on and profit operations done in Morocco, even occasional, and on income a treaty gives Morocco to tax, wherever the seat is (Art. 5-I).

## Rates, bands and thresholds

| Item | Amount | Conditions | Tax year | Source |
|---|---|---|---|---|
| Withholding on Art. 15 gross income | 10% | Gross, excl. VAT, paid to non-resident persons or companies | 2026 | CGI Art. 19-IV-B https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Dividends | 11.25% | Amounts distributed from 1 January 2026; 10% from 1 January 2027 | 2026 | CGI Art. 19-IV-B, 247-XXXVII-C https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Foreign contractor flat tax | 8% of the contract excl. VAT | Option by a non-resident company awarded works, construction or assembly contracts | 2026 | CGI Art. 16, 19-III-A https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |

## The base

**Art. 15 list.** Withholding applies to amounts paid, made available or credited to non-residents for: copyright royalties, including film and television (I); patent, design, plan, formula, secret process and trademark licences (II); scientific, technical or other information and studies, in or outside Morocco (III); technical assistance and personnel provided to businesses in Morocco (IV); artistic or sporting activities (V); rental of any equipment (VI); interest and other fixed-income investments, except those in Art. 6-I-C-3 and Art. 45 (VII); road transport from Morocco abroad, for the part of the price for the trip in Morocco (VIII); commissions and fees (IX); and services of any kind used in Morocco or supplied by non-residents (X).

**Who withholds.** Any taxpayer paying or involved in paying (Art. 160-I). If one non-resident is paid by another, the client in Morocco owes the tax (Art. 160-II).

**Branches.** Art. 5-II does not apply where a Moroccan branch does the work without the foreign head office intervening; that income falls in the branch result, taxed like a Moroccan company. Work the head office does for its own branch is caught by the withholding.

**Art. 16 flat tax.** The option is made with the Art. 148-III declaration or after each contract is signed. For a turnkey contract the base includes materials and equipment, whoever supplies them, however billed. The company pays within the month after each receipt (Art. 170-VI).

**Non-resident capital gains.** Non-resident companies are exempt on gains on securities listed on the Casablanca exchange, except shares in real-estate-rich companies under Art. 61-II (Art. 6-I, point 10). Tax on gains on real estate and securities realised in Morocco is paid with the Art. 20-III return (Art. 170-VIII).

**Foreign tax credit.** Companies credit foreign tax on foreign income taxed in a treaty country, if paid and proved, up to the share of Moroccan tax on that income (Art. 19 bis). Individuals have the same limit under Art. 77. A treaty tax-sparing exemption counts as payment, with a certificate from the foreign authority. Without a treaty, Art. 19 bis gives no credit.

## Deadlines and filing

| Duty | When | Source |
|---|---|---|
| Art. 15 withholding | In the month after the payment, to the tax receiver for the payer's seat | CGI Art. 174-III |
| Art. 16 flat tax | Within the month after each receipt | CGI Art. 170-VI |

## Penalties and interest

Anyone who has not paid over the sums they are liable for on time owes them personally, whether or not withheld, plus the Art. 208 penalty and surcharges (Art. 198). The figures sit in [company tax](morocco-corporate-income-tax.md).

## Cross-border points

Treaties can reduce these rates, and treaty rates are not in this skill: read the treaty. VAT on services from non-residents is in [VAT](morocco-vat.md). Related party pricing is in [transfer pricing](ma-transfer-pricing.md).

## Two worked examples that recompute

**Example 1: royalty.** A Casablanca company pays a non-treaty licensor a trademark royalty of MAD 1,000,000 excl. VAT. Art. 15-II applies. Withhold MAD 100,000 and pay it in the following month; the licensor gets MAD 900,000.

```oa-check
name: Art. 15 royalty withholding
inputs:
  royalty: 1000000
steps:
  - tax: royalty * 0.10
  - net: royalty - tax
expected:
  tax: 100000.00
  net: 900000.00
```

**Example 2: should a foreign contractor opt for the flat tax?** The contract is MAD 10,000,000 excl. VAT. The flat tax is MAD 800,000. Normal tax at 20% costs the same on profit of MAD 4,000,000, a 40% margin. Below that margin the normal regime is cheaper; above it, the option is. Assume the 20% rate and no other Moroccan income.

```oa-check
name: Art. 16 option break-even
inputs:
  contract: 10000000
steps:
  - flat: contract * 0.08
  - breakeven_profit: flat / 0.20
  - margin: breakeven_profit / contract
expected:
  flat: 800000.00
  breakeven_profit: 4000000.00
  margin: 0.40
```

## Ask the client first

1. Is the payer in Morocco, and is the payee resident, and where?
2. What exactly is paid for, so which Art. 15 line?
3. Is there a treaty, and has the payee shown residence?
4. Is there a Moroccan branch, and did the head office intervene?
5. For contractors: contract value, type, expected margin.
6. Date of the payment or distribution.

## Sources

| Source | URL | Read on |
|---|---|---|
| DGI, Code General des Impots 2026 (French); Art. 4, 5, 6-I (point 10), 13, 15, 16, 19, 19 bis, 77, 160, 170-VI, 170-VIII, 174-III, 198, 247-XXXVII-C read from the PDF | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 | 2026-11-01 |

Not yet confirmed: treaty list and treaty rates; proof of residence needed for treaty rates; IR rate for non-resident individuals (Art. 73 not read for this); Art. 20-III return mechanics; form numbers and the SIMPL portal path for the withholding; dividend exemptions in Art. 6-I-C.

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
