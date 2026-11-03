---
name: ma-transfer-pricing
description: >
  Use this skill for Morocco transfer pricing for tax year 2026: related party adjustments under
  Art. 213-II of the Code General des Impots, the master file and local file under Art. 214-III,
  the MAD 50 million thresholds, the 0.5% fine, the country by country report under Art. 154 ter,
  and advance pricing agreements under Art. 234 bis. Covers companies subject to impot sur les
  societes with related parties in or outside Morocco. Trigger on phrases like "prix de transfert
  Maroc", "Morocco transfer pricing", "fichier principal", "fichier local", "declaration pays par
  pays Maroc", "CbCR Morocco", "accord prealable prix de transfert", "liens de dependance",
  "benefices indirectement transferes", "أسعار التحويل المغرب". Replies in the user's language.
version: 0.1
jurisdiction: MA
tax_year: 2026
tier: 2
last_updated: 2026-11-01
category: transfer-pricing
---

# Morocco transfer pricing v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing position or professional obligations. Verify figures against the cited primary sources or with a licensed professional before relying on them.

## Who this applies to

Any company in Morocco with direct or indirect dependency links with companies in or outside Morocco can have profits adjusted (Art. 213-II). The documentation duty covers only transactions with related companies outside Morocco, and only above the thresholds below (Art. 214-III-A). The country by country report covers multinational groups at the level in Art. 154 ter.

## Rates, bands and thresholds

| Item | Amount | Conditions | Tax year | Source |
|---|---|---|---|---|
| Documentation threshold, turnover | MAD 50,000,000 | Turnover made and declared, excl. VAT, equal or above; with transactions with related companies outside Morocco | 2026 | CGI Art. 214-III-A https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Documentation threshold, assets | MAD 50,000,000 | Gross assets on the balance sheet at year end, equal or above. Either test is enough | 2026 | same |
| Time to supply missing documents in an audit | 30 days | From receipt of the request under Art. 219 | 2026 | same |
| Local file, transaction category threshold | MAD 1,000,000 | Category total excl. taxes, equal or above, with no netting of income against charges or of acquisitions against disposals; the Section II details are required per category | 2026 | Decree 2-22-1020 Art. 4-II, annexed to the CGI https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Time to answer a request on foreign operations | 30 days | From receipt of the Art. 219 request; applies to operations with companies outside Morocco, with no turnover or asset test in the text | 2026 | CGI Art. 214-III-B https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Fine for missing documents | 0.5% of the transactions concerned | Minimum MAD 200,000 per year concerned; issued by assessment roll | 2026 | CGI Art. 185-IV https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Country by country report, group threshold | MAD 8,122,500,000 | Consolidated annual turnover excl. VAT in the year before the one reported | 2026 | CGI Art. 154 ter-I-b https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Country by country report, deadline | 12 months | After year end; electronic, on the DGI model | 2026 | CGI Art. 154 ter-I https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Country by country report, fine | MAD 500,000 | After a letter gives 15 days to file or complete | 2026 | CGI Art. 199 bis https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Advance pricing agreement, length | Maximum 4 financial years | Only for transactions with related companies outside Morocco | 2026 | CGI Art. 234 bis https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Advance pricing agreement, request | At least 6 months before the first year opens | Filed at the head office of the tax administration | 2026 | Decree 2-16-571 Art. 1, 3, annexed to the CGI https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |

## The base

**Adjustment.** Profits transferred indirectly, through higher or lower purchase or sale prices or by any other means, are added back to the taxable result and or declared turnover (Art. 213-II). The amount is set by comparison with similar companies, or by direct assessment on information the administration holds. The CGI names these two routes. Neither the CGI nor Decree 2-22-1020 lists OECD methods; the local file must name the most suitable method for each category and explain why prices meet the arm's length principle (Decree Art. 4-II f, l). A foreign company with permanent activity in Morocco can have foreign costs limited where their size is not justified (Art. 213-III). Adjustments follow the procedures in Art. 220 or 221 (Art. 213-IV).

**Documentation.** The file has two parts (Art. 214-III-A): a master file on all related companies' activities, the overall transfer pricing policy and the worldwide split of profits and activities; and a local file on the audited company's transactions with those related companies. It goes to the administration electronically, in a format that can be read and processed, in Arabic, French or English (Decree 2-22-1020 Art. 5, 6, published in the Bulletin Officiel of 5 February 2026).

- Master file, five parts in this order (Decree Art. 3): organisational structure; business lines; intangibles; intra-group financing; financial and tax position.
- Local file, three parts in this order (Decree Art. 4): the Moroccan company; controlled transactions; financial information. The controlled transactions part covers each category of MAD 1 million or more: description, amounts by tax jurisdiction, counterparties, key agreements, comparability and functional analysis, method, tested party, assumptions, comparables, adjustments and the arm's length conclusion.

**When.** The documentation is due at the start of the audit: it must be available on the date the accounting audit begins (Art. 210). A related company with no file on that date gets the Art. 219 request and 30 days, then the fine (Art. 185-IV, 214-III-A). For operations with companies outside Morocco, the administration can also ask, under Art. 219, for the nature of the relationship, the services or products, the pricing method and its support, and the foreign company's tax regime and rates; the company has 30 days (Art. 214-III-B). If the documents under A or B are not supplied in time, or are incomplete, insufficient or wrong, the dependency link is presumed established (Art. 214-III-C). It can also request information from tax authorities of states with an exchange agreement (Art. 214-II).

**Country by country report: who files** (Art. 154 ter). A Moroccan company subject to IS files if it (a) holds stakes abroad that require consolidated accounts, or would if its shares were listed in Morocco; (b) meets the turnover threshold; and (c) has no parent in or outside Morocco. A Moroccan subsidiary files in place of a foreign parent if the parent's state does not require the report and the parent would have to file if it were in Morocco, or if that state has no exchange agreement with Morocco, or if the group designates it and it has told the administration (II). It also files when the administration tells it that the parent state has failed on exchange (III). Where several Moroccan group companies are caught under II or III, the group designates one, which tells the administration first (IV).

**Advance agreement** (Art. 234 bis, 234 ter). The administration cannot challenge an agreed method. The agreement is void from its start date if facts were misstated, information hidden, errors or omissions are the company's, the method or duties are not kept, or fraud is used. The administration can use those grounds only through the Art. 220 or 221 procedures. The agreement covers the method and its support (Decree 2-16-571 Art. 1). A preliminary meeting is optional (Art. 2). The request names the associated companies, the operations, the period and the proposed method (Art. 4), with the documents in Art. 5, including certified financial and tax documents for the last four years. A monitoring report is filed each year (Art. 7).

**Prior consultation** (Art. 234 quater). Operations between related companies in Morocco can go to prior tax consultation. Operations with companies outside Morocco cannot.

**Abuse of law** (Art. 213-V). Fictitious operations, or those aimed only at tax benefits against the law's purpose, or at avoiding or reducing tax, can be set aside.

## Deadlines and filing

| Duty | When | Source |
|---|---|---|
| Master and local file | Available on the first day of the audit; missing items within 30 days of the Art. 219 request | CGI Art. 210, 214-III-A |
| Country by country report | Within 12 months of year end, electronically | CGI Art. 154 ter |
| Advance agreement | Request at least 6 months before the first year opens; monitoring report every year | CGI Art. 234 bis; Decree 2-16-571 Art. 3, 7 |

Keep accounting documents for 10 years (Art. 211; Art. 185 bis sets a MAD 50,000 fine per year for not doing so).

## Penalties and interest

Missing file: 0.5% of the transactions covered by the documents not produced, minimum MAD 200,000 per year (Art. 185-IV). Missing or incomplete country by country report: MAD 500,000 (Art. 199 bis). Late, incomplete, insufficient or wrong documents also bring the presumed dependency link (Art. 214-III-C). Tax on an adjustment bears the general surcharges and interest in [company tax](morocco-corporate-income-tax.md).

## Cross-border points

Withholding on payments to non-residents, including related ones, is in [cross-border](ma-cross-border.md). Treaty relief on a Moroccan adjustment is not covered here: see Not yet confirmed.

## Two worked examples that recompute

**Example 1: the minimum fine decides.** A company with turnover of MAD 80 million buys MAD 30 million from its French parent and produces no file after the 30 days. 0.5% gives MAD 150,000, below the minimum, so the fine is MAD 200,000 for that year. With MAD 60 million of purchases the fine would be MAD 300,000.

```oa-check
name: Art. 185-IV fine on MAD 30 million
inputs:
  transactions: 30000000
steps:
  - percent: transactions * 0.005
  - fine: max(percent, 200000)
expected:
  percent: 150000.00
  fine: 200000.00
```

**Example 2: should the company document at all?** Turnover is MAD 40 million but gross assets are MAD 55 million, with related purchases abroad of MAD 12 million. Turnover misses the test; assets pass it, so the file is required. An adjustment of MAD 2 million to the price at the 20% normal rate adds MAD 400,000 of tax before surcharges, and the missing file costs MAD 200,000 more (0.5% of 12 million is 60,000, below the minimum). Assume a year opened in 2026 and net profit below MAD 100 million, so the 20% rate applies (Art. 19-I, 247-XXXVII-A; [company tax](morocco-corporate-income-tax.md)).

```oa-check
name: Adjustment tax and missing-file fine
inputs:
  adjustment: 2000000
  transactions: 12000000
steps:
  - tax: adjustment * 0.20
  - fine: max(transactions * 0.005, 200000)
  - cost: tax + fine
expected:
  tax: 400000.00
  fine: 200000.00
  cost: 600000.00
```

## Ask the client first

1. Turnover excl. VAT and gross assets at year end.
2. Which related companies, in which countries, and direct or indirect links.
3. Value of each transaction type with related companies outside Morocco.
4. Is an audit notified, and has an Art. 219 request arrived?
5. Group consolidated turnover, who the ultimate parent is, and whether its state requires the report.
6. Is an advance agreement in place or wanted?

## Sources

| Source | URL | Read on |
|---|---|---|
| DGI, Code General des Impots 2026 (French); Art. 19-I, 154 ter, 185-IV, 185 bis, 199 bis, 210, 211, 213, 214, 219, 234 bis, 234 ter, 234 quater, 247-XXXVII-A and annexed Decrees 2-16-571 and 2-22-1020 read from the PDF | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 | 2026-11-01 |

Not yet confirmed: the first year or audit Decree 2-22-1020 applies to, as the decree states no start date beyond publication; the meaning of "liens de dependance", as the articles and decrees read give no percentage; pricing methods the DGI accepts in practice; the portal and form for the country by country report and for sending the file; treaty mutual agreement and corresponding adjustments.

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
