---
name: greece-vat-return
description: >
  Greek VAT (ΦΠΑ) for 2026 under the VAT Code ratified by ν. 5144/2024, which replaced ν. 2859/2000.
  Covers who is a taxable person, the 24%, 13%, 6% and 4% rates and the 30% island reduction from
  1 January 2026, the EUR 10,000 small business exemption and the EU SME scheme (EUR 100,000 Union
  turnover), monthly and quarterly periodic returns, payment and the two-instalment option, input
  VAT and blocked costs, the reverse charge, intra-EU supplies and acquisitions, recapitulative
  statements, EU distance sales and OSS, refunds to foreign businesses, and the Tax Procedure Code
  fines for late or wrong returns. Trigger on "Greek VAT", "ΦΠΑ", "periodic VAT return Greece",
  "myAADE VAT", "Greek VAT rates 2026", "small business exemption Greece", "reverse charge Greece",
  "Greek island VAT". Out of scope: e-invoicing and myDATA transmission (greece-einvoice), company
  set-up (gr-company-formation), income tax (gr-income-tax), the country overview (gr-tax-overview),
  cross-border income (gr-cross-border). gr-vat-return points here.
version: 2.2
jurisdiction: GR
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Greece VAT (ΦΠΑ), 2026: rates, returns, reverse charge and penalties (v2.1)

Tax year: calendar 2026. Authority: AADE (Ανεξάρτητη Αρχή Δημοσίων Εσόδων). Law: the VAT Code (Κώδικας ΦΠΑ) ratified by ν. 5144/2024 (ΦΕΚ Α' 162/11.10.2024), read here in the Ministry of Finance administrative codification current to ν. 5313/2026 (in force to 18.9.2026). The old code, ν. 2859/2000, is repealed (VAT Code art. 71(5)); a reference to it in another law now means the matching article of the new code (art. 71(1)). Fines and interest are in the Tax Procedure Code, ν. 5104/2024 ("TPC"). Article numbers below are VAT Code articles unless marked TPC. Sub-points keep the Greek letters of the law (α, β, γ, δ, ε, στ, ζ, η, θ).

Load this skill with eu-vat-directive (EU rules) and vat-workflow-base (the return workflow).

## Who this applies to

- **Taxable persons.** Anyone who carries on an economic activity independently, wherever established, is a taxable person (arts. 3 and 4). Tax is charged on supplies of goods and services in Greece for consideration, intra-EU acquisitions and imports (art. 2).
- **Who pays.** Normally the supplier established in Greece (art. 40(1)(α)). The customer pays instead in the reverse-charge cases under "Cross-border points" and for listed domestic supplies such as recyclable scrap (art. 45).
- **Registration.** The VAT number is the ordinary Greek tax number (ΑΦΜ) issued under the TPC (art. 41(2)). For intra-EU services it is used with the prefix EL (art. 41(5)(α), (6)(α)).
- **Out (small businesses).** A business established in Greece can opt for exemption if its Greek turnover in the previous and the current year does not exceed EUR 10,000 (art. 44α(1)). It then charges no VAT, writes "χωρίς φόρο προστιθέμενης αξίας-απαλλαγή μικρών επιχειρήσεων" on its invoices, and cannot deduct input VAT (art. 44α(8)). The exemption is not available to farmers in the special scheme, for new means of transport, or for occasional property supplies (art. 44α(2)). It may leave the exemption voluntarily during the year and rejoin in the next year (art. 44α(4)).
- **EU SME scheme.** From 1 January 2025 a business established in another member state can use the Greek exemption if its Greek turnover is not over EUR 10,000 and its Union turnover is not over EUR 100,000, in the current and previous year, after notifying its home state and getting an "EX" number (art. 44β(1)). It needs no Greek VAT number and files no Greek returns (art. 44ε(1)). A Greek business can use the same scheme in other member states through AADE (arts. 44γ, 44στ).
- **Out (exempt only).** A person making only exempt supplies without deduction files no return (art. 41(3)(β)), except for periods in which it makes intra-EU acquisitions or receives reverse-charge supplies (art. 43(8)).
- **Not covered in this skill.** Farmers' flat-rate scheme (arts. 48-49), travel agents (art. 50), margin schemes (arts. 52-53), investment gold (art. 54), the lump-sum scheme (art. 47), property supplies under art. 8. Refer these.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 24% | 2026 | VAT Code art. 26(1): https://minfin.gov.gr/wp-content/uploads/2026/10/Κοινοποίηση-Διοικητικής-Κωδικοποίησης-του-ν.5144-2024-γι.pdf |
| Reduced rate, goods and services in Annex III | 13% (for example hotel stays, passenger transport, restaurants and cafés except drinks, water supply) | 2026 | art. 26(1) and Annex III: same URL |
| Lower rate where Annex III says so | 6% (for example books, medicines for human use, electricity and natural gas, theatre and cinema tickets) | 2026 | art. 26(1) and Annex III: same URL |
| Lowest rate where Annex III says so | 4% (works to remove architectural barriers for people with disabilities, Annex III B.14) | 2026 | art. 26(1) and Annex III: same URL |
| Island reduction, automatic | Rates cut by 30% on the islands of the North Aegean Region, Samothrace and the Dodecanese with a population of up to 20,000 at the latest census: 24% to 17%, 13% to 9%, 6% to 4%, 4% to 3% | From 1.1.2026 (ν. 5246/2025 arts. 11 and 47(5)) | art. 26(4A), (5), (6): same URL; ν. 5246/2025 (ΦΕΚ Α' 198/11.11.2025): https://www.aade.gr/sites/default/files/2025-11/%CE%91%CE%A0%CE%9F%CE%A3%CE%A0%CE%91%CE%A3%CE%9C%CE%91%20%CE%A6%CE%95%CE%9A%20%CE%91%20198_2025%20%CE%9D%205246_2025.pdf |
| Island reduction, by ministerial decision | Rates cut by 30% on Lesvos, Kos, Samos and Chios while a migrant reception centre operates there. The decision in force is Α.1150/2021 (ΦΕΚ Β' 2828), so the cut applies on these four islands in 2026. Leros was taken out of art. 26(4) from 1.1.2026 and now gets the cut under art. 26(4A) | 2026 | art. 26(4): same URL; AADE circular Ε.2113/2025, point 1: https://www.aade.gr/sites/default/files/2026-01/e2113_2025.pdf |
| Islands that get the reduction | Only those in the annex to AADE circular Ε.2113/2025 (built from ELSTAT census data). Main islands: Agathonisi, Agios Efstratios, Astypalaia, Ikaria, Kalymnos, Karpathos, Kasos, Kos, Leipsoi, Leros, Lesvos, Limnos, Megisti, Nisyros, Oinousses, Patmos, Samothrace, Samos, Symi, Tilos, Fournoi, Chalki, Chios, Psara, plus the islets listed there. Rhodes is not on the list | 2026 | Ε.2113/2025, point 2 and annex: same URL |
| Island reduction does not apply | Tobacco products and means of transport | 2026 | art. 26(4B): same URL |
| Small business exemption, Greek turnover | EUR 10,000 (previous and current year) | From 1.1.2025 | art. 44α(1): same URL |
| EU SME scheme, Union turnover | EUR 100,000 (previous and current year) | From 1.1.2025 | arts. 44β(1), 44δ(2): same URL |
| EU distance sales and e-services threshold | EUR 10,000 a year, all member states together | 2026 | art. 19(1): same URL |
| Net VAT payable carried forward instead of paid | Up to EUR 30 | 2026 | art. 43(6): same URL |
| Two interest-free instalments allowed | Tax due over EUR 100 on a return filed on time | 2026 | art. 43(6): same URL |
| VAT on exempt use deducted in full anyway | Up to EUR 30 a year | 2026 | art. 36(8): same URL |

Rounding on islands: the reduced rate is rounded to the nearest whole number, with 0.5 rounded up (art. 26(6)). So 6% x 0.7 = 4.2% gives 4%, and 4% x 0.7 = 2.8% gives 3%. The reduction covers goods that, when the tax becomes chargeable, (βα) are on those islands and are supplied by a taxable person established there, (ββ) are sold from anywhere in Greece to a taxable person or a non-taxable legal person established there, (βγ) are acquired from another member state by such a person established there, or (βδ) are imported into those islands (art. 26(4)(β), applied to the art. 26(4A) islands by art. 26(4A)). It also covers services physically performed there by a business established there (art. 26(5)). A permanent island branch counts as being established there. A mainland seller delivering to a private consumer on an island charges the normal rate (Ε.2113/2025, point 5, examples 2 and 6).

## The taxable base

- **Base.** The consideration, without the VAT itself (art. 24). The rate is the one in force when the tax becomes chargeable (art. 26(2)).
- **Input VAT.** Deductible on costs used for taxable supplies and for exempt supplies with credit, such as exports and intra-EU supplies (art. 35). The business must have registered its start of activity and hold a valid invoice (art. 37(1)).
- **Blocked costs (art. 35(4)).** No deduction for: tobacco; alcohol not bought for taxable resale; receptions, entertainment and hospitality; housing, food, drink, travel and entertainment for staff or representatives; private passenger cars up to 9 seats, motorcycles, private leisure boats and aircraft, and their fuel, repair, maintenance, hire and running costs. The car block does not apply to vehicles held for sale, hire or paid passenger transport.
- **Partial exemption (art. 36).** Common input VAT is deducted at the ratio of taxable (with credit) turnover to total turnover. Subsidies not in the taxable base go in the denominator. The percentage is rounded up to the next whole number (art. 36(2)). Sales of fixed assets and incidental property and financial transactions are left out (art. 36(3)). The ratio for the year is used for the final figure for that year and provisionally for the next year's returns (art. 36(4)).
- **Capital goods.** Deductions on capital goods are adjusted under art. 38.
- **Leaving or joining the exemption (art. 44α(5)-(7)).** On moving into the normal regime, VAT on stock held the day before is deducted; on moving into the exemption, VAT deducted on stock is repaid. Capital goods still inside the adjustment period are adjusted too. A stock declaration is filed within 2 months of the change. The deduction is claimed on the return for the period in which the stock declaration is filed.

## Deadlines and filing

- **Tax period (art. 43(1)).** One calendar month for a business on double-entry books. One calendar quarter for a business on single-entry books. AADE may set a different period, not shorter than 1 month or longer than 1 year (art. 43(12)(α)).
- **Return deadline (art. 43(4)).** The last working day for public services of the month after the period ends. A return is filed for every period, including nil periods, unless the business has declared it is dormant or suspended (art. 43(3)).
- **Payment (art. 43(6)).** Net VAT over EUR 30 is paid by the same day as the return is due. Up to EUR 30 is carried to the next period. A negative balance is carried forward or refunded under art. 39.
- **Two instalments (art. 43(6)).** If the tax due is over EUR 100 and the return is on time, the business may pay in two equal interest-free instalments; the second is due by the last working day of the month after the return is filed.
- **2026 return dates (computed from art. 43(4)).** June 2026 return: Friday 31 July 2026. Q3 2026 return: Friday 30 October 2026 (31 October is a Saturday). December 2026 and Q4 2026 returns: Friday 29 January 2027 (31 January is a Sunday). Check AADE for any extension (art. 43(12)(β)).
- **No annual VAT return.** Art. 43 provides only periodic returns, plus a six-monthly return for the lump-sum scheme (art. 43(2)).
- **Recapitulative statements (art. 41(4)-(7)).** Filed for intra-EU supplies of goods, intra-EU acquisitions, B2B services supplied to EU customers under the general rule, and B2B services received from EU suppliers. Each transaction goes into the period in which the tax becomes chargeable. Intrastat is filed monthly (art. 41(4)(γ)).
- **Invoices and books.** Books and invoices follow the Greek Accounting Standards, ν. 4308/2014 (art. 41(3)(α)). Their data is sent electronically to AADE's myDATA platform under TPC art. 16. From 2 March 2026 (businesses with 2023 gross revenue over EUR 1,000,000) and 2 November 2026 (all others), domestic B2B, non-EU B2B and B2G invoices must be issued electronically. See greece-einvoice for the dates, channels and myDATA fines.
- **Where.** Returns and payments go through AADE's online services (myAADE / TAXISnet).

## Penalties and interest

All from the TPC (ν. 5104/2024, AADE codification Ε.2109/2025, current to ν. 5259/2025), with art. 53 as amended by ν. 5301/2026 art. 37 (ΦΕΚ Α' 74/15.05.2026, applying to breaches from 19.4.2024). The TPC still names articles of the old VAT Code; art. 71(1) of the new code maps them to the new articles.

- **Late or missing VAT return with tax due.** EUR 250 per breach on single-entry books, EUR 500 on double-entry books (TPC art. 53(2), as amended by ν. 5301/2026).
- **Late or missing VAT return with no tax due.** EUR 100 per breach (TPC art. 53(1A), added by ν. 5301/2026).
- **Return never filed where tax would be due.** 50% of the tax on the missing return (TPC art. 53(6)).
- **Late amended VAT return.** No fixed fine under art. 53(1) or (2) if the original return was filed on time (TPC art. 53(7)(α)). Interest still runs.
- **Inaccurate VAT return.** 50% of the difference between the tax declared and the tax AADE assesses (TPC art. 54(2)).
- **Trading without registering the start of activity.** 50% of the VAT that should have been paid for the whole period of activity (TPC art. 53(10)).
- **Late payment interest.** Runs from the day after the payment deadline. For a late or amended return, it runs from the date the tax should first have been paid. No interest on interest (TPC art. 52(1), (5)). The rate is not in the TPC; see "Not yet confirmed".
- **Not issuing an e-invoice where one is required.** Treated as not issuing the invoice (AADE press release 17.2.2026, citing circular Ε.2004/2026). With VAT: 50% of the VAT on it, at least EUR 250 (single-entry) or EUR 500 (double-entry) per audit; 100% on a repeat (TPC art. 57(6)). Without VAT: EUR 500 (single-entry) or EUR 1,000 (double-entry) per audit (TPC art. 57(5)). See greece-einvoice.

## Cross-border points

- **B2B services received from abroad.** Where the place of supply is Greece under the general rule (art. 18(2)(α)) and the supplier is not established in Greece, the Greek business customer pays the VAT (art. 40(1)(στ)). It declares output VAT and, if it has full deduction, the same amount as input VAT. It files a recapitulative statement for services from EU suppliers (art. 41(6)).
- **Goods from non-established suppliers.** The Greek taxable customer pays the VAT on triangular onward supplies (art. 40(1)(ε)(εα)) and on supplies located in Greece under art. 17(3) (art. 40(1)(ε)(εβ)).
- **Intra-EU acquisitions.** Taxed in Greece; the acquirer pays (arts. 14 and 40(1)(θ)). Same self-assessment as above.
- **Intra-EU supplies of goods.** Exempt with credit under the conditions of art. 33. They are listed on the recapitulative statement and the customer's VAT number goes on the invoice (art. 41(4)).
- **B2B services supplied to EU customers.** Place of supply is the customer's state under art. 18(2)(α); invoice without Greek VAT and list on the recapitulative statement (art. 41(5)).
- **Exports.** Exempt with credit (art. 29).
- **Distance sales and e-services to EU consumers.** Greek VAT applies only while the year's total of such sales stays at or below EUR 10,000 and did not exceed it last year (art. 19(1)). Above that, the customer's state's VAT applies, declared through the OSS schemes (arts. 56-58).
- **Non-established businesses.** A business established outside the EU that is liable for Greek VAT must appoint a fiscal representative before its first taxable supply (art. 41(3)(δ)). An EU business without a Greek establishment may appoint one (art. 41(3)(ε)).
- **Refunds to foreign businesses (art. 39(2)-(8)).** An EU business with no Greek establishment and no Greek supplies (other than listed exceptions) claims Greek VAT back through its home state's electronic portal, for a period of 3 months to 1 calendar year (art. 39(5), (6)). A non-EU business can claim only if its country gives Greek businesses the same right (art. 39(8)).
- **Imports.** VAT is collected by customs; the rate is the domestic rate for the same goods (arts. 26(3), 67).

## Worked examples

### Example 1: Athens company, monthly return for June 2026

An ΙΚΕ in Athens keeps double-entry books, so it files monthly. In June 2026 it sells goods for EUR 40,000 at 24% and food products for EUR 10,000 at 13%. It buys goods for EUR 5,000 from a German supplier who invoices it without VAT (an intra-EU acquisition). Its Greek purchase invoices carry EUR 6,000 of VAT, all on costs for taxable sales. It also paid EUR 300 of VAT on a client dinner.

Output VAT: 40,000 x 24% = 9,600 and 10,000 x 13% = 1,300. The acquisition is self-assessed at 24%: 5,000 x 24% = 1,200 output and 1,200 input. The dinner VAT is blocked (art. 35(4)(γ)) and is left out. Total output is 12,100; deductible input is 6,000 + 1,200 = 7,200; net payable is 4,900. The return and payment are due by Friday 31 July 2026. Because the tax is over EUR 100 and the return is on time, the company may pay 2,450 by 31 July and 2,450 by Monday 31 August 2026. The acquisition also goes on the recapitulative statement and on Intrastat.

```oa-check
name: Athens company, June 2026 monthly VAT return
inputs:
  sales_24: 40000
  sales_13: 10000
  eu_acquisition: 5000
  domestic_input_vat: 6000
steps:
  - output_24: pct(sales_24, 24)
  - output_13: pct(sales_13, 13)
  - acquisition_vat: pct(eu_acquisition, 24)
  - total_output: output_24 + output_13 + acquisition_vat
  - total_input: domestic_input_vat + acquisition_vat
  - net_payable: total_output - total_input
  - each_instalment: net_payable / 2
expected:
  output_24: 9600
  output_13: 1300
  acquisition_vat: 1200
  total_output: 12100
  total_input: 7200
  net_payable: 4900
  each_instalment: 2450
```

### Example 2: sole trader crosses the EUR 10,000 small business limit in September 2026

A graphic designer in Thessaloniki keeps single-entry books and uses the small business exemption. Her 2025 turnover was EUR 8,000. From 1 January to 19 September 2026 she invoices EUR 9,400. On 20 September 2026 she issues an invoice for EUR 1,500. In Q4 2026 she invoices a further EUR 3,000 and pays EUR 150 of input VAT on supplies. On the day before she left the exemption she held stock on which she had paid EUR 480 of VAT; she files the stock declaration in November 2026.

The 20 September invoice takes her to 9,400 + 1,500 = 10,900, which is 900 over the limit. Under art. 44α(3) she enters the normal regime from that invoice, for its whole value, so it carries 1,500 x 24% = 360 of VAT. Her Q3 return shows 360 payable, due by Friday 30 October 2026. In Q4, output is 3,000 x 24% = 720. The stock VAT of 480 is deducted on the return for the quarter in which she filed the stock declaration (art. 44α(7)), so Q4 deducts 480 + 150 = 630, leaving 90 payable by Friday 29 January 2027. Because she exceeded EUR 10,000 in 2026, she cannot use the exemption in 2027 (art. 44δ(1)).

```oa-check
name: Sole trader leaves the small business exemption (2026)
inputs:
  sales_to_19_sep: 9400
  crossing_invoice: 1500
  q4_sales: 3000
  threshold: 10000
  stock_vat: 480
  q4_input_vat: 150
steps:
  - turnover_after_crossing: sales_to_19_sep + crossing_invoice
  - excess_over_limit: turnover_after_crossing - threshold
  - q3_output: pct(crossing_invoice, 24)
  - q4_output: pct(q4_sales, 24)
  - q4_deductible: stock_vat + q4_input_vat
  - q4_net_payable: q4_output - q4_deductible
  - turnover_2026: turnover_after_crossing + q4_sales
expected:
  turnover_after_crossing: 10900
  excess_over_limit: 900
  q3_output: 360
  q4_output: 720
  q4_deductible: 630
  q4_net_payable: 90
  turnover_2026: 13900
```

## Ask the client first

1. Double-entry or single-entry books? This sets monthly or quarterly returns (art. 43(1)) and the size of most fines.
2. Where is the business established, and where are the goods or the services physically supplied? An island on the annex to AADE circular Ε.2113/2025 cuts the rate by 30% (art. 26(4), (4A), (5)).
3. Turnover in 2025 and 2026 so far, in Greece and across the EU? This decides the small business exemption and the EU SME scheme (arts. 44α, 44β).
4. Does it buy or sell across borders: EU goods, EU or non-EU services, sales to EU consumers? This brings in the reverse charge, recapitulative statements, Intrastat and OSS.
5. Does it make any exempt supplies, or receive subsidies? This decides partial exemption (art. 36).
6. Which costs are cars, fuel, meals, travel or entertainment? These are blocked (art. 35(4)).

## Sources

| Source | URL | Read on |
|---|---|---|
| VAT Code (ν. 5144/2024), Ministry of Finance administrative codification to ν. 5313/2026, arts. 2-4, 18, 19, 24, 26, 29, 33, 35-41, 43, 44 to 44ζ, 45, 56-58, 67, 71 and Annex III | https://minfin.gov.gr/wp-content/uploads/2026/10/Κοινοποίηση-Διοικητικής-Κωδικοποίησης-του-ν.5144-2024-γι.pdf | 2026-10-23 |
| Ministry of Finance page publishing that codification (12.10.2026) | https://minfin.gov.gr/koinopoiisi-dioikitikis-kodikopoiisis-tou-n-5144-2024-gia-ton-kodika-tou-forou-prostithemenis-axias-symfona-me-tin-par-55-tou-arthr-83-tou-n-5104-2024/ | 2026-10-23 |
| Tax Procedure Code (ν. 5104/2024), AADE codification Ε.2109/2025 (to ν. 5259/2025), arts. 52-54 and 57 | https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf | 2026-10-23 |
| ν. 5246/2025 (ΦΕΚ Α' 198/11.11.2025), art. 11 (amends VAT Code art. 26) and art. 47(5) (in force 1.1.2026), copy hosted by AADE | https://www.aade.gr/sites/default/files/2025-11/%CE%91%CE%A0%CE%9F%CE%A3%CE%A0%CE%91%CE%A3%CE%9C%CE%91%20%CE%A6%CE%95%CE%9A%20%CE%91%20198_2025%20%CE%9D%205246_2025.pdf | 2026-10-23 |
| AADE circular Ε.2113/31.12.2025 on the 30% island reduction (art. 26(4)-(5)), with the annex of islands | https://www.aade.gr/sites/default/files/2026-01/e2113_2025.pdf | 2026-10-23 |
| ν. 5301/2026 (ΦΕΚ Α' 74/15.05.2026), art. 37 (amends TPC art. 53), copy hosted by AADE | https://www.aade.gr/sites/default/files/2026-05/%CE%BD%205301_2026.pdf | 2026-10-23 |
| AADE, decision Α.1128/2025 on mandatory e-invoicing | https://www.aade.gr/egkyklioi-kai-apofaseis/mydata-diataxeis/1128-15-09-2025 | 2026-10-23 |
| AADE, decision Α.1197/2026 (second period moved to 2.11.2026) | https://www.aade.gr/egkyklioi-kai-apofaseis/1197-30-09-2026 | 2026-10-23 |
| AADE press release 17.2.2026 (e-invoicing dates and fines) | https://www.aade.gr/deltia-typoy-anakoinoseis/deltio-typoy-17022026 | 2026-10-23 |

Not yet confirmed: the late payment interest rate (set outside the TPC); the fine for a late OSS return where Greece is the member state of consumption (TPC art. 53(3) was repealed from 19.4.2024 by ν. 5301/2026 art. 37(11), and no replacement was found); any amendment to TPC arts. 52-58 after ν. 5301/2026; the deadline and form for recapitulative statements and the AADE decision on how periodic returns are filed; the domestic refund procedure and timing for a Greek business with a credit balance; the capital goods adjustment periods in art. 38.

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
