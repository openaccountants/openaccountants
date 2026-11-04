---
name: de-einkommensteuer-freelancer
description: "German income tax (Einkommensteuer) on the profit of one self-employed person resident in Germany, tax year 2026. Covers Freiberufler (§ 18 EStG) versus trade (§ 15 EStG), the cash-basis profit (EÜR, § 4(3)) with Anlage EÜR and Anlage S or G, business expenses including the home office flat rate and the EUR 6 day rate, low-value assets and depreciation (§§ 6, 7), the Investitionsabzugsbetrag (§ 7g), the 2026 tariff with the EUR 12,348 Grundfreibetrag (§ 32a), splitting, the solidarity surcharge, church tax, pension and health special expenses, losses (§ 10d), prepayments (§ 37), the § 35 trade tax credit, filing deadlines with and without a Steuerberater (§ 149 AO) and the late-filing surcharge (§ 152 AO). Trigger on: Freiberufler, Selbständige, EÜR, Anlage S, Homeoffice-Pauschale, Investitionsabzugsbetrag, Vorauszahlungen, German freelancer tax. Out of scope: trade tax (de-trade-tax), investments (de-capital-gains), social contributions (de-social-contributions), partners and part-yea"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/de-einkommensteuer-freelancer"
  jurisdiction: "DE"
  tax_year: "2026"
  last_updated: "2026-10-27"
  authored_by: "Michael Cutajar and the OpenAccountants team"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Income tax for the self-employed in Germany (Einkommensteuer for Freiberufler and Gewerbetreibende)

How Germany taxes the profit of one self-employed person in tax year 2026, the calendar year (§ 2(7) EStG). The tariff applies "ab dem Veranlagungszeitraum 2026" ([§ 32a EStG](https://www.gesetze-im-internet.de/estg/__32a.html)). A short table gives 2025 figures for returns being filed now. This skill is for information and computation only, not tax advice; a Steuerberater must review a real return before it is filed.

## Who this applies to

- **In scope.** One individual resident in Germany with income from self-employed work (§ 18 EStG) or a trade (§ 15 EStG), assessed alone or jointly with a spouse. Tax office: the local Finanzamt; returns go through ELSTER.
- **Freiberufler ([§ 18(1) no. 1 EStG](https://www.gesetze-im-internet.de/estg/__18.html)).** Self-employed scientific, artistic, writing, teaching or educational work, and the named professions (among them doctors, dentists, vets, lawyers, notaries, engineers, architects, auditors, tax advisers, Heilpraktiker, physiotherapists, journalists, interpreters, translators) "und ähnlicher Berufe". Qualified staff are allowed if the owner leads the work and answers for it with their own expertise. § 18(1) no. 3 adds other self-employed work such as executor or supervisory board fees.
- **Trade ([§ 15(2) EStG](https://www.gesetze-im-internet.de/estg/__15.html)).** An independent, lasting activity for profit in general economic life that is not farming, a liberal profession or other self-employed work: what is left over. Whether an unnamed job is "similar" is decided case by case: refer it to a Steuerberater, as is splitting one person's mixed freelance and trade work.
- **The split decides trade tax, registration and the bookkeeping duty, not the tariff.**

| Point | Freiberufler | Trade |
| --- | --- | --- |
| Trade tax | None ([§ 2(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html)) | Above the EUR 24,500 allowance; partly credited (§ 35 EStG). Worked out in `de-trade-tax` |
| Registration within one month (§ 138 AO) | Tax office, start-up details electronically | Municipality, which tells the tax office |
| Bookkeeping duty by size (§ 141 AO) | None | After a limit in the rates table is crossed and the office gives notice |
| Profit form | Anlage S | Anlage G |

- **Out of scope, with the skill to use.** Partnerships (GbR, OHG, KG, Partnerschaftsgesellschaft; a partnership that also trades is a trade as a whole, § 15(3) no. 1 EStG): `de-partners-and-part-year`. Companies (GmbH, UG): `de-corporate-tax`. Wages only: `de-employee-income-tax`. Letting: `de-rental-income`. Legal form: `germany-formation`. VAT returns: `germany-vat-return` and `de-vat-annual-and-special-schemes`. Records, the GWG pool and the car logbook: `germany-bookkeeping`. Contributions: `de-social-contributions`. Prepayment planning: `de-estimated-tax`. Investments: `de-capital-gains`. Crypto: `de-crypto-tax`. Staff: `de-payroll`. Non-residents: `de-non-resident-tax`.
- **Also refer.** Selling or closing the business, extraordinary income (§ 34), retained profits (§ 34a), the progression clause (§ 32b); electric and hybrid business cars and any dispute over private car use; the exact church tax rate and rounding for a client (state rules).

## Rates, bands and thresholds

### The 2026 tariff (§ 32a EStG)

| Zone of taxable income (single) | From | To | Formula ([§ 32a(1) EStG](https://www.gesetze-im-internet.de/estg/__32a.html)) |
| --- | --- | --- | --- |
| 1, basic allowance (Grundfreibetrag) | 0 | EUR 12,348 | tax = 0 |
| 2 | EUR 12,349 | EUR 17,799 | (914.51 * y + 1400) * y |
| 3 | EUR 17,800 | EUR 69,878 | (173.10 * z + 2397) * z + 1034.87 |
| 4 | EUR 69,879 | EUR 277,825 | 0.42 * x - 11135.63 |
| 5 | EUR 277,826 | none | 0.45 * x - 19470.38 |

- **x** is taxable income rounded down to a full euro; **y** is one ten-thousandth of x above the basic allowance; **z** is one ten-thousandth of x above EUR 17,799 (§ 32a(1) sentence 4). Round the tax down to a full euro. The statute prints a decimal comma and a space between thousands.
- **Splitting.** Spouses assessed together pay twice the tax on half their joint taxable income (§ 32a(5)), if both are fully liable to German tax and do not live apart for good ([§ 26 EStG](https://www.gesetze-im-internet.de/estg/__26.html)); registered partners count as spouses (§ 2(8)). § 32a(6) extends it to a widowed person for the year after the death, and to some years in which a marriage ended.
- **Marginal rates** (on the next euro, not the whole income): entry 14%, top 42% from the start of zone 4, highest 45% in zone 5. The 2026 statute prints only the factors 0.42 and 0.45; the 14% entry rate wording comes from the ministry's 2025 tax booklet, whose 2025 zone limits must not be used for 2026.

### All 2026 figures

| Item | Rate or amount | Year | Source |
| --- | --- | --- | --- |
| Basic allowance (Grundfreibetrag), single | EUR 12,348 | 2026 | https://www.gesetze-im-internet.de/estg/__32a.html |
| Top rate zone starts | EUR 69,879 | 2026 | https://www.gesetze-im-internet.de/estg/__32a.html |
| Highest rate zone starts | EUR 277,826 | 2026 | https://www.gesetze-im-internet.de/estg/__32a.html |
| Solidarity surcharge: none unless income tax (single) is more than | EUR 20,350 | 2026 | https://www.gesetze-im-internet.de/solzg_1995/__3.html |
| The same limit under splitting | EUR 40,700 | 2026 | https://www.gesetze-im-internet.de/solzg_1995/__3.html |
| Solidarity surcharge rate, on the income tax | 5.5% | 2026 | https://www.gesetze-im-internet.de/solzg_1995/__4.html |
| Surcharge cap: share of the excess of the tax over the limit | 11.9% | 2026 | https://www.gesetze-im-internet.de/solzg_1995/__4.html |
| Church tax for members, on the income tax, by state | 8% or 9% | 2025 booklet | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9 |
| Trade tax allowance per business (individuals, partnerships) | EUR 24,500 | 2026 | https://www.gesetze-im-internet.de/gewstg/__11.html |
| Bookkeeping duty can start: turnover in the calendar year more than | EUR 800,000 | 2026 | https://www.gesetze-im-internet.de/ao_1977/__141.html |
| Or trade profit in the financial year more than | EUR 80,000 | 2026 | https://www.gesetze-im-internet.de/ao_1977/__141.html |
| Kleinunternehmer: previous year's turnover not above | EUR 25,000 | 2026 | https://www.gesetze-im-internet.de/ustg_1980/__19.html |
| And current year's turnover not above | EUR 100,000 | 2026 | https://www.gesetze-im-internet.de/ustg_1980/__19.html |
| Start-up year: that year's turnover not above (ministry reading) | EUR 25,000 | 2026 | EÜR instructions 2026, line 12 (Sources) |
| Home office that is the centre of all work: yearly flat amount instead of actual costs | EUR 1,260 | 2026 | https://www.gesetze-im-internet.de/estg/__4.html |
| Home office day rate, per calendar day worked mainly at home | EUR 6 | 2026 | https://www.gesetze-im-internet.de/estg/__4.html |
| Yearly cap on day rates | EUR 1,260 | 2026 | https://www.gesetze-im-internet.de/estg/__4.html |
| Home to own premises: per full km one way, per day visited | EUR 0.38 | 2026 | https://www.gesetze-im-internet.de/estg/__9.html |
| Yearly cap on that, not for one's own or a provided car | EUR 4,500 | 2026 | https://www.gesetze-im-internet.de/estg/__9.html |
| Meals in Germany: full 24-hour day away | EUR 28 | 2026 | https://www.gesetze-im-internet.de/estg/__9.html |
| Meals: arrival and departure day with overnight stay, each; or a day over eight hours away without one | EUR 14 | 2026 | https://www.gesetze-im-internet.de/estg/__9.html |
| Meals abroad, example Austria: full day / arrival, departure or over eight hours | EUR 50 / EUR 33 | 2026 | BMF letter of 5 December 2025 (Sources) |
| Business trips in a private car, per full km (or actual cost share) | EUR 0.30 | 2026 | EÜR instructions 2026, line 72 (the highest BRKG rate, § 5(2): https://www.gesetze-im-internet.de/brkg_2005/__5.html) |
| Low-value asset (GWG): expensed in full if cost net of deductible input VAT is not more than | EUR 800 | 2026 | https://www.gesetze-im-internet.de/estg/__6.html |
| Running register needed if a GWG is worth more than | EUR 250 | 2026 | https://www.gesetze-im-internet.de/estg/__6.html |
| Declining balance, movable assets bought 1 July 2025 to 31 December 2027: up to three times straight-line, not more than | 30% | 2026 | https://www.gesetze-im-internet.de/estg/__7.html |
| § 7g investment deduction: share of a future asset's expected cost | 50% | 2026 | https://www.gesetze-im-internet.de/estg/__7g.html |
| § 7g profit limit: profit before the deduction not more than | EUR 200,000 | 2026 | https://www.gesetze-im-internet.de/estg/__7g.html |
| § 7g cap on open deductions (this year and three before), per business | EUR 200,000 | 2026 | https://www.gesetze-im-internet.de/estg/__7g.html |
| § 7g special depreciation over the year bought and four after, in total | 40% | 2026 | https://www.gesetze-im-internet.de/estg/__7g.html |
| "Almost only" business use for § 7g means at least | 90% | 2026 | EÜR instructions 2026, line 89 |
| Writing or journalism as main work: flat expense share of receipts, cap EUR 3,600 | 30% | 2026 | EÜR instructions 2026, line 24 |
| Scientific, artistic or writing side work, side-line teaching and examining: flat share, cap EUR 900 | 25% | 2026 | EÜR instructions 2026, line 24 |
| Pension contributions within the cap deductible | 100% | 2026 | https://www.gesetze-im-internet.de/estg/__10.html |
| Miners' pension insurance ceiling, per year | EUR 124,800 | 2026 | https://www.gesetze-im-internet.de/svbezgrv_2026/__4.html |
| Miners' pension insurance rate | 24.7% | 2026 | https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html |
| Pension contribution cap, single (124,800 x 24.7% = 30,825.60, rounded up) | EUR 30,826 | 2026 | https://www.gesetze-im-internet.de/estg/__10.html |
| Same cap for spouses assessed together | EUR 61,652 | 2026 | https://www.gesetze-im-internet.de/estg/__10.html |
| Statutory health contribution with sick pay claim: cut by | 4% | 2026 | https://www.gesetze-im-internet.de/estg/__10.html |
| Cap for health, care and other insurance together | EUR 2,800 | 2026 | https://www.gesetze-im-internet.de/estg/__10.html |
| Lower cap (KSK insured, employer health share, or cost refunds without own expense) | EUR 1,900 | 2026 | https://www.gesetze-im-internet.de/estg/__10.html |
| Loss carry-back cap, single / joint | EUR 1,000,000 / EUR 2,000,000 | 2026 | https://www.gesetze-im-internet.de/estg/__10d.html |
| Loss carry-forward above EUR 1 million (2 million joint) of total income: share of the excess | 70% for 2024 to 2027; 60% from 2028 | 2026 | https://www.gesetze-im-internet.de/estg/__10d.html ; https://www.recht.bund.de/bgbl/1/2024/108/VO.html |
| Prepayments set only if at least, per year / per due date | EUR 400 / EUR 100 | 2026 | https://www.gesetze-im-internet.de/estg/__37.html |
| Prepayments raised after the year end only if the increase is at least | EUR 5,000 | 2026 | https://www.gesetze-im-internet.de/estg/__37.html |
| § 35 trade tax credit: multiple of the trade tax base amount | 4 times | 2026 | https://www.gesetze-im-internet.de/estg/__35.html |
| Employee side income threshold for a compulsory assessment | EUR 410 | 2026 | https://www.gesetze-im-internet.de/estg/__46.html |

### Surcharge and church tax mechanics

- **A limit with a sliding zone, not an allowance.** Up to the limit, no surcharge. Above it, the lower of 5.5% on the whole tax and 11.9% of the excess. Fractions of a cent are dropped (§ 4 SolzG). The base is the assessed income tax worked out with child allowances; tax under § 32d(3) and (4) EStG is left out of the limit test. § 6(27) SolzG starts these limits in 2026 ([§ 6 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__6.html)). Prepayments carry the surcharge too (§ 3(1) no. 2). Investment income at the flat rate carries its own surcharge: `de-capital-gains`.
- **Church tax.** The state and its church tax rules set the rate and rounding. Its base is the income tax worked out with child allowances in every case and without the § 35 credit ([§ 51a(2) EStG](https://www.gesetze-im-internet.de/estg/__51a.html): "§ 35 ist ... nicht anzuwenden"), so the credit does not lower a trader's church tax. Church tax paid is a special expense (§ 10(1) no. 4 EStG), except on flat-taxed investment income.

### 2025 figures, for returns being filed now

| Item (tax year 2025) | Value | Source |
| --- | --- | --- |
| Basic allowance | EUR 12,096 | Ministry tax booklet 2025 (Sources) |
| Top rate zone starts | EUR 68,481 | Same |
| Surcharge limit, single / splitting | EUR 19,950 / EUR 39,900 | Same |

The 2025 formulas are those of § 32a in its 2025 wording, which the consolidated statute no longer prints; take them from the ELSTER program for 2025.

## The taxable base

### Profit method

For a trade and for self-employed work the taxed income is the profit (§ 2(2) EStG).

| Criterion | EÜR (§ 4(3) EStG) | Balance sheet (§ 4(1), § 5 EStG) |
| --- | --- | --- |
| Who | Anyone not bound by law to keep books who also keeps none. Always open to a Freiberufler | Traders bound to keep books, and anyone who keeps books by choice |
| Profit is | Business receipts less business expenses | The change in business net assets, plus withdrawals, less contributions |
| Timing | Cash basis: receipts when they arrive, expenses when paid ([§ 11 EStG](https://www.gesetze-im-internet.de/estg/__11.html)) | Accruals |
| Sent as | Anlage EÜR with the asset schedule Anlage AVEÜR, electronically ([§ 60(4) EStDV](https://www.gesetze-im-internet.de/estdv_1955/__60.html)) | Balance sheet and P&L, electronically (§ 5b EStG) |

- **Bookkeeping duty for a trade.** Either § 141 AO limit is enough; the duty starts only with the financial year after the office's notice (§ 141(2) AO). Whoever must keep books under another law, such as a merchant under the Commercial Code, must also do so for tax ([§ 140 AO](https://www.gesetze-im-internet.de/ao_1977/__140.html)).
- **Year end.** Regularly recurring receipts and payments made a short time before or after the year end count in the year they belong to (§ 11 EStG).
- **Not pure cash** ([§ 4(3) EStG](https://www.gesetze-im-internet.de/estg/__4.html)). Depreciation and the low-value asset rules apply. Fixed assets that do not wear out, shares, securities, and land and buildings held as current assets count only when sold or withdrawn, and go into a running register. Money collected and paid out in another's name and for their account is left out.
- **Paper EÜR only in hardship cases** (EÜR instructions 2026).
- **Never deductible.** Income tax and other personal taxes ([§ 12 no. 3 EStG](https://www.gesetze-im-internet.de/estg/__12.html)) and trade tax (§ 4(5b) EStG).

### VAT status changes every EÜR figure (§ 19 UStG)

- **Both limits must be met**; a turnover exactly at a limit is still inside. The receipt that crosses a limit in the current year is already taxed normally; earlier receipts stay exempt (EÜR instructions, line 12). Opting out binds for at least five calendar years (§ 19(3) UStG).
- **Kleinunternehmer.** Receipts go on line 12 at the gross amount received. Its sales are exempt, so input VAT is not deductible ([§ 15(2) no. 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__15.html)): every cost counts gross.
- **Normal VAT scheme.** VAT collected and VAT refunded are receipts (form lines 17, 18); deductible input VAT and VAT paid to the office are expenses (lines 58, 59), with the ten-day rule of § 11(2) sentence 2 EStG at the year end.
- **The EUR 800 GWG test** uses cost less deductible input VAT only (§ 6(2) EStG: "vermindert um einen darin enthaltenen Vorsteuerbetrag"), so a Kleinunternehmer tests the gross price. Example: a chair at EUR 952 gross (EUR 800 plus 19% VAT, [§ 12(1) UStG](https://www.gesetze-im-internet.de/ustg_1980/__12.html)) is above EUR 800 for a Kleinunternehmer and must be depreciated or pooled; a business in the normal scheme records EUR 800 and expenses it in full.

### Business expenses (Betriebsausgaben)

Business expenses are the costs caused by the business (§ 4(4) EStG); § 4(5) limits some. Home office room costs, gifts and entertainment must be recorded one by one and apart from other expenses, or the deduction is lost (§ 4(7) EStG).

- **Home office.** Room is the centre of all work: actual costs or the EUR 1,260 flat amount, less one twelfth per full month it is not. Otherwise no room costs, only the EUR 6 day rate (§ 4(5) no. 6c): for a day worked mainly at home without visiting a first place of work (also on a day away if no other workplace is available for good). One day rate per day, and none so far as room costs are deducted.
- **Commuting** to one's own premises uses the employee allowance rules of § 9 EStG through § 4(5) no. 6: EUR 0.38 from the first kilometre, one way, not for flights. For a business car, the costs above the allowance are added back; list-price method and logbook: `germany-bookkeeping`.
- **Meals** on business trips (§ 4(5) no. 5 with § 9(4a)): flat amounts only; nothing for eight hours or less; they stop after three months at one place; abroad, the country amounts in the ministry's letter of 5 December 2025, in force from 1 January 2026.
- **Business trips** are not commuting: every kilometre counts, at EUR 0.30 or the actual cost share.
- **Flat expense shares** for writers, journalists, side-line teachers and examiners replace all actual expenses of that activity. They rest on a ministry letter of 6 April 2023 (BStBl I S. 671) that the 2026 EÜR instructions cite, not on the statute.

### Assets: GWG, depreciation and the Investitionsabzugsbetrag

- **GWG** is tested asset by asset and is a choice. § 6(2a) offers a yearly pool instead (`germany-bookkeeping`). Other assets are depreciated evenly over their useful life, by months in the year bought ([§ 7(1) EStG](https://www.gesetze-im-internet.de/estg/__7.html)), or by the 30% declining balance for movables bought 1 July 2025 to 31 December 2027 (§ 7(2)).
- **§ 7g investment deduction ([§ 7g EStG](https://www.gesetze-im-internet.de/estg/__7g.html)).** Up to 50% of a planned movable asset's expected cost comes off profit in advance. The EUR 200,000 profit limit is a cliff (EUR 200,001 means no deduction that year); the EUR 200,000 cap on open deductions is a different rule with the same number. A deduction may create a loss. Not bought by the end of the third year after: it is undone in the year taken (§ 7g(3)). In the year bought, up to the same share of the real cost is added back (not more than the open deductions) and the cost may be cut by as much (§ 7g(2)). The asset must be let or used only or almost only (at least 90%) in a German establishment until the end of the year after purchase (§ 7g(4)). Special depreciation of up to 40% also needs the profit limit met in the year before purchase (§ 7g(5), (6)).

### From profit to taxable income

The order is set by [§ 2 EStG](https://www.gesetze-im-internet.de/estg/__2.html): income of each type (profit for a business; receipts less Werbungskosten for a job, letting and the rest, [§ 9 EStG](https://www.gesetze-im-internet.de/estg/__9.html)) → total income (§ 2(3)) → less losses, special expenses and extraordinary burdens = income (§ 2(4)) → less child allowances = taxable income (§ 2(5)) → tariff, less reductions such as the § 35 credit = tax to be assessed (§ 2(6)) → less prepayments and tax withheld. The tariff works on taxable income, never on turnover or profit. Flat-taxed investment income stays outside (§ 2(5b); `de-capital-gains`).

### Special expenses: pension and health insurance

Private costs: they do not reduce profit. They come off total income and go on Anlage Vorsorgeaufwand ([§ 10 EStG](https://www.gesetze-im-internet.de/estg/__10.html)).

- **Pension contributions (§ 10(1) no. 2):** statutory insurance, professional schemes with comparable benefits, and a private contract paying only a lifelong monthly annuity not before age 62, with rights not inheritable, transferable, lendable against, saleable or payable as a lump sum. With a job as well, the employer's tax-free share is added before the cap and taken off after.
- **Basic health and care cover is deductible in full**, even above the cap, leaving nothing for other insurance (§ 10(4) sentence 4); for private cover only the statutory-level part counts. Other insurance (no. 3a: unemployment, accident, liability, term life) counts only while the cap has room.
- **Which cap.** Insured through the Künstlersozialkasse (§ 3 no. 57), or with a job and an employer health contribution (no. 62): EUR 1,900. Paying all cover alone with no claim to cover or refunds without own expense: EUR 2,800. Spouses assessed together add their own caps. Contribution rates: `de-social-contributions`.

### Losses (§ 10d EStG)

A loss first offsets other income of the same year; the rest goes back one year, then two, ahead of special expenses (on request carry-back is waived, only as a whole), and then forward without time limit, subject to the 70%/60% rule above EUR 1 million. The office fixes the remaining loss each year end (§ 10d(4)), which triggers a duty to file the next year. Trade tax losses follow § 10a GewStG (`de-trade-tax`).

### Trade tax credit (§ 35 EStG), traders only

Income tax is reduced by four times the trade tax base amount (Messbetrag) set for the same year ([§ 35 EStG](https://www.gesetze-im-internet.de/estg/__35.html)). Two caps: only the part of the tariff tax that falls on trade income (positive trade income over all positive income, times the tax), and never more than the trade tax actually payable. No refund or carry-over of an unused credit. A trade income (rounded down to EUR 100) not above EUR 24,500 pays no trade tax, so gets no credit. The base amount is the trade income less the allowance, times the 3.5% Steuermesszahl ([§ 11(1) and (2) GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html)); Example 3 works it through. The data go on Anlage G.

## Deadlines and filing

- **Registration** within one month of starting ([§ 138(4) AO](https://www.gesetze-im-internet.de/ao_1977/__138.html)).
- **Forms**, as named in ELSTER's instructions for the 2025 return, the latest published: main form ESt 1 A; Anlage S (self-employed work) or Anlage G (trade, including the § 35 data); Anlage EÜR with Anlage AVEÜR, one set per business; Anlage Vorsorgeaufwand; Anlage Sonderausgaben (church tax, donations, own training).
- **Who must file** ([§ 56 EStDV](https://www.gesetze-im-internet.de/estdv_1955/__56.html)): without wages, if total income exceeds the basic allowance (twice it for a joint assessment); also after a loss notice for the year before, and whenever the office asks (§ 149(1) AO).
- **Electronic filing is a duty** with business income ([§ 25(4) EStG](https://www.gesetze-im-internet.de/estg/__25.html)), except in the employee cases of § 46(2) nos. 2 to 8; the office can waive it for hardship.
- **Side income next to a job** ([§ 46 EStG](https://www.gesetze-im-internet.de/estg/__46.html)): an employee must be assessed if income without wage tax is more than EUR 410; if such income is not more than EUR 410 in total it is taken off again. Neither helps someone without wages.

| Deadline | 2026 return | 2025 return | Source |
| --- | --- | --- | --- |
| Without an adviser: seven months after the year | 31 July 2027 is a Saturday, so Monday 2 August 2027 | Friday 31 July 2026: passed, file now | [§ 149(2) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html), [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) |
| With a Steuerberater: last day of February of the second following year | Tuesday 29 February 2028 | 28 February 2027 is a Sunday, so Monday 1 March 2027 | § 149(3) AO |
| Late-filing surcharge becomes compulsory: not filed within 14 months of the year end | After 29 February 2028 | After February 2027; an advised return filed by Monday 1 March 2027 is on time | [§ 152(2) no. 1 AO](https://www.gesetze-im-internet.de/ao_1977/__152.html) |

- **Called in early.** The office may call in a return early with four months' notice (§ 149(4) AO), for example after a late return or a business start or close.
- **Extension** ([§ 109 AO](https://www.gesetze-im-internet.de/ao_1977/__109.html)): possible; for an advised return beyond February only if prevented through no fault of one's own.
- **Pandemic extensions** ended with tax year 2024 ([Art. 97 § 36 EGAO](https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html)); they do not apply to 2025 or 2026.
- **Prepayments (§ 37 EStG).** Due 10 March, 10 June, 10 September and 10 December (§ 37(1)); both minimums must be met. Set by notice, as a rule from the last assessment's tax less tax withheld. The office can adjust them until the end of the 15th calendar month after the year (§ 37(3)); a rise after the year end is added to the last prepayment and due one month after the notice (§ 37(4)). In the first year the office uses the tax it expects, so the profit estimate given at registration matters (`de-estimated-tax`). Example: last assessment EUR 10,548, nothing withheld: EUR 2,637 on each date.
- **Paying the balance.** Due within one month of the notice; the part matching overdue prepayments at once (§ 36(4) EStG).

## Penalties and interest

| Item | Value | Source |
| --- | --- | --- |
| Late-filing surcharge per started month, on assessed tax less prepayments and tax withheld | 0.25% | [§ 152(5) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html) |
| Minimum per started month for a yearly return | EUR 25 | § 152(5) sentence 2 |
| Highest surcharge per return | EUR 25,000 | § 152(10) |
| Interest on a balance or refund, per full month (1.8% a year) | 0.15% | [§ 238(1a) AO](https://www.gesetze-im-internet.de/ao_1977/__238.html) |

- **May or must.** The surcharge may be set for any late return unless the delay is excusable (§ 152(1)). It is compulsory after 14 months (or when a return called in early misses its date, § 152(2) no. 3), unless the deadline was extended, the tax is nil or below, or the tax is not above prepayments plus tax withheld (§ 152(3)); it then stays possible at discretion.
- **Example.** A 2026 return without an adviser filed three months and five days after Monday 2 August 2027, balance EUR 2,000: 0.25% x 2,000 = EUR 5 a month, below the EUR 25 minimum, so 4 started months x EUR 25 = EUR 100, if the office sets one.
- **Interest** starts 15 months after the end of the tax year and runs until the assessment takes effect ([§ 233a(2) AO](https://www.gesetze-im-internet.de/ao_1977/__233a.html)); only full months count.
- **Late payment** of a balance or a prepayment carries the late payment surcharge for each started month ([§ 240 AO](https://www.gesetze-im-internet.de/ao_1977/__240.html)).

## Cross-border points

- This skill assumes full German residence for the whole year. A move to or from Germany in the year: `de-partners-and-part-year`. Non-residents with German freelance income: `de-non-resident-tax`. Treaty withholding: `de-treaty-withholding-rates`. Leaving with large holdings: `leaving-germany-exit-tax`.
- Splitting needs both spouses fully liable to German tax (§ 26 EStG).
- § 7g needs the asset used in a domestic establishment (§ 7g(4)).
- Meals abroad use the country amounts of the BMF letter of 5 December 2025, not the German flat rates.
- Foreign income exempt under a treaty can still raise the rate through § 32b (progression clause): refer.
- Selling to EU clients changes the VAT treatment, not the income tax: `germany-vat-return`.

## Worked examples

**Example 1: translator (Freiberufler), zone 3, home office day rate.** A single translator, EÜR, Kleinunternehmer not used. Receipts EUR 72,000; other business expenses EUR 12,000; 150 days worked mainly at home, no centre-of-work room, so 150 x EUR 6 = EUR 900 day rates (under the EUR 1,260 cap). Profit EUR 59,100. Special expenses (pension and health) EUR 9,100, so taxable income EUR 50,000. Zone 3: z = (50,000 - 17,799) / 10,000 = 3.2201; tax = (173.10 x 3.2201 + 2,397) x 3.2201 + 1,034.87 = 10,548.33, rounded down to EUR 10,548. Below EUR 20,350: no surcharge. Church tax at 9%: EUR 949.32.

```oa-check
name: DE 2026 translator, zone 3, home office day rate
inputs:
  receipts: 72000
  other_expenses: 12000
  home_days: 150
  special_expenses: 9100
steps:
  - day_rates: min(home_days * 6, 1260)
  - profit: receipts - other_expenses - day_rates
  - taxable: floor(profit - special_expenses)
  - z: (taxable - 17799) / 10000
  - tax: floor((173.10 * z + 2397) * z + 1034.87)
  - soli: 0
  - church: tax * 0.09
expected:
  day_rates: 900
  profit: 59100
  taxable: 50000
  tax: 10548
  church: 949.32
```

**Example 2: consultant with an Investitionsabzugsbetrag, surcharge sliding zone.** A single IT consultant plans to buy equipment costing EUR 20,000 next year. Profit before the deduction EUR 100,000, within the EUR 200,000 limit, so 50% x 20,000 = EUR 10,000 comes off: profit EUR 90,000. Special expenses EUR 9,700: taxable income EUR 80,300, zone 4. Tax 0.42 x 80,300 - 11,135.63 = 22,590.37, so EUR 22,590. Surcharge: 5.5% x 22,590 = EUR 1,242.45; cap 11.9% x (22,590 - 20,350) = EUR 266.56; the lower, EUR 266.56, applies. If the equipment is not bought by the end of the third year, the EUR 10,000 is undone in 2026 and interest follows.

```oa-check
name: DE 2026 consultant, § 7g deduction and surcharge sliding zone
inputs:
  profit_before: 100000
  planned_cost: 20000
  special_expenses: 9700
steps:
  - iab: planned_cost * 0.5
  - profit: profit_before - iab
  - taxable: floor(profit - special_expenses)
  - tax: floor(0.42 * taxable - 11135.63)
  - soli_full: tax * 0.055
  - soli_cap: (tax - 20350) * 0.119
  - soli: min(soli_full, soli_cap)
expected:
  iab: 10000
  profit: 90000
  taxable: 80300
  tax: 22590
  soli_full: 1242.45
  soli_cap: 266.56
  soli: 266.56
```

**Example 3: sole trader with the § 35 credit, Hebesatz 400%.** A single online retailer (trade, § 15 EStG). Trade profit EUR 110,000, his only income; special expenses EUR 10,000, so taxable income EUR 100,000, zone 4. Tariff tax 0.42 x 100,000 - 11,135.63 = 30,864.37, so EUR 30,864. Trade tax: trade income EUR 110,000 (already a multiple of EUR 100) less the EUR 24,500 allowance = EUR 85,500; base amount 85,500 x 3.5% = EUR 2,992.50 ([§ 11 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html)); at a 400% Hebesatz the municipality charges EUR 11,970. Credit: 4 x 2,992.50 = EUR 11,970. First cap: all his income is trade income, so the share of tariff tax on it is the full EUR 30,864. Second cap: trade tax payable EUR 11,970. The credit is EUR 11,970 ([§ 35(1) EStG](https://www.gesetze-im-internet.de/estg/__35.html)). Income tax EUR 18,894, below EUR 20,350, so no surcharge. Church tax at 9% is worked out on the tax before the § 35 credit ([§ 51a(2) EStG](https://www.gesetze-im-internet.de/estg/__51a.html)): 9% x 30,864 = EUR 2,777.76. Total income tax plus trade tax EUR 30,864: at a 400% Hebesatz 4 x the base amount equals the trade tax, so the credit absorbs it in full; above 400% the credit stops at 4 x the base amount and the rest of the trade tax is a real cost.

```oa-check
name: DE 2026 sole trader, § 35 trade tax credit at Hebesatz 400%
inputs:
  trade_profit: 110000
  special_expenses: 10000
  hebesatz_pct: 400
steps:
  - taxable: floor(trade_profit - special_expenses)
  - tariff_tax: floor(0.42 * taxable - 11135.63)
  - trade_income: floor(trade_profit / 100) * 100
  - messbetrag: max(0, trade_income - 24500) * 0.035
  - trade_tax: messbetrag * hebesatz_pct / 100
  - cap_share: tariff_tax * trade_profit / trade_profit
  - credit: min(4 * messbetrag, cap_share, trade_tax)
  - income_tax: tariff_tax - credit
  - church: tariff_tax * 0.09
expected:
  taxable: 100000
  tariff_tax: 30864
  messbetrag: 2992.5
  trade_tax: 11970
  credit: 11970
  income_tax: 18894
  church: 2777.76
```

A married couple with the same EUR 100,000 joint taxable income under splitting pays twice the tax on EUR 50,000: 2 x 10,548 = EUR 21,096, against EUR 30,864 for one single person; their EUR 40,700 surcharge limit is not exceeded.

## Ask the client first

- What exactly do you do, and on what qualification? Is a trade registered?
- EÜR or books? Any notice from the tax office to keep books?
- Turnover in 2025 and expected for 2026? Small-business VAT rule (§ 19 UStG) used, or opted out?
- Other income this year: job, pension, rent, investments? Married or registered partner, wanting joint assessment? Children?
- Church member, and which federal state? Health and pension cover: statutory, private, professional scheme, Künstlersozialkasse?
- Prepayments set? A loss carried from earlier years? Is the 2025 return filed, and does a Steuerberater prepare your returns?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| EStG § 2, § 4, § 6, § 7, § 7g, § 9, § 10, § 10d, § 11, § 12, § 15, § 18, § 25, § 26, § 32a, § 35, § 36, § 37, § 46, § 51a | https://www.gesetze-im-internet.de/estg/ | 2026-10-26 |
| EStDV § 56, § 60 | https://www.gesetze-im-internet.de/estdv_1955/ | 2026-10-26 |
| AO § 108, § 109, § 138, § 140, § 141, § 149, § 152, § 233a, § 238, § 240 | https://www.gesetze-im-internet.de/ao_1977/ | 2026-10-26 |
| EGAO Art. 97 § 36 | https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html | 2026-10-24 |
| SolzG § 3, § 4, § 6 | https://www.gesetze-im-internet.de/solzg_1995/ | 2026-10-26 |
| UStG § 12, § 15, § 19 | https://www.gesetze-im-internet.de/ustg_1980/ | 2026-10-24 |
| GewStG § 2, § 11 | https://www.gesetze-im-internet.de/gewstg/ | 2026-10-24 |
| BRKG § 5 | https://www.gesetze-im-internet.de/brkg_2005/__5.html | 2026-10-26 |
| SVBezGrV 2026 § 4 | https://www.gesetze-im-internet.de/svbezgrv_2026/__4.html | 2026-10-24 |
| RVBeitrSBek 2026 | https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html | 2026-10-24 |
| BGBl. 2024 I Nr. 108, Art. 6 (loss share back to 60% from 2028) | https://www.recht.bund.de/bgbl/1/2024/108/VO.html | 2026-10-24 |
| BMF letter of 1 September 2026: Anlage EÜR 2026 and instructions | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2 | 2026-10-26 |
| BMF letter of 5 December 2025: meal and overnight amounts abroad from 1 January 2026 | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Lohnsteuer/2025-12-05-steuerliche-behandlung-reisekosten-2026.pdf?__blob=publicationFile&v=5 | 2026-10-26 |
| BMF, Steuern von A bis Z, 2025 edition | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9 | 2026-10-24 |
| ELSTER help, 2025 income tax return | https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2025 | 2026-10-24 |

Not yet confirmed: the 2026 ELSTER form names (taken from the 2025 instructions); church tax rates and rounding per state (8% or 9% from the 2025 federal booklet, state laws not read); the ministry letter of 6 April 2023 itself (its 30%/EUR 3,600 and 25%/EUR 900 figures are taken from the 2026 EÜR instructions, line 24).

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-27. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `de-einkommensteuer-freelancer` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/de-einkommensteuer-freelancer. If neither is available, confirm every figure against the official source pages cited above before relying on it.
