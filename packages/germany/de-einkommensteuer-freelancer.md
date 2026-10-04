---
name: de-einkommensteuer-freelancer
description: Computes Einkommensteuer for Freiberufler including Betriebsausgaben, Sonderausgaben, and progressive tax brackets.
jurisdiction: DE
tax_year: 2026
last_updated: 2026-09-27
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Income tax for the self-employed in Germany (Einkommensteuer for Freiberufler and Gewerbetreibende)

How Germany taxes the profit of one self-employed person: Freiberufler or trade, the EÜR, the tariff, surcharge and church tax, expenses, special expenses, losses, prepayments, the return, late filing, and how the VAT small-business rule (§ 19 UStG) changes the numbers. Figures are for tax year 2026, the calendar year (§ 2(7) EStG); the tariff applies "ab dem Veranlagungszeitraum 2026" ([§ 32a EStG](https://www.gesetze-im-internet.de/estg/__32a.html)). A short section gives 2025 figures for returns being filed now. The ministry's tax booklet (2025 edition) and ELSTER's 2025 instructions are the latest editions and are labelled where used.

## Scope

- **Covers.** One individual resident in Germany with income from self-employed work (§ 18 EStG) or a trade (§ 15 EStG), assessed alone or jointly with a spouse. Tax office: the local Finanzamt; returns go through ELSTER.
- **Other German Guides.** Start-up checks: `de-freelance-intake`. Trade tax: `de-trade-tax`. Letting: `de-rental-income`. Legal form: `germany-formation`. VAT returns: `germany-vat-return`. Records: `germany-bookkeeping`. Social contributions: `de-social-contributions`. Prepayment planning: `de-estimated-tax`. Investments: `de-capital-gains`. Crypto: `de-crypto-tax`. Staff: `de-payroll`.
- **Not covered.** Partnerships, companies, employees with no business, and the cases under "When to refuse or refer".

## Ask the client first

- What exactly do you do, and on what qualification? Is a trade registered?
- EÜR or books? Any notice from the tax office to keep books?
- Total turnover in 2025 and expected for 2026? Small-business VAT rule (§ 19 UStG) used, or opted out?
- Other income this year: job, pension, rent, investments?
- Married or registered partner, wanting joint assessment? Children?
- Church member? Which federal state?
- Health and pension cover: statutory, private, professional scheme, Künstlersozialkasse?
- Prepayments set? A loss carried from earlier years?
- Is the 2025 return filed? Does a Steuerberater prepare your returns?

## The method, step by step

1. **Type of income:** § 18 or § 15 EStG. Register within one month ([§ 138(4) AO](https://www.gesetze-im-internet.de/ao_1977/__138.html): "innerhalb eines Monats nach dem meldepflichtigen Ereignis").
2. **VAT status:** test both § 19 UStG limits; it decides gross or net recording.
3. **Profit method:** EÜR (§ 4(3) EStG) unless books must be or are kept; for a trade, test § 141 AO and look for a notice.
4. **Profit:** cash-basis receipts less expenses, within § 4(5) EStG, with the § 4(7) records; each asset under § 6(2) or § 7; § 7g within its profit limit.
5. **Send the EÜR**, one per business, electronically ([§ 60(4) EStDV](https://www.gesetze-im-internet.de/estdv_1955/__60.html)).
6. **Taxable income** in the order of § 2 EStG: other income, losses, special expenses, child allowances.
7. **Tariff:** § 32a(1), or splitting under § 32a(5). Round income down to a full euro, then the tax down.
8. **Credit and surcharges:** § 35 credit for a trade; surcharge limit tested on the tax; church tax on the § 51a(2) base, which ignores § 35.
9. **File and pay** by the § 149 AO deadline; pay any balance within one month; diary the § 37 prepayment dates.

## Freiberufler or trade

The split decides trade tax, registration and the bookkeeping duty, not the tariff.

- **Freiberufler ([§ 18(1) no. 1 EStG](https://www.gesetze-im-internet.de/estg/__18.html)).** Self-employed scientific, artistic, writing, teaching or educational work, and the named professions (among them doctors, dentists, vets, lawyers, notaries, engineers, architects, auditors, tax advisers, Heilpraktiker, physiotherapists, journalists, interpreters, translators) "und ähnlicher Berufe". Qualified staff are allowed if the owner leads the work and answers for it with their own expertise. § 18(1) no. 3 adds other self-employed work such as executor or supervisory board fees.
- **Trade ([§ 15(2) EStG](https://www.gesetze-im-internet.de/estg/__15.html)).** An independent, lasting activity for profit in general economic life that is not farming, a liberal profession or other self-employed work: what is left over. Whether an unnamed job is "similar" is decided case by case: refer it.

| Point | Freiberufler | Trade |
| --- | --- | --- |
| Trade tax | None ([§ 2(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html)) | Above the allowance below; partly credited (§ 35 EStG) |
| Registration within one month (§ 138 AO) | Tax office, start-up details electronically | Municipality, which tells the tax office |
| Bookkeeping duty by size (§ 141 AO) | None | After a limit below is crossed and the office gives notice |
| Profit form | Anlage S | Anlage G |

| Trade limits | Value | Source |
| --- | --- | --- |
| Trade tax allowance for individuals and partnerships, per business per year; only the excess is taxed | EUR 24,500 | [§ 11(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html): "Freibetrag in Höhe von 24 500 Euro" |
| Bookkeeping duty can start: total turnover of the business in the calendar year more than | EUR 800,000 | [§ 141(1) no. 1 AO](https://www.gesetze-im-internet.de/ao_1977/__141.html): "von mehr als 800 000 Euro im Kalenderjahr" |
| Or: trade profit in the financial year more than | EUR 80,000 | § 141(1) no. 4 AO: "Gewinn aus Gewerbebetrieb von mehr als 80 000 Euro im Wirtschaftsjahr" |

Either limit is enough. The duty starts only with the financial year after the tax office's notice (§ 141(2) AO). Whoever must keep books under another law, such as a merchant under the Commercial Code, must also do so for tax ([§ 140 AO](https://www.gesetze-im-internet.de/ao_1977/__140.html)). Trade tax itself is worked out in `de-trade-tax`.

## How profit is found

For a trade and for self-employed work the taxed income is the profit (§ 2(2) EStG).

| Criterion | EÜR (§ 4(3) EStG) | Balance sheet (§ 4(1), § 5 EStG) |
| --- | --- | --- |
| Who | Anyone not bound by law to keep books who also keeps none. Always open to a Freiberufler | Traders bound to keep books, and anyone who keeps books by choice |
| Profit is | Business receipts less business expenses | The change in business net assets, plus withdrawals, less contributions |
| Timing | Cash basis: receipts when they arrive, expenses when paid ([§ 11 EStG](https://www.gesetze-im-internet.de/estg/__11.html)) | Accruals |
| Sent as | Anlage EÜR with the asset schedule Anlage AVEÜR, electronically (§ 60(4) EStDV) | Balance sheet and P&L, electronically (§ 5b EStG) |

- **Year end.** Regularly recurring receipts and payments made a short time before or after the year end count in the year they belong to (§ 11 EStG).
- **Not pure cash** ([§ 4(3) EStG](https://www.gesetze-im-internet.de/estg/__4.html)). Depreciation and the low-value asset rules apply. Fixed assets that do not wear out, shares, securities, and land and buildings held as current assets count only when sold or withdrawn, and go into a running register. Money collected and paid out in another's name and for their account is left out.
- **Paper only in hardship cases** ([ministry letter of 1 September 2026 with the 2026 EÜR form and instructions](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2), cited below as "EÜR instructions").
- **Never deductible.** Income tax and other personal taxes ([§ 12 no. 3 EStG](https://www.gesetze-im-internet.de/estg/__12.html)) and trade tax (§ 4(5b) EStG).

## VAT and the income tax figures (§ 19 UStG)

VAT is its own tax (`germany-vat-return`), but the VAT status decides how every amount enters the EÜR.

| What | Value | Source |
| --- | --- | --- |
| Small business (Kleinunternehmer): total turnover of the previous calendar year not above | EUR 25,000 | [§ 19(1) UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html): "im vorangegangenen Kalenderjahr 25 000 Euro nicht überschritten hat" |
| And total turnover of the current calendar year not above | EUR 100,000 | § 19(1) UStG: "im laufenden Kalenderjahr 100 000 Euro nicht überschreitet" |
| Start-up year: turnover of that year not above (the ministry's reading) | EUR 25,000 | EÜR instructions, line 12: "darf der Gesamtumsatz im laufenden Kj. 25.000 € nicht überschreiten" |

- **Both limits must be met**; a turnover exactly at a limit is still inside. The receipt that crosses a limit in the current year is already taxed normally; earlier receipts stay exempt (EÜR instructions, line 12). Opting out binds for at least five calendar years (§ 19(3) UStG).
- **Kleinunternehmer.** Receipts go on line 12 at the gross amount received ("mit dem tatsächlich vereinnahmten Gesamtbetrag"). Its sales are exempt, so input VAT is not deductible ([§ 15(2) no. 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__15.html)): every cost counts gross.
- **Normal VAT scheme.** VAT collected and VAT refunded are receipts (form lines 17, 18); deductible input VAT and VAT paid to the office are expenses (lines 58, 59), with the ten-day rule of § 11(2) sentence 2 EStG at the year end.
- **The EUR 800 low-value test** uses cost less deductible input VAT only ([§ 6(2) EStG](https://www.gesetze-im-internet.de/estg/__6.html): "vermindert um einen darin enthaltenen Vorsteuerbetrag (§ 9b Absatz 1)"), so a Kleinunternehmer tests the gross price.

## From profit to taxable income

The order is set by [§ 2 EStG](https://www.gesetze-im-internet.de/estg/__2.html): income of each type (profit for a business; receipts less expenses for a job, letting and the rest) → total income (Gesamtbetrag der Einkünfte, § 2(3)) → less losses, special expenses and extraordinary burdens = income (Einkommen, § 2(4)) → less child allowances = taxable income (zu versteuerndes Einkommen, § 2(5)) → tariff, less reductions such as the § 35 credit = tax to be assessed (§ 2(6)) → less prepayments and tax withheld. The tariff works on taxable income, never on turnover or profit. Flat-taxed investment income stays outside (§ 2(5b); `de-capital-gains`).

## Figures for tax year 2026

### The tariff (§ 32a EStG)

| Zone of taxable income (single) | From | To | Formula, English notation ([§ 32a(1) EStG](https://www.gesetze-im-internet.de/estg/__32a.html)) |
| --- | --- | --- | --- |
| 1, basic allowance (Grundfreibetrag) | 0 | EUR 12,348 | tax = 0 |
| 2 | EUR 12,349 | EUR 17,799 | (914.51 * y + 1400) * y |
| 3 | EUR 17,800 | EUR 69,878 | (173.10 * z + 2397) * z + 1034.87 |
| 4 | EUR 69,879 | EUR 277,825 | 0.42 * x - 11135.63 |
| 5 | EUR 277,826 | none | 0.45 * x - 19470.38 |

- **x** is taxable income rounded down to a full euro; **y** is one ten-thousandth of x above the basic allowance; **z** is one ten-thousandth of x above EUR 17,799 (§ 32a(1) sentence 4). Round the tax down to a full euro. The statute prints a decimal comma and a space between thousands.
- **Splitting.** Spouses assessed together pay twice the tax on half their joint taxable income (§ 32a(5)), if both are fully liable to German tax and do not live apart for good ([§ 26 EStG](https://www.gesetze-im-internet.de/estg/__26.html)); registered partners count as spouses (§ 2(8)). § 32a(6) extends it to a widowed person for the year after the death, and to some years in which a marriage ended.
- **Outside this Guide:** § 32b (progression clause), § 32d (investment income), § 34 (extraordinary income such as selling the business), § 34a (retained profits).

| Marginal rates (a rate on the next euro, not on the whole income) | Value | Source: [ministry tax booklet, 2025 edition](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9) |
| --- | --- | --- |
| Entry rate, first taxed euro | 14% | "von 14 Pro- zent (Eingangssteuersatz)" |
| Top rate, reached at the start of zone 4 | 42% | "bis auf 42 Prozent (Spitzensteuersatz) an" |
| Highest rate, zone 5 | 45% | "auf dann 45 Prozent (Reichensteuer)" |

The 2026 statute prints only the factors 0.42 and 0.45; the percentages come from the 2025 booklet, whose 2025 zone limits must not be used for 2026.

### Solidarity surcharge and church tax

| What | Value | Source |
| --- | --- | --- |
| No surcharge unless the income tax (single assessment) is more than | EUR 20,350 | [§ 3(3) no. 2 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html): "in anderen Fällen 20 350 Euro übersteigt" |
| The same limit for spouses under splitting | EUR 40,700 | § 3(3) no. 1 SolzG: "Einkommensteuergesetzes 40 700 Euro" |
| Rate, on the income tax and not on the income | 5.5% | [§ 4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html): "beträgt 5,5 Prozent der Bemessungsgrundlage" |
| Cap: not more than this share of the excess of the tax over the limit | 11.9% | § 4 SolzG: "nicht mehr als 11,9 Prozent des Unterschiedsbetrages" |
| Church tax for members, on the income tax | 8% or 9% | [Tax booklet, 2025 edition](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9): "je nach Bundesland 8 oder 9 Prozent" |

- **A limit with a sliding zone, not an allowance.** Up to the limit, no surcharge. Above it, the lower of the full rate on the whole tax and the cap on the excess. Fractions of a cent are dropped (§ 4 SolzG). The base is the assessed income tax worked out with child allowances; tax under § 32d(3) and (4) EStG is left out of the limit test. § 6(27) SolzG starts these limits in 2026 ([§ 6 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__6.html)). Prepayments carry the surcharge too (§ 3(1) no. 2).
- **Church tax.** The state and its church tax rules set the rate and rounding. Its base is the income tax worked out with child allowances in every case and without the § 35 credit ([§ 51a(2) EStG](https://www.gesetze-im-internet.de/estg/__51a.html): "§ 35 ist ... nicht anzuwenden"), so the credit does not lower a trader's church tax. Church tax paid is a special expense (§ 10(1) no. 4 EStG), except on flat-taxed investment income.

### Business expenses a freelancer meets

Business expenses are the costs caused by the business (§ 4(4) EStG); § 4(5) limits some. Home office room costs, gifts and entertainment must be recorded one by one and apart from other expenses, or the deduction is lost (§ 4(7) EStG).

| What | Value | Source |
| --- | --- | --- |
| Home office room that is the centre of all work: yearly flat amount instead of actual costs | EUR 1,260 | [§ 4(5) no. 6b EStG](https://www.gesetze-im-internet.de/estg/__4.html): "pauschal ein Betrag von 1 260 Euro (Jahrespauschale)" |
| Day rate for each calendar day worked mainly at home | EUR 6 | § 4(5) no. 6c: "ein Betrag von 6 Euro (Tagespauschale)" |
| Yearly cap on day rates | EUR 1,260 | § 4(5) no. 6c: "höchstens 1 260 Euro im Wirtschafts- oder Kalenderjahr" |
| Home to own premises: per full km one way, per day visited | EUR 0.38 | [§ 9(1) sentence 3 no. 4 EStG](https://www.gesetze-im-internet.de/estg/__9.html): "von 0,38 Euro anzusetzen" |
| Yearly cap, not for trips in one's own or a provided car | EUR 4,500 | Same sentence: "höchstens jedoch 4 500 Euro im Kalenderjahr" |
| Meals in Germany: full day of 24 hours away | EUR 28 | § 9(4a) no. 1: "28 Euro für jeden Kalendertag" |
| Meals: arrival and departure day of a trip with overnight stay, each | EUR 14 | § 9(4a) no. 2: "jeweils 14 Euro für den An- und Abreisetag" |
| Meals: day without overnight stay, more than eight hours away | EUR 14 | § 9(4a) no. 3: "14 Euro für den Kalendertag, an dem der Arbeitnehmer ohne Übernachtung" |
| Business trips in a private car: per full km (or the actual cost share) | EUR 0.30 | EÜR instructions, lines 69-74: "pauschal mit 0,30 € für jeden vollen km" |

- **Home office.** Room is the centre: actual costs or the flat amount, less one twelfth per full month it is not. Otherwise no room costs, only the day rate: for a day worked mainly at home without visiting a first place of work (also on a day away if no other workplace is available for good). One day rate per day, and none so far as room costs are deducted.
- **Commuting** to one's own premises uses the employee allowance (§ 4(5) no. 6): one rate from the first kilometre, one-way, not for flights. For a business car, the costs above the allowance are added back (sentence 3); list-price method and logbook: `germany-bookkeeping`.
- **Meals** on business trips (§ 4(5) no. 5): flat amounts only; nothing for eight hours or less; they stop after three months at one place; abroad, the ministry's country amounts.
- **Business trips** are not commuting: every kilometre counts. The per-km flat rate rests on the instructions; it matches the higher car rate of [§ 5(2) BRKG](https://www.gesetze-im-internet.de/brkg_2005/__5.html).

| Assets | Value | Source |
| --- | --- | --- |
| Low-value asset (GWG), movable, wearing out, usable alone: expensed in full if cost net of deductible input VAT is not more than | EUR 800 | [§ 6(2) EStG](https://www.gesetze-im-internet.de/estg/__6.html): "für das einzelne Wirtschaftsgut 800 Euro nicht übersteigen" |
| Running register needed if its value is more than | EUR 250 | § 6(2) sentence 4: "deren Wert 250 Euro übersteigt" |
| Declining balance, movable assets bought 1 July 2025 to 31 December 2027: at most three times the straight-line rate and not more than | 30% | [§ 7(2) EStG](https://www.gesetze-im-internet.de/estg/__7.html): "30 Prozent nicht übersteigen" |
| § 7g investment deduction: share of a future movable asset's expected cost taken off profit in advance | 50% | [§ 7g(1) EStG](https://www.gesetze-im-internet.de/estg/__7g.html): "bis zu 50 Prozent der voraussichtlichen Anschaffungs- oder Herstellungskosten" |
| § 7g profit limit: the year's profit before the deduction not more than | EUR 200,000 | § 7g(1) sentence 2 no. 1: "200 000 Euro nicht überschreitet" |
| § 7g cap on open deductions of the year and three years before, per business | EUR 200,000 | § 7g(1) sentence 4: "darf je Betrieb 200 000 Euro nicht übersteigen" |
| § 7g special depreciation, in total over the year bought and four after | 40% | § 7g(5): "Sonderabschreibungen bis zu insgesamt 40 Prozent" |
| "Almost only" business use for § 7g means at least | 90% | EÜR instructions, line 89: "fast ausschließlich (mindestens 90 %)" |
| Writing or journalism as main work: flat share of receipts instead of actual expenses | 30% | EÜR instructions 2026, line 24: "pauschal 30 % der Betriebseinnahmen, maximal 3.600 € jährlich" |
| Yearly cap on that flat amount | EUR 3,600 | Same sentence |
| Scientific, artistic or writing side work, side-line teaching and examining: flat share | 25% | Line 24: "pauschal 25 % der Betriebseinnahmen, maxi- mal 900 € jährlich" |
| Yearly cap on that flat amount | EUR 900 | Same sentence |

- **GWG** is tested asset by asset and is a choice. § 6(2a) offers a yearly pool instead (`germany-bookkeeping`). Other assets are depreciated evenly over their useful life, by months in the year bought (§ 7(1)).
- **§ 7g.** The profit limit is a cliff; the cap is a different rule with the same number. Not bought by the end of the third year after the deduction: it is undone in the year taken (§ 7g(3)). In the year bought, up to the same share of the real cost is added back (not more than the open deductions) and the cost may be cut by as much (§ 7g(2)). The asset must be let or used only or almost only in a German establishment until the end of the year after purchase (§ 7g(4)); special depreciation also needs the profit limit met in the year before purchase (§ 7g(6)). A deduction may create a loss.
- **Flat shares** replace all actual expenses of that activity. They rest on a ministry letter of 6 April 2023 that the instructions cite, not on the statute.

### Special expenses: pension and health insurance

Private costs: they do not reduce profit. They are taken off the total income and go on Anlage Vorsorgeaufwand.

| What | Value | Source |
| --- | --- | --- |
| Share of pension contributions within the cap that is deductible, from 2023 | 100% | [§ 10(3) sentence 6 EStG](https://www.gesetze-im-internet.de/estg/__10.html): "ab dem Kalenderjahr 2023 beträgt er 100 Prozent" |
| 2026 miners' pension insurance contribution ceiling, per year | EUR 124,800 | [§ 4(1) no. 2 SVBezGrV 2026](https://www.gesetze-im-internet.de/svbezgrv_2026/__4.html): "auf 124 800 Euro jährlich" |
| 2026 miners' pension insurance contribution rate | 24.7% | [RVBeitrSBek 2026](https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html): "in der knappschaftlichen Rentenversicherung 24,7 Prozent" |
| 2026 cap on pension contributions, single: ceiling x rate = 30,825.60, rounded up to a full euro | EUR 30,826 | § 10(3) sentence 1 EStG: "Höchstbeitrag zur knappschaftlichen Rentenversicherung, aufgerundet auf einen vollen Betrag in Euro" |
| 2026 cap for spouses assessed together, doubled | EUR 61,652 | § 10(3) sentence 2: "verdoppelt sich der Höchstbetrag" |
| Statutory health insurance with a claim to sick pay: contribution cut by this share | 4% | § 10(1) no. 3(a): "ist der jeweilige Beitrag um 4 Prozent zu vermindern" |
| Yearly cap for health, care and other insurance together | EUR 2,800 | § 10(4) sentence 1: "insgesamt bis 2 800 Euro abgezogen werden" |
| Lower cap where a claim to refund of sickness costs exists wholly or partly without own expense, or tax-free § 3 no. 9, 14, 57 or 62 payments are made | EUR 1,900 | § 10(4) sentence 2: "Der Höchstbetrag beträgt 1 900 Euro" |

- **Pension contributions (§ 10(1) no. 2):** statutory insurance, professional schemes with comparable benefits, and a private contract paying only a lifelong monthly annuity not before age 62, with rights not inheritable, transferable, lendable against, saleable or payable as a lump sum. With a job as well, the employer's tax-free share is added before the cap and taken off after.
- **Basic health and care cover is deductible in full**, even above the cap, leaving nothing for other insurance (§ 10(4) sentence 4); for private cover only the statutory-level part counts. Other insurance (no. 3a: unemployment, accident, liability, term life) counts only while the cap has room.
- **Which cap.** Insured through the Künstlersozialkasse (§ 3 no. 57), or with a job and an employer health contribution (no. 62): the lower cap. Paying all cover alone with no claim to cover or refunds without own expense: the higher cap. Spouses assessed together add their own caps. Contribution rates: `de-social-contributions`.

### Losses (§ 10d EStG)

| What | Value | Source |
| --- | --- | --- |
| Carry-back cap, single assessment | EUR 1,000,000 | [§ 10d(1) EStG](https://www.gesetze-im-internet.de/estg/__10d.html): "bis zu einem Betrag von 1 000 000 Euro" |
| Carry-back cap, spouses assessed together | EUR 2,000,000 | § 10d(1): "2 000 000 Euro" |
| Carry-forward: above a total income of 1 million euro (2 million for spouses assessed together) losses are deducted only up to this share of the excess | 70% | § 10d(2): "bis zu 70 Prozent des 1 Million Euro übersteigenden Gesamtbetrags der Einkünfte" |

A loss first offsets other income of the same year; the rest goes back one year, then two, ahead of special expenses (on request carry-back is waived, only as a whole), and then forward without time limit. The office fixes the remaining loss each year end (§ 10d(4)), which triggers a duty to file the next year. Trade tax losses follow § 10a GewStG (`de-trade-tax`).

### Prepayments (Vorauszahlungen, § 37 EStG)

| What | Value | Source |
| --- | --- | --- |
| Prepayments are set only if they are at least this much in the calendar year | EUR 400 | [§ 37(5) EStG](https://www.gesetze-im-internet.de/estg/__37.html): "mindestens 400 Euro im Kalenderjahr" |
| And at least this much for one due date | EUR 100 | § 37(5): "mindestens 100 Euro für einen Vorauszahlungszeitpunkt" |
| After the year ends, prepayments are raised only if the increase is at least | EUR 5,000 | § 37(5) sentence 2: "auf mindestens 5 000 Euro beläuft" |

- **Due** 10 March, 10 June, 10 September and 10 December (§ 37(1)); both minimums must be met.
- **Amount.** Set by notice, as a rule from the last assessment's tax less tax withheld. The office can adjust them to the expected tax until the end of the 15th calendar month after the year (§ 37(3)); a rise after the year end is added to the last prepayment and due one month after the notice (§ 37(4)). In the first year the office uses the tax it expects, so the profit estimate given at registration matters (`de-estimated-tax`).
- **A late prepayment** carries the late payment surcharge ([§ 240 AO](https://www.gesetze-im-internet.de/ao_1977/__240.html)).

### Trade tax credit (§ 35 EStG), traders only

Income tax is reduced by four times the trade tax base amount (Messbetrag) set for the same year ([§ 35 EStG](https://www.gesetze-im-internet.de/estg/__35.html): "das Vierfache"). Two caps: only the part of the tariff tax that falls on trade income (positive trade income divided by all positive income, times the tax), and never more than the trade tax actually payable. No refund or carry-over of an unused credit. The data go on Anlage G.

### 2025 figures, for returns being filed now

| What (tax year 2025) | Value | Source |
| --- | --- | --- |
| Basic allowance | EUR 12,096 | [Tax booklet, 2025 edition](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9): "Grundfreibetrag in Höhe von 12.096 Euro (2025)" |
| Top rate zone starts at | EUR 68,481 | Booklet: "Ab 68.481 Euro (2024: 66.761 Euro)" |
| Solidarity surcharge limit, single | EUR 19,950 | Booklet: "Einkommensteuer nicht mehr als 19.950 Euro" |
| The same under splitting | EUR 39,900 | Booklet: "nicht mehr als 39.900 Euro" |

The 2025 formulas are those of § 32a in its 2025 wording, which the consolidated statute no longer prints; take them from the ELSTER program for 2025. Deadlines for 2025 are under "Filing and payment".

## Boundaries and exceptions

| Situation | Result | Source |
| --- | --- | --- |
| Taxable income exactly EUR 12,348 (single) | Zone 1: no tax. Zone 2 starts at the next euro | [§ 32a EStG](https://www.gesetze-im-internet.de/estg/__32a.html) |
| Income tax exactly EUR 20,350 (single) | No surcharge: the limit must be exceeded | [§ 3(3) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html) |
| Profit before § 7g deduction EUR 200,001 | No investment deduction at all for that year (cliff) | [§ 7g(1) EStG](https://www.gesetze-im-internet.de/estg/__7g.html) |
| Previous-year turnover exactly EUR 25,000 | Still a Kleinunternehmer if the current year stays within EUR 100,000 | [§ 19(1) UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html) |
| Trade income (Gewerbeertrag, rounded down to EUR 100) not above EUR 24,500 | No trade tax, so no § 35 credit | [§ 11(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html) |
| Assessed tax not above prepayments plus tax withheld | Surcharge not compulsory even after 14 months; still possible at discretion | [§ 152(3) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html) |

## Worked cases

2026, single unless stated; taxable income is an assumption after all deductions; church tax rounding follows state rules.

1. **Translator, zone 3** ([§ 32a EStG](https://www.gesetze-im-internet.de/estg/__32a.html)). Taxable income EUR 50,000. z = (50,000 - 17,799) / 10,000 = 3.2201. Tax = (173.10 x 3.2201 + 2,397) x 3.2201 + 1,034.87 = 10,548.33, rounded down to EUR 10,548. Below EUR 20,350: no surcharge ([§ 3(3) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html)). Church tax at 9%: EUR 949.32.
2. **Consultant in the sliding zone** ([§ 4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html)). Taxable income EUR 80,300, zone 4: 0.42 x 80,300 - 11,135.63 = 22,590.37, so tax EUR 22,590. Surcharge: full rate 5.5% x 22,590 = EUR 1,242.45; cap 11.9% x (22,590 - 20,350) = EUR 266.56; the lower, EUR 266.56, applies.
3. **Trader with the § 35 credit** ([§ 35 EStG](https://www.gesetze-im-internet.de/estg/__35.html)). Trade profit EUR 110,000, the only income; taxable income EUR 100,000; assumed trade tax multiplier (Hebesatz) 400%. Tariff tax 0.42 x 100,000 - 11,135.63 = 30,864.37, so EUR 30,864. Trade tax base amount (110,000 - 24,500) x 3.5% = EUR 2,992.50 ([§ 11 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html)); trade tax at 400% = EUR 11,970 (details in `de-trade-tax`). Credit 4 x 2,992.50 = EUR 11,970, within both caps. Income tax EUR 18,894: below EUR 20,350, so no surcharge. Church tax (9%) is on EUR 30,864, not on EUR 18,894: EUR 2,777.76 ([§ 51a(2) EStG](https://www.gesetze-im-internet.de/estg/__51a.html)).
4. **Married couple, splitting** ([§ 32a(5) EStG](https://www.gesetze-im-internet.de/estg/__32a.html)). Joint taxable income EUR 100,000. Tax on half, EUR 50,000, is EUR 10,548 (case 1); doubled, EUR 21,096. The couple's limit of EUR 40,700 is not exceeded, so no surcharge. One person alone with EUR 100,000 would pay EUR 30,864.
5. **Prepayments** ([§ 37 EStG](https://www.gesetze-im-internet.de/estg/__37.html)). Last assessment: income tax EUR 10,548, nothing withheld. Prepayments EUR 2,637 on each of the four dates, above both minimums (EUR 400 a year, EUR 100 a date).
6. **Kleinunternehmer buying a chair** ([§ 6(2) EStG](https://www.gesetze-im-internet.de/estg/__6.html)). 2025 turnover EUR 22,000, 2026 expected EUR 24,000: both § 19 limits met. An office chair costs EUR 952 gross (EUR 800 plus 19% VAT, [§ 12(1) UStG](https://www.gesetze-im-internet.de/ustg_1980/__12.html)). No input VAT is deductible, so the cost is EUR 952: above EUR 800, it is depreciated over its useful life or pooled. A business in the normal VAT scheme would record EUR 800 and could expense it in full.
7. **Late 2026 return** ([§ 152 AO](https://www.gesetze-im-internet.de/ao_1977/__152.html)). No adviser; filed three months and five days after Monday 2 August 2027. Tax less prepayments and tax withheld EUR 2,000. 0.25% x 2,000 = EUR 5 a month, below the EUR 25 minimum, so 4 started months x EUR 25 = EUR 100, if the office sets one (it may; it is not yet compulsory, as 14 months have not passed).

## When to refuse or refer

- Partnerships (GbR, OHG, KG, Partnerschaftsgesellschaft) and companies (GmbH, UG); a partnership that also trades is a trade as a whole (§ 15(3) no. 1 EStG). People with wages only.
- Whether an unnamed job is a "similar profession", and splitting one person's mixed freelance and trade work: refer to a Steuerberater.
- Cross-border cases: living or working abroad, foreign tax, treaties, moving to or from Germany in the year.
- Selling or closing the business, extraordinary income (§ 34), retained profits (§ 34a), the progression clause (§ 32b).
- Electric and hybrid business cars, and any dispute over private use of a car.
- The exact church tax rate and rounding for a client: state rules, not on the federal pages.
- A final liability for a real client: the worked cases show the method; a professional must check the full return.
- Trade tax: `de-trade-tax`. Rentals: `de-rental-income`. Choosing a legal form: `germany-formation`. VAT returns: `germany-vat-return`.

## Filing and payment

**Forms**, as named in ELSTER's instructions for the 2025 return, the latest published ([ELSTER help, 2025 return](https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2025)): main form ESt 1 A; Anlage S (self-employed work) or Anlage G (trade, including the § 35 data); Anlage EÜR with Anlage AVEÜR, one set per business; Anlage Vorsorgeaufwand (insurance); Anlage Sonderausgaben (church tax, donations, own training).

- **Who must file** ([§ 56 EStDV](https://www.gesetze-im-internet.de/estdv_1955/__56.html)): without wages, if total income exceeds the basic allowance (twice it for a joint assessment); also after a loss notice for the year before, and whenever the office asks (§ 149(1) AO).
- **Electronic filing is a duty** with business income ([§ 25(4) EStG](https://www.gesetze-im-internet.de/estg/__25.html)), except in the employee cases of § 46(2) nos. 2 to 8; the office can waive it for hardship.
- **Side income next to a job** ([§ 46 EStG](https://www.gesetze-im-internet.de/estg/__46.html)): an employee must be assessed if income without wage tax is more than EUR 410 ("jeweils mehr als 410 Euro"); if such income is not more than EUR 410 in total it is taken off again ("insgesamt nicht mehr als 410 Euro"). Neither helps someone without wages.

| Deadline | 2026 return | 2025 return | Source |
| --- | --- | --- | --- |
| Without an adviser: seven months after the year | 31 July 2027 is a Saturday, so Monday 2 August 2027 | Friday 31 July 2026: passed, file now | [§ 149(2) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html), [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) |
| With a Steuerberater: last day of February of the second following year | Tuesday 29 February 2028 | 28 February 2027 is a Sunday, so Monday 1 March 2027 | § 149(3) AO |
| Late-filing surcharge becomes compulsory: not filed within 14 months of the year end | After 29 February 2028 | After February 2027; an advised return filed by Monday 1 March 2027 is on time | [§ 152(2) no. 1 AO](https://www.gesetze-im-internet.de/ao_1977/__152.html) |

- **One rule for every return.** The 14-month rule applies advised or not, so for an advised return it bites the day after the advised deadline unless that was extended; also when a return called in early (§ 149(4) AO, four months' notice, e.g. after a late return or a business start or close) misses its date (§ 152(2) no. 3).
- **Extension** ([§ 109 AO](https://www.gesetze-im-internet.de/ao_1977/__109.html)): possible; for an advised return beyond February only if prevented through no fault of one's own.
- **Pandemic extensions** ended with tax year 2024 ([Art. 97 § 36 EGAO](https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html)); they do not apply to 2025 or 2026.

| Late return and interest | Value | Source |
| --- | --- | --- |
| Surcharge per started month of delay, on the assessed tax less prepayments and tax withheld | 0.25% | [§ 152(5) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html): "0,25 Prozent der um die festgesetzten Vorauszahlungen" |
| Minimum per started month for a yearly return | EUR 25 | § 152(5) sentence 2: "mindestens jedoch 25 Euro" |
| Highest surcharge per return | EUR 25,000 | § 152(10): "höchstens 25 000 Euro betragen" |
| Interest on a balance or refund after assessment, per full month | 0.15% | [§ 238(1a) AO](https://www.gesetze-im-internet.de/ao_1977/__238.html): "0,15 Prozent für jeden Monat" |
| The same per year | 1.8% | § 238(1a): "1,8 Prozent für jedes Jahr" |

- **May or must.** The surcharge may be set for any late return unless the delay is excusable (§ 152(1)). It is not compulsory if the deadline was extended, the tax is nil or below, or the tax is not above prepayments plus tax withheld (§ 152(3)).
- **Interest** starts 15 months after the end of the tax year and runs until the assessment takes effect ([§ 233a(2) AO](https://www.gesetze-im-internet.de/ao_1977/__233a.html)); only full months count.
- **Paying.** The balance is due within one month of the notice; the part matching overdue prepayments at once (§ 36(4) EStG). Late tax carries the late payment surcharge for each started month (§ 240 AO).

## Completion checklist

- Income type settled (§ 18 or § 15) and registration within one month done.
- VAT status tested against both § 19 limits; EÜR entries gross or net to match.
- EÜR complete: one per business, AVEÜR attached, § 4(7) records kept, low-value assets and depreciation right, § 7g within the profit limit.
- Special expenses within the 2026 caps; the right health cap chosen.
- Loss notice and carry-back choice checked.
- Tariff zone and rounding checked; splitting only if § 26 is met; surcharge limit tested on the tax; church tax base ignores § 35.
- Return filed electronically by Monday 2 August 2027 (advised: Tuesday 29 February 2028); the 2025 return is already due without an adviser.
- Prepayment notice checked and the four dates diaried.

## Disclaimer

This Guide and its outputs are for information and computation only and are not tax, legal or financial advice. Open Accountants accepts no liability for errors, omissions or outcomes from its use. A qualified professional (such as a Steuerberater) must review all outputs before anything is filed or acted on.

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
